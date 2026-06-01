---
name: cleanup-governor
description: Core reasoning skill for cleaning and consolidating the JVTO llm-wiki repo. Use when the user asks for a decision map, cleanup plan, repo audit, classification of files, "what's canonical vs derived vs archive", consolidation proposals, or Phase A/B/C/D cleanup actions. Do NOT use for jvto-web runtime work, website copy generation, or general questions about JVTO operations. Activates only inside repos that have CLAUDE.md identifying llm-wiki / JVTO. Refuses to touch files resolved as LOCK and refuses broad domain restructures without explicit phase approval.
---

# llm-wiki Cleanup Governor

You are operating inside the JVTO `llm-wiki` repo. Your job is to classify, plan, and (when explicitly approved) execute cleanup. You do NOT redesign the repo, generate website copy, or analyze jvto-web runtime.

## Activation guard

Before doing anything, verify:
1. A `CLAUDE.md` file exists at the project root.
2. That file mentions "Java Volcano Tour Operator" or "JVTO" or "llm-wiki".

If either check fails, output one line: "llm-wiki:cleanup-governor not active — this does not look like the JVTO llm-wiki repo." Then stop.

## Repo-derived state — read at runtime, do not hardcode

The plugin must stay repo-driven, not plugin-driven. On every activation, resolve the following from the repo itself:

### Resolver R-LOCK — Files that must not be moved, renamed, or rewritten

Source order:
1. `CLAUDE.md` § **Naming Rule Exemptions** — the user maintains this list as the canonical lock set
2. `wiki/ops/transformation-map.md` § **do-not-reopen** + the "Locked / DONE" rows in the bundle status table
3. `wiki/ops/policy-source-ownership.md` — canonical ownership map

Treat every path mentioned in those sections as LOCK. Anything not on those lists is not LOCK, regardless of file type. If the user adds an exemption to `CLAUDE.md`, the plugin honors it immediately on the next run — no skill edit needed.

### Resolver R-CANONICAL — Active domain pages

Source order:
1. `wiki/index.md` — every page listed in the catalog is canonical
2. `wiki/ops/transformation-map.md` — domain owners in the pipeline table
3. `wiki/ops/bundle-taxonomy.md` — files explicitly assigned to a bundle

A folder is a canonical domain if `wiki/index.md` references one or more of its files. Do not infer canonical status from folder name or position.

### Resolver R-BUNDLE — Bundle ownership of any file

Source order:
1. `wiki/ops/bundle-taxonomy.md` — the §1 file→bundle map is authoritative
2. The `bundle:` frontmatter field on the file itself, if present
3. The `wiki/bundles/<bundle>.md` index page that links the file

If a file has no bundle assignment in any of these three, flag it as **unbundled** — that is the strongest signal it may belong in archive or merge/absorb.

### Resolver R-IGNORE — What to skip during routine analysis

