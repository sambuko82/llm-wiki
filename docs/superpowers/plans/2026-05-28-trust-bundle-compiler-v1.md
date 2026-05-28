# Trust Bundle Compiler v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python compiler that transforms JVTO's 9 trust claims (C1–C9) + their evidence + locked decisions into 7 validated JSON files under `output/website/trust-bundle/`, used by `jvto-web` and downstream consumers (AI search, WA tooling, future bundles).

**Architecture:** Staged pipeline (load → enrich → validate → render → atomic write). Pure-parse loader, strict-gate validator (rules F1–F8), pure-emit renderer. Markdown-first: wiki + YAML registries stay in git, JSON output is generated artifact. Manual trigger via `python scripts/compile_trust.py`. No DB, no server, no jvto-web runtime coupling.

**Tech Stack:** Python 3.10+, `pyyaml` (already used in repo), `pytest` (new dev dep). Standard library for everything else (`dataclasses`, `pathlib`, `re`, `json`, `hashlib`, `argparse`, `datetime`).

---

## Reference

- Spec: `C:\Users\JAVA VOLCANO\.claude\plans\aku-ingin-menjadikan-repo-swift-whisper.md`
- Existing pyyaml usage: [scripts/_db.py](../../scripts/_db.py), [scripts/analyze.py](../../scripts/analyze.py)
- Inputs read by loader (6 sources, all read-only):
  - `raw/_manifest/claim-registry.yml`
  - `raw/_manifest/evidence-registry.yml`
  - `raw/_manifest/entity-registry.yml`
  - `raw/_manifest/decision-registry.yml` (new; seeded in Task 3)
  - `raw/_manifest/conflict-log.md` (table format, migrated in Task 2)
  - `wiki/website/aeo-claims.md` (H2 + bold-label narrative blocks)

---

## File Structure

```
scripts/
  compiler/
    __init__.py
    loader.py        # dataclasses + 6 load_* functions, pure parse
    enricher.py      # enrich() joins 5 sources into list[EnrichedClaim]
    validator.py     # ValidationReport + 13 rule checks (F1–F8)
    renderer.py      # 7 render_* functions, pure emit
  compile_trust.py   # CLI orchestrator: load → enrich → validate → render → atomic write

tests/
  __init__.py
  conftest.py        # pytest fixture path helpers
  fixtures/
    minimal-claim-registry.yml
    minimal-evidence-registry.yml
    minimal-entity-registry.yml
    minimal-decision-registry.yml
    minimal-conflict-log.md
    minimal-aeo-claims.md
  golden/
    claims.json
    faq.json
    aeo-snippets.json
    schema/
      organization.json
      faq-page.json
      tourist-trip.json
  test_loader.py
  test_enricher.py
  test_validator.py
  test_renderer.py
  test_compile_e2e.py
  # (output-schema structural checks are folded into test_compile_e2e.py
  # — every output file is loaded via json.loads() in the happy-path test)

raw/_manifest/
  decision-registry.yml   # NEW
  conflict-log.md         # MODIFIED — adds "Affects Claims" column

requirements-dev.txt      # NEW

output/website/trust-bundle/   # generated; .gitignore? no, commit alongside registry changes
  claims.json
  faq.json
  aeo-snippets.json
  schema/
    organization.json
    faq-page.json
    tourist-trip.json
  _manifest.json
```

**Boundaries:**
- `loader.py` does I/O + parsing only. No business logic.
- `enricher.py` is pure data shaping (joins). Takes raw loader output, returns `list[EnrichedClaim]`.
- `validator.py` takes `list[EnrichedClaim]` + locked decisions + conflicts → `ValidationReport`. No I/O.
- `renderer.py` takes validated enriched data → `dict` per output. No I/O.
- `compile_trust.py` is the only module that writes to disk.

---

## Phase 0 — Project Setup (Tasks 1–3)

### Task 1: Create directory skeleton + dev requirements

**Files:**
- Create: `scripts/compiler/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/conftest.py`
- Create: `tests/fixtures/` (directory)
- Create: `tests/golden/schema/` (directory)
- Create: `requirements-dev.txt`

- [ ] **Step 1: Create the directories and empty __init__ files**

```bash
mkdir -p scripts/compiler tests/fixtures tests/golden/schema
touch scripts/compiler/__init__.py tests/__init__.py
```

- [ ] **Step 2: Create `requirements-dev.txt`**

```
pyyaml>=6.0
pytest>=8.0
```

- [ ] **Step 3: Create `tests/conftest.py` with fixture helpers**

```python
"""Shared pytest fixtures and path helpers."""
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GOLDEN_DIR = Path(__file__).resolve().parent / "golden"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def golden_dir() -> Path:
    return GOLDEN_DIR


@pytest.fixture
def repo_root() -> Path:
    return REPO_ROOT
```

- [ ] **Step 4: Install dev deps and verify pytest discovers no tests yet**

Run:
```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```
Expected output contains: `no tests ran`. Exit code 5 (no tests collected) is acceptable.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/__init__.py tests/__init__.py tests/conftest.py requirements-dev.txt
git commit -m "feat(compiler): scaffold scripts/compiler/ and tests/ skeleton"
```

---

### Task 2: Migrate `raw/_manifest/conflict-log.md` to add `Affects Claims` column

The current file is a markdown table with columns: `ID | Detected | Claim A | Source A | Claim B | Source B | Status | Evidence Weight | Resolution`. F4 needs to know which claim a conflict touches. Adding one column keeps the format consistent.

**Files:**
- Modify: `raw/_manifest/conflict-log.md`

- [ ] **Step 1: Read the current table**

```bash
cat raw/_manifest/conflict-log.md
```

- [ ] **Step 2: Edit the header row to insert `Affects Claims` between `Status` and `Evidence Weight`**

Old header:
```
| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Evidence Weight | Resolution |
|----|----------|---------|---------|---------|---------|--------|-----------------|------------|
```

New header:
```
| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Affects Claims | Evidence Weight | Resolution |
|----|----------|---------|---------|---------|---------|--------|----------------|-----------------|------------|
```

- [ ] **Step 3: Update each existing data row to include the new column value**

For CONF-001 (Stefan Loose year/ISBN), affects claim C9 → insert `C9` before `Evidence Weight` column.
For CONF-002 (Madakaripura height), affects claim C5 (destinations narrative referencing tallest waterfall) → insert `C5`.
For CONF-003 (NIB historical vs active), affects claim C8 (legal/license claim) → insert `C8`.

If unsure which claim a conflict affects, use the empty string `` and add a TODO comment line below the table — but for the three current rows, the mapping is:
- CONF-001 → `C9`
- CONF-002 → `C5`
- CONF-003 → `C8`

- [ ] **Step 4: Commit**

```bash
git add raw/_manifest/conflict-log.md
git commit -m "data(manifest): add 'Affects Claims' column to conflict-log for compiler F4"
```

---

### Task 3: Create `raw/_manifest/decision-registry.yml` with seed entries

**Files:**
- Create: `raw/_manifest/decision-registry.yml`

- [ ] **Step 1: Write the seed file**

```yaml
# Decision Registry — JVTO LLM Wiki
# Final locked decisions for static / semi-static data.
# Once a decision is `status: locked`, the Trust Bundle Compiler treats any conflict-log
# entry listed in `resolves_conflicts` as resolved for validator rule F4.
# Compiler v1 only CONSUMES this file. Lock-creation is an operational workflow
# (Sam + LLM in Obsidian).
# last_updated: 2026-05-28

decisions:
  - decision_id: DEC-001
    topic: stefan_loose_year_isbn
    final_value:
      year: 2018
      isbn: "9783770167654"
    status: provisional
    decided_by: Sam
    decided_at: 2026-05-28
    source_basis:
      - jvto_verification_dossier_p10
    applies_to_claims: [C9]
    resolves_conflicts: []
    resolves_dq: [DQ-001]
    notes: >-
      Provisional until Sam confirms via physical book scan. Once confirmed,
      change status to `locked` and add CONF-001 to resolves_conflicts.
```

Note: status is `provisional` (NOT `locked`) because Sam has not yet physically confirmed the book year. This means F4 will still flag CONF-001 — the correct behavior. When Sam confirms, flip status and add CONF-001 to resolves_conflicts.

- [ ] **Step 2: Commit**

```bash
git add raw/_manifest/decision-registry.yml
git commit -m "data(manifest): seed decision-registry.yml with DEC-001 (Stefan Loose)"
```

---

## Phase 1 — Loader (Tasks 4–11)

### Task 4: Define typed dataclasses in `scripts/compiler/loader.py`

**Files:**
- Create: `scripts/compiler/loader.py` (initial dataclass skeleton)
- Test: `tests/test_loader.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_loader.py
"""Loader module tests."""
import pytest


def test_dataclasses_importable():
    """All dataclass types are exported from loader module."""
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, Conflict, AeoFields,
    )
    assert Claim is not None
    assert Evidence is not None
    assert Entity is not None
    assert Decision is not None
    assert Conflict is not None
    assert AeoFields is not None


