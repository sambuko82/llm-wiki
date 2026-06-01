---
name: entrypoint-router
description: Routes Claude's reading at the start of any llm-wiki session or broad analysis request. Use when a session opens in the llm-wiki repo with no specific task, or when the user asks "analyze this repo", "what's in here", "give me an overview", "where do I start". Returns the minimum sufficient read set sized to the task — small tasks stay small. Does NOT generate content, does NOT classify individual files (that's cleanup-governor), does NOT decide archive vs delete (that's archive-vs-delete).
---

# llm-wiki Entry Point Router

Your only job: stop Claude from reading the repo broadly. Return the **minimum sufficient** read set — the smallest set the task actually requires — then hand off.

"Minimum sufficient" means: read the fewest files that let the current task succeed. Do not add files in case they're needed. Do not expand to the full 8-anchor list out of habit. A small task gets a small read set. A broad task gets a larger one only if the task evidence justifies it.

## Activation guard

Require `CLAUDE.md` mentioning JVTO / llm-wiki. Otherwise no-op.

## Sizing the read set

Use the user's task phrasing (or the absence of one) to pick a tier:

### Tier 0 — No task stated yet (2 files)

Return only:
1. `CLAUDE.md` — project contract
2. `wiki/index.md` — content catalog

Then ask the single follow-up question (see below) and stop. Do not pre-load anchors 3–8.

### Tier 1 — Specific small-scope task named (2–3 files)

Examples: "fix a typo in the homepage copy", "check today's log entry", "look up the Ijen screening fee".

Return Tier 0 plus the **one** file most likely to contain the answer. Use `wiki/index.md` to identify it. Do not add ops/, transformation-map, HANDOFF, etc. unless the file you identified explicitly references them.

### Tier 2 — Cleanup / audit / consolidation task (4 files)

Examples: "audit the repo", "what should I archive", "cleanup decision map".

Return:
1. `CLAUDE.md`
2. `wiki/index.md`
3. `wiki/ops/transformation-map.md`
4. `wiki/log.md` (last ~200 lines only)

This is the cleanup bootstrap. `bundle-taxonomy.md` is added only when bundle assignments are in scope.

### Tier 3 — Cross-layer integration task (5–8 files)

Examples: "wire up a new output bundle", "trace a value from raw → wiki → output", "check website context master against schema".

Return the full anchor set as needed: add `wiki/ops/bundle-taxonomy.md`, `output/INDEX.md`, `output/website/HANDOFF.md`, `wiki/website/website-context-master.md` only as the task touches their concerns.

## Ignore by default for this session (always returned)

Do not read unless the user names them:
- `raw/` root files (anything not in `raw/_manifest/`)
- `raw/backoffice/csv/`, `raw/backoffice/dumps/` (PII, gitignored)
- `raw/FINANCE/*.xlsx` (finance tasks only)
- `wiki/sources/*.md` except the anchor sources (resolved at runtime from `wiki/index.md` frontmatter `sources:` field)
- `wiki/log.md` body beyond the last 200 lines
- `tests/fixtures/`, `tests/golden/`
- All `__pycache__/`
- `.obsidian/`, `.codex-run/`, `.firecrawl/`, `.gstack/`, `.playwright-mcp/`, `.pytest_cache/`
- `output/website/schema/*.receipt.md`
- `output/website/trust-bundle/*.json` (locked artifacts)
- `docs/superpowers/plans/`, `docs/superpowers/specs/`
- Anything under any `_archive/` folder

If `CLAUDE.md` has an `## Analysis Defaults` section, merge its ignore list here.

## Then ask, in one short question (Tier 0 only)

"What's the task — audit, safe cleanup, governance check, or specific work in [domain]?"

Do not read beyond the returned tier until the user answers.

## Exceptions

- If the user opens with `/llm-wiki:decision-map`, skip the question, hand off to `cleanup-governor` Mode A (Tier 2 read set).
- If the user opens with `/llm-wiki:cleanup-safe`, require an existing decision map in conversation context; if none, run Mode A first.
- If the user explicitly names a file outside the returned tier, read that file in addition.

## What this skill does NOT do

- Does not expand reads beyond the sized tier
- Does not classify files (`cleanup-governor` does that)
- Does not decide archive vs delete (`archive-vs-delete` does that)
- Does not check drift (`governance-maintainer` does that)
- Does not generate website copy, do brand work, or run compilers
