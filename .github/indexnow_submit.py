#!/usr/bin/env python3
"""Submit sitemap URLs to IndexNow using the key file already at the repo root."""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

HOST = "rustonroad.github.io"
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
INDEXNOW_URL = "https://api.indexnow.org/indexnow"


def existing_key_file():
    found = []
    for path in Path(".").glob("*.txt"):
        stem = path.stem
        if len(stem) == 32 and all(c in "0123456789abcdef" for c in stem):
            if path.read_text(encoding="utf-8").strip() == stem:
                found.append(path)
    if len(found) != 1:
        sys.exit(f"expected one root IndexNow key file, found {len(found)}")
    return found[0]


def sitemap_entries():
    root = ET.parse("sitemap.xml").getroot()
    entries = []
    for node in root.findall("sm:url", SITEMAP_NS):
        loc = node.find("sm:loc", SITEMAP_NS)
        lastmod = node.find("sm:lastmod", SITEMAP_NS)
        if loc is None or not loc.text:
            continue
        entries.append(
            (
                loc.text.strip(),
                lastmod.text.strip() if lastmod is not None and lastmod.text else "",
            )
        )
    return entries


def paths_for(loc):
    path = loc.split("://", 1)[-1]
    path = path.split("/", 1)[1] if "/" in path else ""
    if path in ("", "/"):
        return ["index.html"]
    if path.endswith("/"):
        return [path + "index.html", path.rstrip("/")]
    return [path]


def changed_files():
    before = os.environ.get("BEFORE_SHA", "")
    sha = os.environ.get("GITHUB_SHA", "HEAD")
    if not before or set(before) == {"0"} or before == sha:
        return set()
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", before, sha],
            text=True,
        )
    except subprocess.CalledProcessError:
        return set()
    return {line.strip() for line in out.splitlines() if line.strip()}


def choose_urls(entries, key):
    key_suffix = f"/{key}.txt"
    blocked = []
    usable = []
    for loc, lastmod in entries:
        if loc.rstrip("/").endswith(key_suffix) or loc.endswith(key_suffix):
            blocked.append(loc)
            continue
        usable.append((loc, lastmod))
    if blocked:
        sys.exit("sitemap lists the IndexNow key file")

    changed = changed_files()
    changed_urls = [
        loc for loc, _last in usable if any(path in changed for path in paths_for(loc))
    ]
    cutoff = (date.today() - timedelta(days=7)).isoformat()
    recent = [loc for loc, lastmod in usable if lastmod and lastmod >= cutoff]
    if changed_urls:
        return changed_urls, "changed in this push"
    if recent:
        return recent, "lastmod within 7 days"
    return [], "none"


def key_is_live(key):
    url = f"https://{HOST}/{key}.txt"
    request = urllib.request.Request(url, headers={"Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8").strip()
        return response.status, body == key


def submit(key, urls):
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": f"https://{HOST}/{key}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        INDEXNOW_URL,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", "replace")
            return response.status, body
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        return error.code, body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    key_path = existing_key_file()
    key = key_path.stem
    urls, mode = choose_urls(sitemap_entries(), key)
    print("indexnow key file: existing root file")
    print(f"indexnow mode: {mode}")
    print(f"indexnow url count: {len(urls)}")
    if args.dry_run:
        return 0
    if not urls:
        print("INDEXNOW_HTTP_STATUS=skipped")
        return 0

    status, matches = key_is_live(key)
    print(f"key file check status {status}")
    if status != 200 or not matches:
        print("INDEXNOW_HTTP_STATUS=key_not_ready")
        return 1

    code, body = submit(key, urls)
    print(f"INDEXNOW_HTTP_STATUS={code}")
    if body.strip():
        print(body.strip())
    if code not in (200, 202):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
