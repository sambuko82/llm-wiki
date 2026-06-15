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

    def test_write_outputs_emits_seven_v1_3_files(self):
        artifacts = {
            "package-registry.json": renderer.build_registry(self.src),
            "package-pricing.json": renderer.build_pricing(self.src),
            "package-itineraries.json": renderer.build_itineraries(self.src),
            "package-operational-days.json": renderer.build_operational_days(self.src),
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


class OperationalDaysTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = loader.load_sources(WIKI)
        cls.itins = renderer.build_itineraries(cls.src)
        cls.recs = renderer.build_operational_days(cls.src)

    def _rec(self, package_id, day):
        return next(r for r in self.recs
                    if r["package_id"] == package_id and r["day"] == day)

    def test_covers_all_16_packages(self):
        pkgs = {r["package_id"] for r in self.recs}
        self.assertEqual(len(pkgs), 16)

    def test_day_counts_match_itineraries(self):
        for it in self.itins:
            n = len([r for r in self.recs if r["package_id"] == it["package_id"]])
            self.assertEqual(n, len(it["days"]),
                             msg=f"{it['package_id']} day-count mismatch")

    def test_total_days_equals_sum_of_itinerary_days(self):
        self.assertEqual(len(self.recs), sum(len(it["days"]) for it in self.itins))

    def test_every_record_has_exactly_ten_keys(self):
        allowed = set(renderer.OPERATIONAL_DAY_KEYS)
        for r in self.recs:
            self.assertEqual(set(r.keys()), allowed)

    def test_meal_codes_only_bld(self):
        for r in self.recs:
            for m in r["meal_codes"]:
                self.assertIn(m, ("B", "L", "D"))

    def test_overnight_status_in_enum(self):
        for r in self.recs:
            self.assertIn(r["overnight_status"], renderer.OVERNIGHT_STATUSES)

    def test_no_invented_hotel_labels(self):
        by_key = {(it["package_id"], d["day"]): d["hotel"]
                  for it in self.itins for d in it["days"]}
        for r in self.recs:
            label = r["hotel_label"]
            if label is not None:
                self.assertEqual(label, by_key[(r["package_id"], r["day"])])

    def test_bromo_1d1n_overnight_in_vehicle(self):
        r = self._rec("bromo-1d1n", 1)
        self.assertEqual(r["overnight_status"], "overnight_in_vehicle")
        self.assertIsNone(r["hotel_label"])
        self.assertIn("vehicle", r["notes"].lower())  # original text preserved

    def test_real_hotel_day_classified_hotel(self):
        r = self._rec("bromo-2d1n", 1)
        self.assertEqual(r["overnight_status"], "hotel")
        self.assertEqual(r["hotel_label"], "Joglo Kecombrang Bromo")

    def test_final_null_day_no_overnight(self):
        r = self._rec("bromo-2d1n", 2)
        self.assertEqual(r["overnight_status"], "no_overnight")
        self.assertIsNone(r["hotel_label"])

    def test_no_cost_or_pii_keys(self):
        forbidden = ("cost", "price", "rate", "room", "area", "node",
                     "email", "phone", "whatsapp", "guest", "passenger", "name")
        for r in self.recs:
            for k in r:
                self.assertFalse(any(s in k.lower() for s in forbidden),
                                 msg=f"forbidden key {k}")

    def test_validate_operational_days_clean(self):
        problems = validator.validate_operational_days(self.recs, self.itins)
        self.assertEqual(problems, [], msg=f"unexpected problems: {problems}")

    def test_validator_flags_invented_hotel(self):
        bad = [dict(r) for r in self.recs]
        bad[0]["hotel_label"] = "Totally Invented Resort"
        problems = validator.validate_operational_days(bad, self.itins)
        self.assertTrue(any("not verbatim" in p for p in problems))

    def test_deterministic_bytes(self):
        a = json.dumps(renderer.build_operational_days(self.src),
                       indent=2, ensure_ascii=False)
        b = json.dumps(renderer.build_operational_days(self.src),
                       indent=2, ensure_ascii=False)
        self.assertEqual(a, b)


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
