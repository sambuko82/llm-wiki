---
description: Start a new JVTO blog post draft. Reads wiki sources, proposes a slug/title/tags, drafts the post, and writes to output/website/blog/.
argument-hint: "[optional: topic or keyword, e.g. 'kawah ijen guide' or 'bromo closure']"
---

You are running `/llm-wiki:blog-create`.

Invoke the `llm-wiki:blog-publisher` skill, Phase 1 — CREATE.

## Preconditions

1. Confirm you are in the llm-wiki repo (`CLAUDE.md` references JVTO / llm-wiki). If not, stop.
2. Read `output/website/blog/_manifest.json` to check existing slugs (avoid duplicates).
3. If the user passed a topic argument, use it. If not, offer the suggested topics list from the skill.

## Action protocol (one-shot — user cukup command ini saja)

1. Select sources (Step 1 of CREATE phase) — list them and wait for confirmation.
2. On confirmation, draft the post and write both files (post `.md` + manifest update + log).
3. Display the full draft in chat.
4. Kirim file output dengan `SendUserFile` (`output/website/blog/<slug>.md`).
5. Tanyakan via `AskUserQuestion`: **Publish sekarang** / **Edit dulu** / **Simpan sebagai draft**.
6. Jika user pilih "Publish sekarang" → langsung jalankan Phase 3 PUBLISH (commit + push). User TIDAK perlu mengetik command publish.

## Hard refusals

- Tidak menulis jika slug sudah ada di `_manifest.json` dengan status "published".
- Tidak menggunakan forbidden phrases dari `output/website/trust-bundle/policies.json`.
- Tidak membuat klaim tanpa wiki source citation.
