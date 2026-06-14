"""Tests for the Policy Bundle Compiler."""
from __future__ import annotations

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
        self.assertEqual(len(self.src.deprecated_rules), 9)
        self.assertEqual(self.src.deprecated_rules[0].deprecated, "Trip.com booking flow")

    def test_parses_faq_answers(self):
        self.assertIn("Q15", self.src.faq_answers)
        self.assertIn("Website Instant Book", self.src.faq_answers["Q15"])


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)
        cls.policy_bundle = renderer.build_policy_bundle(cls.src)
        cls.consumer_bundles = renderer.build_consumer_bundles(cls.policy_bundle)
        cls.deprecated = renderer.build_deprecated_report(cls.src, cls.consumer_bundles)

    def test_policy_bundle_has_expected_domains(self):
        ids = {p["policy_id"] for p in self.policy_bundle}
        self.assertIn("booking-paths", ids)
        self.assertIn("payment-rules", ids)
        self.assertIn("anti-fraud", ids)

    def test_consumer_bundles_cover_requested_consumers(self):
        self.assertEqual(set(self.consumer_bundles), {"checkout", "invoice", "whatsapp"})
        self.assertIn("payment-rules", self.consumer_bundles["checkout"]["policy_ids"])
        self.assertIn("payment-rules", self.consumer_bundles["invoice"]["policy_ids"])
        self.assertIn("ijen-health-screening", self.consumer_bundles["whatsapp"]["policy_ids"])

    def test_deprecated_report_clean_on_current_sources(self):
        self.assertEqual(self.deprecated["summary"]["total_findings"], 0)
        self.assertTrue(all(c["clean"] for c in self.deprecated["consumers"].values()))

    def test_validator_clean(self):
        findings = validator.validate(self.policy_bundle, self.deprecated)
        self.assertEqual(findings, [])

    def test_deprecated_report_flags_checkout_injected_bad_wording(self):
        bad = loader.load_sources(WIKI)
        bad.package_sections["Payment Rules"] += "\nCash refund available for guest-initiated cancellation."
        bundle = renderer.build_policy_bundle(bad)
        consumers = renderer.build_consumer_bundles(bundle)
        report = renderer.build_deprecated_report(bad, consumers)
        self.assertGreater(report["summary"]["total_findings"], 0)
        self.assertFalse(report["consumers"]["checkout"]["clean"])

    def test_write_outputs_emits_expected_files(self):
        gap = renderer.build_gap_report(self.policy_bundle, self.deprecated)
        artifacts = {
            "policy-bundle.json": self.policy_bundle,
            "consumer-bundles.json": self.consumer_bundles,
            "deprecated-wording-report.json": self.deprecated,
            "gap-report.json": gap,
            "_manifest.json": renderer.build_manifest(self.src, gap, dry_run=False),
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