def test_claim_instantiation():
    from scripts.compiler.loader import Claim
    from datetime import date
    c = Claim(
        claim_id="C1",
        name="Test",
        canonical_text="Body",
        domain="credentials",
        category="trust-signal",
        verification_status="verified",
        wiki_pages=[],
        output_pages=[],
        evidence_ids=["E001"],
        evidence_count=1,
        key_proof_ids=[],
        tags=[],
        last_verified=date(2026, 5, 26),
        stale_after_days=None,
        entity_refs=[],
    )
    assert c.claim_id == "C1"
    assert c.stale_after_days is None
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/test_loader.py -v
```
Expected: ImportError (loader module missing or types missing).

- [ ] **Step 3: Write the dataclass definitions**

```python
# scripts/compiler/loader.py
"""Trust Bundle Compiler — loader module.

Pure parse, no business logic. Reads 6 sources, returns typed dataclasses.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Optional


# ---------- Dataclasses ----------

@dataclass(frozen=True)
class Claim:
    claim_id: str
    name: str
    canonical_text: str
    domain: str
    category: str
    verification_status: str
    wiki_pages: list[str]
    output_pages: list[str]
    evidence_ids: list[str]
    evidence_count: int
    key_proof_ids: list[str]
    tags: list[str]
    last_verified: date
    stale_after_days: Optional[int]    # None → default 90 in validator F1
    entity_refs: list[str]             # may be empty (field not yet present in registry)


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    claim: str                          # back-ref to claim_id (cross-check only)
    source_file: str
    evidence_type_code: int             # raw numeric from YAML
    evidence_type: str                  # mapped slug
    description: str
    verification_status: str
    last_verified: date
    proof_ids: list[str]


@dataclass(frozen=True)
class Entity:
    entity_id: str
    name: str
    type: str
    aliases: list[str]
    wiki_pages: list[str]
    schema_type: Optional[str]
    canonical_url: Optional[str]
    claims: list[str]                   # forward-ref to claim_ids
    tags: list[str]


@dataclass(frozen=True)
class Decision:
    decision_id: str
    topic: str
    final_value: Any                    # scalar or dict
    secondary_facts: Optional[dict]
    status: str                         # locked / provisional / superseded
    decided_by: str
    decided_at: date
    source_basis: list[str]
    applies_to_claims: list[str]
    resolves_conflicts: list[str]
    resolves_dq: list[str]
    superseded_by: Optional[str]
    notes: str


@dataclass(frozen=True)
class Conflict:
    conflict_id: str                    # e.g. CONF-001
    detected: date
    claim_a: str
    source_a: str
    claim_b: str
    source_b: str
    status: str                         # open / resolved
    affects_claims: list[str]           # parsed from new column
    evidence_weight: str
    resolution: str


@dataclass(frozen=True)
class AeoFields:
    claim_id: str
    ai_snippet: str
    short: str
    cs_reply: str
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/test_loader.py -v
```
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py
git commit -m "feat(compiler): define loader dataclasses"
```

---

### Task 5: Implement `load_claims()`

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-claim-registry.yml`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture YAML**

```yaml
# tests/fixtures/minimal-claim-registry.yml
claims:
  - claim_id: C1
    name: Test Claim One
    canonical_text: First test claim body text.
    domain: credentials
    category: trust-signal
    verification_status: verified
    wiki_pages: [wiki/test/one.md]
    output_pages: [output/test/]
    evidence_ids: [E001, E002]
    evidence_count: 2
    key_proof_ids: [proof-a]
    tags: [test, trust-signal]
    last_verified: 2026-05-26

  - claim_id: C2
    name: Test Claim Two
    canonical_text: Second test claim.
    domain: products
    category: tour-package
    verification_status: verified
    wiki_pages: [wiki/test/two.md]
    output_pages: []
    evidence_ids: [E003]
    evidence_count: 1
    key_proof_ids: []
    tags: []
    last_verified: 2026-05-12
    stale_after_days: 30
    entity_refs: [ENT-001]
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_claims_parses_minimal_fixture(fixtures_dir):
    from scripts.compiler.loader import load_claims
    claims = load_claims(fixtures_dir / "minimal-claim-registry.yml")
    assert len(claims) == 2
    assert claims[0].claim_id == "C1"
    assert claims[0].stale_after_days is None
    assert claims[0].entity_refs == []
    assert claims[1].claim_id == "C2"
    assert claims[1].stale_after_days == 30
    assert claims[1].entity_refs == ["ENT-001"]


def test_load_claims_dates_parsed(fixtures_dir):
    from scripts.compiler.loader import load_claims
    from datetime import date
    claims = load_claims(fixtures_dir / "minimal-claim-registry.yml")
    assert claims[0].last_verified == date(2026, 5, 26)
```

- [ ] **Step 3: Run test to verify it fails**

```bash
pytest tests/test_loader.py::test_load_claims_parses_minimal_fixture -v
```
Expected: ImportError on `load_claims`.

- [ ] **Step 4: Implement `load_claims()`**

Append to `scripts/compiler/loader.py`:

```python
import yaml


def _to_date(value: Any) -> date:
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise ValueError(f"Cannot coerce to date: {value!r}")


def load_claims(path: Path) -> list[Claim]:
    """Parse claim-registry.yml → list[Claim]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Claim] = []
    for item in data["claims"]:
        out.append(
            Claim(
                claim_id=item["claim_id"],
                name=item["name"],
                canonical_text=item["canonical_text"],
                domain=item["domain"],
                category=item["category"],
                verification_status=item["verification_status"],
                wiki_pages=list(item.get("wiki_pages") or []),
                output_pages=list(item.get("output_pages") or []),
                evidence_ids=list(item.get("evidence_ids") or []),
                evidence_count=int(item.get("evidence_count", 0)),
                key_proof_ids=list(item.get("key_proof_ids") or []),
                tags=list(item.get("tags") or []),
                last_verified=_to_date(item["last_verified"]),
                stale_after_days=item.get("stale_after_days"),
                entity_refs=list(item.get("entity_refs") or []),
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 4 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-claim-registry.yml
git commit -m "feat(compiler): load_claims() with stale_after_days + entity_refs support"
```

---

### Task 6: Implement `load_evidence()` with numeric→slug type mapping

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-evidence-registry.yml`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture YAML**

```yaml
# tests/fixtures/minimal-evidence-registry.yml
evidence:
  - evidence_id: E001
    claim: C1
    source_file: wiki/test/source-one.md
    evidence_type: 1
    description: Official authority document
    verification_status: verified
    last_verified: 2026-05-25
    proof_ids: [proof-a]

  - evidence_id: E002
    claim: C1
    source_file: wiki/test/source-two.md
    evidence_type: 2
    description: JVTO verified internal
    verification_status: verified
    last_verified: 2026-05-12
    proof_ids: []

  - evidence_id: E003
    claim: C2
    source_file: wiki/test/source-three.md
    evidence_type: 6
    description: Customer review
    verification_status: pending
    last_verified: 2026-05-01
    proof_ids: []
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_evidence_maps_type_codes(fixtures_dir):
    from scripts.compiler.loader import load_evidence
    items = load_evidence(fixtures_dir / "minimal-evidence-registry.yml")
    assert len(items) == 3
    assert items[0].evidence_type_code == 1
    assert items[0].evidence_type == "official_authority"
    assert items[1].evidence_type == "jvto_verified_internal"
    assert items[2].evidence_type == "customer_review"


def test_load_evidence_unknown_type_raises(tmp_path):
    from scripts.compiler.loader import load_evidence
    bad = tmp_path / "bad.yml"
    bad.write_text(
        "evidence:\n"
        "  - evidence_id: E999\n"
        "    claim: C1\n"
        "    source_file: x\n"
        "    evidence_type: 99\n"
        "    description: x\n"
        "    verification_status: verified\n"
        "    last_verified: 2026-05-01\n"
        "    proof_ids: []\n"
    )
    with pytest.raises(ValueError, match="unknown evidence_type"):
        load_evidence(bad)
```

- [ ] **Step 3: Run tests to verify failure**

```bash
pytest tests/test_loader.py::test_load_evidence_maps_type_codes -v
```
Expected: ImportError on `load_evidence`.

- [ ] **Step 4: Implement `load_evidence()`**

Append to `scripts/compiler/loader.py`:

```python
EVIDENCE_TYPE_SLUGS: dict[int, str] = {
    1: "official_authority",
    2: "jvto_verified_internal",
    4: "reputable_media",
    5: "structured_dataset",
    6: "customer_review",
    8: "ai_generated",
}


def load_evidence(path: Path) -> list[Evidence]:
    """Parse evidence-registry.yml → list[Evidence] with numeric→slug type mapping."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Evidence] = []
    for item in data["evidence"]:
        code = int(item["evidence_type"])
        slug = EVIDENCE_TYPE_SLUGS.get(code)
        if slug is None:
            raise ValueError(
                f"unknown evidence_type code {code} for {item['evidence_id']}; "
                f"add it to EVIDENCE_TYPE_SLUGS in loader.py"
            )
        out.append(
            Evidence(
                evidence_id=item["evidence_id"],
                claim=item["claim"],
                source_file=item["source_file"],
                evidence_type_code=code,
                evidence_type=slug,
                description=item["description"],
                verification_status=item["verification_status"],
                last_verified=_to_date(item["last_verified"]),
                proof_ids=list(item.get("proof_ids") or []),
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 6 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-evidence-registry.yml
git commit -m "feat(compiler): load_evidence() with numeric→slug type mapping"
```

---

### Task 7: Implement `load_entities()`

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-entity-registry.yml`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture YAML**

```yaml
# tests/fixtures/minimal-entity-registry.yml
entity_types:
  - destination
  - person

entities:
  - entity_id: ENT-001
    name: Test Destination
    type: destination
    aliases: [Test, Destination]
    wiki_pages: [wiki/destinations/test.md]
    schema_type: TouristAttraction
    canonical_url: /destinations/test
    claims: [C1, C2]
    tags: [test]

  - entity_id: ENT-002
    name: Test Person
    type: person
    aliases: []
    wiki_pages: [wiki/people/test.md]
    claims: [C1]
    tags: []
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_entities(fixtures_dir):
    from scripts.compiler.loader import load_entities
    items = load_entities(fixtures_dir / "minimal-entity-registry.yml")
    assert len(items) == 2
    assert items[0].entity_id == "ENT-001"
    assert items[0].schema_type == "TouristAttraction"
    assert items[0].canonical_url == "/destinations/test"
    assert items[0].claims == ["C1", "C2"]
    assert items[1].schema_type is None
    assert items[1].canonical_url is None
```

- [ ] **Step 3: Run test to verify failure**

```bash
pytest tests/test_loader.py::test_load_entities -v
```
Expected: ImportError on `load_entities`.

- [ ] **Step 4: Implement `load_entities()`**

Append to `scripts/compiler/loader.py`:

```python
def load_entities(path: Path) -> list[Entity]:
    """Parse entity-registry.yml → list[Entity]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Entity] = []
    for item in data["entities"]:
        out.append(
            Entity(
                entity_id=item["entity_id"],
                name=item["name"],
                type=item["type"],
                aliases=list(item.get("aliases") or []),
                wiki_pages=list(item.get("wiki_pages") or []),
                schema_type=item.get("schema_type"),
                canonical_url=item.get("canonical_url"),
                claims=list(item.get("claims") or []),
                tags=list(item.get("tags") or []),
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 7 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-entity-registry.yml
git commit -m "feat(compiler): load_entities()"
```

---

### Task 8: Implement `load_decisions()`

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-decision-registry.yml`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture YAML**

```yaml
# tests/fixtures/minimal-decision-registry.yml
decisions:
  - decision_id: DEC-001
    topic: test_locked_topic
    final_value:
      year: 2018
      isbn: "9783770167654"
    status: locked
    decided_by: Sam
    decided_at: 2026-05-28
    source_basis: [physical_book_check]
    applies_to_claims: [C1]
    resolves_conflicts: [CONF-001]
    resolves_dq: [DQ-001]
    notes: Test locked decision.

  - decision_id: DEC-002
    topic: test_provisional_topic
    final_value: 2015
    secondary_facts:
      related_year: 2016
    status: provisional
    decided_by: Sam
    decided_at: 2026-05-28
    source_basis: [ahu_certificate]
    applies_to_claims: [C2]
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_decisions(fixtures_dir):
    from scripts.compiler.loader import load_decisions
    items = load_decisions(fixtures_dir / "minimal-decision-registry.yml")
    assert len(items) == 2
    assert items[0].decision_id == "DEC-001"
    assert items[0].status == "locked"
    assert items[0].final_value == {"year": 2018, "isbn": "9783770167654"}
    assert items[0].resolves_conflicts == ["CONF-001"]
    assert items[1].status == "provisional"
    assert items[1].final_value == 2015
    assert items[1].secondary_facts == {"related_year": 2016}
    assert items[1].resolves_conflicts == []
    assert items[1].superseded_by is None
```

- [ ] **Step 3: Run test to verify failure**

```bash
pytest tests/test_loader.py::test_load_decisions -v
```
Expected: ImportError on `load_decisions`.

- [ ] **Step 4: Implement `load_decisions()`**

Append to `scripts/compiler/loader.py`:

```python
def load_decisions(path: Path) -> list[Decision]:
    """Parse decision-registry.yml → list[Decision]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Decision] = []
    for item in data["decisions"]:
        out.append(
            Decision(
                decision_id=item["decision_id"],
                topic=item["topic"],
                final_value=item["final_value"],
                secondary_facts=item.get("secondary_facts"),
                status=item["status"],
                decided_by=item["decided_by"],
                decided_at=_to_date(item["decided_at"]),
                source_basis=list(item.get("source_basis") or []),
                applies_to_claims=list(item.get("applies_to_claims") or []),
                resolves_conflicts=list(item.get("resolves_conflicts") or []),
                resolves_dq=list(item.get("resolves_dq") or []),
                superseded_by=item.get("superseded_by"),
                notes=item.get("notes", "") or "",
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 8 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-decision-registry.yml
git commit -m "feat(compiler): load_decisions()"
```

---

### Task 9: Implement `load_conflicts()` — markdown table parser

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-conflict-log.md`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture file**

```markdown
# Conflict Log

*Test fixture conflicts.*

---

| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Affects Claims | Evidence Weight | Resolution |
|----|----------|---------|---------|---------|---------|--------|----------------|-----------------|------------|
| CONF-001 | 2026-05-11 | A1 | src/a | B1 | src/b | open | C1 | W1 | Pending |
| CONF-002 | 2026-05-11 | A2 | src/a2 | B2 | src/b2 | resolved | C1, C2 | W2 | Done |
| CONF-003 | 2026-05-11 | A3 | src/a3 | B3 | src/b3 | open | C2 | W3 | Pending |

---
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_conflicts(fixtures_dir):
    from scripts.compiler.loader import load_conflicts
    items = load_conflicts(fixtures_dir / "minimal-conflict-log.md")
    assert len(items) == 3
    assert items[0].conflict_id == "CONF-001"
    assert items[0].status == "open"
    assert items[0].affects_claims == ["C1"]
    assert items[1].status == "resolved"
    assert items[1].affects_claims == ["C1", "C2"]
    assert items[2].affects_claims == ["C2"]


def test_load_conflicts_empty_affects(tmp_path):
    from scripts.compiler.loader import load_conflicts
    md = tmp_path / "empty.md"
    md.write_text(
        "| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Affects Claims | Evidence Weight | Resolution |\n"
        "|----|----------|---------|---------|---------|---------|--------|----------------|-----------------|------------|\n"
        "| CONF-X | 2026-01-01 | A | s | B | s | open |  | w | r |\n"
    )
    items = load_conflicts(md)
    assert items[0].affects_claims == []
```

- [ ] **Step 3: Run test to verify failure**

```bash
pytest tests/test_loader.py::test_load_conflicts -v
```
Expected: ImportError on `load_conflicts`.

- [ ] **Step 4: Implement `load_conflicts()`**

Append to `scripts/compiler/loader.py`:

```python
import re

_CONFLICT_ROW_RE = re.compile(r"^\|\s*CONF-\d+", re.MULTILINE)


def load_conflicts(path: Path) -> list[Conflict]:
    """Parse the markdown table in conflict-log.md → list[Conflict].

    Expected columns (order matters):
      ID | Detected | Claim A | Source A | Claim B | Source B | Status |
      Affects Claims | Evidence Weight | Resolution
    """
    text = path.read_text(encoding="utf-8")
    out: list[Conflict] = []
    for line in text.splitlines():
        if not _CONFLICT_ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 10:
            raise ValueError(f"conflict row has {len(cells)} cells, expected 10: {line!r}")
        affects = cells[7]
        affects_list = [c.strip() for c in affects.split(",")] if affects else []
        affects_list = [c for c in affects_list if c]
        out.append(
            Conflict(
                conflict_id=cells[0],
                detected=_to_date(cells[1]),
                claim_a=cells[2],
                source_a=cells[3],
                claim_b=cells[4],
                source_b=cells[5],
                status=cells[6],
                affects_claims=affects_list,
                evidence_weight=cells[8],
                resolution=cells[9],
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 10 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-conflict-log.md
git commit -m "feat(compiler): load_conflicts() markdown table parser"
```

---

### Task 10: Implement `load_aeo_narratives()` — markdown H2 + bold-label parser

The real `wiki/website/aeo-claims.md` uses this pattern per claim:
```
## C1 — Safety-Led Operations *(safety)*

**Claim**: ...
**AI snippet**: *...*
**Short**: *...*
**CS reply**: *"..."*
**Evidence**: ...
```

**Files:**
- Modify: `scripts/compiler/loader.py`
- Create: `tests/fixtures/minimal-aeo-claims.md`
- Modify: `tests/test_loader.py`

- [ ] **Step 1: Create the fixture file**

```markdown
# AEO Claims (test fixture)

## C1 — Test Claim One *(safety)*

**Claim**: First claim body.

**Mechanism**:
- m1
- m2

**AI snippet**: *AI snippet text for C1.*

**Short**: *Short for C1.*

**CS reply**: *"CS reply for C1."*

**Evidence**: x. See [[people/x]].

---

## C2 — Test Claim Two *(operational)*

**Claim**: Second claim.

**AI snippet**: *AI snippet for C2.*

**Short**: *Short for C2.*

**CS reply**: *"CS reply for C2."*

**Evidence**: y.

---
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_loader.py`:

```python
def test_load_aeo_narratives(fixtures_dir):
    from scripts.compiler.loader import load_aeo_narratives
    narratives = load_aeo_narratives(fixtures_dir / "minimal-aeo-claims.md")
    assert set(narratives.keys()) == {"C1", "C2"}
    c1 = narratives["C1"]
    assert c1.ai_snippet == "AI snippet text for C1."
    assert c1.short == "Short for C1."
    assert c1.cs_reply == "CS reply for C1."
    c2 = narratives["C2"]
    assert c2.ai_snippet == "AI snippet for C2."
```

- [ ] **Step 3: Run test to verify failure**

```bash
pytest tests/test_loader.py::test_load_aeo_narratives -v
```
Expected: ImportError on `load_aeo_narratives`.

- [ ] **Step 4: Implement `load_aeo_narratives()`**

Append to `scripts/compiler/loader.py`:

```python
_H2_CLAIM_RE = re.compile(r"^##\s+(C\d+)\b", re.MULTILINE)
_FIELD_RE = re.compile(
    r"^\*\*(AI snippet|Short|CS reply)\*\*:\s*\*?\"?(.*?)\"?\*?\s*$",
    re.MULTILINE,
)


def _strip_wrappers(text: str) -> str:
    """Strip leading/trailing `*` italics and `"` quote wrappers if present."""
    text = text.strip()
    while text and text[0] in '*"' and text[-1:] in '*"':
        text = text[1:-1].strip()
    return text


def load_aeo_narratives(path: Path) -> dict[str, AeoFields]:
    """Parse wiki/website/aeo-claims.md → dict[claim_id, AeoFields].

    Splits by H2 headers matching `## C<N>` and extracts three bold-labeled
    fields per block: `AI snippet`, `Short`, `CS reply`.
    """
    text = path.read_text(encoding="utf-8")
    starts = [(m.group(1), m.start()) for m in _H2_CLAIM_RE.finditer(text)]
    starts.append(("__END__", len(text)))
    out: dict[str, AeoFields] = {}
    for i, (cid, pos) in enumerate(starts[:-1]):
        block = text[pos:starts[i + 1][1]]
        fields: dict[str, str] = {}
        for fm in _FIELD_RE.finditer(block):
            fields[fm.group(1)] = _strip_wrappers(fm.group(2))
        out[cid] = AeoFields(
            claim_id=cid,
            ai_snippet=fields.get("AI snippet", ""),
            short=fields.get("Short", ""),
            cs_reply=fields.get("CS reply", ""),
        )
    return out
```

- [ ] **Step 5: Run tests**

```bash
pytest tests/test_loader.py -v
```
Expected: 11 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/compiler/loader.py tests/test_loader.py tests/fixtures/minimal-aeo-claims.md
git commit -m "feat(compiler): load_aeo_narratives() H2 + bold-label parser"
```

---

### Task 11: Implement `enricher.enrich()` — join 5 sources into `EnrichedClaim`

**Files:**
- Create: `scripts/compiler/enricher.py`
- Create: `tests/test_enricher.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_enricher.py
"""Enricher module tests."""
from datetime import date


def _sample_inputs():
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, AeoFields,
    )
    claim_c1 = Claim(
        claim_id="C1", name="One", canonical_text="t1", domain="d", category="c",
        verification_status="verified", wiki_pages=[], output_pages=[],
        evidence_ids=["E001", "E002"], evidence_count=2, key_proof_ids=[],
        tags=[], last_verified=date(2026, 5, 26),
        stale_after_days=None, entity_refs=[],
    )
    e1 = Evidence(
        evidence_id="E001", claim="C1", source_file="x",
        evidence_type_code=1, evidence_type="official_authority",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 25), proof_ids=[],
    )
    e2 = Evidence(
        evidence_id="E002", claim="C1", source_file="y",
        evidence_type_code=2, evidence_type="jvto_verified_internal",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 12), proof_ids=[],
    )
    e_stray = Evidence(
        evidence_id="E999", claim="C1", source_file="z",
        evidence_type_code=6, evidence_type="customer_review",
        description="d", verification_status="verified",
        last_verified=date(2026, 5, 1), proof_ids=[],
    )
    ent = Entity(
        entity_id="ENT-001", name="Ijen", type="destination",
        aliases=[], wiki_pages=[], schema_type="TouristAttraction",
        canonical_url="/d/ijen", claims=["C1"], tags=[],
    )
    dec_locked = Decision(
        decision_id="DEC-001", topic="t", final_value={"x": 1},
        secondary_facts=None, status="locked",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    dec_prov = Decision(
        decision_id="DEC-002", topic="t2", final_value=2015,
        secondary_facts=None, status="provisional",
        decided_by="Sam", decided_at=date(2026, 5, 28),
        source_basis=["x"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    narr = {"C1": AeoFields("C1", "ai", "short", "cs")}
    return [claim_c1], [e1, e2, e_stray], [ent], [dec_locked, dec_prov], narr


def test_enrich_joins_by_claim_evidence_ids():
    """Evidence resolved by claim.evidence_ids (whitelist), not by evidence.claim back-ref."""
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert len(enriched) == 1
    ec = enriched[0]
    assert ec.claim.claim_id == "C1"
    # E999 is excluded because not in claim.evidence_ids even though its back-ref matches
    assert [e.evidence_id for e in ec.evidence] == ["E001", "E002"]


def test_enrich_attaches_locked_decisions_only():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    ec = enriched[0]
    assert [d.decision_id for d in ec.decisions] == ["DEC-001"]


def test_enrich_attaches_entities_by_back_ref():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert [e.entity_id for e in enriched[0].entities] == ["ENT-001"]


def test_enrich_attaches_narrative():
    from scripts.compiler.enricher import enrich
    claims, evidence, entities, decisions, narratives = _sample_inputs()
    enriched = enrich(claims, evidence, entities, decisions, narratives)
    assert enriched[0].narrative.ai_snippet == "ai"
```

- [ ] **Step 2: Run test to verify failure**

```bash
pytest tests/test_enricher.py -v
```
Expected: ImportError on `enrich`.

- [ ] **Step 3: Implement `enricher.py`**

```python
# scripts/compiler/enricher.py
"""Trust Bundle Compiler — enricher module.

Joins loader outputs into EnrichedClaim list. Pure data shaping, no I/O.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from scripts.compiler.loader import (
    Claim, Evidence, Entity, Decision, AeoFields,
)


@dataclass(frozen=True)
class EnrichedClaim:
    claim: Claim
    evidence: list[Evidence]
    entities: list[Entity]
    decisions: list[Decision]            # locked only
    narrative: Optional[AeoFields]


def enrich(
    claims: list[Claim],
    evidence: list[Evidence],
    entities: list[Entity],
    decisions: list[Decision],
    narratives: dict[str, AeoFields],
) -> list[EnrichedClaim]:
    """Join sources by claim_id. Evidence resolved by claim.evidence_ids (whitelist)."""
    evidence_by_id = {e.evidence_id: e for e in evidence}
    out: list[EnrichedClaim] = []
    for claim in claims:
        ev = [evidence_by_id[eid] for eid in claim.evidence_ids if eid in evidence_by_id]
        ents = [e for e in entities if claim.claim_id in e.claims]
        decs = [
            d for d in decisions
            if d.status == "locked" and claim.claim_id in d.applies_to_claims
        ]
        narr = narratives.get(claim.claim_id)
        out.append(EnrichedClaim(claim=claim, evidence=ev, entities=ents, decisions=decs, narrative=narr))
    return out
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_enricher.py -v
```
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/enricher.py tests/test_enricher.py
git commit -m "feat(compiler): enricher.enrich() joins 5 sources into EnrichedClaim"
```

---

## Phase 2 — Validator (Tasks 12–19)

### Task 12: Validator skeleton — `ValidationReport`, `Violation`, `run()` shell

**Files:**
- Create: `scripts/compiler/validator.py`
- Create: `tests/test_validator.py`

- [ ] **Step 1: Write the failing test**

```python
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
```

- [ ] **Step 2: Run test to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: ImportError.

- [ ] **Step 3: Implement skeleton**

```python
# scripts/compiler/validator.py
"""Trust Bundle Compiler — validator module.

Strict gate. Takes enriched claims + decisions + conflicts + narratives,
returns ValidationReport with rule violations F1..F8.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

from scripts.compiler.loader import Decision, Conflict, AeoFields
from scripts.compiler.enricher import EnrichedClaim


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class Violation:
    rule_id: str
    severity: Severity
    target_id: str                     # claim_id, decision_id, or conflict_id
    message: str


@dataclass
class ValidationReport:
    violations: list[Violation] = field(default_factory=list)

    @property
    def errors(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == Severity.ERROR]

    @property
    def warnings(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == Severity.WARNING]

    @property
    def has_errors(self) -> bool:
        return any(v.severity == Severity.ERROR for v in self.violations)

    def rule_summary(self) -> dict[str, str]:
        """Map rule prefix → 'pass' / 'N errors' / 'M warnings'."""
        rule_status: dict[str, dict[str, int]] = {}
        for v in self.violations:
            prefix = v.rule_id.rstrip("abcd")  # F2a → F2
            bucket = rule_status.setdefault(prefix, {"error": 0, "warning": 0})
            bucket[v.severity.value] += 1
        out: dict[str, str] = {}
        for rule in ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"):
            if rule not in rule_status:
                out[rule] = "pass"
            else:
                b = rule_status[rule]
                parts = []
                if b["error"]:
                    parts.append(f"{b['error']} errors")
                if b["warning"]:
                    parts.append(f"{b['warning']} warnings")
                out[rule] = ", ".join(parts) if parts else "pass"
        return out


def run(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    narratives: dict[str, AeoFields],
    all_claim_ids: set[str],
    today: Optional[date] = None,
) -> ValidationReport:
    """Run all rules F1..F8 and return a single ValidationReport."""
    if today is None:
        today = date.today()
    report = ValidationReport()
    # Rules added by Tasks 13–19.
    return report
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator skeleton — ValidationReport, Violation, run()"
```

---

### Task 13: Rule F1 — freshness check (`last_verified` ≤ stale_after_days or 90)

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_validator.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 4 new tests fail (rule not implemented).

- [ ] **Step 3: Implement F1 inside `run()`**

In `scripts/compiler/validator.py`, replace the body of `run()`:

```python
def run(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    narratives: dict[str, AeoFields],
    all_claim_ids: set[str],
    today: Optional[date] = None,
) -> ValidationReport:
    if today is None:
        today = date.today()
    report = ValidationReport()
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
    return report


def _check_f1_freshness(ec: EnrichedClaim, today: date, report: ValidationReport) -> None:
    window = ec.claim.stale_after_days if ec.claim.stale_after_days is not None else 90
    age_days = (today - ec.claim.last_verified).days
    if age_days > window:
        report.violations.append(
            Violation(
                rule_id="F1",
                severity=Severity.ERROR,
                target_id=ec.claim.claim_id,
                message=(
                    f"stale: last_verified {ec.claim.last_verified} is {age_days} days old "
                    f"(limit {window})"
                ),
            )
        )
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F1 freshness rule (default 90, per-claim override)"
```

---

### Task 14: Rules F2a, F2b, F2c — evidence chain integrity

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_validator.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 3 new tests fail.

- [ ] **Step 3: Implement F2 family**

Add to `scripts/compiler/validator.py`:

```python
def _check_f2_evidence(ec: EnrichedClaim, report: ValidationReport) -> None:
    declared = ec.claim.evidence_ids
    resolved_ids = {e.evidence_id for e in ec.evidence}

    # F2a: at least one evidence_id declared
    if not declared:
        report.violations.append(
            Violation("F2a", Severity.ERROR, ec.claim.claim_id,
                      "claim has no evidence_ids declared")
        )

    # F2b: every declared id resolves
    for eid in declared:
        if eid not in resolved_ids:
            report.violations.append(
                Violation("F2b", Severity.ERROR, ec.claim.claim_id,
                          f"evidence_id {eid} declared but not found in evidence-registry")
            )

    # F2c: every resolved evidence is verified
    for e in ec.evidence:
        if e.verification_status != "verified":
            report.violations.append(
                Violation("F2c", Severity.ERROR, ec.claim.claim_id,
                          f"evidence {e.evidence_id} has status={e.verification_status!r}, expected 'verified'")
            )
```

And call it in `run()`:

```python
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
        _check_f2_evidence(ec, report)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 10 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F2a/F2b/F2c evidence chain rules"
```

---

### Task 15: Rule F3 — entity reference coverage (warning-only)

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 2 new tests fail (signature mismatch or rule missing).

- [ ] **Step 3: Update `run()` to accept `known_entity_ids` and implement F3**

Update `run()` signature:

```python
def run(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    narratives: dict[str, AeoFields],
    all_claim_ids: set[str],
    today: Optional[date] = None,
    known_entity_ids: Optional[set[str]] = None,
) -> ValidationReport:
    if today is None:
        today = date.today()
    if known_entity_ids is None:
        known_entity_ids = set()
    report = ValidationReport()
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
        _check_f2_evidence(ec, report)
        _check_f3_entities(ec, known_entity_ids, report)
    return report


def _check_f3_entities(ec: EnrichedClaim, known: set[str], report: ValidationReport) -> None:
    for eid in ec.claim.entity_refs:
        if eid not in known:
            report.violations.append(
                Violation("F3", Severity.WARNING, ec.claim.claim_id,
                          f"entity_ref {eid} unresolved in entity-registry")
            )
```

Also update older tests that called `run()` without `known_entity_ids` — they still work because of the default, but update by passing the keyword if needed.

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 12 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F3 entity coverage (warning-only)"
```

---

### Task 16: Rule F4 — conflict touches claim AND no locked decision covers it

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 4 new tests fail.

- [ ] **Step 3: Implement F4**

Add to `scripts/compiler/validator.py`:

```python
def _check_f4_conflicts(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    report: ValidationReport,
) -> None:
    # Build set of conflict_ids resolved by locked decisions
    locked_resolves: set[str] = set()
    for d in decisions:
        if d.status == "locked":
            locked_resolves.update(d.resolves_conflicts)

    enriched_ids = {ec.claim.claim_id for ec in enriched_claims}
    for c in conflicts:
        if c.status != "open":
            continue
        for cid in c.affects_claims:
            if cid not in enriched_ids:
                continue
            if c.conflict_id in locked_resolves:
                continue
            report.violations.append(
                Violation("F4", Severity.ERROR, cid,
                          f"unresolved conflict {c.conflict_id} touches {cid} and no locked decision covers it")
            )
```

Call once after the per-claim loop:

```python
    _check_f4_conflicts(enriched_claims, decisions, conflicts, report)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 16 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F4 conflict+lock rule"
```

---

### Task 17: Rule F5 — every claim has matching narrative

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 3 new tests fail.

- [ ] **Step 3: Implement F5**

```python
def _check_f5_narratives(ec: EnrichedClaim, report: ValidationReport) -> None:
    n = ec.narrative
    if n is None:
        report.violations.append(
            Violation("F5", Severity.ERROR, ec.claim.claim_id,
                      "no narrative block found in aeo-claims.md")
        )
        return
    missing = [f for f in ("ai_snippet", "short", "cs_reply") if not getattr(n, f)]
    if missing:
        report.violations.append(
            Violation("F5", Severity.ERROR, ec.claim.claim_id,
                      f"narrative missing fields: {', '.join(missing)}")
        )
```

Call in per-claim loop:

```python
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
        _check_f2_evidence(ec, report)
        _check_f3_entities(ec, known_entity_ids, report)
        _check_f5_narratives(ec, report)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 19 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F5 narrative completeness"
```

---

### Task 18: Rules F6 + F7 — cross-check warnings

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 2 new tests fail.

- [ ] **Step 3: Implement F6 + F7**

```python
def _check_f6_f7_crosschecks(ec: EnrichedClaim, report: ValidationReport) -> None:
    # F6: every resolved evidence has back-ref matching this claim's id
    for e in ec.evidence:
        if e.claim != ec.claim.claim_id:
            report.violations.append(
                Violation("F6", Severity.WARNING, ec.claim.claim_id,
                          f"evidence {e.evidence_id} back-ref claim={e.claim!r} but listed under {ec.claim.claim_id}")
            )
    # F7: evidence_count field matches actual count
    if ec.claim.evidence_count != len(ec.claim.evidence_ids):
        report.violations.append(
            Violation("F7", Severity.WARNING, ec.claim.claim_id,
                      f"evidence_count={ec.claim.evidence_count} but len(evidence_ids)={len(ec.claim.evidence_ids)}")
        )
```

Call in per-claim loop:

```python
        _check_f6_f7_crosschecks(ec, report)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 21 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F6/F7 cross-check warnings"
```

---

### Task 19: Rules F8a–F8d — decision integrity

**Files:**
- Modify: `scripts/compiler/validator.py`
- Modify: `tests/test_validator.py`

- [ ] **Step 1: Write failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify failure**

```bash
pytest tests/test_validator.py -v
```
Expected: 5 new tests fail.

- [ ] **Step 3: Implement F8 family**

```python
def _check_f8_decisions(
    decisions: list[Decision],
    conflicts: list[Conflict],
    all_claim_ids: set[str],
    report: ValidationReport,
) -> None:
    conflict_ids = {c.conflict_id for c in conflicts}
    # F8a + F8d per decision
    for d in decisions:
        if not d.source_basis:
            report.violations.append(
                Violation("F8a", Severity.ERROR, d.decision_id,
                          "locked decision has empty source_basis" if d.status == "locked"
                          else "decision has empty source_basis")
            )
        for cid in d.applies_to_claims:
            if cid not in all_claim_ids:
                report.violations.append(
                    Violation("F8d", Severity.ERROR, d.decision_id,
                              f"applies_to_claims references unknown claim {cid}")
                )
        # F8b
        for conf_id in d.resolves_conflicts:
            if conf_id not in conflict_ids:
                report.violations.append(
                    Violation("F8b", Severity.WARNING, d.decision_id,
                              f"resolves_conflicts references unknown conflict {conf_id}")
                )

    # F8c: no two locked on same topic
    locked_by_topic: dict[str, list[str]] = {}
    for d in decisions:
        if d.status == "locked":
            locked_by_topic.setdefault(d.topic, []).append(d.decision_id)
    for topic, ids in locked_by_topic.items():
        if len(ids) > 1:
            report.violations.append(
                Violation("F8c", Severity.ERROR, ids[-1],
                          f"multiple locked decisions on topic {topic!r}: {ids}; use superseded_by to chain")
            )
```

Call once after per-claim loop and F4:

```python
    _check_f8_decisions(decisions, conflicts, all_claim_ids, report)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_validator.py -v
```
Expected: 26 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/validator.py tests/test_validator.py
git commit -m "feat(compiler): validator F8a–F8d decision integrity"
```

---

## Phase 3 — Renderer (Tasks 20–26)

### Task 20: Renderer skeleton + `render_claims()`

**Files:**
- Create: `scripts/compiler/renderer.py`
- Create: `tests/test_renderer.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_renderer.py
"""Renderer module tests."""
from datetime import date


def _enriched_c1():
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, AeoFields,
    )
    from scripts.compiler.enricher import EnrichedClaim
    claim = Claim(
        claim_id="C1", name="Safety-Led Operations",
        canonical_text="Volcano travel is unpredictable.",
        domain="credentials", category="trust-signal",
        verification_status="verified",
        wiki_pages=["wiki/x.md"], output_pages=["output/x"],
        evidence_ids=["E001"], evidence_count=1,
        key_proof_ids=["sprin-polpar"],
        tags=["police-led", "safety"],
        last_verified=date(2026, 5, 26),
        stale_after_days=None, entity_refs=[],
    )
    ev = Evidence(
        evidence_id="E001", claim="C1", source_file="wiki/people/agung-sambuko.md",
        evidence_type_code=2, evidence_type="jvto_verified_internal",
        description="Founder is active Tourist Police officer",
        verification_status="verified",
        last_verified=date(2026, 5, 25),
        proof_ids=["sprin-polpar"],
    )
    dec = Decision(
        decision_id="DEC-001", topic="founding_year",
        final_value=2015, secondary_facts=None,
        status="locked", decided_by="Sam",
        decided_at=date(2026, 5, 28),
        source_basis=["AHU"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    narr = AeoFields("C1", "snippet", "short", "cs reply")
    return EnrichedClaim(claim=claim, evidence=[ev], entities=[], decisions=[dec], narrative=narr)


def test_render_claims_structure():
    from scripts.compiler.renderer import render_claims
    out = render_claims([_enriched_c1()], compiled_at="2026-05-28T00:00:00Z")
    assert out["version"] == "1.0"
    assert out["compiled_at"] == "2026-05-28T00:00:00Z"
    assert len(out["claims"]) == 1
    c = out["claims"][0]
    assert c["id"] == "C1"
    assert c["last_verified"] == "2026-05-26"
    assert c["evidence"][0]["type"] == "jvto_verified_internal"
    assert c["decisions"][0]["decision_id"] == "DEC-001"
    assert c["decisions"][0]["final_value"] == 2015
    assert c["narrative"]["ai_snippet"] == "snippet"
```

- [ ] **Step 2: Run test to verify failure**

```bash
pytest tests/test_renderer.py -v
```
Expected: ImportError.

- [ ] **Step 3: Implement `render_claims()`**

```python
# scripts/compiler/renderer.py
"""Trust Bundle Compiler — renderer module.

Pure emission. Takes enriched + validated data, returns dicts ready for json.dump.
"""
from __future__ import annotations

from typing import Any

from scripts.compiler.enricher import EnrichedClaim
from scripts.compiler.loader import Entity


_BUNDLE_VERSION = "1.0"
_COMPILER_VERSION = "0.1.0"


def render_claims(enriched: list[EnrichedClaim], compiled_at: str) -> dict[str, Any]:
    """Build claims.json structure."""
    return {
        "version": _BUNDLE_VERSION,
        "compiled_at": compiled_at,
        "claims": [_render_one_claim(ec) for ec in enriched],
    }


def _render_one_claim(ec: EnrichedClaim) -> dict[str, Any]:
    return {
        "id": ec.claim.claim_id,
        "name": ec.claim.name,
        "canonical_text": ec.claim.canonical_text,
        "domain": ec.claim.domain,
        "category": ec.claim.category,
        "last_verified": ec.claim.last_verified.isoformat(),
        "evidence": [
            {
                "id": e.evidence_id,
                "type": e.evidence_type,
                "source_file": e.source_file,
                "description": e.description,
                "proof_ids": e.proof_ids,
            }
            for e in ec.evidence
        ],
        "narrative": {
            "ai_snippet": ec.narrative.ai_snippet if ec.narrative else "",
            "short": ec.narrative.short if ec.narrative else "",
            "cs_reply": ec.narrative.cs_reply if ec.narrative else "",
        },
        "decisions": [
            {
                "decision_id": d.decision_id,
                "topic": d.topic,
                "final_value": d.final_value,
                "decided_at": d.decided_at.isoformat(),
            }
            for d in ec.decisions
        ],
        "tags": ec.claim.tags,
    }
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_claims()"
```

---

### Task 21: `render_organization_schema()` — JSON-LD TravelAgency

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write the failing test**

```python
def test_render_organization_schema():
    from scripts.compiler.renderer import render_organization_schema
    org = render_organization_schema(
        legal_name="PT Java Volcano Rendezvous",
        brand_name="Java Volcano Tour Operator",
        nib="1102230032918",
        tdup="1102230032918",
        founder_name="Agung Sambuko",
        founder_job="Tourist Police Officer",
        url="https://javavolcano-touroperator.com",
    )
    assert org["@context"] == "https://schema.org"
    assert org["@type"] == "TravelAgency"
    assert org["legalName"] == "PT Java Volcano Rendezvous"
    identifiers = {i["propertyID"]: i["value"] for i in org["identifier"]}
    assert identifiers["NIB"] == "1102230032918"
    assert identifiers["TDUP"] == "1102230032918"
    assert org["founder"]["name"] == "Agung Sambuko"
```

- [ ] **Step 2: Run test to verify failure**

```bash
pytest tests/test_renderer.py::test_render_organization_schema -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

Append to `scripts/compiler/renderer.py`:

```python
def render_organization_schema(
    legal_name: str,
    brand_name: str,
    nib: str,
    tdup: str,
    founder_name: str,
    founder_job: str,
    url: str,
) -> dict[str, Any]:
    """Build schema/organization.json (JSON-LD TravelAgency)."""
    return {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": brand_name,
        "legalName": legal_name,
        "url": url,
        "identifier": [
            {"@type": "PropertyValue", "propertyID": "NIB", "value": nib},
            {"@type": "PropertyValue", "propertyID": "TDUP", "value": tdup},
        ],
        "founder": {
            "@type": "Person",
            "name": founder_name,
            "jobTitle": founder_job,
        },
    }
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_organization_schema() JSON-LD TravelAgency"
```

---

### Task 22: `render_faq_page_schema()` — JSON-LD FAQPage

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write failing test**

```python
def test_render_faq_page_schema():
    from scripts.compiler.renderer import render_faq_page_schema
    faq = render_faq_page_schema([
        {"question": "Is JVTO licensed?", "answer": "Yes, NIB 1102230032918."},
        {"question": "Do you offer private tours?", "answer": "Yes, all tours are private."},
    ])
    assert faq["@context"] == "https://schema.org"
    assert faq["@type"] == "FAQPage"
    assert len(faq["mainEntity"]) == 2
    q0 = faq["mainEntity"][0]
    assert q0["@type"] == "Question"
    assert q0["name"] == "Is JVTO licensed?"
    assert q0["acceptedAnswer"]["@type"] == "Answer"
    assert q0["acceptedAnswer"]["text"] == "Yes, NIB 1102230032918."
```

- [ ] **Step 2: Run test**

```bash
pytest tests/test_renderer.py::test_render_faq_page_schema -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

```python
def render_faq_page_schema(qa_pairs: list[dict[str, str]]) -> dict[str, Any]:
    """Build schema/faq-page.json (JSON-LD FAQPage)."""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": qa["question"],
                "acceptedAnswer": {"@type": "Answer", "text": qa["answer"]},
            }
            for qa in qa_pairs
        ],
    }
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_faq_page_schema() JSON-LD FAQPage"
```

---

### Task 23: `render_tourist_trip_schema()` — array deduplicated by canonical_url

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write failing test**

```python
def test_render_tourist_trip_schema_dedupes_by_url():
    from scripts.compiler.renderer import render_tourist_trip_schema
    from scripts.compiler.loader import Entity
    entities = [
        Entity("ENT-001", "Kawah Ijen", "destination", [], [],
               "TouristAttraction", "/destinations/ijen-crater", ["C1"], []),
        Entity("ENT-001-dup", "Kawah Ijen", "destination", [], [],
               "TouristAttraction", "/destinations/ijen-crater", ["C4"], []),  # duplicate URL
        Entity("ENT-002", "Mount Bromo", "destination", [], [],
               "TouristAttraction", "/destinations/mount-bromo", ["C1"], []),
        Entity("ENT-003", "Founder Person", "person", [], [],
               "Person", "/people/founder", ["C1"], []),  # not a destination → excluded
    ]
    trips = render_tourist_trip_schema(entities, base_url="https://javavolcano-touroperator.com")
    assert len(trips) == 2  # one per unique destination URL
    urls = [t["url"] for t in trips]
    assert "https://javavolcano-touroperator.com/destinations/ijen-crater" in urls
    assert "https://javavolcano-touroperator.com/destinations/mount-bromo" in urls
    assert all(t["@type"] == "TouristTrip" for t in trips)


def test_render_tourist_trip_excludes_entities_without_url():
    from scripts.compiler.renderer import render_tourist_trip_schema
    from scripts.compiler.loader import Entity
    entities = [
        Entity("ENT-X", "No URL Place", "destination", [], [], "TouristAttraction", None, [], []),
    ]
    trips = render_tourist_trip_schema(entities, base_url="https://x")
    assert trips == []
```

- [ ] **Step 2: Run test**

```bash
pytest tests/test_renderer.py::test_render_tourist_trip_schema_dedupes_by_url -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

```python
def render_tourist_trip_schema(entities: list[Entity], base_url: str) -> list[dict[str, Any]]:
    """Build schema/tourist-trip.json — one TouristTrip per destination, deduplicated by canonical_url.

    Resolves the open sprint item 'Duplicate TouristTrip in tour page JSON-LD schemas'
    by collapsing entities that share a canonical_url into a single entry.
    """
    seen: dict[str, dict[str, Any]] = {}
    for e in entities:
        if e.type != "destination":
            continue
        if not e.canonical_url:
            continue
        key = e.canonical_url
        if key in seen:
            continue
        seen[key] = {
            "@context": "https://schema.org",
            "@type": "TouristTrip",
            "name": e.name,
            "url": base_url.rstrip("/") + e.canonical_url,
        }
    return list(seen.values())
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_tourist_trip_schema() deduped by canonical_url"
```

---

### Task 24: `render_faq()` — short → cs_reply fallback

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write failing test**

```python
def test_render_faq_uses_short_preferred():
    from scripts.compiler.renderer import render_faq
    faq = render_faq([_enriched_c1()])
    assert faq["version"] == "1.0"
    assert len(faq["items"]) == 1
    item = faq["items"][0]
    assert item["question"] == "Safety-Led Operations"
    assert item["answer"] == "short"
    assert item["source_claim_id"] == "C1"


def test_render_faq_falls_back_to_cs_reply_when_short_empty():
    from scripts.compiler.renderer import render_faq
    from scripts.compiler.loader import AeoFields
    from scripts.compiler.enricher import EnrichedClaim
    ec = _enriched_c1()
    blank_short = AeoFields("C1", "snippet", "", "cs reply")
    ec2 = EnrichedClaim(claim=ec.claim, evidence=ec.evidence, entities=ec.entities,
                        decisions=ec.decisions, narrative=blank_short)
    faq = render_faq([ec2])
    assert faq["items"][0]["answer"] == "cs reply"
```

- [ ] **Step 2: Run test**

```bash
pytest tests/test_renderer.py::test_render_faq_uses_short_preferred -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

```python
def render_faq(enriched: list[EnrichedClaim]) -> dict[str, Any]:
    """Build faq.json. Answer prefers narrative.short, falls back to narrative.cs_reply."""
    items: list[dict[str, Any]] = []
    for ec in enriched:
        n = ec.narrative
        if n is None:
            continue
        answer = n.short if n.short else n.cs_reply
        items.append({
            "question": ec.claim.name,
            "answer": answer,
            "source_claim_id": ec.claim.claim_id,
            "target_pages": ec.claim.output_pages,
        })
    return {"version": _BUNDLE_VERSION, "items": items}
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_faq() with short→cs_reply fallback"
```

---

### Task 25: `render_aeo_snippets()`

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write failing test**

```python
def test_render_aeo_snippets_topic_from_tags():
    from scripts.compiler.renderer import render_aeo_snippets
    snippets = render_aeo_snippets([_enriched_c1()])
    assert snippets["version"] == "1.0"
    assert len(snippets["snippets"]) == 1
    s = snippets["snippets"][0]
    # topic is first tag if any, else claim_id lowercased
    assert s["topic"] == "police-led"
    assert s["tldr"] == "snippet"
    assert s["claim_ids"] == ["C1"]
    assert "FAQPage" in s["use_for"]
```

- [ ] **Step 2: Run test**

```bash
pytest tests/test_renderer.py::test_render_aeo_snippets_topic_from_tags -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

```python
def render_aeo_snippets(enriched: list[EnrichedClaim]) -> dict[str, Any]:
    """Build aeo-snippets.json — AI ingestion TL;DR pack."""
    snippets: list[dict[str, Any]] = []
    for ec in enriched:
        n = ec.narrative
        if n is None or not n.ai_snippet:
            continue
        topic = ec.claim.tags[0] if ec.claim.tags else ec.claim.claim_id.lower()
        snippets.append({
            "topic": topic,
            "tldr": n.ai_snippet,
            "claim_ids": [ec.claim.claim_id],
            "use_for": ["llms.txt", "FAQPage", "TL;DR block"],
        })
    return {"version": _BUNDLE_VERSION, "snippets": snippets}
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_aeo_snippets()"
```

---

### Task 26: `render_manifest()` — build report

**Files:**
- Modify: `scripts/compiler/renderer.py`
- Modify: `tests/test_renderer.py`

- [ ] **Step 1: Write failing test**

```python
def test_render_manifest_includes_validation_summary():
    from scripts.compiler.renderer import render_manifest
    from scripts.compiler.validator import ValidationReport, Violation, Severity
    rep = ValidationReport(violations=[
        Violation("F3", Severity.WARNING, "C1", "entity ENT-099 unresolved"),
        Violation("F3", Severity.WARNING, "C2", "entity ENT-098 unresolved"),
    ])
    m = render_manifest(
        report=rep,
        inputs={"claims": 9, "evidence": 25, "entities": 50, "decisions": 1, "narratives": 9},
        outputs={"claims": 9, "schema_files": 3, "faq_items": 9, "aeo_snippets": 9},
        input_hashes={"claim-registry.yml": "sha256:abc"},
        compiled_at="2026-05-28T00:00:00Z",
    )
    assert m["compiled_at"] == "2026-05-28T00:00:00Z"
    assert m["compiler_version"] == "0.1.0"
    assert m["inputs"]["claims"] == 9
    assert m["validation"]["F3"] == "2 warnings"
    assert m["validation"]["F1"] == "pass"
```

- [ ] **Step 2: Run test**

```bash
pytest tests/test_renderer.py::test_render_manifest_includes_validation_summary -v
```
Expected: ImportError.

- [ ] **Step 3: Implement**

```python
def render_manifest(
    report,  # ValidationReport (avoid import cycle)
    inputs: dict[str, int],
    outputs: dict[str, int],
    input_hashes: dict[str, str],
    compiled_at: str,
) -> dict[str, Any]:
    """Build _manifest.json — build report."""
    return {
        "compiled_at": compiled_at,
        "compiler_version": _COMPILER_VERSION,
        "inputs": inputs,
        "outputs": outputs,
        "validation": report.rule_summary(),
        "input_hashes": input_hashes,
    }
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/test_renderer.py -v
```
Expected: 9 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/compiler/renderer.py tests/test_renderer.py
git commit -m "feat(compiler): renderer.render_manifest() build report"
```

---

## Phase 4 — CLI + E2E (Tasks 27–29)

### Task 27: CLI `scripts/compile_trust.py` — orchestrator + atomic write + log append

**Files:**
- Create: `scripts/compile_trust.py`

- [ ] **Step 1: Write the orchestrator**

```python
#!/usr/bin/env python3
"""Trust Bundle Compiler — CLI entry.

Reads 6 inputs, validates with strict gate, writes 7 JSON outputs under
output/website/trust-bundle/ via atomic per-file replace.

Usage:
  python scripts/compile_trust.py                # strict mode, real write
  python scripts/compile_trust.py --dry-run      # validate only, no write
  python scripts/compile_trust.py --verbose      # print each violation
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from scripts.compiler.loader import (
    load_claims, load_evidence, load_entities, load_decisions,
    load_conflicts, load_aeo_narratives,
)
from scripts.compiler.enricher import enrich
from scripts.compiler.validator import run as validate, Severity
from scripts.compiler.renderer import (
    render_claims, render_organization_schema, render_faq_page_schema,
    render_tourist_trip_schema, render_faq, render_aeo_snippets,
    render_manifest,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

INPUT_PATHS = {
    "claim-registry.yml": REPO_ROOT / "raw" / "_manifest" / "claim-registry.yml",
    "evidence-registry.yml": REPO_ROOT / "raw" / "_manifest" / "evidence-registry.yml",
    "entity-registry.yml": REPO_ROOT / "raw" / "_manifest" / "entity-registry.yml",
    "decision-registry.yml": REPO_ROOT / "raw" / "_manifest" / "decision-registry.yml",
    "conflict-log.md": REPO_ROOT / "raw" / "_manifest" / "conflict-log.md",
    "aeo-claims.md": REPO_ROOT / "wiki" / "website" / "aeo-claims.md",
}

OUTPUT_DIR = REPO_ROOT / "output" / "website" / "trust-bundle"
LOG_PATH = REPO_ROOT / "wiki" / "log.md"

# JVTO constants (from CLAUDE.md). Hard-coded here intentionally — these are
# the canonical Organization schema fields, not bundle content.
ORG_LEGAL_NAME = "PT Java Volcano Rendezvous"
ORG_BRAND_NAME = "Java Volcano Tour Operator"
ORG_NIB = "1102230032918"
ORG_TDUP = "1102230032918"   # adjust when TDUP gets a distinct number
ORG_FOUNDER_NAME = "Agung Sambuko"
ORG_FOUNDER_JOB = "Tourist Police Officer"
ORG_URL = "https://javavolcano-touroperator.com"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return "sha256:" + h.hexdigest()[:16]


def _atomic_write_json(target: Path, data) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    import os
    os.replace(tmp, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="validate only; do not write outputs")
    parser.add_argument("--verbose", action="store_true",
                        help="print every violation, not just the summary")
    args = parser.parse_args()

    # Load
    claims = load_claims(INPUT_PATHS["claim-registry.yml"])
    evidence = load_evidence(INPUT_PATHS["evidence-registry.yml"])
    entities = load_entities(INPUT_PATHS["entity-registry.yml"])
    decisions = load_decisions(INPUT_PATHS["decision-registry.yml"])
    conflicts = load_conflicts(INPUT_PATHS["conflict-log.md"])
    narratives = load_aeo_narratives(INPUT_PATHS["aeo-claims.md"])

    print(f"Loaded: {len(claims)} claims, {len(evidence)} evidence, "
          f"{len(entities)} entities, {len(decisions)} decisions, "
          f"{len(conflicts)} conflicts, {len(narratives)} narratives", file=sys.stderr)

    # Enrich
    enriched = enrich(claims, evidence, entities, decisions, narratives)

    # Validate
    all_claim_ids = {c.claim_id for c in claims}
    known_entity_ids = {e.entity_id for e in entities}
    report = validate(
        enriched_claims=enriched,
        decisions=decisions,
        conflicts=conflicts,
        narratives=narratives,
        all_claim_ids=all_claim_ids,
        known_entity_ids=known_entity_ids,
    )

    # Report
    summary = report.rule_summary()
    print("Validation:", file=sys.stderr)
    for rule, status in summary.items():
        marker = "✓" if status == "pass" else ("⚠" if "warning" in status and "error" not in status else "✗")
        print(f"  {marker} {rule}: {status}", file=sys.stderr)
    if args.verbose or report.has_errors:
        for v in report.violations:
            print(f"  [{v.rule_id} {v.severity.value}] {v.target_id}: {v.message}", file=sys.stderr)

    if report.has_errors:
        print(f"\n{len(report.errors)} errors, {len(report.warnings)} warnings. "
              f"Strict mode → no output written.", file=sys.stderr)
        return 1

    if args.dry_run:
        print("\n--dry-run: validation passed, no output written.", file=sys.stderr)
        return 0

    # Render
    compiled_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    claims_doc = render_claims(enriched, compiled_at=compiled_at)
    org_doc = render_organization_schema(
        legal_name=ORG_LEGAL_NAME, brand_name=ORG_BRAND_NAME,
        nib=ORG_NIB, tdup=ORG_TDUP,
        founder_name=ORG_FOUNDER_NAME, founder_job=ORG_FOUNDER_JOB,
        url=ORG_URL,
    )
    qa_pairs = [{"question": item["question"], "answer": item["answer"]}
                for item in render_faq(enriched)["items"]]
    faq_page_doc = render_faq_page_schema(qa_pairs)
    trip_doc = render_tourist_trip_schema(entities, base_url=ORG_URL)
    faq_doc = render_faq(enriched)
    aeo_doc = render_aeo_snippets(enriched)
    manifest_doc = render_manifest(
        report=report,
        inputs={
            "claims": len(claims),
            "evidence": len(evidence),
            "entities": len(entities),
            "decisions": len(decisions),
            "narratives": len(narratives),
        },
        outputs={
            "claims": len(claims_doc["claims"]),
            "schema_files": 3,
            "faq_items": len(faq_doc["items"]),
            "aeo_snippets": len(aeo_doc["snippets"]),
        },
        input_hashes={k: _sha256(p) for k, p in INPUT_PATHS.items()},
        compiled_at=compiled_at,
    )

    # Write
    _atomic_write_json(OUTPUT_DIR / "claims.json", claims_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "organization.json", org_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "faq-page.json", faq_page_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "tourist-trip.json", trip_doc)
    _atomic_write_json(OUTPUT_DIR / "faq.json", faq_doc)
    _atomic_write_json(OUTPUT_DIR / "aeo-snippets.json", aeo_doc)
    _atomic_write_json(OUTPUT_DIR / "_manifest.json", manifest_doc)

    # Append log line
    log_line = (
        f"\n## [{compiled_at[:10]}] compile | trust-bundle v0.1.0 — "
        f"{len(claims)} claims, {len(report.errors)} errors, {len(report.warnings)} warnings\n"
    )
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"\nWrote 7 files to {OUTPUT_DIR.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Smoke-run dry-run against current repo**

```bash
python scripts/compile_trust.py --dry-run --verbose
```
Expected: prints Validation summary to stderr; if violations exist, prints each; exits 1 (because DEC-001 is `provisional` so CONF-001 will still trigger F4, and possibly stale data). This is **expected for first run** — the goal is to see the gate working.

- [ ] **Step 3: Commit**

```bash
git add scripts/compile_trust.py
git commit -m "feat(compiler): CLI orchestrator with atomic per-file write + log append"
```

---

### Task 28: E2E test — happy path against synthetic fixtures

**Files:**
- Create: `tests/test_compile_e2e.py`
- Add fixtures: `tests/fixtures/e2e/` directory with clean copies

- [ ] **Step 1: Create the E2E happy-path fixture set**

Create directory `tests/fixtures/e2e/` and add a complete consistent set covering 2 claims, evidence, entities, one locked decision, one resolved conflict, and matching narratives:

`tests/fixtures/e2e/claim-registry.yml`:
```yaml
claims:
  - claim_id: C1
    name: Police-Led
    canonical_text: Founder is active Tourist Police officer.
    domain: credentials
    category: trust-signal
    verification_status: verified
    wiki_pages: [wiki/people/agung.md]
    output_pages: [output/about/]
    evidence_ids: [E001]
    evidence_count: 1
    key_proof_ids: [sprin-polpar]
    tags: [police-led]
    last_verified: 2026-05-26
  - claim_id: C2
    name: Private Tours
    canonical_text: All tours are private.
    domain: products
    category: tour-package
    verification_status: verified
    wiki_pages: [wiki/products.md]
    output_pages: [output/tours/]
    evidence_ids: [E002]
    evidence_count: 1
    key_proof_ids: [nib]
    tags: [private]
    last_verified: 2026-05-26
```

`tests/fixtures/e2e/evidence-registry.yml`:
```yaml
evidence:
  - evidence_id: E001
    claim: C1
    source_file: wiki/people/agung.md
    evidence_type: 2
    description: Founder is active Tourist Police officer
    verification_status: verified
    last_verified: 2026-05-25
    proof_ids: [sprin-polpar]
  - evidence_id: E002
    claim: C2
    source_file: wiki/products.md
    evidence_type: 5
    description: All packages are private
    verification_status: verified
    last_verified: 2026-05-12
    proof_ids: [nib]
```

`tests/fixtures/e2e/entity-registry.yml`:
```yaml
entity_types: [destination]
entities:
  - entity_id: ENT-001
    name: Kawah Ijen
    type: destination
    aliases: [Ijen]
    wiki_pages: [wiki/destinations/ijen.md]
    schema_type: TouristAttraction
    canonical_url: /destinations/ijen-crater
    claims: [C1]
    tags: [destination]
```

`tests/fixtures/e2e/decision-registry.yml`:
```yaml
decisions:
  - decision_id: DEC-001
    topic: test_topic
    final_value: locked_value
    status: locked
    decided_by: Sam
    decided_at: 2026-05-28
    source_basis: [x]
    applies_to_claims: [C1]
    resolves_conflicts: []
```

`tests/fixtures/e2e/conflict-log.md`:
```markdown
| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Affects Claims | Evidence Weight | Resolution |
|----|----------|---------|---------|---------|---------|--------|----------------|-----------------|------------|
| CONF-001 | 2026-05-01 | A | sa | B | sb | resolved | C1 | w | resolved by DEC-001 |
```

`tests/fixtures/e2e/aeo-claims.md`:
```markdown
# Test AEO

## C1 — Police-Led *(safety)*

**Claim**: text.

**AI snippet**: *AI snippet C1.*

**Short**: *Short C1.*

**CS reply**: *"CS C1."*

---

## C2 — Private Tours *(operational)*

**Claim**: text.

**AI snippet**: *AI snippet C2.*

**Short**: *Short C2.*

**CS reply**: *"CS C2."*

---
```

- [ ] **Step 2: Write the E2E happy-path test**

```python
# tests/test_compile_e2e.py
"""End-to-end compile tests using synthetic fixture sets."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _setup_e2e_repo(tmp_path, source_dir):
    """Copy compiler code + fixtures into tmp_path so we get isolated output."""
    work = tmp_path / "work"
    work.mkdir()
    # Copy compiler scripts and tests modules
    shutil.copytree(REPO_ROOT / "scripts", work / "scripts")
    # Layout fixture inputs
    (work / "raw" / "_manifest").mkdir(parents=True)
    (work / "wiki" / "website").mkdir(parents=True)
    src = REPO_ROOT / "tests" / "fixtures" / source_dir
    shutil.copy(src / "claim-registry.yml", work / "raw" / "_manifest" / "claim-registry.yml")
    shutil.copy(src / "evidence-registry.yml", work / "raw" / "_manifest" / "evidence-registry.yml")
    shutil.copy(src / "entity-registry.yml", work / "raw" / "_manifest" / "entity-registry.yml")
    shutil.copy(src / "decision-registry.yml", work / "raw" / "_manifest" / "decision-registry.yml")
    shutil.copy(src / "conflict-log.md", work / "raw" / "_manifest" / "conflict-log.md")
    shutil.copy(src / "aeo-claims.md", work / "wiki" / "website" / "aeo-claims.md")
    (work / "wiki" / "log.md").write_text("# Log\n", encoding="utf-8")
    return work


def test_e2e_happy_path(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}"
    bundle = work / "output" / "website" / "trust-bundle"
    expected = [
        "claims.json",
        "faq.json",
        "aeo-snippets.json",
        "_manifest.json",
        "schema/organization.json",
        "schema/faq-page.json",
        "schema/tourist-trip.json",
    ]
    for rel in expected:
        f = bundle / rel
        assert f.exists(), f"missing output: {rel}"
        # parses as JSON
        json.loads(f.read_text(encoding="utf-8"))
    manifest = json.loads((bundle / "_manifest.json").read_text(encoding="utf-8"))
    assert manifest["inputs"]["claims"] == 2
    assert manifest["validation"]["F1"] == "pass"
    assert manifest["validation"]["F2"] == "pass"
    assert manifest["validation"]["F4"] == "pass"
    # Log was appended
    log_text = (work / "wiki" / "log.md").read_text(encoding="utf-8")
    assert "compile | trust-bundle v0.1.0" in log_text
```

- [ ] **Step 3: Run the test**

```bash
pytest tests/test_compile_e2e.py::test_e2e_happy_path -v
```
Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add tests/test_compile_e2e.py tests/fixtures/e2e/
git commit -m "test(compiler): E2E happy-path against synthetic fixture set"
```

---

### Task 29: E2E test — strict-fail path + atomic-write safety

**Files:**
- Create: `tests/fixtures/e2e-stale/` (mirror of e2e but with one stale claim)
- Modify: `tests/test_compile_e2e.py`

- [ ] **Step 1: Create the stale fixture set**

Duplicate `tests/fixtures/e2e/` to `tests/fixtures/e2e-stale/`. Modify `claim-registry.yml` to set `C1.last_verified: 2025-01-01` (well beyond 90 days from today). Leave everything else identical.

- [ ] **Step 2: Write the failing tests**

Append to `tests/test_compile_e2e.py`:

```python
def test_e2e_strict_fail_writes_nothing(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e-stale")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "F1" in result.stderr
    assert "stale" in result.stderr.lower()
    bundle = work / "output" / "website" / "trust-bundle"
    assert not bundle.exists(), "strict-fail should not write any output"


def test_e2e_dry_run_writes_nothing_even_when_clean(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py", "--dry-run"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0
    bundle = work / "output" / "website" / "trust-bundle"
    assert not bundle.exists(), "dry-run should not write any output"


def test_e2e_atomic_write_leaves_no_tmp_files(tmp_path):
    """A successful run leaves zero .tmp files behind."""
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0
    tmps = list((work / "output").rglob("*.tmp"))
    assert tmps == []
```

- [ ] **Step 3: Run tests**

```bash
pytest tests/test_compile_e2e.py -v
```
Expected: 4 passed (1 from Task 28 + 3 new).

- [ ] **Step 4: Commit**

```bash
git add tests/test_compile_e2e.py tests/fixtures/e2e-stale/
git commit -m "test(compiler): E2E strict-fail + dry-run + atomic-write safety"
```

---

## Phase 5 — Real-Data Verification + Docs Update (Task 30)

### Task 30: Real-data dry-run + fix violations + update wiki/index.md + CLAUDE.md

**Files:**
- Modify: `raw/_manifest/claim-registry.yml` (if F-rules surface fixes)
- Modify: `raw/_manifest/evidence-registry.yml` (if applicable)
- Modify: `raw/_manifest/decision-registry.yml` (lock CONF-002 + CONF-003 when ready)
- Modify: `wiki/index.md` (add Trust Bundle output pointer)
- Modify: `CLAUDE.md` (Current Sprint update)

- [ ] **Step 1: Run dry-run against real data**

```bash
python scripts/compile_trust.py --dry-run --verbose
```
Capture output. Expect violations such as:
- F4 on CONF-001/002/003 because no locked decision resolves them yet (DEC-001 is provisional)
- Possibly F1 if any claim's `last_verified` is older than 90 days
- Possibly F7 if `evidence_count` mismatches actual array length anywhere

- [ ] **Step 2: For each error-severity violation, fix at the source**

For each violation, choose one of these resolutions:
- **F1 stale**: re-verify the claim by inspecting evidence + updating `last_verified` in claim-registry.yml. If the underlying data has not actually been re-checked, do not bump the date — instead, raise the question with Sam.
- **F2b unresolved evidence_id**: either add the missing evidence entry or remove the stale id from the claim.
- **F2c unverified**: change `verification_status: verified` only if you have evidence; otherwise leave the failure and document why.
- **F4 unresolved conflict**: add an entry to `decision-registry.yml` with `status: locked` and the relevant `resolves_conflicts: [CONF-NNN]` IF Sam has confirmed the decision. For CONF-001 (Stefan Loose) leave as `provisional` until the physical book check. For CONF-002/003, ask Sam.
- **F7 count mismatch**: update `evidence_count` field to match `len(evidence_ids)`.
- **F5 missing narrative**: add the H2 block in `wiki/website/aeo-claims.md`.

- [ ] **Step 3: Re-run dry-run until exit 0 or only warnings remain**

```bash
python scripts/compile_trust.py --dry-run --verbose
```

- [ ] **Step 4: Real run (writes output)**

```bash
python scripts/compile_trust.py
```
Expected: exit 0. Inspect `output/website/trust-bundle/_manifest.json`.

- [ ] **Step 5: Validate JSON-LD outputs in Google Rich Results Test**

Open https://search.google.com/test/rich-results in a browser. Paste the content of:
- `output/website/trust-bundle/schema/organization.json` — expect no errors
- `output/website/trust-bundle/schema/faq-page.json` — expect no errors
- One item from `output/website/trust-bundle/schema/tourist-trip.json` — expect no errors

- [ ] **Step 6: Update `wiki/index.md`**

Add a line under a "Compiled Outputs" or appropriate section:
```markdown
- [[output/website/trust-bundle/_manifest|Trust Bundle (compiled)]] — `output/website/trust-bundle/*.json` — Generated by `scripts/compile_trust.py`. Source registries: claim, evidence, entity, decision; conflict log; aeo-claims narrative.
```

- [ ] **Step 7: Update `CLAUDE.md` Current Sprint section**

Replace the **Last completed** line to mention Trust Bundle Compiler v1 shipped, and update **Open items** to remove "Deduplicate TouristTrip in tour page JSON-LD schemas" (now resolved by `schema/tourist-trip.json`).

- [ ] **Step 8: Commit**

```bash
git add raw/_manifest/ wiki/index.md CLAUDE.md output/website/trust-bundle/
git commit -m "feat(compiler): ship Trust Bundle v1 — first compiled output

- Real-data compile passes strict gate
- TouristTrip dedup resolves open sprint item
- wiki/index.md + CLAUDE.md updated"
```

---

## Acceptance Criteria

- [ ] `pytest tests/ -v` reports 100% pass (all unit, enricher, validator, renderer, E2E, and output schema tests).
- [ ] `python scripts/compile_trust.py` exits 0 on current repo state (or, if errors remain, every error has been triaged with Sam and either fixed or documented in `raw/_manifest/decision-queue.md`).
- [ ] All 7 JSON files exist under `output/website/trust-bundle/` and parse as valid JSON.
- [ ] `_manifest.json` shows zero error-severity violations (warnings acceptable).
- [ ] Google Rich Results Test reports no errors for organization, faq-page, and a tourist-trip item.
- [ ] `wiki/log.md` has a compile entry dated today.
- [ ] `output/website/trust-bundle/schema/tourist-trip.json` contains exactly one entry per destination canonical_url.
