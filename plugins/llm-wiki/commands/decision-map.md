---
description: Audit-only. Produce the 9-section decision map for the llm-wiki repo. No file changes.
argument-hint: "[optional: scope, e.g. 'wiki/sources only' or 'output/ only']"
---

You are running `/llm-wiki:decision-map` in Mode A (Audit only).

Invoke the `llm-wiki:cleanup-governor` skill.

If the user passed a scope argument, restrict the decision map to that scope. Otherwise, cover the whole repo.

Read only what's needed to produce the 9-section map. Prefer `Glob` and `Grep` over reading every file. Use `CLAUDE.md`, `wiki/index.md`, `wiki/ops/transformation-map.md`, and `wiki/ops/bundle-taxonomy.md` as ground truth for what exists, what's locked, what's canonical, and which bundle owns what — do not assume from prior conversation memory.

Return the 9-section map exactly as specified in the cleanup-governor skill:
1. PRIMARY ENTRY POINTS
2. KEEP AS CANONICAL
3. LOCK / DO-NOT-TOUCH
4. ARCHIVE CANDIDATES
5. DELETE CANDIDATES
6. MERGE / ABSORB / INDEX
7. IGNORE BY DEFAULT
8. CLEANUP PHASE PLAN
9. EXECUTION PROPOSAL

Stop at section 9. Do not execute. Do not write or edit any file. End with: "Stopped here. Confirm phases A/B/C/D before any execution."
