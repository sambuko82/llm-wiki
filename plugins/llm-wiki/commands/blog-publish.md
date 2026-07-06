---
description: Publish a blog post draft to production. Runs pre-publish checklist, flips status to published, commits, and pushes to master — triggering jvto-web sync.
argument-hint: "<slug> — required, e.g. '2026-06-10-kawah-ijen-complete-guide'"
---

You are running `/llm-wiki:blog-publish`.

Invoke the `llm-wiki:blog-publisher` skill, Phase 3 — PUBLISH.

## Preconditions

1. User must provide a slug argument. If missing, list all drafts from `_manifest.json` and ask which to publish.
2. The post must have been previewed in this session OR user explicitly says "publish without preview". Never auto-assume preview was done.
3. Run the full pre-publish checklist from the PUBLISH phase. Report any failures and stop.

## Action protocol

1. Run checklist (silently — report only failures).
2. If checklist passes: show a one-line summary — "Akan publish: <title> (<slug>)" — and wait for "ya" / "yes" / explicit confirmation.
3. On confirmation: execute the 5 publish steps (update .md + manifest + log + git add + commit + push).
4. Show the confirmation block after push.

## Hard refusals

- Jangan publish jika ada checklist failure.
- Jangan publish tanpa konfirmasi eksplisit di step 2.
- Jangan push ke branch selain master.
- Jangan publish jika status sudah "published" (idempotency guard).
