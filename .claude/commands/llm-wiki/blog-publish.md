---
description: Publish a drafted JVTO blog post to production. Updates status to published, commits, and pushes to master — jvto-web sync picks it up automatically.
argument-hint: "<slug> (e.g. 2026-06-11-kawah-ijen-guide)"
---

You are running `/llm-wiki:blog-publish`.

Invoke the `blog-publisher` skill, Phase 3 — PUBLISH.

## Preconditions

1. The slug argument is required. If not provided, list all draft posts from `output/website/blog/_manifest.json` and ask which to publish.
2. Confirm `output/website/blog/<slug>.md` exists and has `status: "draft"`.

## Action protocol

Run the pre-publish checklist from the skill, then execute publish steps:
1. Update status `draft` → `published` in both `.md` frontmatter and `_manifest.json`
2. Update `generated` timestamp in `_manifest.json`
3. Append to `wiki/log.md`
4. Commit + push to master
5. Confirm with the post-publish summary block from the skill
