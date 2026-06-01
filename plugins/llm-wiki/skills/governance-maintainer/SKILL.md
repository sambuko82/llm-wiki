---
name: governance-maintainer
description: Detects drift, clutter, and misplaced additions in llm-wiki after changes are made. Use when the user asks "is this clean", "did this break the layering", "check what changed", "is the repo drifting", or when reviewing a recent commit / PR / batch of edits. Reads git status and recent log entries, then reports drift only. Does NOT execute fixes — surfaces issues with one-line remediation suggestions.
---

# llm-wiki Governance Maintainer

You run after work is done. You catch the patterns that re-introduce confusion: strategy notes landing in `output/`, raw files bypassing the manifest, canonical pages drifting from sources, duplicate concept files appearing.

## Activation guard

Same JVTO / llm-wiki guard as the other skills.

## Inputs

When activated, gather (in order) using the available local shell — `git` syntax is identical across platforms, no shell-specific wrapping needed:
1. `git status` — uncommitted changes
2. `git log --since="1 week ago" --name-status` — recent committed changes
3. Last 50 lines of `wiki/log.md` — declared changes
4. Filesystem scan for newly-created files outside expected paths (use `Glob`)

Stop scanning as soon as you have enough signal. Do not read file contents unless a drift flag fires.

## Drift checks

Run these in order. Report only the ones that fire. All "expected" locations are resolved at runtime from `wiki/ops/transformation-map.md` and `wiki/ops/bundle-taxonomy.md` — do not hardcode them here.

### D1 — New file in `output/` root (not in a bundle subfolder)

Expected layout per `wiki/ops/transformation-map.md` § Output Path Convention: `output/<domain>/<bundle>/`. Any new file matching `output/*.md` or `output/*.html` that is not the `INDEX.md` anchor is drift.

Remediation: "Move to `output/<bundle>/` or archive."

### D2 — New file in `wiki/sources/` without manifest entry

Cross-check every new `wiki/sources/*.md` against `raw/_manifest/raw-files-index.csv`. Missing manifest entry → drift.

Remediation: "Add entry to `raw/_manifest/raw-files-index.csv` or move file out of sources/."

### D3 — Strategy/blueprint/synthesis content in `output/` or `wiki/`

Heuristic: frontmatter `type: blueprint | strategy | synthesis | proposal` outside `docs/superpowers/specs/`. Drift.

Remediation: "Move to `docs/superpowers/specs/` or archive."

### D4 — Duplicate concept signal

Resolve bundle ownership via R-BUNDLE (cleanup-governor skill) for every changed file. If 3+ non-archive files resolve to the same bundle slot for the same concept, drift.

Remediation: "Designate one canonical, archive the rest. Route through `archive-vs-delete`."

### D5 — File at repo root that isn't a documented anchor

Documented roots: every path listed at the repo root in `CLAUDE.md` § Naming Rule Exemptions or in the directory tree at the top of `CLAUDE.md`. Any new repo-root file not on either list is drift.

Remediation: "Move into the matching layer folder (`wiki/`, `output/`, `docs/`, `scripts/`)."

### D6 — Canonical file edited without `last_updated` bump

For every changed `wiki/**/*.md`, check that `last_updated` in the frontmatter matches today's date. Stale frontmatter → drift.

Remediation: "Bump `last_updated` to today, re-run any compiler that consumes the file."

### D7 — Output edited without `wiki/log.md` entry

If files under `output/` changed in the last 24h with no matching log entry, drift.

Remediation: "Append a `[YYYY-MM-DD] compile | <bundle>` entry to `wiki/log.md`."

### D8 — Empty / stub folder added

New folder containing only `.gitkeep` and not registered in `wiki/ops/transformation-map.md` as a planned bundle. Drift.

Remediation: "Either register the bundle in transformation-map or delete the folder."

### D9 — File outside the active path being heavily read or cited

If the user's recent activity references a file under any `_archive/` or in the R-IGNORE set without explicit reason, drift on the analysis side, not the repo side.

Remediation: "Move the file back to active path, OR confirm this is a one-off provenance check."

## Output format

Return a single drift report:

```
Drift checks: D1–D9 run. N flags fired.

[D3] wiki/sources/<file>.md duplicates concept already canonical in wiki/seo/why-jvto-architecture.md.
  → Remediation: archive via /llm-wiki:cleanup-safe Phase B.

[D6] wiki/destinations/kawah-ijen.md edited today, last_updated still 2026-05-28.
  → Remediation: bump last_updated to 2026-06-01.

Clean: D1, D2, D4, D5, D7, D8, D9.
```

If nothing fires: "Drift checks: 9/9 clean."

## What this skill does NOT do

- Does not classify (`cleanup-governor`)
- Does not route reads (`entrypoint-router`)
- Does not decide archive vs delete (`archive-vs-delete`)
- Does not execute fixes — only reports
