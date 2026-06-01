---
description: Execute Phase A (safe) cleanup actions only. Requires a prior decision map and explicit user approval.
argument-hint: "[required: 'phase-a' or 'phase-b <named-item>']"
---

You are running `/llm-wiki:cleanup-safe` in Mode B (Safe cleanup).

Invoke the `llm-wiki:cleanup-governor` skill.

## Preconditions (check before any action)

1. A prior `/llm-wiki:decision-map` output exists in this conversation. If not, run it first and stop.
2. The user passed an argument. If not, ask: "Phase A (all safe items) or Phase B (named item)?"
3. The argument names actions that appeared in the decision map's §9 EXECUTION PROPOSAL. If not, refuse.

## Action protocol

For each action you intend to take:

1. Show the exact action as a table row: `action | source | target | reason`.
2. Group them: moves, deletions, .gitignore additions, CLAUDE.md additions, archive folder creations.
3. Show the full new content of any modified file (CLAUDE.md, .gitignore) as a unified diff.
4. Pause and wait for explicit "yes, do it" or equivalent. Do NOT proceed on silence or ambiguity.
5. On approval, execute using the available local tools:
   - Use `Edit` / `Write` for content changes to `.gitignore`, `CLAUDE.md`, or any markdown file.
   - Use the available local shell (PowerShell, cmd, bash — whatever the environment exposes) for file moves, renames, deletions, and folder creation. Stay environment-agnostic: prefer cross-platform shell idioms or fall back to `Write` + delete pairs where shell syntax would differ.
6. After execution, list every file created or modified with its full path.
7. Append a single entry to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] cleanup-safe | Phase <X>
   Actions: <count>. Files moved: <list>. Files deleted: <list>. Rules added: <list>.
   ```

## Hard refusals

- Refuse any action touching a file the cleanup-governor skill resolves as LOCK (resolved at runtime from `CLAUDE.md` Naming Rule Exemptions + `wiki/ops/transformation-map.md`).
- Refuse any action outside the named phase scope.
- Refuse to delete a file that has any active citation (run `Grep` first across `wiki/` and `output/`).
- Refuse if the user has not seen the diff for `.gitignore` or `CLAUDE.md` edits.
