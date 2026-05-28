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


def _make_evidence(eid="E1", claim="C1", status="verified"):
    from scripts.compiler.loader import Evidence
    return Evidence(
        evidence_id=eid, claim=claim, source_file="x",
        evidence_type_code=1, evidence_type="official_authority",
        description="d", verification_status=status,
        last_verified=date(2026, 5, 25), proof_ids=[],
    )


def test_f2a_no_evidence_ids_fails():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Claim
    c = Claim(
        claim_id="C1", name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=[], evidence_count=0,
        key_proof_ids=[], tags=[],
        last_verified=date(2026, 5, 26), stale_after_days=None, entity_refs=[],
    )
    ec = _ec(c, evidence=[])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f2a = [v for v in rep.violations if v.rule_id == "F2a"]
    assert len(f2a) == 1
    assert f2a[0].severity == Severity.ERROR


def test_f2b_unresolved_evidence_id_fails():
    """Claim references E2 but enriched evidence list is empty (E2 missing from registry)."""
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Claim
    c = Claim(
        claim_id="C1", name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=["E2"], evidence_count=1,
        key_proof_ids=[], tags=[],
        last_verified=date(2026, 5, 26), stale_after_days=None, entity_refs=[],
    )
    ec = _ec(c, evidence=[])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f2b = [v for v in rep.violations if v.rule_id == "F2b"]
    assert len(f2b) == 1
    assert "E2" in f2b[0].message


def test_f2c_unverified_evidence_fails():
    from scripts.compiler.validator import run, Severity
    ec = _ec(_make_claim(), evidence=[_make_evidence(status="pending")])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f2c = [v for v in rep.violations if v.rule_id == "F2c"]
    assert len(f2c) == 1
    assert f2c[0].severity == Severity.ERROR


def test_f2_clean_passes():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f2 = [v for v in rep.violations if v.rule_id.startswith("F2")]
    assert f2 == []


def test_f3_unresolved_entity_ref_warns():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Claim
    c = Claim(
        claim_id="C1", name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=["E1"], evidence_count=1,
        key_proof_ids=[], tags=[],
        last_verified=date(2026, 5, 26), stale_after_days=None,
        entity_refs=["ENT-999"],
    )
    ec = _ec(c, evidence=[_make_evidence()], entities=[])  # ENT-999 not in entities
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"},
              today=date(2026, 5, 28), known_entity_ids={"ENT-001"})
    f3 = [v for v in rep.violations if v.rule_id == "F3"]
    assert len(f3) == 1
    assert f3[0].severity == Severity.WARNING


def test_f3_empty_entity_refs_is_clean():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"},
              today=date(2026, 5, 28), known_entity_ids=set())
    f3 = [v for v in rep.violations if v.rule_id == "F3"]
    assert f3 == []


def _make_conflict(cid="CONF-001", status="open", affects=("C1",)):
    from scripts.compiler.loader import Conflict
    return Conflict(
        conflict_id=cid, detected=date(2026, 1, 1),
        claim_a="A", source_a="sa", claim_b="B", source_b="sb",
        status=status, affects_claims=list(affects),
        evidence_weight="w", resolution="r",
    )


def _make_decision(did="DEC-001", status="locked", applies=("C1",), resolves=("CONF-001",)):
    from scripts.compiler.loader import Decision
    return Decision(
        decision_id=did, topic="t", final_value=None,
        secondary_facts=None, status=status,
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=list(applies),
        resolves_conflicts=list(resolves), resolves_dq=[],
        superseded_by=None, notes="",
    )


