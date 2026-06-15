"""PKG validation rules — first pass (spec §6).

Each rule appends findings to a flat list. A finding is a dict:
  {rule_id, severity, package_id, field, wiki_value, reference_value, message}
severity: "error" blocks a clean compile under --strict; "warn" reports only.

v1.1 implements PKG-01..PKG-12:
  PKG-01..05, 07..10 — per-package (slug/title/route/pricing/itinerary + wording)
  PKG-06            — inclusion/exclusion readiness (doc-level coverage + no overpromise)
  PKG-11            — DB-export reconciliation (canonical 16 vs DB 22 + variant breakdown)
  PKG-12            — forbidden/deprecated wording sweep over ACTIVE package source
                      (overview/pricing/itineraries). The policy-source-ownership
                      deprecated table and wiki/log.md history are guardrail/audit
                      containers and are intentionally NOT scanned; a full-repo
                      sweep is the Global Validator's job (transformation-map P6).
"""
from __future__ import annotations

import re

from . import loader

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

        # PKG-04 pricing detail present + parseable (origin-aware lookup)
        if not loader.detail_for(sources.pricing_tables, pk):
            findings.append(_finding(
                "PKG-04", WARN, pid, "pricing",
                "no parseable pricing tier table found in packages-full-pricing"))

        # PKG-05 itinerary detail present + parseable
        if not loader.detail_for(sources.itinerary_tables, pk):
            findings.append(_finding(
                "PKG-05", WARN, pid, "itinerary",
                "no parseable itinerary day table found in packages-itineraries"))

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

    # --- document-level rules (PKG-06 / PKG-11 / PKG-12) ---
    findings.extend(_pkg06_inclusions(sources))
    findings.extend(_pkg11_db_reconciliation(sources))
    findings.extend(_pkg12_forbidden_wording(sources))

    return findings


# overpromise phrases that contradict the "no hidden costs, but bounded" model
_OVERPROMISE = (
    "everything included", "all expenses included", "all-expenses-included",
    "unlimited extras", "unlimited add-ons", "all costs included",
)

# forbidden/deprecated wording (lowercased literal substrings) — see
# wiki/ops/policy-source-ownership.md §deprecated. Negative/correct forms
# (e.g. "cash refund is not available") are deliberately NOT substrings here.
_FORBIDDEN = (
    "trip.com",
    "blue fire guaranteed", "guaranteed blue fire",
    "sunrise guaranteed", "guaranteed sunrise",
    "cash refund is available", "cash refunds are available",
    "cash refund available for guest",
    "police escort included", "police escort is included",
    "unesco endorses jvto",
    "50% cancellation fee", "50% fee",
)


_OPERATIONAL_DAY_KEYS = (
    "package_id", "slug", "day", "title", "meal_codes", "hotel_label",
    "overnight_status", "source_basis", "missing_fields", "notes",
)
_OVERNIGHT_STATUSES = (
    "hotel", "no_overnight", "overnight_in_vehicle", "return_same_day", "unknown",
)
# substrings that would signal a PII or cost/room key leaked into the artifact
_FORBIDDEN_KEY_SUBSTR = (
    "email", "phone", "whatsapp", "guest", "passenger", "name",
    "cost", "price", "rate", "room", "area", "node",
)


def validate_operational_days(records: list[dict], itineraries: list[dict]) -> list[str]:
    """Integrity checks for package-operational-days.json (spec §5, v1.3).

    Returns a list of problem strings (empty == artifact is sound). Asserts:
    every canonical package + every itinerary day appears; meal_codes ⊆ {B,L,D};
    overnight_status ∈ enum; hotel_label is None or a verbatim itinerary hotel
    (no invented labels); record keys are exactly the 10 allowed (no cost/room/
    PII keys leaked).
    """
    problems: list[str] = []

    # index source itinerary days by (package_id, day) for cross-checks
    src_days: dict[tuple, dict] = {}
    src_pkgs: set = set()
    for it in itineraries:
        src_pkgs.add(it["package_id"])
        for d in it["days"]:
            src_days[(it["package_id"], d["day"])] = d

    rec_pkgs = {r["package_id"] for r in records}
    for missing in sorted(src_pkgs - rec_pkgs):
        problems.append(f"package missing from operational-days: {missing}")

    seen: set = set()
    for r in records:
        rid = f"{r.get('package_id')}:{r.get('day')}"

        keys = set(r.keys())
        if keys != set(_OPERATIONAL_DAY_KEYS):
            problems.append(f"{rid}: key set {sorted(keys)} != allowed 10")
        for k in keys:
            low = k.lower()
            if any(sub in low for sub in _FORBIDDEN_KEY_SUBSTR):
                problems.append(f"{rid}: forbidden key '{k}' (cost/room/PII)")

        key = (r["package_id"], r["day"])
        seen.add(key)
        src = src_days.get(key)
        if src is None:
            problems.append(f"{rid}: day not present in itineraries source")
            continue

        for m in r["meal_codes"]:
            if m not in ("B", "L", "D"):
                problems.append(f"{rid}: invalid meal code '{m}'")

        if r["overnight_status"] not in _OVERNIGHT_STATUSES:
            problems.append(f"{rid}: invalid overnight_status '{r['overnight_status']}'")

        label = r["hotel_label"]
        if label is not None and label != src["hotel"]:
            problems.append(
                f"{rid}: hotel_label '{label}' not verbatim from itinerary "
                f"hotel '{src['hotel']}'")

    for key in sorted(set(src_days) - seen):
        problems.append(f"itinerary day missing from operational-days: {key}")

    return problems


