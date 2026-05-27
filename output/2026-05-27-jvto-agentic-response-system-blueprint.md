---
type: blueprint
title: JVTO Agentic Business Response System — Foundational Blueprint
last_updated: 2026-05-27
audience: founder
status: conceptual (tool-agnostic)
scope: pattern / architecture only — no tool mapping, no implementation
---

# JVTO Agentic Business Response System (ABRS)

Blueprint pola dasar — **bukan inventory tools, bukan rencana eksekusi.** Hanya pola berpikir: bagaimana data baru menjadi tindakan bisnis otomatis, dengan JVTO sebagai konteks.

---

## 1. Definisi 1 kalimat

**JVTO ABRS** adalah sistem yang **mengubah sinyal baru (apa pun bentuknya) menjadi keputusan dan output bisnis** dengan referensi tetap ke knowledge base internal JVTO (wiki, SSOT, brand voice, kebijakan), tanpa harus menunggu founder.

Bedanya dengan chatbot/AI assistant biasa: ABRS **tidak menjawab pertanyaan** — ia **bereaksi terhadap kondisi baru** dan menghasilkan keluaran bisnis nyata (balasan terkirim, harga keluar, asset rilis, status berubah, wiki updated).

---

## 2. Inti pola (7 lapisan)

Pola yang sama berulang setiap kali. Apa pun input-nya, melalui 7 lapisan ini:

```
[1] DETEKSI    → ada sinyal baru
[2] PAHAM      → ini apa, dari mana, tentang apa
[3] COCOKKAN   → masuk ke knowledge base yang mana
[4] NILAI      → dampak bisnis berapa, urgency level apa
[5] ARAHKAN    → siapa/apa yang harus bertindak
[6] VALIDASI   → lolos gate atau perlu human-in-loop
[7] KELUARKAN  → output bisnis konkret + log
```

Tujuh lapisan ini **deterministik per data class**. Artinya, untuk setiap jenis sinyal, jawaban di tiap lapisan sudah bisa dipre-defined. Yang dilakukan agent: jalankan lapisan berurutan, lalu eksekusi.

---

## 3. Lapisan detail

### Lapisan 1 — DETEKSI (Trigger)

**Pertanyaan**: Ada sinyal baru atau tidak?

**Sumber sinyal** (jenis trigger):
- **Push** — kejadian datang sendiri (review baru muncul, pesan WA masuk, booking masuk, refund diminta, cancellation)
- **Pull** — agent yang scan periodik (cek ranking SEO, cek mention AI, cek status volcano BBKSDA, cek hotel rates)
- **Schedule** — waktu tertentu (Senin pagi, Jumat sore, tanggal 25, akhir kuartal)
- **Internal** — perubahan di KB sendiri (SSOT version bump, wiki page edit, sprint item closed)

**Output lapisan 1**: paket data mentah + metadata (kapan terjadi, dari mana, jenis push/pull/schedule/internal).

### Lapisan 2 — PAHAM (Comprehension)

**Pertanyaan**: Apa isi sinyal ini sebenarnya?

**Yang dilakukan**:
- **Klasifikasi jenis**: review / inquiry / booking / news / vendor update / internal alert / dst.
- **Ekstraksi entitas**: destinasi mana, crew mana, paket mana, customer siapa, bahasa apa, sentimen apa.
- **Ekstraksi maksud**: pertanyaan / komplain / pujian / minta perubahan / minta refund / cuma share / dst.
- **Normalisasi**: format tanggal, harga (IDR), pax count, currency.

**Output lapisan 2**: representasi terstruktur — paket data dengan label + entity list + intent label.

### Lapisan 3 — COCOKKAN (Knowledge Match)

**Pertanyaan**: Sinyal ini terhubung ke knowledge base JVTO yang mana?

**Yang dicocokkan**:
- **Entitas yang disebut** → halaman wiki yang relevan (destinasi, crew, paket, claim C1-C9, kebijakan).
- **Pola serupa sebelumnya** → kasus historis yang mirip (review serupa, inquiry serupa, situasi serupa).
- **Aturan brand voice** → forbidden phrases ("blue fire guaranteed", dll), approved language untuk konteks Ijen, format harga IDR.
- **Aturan kebijakan** → cancellation policy, FOC, travel credit, deposit rules.
- **Status compliance** → BBKSDA SE, ISIC requirement, HPWKI training chain.

**Output lapisan 3**: bundle referensi — daftar wiki page yang berhubungan + aturan yang berlaku + kasus historis terdekat.

### Lapisan 4 — NILAI (Business Impact Assessment)

**Pertanyaan**: Seberapa penting ini? Dampaknya ke apa?

