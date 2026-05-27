---
type: synthesis
title: JVTO System — Holistic Synthesis (Reset View)
last_updated: 2026-05-27
audience: founder
status: foundational synthesis
mode: JVTO Business-First (attract / reassure / convince / convert international tourists)
---

# JVTO System — Holistic Synthesis

Dokumen reset. Bukan tentang dashboard, bukan tentang blueprint terpisah. **Ini tentang sistem secara utuh** — dari data mentah masuk sampai tourist asing klik "Book Now". Lensa tunggal: business-first.

---

## 1. Definisi sistem dalam 1 kalimat

JVTO sedang membangun sebuah **mesin produksi konten + bukti** yang dijalankan bersama oleh **manusia (Anda) dan LLM (Cowork)** dengan **Obsidian sebagai meja kerja bersama**, di mana setiap data baru yang Anda kumpulkan diolah secara progresif menjadi **aset website yang membuat tourist asing percaya dan booking langsung**.

Tidak lebih, tidak kurang.

---

## 2. Tiga komponen sistem — peran masing-masing

Sistem ini punya **tiga komponen yang saling berbeda peran**. Memahami pembagian peran ini adalah inti — kalau salah, semua optimasi salah arah.

### 2.1 Obsidian — Meja kerja bersama (interface layer)

Obsidian **bukan** wiki, bukan database, bukan CMS. Obsidian adalah **antarmuka**.

Fungsinya untuk Anda:
- Tempat **memasukkan** data baru (paste web clip, drop file, tulis catatan)
- Tempat **membaca** apa yang sudah dikumpulkan (wikilinks, graph view)
- Tempat **memeriksa** apa yang LLM tulis (semua hasil LLM = file markdown yang bisa Anda baca)
- Tempat **mengoreksi** kalau ada yang salah (edit file langsung)

Fungsinya untuk LLM (Cowork):
- Akses file langsung (markdown = mudah dibaca)
- Struktur folder yang konsisten (wiki/raw/output)
- Wikilinks sebagai graph navigation

Kenapa Obsidian, bukan Notion atau Google Docs:
- File lokal — tidak ada vendor lock-in, tidak ada API limit
- Markdown — paling LLM-friendly
- Git-friendly — versi history alami
- Anda tetap pegang **kontrol penuh** atas file

### 2.2 LLM Wiki — Otak yang hidup (knowledge layer)

LLM Wiki **bukan sekadar folder catatan**. LLM Wiki adalah:

> Struktur knowledge yang dirancang khusus agar LLM bisa membaca, menulis, memvalidasi, dan menghasilkan output bisnis darinya — dengan disiplin yang konsisten.

Ciri-ciri yang membuat sesuatu **layak disebut "LLM Wiki"** (semua sudah Anda terapkan):

| Ciri | Apa | Mengapa penting untuk LLM |
|---|---|---|
| **Frontmatter konsisten** | `type`, `title`, `sources`, `last_updated` di tiap file | LLM bisa filter, sort, dependency-trace |
| **Wikilinks tertib** | `[[folder/page-name]]` | LLM bisa traverse knowledge graph |
| **SSOT terpisah dari output** | `/raw/` immutable, `/wiki/` curated, `/output/` derived | LLM tahu mana truth, mana turunan |
| **Workflow ter-dokumentasi** | `Workflow 1/2/3/4/5/6` di CLAUDE.md | LLM tahu prosedur, tidak improvisasi |
| **Source attribution** | Setiap klaim ter-cite `[[sources/xxx]]` | LLM tidak fabrikasi |
| **Voice invariants tertulis** | `wiki/website/brand-voice.md` | LLM tidak menulis bebas |
| **Log apendable** | `wiki/log.md` | LLM tahu apa yang terjadi sebelumnya |

**LLM Wiki = Wiki yang tahu dirinya sedang dipakai LLM untuk bekerja.**

