"""Renderers — build in-memory previews; optional atomic write behind --write.

v1 emits 3 of the 6 spec artifacts: package-registry, gap-report, _manifest.
package-pricing / package-itineraries / booking-compatibility are deferred to a
later pass (spec §5). Write path is atomic (temp + os.replace), mirroring
scripts/compile_trust.py.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from . import loader

SCHEMA_VERSION = "package-readiness/v1.2"
OUTPUTS = (
    "package-registry.json",
    "package-pricing.json",
    "package-itineraries.json",
    "booking-compatibility.json",
    "gap-report.json",
    "_manifest.json",
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


def build_booking_compatibility(sources) -> list[dict]:
    # All 16 canonical packages are live website tour pages (Instant Book path)
    # and bookable via WhatsApp-assisted flow. See packages-overview §booking-flow.
    return [
        {
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "instant_book": True,
            "whatsapp_assisted": True,
            "booking_paths": ["website_instant_book", "whatsapp_assisted"],
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


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_manifest(sources, findings: list[dict], *, dry_run: bool) -> dict:
    by_rule: dict[str, int] = {}
    for f in findings:
        by_rule[f["rule_id"]] = by_rule.get(f["rule_id"], 0) + 1
    return {
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


def _atomic_write_json(path: Path, data) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def write_outputs(out_dir: str | Path, artifacts: dict) -> list[str]:
    """Atomically write each {filename: data} pair. Caller controls the set;
    OUTPUTS defines the canonical v1.2 six."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, data in artifacts.items():
        _atomic_write_json(out / name, data)
    return list(artifacts)