**Dimensi penilaian**:
- **Revenue impact**: rupiah hilang/dapat? deal pending? FOC peluang?
- **Trust impact**: review negatif publik? brand attack? mention di press?
- **Safety/compliance impact**: insiden? closure notice? regulatory change?
- **Operational impact**: crew conflict? hotel double-book? day-of issue?
- **Strategic impact**: signal pasar baru? competitor move? channel baru?

**Output dimensi**: skor per dimensi (rendah / sedang / tinggi / kritis).

**Output lapisan 4**: profil dampak agregat + level urgency (auto / soon / urgent / now).

### Lapisan 5 — ARAHKAN (Routing)

**Pertanyaan**: Aksi apa yang harus diambil, oleh siapa atau apa?

**Pilihan rute**:
- **Auto-act** — sistem langsung jalan (low risk, high confidence)
- **Auto-draft + approve** — sistem siapkan, manusia approve cepat
- **Escalate** — naikkan ke founder untuk keputusan
- **Park + monitor** — tidak ada aksi sekarang, masuk watch list
- **Update KB only** — tidak ada output eksternal, hanya wiki yang berubah

**Aturan routing berlapis**:
- Berdasarkan urgency dari lapisan 4
- Berdasarkan confidence agent (apakah pola cukup jelas)
- Berdasarkan policy (refund > Rp X selalu human, balasan WA pricing question boleh auto-draft)
- Berdasarkan workload (kalau auto queue penuh, tetap escalate)

**Output lapisan 5**: rute spesifik + action plan + siapa accountable.

### Lapisan 6 — VALIDASI (Gate)

**Pertanyaan**: Sebelum output keluar, sudah benar?

**Gate yang harus lolos** (semuanya, atau output diblokir):
- **Brand voice gate** — tidak melanggar voice invariants
- **Factual gate** — tidak ada klaim yang tidak ada di KB
- **Policy gate** — tidak melanggar kebijakan harga / cancellation / inclusion
- **Language gate** — bahasa & ton sesuai audience (ID/EN, formal/casual)
- **Privacy gate** — tidak ekspos PII customer lain / data internal
- **Legal/risk gate** — tidak menjanjikan yang regulatorinya bukan JVTO yang mengatur (mis. "guaranteed blue fire")

**Hasil gate**:
- Lolos semua → lanjut ke lapisan 7
- Ada flag → balik ke lapisan 5 dengan note (mungkin perlu human atau auto-revise)
- Hard fail → blokir, log, eskalasi

**Output lapisan 6**: keputusan boleh-rilis (yes/no/revise) + flag list jika ada.

### Lapisan 7 — KELUARKAN (Action + Log)

**Pertanyaan**: Eksekusi apa yang terjadi sekarang?

**Jenis output**:
- **Respond** — kirim balasan ke kanal asal (WA, email, review reply, web form follow-up)
- **Generate** — buat asset baru (quote PDF, brochure, social post, landing copy)
- **Update** — ubah state internal (wiki page, status booking, task list, watch list)
- **Trigger** — picu workflow lain (deploy, publish, schedule)
- **Notify** — kasih tahu owner/crew (briefing, alert, summary)
- **Decide** — ambil keputusan logis (set price, assign crew, pick hotel)

**Wajib hadir setiap output**: **log lengkap**.
- Apa sinyal asal
- Klasifikasi di tiap lapisan
- Rute yang dipilih + alasan
- Gate yang dilewati
- Output final + timestamp
- Reversible? (kalau salah, bagaimana undo)

**Output lapisan 7**: action executed + log entry permanent.

---

## 4. Taksonomi "data baru" untuk JVTO

Apa saja yang menjadi trigger valid? Dikelompokkan agar setiap kelas punya playbook tersendiri.

### Kelas A — Sinyal Customer (eksternal, dari calon/customer)
- A1. WA inquiry baru (cold — belum ada history)
- A2. WA follow-up (warm — sudah ada thread)
- A3. Email inquiry baru
- A4. Form submission website
- A5. Review baru (Google / Trustpilot / TripAdvisor)
- A6. Complaint formal
- A7. Refund request
- A8. Cancellation
- A9. Late/no payment
- A10. Reschedule request

### Kelas B — Sinyal Operasional (eksternal, dari rekanan/lingkungan)
- B1. Hotel rate update dari vendor
- B2. Vehicle issue (rusak, driver sakit)
- B3. Weather/volcano alert (BBKSDA closure, gas activity tinggi)
- B4. Day-of issue (no-show, delay, accident)
- B5. Partner update (HPWKI/INDECON/ISIC change)
- B6. Crew availability change (sakit, cuti, conflict)
- B7. Permit / regulatory change (BBKSDA SE baru, KBLI update)

