"""Tests for the Package Readiness Compiler (v1.1).

Stdlib unittest only — no third-party deps. Runs under either:
    pytest tests/package_compiler/
    python -m unittest discover -s tests/package_compiler
"""
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

import compile_packages  # noqa: E402
from package_compiler import loader, renderer, validator  # noqa: E402


class LoaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)

    def test_parses_16_canonical_packages(self):
        self.assertEqual(len(self.src.packages), 16)

    def test_sitemap_slugs_12_surabaya_4_bali(self):
        self.assertEqual(len(self.src.sitemap_slugs["surabaya"]), 12)
        self.assertEqual(len(self.src.sitemap_slugs["bali"]), 4)

    def test_bali_slug_normalisation_and_url(self):
        bali = [p for p in self.src.packages if p.origin == "bali"]
        self.assertEqual(len(bali), 4)
        for p in bali:
            self.assertFalse(p.norm_slug.startswith("bali/"))
            self.assertTrue(p.public_url.startswith("/tours/from-bali/"))


class ValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)
        cls.findings = validator.validate(cls.src)

    def test_zero_findings_on_clean_source(self):
        self.assertEqual(self.findings, [], msg=f"unexpected findings: {self.findings}")

    def test_no_error_severity(self):
        errors = [f for f in self.findings if f["severity"] == "error"]
        self.assertEqual(errors, [])

    def test_pkg12_flags_injected_forbidden_wording(self):
        bad = loader.load_sources(WIKI)
        bad.overview_text += "\n\nBlue Fire guaranteed every night."
        findings = validator.validate(bad)
        rules = {f["rule_id"] for f in findings}
        self.assertIn("PKG-12", rules)

    def test_pkg11_flags_canonical_exceeding_db(self):
        bad = loader.load_sources(WIKI)
        # shrink the DB packages count below canonical -> error
        bad.db_export_text = bad.db_export_text.replace("`packages` | 22", "`packages` | 5")
        findings = validator.validate(bad)
        pkg11 = [f for f in findings if f["rule_id"] == "PKG-11" and f["severity"] == "error"]
        self.assertTrue(pkg11, msg="PKG-11 should error when canonical > DB count")


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)

    def test_registry_has_16_packages(self):
        reg = renderer.build_registry(self.src)
        self.assertEqual(len(reg), 16)
        self.assertTrue(all("public_url" in r for r in reg))

    def test_manifest_clean_when_no_findings(self):
        man = renderer.build_manifest(self.src, [], dry_run=True)
        self.assertTrue(man["clean"])
        self.assertEqual(man["canonical_package_count"], 16)

    def test_manifest_not_clean_with_error(self):
        err = [{"rule_id": "PKG-01", "severity": "error", "package_id": "x",
                "field": "slug", "wiki_value": None, "reference_value": None,
                "message": "test"}]
        man = renderer.build_manifest(self.src, err, dry_run=True)
        self.assertFalse(man["clean"])

    def test_write_outputs_emits_six_v1_2_files(self):
        artifacts = {
            "package-registry.json": renderer.build_registry(self.src),
            "package-pricing.json": renderer.build_pricing(self.src),
            "package-itineraries.json": renderer.build_itineraries(self.src),
            "booking-compatibility.json": renderer.build_booking_compatibility(self.src),
            "gap-report.json": renderer.build_gap_report([]),
            "_manifest.json": renderer.build_manifest(self.src, [], dry_run=False),
        }
        self.assertEqual(sorted(artifacts), sorted(renderer.OUTPUTS))
        with tempfile.TemporaryDirectory() as d:
            written = renderer.write_outputs(d, artifacts)
            self.assertEqual(sorted(written), sorted(renderer.OUTPUTS))
            for name in renderer.OUTPUTS:
                path = Path(d) / name
                self.assertTrue(path.exists())
                json.loads(path.read_text(encoding="utf-8"))  # valid JSON

    def test_pricing_16_packages_with_tiers(self):
        pricing = renderer.build_pricing(self.src)
        self.assertEqual(len(pricing), 16)
        self.assertTrue(all(p["currency"] == "IDR" for p in pricing))
        self.assertTrue(all(len(p["pax_tiers"]) >= 1 for p in pricing),
                        msg="every package must have >=1 parsed pricing tier")
        bali = [p for p in pricing if "from-bali" not in p["package_id"]
                and p["ferry_included"]]
        self.assertTrue(all(p["ferry_included"] for p in pricing
                            if p["package_id"].startswith("bali/")))

    def test_itineraries_16_packages_with_days(self):
        itins = renderer.build_itineraries(self.src)
        self.assertEqual(len(itins), 16)
        self.assertTrue(all(len(it["days"]) >= 1 for it in itins),
                        msg="every package must have >=1 parsed itinerary day")

    def test_booking_compatibility_all_dual_path(self):
        bc = renderer.build_booking_compatibility(self.src)
        self.assertEqual(len(bc), 16)
        self.assertTrue(all(b["instant_book"] and b["whatsapp_assisted"] for b in bc))

    def test_collision_slug_resolved_by_origin(self):
        # two packages share norm_slug ijen-bromo-madakaripura-3d2n (Surabaya + Bali)
        shared = [p for p in self.src.packages
                  if p.norm_slug == "ijen-bromo-madakaripura-3d2n"]
        self.assertEqual(len(shared), 2)
        rows = {p.origin: loader.detail_for(self.src.pricing_tables, p) for p in shared}
        self.assertIsNotNone(rows["surabaya"])
        self.assertIsNotNone(rows["bali"])


class CliBehaviourTests(unittest.TestCase):
    def test_dry_run_does_not_write(self):
        with mock.patch.object(renderer, "write_outputs") as w:
            rc = compile_packages.main(["--dry-run", "--strict"])
        self.assertEqual(rc, 0)
        w.assert_not_called()

    def test_write_flag_calls_write_outputs(self):
        with mock.patch.object(renderer, "write_outputs", return_value=list(renderer.OUTPUTS)) as w:
            rc = compile_packages.main(["--write"])
        self.assertEqual(rc, 0)
        w.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
