---
name: content-restructure-integrity
description: Keep output/INDEX.md accurate after any output restructuring. Use whenever output files are moved, renamed, added, or deleted ("reorganise output/", "move these pages", "I added/renamed output files"). After the restructure, run `python scripts/verify_output_index.py` and fix output/INDEX.md until it passes. This is a semantic index↔files check — it does not warn on shell commands.
---

# Content Restructure Integrity

The recurring failure is not the shell command used to move files — it is
`output/INDEX.md` going **stale** after files move or new output pages are added
(this happened in the 2026-05-16 output reorganisation). This skill enforces one
invariant: after any change to output topology, `output/INDEX.md` must accurately
reflect the final files, proven by `scripts/verify_output_index.py`.

## Activation guard

Confirm this is the JVTO llm-wiki repo: `CLAUDE.md` exists at the repo root and
mentions "Java Volcano Tour Operator", "JVTO", or "llm-wiki". If not, output the
single line `content-restructure-integrity not active — this does not look like the JVTO llm-wiki repo.`
and stop.

## When to run

Run the validator after you or the user change anything under `output/`:

- move or rename output files,
- add a new output page (blog post, market page, destination, schema, etc.),
- delete or archive an output file.

This is a semantic check, not a command watcher. Do **not** add or rely on warnings
that fire on `sed`, `git mv`, `mv`, or Excel extraction — those flag the tool, not the
invariant. Run the validator instead.

## Procedure

1. Make the restructure changes.
2. Update `output/INDEX.md` so it matches the final files:
   - every catalog entry (the first column of a table) points to a file that exists,
   - every tracked `output/**.md` file appears once, unless it is listed in
     `scripts/output_index_exclude.txt`,
   - no path is indexed twice.
3. Run the validator and fix every reported problem until it prints `in sync`:
   ```bash
   python scripts/verify_output_index.py
   ```
4. Commit. The commit gate (`.claude/settings.json` PreToolUse hook) and CI run the
   same validator, so a stale index blocks the commit and fails the build.

## Reading the output

Each problem is one actionable line:

- `[stale] indexed path does not exist` → fix the path in `output/INDEX.md`, or restore the file.
- `[uncovered] tracked output markdown not in index` → add a catalog row, or add the path
  to `scripts/output_index_exclude.txt` if it is genuinely not catalog content
  (e.g. a `*-schema.receipt.md` artifact).
- `[duplicate] indexed more than once` → remove the extra row.

## What this skill does NOT do

- It does not edit page content, wiki pages, or anything beyond `output/INDEX.md`
  and (when justified) `scripts/output_index_exclude.txt`.
- It does not validate JSON-schema content, in-page link targets, or `wiki/index.md`.
- It does not add command-pattern warnings or block shell commands by name.