### Kelas C — Sinyal Knowledge (internal)
- C1. SSOT version bump
- C2. DB export refresh (booking, finance, reviews update)
- C3. Wiki page edit (founder atau staff)
- C4. New source ditemukan (web clip, press mention)
- C5. Health check finding (contradiction, stale claim, orphan)

### Kelas D — Sinyal Market (eksternal, intelligence)
- D1. Competitor new content/page
- D2. Keyword volume / ranking drift
- D3. Brand mention di AI search results
- D4. Press / media baru menyebut JVTO atau competitor
- D5. Travel advisory change (untuk source country)
- D6. Social trend (Indonesia tourism, Bromo/Ijen mentions)

### Kelas E — Sinyal Internal (terjadwal / state-driven)
- E1. Schedule recurring (Senin pagi, Jumat sore, tanggal 25)
- E2. Sprint cycle event (start sprint, end sprint, retro)
- E3. Quarterly review trigger
- E4. Tax deadline trigger
- E5. Approval queue threshold (X items menunggu)
- E6. KPI breach (margin di bawah X%, response time di atas Y jam)

### Kelas F — Sinyal Booking-flow (semi-internal, semi-customer)
- F1. New booking confirmed
- F2. Deposit received
- F3. Balance due in N days
- F4. T-N days pre-tour (briefing time)
- F5. Tour day commencement
- F6. Tour day completion
- F7. Post-tour day +1 (review request window)
- F8. Post-tour day +7 (follow-up window)

Setiap kelas (~50 jenis trigger) punya: priority default, default route, default validation profile.

---

## 5. Logika keputusan per lapisan (matriks ringkas)

Tabel pendek menunjukkan bagaimana 7 lapisan diisi berbeda per kelas data:

