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