def test_f4_unresolved_conflict_no_lock_fails():
    from scripts.compiler.validator import run, Severity
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    conflicts = [_make_conflict()]
    rep = run([ec], [], conflicts, {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f4 = [v for v in rep.violations if v.rule_id == "F4"]
    assert len(f4) == 1
    assert f4[0].severity == Severity.ERROR


def test_f4_resolved_conflict_passes():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    conflicts = [_make_conflict(status="resolved")]
    rep = run([ec], [], conflicts, {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    assert [v for v in rep.violations if v.rule_id == "F4"] == []


def test_f4_locked_decision_resolves_conflict():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    conflicts = [_make_conflict()]
    decisions = [_make_decision()]
    rep = run([ec], decisions, conflicts, {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    assert [v for v in rep.violations if v.rule_id == "F4"] == []


def test_f4_provisional_decision_does_not_resolve():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    conflicts = [_make_conflict()]
    decisions = [_make_decision(status="provisional")]
    rep = run([ec], decisions, conflicts, {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f4 = [v for v in rep.violations if v.rule_id == "F4"]
    assert len(f4) == 1


def test_f5_missing_narrative_fails():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.enricher import EnrichedClaim
    claim = _make_claim()
    # Build EnrichedClaim with narrative=None
    ec = EnrichedClaim(claim=claim, evidence=[_make_evidence()], entities=[], decisions=[], narrative=None)
    rep = run([ec], [], [], {}, {"C1"}, today=date(2026, 5, 28))
    f5 = [v for v in rep.violations if v.rule_id == "F5"]
    assert len(f5) == 1
    assert f5[0].severity == Severity.ERROR


def test_f5_present_narrative_passes():
    from scripts.compiler.validator import run
    ec = _ec(_make_claim(), evidence=[_make_evidence()])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    assert [v for v in rep.violations if v.rule_id == "F5"] == []


def test_f5_empty_narrative_fields_fail():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import AeoFields
    from scripts.compiler.enricher import EnrichedClaim
    claim = _make_claim()
    bad = AeoFields("C1", "", "", "")
    ec = EnrichedClaim(claim=claim, evidence=[_make_evidence()], entities=[], decisions=[], narrative=bad)
    rep = run([ec], [], [], {"C1": bad}, {"C1"}, today=date(2026, 5, 28))
    f5 = [v for v in rep.violations if v.rule_id == "F5"]
    assert len(f5) == 1


def test_f6_back_ref_mismatch_warns():
    from scripts.compiler.validator import run, Severity
    # E1 back-ref says claim=C2 but C1.evidence_ids includes E1 → mismatch
    bad_ev = _make_evidence(eid="E1", claim="C2")
    from scripts.compiler.loader import Claim
    c = Claim(
        claim_id="C1", name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=["E1"], evidence_count=1,
        key_proof_ids=[], tags=[],
        last_verified=date(2026, 5, 26), stale_after_days=None, entity_refs=[],
    )
    ec = _ec(c, evidence=[bad_ev])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f6 = [v for v in rep.violations if v.rule_id == "F6"]
    assert len(f6) == 1
    assert f6[0].severity == Severity.WARNING


def test_f7_evidence_count_mismatch_warns():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Claim
    c = Claim(
        claim_id="C1", name="n", canonical_text="t",
        domain="d", category="c", verification_status="verified",
        wiki_pages=[], output_pages=[], evidence_ids=["E1"], evidence_count=99,  # mismatch
        key_proof_ids=[], tags=[],
        last_verified=date(2026, 5, 26), stale_after_days=None, entity_refs=[],
    )
    ec = _ec(c, evidence=[_make_evidence()])
    rep = run([ec], [], [], {"C1": ec.narrative}, {"C1"}, today=date(2026, 5, 28))
    f7 = [v for v in rep.violations if v.rule_id == "F7"]
    assert len(f7) == 1
    assert f7[0].severity == Severity.WARNING


def test_f8a_empty_source_basis_fails():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Decision
    d = Decision(
        decision_id="DEC-001", topic="t", final_value=None,
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=[], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    rep = run([], [d], [], {}, {"C1"}, today=date(2026, 5, 28))
    f8a = [v for v in rep.violations if v.rule_id == "F8a"]
    assert len(f8a) == 1
    assert f8a[0].severity == Severity.ERROR


def test_f8b_resolves_unknown_conflict_warns():
    from scripts.compiler.validator import run, Severity
    d = _make_decision(resolves=("CONF-999",))
    rep = run([], [d], [], {}, {"C1"}, today=date(2026, 5, 28))
    f8b = [v for v in rep.violations if v.rule_id == "F8b"]
    assert len(f8b) == 1
    assert f8b[0].severity == Severity.WARNING


def test_f8c_duplicate_locked_topic_fails():
    from scripts.compiler.validator import run, Severity
    from scripts.compiler.loader import Decision
    d1 = Decision(
        decision_id="DEC-001", topic="same_topic", final_value=1,
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 1),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    d2 = Decision(
        decision_id="DEC-002", topic="same_topic", final_value=2,
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    rep = run([], [d1, d2], [], {}, {"C1"}, today=date(2026, 5, 28))
    f8c = [v for v in rep.violations if v.rule_id == "F8c"]
    assert len(f8c) == 1


def test_f8c_superseded_chain_passes():
    from scripts.compiler.validator import run
    from scripts.compiler.loader import Decision
    d1 = Decision(
        decision_id="DEC-001", topic="t", final_value=1,
        secondary_facts=None, status="superseded",
        decided_by="Sam", decided_at=date(2026, 5, 1),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by="DEC-002", notes="",
    )
    d2 = Decision(
        decision_id="DEC-002", topic="t", final_value=2,
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    rep = run([], [d1, d2], [], {}, {"C1"}, today=date(2026, 5, 28))
    assert [v for v in rep.violations if v.rule_id == "F8c"] == []


def test_f8d_unknown_applies_to_claim_fails():
    from scripts.compiler.validator import run, Severity
    d = _make_decision(applies=("C999",))
    rep = run([], [d], [], {}, {"C1"}, today=date(2026, 5, 28))
    f8d = [v for v in rep.violations if v.rule_id == "F8d"]
    assert len(f8d) == 1
    assert f8d[0].severity == Severity.ERROR
