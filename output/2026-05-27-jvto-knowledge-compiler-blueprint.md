---
type: blueprint
title: JVTO Knowledge Compiler — Evidence-to-Asset Pipeline Blueprint
last_updated: 2026-05-27
audience: founder
status: conceptual (tool-agnostic, pipeline pattern only)
scope: compilation pattern — paralel & komplemen terhadap ABRS (reactive blueprint)
---

# JVTO Knowledge Compiler (JKC)

Blueprint pola **compiler** untuk JVTO. Bukan event handler, bukan chatbot, bukan dashboard. Ini adalah **mesin transformasi**: bukti mentah → knowledge terstruktur → aset bisnis multi-format → dampak ekonomi terukur.

> **Catatan posisi**: JKC adalah komplementer terhadap ABRS (Agentic Business Response System).
> - ABRS = reaktif, event-driven, "ada sinyal → ambil tindakan"
> - JKC = transformatif, batch/continuous, "ada knowledge → wujudkan jadi aset"
> Dua-duanya bersandar pada KB yang sama, dua-duanya melewati validation gate yang sama.

---

## 1. Tesis 1 kalimat

**JKC mengubah satu set bukti otentik JVTO menjadi banyak bentuk aset bisnis yang konsisten, terverifikasi, dan terlacak balik ke sumbernya**, dengan target khusus: AI search engine dan tourist asing memahami legitimasi JVTO dalam hitungan detik.

---

## 2. Mengapa "compiler", bukan "database" atau "CMS"

Compiler punya tiga sifat yang krusial untuk JVTO:

1. **Deterministik** — input yang sama → output yang sama. Tidak bergantung mood AI atau improvisasi.
2. **Multi-target** — satu source (bukti) → banyak target (web, schema, llms.txt, PDF, social, WA, sales material).
3. **Traceable** — setiap byte di output bisa di-trace balik ke evidence asli (audit chain).

JVTO punya 24 SHA-256-verified proof items + 92 wiki pages + 195 reviews + 14 crew KTA. Tanpa compiler, setiap output dibuat manual → drift, inconsistency, klaim tidak terverifikasi. Dengan compiler, output deterministik dan integritas terjaga.

JVTO **bukan** kekurangan data. JVTO **kekurangan pipeline**.

---

## 3. Arsitektur compiler: 6 stage

Pola tetap. Apa pun bukti yang masuk, melewati 6 stage ini sampai jadi aset bisnis dan dampak ekonomi.

```
[1] INTAKE              — bukti diamankan, immutable
[2] ANALYSIS            — makna bisnis diekstrak
[3] STATEFUL UPDATE     — knowledge hidup di-update, tidak ditimpa
[4] VALIDATION          — gate kebenaran + brand + legal
[5] OUTPUT COMPILATION  — render ke N format aset
[6] BUSINESS IMPACT     — dampak ekonomi diukur, di-feedback
```

Plus **cross-cutting target khusus**: AI Search & Discovery Portal — bentuk output prioritas (lapis 5) yang ditujukan agar AI search engine memahami JVTO.

### Stage 1 — INTAKE (Evidence Custody)

**Pertanyaan**: Bukti baru masuk, apakah aman dan terdokumentasi?

**Yang terjadi**:
- Capture bukti mentah dalam bentuk aslinya (foto, PDF, screenshot, file teks, JSON, gpx, csv, Excel)
- Hash SHA-256 dihitung dan dicatat
- Metadata: kapan didapat, dari siapa, format, ukuran, jenis bukti
- Simpan di immutable layer (raw/ folder atau equivalent) — **tidak boleh diedit pasca-intake**
- Register entry di evidence registry

**Output stage 1**: bukti yang sudah ter-tag, ter-hash, immutable.

**Kenapa stage ini ada**: bukti asli adalah dasar trust. Kalau diedit, claim runtuh. Compile harus dimulai dari bukti yang dijamin asli.

### Stage 2 — ANALYSIS (Business Meaning Extraction)

**Pertanyaan**: Apa nilai bisnis bukti ini? Untuk siapa?

**Bukan bertanya**: "data ini tentang apa?" (itu deskriptif)
**Bertanya**: "apa yang bisa dilakukan dengan data ini secara bisnis?" (itu strategis)

