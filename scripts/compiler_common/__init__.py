"""Shared primitives for the wiki's compile_*.py entry points.

Extracted 2026-07-06 from scripts/policy_compiler/renderer.py and
scripts/package_compiler/renderer.py, which had byte-identical copies of
`_sha`, `_atomic_write_json`, and `write_outputs`, plus compile_packages.py
and compile_policy_bundle.py sharing an identical --dry-run/--write/--verbose/
--strict argparse scaffold.

scripts/compiler/ (trust bundle) is intentionally NOT unified here — its CLI
surface (no --write/--strict flags) and write strategy (per-call
tempfile.mkstemp vs. Path.with_suffix) already differ, so folding it in would
change trust-bundle's behavior rather than just deduplicate it.
"""
