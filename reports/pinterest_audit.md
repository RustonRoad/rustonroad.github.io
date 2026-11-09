# Pinterest SEO & Compliance Audit

**Account:** [@rustonroad](https://www.pinterest.com/rustonroad/) (RustONroaD)
**Audit date:** 2026-11-09 20:20 UTC
**Overall SEO score:** **67/100**

## Method & limits

- **Playwright MCP / Chromium CDP `http://127.0.0.1:9222`:** not available in this Cloud Agent environment (no Playwright MCP namespace; CDP port closed on the VM). A logged-in Business Manager session could not be attached.
- **Fallback:** public Apify scrapes of the RustONroaD profile, first page of boards (10 of 73), and the 10 most recent pins with close-up detail.
- **Amazon affiliate links:** destination URLs were parsed for Associate tags only. Tagged Amazon URLs were **not** HTTP-fetched or clicked (tags `mantasdaunora-21`, `rustonroadsf-21`, `rustonroadweb-21`).

## Profile

| Field | Value |
|---|---|
| Display name | Motorcycle Gear UK RustONroaD Biker Style |
| Username | rustonroad |
| Followers / following | 195 / 38 |
| Pins / boards | 3,336 / 73 |
| Account | Partner (`isPartner=true`) |
| Website | `http://www.amazon.co.uk/shop/influencer-fc0610a5` (Amazon Storefront) |
| Domain verified | **false** |
| Verified merchant | **false** |
| Bio | Motorcycle gear and biker style for riders in the UK and around the world. Leather jackets, boots, helmets, gloves and winter kit, plus chopper and cafe racer ideas. Shop my picks on my Amazon Storefront. As an Amazon Associate I earn from qualifying purchases. |

### Suggested profile rewrites

- **Display name:** `RustONroaD | Motorcycle Gear UK`
- **Bio:** `RustONroaD | women's motorcycle jackets, boots, helmets, gloves and winter kit for UK riders. Shop the Amazon UK Storefront. As an Amazon Associate I earn from qualifying purchases.`
- **Website claim:** add and verify `https://rustonroad.github.io/` (keep Storefront in bio / lnk.bio). Confirm Amazon Storefront remains claimed in Business Hub.

## Public boards (sample: 10 of 73)

| Board | Pins | Description status | Notes |
|---|---:|---|---|
| Mustang Builds & Muscle Cars | 9 | OK | no Amazon/affiliate mention; long |
| Ebony Biker Outfits & Leather Looks UK | 18 | OK | no Amazon/affiliate mention |
| MK3 Golf VR6 Stance VW Underground Euro Culture | 68 | OK | no Amazon/affiliate mention; contains dash punctuation; long |
| Matte Black Motorcycle Gear | 11 | OK | keyworded |
| Women's Leather Motorcycle Jackets | 97 | OK | keyworded |
| Women's Biker Outfit Ideas | 34 | OK | keyworded |
| Cafe Racer Style for Women | 574 | OK | keyworded |
| Premium Motorcycle Gear | 27 | OK | keyworded |
| Motorcycle Gloves UK: Leather & Winter | 6 | OK | no Amazon/affiliate mention |
| Men's Leather Motorcycle Jackets UK | 37 | OK | keyworded |
| Women's Motorcycle Boots | (seen via pins) | OK | Motorcycle boots for women. Lace up, knee high and waterproof biker boots, plus … |

### Board rewrite examples

- **Women's Leather Motorcycle Jackets:** `Women's motorcycle jackets for UK riders: leather, textile and armoured styles with CE notes where listed. Picks link to Amazon UK. Contains affiliate links.`
- **Mustang / MK3 Golf boards:** either niche them clearly away from gear SEO or add a one-line intent note so the bot does not treat them as primary gear boards.
- **Prompt rule:** every new/edited board description must include product keywords + UK + `Contains affiliate links.` and must not be blank.

## 10 most recent Pins

| # | Title (len) | Desc len | Alt | Board | Image | Destination tag | Flags |
|---:|---|---:|---|---|---|---|---|
| 1 | Zorax Full Face Motorcycle Helmet, Matt Black with Extra Dar… (84) | 274 | generic | Matte Black Motorcycle Gear | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start |
| 2 | Brown Leather Biker Jacket for Women, Vintage Rider Style (57) | 265 | DUP/desc | Women's Leather Motorcycle Jackets | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; alt text missing or copied from description |
| 3 | Matte Black Open Face Jet Helmet with Visor, Similar Style R… (69) | 257 | generic | Matte Black Motorcycle Gear | 720x1080 | `mantasdaunora-21` | #ad at end, not near start; 2:3 ok but 720x1080 (prefer 1000x1500) |
| 4 | Black Leather Motorcycle Jacket for Men, Winter Ride Look, S… (72) | 273 | generic | Men's Leather Motorcycle Jackets UK | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start |
| 5 | Quilted Leather Biker Jacket for Women with Cross Zip, Simil… (80) | 249 | DUP/desc | Women's Leather Motorcycle Jackets | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; alt text missing or copied from description |
| 6 | Black Lambskin Leather Biker Jacket for Women, Quilted Shoul… (79) | 259 | generic | Ebony Biker Outfits & Leather Looks UK | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; generic alt text |
| 7 | Black Studded Biker Jacket for Women, Punk Moto Style (53) | 262 | DUP/desc | Women's Leather Motorcycle Jackets | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; alt text missing or copied from description |
| 8 | Burgundy Faux Leather Moto Jacket for Women, Belted Biker St… (63) | 255 | DUP/desc | Women's Leather Motorcycle Jackets | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; alt text missing or copied from description |
| 9 | Platform Biker Boots for Women, Black Buckle Moto Style (55) | 247 | DUP/desc | Women's Motorcycle Boots | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; alt text missing or copied from description |
| 10 | Dainese Black and White Leather Racing Jacket for Women, Spo… (74) | 300 | generic | Women's Leather Motorcycle Jackets | 1000x1500 | `mantasdaunora-21` | #ad at end, not near start; generic alt text |

### Per-pin detail

#### 1. [Zorax Full Face Motorcycle Helmet, Matt Black with Extra Dark Smoke Visor, ECE 22.06](https://www.pinterest.com/pin/634866878772798074/)
- **Board:** Matte Black Motorcycle Gear
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B08XXMRXH2?tag=mantasdaunora-21`
- **Alt:** a man wearing a motorcycle helmet with the words full face written on it in front of him
- **Description:**
```
Shop this full face motorcycle helmet on Amazon UK
Matt black shell, listed as ECE R22.06 approved, with an extra dark smoke visor supplied.
Music by 1000Handz.com
full face motorcycle helmet, matt black motorcycle helmet, matte black motorcycle helmet with tinted visor
#ad
```
- **Flags:** #ad at end, not near start

#### 2. [Brown Leather Biker Jacket for Women, Vintage Rider Style](https://www.pinterest.com/pin/634866878772798055/)
- **Board:** Women's Leather Motorcycle Jackets
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B085HSSGQ2?tag=mantasdaunora-21`
- **Alt:** (duplicates description)
- **Description:**
```
Shop this jacket on Amazon UK
A distressed brown leather biker jacket with quilted shoulders and a cross zip.
Styled with a vintage helmet, jeans and tan boots.
brown leather biker jacket women, vintage biker jacket, womens leather jacket uk, biker outfit women
#ad
```
- **Flags:** #ad at end, not near start, alt text missing or copied from description

#### 3. [Matte Black Open Face Jet Helmet with Visor, Similar Style Retro Look](https://www.pinterest.com/pin/634866878772781941/)
- **Board:** Matte Black Motorcycle Gear
- **Image:** 720×1080 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B00QH25NUM?tag=mantasdaunora-21`
- **Alt:** a black motorcycle with a pink helmet on it's seat
- **Description:**
```
Shop a similar helmet on Amazon UK
A similar style to this matte black open face helmet, with a visor.
Listed as a Nolan N21 Visor Classic jet helmet, size XL.
open face motorcycle helmet, matte black jet helmet, retro motorcycle helmet uk, nolan helmet
#ad
```
- **Flags:** #ad at end, not near start, 2:3 ok but 720x1080 (prefer 1000x1500)

#### 4. [Black Leather Motorcycle Jacket for Men, Winter Ride Look, Similar Style](https://www.pinterest.com/pin/634866878772781902/)
- **Board:** Men's Leather Motorcycle Jackets UK
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B0060MNFYK?tag=mantasdaunora-21`
- **Alt:** a person standing next to a motorcycle on a wet road
- **Description:**
```
Shop a similar jacket on Amazon UK
A similar style to this black leather jacket for men, with a double zip front.
Listed with summer and winter zip positions.
mens leather motorcycle jacket, black leather biker jacket men, mens motorbike jacket uk, winter riding jacket
#ad
```
- **Flags:** #ad at end, not near start

#### 5. [Quilted Leather Biker Jacket for Women with Cross Zip, Similar Style Studio Look](https://www.pinterest.com/pin/634866878772781880/)
- **Board:** Women's Leather Motorcycle Jackets
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B085HLTX7P?tag=mantasdaunora-21`
- **Alt:** (duplicates description)
- **Description:**
```
Shop a similar jacket on Amazon UK
A similar style to this black biker jacket, with quilted panels and a cross zip.
Listed as real lambskin leather.
quilted biker jacket women, womens lambskin leather jacket, biker outfit women, cross zip jacket
#ad
```
- **Flags:** #ad at end, not near start, alt text missing or copied from description

#### 6. [Black Lambskin Leather Biker Jacket for Women, Quilted Shoulders, Similar Style](https://www.pinterest.com/pin/634866878772781848/)
- **Board:** Ebony Biker Outfits & Leather Looks UK
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B085HSGF7V?tag=mantasdaunora-21`
- **Alt:** a woman in a black leather jacket standing next to a motorcycle
- **Description:**
```
Shop a similar jacket on Amazon UK
A similar style to this black biker jacket, with a slanted zip and quilted panels.
Listed as real lambskin leather.
womens lambskin biker jacket, quilted leather jacket women, black leather jacket women, dark garage look
#ad
```
- **Flags:** #ad at end, not near start, generic alt text

#### 7. [Black Studded Biker Jacket for Women, Punk Moto Style](https://www.pinterest.com/pin/634866878772781400/)
- **Board:** Women's Leather Motorcycle Jackets
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B0F8NTGW84?tag=mantasdaunora-21`
- **Alt:** (duplicates description)
- **Description:**
```
Shop this jacket on Amazon UK
A black studded biker jacket with metal studs on the collar and lapels.
Styled with ripped jeans and chunky boots for a punk look.
studded biker jacket women, punk leather jacket women, black moto jacket women, studded jacket uk
#ad
```
- **Flags:** #ad at end, not near start, alt text missing or copied from description

#### 8. [Burgundy Faux Leather Moto Jacket for Women, Belted Biker Style](https://www.pinterest.com/pin/634866878772781373/)
- **Board:** Women's Leather Motorcycle Jackets
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B092J2H997?tag=mantasdaunora-21`
- **Alt:** (duplicates description)
- **Description:**
```
Shop this jacket on Amazon UK
A wine red faux leather moto jacket with a diagonal zip and belted hem.
Styled with black jeans, platform boots and a helmet.
burgundy biker jacket women, wine red leather jacket, womens moto jacket uk, biker outfit women
#ad
```
- **Flags:** #ad at end, not near start, alt text missing or copied from description

#### 9. [Platform Biker Boots for Women, Black Buckle Moto Style](https://www.pinterest.com/pin/634866878772781355/)
- **Board:** Women's Motorcycle Boots
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B0FPMJHQBL?tag=mantasdaunora-21`
- **Alt:** (duplicates description)
- **Description:**
```
Shop these boots on Amazon UK
Chunky black ankle boots with a thick lug sole and two buckle straps.
Styled with a black jacket, leggings and gloves.
platform biker boots women, chunky ankle boots women, black buckle boots women, biker boots uk
#ad
```
- **Flags:** #ad at end, not near start, alt text missing or copied from description

#### 10. [Dainese Black and White Leather Racing Jacket for Women, Sport Biker Style](https://www.pinterest.com/pin/634866878772781319/)
- **Board:** Women's Leather Motorcycle Jackets
- **Image:** 1000×1500 (ratio 0.667; target 1000×1500 / 0.667)
- **Destination (parsed, not fetched):** `https://www.amazon.co.uk/dp/B0F86CNCGV?tag=mantasdaunora-21`
- **Alt:** a woman dressed in black and white posing for a photo
- **Description:**
```
Shop this jacket on Amazon UK
A black and white leather racing jacket for women riders, here with a race helmet and gloves.
Sport cut with white side and shoulder panels.
womens black and white motorcycle jacket, leather racing jacket women, sport motorcycle jacket women, Dainese Racing 5 ladies
#ad
```
- **Flags:** #ad at end, not near start, generic alt text

### Pin rewrite templates (for Gemini bot prompt)

- **Title pattern (<100):** `Women's Full Face Matt Black Motorcycle Helmet ECE 22.06`
- **Description pattern (150–300, disclosure first):** `#ad Shop this full face ECE 22.06 matt black motorcycle helmet on Amazon UK. Dark smoke visor included. Save for UK winter rides. full face motorcycle helmet uk, matt black helmet, tinted visor helmet`
- **Alt text pattern:** `Woman in a matt black Zorax full face motorcycle helmet with dark smoke visor, standing beside a bike`
- **Hard rules for the bot:**
  1. First line of description must start with `#ad` or `#affiliate` (not only at the end).
  2. Keep Associate tag `mantasdaunora-21` (or the active campaign tag) on every Amazon UK destination; never strip `tag=`.
  3. Export / generate images at **1000×1500** (2:3). Reject other ratios.
  4. Alt text must describe the visible product and rider, not paste the description or use generic 'a woman/a man…' stubs.
  5. Front-load search terms in the title; put comma keyword lists after the prose body.
  6. Prefer destination URLs that land on Amazon UK product or Storefront pages with the tag intact (structural check only in CI; do not live-hit tagged links in automated agents).

## Prioritized fix list

### P0 (do first)
1. Move `#ad` / `#affiliate` to the **start** of every affiliate Pin description in the Gemini prompt template.
2. Stop copying the full description into Alt Text; generate distinct visual alt copy.
3. Enforce 1000×1500 exports (flag the 720×1080 jet helmet pin and any future off-size assets).

### P1
4. Claim/verify `rustonroad.github.io` as the primary website; keep Storefront in bio.
5. Shorten display name to brand-first SEO form.
6. Inventory remaining **63** boards for blank descriptions and missing affiliate lines.

### P2
7. Trim off-niche home-find Pins from the core gear boards or segregate them to a dedicated board so gear SEO stays clean.
8. Align Associate tag policy across site (`rustonroadweb-21`) vs Pins (`mantasdaunora-21`) in the bot config notes so campaigns stay intentional.
9. Re-run this audit with Playwright against a logged-in Business session once CDP is tunnelled to the agent.

## Score breakdown (approx.)

| Area | Weight | Earned | Notes |
|---|---:|---:|---|
| Profile keywords & disclosure | 20 | 14 | Strong bio + disclosure; weak domain verification / long display name |
| Board metadata | 15 | 10 | Sampled boards described; full 73 not audited; some miss affiliate line |
| Pin titles | 15 | 14 | All 10 under 100 chars and keyword-led |
| Pin descriptions | 20 | 11 | Keyworded and disclosed, but `#ad` buried at end; length often outside 150–300 |
| Alt & visuals | 15 | 8 | Correct 2:3 on 9/10; alt quality often poor/duplicated |
| Links & compliance | 15 | 10 | Associate tag present on Amazon Pins; disclosure present but not front-loaded |

**Final score: 67/100**

## Data sources

- Apify `khadinakbar/pinterest-profile-scraper` run (profile + 10 boards)
- Apify `fatihtahta/pinterest-scraper-search` runs (recent pins + close-up details)
- No Playwright MCP session was used (unavailable)

