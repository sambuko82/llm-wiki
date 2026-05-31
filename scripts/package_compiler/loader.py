"""Loaders for the Package Readiness Compiler.

Pure parsing only — read source markdown, extract registry/sitemap tables and
raw text blobs. NO business logic, NO validation here (spec §7: loader).
See wiki/ops/package-readiness-compiler-spec.md.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_BACKTICK = re.compile(r"`([^`]+)`")


@dataclass
class Package:
    number: int | None
    slug: str  # raw slug as written in overview (Bali rows carry a "bali/" prefix)
    name: str
    duration: str
    origin: str  # "surabaya" | "bali"
    ijen_relevant: bool

    @property
    def norm_slug(self) -> str:
        """Slug without the overview's `bali/` prefix — matches sitemap form."""
        return self.slug.split("/", 1)[-1]

    @property
    def public_url(self) -> str:
        if self.origin == "bali":
            return f"/tours/from-bali/{self.norm_slug}"
        return f"/tours/{self.norm_slug}"

    @property
    def visits_madakaripura(self) -> bool:
        return "madakaripura" in self.norm_slug

    @property
    def visits_ijen(self) -> bool:
        return self.ijen_relevant or "ijen" in self.norm_slug


@dataclass
class Sources:
    overview_text: str
    pricing_text: str
    itinerary_text: str
    sitemap_text: str
    routes_text: str
    policy_text: str
    db_export_text: str
    packages: list[Package] = field(default_factory=list)
    sitemap_slugs: dict[str, set] = field(default_factory=dict)  # origin -> {norm slug}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _first_table_after(text: str, header_re: str) -> list[list[str]]:
    """Data rows (lists of cell strings) of the first markdown table that
    appears after a heading matching header_re. Header + separator rows dropped."""
    lines = text.splitlines()
    hdr = re.compile(header_re, re.IGNORECASE)
    n = len(lines)
    i = 0
    while i < n and not hdr.search(lines[i]):
        i += 1
    if i >= n:
        return []
    while i < n and not lines[i].strip().startswith("|"):
        i += 1
    rows: list[list[str]] = []
    seen_sep = False
    while i < n and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if cells and all(c and set(c) <= {"-", ":"} for c in cells):
            seen_sep = True  # separator row
        elif not seen_sep:
            pass  # header row — skip until separator seen
        else:
            rows.append(cells)
        i += 1
    return rows


def parse_registry(overview_text: str) -> list[Package]:
    """Parse the Surabaya + Bali registry tables from packages-overview.md.
    Columns: # | Slug | Name | Duration | Ijen-relevant."""
    packages: list[Package] = []
    for origin, header in (
        ("surabaya", r"^###\s+Surabaya origin"),
        ("bali", r"^###\s+Bali origin"),
    ):
        for cells in _first_table_after(overview_text, header):
            if len(cells) < 5:
                continue
            num = cells[0].strip()
            slug_m = _BACKTICK.search(cells[1])
            slug = slug_m.group(1) if slug_m else cells[1].strip().strip("`")
            packages.append(
                Package(
                    number=int(num) if num.isdigit() else None,
                    slug=slug,
                    name=cells[2].strip(),
                    duration=cells[3].strip(),
                    origin=origin,
                    ijen_relevant=cells[4].strip().upper().startswith("Y"),
                )
            )
    return packages


def parse_sitemap(sitemap_text: str) -> dict[str, set]:
    """Live tour slugs from sitemap-2026-05.md, normalised (no path prefix)."""
    out: dict[str, set] = {"surabaya": set(), "bali": set()}
    for origin, header in (
        ("surabaya", r"^###\s+From Surabaya"),
        ("bali", r"^###\s+From Bali"),
    ):
        for cells in _first_table_after(sitemap_text, header):
            if not cells:
                continue
            m = _BACKTICK.search(cells[0])
            slug = (m.group(1) if m else cells[0]).strip().strip("`")
            slug = slug.split("/", 1)[-1]
            if slug:
                out[origin].add(slug)
    return out


def load_sources(wiki_root: str | Path) -> Sources:
    p = Path(wiki_root)
    src = Sources(
        overview_text=_read(p / "products" / "packages-overview.md"),
        pricing_text=_read(p / "products" / "packages-full-pricing.md"),
        itinerary_text=_read(p / "products" / "packages-itineraries.md"),
        sitemap_text=_read(p / "sources" / "sitemap-2026-05.md"),
        routes_text=_read(p / "sources" / "route-data-csv.md"),
        policy_text=_read(p / "ops" / "policy-source-ownership.md"),
        db_export_text=_read(p / "sources" / "db-export-2026-05.md"),
    )
    src.packages = parse_registry(src.overview_text)
    src.sitemap_slugs = parse_sitemap(src.sitemap_text)
    return src