Wiki Anda sudah ini — 92 pages, struktur disiplin, claim graph C1-C9, evidence registry dengan SHA-256. Bedanya dengan wiki biasa: setiap halaman dirancang agar LLM bisa **andalkannya untuk produksi** bukan sekadar lookup.

### 2.3 Cowork — Pekerja yang hidup di meja Anda (execution layer)

Cowork **bukan chatbot**. Cowork adalah **agen yang bekerja di filesystem Anda dengan tool eksternal**:
- Bisa baca/tulis file di folder Anda (Obsidian vault sekaligus jadi vault Cowork)
- Bisa panggil tool eksternal (browser, web fetch, Drive, Gmail, dll)
- Bisa menjalankan script
- Bisa membuat dashboard live (artifact)
- Bisa di-schedule

Peran Cowork dalam sistem ini:
- **Ingest**: ubah raw data jadi wiki source page
- **Compile**: ubah wiki jadi website asset
- **Validate**: cek konsistensi, contradiction, voice invariants
- **Monitor**: pantau review, mention, SEO health
- **Produce**: bikin dashboard, briefing, draft email/WA

---

## 3. Proses (the loop)

Sistem ini berjalan dalam **loop tunggal** yang berulang setiap kali data baru masuk:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   [1] ANDA mengumpulkan data baru                           │
│       (web clip, screenshot, file, foto, exporter)          │
│                              │                              │
│                              ▼                              │
│   [2] ANDA drop ke /raw/ via Obsidian                       │
│       (atau share via Cowork chat)                          │
│                              │                              │
│                              ▼                              │
│   [3] COWORK baca + pahami + diskusi dengan Anda            │
│       (klarifikasi, ekstraksi, deteksi conflict)            │
│                              │                              │
│                              ▼                              │
│   [4] COWORK tulis /wiki/sources/[slug].md                  │
│       (struktur konsisten, ter-cite, ter-frontmatter)       │
│                              │                              │
│                              ▼                              │
│   [5] COWORK update halaman wiki yang terkait               │
│       (destinations, credentials, claims, reviews, dst)     │
│                              │                              │
│                              ▼                              │
│   [6] COWORK append /wiki/log.md                            │
│       (apa yang berubah, kapan, kenapa)                     │
│                              │                              │
│                              ▼                              │
│   [7] COWORK compile /output/ asset bila diminta            │
│       (page copy, schema, llms.txt, social, email, WA)      │
│                              │                              │
│                              ▼                              │
│   [8] ANDA review di Obsidian                               │
│       (file ter-render = mudah dibaca)                      │
│                              │                              │
│                              ▼                              │
│   [9] ANDA approve → deploy ke jvto-web                     │
│       (atau revisi, balik ke [3])                           │
│                              │                              │
│                              ▼                              │
│   [10] WEBSITE update                                       │
│        (tourist asing lihat aset baru/perbaikan)            │
│                              │                              │
│                              ▼                              │
│   [11] TOURIST RESPOND (review, inquiry, booking)           │
│                              │                              │
│                              └────────┐                     │
│                                       ▼                     │
│                              kembali ke [1]                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Loop ini adalah sistem itu sendiri.** Setiap fase punya tanggung jawab jelas. Anda tidak harus menjalankan semua sekaligus — loop bisa jalan kalau bahkan baru 1 data point masuk.

---

## 4. Alur (siapa lakukan apa, kapan)

