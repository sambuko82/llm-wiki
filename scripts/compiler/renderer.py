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
