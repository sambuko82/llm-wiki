"""Enricher module tests."""
from datetime import date


def _sample_inputs():
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, AeoFields,
    )
    claim_c1 = Claim(
        claim_id="C1", name="One", canonical_text="t1", domain="d", category="c",
        verification_status="verified", wiki_pages=[], output_pages=[],
        evidence_ids=["E001", "E002"], evidence_count=2, key_proof_ids=[],
        tags=[], last_verified=date(2026, 5, 26),
        stale_after_days=None, entity_refs=[],
    )
    e1 = Evidence(
        evidence_id="E001", claim="C1", source_file="x",
        evidence_type_code=1, evidence_type="official_authority",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 25), proof_ids=[],
    )
    e2 = Evidence(
        evidence_id="E002", claim="C1", source_file="y",
        evidence_type_code=2, evidence_type="jvto_verified_internal",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 12), proof_ids=[],
    )
    e_stray = Evidence(
        evidence_id="E999", claim="C1", source_file="z",
        evidence_type_code=6, evidence_type="customer_review",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 1), proof_ids=[],
    )
    ent = Entity(
        entity_id="ENT-001", name="Ijen", type="destination",
        aliases=[], wiki_pages=[], schema_type="TouristAttraction",
        canonical_url="/d/ijen", claims=["C1"], tags=[],
    )
    dec_locked = Decision(
        decision_id="DEC-001", topic="t", final_value={"x": 1},
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    dec_prov = Decision(
        decision_id="DEC-002", topic="t2", final_value=2015,
        secondary_facts=None, status="provisional",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    narr = {"C1": AeoFields("C1", "ai", "short", "cs")}
    return [claim_c1], [e1, e2, e_stray], [ent], [dec_locked, dec_prov], narr


def test_enrich_joins_by_claim_evidence_ids():
    """Evidence resolved by claim.evidence_ids (whitelist), not by evidence.claim back-ref."""
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert len(enriched) == 1
    ec = enriched[0]
    assert ec.claim.claim_id == "C1"
    # E999 is excluded because not in claim.evidence_ids even though its back-ref matches
    assert [e.evidence_id for e in ec.evidence] == ["E001", "E002"]


def test_enrich_attaches_locked_decisions_only():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    ec = enriched[0]
    assert [d.decision_id for d in ec.decisions] == ["DEC-001"]


def test_enrich_attaches_entities_by_back_ref():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert [e.entity_id for e in enriched[0].entities] == ["ENT-001"]


def test_enrich_attaches_narrative():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert enriched[0].narrative.ai_snippet == "ai"