**5 dimensi nilai bisnis JVTO** (per bukti, di-score):
- **Trust value** — apakah memperkuat klaim C1-C9? Klaim mana?
- **Conversion value** — apakah bisa mengurangi keraguan calon customer di funnel?
- **Differentiation value** — apakah ini hal yang competitor tidak bisa klaim?
- **AI discoverability value** — apakah ini fakta yang AI search akan kutip ketika tourist tanya tentang JVTO/Ijen/Bromo?
- **Operational value** — apakah ini menghemat waktu staff atau menghindari risiko ops?

**Per dimensi**: 0 (no value) / 1 (supports) / 2 (strong) / 3 (anchor evidence).

**Selain skor**, ekstrak:
- **Audience target** — tourist asing? travel agent? crew internal? founder?
- **Asset target candidates** — sebaiknya muncul di: website? schema? llms.txt? PDF? WA template? blog?
- **Claim linkage** — connect ke claim C1-C9 dan ke wiki page existing

**Output stage 2**: bukti yang sudah ber-skor business value + tag audience + tag asset candidates + claim linkage.

### Stage 3 — STATEFUL UPDATE (Living Knowledge)

**Pertanyaan**: Bukti baru ini cocok di mana di knowledge JVTO yang sudah ada?

**Bukan**: simpan sebagai arsip terpisah.
**Adalah**: integrasikan ke struktur knowledge yang sudah hidup.

**Operasi yang dijalankan**:
- **Match** — bukti ini menambahkan / mengubah / mengonfirmasi fakta di wiki page mana saja
- **Diff** — apa yang berubah? klaim yang diperkuat? klaim yang berkonflik?
- **Reconcile** — kalau berkonflik dengan KB existing, masuk decision queue (siapa yang benar?)
- **Cross-link** — update inbound/outbound links di wiki, update index
- **Version** — KB version bump, change log entry

**Yang harus dihindari**:
- Silent overwrite (data lama hilang tanpa jejak)
- Fragmentation (bukti yang sama dicopy ke banyak tempat → drift)
- Stale referenced (output lama merujuk fakta yang sudah berubah)

**Output stage 3**: KB yang ter-update, dengan diff terdokumentasi, conflict di-queue, cross-link konsisten.

### Stage 4 — VALIDATION (Pre-Compile Gate)

**Pertanyaan**: Sebelum compile keluar, semua syarat terpenuhi?

**Gate yang harus lolos**:
- **Factual integrity** — setiap klaim ada bukti di KB, hash valid
- **Brand voice compliance** — voice invariants tidak dilanggar (tidak ada "blue fire guaranteed", price selalu IDR, dst)
- **Legal/policy compliance** — claim seperti "mandatory health screening" diberi qualifier, "police escort" diberi konteks
- **Privacy** — customer PII tidak masuk output publik, internal crew PII tidak masuk public-facing
- **Source attribution** — setiap fakta sensitif ter-cite ke source slug
- **Versioning** — output mencatat KB version yang dipakai

**Hasil**:
- Lolos semua → compile boleh jalan
- Flag → balik ke stage 2/3 untuk diperbaiki
- Hard fail → block + escalate

**Output stage 4**: keputusan compile-or-block + flag list (jika ada).

### Stage 5 — OUTPUT COMPILATION (Multi-Format Asset Engine)

**Pertanyaan**: Dari knowledge yang tervalidasi, render ke format apa saja?

Ini adalah stage di mana satu source jadi N target. **Same data, different shape, same truth.**

**JVTO output targets** (taksonomi tetap, satu source bisa hit multiple):

**Web targets** (HTML/Next.js)
- Halaman destinasi (5)
- Halaman paket tour (16)
- Halaman travel-guide (10+)
- Halaman policy (3+)
- Halaman team & crew bio (14)
- Halaman why-jvto / verify-jvto (trust hub)
- Halaman press & recognition
- Blog post / artikel

**Structured data targets** (JSON-LD)
- Organization schema
- TouristTrip per paket
- FAQPage
- GovernmentPermit
- Person (founder, doctor, crew)
- Review / AggregateRating
- BreadcrumbList

**AI-readable targets** (special — lihat section 4)
- `/llms.txt` (concise navigation untuk AI agents)
- `/llms-full.txt` (full curated knowledge dump)
- `sameAs` cross-references (Trustpilot, TripAdvisor, Google Maps CID, GetYourGuide)
- Trust verification page (SHA-256 hash registry)
- Evidence asset structure (named pillars, costly signals)

**Marketing targets**
- Social post (IG, FB, X, LinkedIn) — caption + hashtag set + image brief
- Email newsletter
- Brochure PDF
- Hero image briefs (untuk image gen / fotografer)
- Banner ad copy
- Press release draft

