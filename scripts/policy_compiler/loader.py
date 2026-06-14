"""Load and parse canonical policy bundle sources."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class OwnershipRow:
    domain: str
    canonical_sources: list[str]
    supporting_sources: list[str]
    consumers: list[str]
    notes: str


@dataclass
class DeprecatedRule:
    deprecated: str
    correct: str


@dataclass
class Sources:
    policy_text: str
    packages_text: str
    faq_text: str
    ownership_rows: list[OwnershipRow] = field(default_factory=list)
    deprecated_rules: list[DeprecatedRule] = field(default_factory=list)
    package_sections: dict[str, str] = field(default_factory=dict)
    faq_answers: dict[str, str] = field(default_factory=dict)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _strip_links(value: str) -> str:
    return value.replace("[[", "").replace("]]", "").strip()


def _split_sources(value: str) -> list[str]:
    return [
        _strip_links(part).strip().strip("`")
        for part in value.split(",")
        if part.strip() and part.strip() != "-"
    ]


def _split_consumers(value: str) -> list[str]:
    return [part.strip().lower() for part in value.split(",") if part.strip()]


def _parse_table_after(text: str, heading: str) -> list[list[str]]:
    lines = text.splitlines()
    i = 0
    while i < len(lines) and heading.lower() not in lines[i].lower():
        i += 1
    while i < len(lines) and not lines[i].strip().startswith("|"):
        i += 1
    rows: list[list[str]] = []
    seen_sep = False
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if cells and all(c and set(c) <= {"-", ":"} for c in cells):
            seen_sep = True
        elif seen_sep:
            rows.append(cells)
        i += 1
    return rows


def parse_ownership(policy_text: str) -> list[OwnershipRow]:
    rows: list[OwnershipRow] = []
    for cells in _parse_table_after(policy_text, "Ownership Table"):
        if len(cells) < 5:
            continue
        rows.append(
            OwnershipRow(
                domain=cells[0],
                canonical_sources=_split_sources(cells[1]),
                supporting_sources=_split_sources(cells[2]),
                consumers=_split_consumers(cells[3]),
                notes=cells[4],
            )
        )
    return rows


def parse_deprecated(policy_text: str) -> list[DeprecatedRule]:
    rules: list[DeprecatedRule] = []
    for cells in _parse_table_after(policy_text, "Deprecated / Do Not Use Wording"):
        if len(cells) < 2:
            continue
        deprecated = cells[0].strip()
        quoted = re.match(r'^"([^"]+)"(?:\s*\(.+\))?$', deprecated)
        if quoted:
            deprecated = quoted.group(1)
        else:
            deprecated = deprecated.strip('"')
        rules.append(DeprecatedRule(deprecated=deprecated, correct=cells[1]))
    return rules


def parse_h2_sections(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current:
                out[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = [line]
            continue
        if current:
            buf.append(line)
    if current:
        out[current] = "\n".join(buf).strip()
    return out


def parse_faq_answers(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^\*\*(Q[\w\d]+)\.\s+(.+?)\*\*\s*$", text, re.M))
    out: dict[str, str] = {}
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        qid = match.group(1)
        question = match.group(2).strip()
        answer = text[start:end].strip()
        answer = re.split(r"\n---\n|\n##\s+", answer, maxsplit=1)[0].strip()
        out[qid] = f"{question}\n\n{answer}".strip()
    return out


def load_sources(wiki_root: str | Path) -> Sources:
    p = Path(wiki_root)
    src = Sources(
        policy_text=_read(p / "ops" / "policy-source-ownership.md"),
        packages_text=_read(p / "products" / "packages-overview.md"),
        faq_text=_read(p / "website" / "faq-master.md"),
    )
    src.ownership_rows = parse_ownership(src.policy_text)
    src.deprecated_rules = parse_deprecated(src.policy_text)
    src.package_sections = parse_h2_sections(src.packages_text)
    src.faq_answers = parse_faq_answers(src.faq_text)
    return src
