"""PKG validation rules — first pass (spec §6).

Each rule appends findings to a flat list. A finding is a dict:
  {rule_id, severity, package_id, field, wiki_value, reference_value, message}
severity: "error" blocks a clean compile under --strict; "warn" reports only.

v1 implements PKG-01..PKG-05 and PKG-07..PKG-10. PKG-06 (inclusion/exclusion
count vs DB), PKG-11 (DB reconciliation), PKG-12 (forbidden-phrase sweep) are
deferred to a later pass — see spec.
"""
from __future__ import annotations

import re

ERROR = "error"
WARN = "warn"


def _finding(rule_id, severity, package_id, field, message,
             wiki_value=None, reference_value=None):
    return {
        "rule_id": rule_id,
        "severity": severity,
        "package_id": package_id,
        "field": field,
        "wiki_value": wiki_value,
        "reference_value": reference_value,
        "message": message,
    }


def _has(text: str, *needles: str) -> bool:
    low = text.lower()
    return all(n.lower() in low for n in needles)


def validate(sources) -> list[dict]:
    findings: list[dict] = []
    ov = sources.overview_text
    pricing = sources.pricing_text
    itin = sources.itinerary_text

    # --- document-level wording probes (shared across per-package checks) ---
    health_conditional = (
        (_has(ov, "health-screening") or _has(ov, "health screening"))
        and (_has(ov, "bbksda") or _has(ov, "conditional"))
    )
    health_mandatory_bad = _has(ov, "universally mandatory")
    ferry_ok = _has(ov, "ferry") and _has(ov, "gilimanuk")
    helmet_caveat_ok = _has(ov, "helmet") and _has(ov, "not a jvto inclusion")
    helmet_bad = bool(
        re.search(r"jvto[^.\n]{0,40}provides?[^.\n]{0,20}helmet", ov, re.I)
        or re.search(r"helmet[s]?[^.\n]{0,30}included\s+(by|as)[^.\n]{0,20}jvto", ov, re.I)
    )
    booking_instant = _has(ov, "instant book")
    booking_whatsapp = _has(ov, "whatsapp")

    for pk in sources.packages:
        pid = pk.slug

        # PKG-01 slug exists
        if not pk.norm_slug:
            findings.append(_finding("PKG-01", ERROR, pid, "slug", "package has no slug"))

        # PKG-02 title exists
        if not pk.name:
            findings.append(_finding("PKG-02", ERROR, pid, "title", "package has no title"))

        # PKG-03 public route candidate present in sitemap snapshot
        live = sources.sitemap_slugs.get(pk.origin, set())
        if pk.norm_slug not in live:
            findings.append(_finding(
                "PKG-03", ERROR, pid, "public_url",
                f"derived url {pk.public_url} not found in sitemap snapshot",
                wiki_value=pk.public_url, reference_value=sorted(live)))

        # PKG-04 pricing mention/source
        if pk.norm_slug not in pricing and pk.slug not in pricing:
            findings.append(_finding(
                "PKG-04", WARN, pid, "pricing",
                "no pricing mention found in packages-full-pricing"))

        # PKG-05 itinerary mention/source
        if pk.norm_slug not in itin and pk.slug not in itin:
            findings.append(_finding(
                "PKG-05", WARN, pid, "itinerary",
                "no itinerary mention found in packages-itineraries"))

        # PKG-07 Ijen packages require conditional health-screening wording
        if pk.visits_ijen and (not health_conditional or health_mandatory_bad):
            findings.append(_finding(
                "PKG-07", ERROR, pid, "health_screening",
                "Ijen package missing conditional health-screening wording "
                "or wording asserts 'universally mandatory'"))

        # PKG-08 Bali-origin packages require ferry inclusion
        if pk.origin == "bali" and not ferry_ok:
            findings.append(_finding(
                "PKG-08", ERROR, pid, "ferry",
                "Bali-origin package missing Gilimanuk-Ketapang ferry inclusion"))

        # PKG-09 Madakaripura helmet must NOT be a JVTO inclusion
        if pk.visits_madakaripura and (helmet_bad or not helmet_caveat_ok):
            findings.append(_finding(
                "PKG-09", ERROR, pid, "helmet",
                "Madakaripura package: helmet caveat missing or helmet implied "
                "as a JVTO inclusion"))

        # PKG-10 booking path compatibility documented
        if not (booking_instant and booking_whatsapp):
            findings.append(_finding(
                "PKG-10", ERROR, pid, "booking_paths",
                "booking paths must mention both Instant Book and WhatsApp-assisted"))

    return findings