| Tahap | Manusia (Anda) lakukan | Cowork (LLM) lakukan | Output tahap |
|---|---|---|---|
| **Kumpul** | Browse web, scan PDF, foto field ops, ekspor DB, kumpul review | — | File raw di Obsidian /raw/ |
| **Drop** | Drag-drop ke /raw/ atau share di chat Cowork | — | Source tersedia untuk diolah |
| **Pahami** | Konteks singkat ("ini apa, dari mana") | Klarifikasi, baca, struktur ekstrak, deteksi conflict dengan wiki existing | Pemahaman bersama |
| **Tulis source** | Approve framing | Bikin /wiki/sources/[slug].md dengan format konsisten | Source page terstruktur |
| **Update domain** | — | Update halaman wiki yang relevan (destinations, credentials, reviews, dll) | Wiki konsisten dengan source baru |
| **Catat log** | — | Append /wiki/log.md | Audit trail |
| **Compile** | Trigger ("buat halaman X" / "siapkan llms.txt") | Tarik dari wiki, render ke format target | File di /output/ |
| **Review** | Buka file di Obsidian, baca | — | Approval atau revisi |
| **Revisi** | Beri feedback spesifik | Edit + re-compile | Versi baru |
| **Approve** | Tandai approved | — | Siap deploy |
| **Deploy** | Sync ke jvto-web (manual atau script) | (bisa bantu kalau diberi access) | Website live |
| **Monitor** | Cek dashboard | Pantau review baru, SEO drift, brand mention | Trigger loop berikutnya |

Pembagian peran ini **bukan kaku** — ada zona overlap (mis. Anda boleh tulis langsung di wiki, Cowork boleh mulai loop tanpa data baru). Tapi pola defaultnya seperti tabel di atas.

---

## 5. Apa yang dihasilkan — taksonomi output

Dari loop ini, ada **5 jenis output** yang menjadi aset bisnis nyata untuk JVTO:

### Output Type 1 — Wiki page (knowledge yang hidup)

**Form**: file markdown di `/wiki/`
**Lokasi konsumsi**: dibaca oleh Cowork untuk produksi selanjutnya; dibaca oleh Anda untuk verifikasi
**Nilai bisnis**: foundation. Tanpa wiki yang akurat, output downstream juga akurasi terbatas.

### Output Type 2 — Website page content (landing copy)

**Form**: file markdown/MDX di `/output/website/pages/`
**Lokasi konsumsi**: deploy ke jvto-web → tourist asing baca di browser
**Nilai bisnis**: tempat konversi. Setiap halaman destinasi/paket/why-jvto = tempat tourist membuat keputusan.
**Kaitan ke 4 fungsi bisnis**: ATTRACT (SEO/AEO), REASSURE (proof), CONVINCE (story), CONVERT (CTA)

### Output Type 3 — Structured data (untuk AI search + schema)

**Form**: JSON-LD per page, `llms.txt`, `llms-full.txt`, `evidence-registry.json`, schema.org markup
**Lokasi konsumsi**: AI search engine (ChatGPT/Perplexity/Gemini/Claude/Google AI), validator pihak ke-3
**Nilai bisnis**: dengan tourist 2026+ makin tanya AI dulu sebelum buka website, ini = pre-discovery layer. Kalau JVTO tidak ada di sini, tourist tidak pernah sampai ke website.
**Kaitan ke 4 fungsi bisnis**: ATTRACT (terutama)

### Output Type 4 — Operational content (template & response)

**Form**: WA canned response, email template, custom quote PDF, FAQ snippet
**Lokasi konsumsi**: staff JVTO pakai langsung saat respon ke tourist
**Nilai bisnis**: kecepatan + konsistensi di funnel bottom. Setiap detik delay = lead lari ke OTA.
**Kaitan ke 4 fungsi bisnis**: CONVINCE + CONVERT

### Output Type 5 — Visual asset (untuk channel marketing)

**Form**: social post (caption + image brief), brochure PDF, hero image brief, video clip brief
**Lokasi konsumsi**: Instagram/Facebook/X/LinkedIn, email blast, paid ads
**Nilai bisnis**: distribution di luar website — bawa traffic balik.
**Kaitan ke 4 fungsi bisnis**: ATTRACT + REASSURE (testimonial visual)

---

## 6. Kenapa Obsidian + LLM Wiki + Cowork (bukan satu tool saja)

Sederhana: **masing-masing tidak bisa menggantikan dua lainnya.**

