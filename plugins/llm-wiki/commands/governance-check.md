---
description: Detect drift, clutter, and misplaced additions in llm-wiki. Reports only, no fixes.
argument-hint: "[optional: 'since <date>' or 'since last commit']"
---

You are running `/llm-wiki:governance-check` in Mode D (Ongoing governance).

Invoke the `llm-wiki:governance-maintainer` skill.

Default scope: last 7 days of changes plus current uncommitted changes. If the user passed a `since` argument, use that instead. Gather git state using the available local shell — `git status` and `git log` syntax is identical on Windows, macOS, and Linux, so no shell-specific wrapping is needed.

Run drift checks D1–D9 from the skill. Report only flags that fire. If none fire, return: "Drift checks: 9/9 clean."

Do NOT fix anything. Do NOT edit any file. Each flag includes a one-line remediation pointing to the appropriate command (`/llm-wiki:cleanup-safe` or manual edit).
