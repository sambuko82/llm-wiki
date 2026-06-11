---
name: blog-publisher
description: Manages the full JVTO blog lifecycle — draft, preview, publish. Use when the user wants to write a blog post ("write a blog about X", "buat blog tentang X"), preview a draft ("/llm-wiki:blog-preview <slug>"), or publish to production ("/llm-wiki:blog-publish <slug>"). Writes to output/website/blog/ and manages _manifest.json. On publish, commits and pushes to master — jvto-web sync picks it up automatically.
---

# JVTO Blog Publisher

Three phases: CREATE → PREVIEW → PUBLISH. **One-shot flow preferred**: `/llm-wiki:blog-create <topik>` membuat draft, commit ke branch saat ini, kirim file, lalu tanya publish lewat tombol (`AskUserQuestion`) — user tidak perlu mengetik command publish yang panjang. PREVIEW dan PUBLISH tetap tersedia sebagai command terpisah untuk draft lama. You never auto-publish without an explicit user choice (tombol "Publish sekarang" dihitung sebagai pilihan eksplisit).

## Activation guard

Require `CLAUDE.md` mentioning JVTO / llm-wiki AND one of:
- User says "write a blog", "create a post", "draft an article", "buat blog", "tulis artikel"
- User invokes `/llm-wiki:blog-create`, `/llm-wiki:blog-preview`, `/llm-wiki:blog-publish`
- User names a slug that resolves to `output/website/blog/<slug>.md`

## File conventions

Post file: `output/website/blog/<slug>.md`
Manifest:  `output/website/blog/_manifest.json`

Slug format: `YYYY-MM-DD-<kebab-case-topic>` (e.g. `2026-06-10-kawah-ijen-complete-guide`)

### Post frontmatter (all fields required)

```yaml
---
title: "Human-readable title (max 70 chars)"
slug: "2026-06-10-kawah-ijen-complete-guide"
date: "2026-06-10"
status: "draft"
tags: [ijen, safety, guide]
seo_title: "Kawah Ijen Complete Guide 2026 | JVTO"
seo_description: "One sentence, max 160 chars."
sources: [destinations/kawah-ijen, credentials/trust-signals]
estimated_read_min: 5
---
```

### Manifest schema

```json
{
  "generated": "2026-06-10T00:00:00Z",
  "posts": [
    {
      "slug": "2026-06-10-kawah-ijen-complete-guide",
      "title": "Kawah Ijen Complete Guide 2026",
      "date": "2026-06-10",
      "status": "draft",
      "tags": ["ijen", "safety", "guide"],
      "seo_description": "...",
      "estimated_read_min": 5
    }
  ]
}
```

---

## Phase 1 — CREATE

**Trigger**: `/llm-wiki:blog-create` or "write a blog about X" or "buat blog tentang X"

### Step 1: Source selection

1. Read `wiki/index.md` to identify 2–3 wiki pages most relevant to the topic
2. Read those pages
3. List sources with a 1-line summary of what each contributes
4. State the proposed slug, title, tags, and SEO description
5. Ask: "Lanjut draft dengan sources ini?" — wait for confirmation before writing

### Step 2: Draft the post

Structure:
1. **Hook** — 2–3 kalimat, langsung, evidence-led. Cite satu fakta konkret dari wiki sources.
2. **Body** — H2 sections, 400–800 kata total. Setiap klaim traceable ke sumber.
3. **CTA** — Link ke relevant tour, `/trust`, `/verify-jvto`, atau `/policy`.

Brand voice rules (from `wiki/website/brand-voice.md`):
- Tidak boleh mengada-ada stats atau klaim — cite only wiki sources
- Tidak boleh menggunakan forbidden phrases dari `output/website/trust-bundle/policies.json` → `forbidden_wording`
- "Tourist Police officer" bukan "safety-focused guide"
- "100% Private" bukan "private tours"

### Step 3: Write + commit draft

1. Write `output/website/blog/<slug>.md` (frontmatter + body)
2. Add/update entry di `output/website/blog/_manifest.json` (status: "draft")
3. Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] blog-draft | <title>
   Slug: <slug>. Sources: <list>. Status: draft.
   ```
4. **Auto-commit ke branch saat ini** (bukan push — hanya commit lokal):
   ```
   git add output/website/blog/<slug>.md output/website/blog/_manifest.json wiki/log.md
   git commit -m "blog | draft | <title>"
   ```
   Draft sekarang tersimpan di repo lokal dan dapat dipreview langsung dari filesystem.

### Step 4: Deliver + ask publish (one-shot handoff)

Tujuan: user cukup satu command (`/llm-wiki:blog-create`). Setelah draft berhasil di-commit:

1. Tampilkan seluruh post di chat untuk dibaca langsung.
2. Kirim file output dengan tool `SendUserFile` (path: `output/website/blog/<slug>.md`, status: `normal`, caption: judul post).
3. Tanyakan dengan tool `AskUserQuestion` (1 pertanyaan, header "Publish?"):
   - **Publish sekarang** — update status ke published, push ke master, sync ke jvto-web
   - **Tidak sekarang** — draft sudah tersimpan di repo lokal; publish nanti via `/llm-wiki:blog-publish <slug>`

4. Routing jawaban:
   - "Publish sekarang" → langsung jalankan **Phase 3 — PUBLISH** (lewati pre-publish konfirmasi tambahan; checklist tetap dijalankan).
   - "Tidak sekarang" → konfirmasi draft tersimpan, beri tahu path file + cara publish nanti.

---

## Phase 2 — PREVIEW

**Trigger**: `/llm-wiki:blog-preview <slug>` atau "preview blog <slug>"

1. Read `output/website/blog/<slug>.md`
2. Render di chat dengan header block:

```
─────────────────────────────────────────────
BLOG PREVIEW · DRAFT
Slug:     2026-06-10-kawah-ijen-complete-guide
Title:    Kawah Ijen Complete Guide 2026
SEO:      Kawah Ijen Complete Guide 2026 | JVTO
Tags:     ijen, safety, guide
Read:     ~5 min
Status:   DRAFT — belum publish ke produksi
─────────────────────────────────────────────