**Sales targets**
- Custom tour quote PDF
- Plan B proposal (alternative dates / packages bila booking gagal)
- Proposal travel agent (B2B partnership)
- Comparison sheet (JVTO vs OTA vs competitor)
- Group package proposal (corporate / family)

**Operational targets**
- WhatsApp canned response per intent + per stage
- Email template (booking conf, payment reminder, post-tour review request)
- Internal briefing (Monday/Friday/Quarterly)
- Crew runbook
- Customer arrival packet

**Compliance targets**
- Document registry per regulator (BBKSDA SE, KBLI, HPWKI)
- Audit packet (untuk regulatory inspection)
- ISIC provider record sync

**Compile rule**:
- Setiap target punya **template + slot definitions** (slot mana mengambil fakta apa)
- Compiler tarik fakta dari KB + isi slot → render → output
- Output file tersimpan + ter-hash + ter-version + traceable balik ke evidence asli

**Output stage 5**: aset bisnis siap pakai, multi-format, konsisten.

### Stage 6 — BUSINESS IMPACT (Outcome Measurement & Feedback)

**Pertanyaan**: Aset yang dipublish menghasilkan dampak apa?

**Metrik per layer** (yang JVTO concern):

**Trust layer**
- Trustpilot/Google/TripAdvisor rating drift
- AI brand mention share (Perplexity/ChatGPT/Gemini/Claude)
- Press mention count
- Direct mention dari customer ("saya pilih JVTO karena...")

**Discovery layer**
- Organic search ranking per 15 keyword target
- Click-through rate dari SERP
- AI search citation count (apakah JVTO dikutip ketika tourist tanya AI tentang Ijen tour operator)
- llms.txt access logs (apakah AI crawler ambil)

**Conversion layer**
- Inquiry → booking conversion rate
- Direct booking vs OTA mix (direct = margin tinggi)
- Average order value
- Lead-to-booking time
- Custom quote → close rate

**Retention / Reputation layer**
- Refund / dispute rate
- Repeat customer rate
- Referral rate (review mention "tell friend")
- Negative review response time
- Crisis recovery (kalau ada incident, berapa lama trust pulih)

**Operational efficiency layer**
- Founder time spent on routine ops (target: turun)
- Asset production cycle time (evidence → published)
- Brand drift incidents (target: 0)
- Output revision cycles (lower = better template/KB)

**Feedback ke compiler**:
- Metrik yang turun → evidence/output mana yang lemah? identifikasi → re-compile dengan improvement
- AI search tidak kutip JVTO → llms.txt / schema kurang AI-friendly → revisit stage 5 output template
- Conversion turun di satu paket → analisis: copy lemah? trust signal kurang? harga off? → re-compile

**Output stage 6**: dashboard impact + insight ke pipeline + backlog improvement.

---

## 4. Target khusus: AI Search & Discovery Portal

JVTO punya kondisi unik: **tourist asing makin mencari rekomendasi lewat AI search** (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) sebelum sampai ke website. Yang JVTO butuh: AI search engine **mengenali JVTO sebagai operator legal dan kredibel di hitungan detik**.

Ini adalah output kelas khusus dari stage 5, dengan persyaratan ekstra:

### 4.1 Karakteristik AI-readable output

- **Concise dan navigable** — AI agent harus bisa membaca dalam batas context window
- **Evidence-anchored** — tiap klaim disertai source URL atau hash
- **Cross-referenced** — sameAs ke external authoritative sources (Trustpilot, Tripadvisor, Google Maps CID, ISIC, INDECON)
- **Structured-first** — JSON-LD lebih disukai daripada free prose
- **Stable URLs** — AI cache butuh URL yang tidak berubah
- **No marketing fluff** — claim, evidence, source — selesai. AI tidak peduli "experience the magic"

### 4.2 Spesifik bentuk aset

**`/llms.txt`** (lightweight nav)
- Identitas singkat JVTO (legal name, NIB, KBLI)
- 9 claim utama (C1-C9) dengan 1-baris evidence per claim
- Daftar URL utama (destinations, packages, why-jvto)
- Link ke `/llms-full.txt`

**`/llms-full.txt`** (full curated dump)
- Full SSOT-derived snapshot per kategori
- Pricing tables structured
- Crew + credentials
- Permit registry
- Aggregate rating + sample reviews
- Press mentions dengan URL
- Update frequency declared (last updated, next scheduled)