| Coba ganti dengan | Yang hilang | Konsekuensi |
|---|---|---|
| **Obsidian saja** (tanpa Cowork) | Eksekusi otomatis hilang | Anda kerja manual mengubah wiki → output. Skala terbatas, founder bottleneck. |
| **Cowork saja** (tanpa Obsidian/Wiki) | Persistent knowledge hilang | Setiap sesi mulai dari nol, tidak ada akumulasi, tidak ada cross-link. |
| **Wiki saja** (tanpa Obsidian) | Interface manusiawi hilang | Anda terikat di terminal/IDE, sulit drop file, sulit graph view, no live preview. |
| **Notion / Google Docs** (gantikan Obsidian + Wiki) | File access untuk LLM lambat, vendor-locked, API limit, struktur kurang LLM-friendly | Cowork tidak bisa baca/tulis efisien, ada cost API tambahan. |

Tiga komponen ini membentuk **kapasitas bersama** — manusia + LLM + persistent knowledge — yang lebih besar dari jumlah bagian.

---

## 7. Optimasi dengan konsep Cowork (apa yang Cowork bisa lakukan optimal)

Cowork punya beberapa kapabilitas yang tidak dimiliki LLM standar — saya gunakan untuk optimasi sistem JVTO:

### 7.1 Filesystem access langsung

Cowork **bisa baca dan tulis file langsung** di vault Obsidian Anda. Artinya:
- Tidak perlu copy-paste manual
- Wiki update otomatis saat data baru masuk
- Output langsung tersimpan di /output/ siap deploy
- Anda buka Obsidian, file sudah ada — tidak ada step "kirim ke AI lalu paste hasilnya"

### 7.2 Bash + script execution

Cowork bisa jalankan script. Artinya:
- Bisa hitung SHA-256 hash untuk evidence files
- Bisa parse CSV dari backoffice export
- Bisa run script kompilasi (mis. CSV → JSON SSOT)
- Bisa jalankan link checker, schema validator, dll

### 7.3 MCP tools (browser, web fetch, dll)

Cowork punya akses tool eksternal yang Anda tidak perlu setup sendiri:
- Browser (untuk scrape review live, cek SERP, screenshot competitor)
- Web fetch (untuk ingest source URL)
- Wolfram (untuk hitung sunrise/sunset, elevation)
- AllTrails (untuk validate GPX data)

### 7.4 Artifacts (persistent live HTML)

Cowork bisa bikin halaman HTML yang **persisten antar sesi** + bisa **refresh data live** saat dibuka. Artinya:
- Dashboard yang tetap ada
- Bisa Anda bookmark dan buka kapan saja
- Refresh button bawaan → data segar
- Bisa di-embed atau di-share

### 7.5 Scheduled tasks

Cowork bisa di-schedule. Artinya:
- Loop monitoring otomatis (daily review check, weekly sprint check)
- Briefing otomatis (Monday brief, Friday brief)
- Tidak perlu Anda buka sesi setiap kali

### 7.6 Session continuity

Cowork bisa baca transcript sesi sebelumnya. Artinya:
- Konteks tidak hilang antar hari
- Bisa refer ke "yang kita diskusikan kemarin"
- Akumulasi pemahaman dari waktu ke waktu

---

## 8. Bagaimana sistem ini melayani 4 fungsi bisnis JVTO

| Fungsi | Bagaimana sistem ini melayani |
|---|---|
| **ATTRACT** (tourist menemukan JVTO) | Output Type 3 (AI/SEO surface) + Output Type 2 (landing pages SEO-optimized) + Output Type 5 (social distribution) |
| **REASSURE** (tourist meragu hilang) | Output Type 2 dengan trust signals lengkap + /verify-jvto evidence registry + review compilation + Output Type 4 (WA reply yang inject proof) |
| **CONVINCE** (tourist yakin JVTO terbaik) | Output Type 2 dengan story + crew bio + claim-evidence linkage + Output Type 4 (per-package proof pack) |
| **CONVERT** (tourist klik Book / kirim WA) | Output Type 2 CTA terstruktur + Output Type 4 fast response + custom quote PDF cepat |

