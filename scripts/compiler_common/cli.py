"""Shared --dry-run/--write/--verbose/--strict argparse scaffold.

Used by compile_packages.py and compile_policy_bundle.py, which had
byte-identical flag definitions apart from the parser description and the
--write/--verbose help text.
"""
from __future__ import annotations

import argparse


def build_dry_run_write_parser(
    description: str,
    write_help: str,
    verbose_help: str,
) -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("--dry-run", action="store_true",
                    help="run + report, write nothing (default behaviour)")
    ap.add_argument("--write", action="store_true", help=write_help)
    ap.add_argument("--verbose", action="store_true", help=verbose_help)
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any error-severity finding remains")
    return ap
