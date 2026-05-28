"""Trust Bundle Compiler — renderer module.

Pure emission. Takes enriched + validated data, returns dicts ready for json.dump.
"""
from __future__ import annotations

from typing import Any

from scripts.compiler.enricher import EnrichedClaim
from scripts.compiler.loader import Entity


_BUNDLE_VERSION = "1.0"
_COMPILER_VERSION = "0.1.0"


def render_claims(enriched: list[EnrichedClaim], compiled_at: str) -> dict[str, Any]:
    """Build claims.json structure."""
    return {
        "version": _BUNDLE_VERSION,
        "compiled_at": compiled_at,
        "claims": [_render_one_claim(ec) for ec in enriched],
    }


def _render_one_claim(ec: EnrichedClaim) -> dict[str, Any]:
    return {
        "id": ec.claim.claim_id,
        "name": ec.claim.name,
        "canonical_text": ec.claim.canonical_text,
        "domain": ec.claim.domain,
        "category": ec.claim.category,
        "last_verified": ec.claim.last_verified.isoformat(),
        "evidence": [
            {
                "id": e.evidence_id,
                "type": e.evidence_type,
                "source_file": e.source_file,
                "description": e.description,
                "proof_ids": e.proof_ids,
            }
            for e in ec.evidence
        ],
        "narrative": {
            "ai_snippet": ec.narrative.ai_snippet if ec.narrative else "",
            "short": ec.narrative.short if ec.narrative else "",
            "cs_reply": ec.narrative.cs_reply if ec.narrative else "",
        },
        "decisions": [
            {
                "decision_id": d.decision_id,
                "topic": d.topic,
                "final_value": d.final_value,
                "decided_at": d.decided_at.isoformat(),
            }
            for d in ec.decisions
        ],
        "tags": ec.claim.tags,
    }


def render_organization_schema(
    legal_name: str,
    brand_name: str,
    nib: str,
    tdup: str,
    founder_name: str,
    founder_job: str,
    url: str,
) -> dict[str, Any]:
    """Build schema/organization.json (JSON-LD TravelAgency)."""
    return {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": brand_name,
        "legalName": legal_name,
        "url": url,
        "identifier": [
            {"@type": "PropertyValue", "propertyID": "NIB", "value": nib},
            {"@type": "PropertyValue", "propertyID": "TDUP", "value": tdup},
        ],
        "founder": {
            "@type": "Person",
            "name": founder_name,
            "jobTitle": founder_job,
        },
    }


def render_faq_page_schema(qa_pairs: list[dict[str, str]]) -> dict[str, Any]:
    """Build schema/faq-page.json (JSON-LD FAQPage)."""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": qa["question"],
                "acceptedAnswer": {"@type": "Answer", "text": qa["answer"]},
            }
            for qa in qa_pairs
        ],
    }


def render_faq(enriched: list[EnrichedClaim]) -> dict[str, Any]:
    """Build faq.json. Answer prefers narrative.short, falls back to narrative.cs_reply."""
    items: list[dict[str, Any]] = []
    for ec in enriched:
        n = ec.narrative
        if n is None:
            continue
        answer = n.short if n.short else n.cs_reply
        items.append({
            "question": ec.claim.name,
            "answer": answer,
            "source_claim_id": ec.claim.claim_id,
            "target_pages": ec.claim.output_pages,
        })
    return {"version": _BUNDLE_VERSION, "items": items}


def render_tourist_trip_schema(entities: list[Entity], base_url: str) -> list[dict[str, Any]]:
    """Build schema/tourist-trip.json — one TouristTrip per destination, deduplicated by canonical_url.

    Resolves the open sprint item 'Duplicate TouristTrip in tour page JSON-LD schemas'
    by collapsing entities that share a canonical_url into a single entry.
    """
    seen: dict[str, dict[str, Any]] = {}
    for e in entities:
        if e.type != "destination":
            continue
        if not e.canonical_url:
            continue
        key = e.canonical_url
        if key in seen:
            continue
        seen[key] = {
            "@context": "https://schema.org",
            "@type": "TouristTrip",
            "name": e.name,
            "url": base_url.rstrip("/") + e.canonical_url,
        }
    return list(seen.values())
