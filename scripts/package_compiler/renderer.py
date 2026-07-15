"""Renderers — build in-memory previews; optional atomic write behind --write.

v1 emits 3 of the 6 spec artifacts: package-registry, gap-report, _manifest.
package-pricing / package-itineraries / booking-compatibility are deferred to a
later pass (spec §5). Write path is atomic (temp + os.replace), mirroring
scripts/compile_trust.py.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from compiler_common.io import sha_text as _sha, atomic_write_json as _atomic_write_json, write_outputs  # noqa: E402

from . import loader

SCHEMA_VERSION = "package-readiness/v1.3"
OUTPUTS = (
    "package-registry.json",
    "package-pricing.json",
    "package-itineraries.json",
    "package-operational-days.json",
    "booking-compatibility.json",
    "gap-report.json",
    "_manifest.json",
)

# overnight_status controlled vocabulary (spec §5, v1.3)
OVERNIGHT_STATUSES = (
    "hotel", "no_overnight", "overnight_in_vehicle", "return_same_day", "unknown",
)
# title keywords that source-back a final-day "no_overnight" classification
_TRIP_END_KEYWORDS = ("return", "finish", "airport", "drop", "handoff", "departure")
# exact key set every operational-day record must carry (no more, no less)
OPERATIONAL_DAY_KEYS = (
    "package_id", "slug", "day", "title", "meal_codes", "hotel_label",
    "overnight_status", "source_basis", "missing_fields", "notes",
)


def build_registry(sources) -> list[dict]:
    return [
        {
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "origin": pk.origin,
            "title": pk.name,
            "duration": pk.duration,
            "public_url": pk.public_url,
            "ijen_relevant": pk.visits_ijen,
            "visits_madakaripura": pk.visits_madakaripura,
            "is_specialty": "taman-safari" in pk.norm_slug,
        }
        for pk in sources.packages
    ]


def _parse_pax(cell: str) -> tuple[int | None, int | None]:
    """'2' -> (2,2); '3–4' -> (3,4); '11+' -> (11,None); '1 (solo)' -> (1,1)."""
    c = cell.lower().replace("(solo)", "").replace("pax", "")
    c = c.replace("–", "-").replace("—", "-").strip()
    if c.endswith("+"):
        digits = re.sub(r"\D", "", c)
        return (int(digits), None) if digits else (None, None)
    if "-" in c:
        a, b = c.split("-", 1)
        da, db = re.sub(r"\D", "", a), re.sub(r"\D", "", b)
        return (int(da) if da else None, int(db) if db else None)
    digits = re.sub(r"\D", "", c)
    v = int(digits) if digits else None
    return (v, v)


def _parse_price(cell: str) -> int | None:
    digits = re.sub(r"[^\d]", "", cell)
    return int(digits) if digits else None


def _parse_meals(cell: str) -> list[str]:
    raw = cell.replace("·", "·")
    parts = re.split(r"[·/,]", raw)
    return [p.strip() for p in parts if p.strip() and p.strip() not in ("—", "-")]


def build_pricing(sources) -> list[dict]:
    out: list[dict] = []
    for pk in sources.packages:
        rows = loader.detail_for(sources.pricing_tables, pk) or []
        tiers = []
        for r in rows:
            if len(r) < 2:
                continue
            mn, mx = _parse_pax(r[0])
            tiers.append({
                "min_pax": mn, "max_pax": mx,
                "idr_per_person": _parse_price(r[1]),
            })
        out.append({
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "currency": "IDR",
            "ferry_included": pk.origin == "bali",
            "pax_tiers": tiers,
        })
    return out


def build_itineraries(sources) -> list[dict]:
    out: list[dict] = []
    for pk in sources.packages:
        rows = loader.detail_for(sources.itinerary_tables, pk) or []
        days = []
        for r in rows:
            if len(r) < 4:
                continue
            day_digits = re.sub(r"\D", "", r[0])
            hotel = r[3].strip()
            days.append({
                "day": int(day_digits) if day_digits else None,
                "title": r[1].strip(),
                "meals": _parse_meals(r[2]),
                "hotel": None if hotel in ("—", "-", "") else hotel,
            })
        out.append({
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "days": days,
        })
    return out


def build_operational_days(sources) -> list[dict]:
    """Explicit, conservative operational-day artifact (spec §5, v1.3).

    Derived from build_itineraries() — makes overnight / meal / hotel semantics
    explicit so downstream consumers never infer them. llm-wiki is the canonical
    public itinerary/day source ONLY: no area / node / cost / room / time fields.
    Records preserve registry order (per package) then day ascending; consumers
    MUST join by package_id + day, never by array index.
    """
    out: list[dict] = []
    for it in build_itineraries(sources):
        days = it["days"]
        last_day = days[-1]["day"] if days else None
        for d in days:
            hotel = d["hotel"]
            title = d["title"]
            meal_codes = [m for m in d["meals"] if m in ("B", "L", "D")]
            missing_fields: list[str] = []
            notes = ""

            if hotel and "vehicle" in hotel.lower():
                overnight_status = "overnight_in_vehicle"
                hotel_label = None  # never invent a hotel name
                source_basis = "package-itineraries.days.hotel"
                notes = hotel  # preserve original source text verbatim
            elif hotel:
                overnight_status = "hotel"
                hotel_label = hotel  # source-backed name, verbatim
                source_basis = "package-itineraries.days.hotel"
            elif d["day"] == last_day and any(
                k in title.lower() for k in _TRIP_END_KEYWORDS
            ):
                overnight_status = "no_overnight"
                hotel_label = None
                source_basis = "package-itineraries.days.hotel+title"
                notes = "Final day; title indicates trip end/return."
            else:
                overnight_status = "unknown"
                hotel_label = None
                source_basis = "package-itineraries.days.hotel"
                missing_fields = ["hotel_label", "overnight_status"]
                notes = "Hotel empty; source does not clearly prove no overnight."

            out.append({
                "package_id": it["package_id"],
                "slug": it["slug"],
                "day": d["day"],
                "title": title,
                "meal_codes": meal_codes,
                "hotel_label": hotel_label,
                "overnight_status": overnight_status,
                "source_basis": source_basis,
                "missing_fields": missing_fields,
                "notes": notes,
            })
    return out


def build_booking_compatibility(sources) -> list[dict]:
    # Website-only booking: all 16 canonical packages are booked exclusively through
    # the official website checkout. WhatsApp/email are support-only and never create,
    # confirm, modify, cancel, or transfer a booking. See packages-overview §booking-flow.
    return [
        {
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "instant_book": True,
            "whatsapp_assisted": False,
            "booking_paths": ["website"],
        }
        for pk in sources.packages
    ]


def build_gap_report(findings: list[dict]) -> dict:
    errors = [f for f in findings if f["severity"] == "error"]
    warns = [f for f in findings if f["severity"] == "warn"]
    return {
        "summary": {"total": len(findings), "errors": len(errors), "warnings": len(warns)},
        "findings": findings,
    }


def build_manifest(sources, findings: list[dict], *, dry_run: bool,
                   counts: dict | None = None) -> dict:
    by_rule: dict[str, int] = {}
    for f in findings:
        by_rule[f["rule_id"]] = by_rule.get(f["rule_id"], 0) + 1
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_by": "scripts/compile_packages.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "canonical_package_count": len(sources.packages),
        "source_hashes": {
            "packages-overview": _sha(sources.overview_text),
            "packages-full-pricing": _sha(sources.pricing_text),
            "packages-itineraries": _sha(sources.itinerary_text),
            "sitemap": _sha(sources.sitemap_text),
            "route-data": _sha(sources.routes_text),
            "policy-source-ownership": _sha(sources.policy_text),
            "db-export": _sha(sources.db_export_text),
        },
        "findings_by_rule": by_rule,
        "artifacts": [n for n in OUTPUTS if n != "_manifest.json"],
        "clean": not any(f["severity"] == "error" for f in findings),
    }
    if counts is not None:
        manifest["record_counts"] = counts
    return manifest