[full post content rendered as markdown]

─────────────────────────────────────────────
Untuk publish: /llm-wiki:blog-publish 2026-06-10-kawah-ijen-complete-guide
Untuk edit: beritahu apa yang ingin diubah.
─────────────────────────────────────────────
```

3. Setelah render, tunggu. Jangan auto-publish.

---

## Phase 3 — PUBLISH

**Trigger**: `/llm-wiki:blog-publish <slug>`, user pilih "Publish sekarang" di handoff CREATE, atau user bilang "publish".

**Konfirmasi**: Jika sampai ke sini lewat tombol "Publish sekarang" (AskUserQuestion di Step 4 CREATE), tombol itu SUDAH menjadi konfirmasi — langsung jalankan checklist + publish tanpa bertanya lagi. Hanya jika dipicu via command `/llm-wiki:blog-publish` tanpa handoff sebelumnya, minta konfirmasi sekali.

### Pre-publish checklist (run silently, report hanya yang gagal)

- [ ] File exists: `output/website/blog/<slug>.md`
- [ ] Semua frontmatter fields ada (title, slug, date, status, tags, seo_title, seo_description, sources, estimated_read_min)
- [ ] `seo_description` ≤ 160 karakter
- [ ] Tidak ada forbidden phrases (cross-check `policies.json` → `forbidden_wording[].phrase`)
- [ ] `_manifest.json` punya entry untuk slug ini
- [ ] Status saat ini adalah "draft" (belum published)
- [ ] Body tidak kosong (minimal 200 kata)

Jika ada yang gagal: report dan stop. Jangan publish.

### Publish steps

1. Update `status` di frontmatter `.md`: `"draft"` → `"published"`
2. Update entry di `_manifest.json`: `"status": "published"`
3. Update `"generated"` di `_manifest.json` ke timestamp sekarang
4. Append ke `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] blog-publish | <title>
   Slug: <slug>. Published to master — jvto-web sync akan mengambil pada dispatch berikutnya.
   ```
5. Stage dan commit:
   ```
   git add output/website/blog/<slug>.md output/website/blog/_manifest.json wiki/log.md
   git commit -m "blog | publish | <title>"
   git push origin master
   ```

### Konfirmasi setelah push

```
✓ Published: <title>
  Slug:   <slug>
  URL:    /blog/<slug> (setelah jvto-web sync)
  Pushed to master ✓

  Langkah berikutnya:
  - jvto-web sync akan berjalan otomatis via repository_dispatch
  - Post akan muncul di /blog dan sitemap setelah sync + deploy selesai
  - Untuk melihat hasilnya: https://javavolcano-touroperator.com/blog/<slug>
```

---

## Edit setelah draft

Jika user ingin mengubah konten draft sebelum publish:
1. Baca file `.md` yang ada
2. Terapkan perubahan yang diminta
3. Tulis ulang file (pertahankan frontmatter, update body)
4. Append ke `wiki/log.md`: `## [DATE] blog-edit | <title>` dengan summary perubahan
5. Tampilkan ulang post yang sudah diedit

Jangan bump status — tetap "draft" sampai user eksplisit publish.

---

## Suggested topics (gunakan ini jika user tidak punya topik)

Ambil dari gap yang sudah teridentifikasi di wiki:

| Topik | Sumber utama | AEO value |
|---|---|---|
| Kawah Ijen Complete Guide | `wiki/destinations/kawah-ijen.md` | Tinggi |
| Bromo Closure Schedule & Plan-B | `wiki/destinations/mount-bromo.md` + `operational-facts.md` | Tinggi |
| How to Verify a Licensed Tour Operator | `wiki/credentials/trust-signals.md` | Tinggi (AEO) |
| Why Ijen Health Screening is Conditional | `policies.json` health_screening | Sedang |
| What 200 Guests Say About Night Trekking Ijen | `wiki/reviews/trustpilot-compilation.md` | Sedang |
| Ijen from Singapore: 4D3N Itinerary | `wiki/seo/seo-strategy.md` + GAP-09 materials | Tinggi |

---

## What this skill does NOT do

- Tidak menulis langsung ke jvto-web — sync dihandle oleh `sync-llm-wiki.yml`
- Tidak auto-approve atau auto-publish tanpa user eksplisit invoke Phase 3
- Tidak edit post yang sudah published (buat draft baru untuk versi update)
- Tidak generate gambar — hanya konten teks
- Tidak membuat slug di luar format `YYYY-MM-DD-<kebab>` 
