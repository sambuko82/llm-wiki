---
description: Preview a JVTO blog draft in chat — renders the full post with metadata header.
argument-hint: "<slug> (e.g. 2026-06-11-kawah-ijen-guide)"
---

You are running `/llm-wiki:blog-preview`.

Invoke the `blog-publisher` skill, Phase 2 — PREVIEW.

## Preconditions

1. The slug argument is required. If not provided, list all posts from `output/website/blog/_manifest.json`.
2. Read `output/website/blog/<slug>.md`.

## Action protocol

Render the post in chat using the preview header block format from the skill. Do not auto-publish after preview.