**Schema JSON-LD lengkap** (harus dedup, valid Rich Results)
- Organization (parent)
- TravelAgency + TouristTrip per paket
- FAQPage per landing page
- Person untuk founder + doctor + named crew
- GovernmentPermit untuk NIB/TDUP/BBKSDA/KBLI
- Review + AggregateRating cross-platform sameAs

**Trust verification page** (`/verify-jvto`)
- SHA-256 hash registry (per proof item)
- Live link ke external registry (AHU portal, OSS, ISIC)
- Press item list dengan URL
- Costly signal items (police docs — yang competitor tidak bisa fake)

**Entity cross-reference (sameAs web)**
- Trustpilot URL
- TripAdvisor URL
- Google Maps CID URL
- GetYourGuide URL
- INDECON spotlight URL
- ISIC provider URL
- BBKSDA Jatim coverage URL
- Detik / Radar Jember article URL

### 4.3 Compile rule khusus AI-readable

- Update frequency: setiap KB version bump → re-compile `/llms.txt` + `/llms-full.txt`
- Validation extra: factual gate, sameAs gate (link harus valid live), schema gate (Rich Results test pass)
- Format: plain text minimalist + structured JSON paralel (AI agent boleh pilih)
- Monitoring: log AI crawler hits per file (bot UA tracking)

### 4.4 Fungsi bisnis spesifik

Ketika tourist Singapura tanya ChatGPT "best operator for Ijen Mount Bromo combination tour", target:
- JVTO masuk top 3 mention
- AI sebut alasan: police-led, BBKSDA-coordinated, 195 verified reviews, 14 KTA crew
- AI link ke javavolcano-touroperator.com (bukan OTA aggregator)
- Tourist clicks → langsung yakin → direct booking (margin tinggi)

Ini bukan SEO biasa. Ini **AEO + GEO + AI-readability**. Stage 5 + target ini = JVTO punya advantage sebelum competitor sadar penting.

---

## 5. Taksonomi evidence JVTO (input space)

Apa saja yang masuk Stage 1?

### Kelas E1 — Bukti legal & regulatori
- NIB 1102230032918
- TDUP issuance 2023-02-11
- KBLI codes (79121, 79911, dst)
- AHU registry record
- BBKSDA SE.1658/KSA.9/2024 dokumen
- ISIC provider ID 259268

### Kelas E2 — Bukti otoritas police-led
- SPRIN POLPAR (founder police assignment)
- SPRIN WAL-TRAVEL (tour police walkalong)
- Bripka rank evidence
- Ditpamobvit unit photos
- Field operation police escort photos

### Kelas E3 — Bukti medical & safety
- Dr. Irwandanu SIP (license)
- Health screening protocol document
- 5 screening photos
- BBKSDA closure / opening notices
- Tourist accident registry (data historis)

### Kelas E4 — Bukti crew & operasional
- 14 KTA codes (KTA-G/D-2024-001..011)
- HPWKI training records
- Crew portraits + bio
- Vehicle fleet + driver allowances
- Hotel partner registry

### Kelas E5 — Bukti customer & reputation
- 195 reviews (Google 123 + Trustpilot 51 + TripAdvisor 21)
- Owner replies di review
- Press mentions (Detik, Radar Jember ×2, BBKSDA, Stefan Loose)
- Testimonial verbatim
- INDECON spotlight feature

### Kelas E6 — Bukti operasional rute & destinasi
- GPX track per destinasi (5 file)
- Route segment library (43 day-segments + 217 activity rows)
- Destination photos + image asset map (54 images)
- Hotel allocation per phase
- 3D viewer URLs

### Kelas E7 — Bukti finansial & komersial
- 22 paket dengan pricing tier
- COGS spreadsheet per paket (15 file)
- Rate cards (crew, vehicle, accommodation, activities, other)
- Booking volume + revenue data dari backoffice
- Margin analysis

### Kelas E8 — Bukti partner & institusional
- HPWKI member confirmation
- INDECON spotlight URL
- ISIC provider URL
- Booking.com 2015 award (homestay era)
- Stefan Loose guidebook citation

Setiap kelas: per evidence punya hash + intake date + source slug + scoring di stage 2.

---

## 6. Mapping evidence × claim × asset

Tabel ringkas: source dan claim dan asset target — agar terlihat compile dependency.