def _pkg06_inclusions(sources) -> list[dict]:
    """PKG-06 — inclusion/exclusion readiness (doc-level)."""
    out: list[dict] = []
    ov = sources.overview_text
    active = (ov + "\n" + sources.pricing_text).lower()

    # coverage: both an inclusions and an exclusions section must exist
    if not (_has(ov, "inclusion")):
        out.append(_finding("PKG-06", WARN, "*", "inclusions",
                            "no inclusions coverage found in packages-overview"))
    if not (_has(ov, "exclusion")):
        out.append(_finding("PKG-06", WARN, "*", "exclusions",
                            "no exclusions coverage found in packages-overview"))

    # forbidden inclusion claim: all-inclusive treated as unlimited extras
    for phrase in _OVERPROMISE:
        if phrase in active:
            out.append(_finding("PKG-06", ERROR, "*", "inclusions",
                                f"overpromise inclusion claim present: '{phrase}'"))

    # Madakaripura helmet must not be a JVTO inclusion (re-affirm at doc level)
    helmet_bad = bool(
        re.search(r"jvto[^.\n]{0,40}provides?[^.\n]{0,20}helmet", ov, re.I)
        or re.search(r"helmet[s]?[^.\n]{0,30}included\s+(by|as)[^.\n]{0,20}jvto", ov, re.I))
    if helmet_bad:
        out.append(_finding("PKG-06", ERROR, "*", "inclusions",
                            "Madakaripura helmet implied as a JVTO inclusion"))
    return out


def _pkg11_db_reconciliation(sources) -> list[dict]:
    """PKG-11 — reconcile canonical package set against DB-export counts."""
    out: list[dict] = []
    canonical = len(sources.packages)
    db = sources.db_export_text

    m = re.search(r"`packages`\s*\|\s*(\d+)\s*\|([^\n|]*)", db)
    if not m:
        out.append(_finding("PKG-11", WARN, "*", "db_packages",
                            "could not read DB `packages` count from db-export"))
        return out
    db_total = int(m.group(1))
    note = m.group(2).lower()

    # error if a canonical package cannot exist in the DB set (canonical > DB)
    if canonical > db_total:
        out.append(_finding("PKG-11", ERROR, "*", "db_packages",
                            f"canonical {canonical} exceeds DB packages {db_total} — "
                            "canonical package missing from DB/export source",
                            wiki_value=canonical, reference_value=db_total))
        return out

    # the extra DB packages must be classified (student/specialty), not assumed public
    extra = db_total - canonical
    classified = ("student" in note) or ("variant" in note) or ("special" in note)
    if extra > 0 and not classified:
        out.append(_finding("PKG-11", WARN, "*", "db_packages",
                            f"{extra} extra DB packages not classified as variants in db-export note",
                            wiki_value=canonical, reference_value=db_total))
    return out


def _pkg12_forbidden_wording(sources) -> list[dict]:
    """PKG-12 — forbidden/deprecated wording sweep over active package source."""
    out: list[dict] = []
    active = "\n".join((
        sources.overview_text, sources.pricing_text, sources.itinerary_text,
    )).lower()
    for phrase in _FORBIDDEN:
        if phrase in active:
            out.append(_finding("PKG-12", ERROR, "*", "wording",
                                f"forbidden/deprecated wording in active package source: '{phrase}'"))
    # Madakaripura-helmet-as-JVTO regex (phrasing the literal list can't catch)
    if re.search(r"helmet[s]?[^.\n]{0,30}included\s+(by|as)[^.\n]{0,20}jvto",
                 active, re.I):
        out.append(_finding("PKG-12", ERROR, "*", "wording",
                            "forbidden wording: Madakaripura helmet included by JVTO"))
    return out