| Kelas | Klasifikasi (L2) | Cocokkan (L3) | Nilai (L4) | Arahkan (L5) | Validasi (L6) | Output (L7) |
|---|---|---|---|---|---|---|
| A1 (WA cold) | inquiry, intent: pricing/info | matched paket, destinasi disebut | revenue: lead value · trust: low risk | auto-draft + approve cepat | brand+language+policy | reply WA |
| A5 (review ≤3★) | review negatif | crew disebut → people page · pola serupa | trust: HIGH · revenue: brand risk | auto-draft + founder approve | brand+factual+legal | reply review + KB update |
| A7 (refund) | refund req | policy match: cancellation rules | revenue: nominal · legal: tinggi | escalate ke founder | full gate | structured response + decision log |
| B3 (volcano closure) | safety alert | impacted bookings × policy | safety: kritis · revenue: tinggi | auto-notify affected + escalate ops | factual+language | mass-comm + reschedule offer |
| B4 (day-of issue) | operational | booking + crew + customer | ops: kritis · trust: tinggi | escalate immediate | factual+legal | direct comm + incident log |
| C1 (SSOT bump) | knowledge update | wiki global | strategic: sedang | update KB only + flag dependent | factual gate | wiki re-sync |
| C4 (new source) | knowledge | wiki sources/* | strategic: sedang | auto-ingest workflow | factual | new source page + cross-link |
| D1 (competitor) | market intel | seo/competitors | strategic: variable | park + watchlist | — | watch entry + monthly report |
| D3 (AI mention) | brand presence | brand voice + claims | trust: sedang | auto-monitor + summary | — | brand pulse update |
| E1 (Monday brief) | recurring | KB cross-domain | strategic: low-med | auto-act | factual | briefing artifact |
| F1 (new booking) | booking conf | customer + package + crew | revenue: rupiah · ops: schedule | auto-draft (welcome + crew alloc) | brand+factual | confirmation + crew assignment |
| F7 (post-tour day +1) | review window | last booking | trust: tinggi (peluang) | auto-act | brand+language | review request message |

Setiap row di atas adalah **playbook deterministik**. Sistem tidak perlu "berpikir creative" untuk kasus standar — pola sudah pre-defined. Yang dibuat agent hanya: jalankan playbook + isi konten sesuai konteks.

Agent jadi "pintar" hanya di:
- Kasus ambigu (kelas tidak jelas) → tanya / escalate
- Konten draft (mengisi blank di template) → generative dengan KB grounding
- Confidence assessment (apakah ini benar-benar kelas A1 atau borderline) → probabilistic

---

## 6. State + invariants (apa yang harus selalu benar)

Sistem agentic stabil hanya kalau invariants berikut dipegang:

1. **Setiap output bisa dilacak balik ke sinyal pemicunya** (audit trail tidak boleh putus).
2. **Setiap klaim dalam output bisa dirujuk ke KB** (tidak ada fabrikasi).
3. **Setiap aksi yang punya konsekuensi finansial ≥ ambang X selalu butuh human approval** (boundary tegas).
4. **Brand voice invariants tidak pernah dilanggar di output otomatis** (gate hard-fail).
5. **Customer PII tidak pernah leak antar kasus** (privacy boundary).
6. **Knowledge base hanya boleh diupdate oleh proses yang ter-logged** (tidak ada silent edit).
7. **Sistem tahu kapan ia tidak tahu** — confidence rendah selalu eskalasi, tidak auto-act ngebut.
8. **Setiap recurring action punya kill switch** — owner bisa stop satu jenis aksi tanpa stop yang lain.
9. **State data trigger tidak hilang sampai loop selesai** — kalau Layer 7 gagal, sinyal masih tersedia untuk retry.
10. **Versi playbook tertulis dan ber-diff** — perubahan policy bisa di-rollback.

Invariants ini bukan implementasi detail; ini **kontrak** yang harus dipenuhi siapa pun yang membangun ABRS — apa pun stack-nya nanti.

---

## 7. Worked examples (3 kasus, fokus polanya)

### Contoh 1 — Review 2★ baru muncul di Google Maps mention crew "Yandi"

| Lapisan | Apa yang terjadi |
|---|---|
| 1. Deteksi | Pull cycle Google Maps cek, ada review baru, 2★, mention "Yandi" |
| 2. Paham | Klasifikasi: review negatif. Entitas: crew = Yandi (driver). Intent: complaint operasional. Bahasa: EN. Sentimen: negatif sedang. |
| 3. Cocokkan | KB match: people/crew-registry (Yandi profile), reviews/* (history Yandi), brand-voice (review reply tone), policy (operational issue). Kasus serupa: 2 review sebelumnya 4★ mention Yandi → tidak pola sistemik. |
| 4. Nilai | Trust: TINGGI (public, ranking impact). Revenue: rendah (1 review tidak material). Strategic: rendah (bukan pola). Urgency: SOON (≤24 jam). |
| 5. Arahkan | Auto-draft reply + founder approve. Cc: tim ops untuk validasi konteks dengan Yandi. |
| 6. Validasi | Brand voice check ✓. Factual: tidak ada klaim, balas empati ✓. Language: EN ✓. Privacy: tidak sebut customer lain ✓. |
| 7. Keluarkan | Draft tersimpan di approval queue. KB update: catatan di reviews/review-patterns. Watch-list: monitor Yandi 2 review berikutnya. Log lengkap. |

### Contoh 2 — Volcano alert BBKSDA: Ijen ditutup 3 hari kedepan

| Lapisan | Apa yang terjadi |
|---|---|
| 1. Deteksi | Pull scan BBKSDA / PVMBG status, status berubah dari "open" ke "closed 3 days". |
| 2. Paham | Klasifikasi: safety/operational alert. Entitas: Kawah Ijen, periode T+0..T+3. Maksud: regulatory closure. |
| 3. Cocokkan | KB: destinations/kawah-ijen (status field), credentials/medical-screening (BBKSDA chain), policy (closure/reschedule). Booking impact: query DB → 4 bookings melibatkan Ijen di window itu. |
| 4. Nilai | Safety: KRITIS. Revenue: 4 bookings × value. Trust: TINGGI (komunikasi salah → kepercayaan rusak). Urgency: NOW. |
| 5. Arahkan | Multi-track: (a) Auto-notify 4 customer affected. (b) Escalate founder untuk keputusan reschedule/credit. (c) Update destination page status field. (d) Push WA blast policy. |
| 6. Validasi | Brand voice ✓. Factual: kutip sumber BBKSDA ✓. Policy: opsi reschedule + credit sesuai kebijakan ✓. Legal: tidak menjanjikan reopen date ✓. |
| 7. Keluarkan | 4 WA + email keluar (template "Ijen Closure Notice"). Founder dapat decision queue. destination page status updated. log lengkap. |

### Contoh 3 — WA inquiry: "Berapa harga 3 hari Bromo Ijen untuk 4 orang dari Surabaya?"

| Lapisan | Apa yang terjadi |
|---|---|
| 1. Deteksi | Push: WA Pro CRM webhook, message baru, sender baru (no history). |
| 2. Paham | Klasifikasi: inquiry pricing. Entitas: 3 hari, Bromo, Ijen, 4 pax, Surabaya start. Bahasa: ID. Intent: minta penawaran. |
| 3. Cocokkan | KB: products/packages-overview → "Ijen Bromo Madakaripura 3D2N from Surabaya" cocok 90%. Pricing table → 4 pax tier. Policy → deposit 20%. Brand voice → ID conversational. |
| 4. Nilai | Revenue: lead. Trust: rendah-sedang. Urgency: SOON (response time = trust signal). |
| 5. Arahkan | Auto-draft balasan: harga, inclusions ringkas, link, ajakan ke discovery. |
| 6. Validasi | Brand voice ✓ (ID, no forbidden phrases). Factual: harga dari rate cards ✓ (tidak fabrikasi). Policy: deposit rule benar ✓. Format harga IDR ✓. |
| 7. Keluarkan | Draft WA reply siap. Owner approve 1 klik → kirim. KB update: kontak baru di customer log. State: thread sekarang "warm — awaiting reply". |

Tiga contoh, tiga jenis sinyal (review/operational alert/inquiry), pola **persis sama**.

---

## 8. Boundary — apa yang ABRS ADALAH dan BUKAN

### ABRS ADALAH
- Sistem reactive — bertindak karena ada sinyal yang masuk
- Pattern-driven — playbook deterministik per kelas data, generative hanya untuk content
- KB-grounded — semua keputusan dirujuk wiki/SSOT
- Audit-able — setiap aksi log balik ke sinyal
- Multi-channel output — bisa keluar ke WA, email, review platform, KB, deploy pipeline, briefing
- Bertanggung jawab di tier "high-frequency, low-individual-stake" + "low-frequency, high-stake dengan human gate"

### ABRS BUKAN
- Bukan general chatbot / AI assistant untuk tanya jawab
- Bukan creative content generator yang berdiri sendiri (asset generation HARUS via trigger + playbook)
- Bukan replacement founder judgment di keputusan strategis (escalate ada porsi)
- Bukan oracle prediksi pasar (D-class hanya watch & summary, bukan decision)
- Bukan workflow engine yang bisa improvise di luar playbook
- Bukan reservoir konten yang dipanggil "tulisin saya post hari ini" — ini reactive, bukan generative-on-demand
- Bukan substitute untuk wiki/SSOT — KB tetap source of truth, ABRS hanya processor

---

## 9. Mindset prerequisite (sebelum sistem dibangun)

Sebelum bicara tools, ini yang harus ditetapkan:

1. **Setiap kelas data sudah dipetakan** — kelas A-F di atas adalah konsep awal; perlu validasi semua kelas terdeteksi.
2. **Setiap kelas punya playbook tertulis** — bukan "minta AI mikir setiap kali"; pola pre-defined.
3. **Threshold escalation eksplisit** — angka rupiah, level urgency, confidence cutoff.
4. **Brand voice = struktur, bukan vibes** — invariants harus machine-checkable (regex bisa, atau rule explicit).
5. **KB versioning disiplin** — kalau wiki page berubah, downstream playbook tahu.
6. **Audit log = first-class citizen** — bukan afterthought; setiap output punya record permanen.
7. **Kill switch per kelas** — founder bisa freeze "auto-reply WA" tanpa freeze "review monitoring".
8. **Failure mode dipikirkan dulu** — apa yang terjadi kalau lapisan 3 gagal cocokkan? kalau gate flag tapi user butuh response cepat?
9. **Owner approval queue tidak boleh jadi bottleneck baru** — UI/UX queue penting; satu approval = 5 detik bukan 5 menit.
10. **Pola harus tetap sama meskipun input new** — kalau muncul kelas G besok (mis. partner baru, channel baru), sistem tinggal tambah playbook, bukan rebuild.

---

## 10. Ringkasan inti (1 paragraf)

JVTO ABRS adalah **mesin reaksi** dengan 7 lapisan tetap (deteksi → paham → cocokkan → nilai → arahkan → validasi → keluarkan) yang diisi dengan **playbook deterministik per kelas data** (A=customer, B=ops, C=knowledge, D=market, E=internal/schedule, F=booking-flow). KB JVTO (wiki + SSOT + brand voice + policy) adalah ground truth; tidak ada output yang lolos tanpa di-anchor di KB. Sistem auto-act di kasus high-frequency low-stake, auto-draft + approve di sebagian besar, escalate di high-stake / low-confidence. Invariants 10 baris di Section 6 adalah kontrak yang harus dipegang siapa pun yang mengimplementasi — apa pun stack-nya.

---

*End of blueprint. Status: conceptual baseline. Implementation, tooling, dan tech-stack pilihan adalah pembahasan terpisah yang baru relevan SETELAH playbook per kelas data diturunkan ke level detail.*
