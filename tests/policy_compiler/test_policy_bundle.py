"""Tests for the Policy Bundle Compiler (v2)."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
WIKI = ROOT / "wiki"

import compile_policy_bundle  # noqa: E402
from policy_compiler import loader, renderer, validator  # noqa: E402


class LoaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)

    def test_parses_policy_domains(self):
        self.assertEqual(len(self.src.ownership_rows), 9)

    def test_parses_deprecated_rules(self):
        # v2 expanded the deprecated table (scenario-aware rows + forbidden phrases).
        self.assertEqual(len(self.src.deprecated_rules), 13)
        self.assertEqual(self.src.deprecated_rules[0].deprecated, "Trip.com booking flow")

    def test_parses_faq_answers(self):
        self.assertIn("Q15", self.src.faq_answers)
        self.assertIn("official JVTO website", self.src.faq_answers["Q15"])

    def test_loads_cancellation_policy(self):
        self.assertEqual(self.src.cancellation_policy["schema_version"], "cancellation-policy/v2.0")
        self.assertEqual(self.src.cancellation_policy["cutoff"]["hours"], 48)

    def test_rejects_unknown_booking_source(self):
        with tempfile.TemporaryDirectory() as d:
            wiki = Path(d) / "wiki"
            # minimal stub tree
            (wiki / "ops").mkdir(parents=True)
            (wiki / "products").mkdir()
            (wiki / "website").mkdir()
            (wiki / "policies").mkdir()
            (wiki / "ops" / "policy-source-ownership.md").write_text("x", encoding="utf-8")
            (wiki / "products" / "packages-overview.md").write_text("x", encoding="utf-8")
            (wiki / "website" / "faq-master.md").write_text("x", encoding="utf-8")
            bad = copy.deepcopy(self.src.cancellation_policy)
            bad["booking_scope"]["allowed_sources"] = ["carrier_pigeon"]
            import yaml
            (wiki / "policies" / "cancellation-package-credit.yml").write_text(yaml.safe_dump(bad), encoding="utf-8")
            with self.assertRaises(ValueError):
                loader.load_cancellation_policy(wiki)


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)
        cls.policy_bundle = renderer.build_policy_bundle(cls.src)
        cls.consumer_bundles = renderer.build_consumer_bundles(cls.policy_bundle)
        cls.decision_matrix = renderer.build_decision_matrix(cls.src.cancellation_policy)
        cls.customer_copy = renderer.build_customer_copy(cls.src.cancellation_policy)
        cls.deprecated = renderer.build_deprecated_report(cls.src, cls.consumer_bundles)

    def test_policy_bundle_has_expected_domains(self):
        ids = {p["policy_id"] for p in self.policy_bundle}
        self.assertIn("booking-paths", ids)
        self.assertIn("payment-rules", ids)
        self.assertIn("cancellation-package-credit", ids)
        self.assertIn("anti-fraud", ids)

    def test_consumer_bundles_cover_controlled_vocabulary(self):
        self.assertEqual(set(self.consumer_bundles), set(renderer.CONSUMERS))
        self.assertNotIn("whatsapp", self.consumer_bundles)
        self.assertIn("payment-rules", self.consumer_bundles["website_checkout"]["policy_ids"])
        self.assertIn("payment-rules", self.consumer_bundles["invoice"]["policy_ids"])
        self.assertIn("cancellation-package-credit", self.consumer_bundles["website_checkout"]["policy_ids"])
        self.assertIn("cancellation-package-credit", self.consumer_bundles["booking_portal"]["policy_ids"])
        # WhatsApp health screening now resolves to read-only customer_support.
        self.assertIn("ijen-health-screening", self.consumer_bundles["customer_support"]["policy_ids"])

    def test_decision_matrix_core_rules(self):
        rules = self.decision_matrix["rules"]
        self.assertEqual(rules["full_voluntary_gte_48h"]["outcome"], "lifetime_package_credit")
        self.assertEqual(rules["full_voluntary_gte_48h"]["cash_refund_percent"], 0)
        self.assertEqual(rules["full_voluntary_lt_48h"]["outcome"], "forfeited")
        self.assertEqual(rules["partial_gte_48h"]["cash_refund_percent"], 100)
        self.assertEqual(rules["partial_lt_48h"]["cash_refund_percent"], 50)
        self.assertEqual(rules["flight_disruption_verified"]["recovery_fee_percent"], 50)
        self.assertEqual(self.decision_matrix["package_credit_locks"]["maximum_transfers"], 1)

    def test_customer_copy_blocks_present_and_numeric(self):
        for key in (
            "package_guarantee_summary",
            "before_48_full_cancellation",
            "after_48_full_cancellation",
            "partial_cancellation",
            "flight_disruption",
            "destination_force_majeure",
            "package_transfer",
            "package_redemption",
        ):
            self.assertIn(key, self.customer_copy)
        self.assertIn("48 hours", self.customer_copy["package_guarantee_summary"])
        self.assertIn("50%", self.customer_copy["flight_disruption"])
        self.assertIn("not cash", self.customer_copy["before_48_full_cancellation"])

    def test_deprecated_report_clean_on_current_sources(self):
        self.assertEqual(self.deprecated["summary"]["total_findings"], 0)
        self.assertTrue(all(c["clean"] for c in self.deprecated["consumers"].values()))

    def test_validator_clean(self):
        findings = validator.validate(
            self.policy_bundle,
            self.deprecated,
            cancellation_policy=self.src.cancellation_policy,
            decision_matrix=self.decision_matrix,
            consumer_bundles=self.consumer_bundles,
        )
        self.assertEqual(findings, [])

    def test_deprecated_report_flags_injected_bad_wording(self):
        bad = loader.load_sources(WIKI)
        bad.package_sections["Cancellation Policy"] += "\nCash refund available for guest-initiated cancellation."
        bundle = renderer.build_policy_bundle(bad)
        consumers = renderer.build_consumer_bundles(bundle)
        report = renderer.build_deprecated_report(bad, consumers)
        self.assertGreater(report["summary"]["total_findings"], 0)
        self.assertFalse(report["consumers"]["website_checkout"]["clean"])

    def test_pol2_rules_fire_on_bad_policy(self):
        cases = {
            "POL2-01": ("booking_scope", lambda p: p["booking_scope"]["allowed_sources"].append("whatsapp")),
            "POL2-07": ("package_credit", lambda p: p["package_credit"].__setitem__("split_allowed", True)),
            "POL2-08": ("package_credit", lambda p: p["package_credit"].__setitem__("maximum_transfers", 3)),
            "POL2-10": ("partial", lambda p: p["partial_cancellation"]["after_cutoff"].__setitem__("cash_refund_percent", 40)),
            "POL2-11": ("flight", lambda p: p["flight_disruption"].__setitem__("recovery_fee_percent", 25)),
        }
        for rule_id, (_label, mutate) in cases.items():
            policy = copy.deepcopy(self.src.cancellation_policy)
            mutate(policy)
            bundle = copy.deepcopy(self.policy_bundle)
            for entry in bundle:
                if entry["policy_id"] == renderer.CANCELLATION_POLICY_ID:
                    entry["canonical_policy"] = policy
            dm = renderer.build_decision_matrix(policy)
            findings = validator.validate_cancellation(bundle, policy, dm, self.consumer_bundles)
            ids = {f["rule_id"] for f in findings}
            self.assertIn(rule_id, ids, msg=f"expected {rule_id} to fire")

    def test_pol2_14_unregistered_consumer(self):
        bundle = copy.deepcopy(self.policy_bundle)
        bundle[0]["unregistered_consumers"] = ["telegram"]
        findings = validator.validate_cancellation(
            bundle, self.src.cancellation_policy, self.decision_matrix, self.consumer_bundles
        )
        self.assertIn("POL2-14", {f["rule_id"] for f in findings})

    def test_write_outputs_emits_expected_files(self):
        gap = renderer.build_gap_report(self.policy_bundle, self.deprecated)
        manifest = renderer.build_manifest(self.src, gap, dry_run=False)
        self.assertEqual(manifest["sync_contract"]["required_gate"]["schema_version"], "policy-bundle/v2.0")
        self.assertTrue(manifest["sync_contract"]["required_gate"]["clean"])
        self.assertEqual(manifest["sync_contract"]["target_path"], "src/data/policy-bundle/")
        self.assertEqual(manifest["cancellation_policy_version"], "2026-07")
        artifacts = {
            "policy-bundle.json": self.policy_bundle,
            "consumer-bundles.json": self.consumer_bundles,
            "decision-matrix.json": self.decision_matrix,
            "customer-copy.json": self.customer_copy,
            "deprecated-wording-report.json": self.deprecated,
            "gap-report.json": gap,
            "_manifest.json": manifest,
        }
        self.assertEqual(sorted(artifacts), sorted(renderer.OUTPUTS))
        with tempfile.TemporaryDirectory() as d:
            written = renderer.write_outputs(d, artifacts)
            self.assertEqual(sorted(written), sorted(renderer.OUTPUTS))
            for name in renderer.OUTPUTS:
                json.loads((Path(d) / name).read_text(encoding="utf-8"))


class CliBehaviourTests(unittest.TestCase):
    def test_dry_run_does_not_write(self):
        with mock.patch.object(renderer, "write_outputs") as w:
            rc = compile_policy_bundle.main(["--dry-run", "--strict"])
        self.assertEqual(rc, 0)
        w.assert_not_called()

    def test_write_flag_calls_write_outputs(self):
        with mock.patch.object(renderer, "write_outputs", return_value=list(renderer.OUTPUTS)) as w:
            rc = compile_policy_bundle.main(["--write"])
        self.assertEqual(rc, 0)
        w.assert_called_once()


class StatusDriftTests(unittest.TestCase):
    def test_active_docs_do_not_reopen_policy_bundle(self):
        active_docs = [
            ROOT / "wiki" / "ops" / "transformation-map.md",
            ROOT / "wiki" / "index.md",
            ROOT / "CLAUDE.md",
        ]
        stale_phrases = [
            "Policy Bundle (P2) is next wedge",
            "Next wedge: Policy Bundle",
            "(1) Policy Bundle",
            "| Policy Bundle Compiler | (subset of Website Logic Bundle) | FUTURE | P2 |",
            "| Policy bundle | `wiki/ops/policy-source-ownership.md`, products/packages-overview, website/faq-master | brand-voice | (planned)",
        ]
        for path in active_docs:
            text = path.read_text(encoding="utf-8")
            for phrase in stale_phrases:
                self.assertNotIn(phrase, text, msg=f"{path} reopens shipped Policy Bundle: {phrase}")

    def test_jvto_web_sync_handoff_exists_with_gate(self):
        handoff = ROOT / "output" / "website" / "policy-bundle" / "JVTO_WEB_SYNC_HANDOFF.md"
        template = ROOT / "docs" / "templates" / "sync-policy-bundle.mjs"
        handoff_text = handoff.read_text(encoding="utf-8")
        template_text = template.read_text(encoding="utf-8")
        self.assertIn('manifest.schema_version === "policy-bundle/v2.0"', handoff_text)
        self.assertIn("manifest.clean === true", handoff_text)
        self.assertIn('const REQUIRED_SCHEMA = "policy-bundle/v2.0";', template_text)
        self.assertIn("website_checkout", template_text)
        self.assertIn("booking_portal", template_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