| Evidence kelas | Claim utama yang didukung | Asset target prioritas |
|---|---|---|
| E1 (legal) | C5 (proof-first trust), C8 (institutional) | verify-jvto, schema GovernmentPermit, /llms-full.txt §licenses |
| E2 (police) | C1 (safety-led), C7 (team credibility), C5 | why-jvto/community-standards, founder bio, verify-jvto, press hub |
| E3 (medical) | C4 (Ijen health screening), C1, C8 | travel-guide/ijen-health-screening, doctor bio, AEO snippets Ijen safety |
| E4 (crew) | C7 (personality economy), C2 (private control), C1 | team page + 14 crew bio, why-jvto/our-team, social posts |
| E5 (reviews) | C6 (reviews registry), all claims (validation) | why-jvto/reviews, AggregateRating schema, trust hub, social proof |
| E6 (rute) | C2 (private execution), tour quality | destination pages, tour packages, 3D viewer, schema TouristTrip |
| E7 (finansial) | C3 (all-inclusive transparency) | policy/booking-payment, pricing table, custom quote engine |
| E8 (partner) | C8 (institutional partners), C5 | verify-jvto, schema sameAs, press recognition |

Setiap evidence bisa back multiple claims. Setiap claim ditarik dari multiple evidence. **Compiler memetakan dependensi ini** sehingga: evidence baru masuk → tahu otomatis asset mana yang perlu re-compile.

---

## 7. Compile dependency graph (konsep)

```
EVIDENCE LAYER (E1..E8, ~hundreds of items)
            │
            ▼
   [Stage 1: INTAKE]
            │
            ▼
   [Stage 2: ANALYSIS]
            │  (skor business value, tag audience, tag asset candidates)
            ▼
   [Stage 3: STATEFUL UPDATE]
            │
            ▼
   ┌────────────────────────────┐
   │  KNOWLEDGE BASE (wiki/SSOT) │
   │  • 92+ pages, versioned     │
   │  • Claim graph C1-C9        │
   │  • Cross-linked             │
   └──────────────┬──────────────┘
                  │
                  ▼
       [Stage 4: VALIDATION]
                  │
                  ▼
       [Stage 5: COMPILE]
                  │
   ┌──────────────┼──────────────┬─────────────┬─────────────┐
   ▼              ▼              ▼             ▼             ▼
 WEB         AI-READABLE      MARKETING     SALES         OPS
(pages,    (llms.txt,      (social,     (proposals,    (WA,
schema,    llms-full,      brochures,    quotes,        briefings,
FAQ,       trust hub,      ads,          comparison,    runbooks,
blog)      sameAs)         press)        Plan B)        templates)
   │              │              │             │             │
   └──────────────┴──────────────┴─────────────┴─────────────┘
                  │
                  ▼
       [Stage 6: IMPACT]
                  │
                  ▼
       Metrik trust + discovery + conversion + retention + ops eff
                  │
                  └──────────── feedback ke stage 2 / 3 / 5 templates
```

Dependency graph ini deterministik: evidence X masuk → KB pages Y..Z affected → asset A..D scheduled re-compile.

---

## 8. Invariants (kontrak yang harus dipegang)

10 invariant yang membuat compiler bisa dipercaya, apa pun stack-nya nanti:

1. **Bukti asli tidak pernah diedit pasca-intake** — versi original immutable, edit hanya di derived layer.
2. **Setiap klaim di output dapat dilacak balik ke evidence (one-hop atau few-hop)** — audit chain tidak putus.
3. **Hash SHA-256 evidence di-cite di output trust-critical** — bukan klaim teks tapi proof.
4. **KB version yang dipakai compile tercatat di output** — output knows its provenance.
5. **Conflict di KB dimasukkan decision queue, tidak silently resolved** — keputusan manusia tetap diperlukan untuk ambiguity.
6. **Re-compile bersifat idempotent** — compile ulang dengan input sama → output sama (bit-exact untuk structured, semantic-equivalent untuk prose).
7. **Tidak ada output publik mengandung PII customer atau internal crew detail** — privacy boundary di gate 4.
8. **Asset baru tidak overwrite asset live tanpa diff review** — staging dulu, promote setelah validasi.
9. **Setiap claim berikatan dengan brand voice rule yang berlaku** — voice invariants tidak bisa dilampaui karena alasan kreatif.
10. **Compile pipeline ber-log lengkap** — siapa/apa men-trigger, evidence apa, KB version berapa, output mana yang berubah.

---

## 9. Boundary — apa JKC ADALAH dan BUKAN

