"""Renderer module tests."""
from datetime import date


def _enriched_c1():
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, AeoFields,
    )
    from scripts.compiler.enricher import EnrichedClaim
    claim = Claim(
        claim_id="C1", name="Safety-Led Operations",
        canonical_text="Volcano travel is unpredictable.",
        domain="credentials", category="trust-signal",
        verification_status="verified",
        wiki_pages=["wiki/x.md"], output_pages=["output/x"],
        evidence_ids=["E001"], evidence_count=1,
        key_proof_ids=["sprin-polpar"],
        tags=["police-led", "safety"],
        last_verified=date(2026, 5, 26),
        stale_after_days=None, entity_refs=[],
    )
    ev = Evidence(
        evidence_id="E001", claim="C1", source_file="wiki/people/agung-sambuko.md",
        evidence_type_code=2, evidence_type="jvto_verified_internal",
        description="Founder is active Tourist Police officer",
        verification_status="verified",
        last_verified=date(2026, 5, 25),
        proof_ids=["sprin-polpar"],
    )
    dec = Decision(
        decision_id="DEC-001", topic="founding_year",
        final_value=2015, secondary_facts=None,
        status="locked", decided_by="Sam",
        decided_at=date(2026, 5, 28),
        source_basis=["AHU"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    narr = AeoFields("C1", "snippet", "short", "cs reply")
    return EnrichedClaim(claim=claim, evidence=[ev], entities=[], decisions=[dec], narrative=narr)


def test_render_claims_structure():
    from scripts.compiler.renderer import render_claims
    out = render_claims([_enriched_c1()], compiled_at="2026-05-28T00:00:00Z")
    assert out["version"] == "1.0"
    assert out["compiled_at"] == "2026-05-28T00:00:00Z"
    assert len(out["claims"]) == 1
    c = out["claims"][0]
    assert c["id"] == "C1"
    assert c["last_verified"] == "2026-05-26"
    assert c["evidence"][0]["type"] == "jvto_verified_internal"
    assert c["decisions"][0]["decision_id"] == "DEC-001"
    assert c["decisions"][0]["final_value"] == 2015
    assert c["narrative"]["ai_snippet"] == "snippet"
