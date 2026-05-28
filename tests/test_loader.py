"""Loader module tests."""
import pytest


def test_dataclasses_importable():
    """All dataclass types are exported from loader module."""
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, Conflict, AeoFields,
    )
    assert Claim is not None
    assert Evidence is not None
    assert Entity is not None
    assert Decision is not None
    assert Conflict is not None
    assert AeoFields is not None


def test_claim_instantiation():
    from scripts.compiler.loader import Claim
    from datetime import date
    c = Claim(
        claim_id="C1",
        name="Test",
        canonical_text="Body",
        domain="credentials",
        category="trust-signal",
        verification_status="verified",
        wiki_pages=[],
        output_pages=[],
        evidence_ids=["E001"],
        evidence_count=1,
        key_proof_ids=[],
        tags=[],
        last_verified=date(2026, 5, 26),
        stale_after_days=None,
        entity_refs=[],
    )
    assert c.claim_id == "C1"
    assert c.stale_after_days is None


def test_load_claims_parses_minimal_fixture(fixtures_dir):
    from scripts.compiler.loader import load_claims
    claims = load_claims(fixtures_dir / "minimal-claim-registry.yml")
    assert len(claims) == 2
    assert claims[0].claim_id == "C1"
    assert claims[0].stale_after_days is None
    assert claims[0].entity_refs == []
    assert claims[1].claim_id == "C2"
    assert claims[1].stale_after_days == 30
    assert claims[1].entity_refs == ["ENT-001"]


def test_load_claims_dates_parsed(fixtures_dir):
    from scripts.compiler.loader import load_claims
    from datetime import date
    claims = load_claims(fixtures_dir / "minimal-claim-registry.yml")
    assert claims[0].last_verified == date(2026, 5, 26)


def test_load_evidence_maps_type_codes(fixtures_dir):
    from scripts.compiler.loader import load_evidence
    items = load_evidence(fixtures_dir / "minimal-evidence-registry.yml")
    assert len(items) == 3
    assert items[0].evidence_type_code == 1
    assert items[0].evidence_type == "official_authority"
    assert items[1].evidence_type == "jvto_verified_internal"
    assert items[2].evidence_type == "customer_review"


def test_load_evidence_unknown_type_raises(tmp_path):
    from scripts.compiler.loader import load_evidence
    bad = tmp_path / "bad.yml"
    bad.write_text(
        "evidence:\n"
        "  - evidence_id: E999\n"
        "    claim: C1\n"
        "    source_file: x\n"
        "    evidence_type: 99\n"
        "    description: x\n"
        "    verification_status: verified\n"
        "    last_verified: 2026-05-01\n"
        "    proof_ids: []\n"
    )
    with pytest.raises(ValueError, match="unknown evidence_type"):
        load_evidence(bad)


def test_load_entities(fixtures_dir):
    from scripts.compiler.loader import load_entities
    items = load_entities(fixtures_dir / "minimal-entity-registry.yml")
    assert len(items) == 2
    assert items[0].entity_id == "ENT-001"
    assert items[0].schema_type == "TouristAttraction"
    assert items[0].canonical_url == "/destinations/test"
    assert items[0].claims == ["C1", "C2"]
    assert items[1].schema_type is None
    assert items[1].canonical_url is None
