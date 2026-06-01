---
name: archive-vs-delete
description: Decides whether a noisy or stale file in llm-wiki should be kept, archived, ignored, or deleted. Use when the user asks "should I delete this", "archive or delete", "is this safe to remove", "what do I do with this file", or when cleanup-governor flags a file as ambiguous. Returns one of four routes with reasoning. Does NOT execute the action — surfaces the decision to the user.
---

# llm-wiki Archive vs Delete Router

You answer one question per file: **keep, archive, ignore, or delete?** You do not execute.

## The four routes

| Route | Definition | When to choose it |
|---|---|---|
| Keep | File stays in active path | It's canonical (per R-CANONICAL), locked (per R-LOCK), or actively cited by an active page |
| Archive | File moves to a `_archive/` subfolder, keeps its original name | Holds provenance, trace, or historical reasoning value; not actively cited; would create noise if left in path |
| Ignore | File stays put but enters the ignore-by-default set (per R-IGNORE) | Cannot be moved (e.g. raw ingest, gitignored cache, contract output), but should not be read in routine sessions |
| Delete | File is removed via git | Empty, broken link, fully redundant with a canonical source, and zero provenance value |

## Decision sequence (apply in this order, stop at the first match)

1. **Resolve the file against R-LOCK** (cleanup-governor skill) → if LOCK, route Keep. Stop.
2. **Resolve against R-CANONICAL** → if it's a canonical domain page or named as a primary entry point in `CLAUDE.md`, route Keep. Stop.
3. **Is the file 0 bytes or pointing to a deleted dependency?**
   - If it's a `.gitkeep` in a folder registered in `wiki/ops/transformation-map.md` as a planned bundle → Keep.
   - Otherwise → Delete candidate. Stop.
4. **Is the file under `raw/`, a cache, or a locked output artifact that cannot be moved?** → Ignore. Stop.
5. **Is the file's content fully absorbed into a canonical wiki page (citation check via `Grep`)?**
   - Does it still hold provenance / verification value? → Archive.
   - Does it hold zero value beyond what's already absorbed? → Delete candidate.
6. **Is the file a duplicate concept of an active canonical file?** (R-BUNDLE resolves owner; if 3+ files share a bundle slot and only one is cited, the others are duplicates.)
   - Newer / better version exists and old version is uncited → Archive.
   - Uncertain → flag as Review later, do not route.
7. **Default if no match** → Review later. Surface to user.

## Provenance check (for steps 5 and 6)

Before routing to Delete, run:
- `Grep` for the filename slug across all of `wiki/`, `output/`, `raw/_manifest/`
- If any active page cites the file by name → demote Delete to Archive
- If only archived pages cite it → Delete is allowed
- If `raw/_manifest/raw-files-index.csv` lists it with `ingest_status=ingested` → Archive (the manifest needs the trace)

## Output format

For each file under review, return a one-row table:

| File | Route | Reason | Next action |
|---|---|---|---|
| `output/faq-2026-05-12-bromo.md` | Delete | 0 bytes; superseded by `output/website/faq/bromo.md` | `/llm-wiki:cleanup-safe` Phase A |
| `wiki/sources/digital-trust-fortress-blueprint.md` | Archive | Absorbed into `wiki/seo/why-jvto-architecture.md` per R-BUNDLE Trust; still cited in `wiki/index.md` for provenance | Move to `wiki/sources/_archive/strategy-syntheses/` |

Never execute. Always end with: "Confirm route(s) before I run cleanup-safe."

## What this skill does NOT do

- Does not produce the full 9-section decision map (`cleanup-governor` does that)
- Does not select the minimum read set (`entrypoint-router` does that)
- Does not act on changes after they happen (`governance-maintainer` does that)
