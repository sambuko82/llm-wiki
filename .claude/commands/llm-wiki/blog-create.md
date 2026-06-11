---
description: Start a new JVTO blog post draft. Reads wiki sources, proposes a slug/title/tags/banner, drafts the post, commits the draft to the current branch, then asks whether to publish.
argument-hint: "[optional: topic or keyword, e.g. 'kawah ijen guide' or 'bromo closure']"
---

You are running `/llm-wiki:blog-create`.

Invoke the `blog-publisher` skill, Phase 1 — CREATE.

## Preconditions

1. Confirm you are in the llm-wiki repo (`CLAUDE.md` references JVTO / llm-wiki). If not, stop.
2. Read `output/website/blog/_manifest.json` to check existing slugs (avoid duplicates).
3. If the user passed a topic argument, use it. If not, offer the suggested topics list from the skill.

## Action protocol

1. Select sources (Step 1 of CREATE phase) — list them and wait for confirmation.
2. On confirmation, draft the post, write both files (post `.md` + manifest update + log entry), and **commit the draft to the current branch** (`git add … && git commit -m "blog | draft | <title>"`). Draft is now in the local repo.
3. Display the full draft in chat.
4. Beritahu lokasi file: `output/website/blog/<slug>.md` sudah tersimpan di repo — dapat dipreview langsung dari filesystem. Tidak perlu SendUserFile.
5. Tanyakan via `AskUserQuestion` (2 pilihan, header "Publish?"):
   - **Publish sekarang** — langsung jalankan Phase 3 PUBLISH (update status → published, push ke master, sync ke jvto-web)
   - **Tidak sekarang** — draft sudah tersimpan di repo lokal; publish nanti via `/llm-wiki:blog-publish <slug>`

## Hard refusals

- Tidak menulis jika slug sudah ada di `_manifest.json` dengan status "published".
- Tidak menggunakan forbidden phrases dari `output/website/trust-bundle/policies.json`.
- Tidak membuat klaim tanpa wiki source citation.