### ADALAH
- Pipeline transformasi deterministik dari evidence → KB → asset
- Multi-target output engine (1 source → N format)
- Validation-gated (tidak ada asset publish tanpa lolos gate)
- KB-grounded (single source of truth via wiki/SSOT)
- Traceable (output → evidence reverse-lookup)
- Versioned (tahu KB version mana yang dipakai)
- AI-discovery aware (target khusus untuk AI search engine)

### BUKAN
- Bukan event handler (itu ABRS — beda sistem, beda peran)
- Bukan creative content generator yang lepas dari KB
- Bukan CMS biasa yang menyimpan dan menampilkan
- Bukan publishing tool standalone — publish hanya outcome stage 5
- Bukan analytics platform — stage 6 hanya metrics scoring, dashboard implementasi terpisah
- Bukan replacement untuk founder judgment di reconcile conflicts di stage 3
- Bukan oracle market — stage 6 metrik hanya internal feedback, bukan prediksi pasar

---

## 10. Hubungan dengan ABRS

**JKC dan ABRS adalah dua roda di mesin yang sama**:

| Aspect | JKC (Compiler) | ABRS (Reactive Agent) |
|---|---|---|
| Trigger | Evidence masuk / schedule / KB version bump | Sinyal eksternal (review, inquiry, alert) |
| Output | Aset (asset durable) | Respons / aksi (action transient) |
| Cadence | Continuous + scheduled | Real-time / near-real-time |
| Audience output | Public (web, AI search) + internal | Spesifik per sinyal (customer / founder / KB) |
| Validation gate | Sama (4-gate framework) | Sama (4-gate framework) |
| KB role | Output destination + source | Decision source |
| Failure mode | Asset off → revert version | Action wrong → rollback action |

Keduanya **share infrastructure**: KB, brand voice gate, evidence registry, audit log.

Keduanya **berbeda peran**: JKC bangun rumah, ABRS jaga pintu.

---

## 11. Prerequisite konseptual (sebelum bicara stack)

Yang harus disepakati dulu sebelum tools:

1. **Evidence registry ada dan disiplin** — setiap bukti ber-hash, ber-source, ber-metadata. Sudah sebagian terjadi di JVTO (24 SHA-256 items, _manifest/ folder).
2. **Claim graph eksplisit (C1-C9 sudah ada di JVTO)** — setiap claim tahu evidence pendukungnya. Sudah tercatat di wiki/website/aeo-claims.md.
3. **Asset taxonomy terdefinisi** — semua jenis output yang JVTO concern di-list (Section 5.2 di blueprint ini).
4. **Template per asset jelas** — slot mana isi apa, fallback kalau evidence missing.
5. **KB versioning konvensi** — versi naik kapan, change log format apa.
6. **Brand voice machine-checkable** — invariants di-encode jadi rules yang bisa diotomasi (regex / structured).
7. **Trace contract** — output format wajib carry: KB version + evidence hash list + compile timestamp.
8. **Conflict resolution policy** — siapa decide kalau evidence baru bertentangan dengan KB lama.
9. **Re-compile triggers tertulis** — kapan harus re-compile asset X (KB version bump? evidence baru di claim X? schedule?).
10. **Failure mode dipetakan** — kalau stage 2 score 0 di semua dimensi, asset target apa yang tetap di-compile (default-only)? Kalau gate 4 hard-fail, evidence di-quarantine atau ditolak?

---

## 12. Ringkasan inti (1 paragraf)

**JKC** adalah **mesin compile bukti → aset** dengan 6 stage tetap (Intake → Analysis → Stateful Update → Validation → Output → Impact). Input space = 8 kelas evidence JVTO (legal, police, medical, crew, customer, rute, finansial, partner). Output space = 5 kategori asset (web, AI-readable, marketing, sales, ops) dengan target khusus **AI Search & Discovery Portal** (`llms.txt`, schema, trust hub, sameAs web). Knowledge base JVTO (wiki + SSOT + claim graph C1-C9) adalah single source of truth — semua compile dirujuk ke KB, semua output dapat ditelusuri balik ke evidence asli via hash. 10 invariant di Section 8 adalah kontrak yang harus dipegang implementasi mana pun. JKC dan ABRS komplementer: JKC bangun aset durable, ABRS jaga respons real-time, keduanya share KB + gate.

---

*End of blueprint. Status: conceptual baseline (compiler pattern). Next conceptual step: pilih satu evidence kelas → satu asset target → trace dependency end-to-end sebagai pilot blueprint (mis. E5 reviews → AI-readable trust hub). Itu pembahasan terpisah dari tooling/stack.*
