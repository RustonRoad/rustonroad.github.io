/* Locale hint only. No network calls, cookies, or storage.
   US hint: browser language is en-US and the timezone starts with America/.
   Without this script both shop links stay visible, UK first. */
(function () {
  "use strict";

  function looksLikeUS() {
    var language = "";
    var timezone = "";
    try {
      language = String(navigator.language || "").toLowerCase();
    } catch (err) {
      language = "";
    }
    try {
      timezone = String(Intl.DateTimeFormat().resolvedOptions().timeZone || "");
    } catch (err) {
      timezone = "";
    }
    var languageIsUS = language === "en-us" || language.indexOf("en-us-") === 0;
    var timezoneIsUS = timezone.indexOf("America/") === 0;
    return languageIsUS && timezoneIsUS;
  }

  function markUSFirst() {
    if (!looksLikeUS()) return;
    var shops = document.querySelectorAll(".ror-shops");
    for (var i = 0; i < shops.length; i++) {
      shops[i].classList.add("us-first");
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", markUSFirst);
  } else {
    markUSFirst();
  }
})();
