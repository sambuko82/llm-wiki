---
description: Return the minimum sufficient read set for the current task. Run before any broader analysis.
argument-hint: "[optional: task description, e.g. 'finance work' or 'website schema']"
---

You are running `/llm-wiki:analysis-start`.

Invoke the `llm-wiki:entrypoint-router` skill.

Return the **minimum sufficient** read set — not the maximum safe set, not a habitual expansion of anchors. Read the bare minimum the task evidence actually demands. Small tasks must stay small.

If the user passed a task description, size the read set to that description and stop there. If they did not, return only the 2-file bootstrap (CLAUDE.md + wiki/index.md) and ask the single follow-up question. Do not pre-load anchors "in case they're needed".

Do not read beyond the returned set until the user answers or names a specific file. Do not run other skills.
