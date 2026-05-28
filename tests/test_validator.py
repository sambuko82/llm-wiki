# tests/test_validator.py
"""Validator module tests."""
from datetime import date


def test_validation_report_has_zero_errors_for_clean_inputs():
    from scripts.compiler.validator import run, Severity
    report = run(
        enriched_claims=[],
        decisions=[],
        conflicts=[],
        narratives={},
        all_claim_ids=set(),
        today=date(2026, 5, 28),
    )
    assert report.violations == []
    assert report.has_errors is False


def test_severity_enum_values():
    from scripts.compiler.validator import Severity
    assert Severity.ERROR.value == "error"
    assert Severity.WARNING.value == "warning"


def _make_claim(claim_id="C1", last_verified=date(2026, 5, 1), stale_after_days=None):
    from scripts.compiler.loader import Claim
    return Claim(
        claim_id=claim_id, name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=["E1"], evidence_count=1,
        key_proof_ids=[], tags=[],
        last_verified=last_verified, stale_after_days=stale_after_days, entity_refs=[],
    )


def _ec(claim, evidence=None, narrative=None, entities=None, decisions=None):
    from scripts.compiler.enricher import EnrichedClaim
    from scripts.compiler.loader import AeoFields
    return EnrichedClaim(
        claim=claim,
        evidence=evidence or [],
        entities=entities or [],
        decisions=decisions or [],
        narrative=narrative or AeoFields(claim.claim_id, "a", "s", "c"),
    )


def test_f1_fresh_within_90_days():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(last_verified=date(2026, 3, 1)))   # 88 days before 2026-05-28
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f1 = [v for v in rep.violations if v.rule_id == "F1"]
    assert f1 == []


def test_f1_stale_beyond_90_days():
    from scripts.compiler.validator import run, Severity
    ec = _ec(_make_claim(last_verified=date(2026, 1, 1)))   # 148 days, stale
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f1 = [v for v in rep.violations if v.rule_id == "F1"]
    assert len(f1) == 1
    assert f1[0].severity == Severity.ERROR
    assert f1[0].target_id == "C1"


def test_f1_per_claim_override_extends_window():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(last_verified=date(2026, 1, 1), stale_after_days=365))
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f1 = [v for v in rep.violations if v.rule_id == "F1"]
    assert f1 == []


def test_f1_per_claim_override_shortens_window():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(last_verified=date(2026, 4, 1), stale_after_days=30))  # 57 days, stale
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f1 = [v for v in rep.violations if v.rule_id == "F1"]
    assert len(f1) == 1