Setiap output yang dihasilkan loop ini bisa di-trace balik: aset ini melayani fungsi A/R/C/C yang mana? Kalau tidak ada jawaban jelas, output itu tidak prioritas.

---

## 9. Karakter sistem (yang harus dijaga)

Lima karakter yang membuat sistem ini berjalan baik dan tidak runtuh seiring waktu:

1. **Progresif** — data masuk pelan-pelan, sistem tetap berjalan. Tidak perlu semua data ada di awal.
2. **Asymmetric work** — Cowork lakukan kerja berat (compile, lint, lookup, format); Anda lakukan kerja ringan (approve, koreksi, arah).
3. **File-first** — semua state tersimpan di filesystem. Kalau Cowork mati, wiki tetap ada. Kalau Obsidian crash, file tetap ada.
4. **Reversible** — ada Git/version history; salah edit bisa rollback.
5. **Business-grounded** — setiap output dikaitkan ke A/R/C/C; tidak ada output untuk output's sake.

---

## 10. Yang tidak ada di sistem ini (eksplisit)

Penting untuk dinyatakan agar tidak salah arah:

- **Tidak ada** chatbot tourist-facing (JVTO bicara dengan tourist via WA manusia, bukan chatbot)
- **Tidak ada** ML model training (sistem pakai LLM, tapi tidak train model sendiri)
- **Tidak ada** vendor SaaS yang menahan data Anda (semua file lokal)
- **Tidak ada** automation tanpa human gate untuk hal trust-critical (Anda tetap approve apa yang masuk website)
- **Tidak ada** "magic AI" yang tahu segalanya (Cowork hanya tahu apa yang ada di wiki + tool yang dipakai)

---

## 11. Status sistem saat ini (jujur)

| Komponen | Status |
|---|---|
| Obsidian sebagai interface | Aktif, vault `llm-wiki` di E: drive |
| LLM Wiki struktur | Matang — 92 pages, workflows ter-dokumentasi, claim graph, evidence registry |
| Cowork integration | Aktif sesi ini — bisa baca/tulis vault, MCP tools tersedia |
| Loop ingest | Sudah jalan beberapa kali (lihat `wiki/log.md`) |
| Loop compile → website | Output sudah produksi di `/output/`, deploy ke jvto-web masih manual |
| Output Type 1 (wiki) | Matang |
| Output Type 2 (landing pages) | Sebagian besar siap, beberapa Silo 2 masih perlu depth |
| Output Type 3 (AI/SEO surface) | Schema sudah, llms.txt belum |
| Output Type 4 (operational) | WA playbook ada, runtime belum |
| Output Type 5 (visual) | Sporadic, belum sistematis |

---

## 12. Ringkasan inti (1 paragraf untuk dibawa keluar)

**JVTO Anda sedang membangun adalah sebuah meja kerja kolaboratif manusia–LLM**: Anda mengumpulkan data dari dunia luar dan menaruhnya di Obsidian; LLM Wiki menyusun data itu menjadi knowledge graph yang konsisten dan terverifikasi; Cowork sebagai LLM pekerja mengubah knowledge itu menjadi aset bisnis (halaman website, AI-readable surface, template operasional, visual marketing) yang membuat tourist asing menemukan, percaya, yakin, dan akhirnya booking JVTO. Setiap data baru yang Anda berikan menggerakkan loop ini selangkah maju — sistem ini **progresif by design**, bukan one-shot project. Cowork bukan menggantikan Anda; Cowork mengangkat beban produksi sehingga Anda fokus ke yang hanya bisa manusia lakukan: pengumpulan bukti, persetujuan, dan hubungan dengan tamu.

---

*Sintesis selesai. Ini adalah peta utuh — bukan rekomendasi eksekusi, bukan plan dashboard, bukan blueprint terpisah. Setelah Anda baca, beri tahu di mana pemahaman saya benar, di mana perlu dikoreksi, dan dari sini ke mana harus melangkah.*
