---
description: Preview a blog post draft in-chat. Renders full content with meta block (slug, SEO title, tags, read time, status).
argument-hint: "<slug> — required, e.g. '2026-06-10-kawah-ijen-complete-guide'"
---

You are running `/llm-wiki:blog-preview`.

Invoke the `llm-wiki:blog-publisher` skill, Phase 2 — PREVIEW.

## Preconditions

1. User must provide a slug argument. If missing, list all drafts from `output/website/blog/_manifest.json` and ask which to preview.
2. File `output/website/blog/<slug>.md` must exist. If not, stop and report.

## Action protocol

1. Read the `.md` file.
2. Render the full preview block as specified in the PREVIEW phase of the skill.
3. After rendering, wait. Do NOT ask "should I publish?" — user will invoke `/llm-wiki:blog-publish` explicitly.

## Hard refusals

- Tidak auto-publish setelah preview.
- Tidak mengubah konten saat preview — hanya membaca dan menampilkan.