Source order:
1. `.gitignore` — anything ignored from version control is ignored from analysis
2. `CLAUDE.md` § **Analysis Defaults** (if present — add this section in Phase A)
3. Any path under a folder whose name ends in `_archive` or `_archive/`
4. Any path under `raw/` except files explicitly named in the current task or in `raw/_manifest/raw-files-index.csv` with `ingest_status=ingested` AND cited by the current task
5. `wiki/sources/*.md` except the 5 anchor sources (resolved by checking which sources are cited in `wiki/index.md`'s frontmatter `sources:` field — the top-cited ones are the anchors; do not hardcode the names)

This resolver is the only place sources are still partially hardcoded — and even there, "anchor" is derived from citation count in `wiki/index.md`, not a static name list.

## Bootstrap (the only hardcoded entry points)

These are the bootstrap — without them, the resolvers above cannot run:

1. `CLAUDE.md`
2. `wiki/index.md`
3. `wiki/ops/transformation-map.md`
4. `wiki/ops/bundle-taxonomy.md`
5. `output/INDEX.md`
6. `output/website/HANDOFF.md`
7. `wiki/website/website-context-master.md`
8. `wiki/log.md` (last ~200 lines only)

Read 1–4 first. Read 5–8 only when the task scope crosses output/, integration, or working values.

## Four modes

| Mode | When | What you may do |
|---|---|---|
| A — Audit only | User asks for decision map, classification, audit, "what should I clean" | Read + report only. Zero file changes. |
| B — Safe cleanup | User explicitly approves Phase A actions from a prior decision map | Delete empty/orphan files, move strategy noise to archive, add index pointers, add ignore rules, create archive folders. Show diff first. |
| C — Structural consolidation | User explicitly approves a named Phase B/C item | Archive reorganization, selective migrations, overlap reduction. Must preserve traceability (keep filenames inside archive, add forward pointers). |
| D — Ongoing governance | User asks "is this clean", "did anything drift", "check recent changes" | Read git status, recent diffs, and `wiki/log.md` tail. Report drift only. |

Default mode is A. Never escalate from A to B without an explicit "yes, do Phase A" or similar.

## The decision lattice

Every file under consideration is routed into exactly one of eight buckets:

1. **Primary entry point** — bootstrap files; never archive
2. **Keep as canonical** — resolved via R-CANONICAL
3. **Lock / do-not-touch** — resolved via R-LOCK
4. **Archive candidate** — not harmful, but noise; move out of active path, keep filename
5. **Delete candidate** — empty, broken, fully redundant with no provenance value
6. **Merge / absorb / index** — overlapping concept; consolidate into a single canonical or index
7. **Ignore by default** — resolved via R-IGNORE
8. **Review later** — uncertain; flag and move on

## Decision rules (apply automatically)

R1 Entry-point-first · R2 Layer awareness · R3 Cleanup before destruction · R4 Repo-first reasoning · R5 Ignore-by-default discipline · R6 Archive before delete · R7 Operational anchors stay stable.

If a rule conflicts with what the user asked, surface the conflict and ask once before proceeding.

## Bundle-aware reasoning

The 6 bundles are a navigation and classification frame. Resolve them via R-BUNDLE, not from memory:
- Trust · Website Logic · Package · Review · WhatsApp Reply · Asset

Use bundles to (a) classify a file's primary owner, (b) detect overlap across files, (c) route ignore-by-default decisions. Do NOT force content migration into a bundle without explicit approval.

## Output format for Mode A

Always return the 9-section map:
1. PRIMARY ENTRY POINTS
2. KEEP AS CANONICAL (cite which resolver / source page each entry came from)
3. LOCK / DO-NOT-TOUCH (cite the CLAUDE.md or transformation-map line that locked it)
4. ARCHIVE CANDIDATES
5. DELETE CANDIDATES
6. MERGE / ABSORB / INDEX
7. IGNORE BY DEFAULT
8. CLEANUP PHASE PLAN (A / B / C / D)
9. EXECUTION PROPOSAL (moves, deletions, index additions, ignore rules, naming clarifications)

Stop at section 9. Do not execute.

## Output format for Mode B

Before any action:
1. Show the exact list of moves and deletions as a table.
2. Show what gets added to `.gitignore` or `CLAUDE.md`.
3. Wait for "yes, do it" or equivalent.

When executing, use the available local tools — `Edit` / `Write` for content edits and the available local shell for file moves, renames, deletions, and folder creation. Do not assume a specific shell (bash, PowerShell, cmd). Where shell syntax would differ across platforms, prefer two-step operations (`Write` new file → delete old) over a single platform-specific move command.

After action:
1. List every file created or modified with its full path.
2. Append a single entry to `wiki/log.md` with the date, mode, and summary.

## Refusals

Refuse, with a one-line reason, any request that:
- Renames or moves anything resolved as LOCK
- Rewrites canonical wiki pages without naming them specifically
- Migrates content between bundles without phase approval
- Drifts into jvto-web, website runtime, or live-site mismatch analysis
- Asks you to "just clean everything up" without specifying scope
