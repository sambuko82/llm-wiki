---
type: ops
title: JVTO WhatsApp Operations Playbook
last_updated: 2026-05-14
sources: [jvto-homepage-clip, ssot-v6, jvto-policy-pack-v6, db-export-2026-05, operational-facts, wa-pro-crm-api]
companion: 2026-05-14-whatsapp-rules-engine
---

# JVTO WhatsApp Operations Playbook

> Playbook ini menghubungkan **lima alur WhatsApp** yang sekarang ditangani JVTO menjadi satu sistem operasional yang dapat dibaca, diikuti, diukur, dan diotomatisasi secara bertahap.
> Audiens utama: Sam (founder, sebagai pengambil keputusan), Inan (staf operasional), David (IT, untuk membangun tooling pendukung).
> Dokumen ini bukan spek teknis. Dokumen ini adalah *peta operasi*. Spek teknis dibuat di Claude Code setelah playbook ini disetujui.
>
> **Untuk eksekusi langsung (AI atau staf baru):** baca companion document -> [[ops/2026-05-14-whatsapp-rules-engine]] — logika murni, tanpa filosofi, dapat diikuti tanpa interpretasi.

---

## 1. Mengapa Playbook Ini Ada

WhatsApp adalah antarmuka utama bisnis JVTO ke dunia luar — sales, concierge, koordinasi vendor, dispatch crew, semua lewat aplikasi ini. Tetapi WhatsApp diperlakukan sebagai inbox bebas: satu nomor menampung lima fungsi berbeda yang ditangani oleh satu orang (Inan), tanpa pemisahan kanal, tanpa prioritas, tanpa SLA tertulis, tanpa pemetaan customer otomatis ke status booking.

Akibatnya:

- Inan keteteran. Lima mode berpikir (sales / concierge / pre-tour ops / B2B / internal) ditumpuk di satu kepala, sepanjang hari, lintas zona waktu.
- Sam tidak punya visibilitas operasional. Tidak ada cara cepat tahu "berapa inquiry yang menunggu" atau "tour besok semua confirm atau belum".
- Risiko bisnis. Inquiry tidak dibalas berjam-jam = konversi hilang. Window Travel tidak dapat confirmation = vendor relationship terganggu. Crew dispatch yang campur dengan tamu = miskomunikasi operasional.
- Risiko teknis. Nomor WhatsApp dipakai via gateway non-resmi (WA Pro CRM) tanpa rate limiting yang disengaja, ada risiko di-ban Meta.

Playbook ini menyusun ulang lima alur WhatsApp tersebut menjadi sistem yang **terpetakan, terukur, dan dapat di-otomatisasi secara bertahap**, tanpa membongkar infrastruktur yang sudah berjalan.

---

## 2. Yang JVTO Sudah Miliki (Inventory)

### 2.1 Sumber Daya Manusia

| Peran | Nama | Kapasitas | Tanggung Jawab Saat Ini |
|---|---|---|---|
| Founder | Sam (Agung Sambuko) | Part-time (juga aktif sebagai Tourist Police) | Strategi, closing inquiry tinggi-nilai, escalation final |
| Operasional WA | Inan | Full-time | Semua channel WhatsApp, vendor/crew coordination |
| IT / Developer | David | Full-time | WA Pro CRM, back office, integrasi |
| Medis | Dr. Ahmad Irwandanu | On-call | Skrining medis Ijen — lihat -> [[people/dr-ahmad-irwandanu]] |
| Crew | Driver, guide, registry | Variable | Eksekusi tour — lihat -> [[people/crew-registry]] |

**Catatan kritis:** Inan = single point of failure. Tidak ada backup. Sakit/cuti = sistem mati.

### 2.2 Infrastruktur Teknis (yang sudah jalan)

- **WA Pro CRM** — gateway WhatsApp internal yang dibangun David. REST API v1 + webhook. Saat ini dipakai hanya untuk: trigger booking → kirim notifikasi ke vendor → kirim notif ke tamu → input ke database. **Inbound chat handling belum diimplementasi.**
- **Back office Laravel** di `new-backoffice.javavolcano-touroperator.com`. Sudah ada Finance Cockpit (Week 3), Booking Overview API (`/booking-overview/api`).
- **MySQL `u1805424_jvto_clone`** sebagai operational database (booking, customer, transaksi).
- **PostgreSQL** di JVTO website utama.
- **llm-wiki** (dokumen ini ada di sini) sebagai content knowledge base.

### 2.3 Aset Konten (untuk grounding AI nantinya)

| Aset | Lokasi | Fungsi dalam playbook |
|---|---|---|
| Brand voice guide | -> [[website/brand-voice]] | Acuan tone semua balasan |
| FAQ master | -> [[website/faq-master]] | Sumber jawaban FAQ otomatis |
| AEO claims | -> [[website/aeo-claims]] | Klaim yang aman dikutip publik |
| Copy bank | -> [[website/copy-bank]] | Frasa & template terverifikasi |
| Operational facts | -> [[website/operational-facts]] | Fakta operasional (jam, lokasi, harga) |
| **Canned responses** | -> [[ops/canned-responses]] | **Template WA + email siap kirim per stage (Triage/Discovery/Proposal/Closing + post-booking), bilingual ID/EN** |
| Destinations | -> [[destinations/kawah-ijen]], [[destinations/mount-bromo]], [[destinations/tumpak-sewu]], [[destinations/madakaripura]], [[destinations/papuma-beach]] | Info destinasi |
| Pricing & itinerary | -> [[products/packages-full-pricing]], -> [[products/packages-itineraries]] | Acuan kuotasi (manual, bukan otomatis) |
| Policy pack | -> [[sources/jvto-policy-pack-v6]] | Booking, payment, cancellation rules |
| Reviews | -> [[reviews/trustpilot-compilation]], -> [[reviews/review-patterns]] | Social proof untuk reply tertentu |

### 2.4 Workflow yang Sudah Berjalan

1. Customer booking via Klook atau website JVTO → webhook ke WA Pro CRM
2. WA Pro CRM → trigger booking hotel ke vendor (lewat WA atau email — perlu konfirmasi alurnya)
3. WA Pro CRM → kirim notifikasi konfirmasi ke tamu
4. WA Pro CRM → tulis ke database `u1805424_jvto_clone`

**Yang BELUM ada:** semua interaksi *setelah* langkah-langkah di atas (chat masuk dari tamu, pertanyaan, perubahan jadwal, koordinasi B2B, dispatch internal) ditangani manual oleh Inan tanpa sistem.

---

## 3. Pin Points — Diagnosis Situasi

Disusun dari yang paling kritis ke paling minor.

### 3.1 Strategis

1. **Lima fungsi, satu otak.** Inan menjalankan sales (JVTO inquiry), concierge (post-booking), service desk (Klook), account management (Window Travel), dan internal ops (vendor + crew). Tiap fungsi punya tone, otoritas, dan SLA berbeda. Tidak ada satu pun bisnis yang skala-nya seperti ini dengan struktur seperti ini.

2. **Inan = single point of failure.** Bus factor = 1. Tidak ada playbook tertulis, tidak ada backup orang, tidak ada documented escalation.

3. **Sales channel paling penting tidak diproteksi.** JVTO direct inquiry = leads paling tinggi-nilai (margin penuh, repeat-potential, brand-defining). Tetapi diberi prioritas sama dengan FAQ Klook ("kapan pickup?"). Ini salah desain.

4. **Tidak ada visibilitas untuk Sam.** Sam tidak tahu kondisi operasi hari ini tanpa bertanya Inan. Founder tanpa dashboard = blind founder.

### 3.2 Operasional

5. **Tidak ada pemetaan otomatis nomor → channel.** Saat chat masuk, Inan harus ingat sendiri: "ini tamu Klook" atau "ini Window" atau "ini inquiry baru". Mental load yang seharusnya dihilangkan dengan database lookup.

6. **Tidak ada state machine customer.** Tidak ada cara cepat tahu "tamu ini di tahap inquiry, quoted, booked, atau post-tour". Setiap kali Inan harus scroll riwayat chat untuk tahu konteks.

7. **Multi-zona waktu Eropa tidak di-handle.** Inquiry masuk jam 02:00 WIB (jam kerja Eropa) dibaca Inan jam 08:00 WIB = sudah 6 jam terlambat respond. Tidak ada auto-acknowledgment.

8. **Multi-bahasa tidak terkelola.** EN dominan, tapi ada permintaan ID, MS (Window Travel), kemungkinan DE/FR/ES dari Eropa. Inan tidak fluent di semua. Tidak ada template multilingual.

9. **Vendor & crew di-mix dengan tamu.** Inan menjawab "Pak Hartono siap pickup jam 00:30?" di tengah-tengah menjawab pertanyaan tamu Eropa. Context-switching mahal.

10. **Tidak ada SLA tertulis.** Tidak ada komitmen internal: "JVTO inquiry harus dibalas dalam 30 menit business hours". Tanpa SLA, tidak ada cara ukur sukses. *Benchmark internasional*: WA/Live Chat maks 2–5 menit (otomatis), email maks 2–4 jam hari kerja. Sumber: -> [[sources/comm-management-theory]] §SLA-Standards.

### 3.3 Risiko Teknis & Compliance

11. **WA Pro CRM = WhatsApp gateway non-resmi.** Bukan WhatsApp Business API resmi (Meta Cloud API). Risiko nomor di-ban kalau pola pengiriman terlalu botty atau volume terlalu agresif. Nomor JVTO = aset bisnis dengan ribuan kontak tamu. Kalau hilang, hilang permanen.

12. **Data tamu Eropa = GDPR exposure.** Personal data nama, nomor, paspor (mungkin), riwayat tour Eropa tersimpan di DB Indonesia, diproses via gateway non-resmi, kalau nanti pakai LLM US-based = ada eksposur. Tidak fatal untuk bisnis kecil, tapi harus disadari.

13. **Kredensial database pernah muncul di chat.** Best practice belum diterapkan secara disiplin. Akan jadi masalah saat tim membesar.

---

## 4. Tujuan yang Ingin Dicapai

Disusun sebagai outcome statement, bukan output statement (yaitu: apa yang berubah, bukan apa yang dibuat).

### 4.1 Outcome Inan
- Inan tidak lagi "keteteran". Stress level mingguan turun dari baseline ≥3 poin (skala 1-10, self-report).
- Inan hanya menyentuh pesan yang **wajib** dia tangani; sisanya di-handle sistem.
- Inan punya kerangka jelas: kapan dia memutuskan sendiri, kapan dia eskalasi ke Sam.

### 4.2 Outcome Sam
- Sam tahu kondisi operasi tanpa bertanya Inan, kapan pun ia mau.
- Sam fokus ke JVTO direct inquiry tinggi-nilai (closing) dan strategi, tidak terganggu hal-hal kecil.
- Sam tahu skor & risiko setiap tour besok pagi sebelum tidur, atau pagi setelah bangun.

### 4.3 Outcome Customer
- Pesan tamu Eropa di luar jam kerja Indonesia mendapat balasan profesional dalam <5 menit (auto-acknowledgment dengan ETA jujur).
- FAQ Klook dijawab konsisten dengan brand voice JVTO, bukan jawaban ad-hoc Inan yang kadang panjang kadang asal.
- Tamu JVTO direct merasa di-handle Sam atau Inan secara personal, bukan oleh bot — karena yang automated hanya yang seharusnya automated.

### 4.4 Outcome Bisnis
- Konversi JVTO direct inquiry → booking minimal terjaga (target: naik 10-20% dari baseline saat ini).
- Window Travel relationship terkelola dengan komitmen waktu respons B2B yang jelas.
- Klook customer satisfaction tetap atau naik (proxy: review rate, repeat).
- Tidak ada nomor WA di-ban Meta.

### 4.5 Outcome Sistemik
- 5 channel WhatsApp memiliki flow tertulis yang Inan, Sam, dan staf masa depan bisa ikuti.
- AI/otomatisasi dipasang **secara bertahap dengan ambang yang terukur**, bukan all-or-nothing.
- Setiap intervensi AI bisa dimatikan tanpa membongkar sistem (graceful degradation).

---

## 5. Pemetaan 5 Kanal WhatsApp JVTO

Setiap kanal punya identitas, audiens, tone, otoritas, dan SLA berbeda. Memperlakukan semuanya sama = sumber chaos saat ini.

| Kanal | Audiens | Stage | Tone | Otoritas | SLA Target |
|---|---|---|---|---|---|
| **A. JVTO Inquiry** | Calon tamu yang belum booking | Pre-sale | Direct, evidence-led, police-led trust | Sam approve untuk pricing/commitment | <30 menit business hours, <6 jam off-hours (dengan auto-ack) |
| **B. JVTO Post-Booking** | Tamu JVTO yang sudah bayar | Booked → in-tour → post-tour | Hangat, personal, reassuring | Inan, eskalasi ke Sam untuk perubahan besar | <15 menit untuk H-2 ke H+1, <2 jam lainnya |
| **C. Klook Customer** | Tamu yang booking via Klook | Booked (sudah bayar di platform) | Service-desk profesional, info-rich | Inan, tidak ada otoritas pricing/refund (semua via Klook) | <1 jam untuk FAQ, <15 menit untuk pickup-day logistik |
| **D. Window Travel B2B** | Agent travel Malaysia (Sarah?) | B2B account | Profesional, peer-to-peer, transactional | Inan, eskalasi Sam untuk commitment besar | <2 jam business hours, batch-able off-hours |
| **E. Vendor & Crew Ops** | Hotel, restaurant, driver, guide | Internal eksekusi | Singkat, instruksional, action-oriented | Inan, Sam tahu garis besar | <30 menit untuk hari-H, <4 jam lainnya |

**Insight kritis:** A dan B (JVTO sendiri) adalah **revenue channel**. C dan D adalah **fulfillment channel** (tamu sudah bayar di tempat lain — pekerjaan kita = eksekusi tour dengan baik). E adalah **internal ops**.

Memperlakukan ketiga kategori ini dengan prioritas dan ekspektasi yang sama = salah alokasi perhatian.

---

## 6. Funnel & Flow per Kanal

Setiap flow ditulis sebagai *state machine* dengan pemicu eksplisit. Format konsisten:

- **Stage** — di mana customer berada
- **Pemicu masuk** — apa yang menyebabkan customer masuk stage ini
- **Aksi sistem** — apa yang otomatis terjadi
- **Aksi manusia** — apa yang Inan/Sam lakukan
- **Pemicu keluar** — apa yang menyebabkan customer keluar stage ini
- **Risk / Watch** — yang harus dipantau

---

### Flow A: JVTO Inquiry Funnel

> Calon tamu yang mengontak JVTO langsung (via WA dari website, referral, review platforms). Channel paling **bernilai tinggi** dan paling **mudah hilang** kalau lambat respons.

```
[A1: Cold Touch] → [A2: Qualified] → [A3: Quoted] → [A4: Negotiating] → [A5: Booked]
                                                          │
                                                          └── [A0: Lost / Ghost]
```

#### A1: Cold Touch
- **Pemicu masuk:** Pesan pertama dari nomor yang tidak ada di database JVTO.
- **Aksi sistem:** 
  - Cek nomor di `bookings`, `klook_bookings`, `window_contacts` — tidak ada match.
  - Tag conversation: `channel=jvto_direct, state=inquiry`.
  - Kalau di luar jam kerja Inan: kirim auto-acknowledgment dalam <2 menit. Format:
    > "Halo, terima kasih sudah menghubungi JVTO. Inan/Sam akan membalas detail tour Anda dalam X jam (jam kerja kami: 08:00–22:00 WIB / UTC+7). Sementara menunggu, Anda bisa lihat paket tour kami di [link]."
  - Bahasa auto-ack: detect dari pesan customer (EN default, ID/MS kalau jelas).
- **Aksi manusia:** Inan baca pesan, qualify (lihat A2 criteria).
- **Pemicu keluar:** Inan/Sam membalas substansial pertama kali → naik ke A2.
- **Risk / Watch:** Tidak dibalas >6 jam off-hours atau >30 menit business hours = risiko ghost.

#### A2: Qualified
- **Pemicu masuk:** Inan/Sam sudah merespons dan customer balas balik dengan info konkret (destinasi, tanggal, pax).
- **Aksi sistem:** Update state ke `qualified`. Log info dasar: destinasi, tanggal (jika ada), pax (jika ada), bahasa, asal negara.
- **Aksi manusia (Inan):** 
  - Konfirmasi 3 hal minimum: **destinasi + tanggal + pax**. Gunakan BANT qualification framework: N (kebutuhan + tipe tur), T (tanggal pasti vs tentatif), B (preferensi hotel sebagai proxy budget), A (pengambil keputusan). Template skrip: -> [[ops/canned-responses]] §Stage-2-Discovery.
  - Kalau pricing question → **eskalasi ke Sam** atau pakai pricing dari -> [[products/packages-full-pricing]] (tidak boleh improvisasi harga).
  - Kalau customer minta "kasih saya itinerary lengkap" → kirim itinerary dari -> [[products/packages-itineraries]].
- **Pemicu keluar:** 
  - Sam/Inan kirim quotation formal → A3.
  - Customer tidak balas >48 jam setelah Inan kirim quotation → A0 (Lost / Ghost, tagged for follow-up).
- **Risk / Watch:** Customer Eropa biasanya butuh detail pricing + itinerary lengkap sebelum commit. Kalau Inan kasih jawaban singkat = signal "tidak profesional" untuk standar Eropa.

#### A3: Quoted
- **Pemicu masuk:** Quotation formal sudah dikirim (dengan harga, inclusion, exclusion, terms).
- **Aksi sistem:** Set reminder 48 jam — kalau tidak ada balasan, tag untuk follow-up.
- **Aksi manusia:**
  - Tunggu respons customer.
  - Kalau ada pertanyaan klarifikasi (inclusion, jam, single vs twin) → jawab langsung pakai -> [[website/operational-facts]].
- **Pemicu keluar:**
  - Customer setuju, minta payment instruction → A4.
  - Customer minta nego (diskon, perubahan paket) → A4.
  - 48 jam tanpa response → trigger follow-up (Inan kirim "ringkasan + nudge").
  - 7 hari tanpa response → A0.
- **Risk / Watch:** Ini stage paling sering bocor. Bagian quotation harus dapat akses langsung ke pricing table & template.

#### A4: Negotiating / Confirming
- **Pemicu masuk:** Customer commit untuk lanjut atau minta perubahan.
- **Aksi sistem:** Generate payment instruction (rekening, terms, deadline DP).
- **Aksi manusia (Sam atau Inan, tergantung otoritas):**
  - Kalau diskon diminta → **Sam approve**, bukan Inan.
  - Kalau perubahan jadwal/paket → konfirmasi kapasitas vendor & crew dulu (lihat Flow E).
  - Kirim payment instruction, ekspektasi DP, deadline.
- **Pemicu keluar:**
  - Customer transfer DP → A5.
  - Customer menghilang setelah payment instruction → A0 setelah 5 hari.
- **Risk / Watch:** Jangan janjikan harga di luar standar pricing tanpa otorisasi Sam. Track diskon yang diberikan (siapa, kenapa, berapa).

#### A5: Booked
- **Pemicu masuk:** DP diterima, booking dibuat di DB.
- **Aksi sistem:**
  - Webhook trigger booking → vendor coordination (Flow E).
  - Notifikasi konfirmasi ke customer (template formal).
  - Transition state: `jvto_direct` channel berubah dari `inquiry` ke `booked` → masuk Flow B.
- **Aksi manusia:** Tidak ada (sudah otomatis). Inan monitor saja.
- **Pemicu keluar:** Customer lulus dari A → masuk ke Flow B.
- **Risk / Watch:** Confirmation harus jelas: tanggal, jam pickup, lokasi pickup, dokumen yang harus dibawa. Banyak komplain post-tour datang karena pre-tour info kurang lengkap.

#### A0: Lost / Ghost
- **Pemicu masuk:** Customer tidak respons dalam window time-out di salah satu stage di atas.
- **Aksi sistem:** Tag `lost`, simpan riwayat. Optional: masukkan ke remarketing list nanti.
- **Aksi manusia:** Tidak ada immediate. Bisa di-mining periodik untuk re-outreach.
- **Risk / Watch:** Jangan agresif follow-up — ganggu brand. Maksimum 2 nudges (48 jam + 7 hari) lalu let go.

#### Titik intervensi AI/otomatisasi di Flow A
- **A1 auto-ack off-hours**: aman, tinggi value, low risk → **otomatisasi penuh**.
- **A2 qualification helper**: AI bisa draft pertanyaan lanjutan ("Anda merencanakan tour untuk berapa orang dan tanggal berapa?") → **draft → Inan kirim**.
- **A3 quotation drafting**: AI compose draft quotation berdasarkan info dari A2 + pricing dari wiki → **draft → Sam approve sebelum kirim**.
- **A4-A5**: **tidak ada AI**. Pricing & commitment = manusia.

---

### Flow B: JVTO Post-Booking Concierge

> Tamu JVTO sendiri yang sudah membayar. Tujuannya: persiapan smooth, in-tour smooth, post-tour positive review.

```
[B1: Confirmation] → [B2: Pre-Tour Prep (H-7 to H-1)] → [B3: D-Day] → [B4: In-Tour] → [B5: Post-Tour] → [B6: Review Request]
```

#### B1: Confirmation
- **Pemicu masuk:** Booking dibuat (dari A5 atau direct booking via website).
- **Aksi sistem:**
  - Kirim email + WA confirmation: ringkasan booking, jadwal, dokumen pendukung (invoice, voucher).
  - Schedule reminder series untuk B2.
- **Aksi manusia:** Inan verifikasi data customer sudah lengkap (paspor name match, kontak darurat, dietary restriction, special request).
- **Pemicu keluar:** Tanggal tour - 7 hari → naik ke B2.

#### B2: Pre-Tour Prep
- **Pemicu masuk:** Tour minus 7 hari hingga minus 1 hari.
- **Aksi sistem (otomatisasi tinggi mungkin):**
  - **H-7**: Welcome message + checklist persiapan (pakaian, fisik, dokumen). Ambil dari -> [[website/faq-master]].
  - **H-3**: Konfirmasi jam pickup, lokasi pickup, kontak driver. **Tetapi**: jam & lokasi diambil dari operational DB, **bukan dari LLM**.
  - **H-1**: Reminder + cek terakhir (flight detail kalau ada, akomodasi night 0, kesehatan).
- **Aksi manusia (Inan):**
  - Jawab pertanyaan customer (mostly FAQ) — gunakan template dari wiki.
  - Cek vendor confirmation (Flow E) — semua hotel & crew sudah locked?
  - Eskalasi ke Sam kalau ada permintaan khusus yang tidak bisa Inan putuskan.
- **Pemicu keluar:** Tanggal tour = H-0 → naik ke B3.
- **Risk / Watch:** Tamu Ijen butuh skrining medis. Pastikan Dr. Irwandanu jadwal cocok — lihat -> [[people/dr-ahmad-irwandanu]].

#### B3: D-Day
- **Pemicu masuk:** Pagi hari tour.
- **Aksi sistem:**
  - Pesan "selamat menikmati tour" + nomor kontak driver/guide.
  - Sam dapat ringkasan tour hari ini (apakah perlu dia tahu apa-apa khusus).
- **Aksi manusia (Inan):**
  - Standby untuk emergency. Pastikan crew sudah dispatch (Flow E).
- **Pemicu keluar:** Tour dimulai → B4.
- **Risk / Watch:** Last-minute cancellation. Late arrivals di pickup point.

#### B4: In-Tour
- **Pemicu masuk:** Customer sedang tour.
- **Aksi sistem:** Tidak ada outbound. Hanya monitoring incoming.
- **Aksi manusia (Inan):**
  - Tanggapi pesan masuk dari tamu (request tambahan, komplain, info).
  - Kalau ada masalah serius (sakit, kecelakaan, komplain berat) → eskalasi ke Sam segera.
- **Pemicu keluar:** Tour selesai → B5.
- **Risk / Watch:** Komplain saat tour = momen krusial. Jangan defensive. Lihat -> [[website/brand-voice]] untuk handling komplain.

#### B5: Post-Tour
- **Pemicu masuk:** Tour selesai (kembali ke hotel/airport).
- **Aksi sistem:**
  - Pesan thank-you + foto/highlights (kalau ada).
  - Set reminder H+2 untuk B6.
- **Aksi manusia (Inan):**
  - Jawab pesan post-tour (tamu sering kirim foto, ucapan terima kasih, atau komplain).
  - Kalau ada komplain → tindak lanjut serius, eskalasi Sam.
- **Pemicu keluar:** H+2 → B6.

#### B6: Review Request
- **Pemicu masuk:** H+2 setelah tour selesai.
- **Aksi sistem:**
  - Kirim permintaan review dengan link Trustpilot/Google.
  - Personalisasi: nama tamu, destinasi, driver name (kalau ada).
- **Aksi manusia:** Tidak ada. Otomatis.
- **Pemicu keluar:** Customer leave review (track) atau 14 hari kemudian → archive.
- **Risk / Watch:** Jangan kirim review request kalau tour ada komplain — sebaliknya kirim apology + recovery offer.

#### Titik intervensi AI/otomatisasi di Flow B
- **B1, B2, B5, B6**: Pesan-pesan template dengan variable (nama, tanggal, lokasi pickup) — **otomatisasi penuh**. Risk rendah karena info diambil dari DB, bukan dari LLM generation.
- **B2 FAQ jawaban**: AI auto-reply untuk FAQ standar ("apa yang harus saya bawa?", "berapa lama di Bromo?") → **otomatisasi setelah Phase 4 (lihat Roadmap)**.
- **B3 D-day comms**: Otomatis dengan data dari DB, **tidak ada generation AI**.
- **B4 in-tour**: **Manual Inan**. Risk tinggi, AI tidak boleh ikut campur.
- **Komplain handling**: **Selalu manual, tidak boleh AI**.

---

### Flow C: Klook Pre-Tour Service Flow

> Tamu yang booking via Klook. JVTO **bukan** brand utama untuk mereka — mereka mengingat "Klook tour". JVTO = vendor execution. Tetap harus dilayani well, tetapi otoritas terbatas (pricing, refund = via Klook).

```
[C1: Booking Received] → [C2: Pre-Tour FAQ] → [C3: D-Day Logistics] → [C4: In-Tour] → [C5: Post-Tour]
```

#### C1: Booking Received
- **Pemicu masuk:** Webhook dari Klook → booking di-input ke DB JVTO.
- **Aksi sistem:**
  - Kirim WA welcome ke nomor tamu (yang diberikan Klook).
  - Tag conversation: `channel=klook, state=booked`.
  - Sediakan kontak Inan untuk pertanyaan logistik.
- **Aksi manusia:** Tidak ada (otomatis).
- **Pemicu keluar:** Tamu balas / pertanyaan masuk → C2.
- **Risk / Watch:** Banyak tamu Klook tidak tahu mereka akan dikontak operator lokal. Welcome message harus jelas: "Saya Inan dari JVTO, operator yang akan mengeksekusi tour Klook Anda."

#### C2: Pre-Tour FAQ
- **Pemicu masuk:** Tamu Klook mengirim pertanyaan apa pun pre-tour.
- **Aksi sistem (otomatisasi tinggi):**
  - Klasifikasi intent: pickup time / what to bring / weather / duration / dress code / dietary / etc.
  - Match ke template di wiki -> [[website/faq-master]] atau output FAQ -> [[output/faq-2026-05-12-ijen]], [[output/faq-2026-05-12-bromo]], dst.
  - Auto-reply dengan template multilingual (EN default, ID kalau tamu pakai ID).
- **Aksi manusia (Inan):** 
  - Approve draft (Phase 3) atau review log (Phase 4 ketika auto-send).
  - Tangani pertanyaan yang **bukan FAQ standar** (perubahan tanggal, refund — semua harus diarahkan ke Klook customer service, bukan ditangani JVTO).
- **Pemicu keluar:** Tanggal tour - 1 hari → C3.
- **Risk / Watch:** **JANGAN ubah booking dari sisi JVTO**. Semua perubahan harus via Klook karena itu sumber transaksinya. Kalau tamu minta change date ke Inan, balas: "Untuk perubahan tanggal, mohon hubungi Klook customer service di [link/nomor]."

#### C3: D-Day Logistics
- **Pemicu masuk:** H-1 hingga D-Day.
- **Aksi sistem:**
  - Kirim final pickup confirmation: jam, lokasi, kontak driver.
  - Data diambil dari operational DB, bukan dari LLM.
- **Aksi manusia (Inan):** Monitor, standby for changes.
- **Pemicu keluar:** Tour dimulai → C4.

#### C4: In-Tour
- **Pemicu masuk:** Customer sedang tour.
- **Aksi sistem:** Tidak ada outbound.
- **Aksi manusia (Inan):** Tanggapi kalau ada masalah. Sama seperti B4.
- **Pemicu keluar:** Tour selesai → C5.

#### C5: Post-Tour
- **Pemicu masuk:** Tour selesai.
- **Aksi sistem:** Pesan thank-you + link review Klook (bukan Trustpilot — karena platform mereka).
- **Aksi manusia:** Tidak ada.

#### Titik intervensi AI/otomatisasi di Flow C
- **Aman untuk auto-handle**: C1 welcome, C2 FAQ standar, C3 logistics info (data-driven), C5 thank-you.
- **Harus manual**: pertanyaan perubahan booking (redirect ke Klook), komplain, edge cases.
- **Goal jangka menengah**: 50-70% pesan Klook di-handle otomatis. Ini = beban Inan paling berkurang.

---

### Flow D: Window Travel B2B Coordination

> Account B2B dengan agent travel Malaysia. Volume rendah, value menengah-tinggi, relationship-driven. **Bukan customer akhir** — partner.

```
[D1: Inquiry / Request] → [D2: Availability Check] → [D3: Confirmation] → [D4: Booking Locked] → [D5: Post-Tour Reconciliation]
```

#### D1: Inquiry / Request
- **Pemicu masuk:** Window Travel kirim pesan request — biasanya tentang ketersediaan tour pada tanggal tertentu untuk jumlah pax tertentu.
- **Aksi sistem:** Tag `channel=window, state=inquiry_b2b`.
- **Aksi manusia (Inan):**
  - Cek ketersediaan crew, vendor (hotel), kapasitas tour pada tanggal yang diminta.
  - Balas dengan ketersediaan + harga B2B (kalau ada agreement khusus).
- **Pemicu keluar:** Window respond → D2.

#### D2: Availability Check
- **Pemicu masuk:** Window konfirmasi tertarik, minta detail lebih.
- **Aksi sistem:** Tidak ada otomatisasi.
- **Aksi manusia (Inan):**
  - Cek vendor (Flow E pre-emptive).
  - Susun draft itinerary B2B.
- **Pemicu keluar:** Detail dikirim → D3.

#### D3: Confirmation
- **Pemicu masuk:** Window kirim "confirm booking".
- **Aksi sistem:** Trigger booking via WA Pro CRM webhook (sama seperti booking JVTO direct).
- **Aksi manusia (Inan):**
  - Konfirmasi ke Window: "Booked, ini detail final."
  - Generate invoice B2B (sesuai term Window).
- **Pemicu keluar:** Confirmation accepted → D4.

#### D4: Booking Locked
- **Pemicu masuk:** Booking confirmed.
- **Aksi sistem:** Booking masuk DB sama seperti booking lain. Tour execution = Flow B equivalent (tapi tag `source=window` untuk reporting).
- **Aksi manusia:** Sama seperti B2-B5 untuk eksekusi tour, tapi communications ke Window (bukan tamu langsung).
- **Pemicu keluar:** Tour selesai → D5.

#### D5: Post-Tour Reconciliation
- **Pemicu masuk:** Tour selesai.
- **Aksi sistem:** Generate invoice reconciliation kalau ada item add-on.
- **Aksi manusia:** Inan kirim summary + invoice akhir ke Window.

#### Titik intervensi AI/otomatisasi di Flow D
- **D1-D2**: AI bisa **draft availability response** (data diambil dari DB), tapi **selalu Inan approve**. B2B = relationship, tone harus terjaga.
- **D3-D5**: Manual atau template-based dengan data DB. Tidak ada generation AI untuk pricing atau commitment.

**Catatan penting Window Travel:** Karena ini B2B dengan volume rendah & relationship-driven, jangan over-otomatisasi. Otomatisasi yang salah di sini = relationship rusak. Lebih baik Inan handle manual dengan AI sebagai notepad/drafting tool.

---

### Flow E: Vendor & Crew Operational Coordination

> Komunikasi internal-execution: hotel, restaurant, driver, guide. **Tidak boleh** dicampur ke pipeline customer.

```
[E1: Trigger Dispatch] → [E2: Vendor Confirmation] → [E3: Crew Briefing] → [E4: Execution Monitoring] → [E5: Reconciliation]
```

#### E1: Trigger Dispatch
- **Pemicu masuk:** Booking dibuat di DB (dari A5, B1, C1, D3).
- **Aksi sistem (sudah ada):**
  - Webhook trigger kirim WA ke vendor (hotel) dengan detail booking.
  - Webhook trigger kirim WA ke driver/guide assigned dengan briefing dasar.
- **Aksi manusia:** Tidak ada (otomatis), tapi Inan monitor.
- **Pemicu keluar:** Vendor & crew respond confirm → E2.
- **Risk / Watch:** Kalau vendor/crew tidak respond dalam 6 jam = trigger alert ke Inan untuk follow-up manual.

#### E2: Vendor Confirmation
- **Pemicu masuk:** Vendor balas (confirm available room/seat).
- **Aksi sistem:** Update booking status di DB → `vendor_confirmed=true`.
- **Aksi manusia:** Inan verifikasi konfirmasi. Kalau vendor tidak available → escalate ke Sam untuk alternative.
- **Pemicu keluar:** Confirmation diterima → E3.

#### E3: Crew Briefing
- **Pemicu masuk:** H-1 hingga H-0.
- **Aksi sistem:**
  - Kirim crew final briefing: nama tamu, jam pickup, lokasi, special request, info dietary, dll.
  - Generate manifest harian.
- **Aksi manusia (Inan):** Verifikasi crew confirm received & ready.
- **Pemicu keluar:** Tour dimulai → E4.

#### E4: Execution Monitoring
- **Pemicu masuk:** Tour berjalan.
- **Aksi sistem:** Monitoring channel terpisah (grup WA crew?).
- **Aksi manusia:** Inan standby untuk emergency. Sam dapat ringkasan kalau ada hal kritis.

#### E5: Reconciliation
- **Pemicu masuk:** Tour selesai.
- **Aksi sistem:** Update DB: tour completed, crew payment due, vendor payment due.
- **Aksi manusia:** Inan/finance reconcile.

#### Titik intervensi AI/otomatisasi di Flow E
- **E1**: Sudah ada otomatisasi (webhook). Pertahankan.
- **E2**: Tidak otomatisasi. Inan handle manual untuk relationship.
- **E3**: Template-based dengan data DB. **Otomatisasi penuh setelah testing.**
- **E4-E5**: Manual.

**Catatan kritis Flow E:** Pisahkan secara fisik nomor WhatsApp untuk vendor/crew ops dari nomor customer-facing. Idealnya:
- 1 nomor untuk customer (JVTO, Klook, Window di-satukan dengan tagging) — yang dikelola sistem ini.
- 1 nomor terpisah untuk vendor & crew ops — bisa grup-grup terpisah, bisa Inan handle manual atau dengan tooling beda.

---

## 7. Lapisan Penghubung Antar Flow

Bagaimana 5 flow di atas saling terhubung — ini bagian yang sering luput.

### 7.1 State Machine Customer (Unified)

Setiap nomor WhatsApp yang pernah berinteraksi dengan JVTO punya **satu profil**, dengan satu state aktif:

```
new → inquiry → qualified → quoted → negotiating → booked → pre_tour → in_tour → post_tour → reviewed → cold
                                                       │
                                                       └── (canceled / lost)
```

State menentukan:
- Flow mana yang aktif untuk customer ini
- SLA yang berlaku
- Otorisasi siapa yang handle
- Tone & template yang dipakai

### 7.2 Channel Resolution Rules

Saat pesan masuk dari nomor X, urutan cek:

1. Apakah nomor X ada di `klook_bookings.guest_phone` dengan booking aktif (belum tour atau tour baru selesai <14 hari)? → Channel = **klook**, masuk Flow C.
2. Apakah nomor X ada di `window_travel_contacts`? → Channel = **window**, masuk Flow D.
3. Apakah nomor X ada di `vendor_contacts` atau `crew_contacts`? → Channel = **vendor/crew**, masuk Flow E.
4. Apakah nomor X ada di `bookings.customer_phone` dengan state booked? → Channel = **jvto_direct, state=post-booking**, masuk Flow B.
5. Apakah nomor X ada di `bookings.customer_phone` dengan state historis (sudah post_tour)? → Channel = **jvto_direct, state=returning**, masuk Flow A (treat as warm lead).
6. Tidak ada match → Channel = **jvto_direct, state=inquiry**, masuk Flow A.

### 7.3 Handoff Antar Flow

| Dari | Ke | Pemicu |
|---|---|---|
| A5 (JVTO Booked) | B1 (Concierge) | DP diterima, booking di-create |
| C1 (Klook Booked) | C2 (Pre-Tour) | Welcome message terkirim |
| D3 (Window Confirm) | B (concierge variant) | Booking locked, tour execution mode |
| Apapun → Vendor/Crew interaction | Flow E | Backend trigger, tidak ada handoff customer-facing |

### 7.4 Single Contact, Multi-Context

Satu customer bisa punya **beberapa interaksi paralel**:
- Booking aktif (Flow B state pre_tour) + inquiry baru untuk tour kedua (Flow A state inquiry).

Solusinya: profil customer = single (1 nomor = 1 profil), tetapi **conversation threads bisa multiple**. Tag tiap thread dengan booking_id terpisah.

### 7.5 Pemisahan Fisik Nomor WhatsApp (Multi-Number Setup)

WA Pro CRM yang dibangun David mendukung multi-nomor. Pemisahan fisik di tingkat nomor = pemisahan mental load Inan + pemisahan risiko brand.

#### Skema 3 Nomor

| Nomor | Inbox System | Audiens | Dipublikasi | Yang Memegang |
|---|---|---|---|---|
| **Nomor 1 — Customer-facing JVTO** | `customer` | JVTO inquiry, JVTO post-booking, Klook tamu | Website, business card, Klook integration, Trustpilot bio | Inan (primary), Sam (untuk inquiry tinggi-nilai) |
| **Nomor 2 — B2B Partners** | `b2b_partner` | Window Travel, partner B2B masa depan | TIDAK dipublikasi. Hanya diberikan langsung ke partner saat onboarding | Inan (primary), Sam (commitment besar) |
| **Nomor 3 — Operations** | `internal_ops` | Hotel, restaurant, driver, guide | Hanya internal | Inan |

#### Mengapa 3, bukan 1 atau 5

- **1 nomor (status quo):** Lima fungsi tumpang-tindih di satu inbox = sumber chaos sekarang.
- **2 nomor (customer + ops):** Lebih baik, tapi B2B Window masih dicampur dengan tamu mass-market — relationship rusak.
- **3 nomor (customer + b2b + ops):** Sweet spot. Pemisahan jelas tanpa overload.
- **5+ nomor:** Inan harus monitor 5 inbox = pindah masalah, bukan menyelesaikannya.

#### Aturan Routing Antar Nomor

1. **Nomor 1 → Nomor 3 (otomatis, customer tidak lihat):** Saat booking confirmed (dari customer manapun), sistem trigger dispatch ke vendor via Nomor 3.
2. **Nomor 2 → Nomor 3 (otomatis):** Saat Window Travel confirm booking, sistem trigger dispatch yang sama via Nomor 3.
3. **Customer dari Nomor 1 tidak pernah dikirim ke Nomor 2 atau 3.** Mereka hanya tahu satu nomor.
4. **B2B partner dari Nomor 2 tidak pernah dikirim ke Nomor 3.** Mereka tahu Nomor 2 saja.
5. **Crew dari Nomor 3 tidak pernah dikirim ke Nomor 1 atau 2.** Mereka tahu Nomor 3 saja.

#### Implikasi untuk David

WA Pro CRM perlu:
- Register 3 nomor terpisah (3 set `api_key` + `number_key` di WA Pro CRM dashboard).
- Webhook handler bisa identifikasi nomor mana yang menerima (lihat `number_key` di payload incoming).
- Routing logic di rules engine (-> [[ops/2026-05-14-whatsapp-rules-engine]] Step 2) → default channel berbeda per nomor.
- Konfigurasi grup WhatsApp di Nomor 3: terpisah per kategori (hotel group, driver group, guide group), atau 1-on-1 per vendor.

#### Migration Path (Existing Operation → Multi-Number)

1. **Minggu 1:** Setup Nomor 2 + Nomor 3 (nomor SIM baru). Tidak diumumkan ke pihak luar dulu.
2. **Minggu 2:** Inan parallel-handle: chat existing tetap di Nomor 1, vendor/crew baru di-route ke Nomor 3.
3. **Minggu 3:** Window diberitahu nomor baru untuk B2B (Nomor 2). Tetap respond di Nomor 1 selama transisi.
4. **Minggu 4:** Vendor/crew migrasi penuh ke Nomor 3. Nomor 1 hanya untuk customer.
5. **Minggu 5+:** Steady state 3-nomor.

#### Risiko Multi-Number

- **Confusion saat transition:** Selama 2-4 minggu pertama, ada miscommunication. Mitigasi: dokumentasi internal jelas, auto-reply Nomor 1 yang menjelaskan ke vendor "tolong kirim ke Nomor 3".
- **Ban risk per nomor:** Setiap nomor non-resmi punya risk ban sendiri. Mitigasi: rate limiting per nomor, traffic pattern yang berbeda (customer-facing volume tinggi, ops volume rendah).
- **Cost:** 3 SIM card + kemungkinan 3 device atau 1 device multi-SIM. Estimasi <Rp 100k/bulan untuk pulsa.

### 7.6 Escalation Path (Otoritas)

```
[Routine] → Inan handle
   ↓
[Decision di luar otoritas Inan] → Eskalasi ke Sam
   ↓
[Decision di luar otoritas Sam] → External (legal, medical, dll)
```

Apa yang **di luar otoritas Inan**:
- Diskon di luar standar
- Refund (kecuali yang sudah jelas di policy)
- Komplain berat (sakit, kecelakaan, kerugian properti)
- Perubahan paket besar
- Confirm tour dengan special request yang berdampak ke crew/vendor cost

Apa yang **bisa Inan putuskan sendiri**:
- Penjelasan FAQ
- Konfirmasi pickup time/location dari DB
- Quotation berdasarkan pricing table standar
- Perubahan kecil (request makanan, tambahan air, dll yang tidak ubah cost)
- Cancel/reschedule di window yang policy izinkan

---

## 8. Titik Intervensi AI/Otomatisasi — Tabel Konsolidasi

| Flow | Stage | Tingkat Otomatisasi | Mengapa |
|---|---|---|---|
| A | A1 auto-ack off-hours | **Otomatis penuh** | Risk rendah, value tinggi, no commitment |
| A | A2 qualification | Draft → manual approve | Tone & qualification = relationship |
| A | A3 quotation | Draft → Sam approve | Pricing = otoritas Sam |
| A | A4-A5 | **Manual** | Commitment & negotiation |
| B | B1 confirmation | **Otomatis** | Template + DB data |
| B | B2 FAQ | Otomatis untuk standar, draft untuk non-standar | Common questions = template aman |
| B | B2 logistik H-3, H-1 | **Otomatis** | DB data driven |
| B | B3 D-day | **Otomatis** | DB data driven |
| B | B4 in-tour | **Manual** | Risk tinggi, sensitive |
| B | B5 post-tour | **Otomatis (template)** | Thank-you generic OK |
| B | B6 review request | **Otomatis (conditional)** | Skip kalau ada komplain |
| C | C1 welcome | **Otomatis** | Template |
| C | C2 FAQ | **Otomatis (Phase 4+)** | Volume tinggi, intent jelas |
| C | C3 logistik | **Otomatis** | DB data driven |
| C | Komplain Klook | **Manual / redirect** | Otoritas terbatas |
| D | D1-D2 | Draft → manual approve | B2B relationship |
| D | D3-D5 | Manual + template | Account-level handling |
| E | E1 dispatch | **Otomatis (sudah ada)** | Sudah jalan |
| E | E2 vendor confirm | **Manual** | Relationship |
| E | E3 crew briefing | **Otomatis (template)** | DB data driven |
| E | E4-E5 | **Manual** | Eksekusi |

---

## 9. Brand Voice per Kanal

Tone berbeda berdasarkan audiens. Referensi utama: -> [[website/brand-voice]].

| Kanal | Tone | Contoh frasa pembuka | Contoh frasa yang tidak pas |
|---|---|---|---|
| A — JVTO Inquiry | Direct, evidence-led, slightly formal | "Halo, terima kasih sudah menghubungi JVTO. Saya akan bantu menyusun tour Anda." | "Selamat datang di paradise Java timur! ✨" (terlalu generik tourism) |
| B — JVTO Post-Booking | Hangat, personal, reassuring | "Hai [Nama], menyambut tour Anda di [Destinasi]. Berikut info persiapan..." | "Dear customer..." (terlalu corporate) |
| C — Klook | Service-desk profesional, info-rich, slightly less personal | "Halo, terima kasih sudah booking via Klook. Saya Inan dari JVTO yang akan mengeksekusi tour Anda." | "Maaf ya, untuk perubahan tanggal tidak bisa..." (tanpa solusi/redirect) |
| D — Window Travel | Profesional, peer-to-peer, transactional | "Hi Sarah, requesting confirmation for the Bromo trip 18-19 May, 4 pax." | Tone B2C dengan terlalu banyak penjelasan dasar |
| E — Vendor/Crew | Singkat, instruksional, action-oriented | "Pak Hartono, pickup besok 00:30, 2 tamu Eropa di Kalibaru. OK?" | Kalimat panjang yang tidak action-oriented |

Aturan tegas semua channel (dari -> [[website/brand-voice]]):
- **Tidak ada generic tourism brochure language.** "Discover paradise" / "magical adventure" = ditolak.
- **Selalu evidence-led.** "Mr. Sam, Tourist Police officer aktif" — bukan "safety-focused guide."
- **Hindari hyperbole.** "Best tour in Java" = banned. Pakai data: "rated Excellent on Trustpilot."
- **Selalu sebut kredibilitas saat relevan.** NIB, POLPAR, BBKSDA, ISIC — tetapi tidak setiap pesan (jangan spam).

---

## 10. Metrik Keberhasilan

Disusun per kanal + per fase otomatisasi. Semua metric harus *measurable* dari log sistem, bukan tebakan.

### 10.1 Metric Waktu Respons

| Channel | Stage | Target SLA P50 | Target SLA P95 |
|---|---|---|---|
| A | First touch business hours | <30 menit | <2 jam |
| A | First touch off-hours (dengan auto-ack) | <2 menit auto-ack, <12 jam Inan/Sam | <24 jam |
| B | Pre-tour FAQ | <30 menit | <2 jam |
| B | D-day / H-3 logistik | <15 menit | <1 jam |
| C | Klook FAQ | <1 jam | <4 jam |
| C | Klook D-day | <15 menit | <1 jam |
| D | Window B2B | <2 jam business hours | <12 jam |
| E | Vendor confirm follow-up | <30 menit hari-H | <4 jam lainnya |

### 10.2 Metric Otomatisasi

- **Auto-handled ratio** per channel (target setelah 3 bulan):
  - Klook: 30-50%
  - JVTO post-booking: 20-30%
  - JVTO inquiry: 5-10% (hanya auto-ack)
  - Window: 0% (selalu manual atau draft-assist)
  - Vendor/Crew: 60-80% (template-based)
- **Draft approval rate without edit** (kualitas AI draft): >70%
- **AI rejection rate**: <10% (kalau tinggi = AI drift, butuh re-prompting)

### 10.3 Metric Bisnis

- **Konversi A → A5** (inquiry → booked): track sebelum/sesudah. Target naik 10-20%.
- **Customer satisfaction proxy**: continuation rate (apakah tamu balas setelah kita kirim) + review rate.
- **Klook review rate**: track sebelum/sesudah.
- **Window Travel repeat rate**: track quarter-over-quarter.

### 10.4 Metric Sumber Daya

- **Inan self-reported overload** mingguan (1-10). Target: turun dari baseline ≥3 poin.
- **Inan working hours per minggu**: target turun sambil throughput naik.
- **Pesan masuk per hari**: total + per channel — untuk capacity planning.

---

## 11. Risiko & Mitigasi (Non-Teknis)

| Risiko | Mitigasi |
|---|---|
| Inan keluar / sakit | Playbook ini menjadi onboarding dokumen. Tahap 6 (Roadmap) harus train Sam atau staf cadangan minimum untuk handle 2-3 hari. |
| AI auto-reply menjawab salah & customer marah | Selalu mulai dari "draft → manual approve" sebelum "auto-send". Auto-send hanya untuk intent yang sudah ≥95% approval rate selama 4 minggu. |
| Customer Eropa kecewa karena response lambat tanpa konteks | Auto-ack off-hours **wajib** sebelum apa pun lain. Ini relief paling cepat di-eksekusi. |
| Klook customer kira mereka harus deal dengan JVTO untuk perubahan | Welcome message C1 harus tegas redirect ke Klook untuk hal-hal account-level. |
| Window Travel relationship rusak karena over-automation | Window = manual atau draft-assist saja. Tidak ada auto-reply pernah. |
| Brand voice drift di auto-reply | Review mingguan: sample 20 pesan auto, audit terhadap -> [[website/brand-voice]]. |
| WA Pro CRM di-ban Meta | Disiplin volume (max rate, random delay), prepare migration playbook ke WhatsApp Cloud API resmi. |
| Sam tidak punya visibilitas | Tahap pelaporan harian / mingguan (dipisah dari playbook ini, tapi konseptual menempel). |

---

## 12. Roadmap Eksekusi

Ini bukan spek teknis. Ini fase **perubahan workflow** yang Sam, Inan, dan David ikuti.

### Fase 0 — Persiapan (1 minggu)
- Review & approve playbook ini.
- Validasi data: pastikan field di DB lengkap untuk channel resolution (klook_bookings, window_contacts, vendor_contacts, crew_contacts).
- Pisahkan nomor WhatsApp untuk customer vs vendor/crew (kalau belum).
- David assess teknis WA Pro CRM untuk handle inbound (saat ini hanya outbound).

### Fase 1 — Foundation: Inbox Visibility (2 minggu)
**Yang berubah dalam hidup Inan:**
- Setiap pesan masuk tagged otomatis dengan channel (Klook / JVTO / Window / Vendor / Crew).
- Inan punya satu view yang tunjukkan: "5 pesan menunggu balasan, 2 dari Klook FAQ, 3 dari JVTO inquiry".
- Tidak ada AI generation. Hanya observation + organization.

**Gate to next phase:** Channel resolution accuracy ≥95% (di-validasi manual 100 pesan).

### Fase 2 — Auto-Ack Off-Hours (1-2 minggu)
**Yang berubah:**
- Customer Eropa yang kirim pesan jam 02:00 WIB dapat balasan profesional dalam <2 menit.
- ETA realistis disebut, link self-serve (website, paket) disertakan.
- Tidak ada classifier, tidak ada draft. Hanya template + waktu kirim.

**Gate:** Customer complaint rate karena slow response turun. Bukti: review/feedback subjektif.

### Fase 3 — Classifier Passive (2 minggu)
**Yang berubah:**
- AI baca pesan masuk, klasifikasi intent + risk + priority.
- Hasilnya kirim ke Telegram Inan: "Pesan dari [Nama], Klook FAQ pickup time, prioritas rendah."
- Inan masih balas sendiri, tapi sudah tahu apa konteks tanpa baca chat dulu.

**Gate:** Classifier accuracy ≥85% (sampling manual review 100 pesan).

### Fase 4 — Draft Assist (3-4 minggu)
**Yang berubah:**
- Untuk Klook FAQ dan JVTO post-booking FAQ: AI generate draft.
- Inan terima draft di Telegram, tap "Approve" atau edit dulu lalu approve.
- Setelah approve, dikirim via WA Pro CRM.

**Gate:** Approval rate without edit ≥70%. Inan reduction in time-to-reply ≥40%.

### Fase 5 — Auto-Reply Selective (4 minggu)
**Yang berubah:**
- Intent Klook FAQ yang sudah punya approval rate ≥95% selama 4 minggu → auto-reply tanpa approval.
- Sam dapat audit log harian (kalau mau).
- Inan dapat opt-out switch untuk matikan auto-reply per intent kalau ada issue.

**Gate:** Customer satisfaction stable atau naik. Tidak ada incident karena auto-reply salah.

### Fase 6 — Expand & Refine (6+ minggu)
**Yang berubah:**
- Tambah intent yang di-auto-handle (B2 logistik H-3, H-1, dll).
- RAG grounding dari llm-wiki diaktifkan (jawaban AI lebih grounded).
- Sam dapat dashboard ringkas.
- Documenting onboarding untuk staf cadangan.

**Gate:** Inan stress level turun ≥3 poin. Booking conversion stabil atau naik.

### Fase 7+ — Strategic
- Evaluasi migrasi ke WhatsApp Business Cloud API resmi.
- Multi-staff support (Inan + cadangan, Sam akses langsung).
- Cross-flow analytics (apa intent yang paling sering, di mana funnel A bocor, dll).

---

## 13. Lampiran: Glosarium Intent Awal (Seed)

Daftar intent yang seharusnya seed di taksonomi sistem. Bukan exhaustive — tumbuh seiring data.

### Klook Channel — FAQ
- `klook_faq_pickup_time` — "Jam berapa pickup?"
- `klook_faq_pickup_location` — "Saya dijemput di mana?"
- `klook_faq_what_to_bring` — "Apa yang harus saya bawa?"
- `klook_faq_dress_code` — "Pakaian apa yang cocok?"
- `klook_faq_duration` — "Tour berapa lama?"
- `klook_faq_meal` — "Apakah makan sudah termasuk?"
- `klook_faq_weather` — "Cuaca bagaimana?"
- `klook_faq_difficulty` — "Apakah tournya berat?"
- `klook_faq_health_screening` — "Apakah perlu skrining medis?"

### Klook Channel — Non-FAQ
- `klook_change_date` → redirect ke Klook CS
- `klook_refund_request` → redirect ke Klook CS
- `klook_complaint` → escalate Inan/Sam

### JVTO Direct — Inquiry
- `jvto_inq_first_touch` — pesan pertama, qualify
- `jvto_inq_pricing` → Sam approve required
- `jvto_inq_availability` — cek DB
- `jvto_inq_custom_request` → manual

### JVTO Direct — Post-Booking
- `jvto_pb_confirm_details` — konfirmasi detail
- `jvto_pb_change_request` → escalate kalau perubahan besar
- `jvto_pb_pre_tour_question` — FAQ standar
- `jvto_pb_d_day_logistics` — pickup info
- `jvto_pb_in_tour_request` → manual
- `jvto_pb_complaint` → escalate

### Window Travel
- `window_inquiry_availability` — draft assist
- `window_confirm_booking` — manual
- `window_change_request` — manual
- `window_invoice_query` — manual

### Vendor / Crew
- `vendor_confirm_received` — auto-log
- `vendor_unavailable` → escalate Inan
- `crew_briefing_confirm` — auto-log
- `crew_emergency` → escalate Inan/Sam immediately

---

## 14. Apa Selanjutnya

Setelah playbook ini di-approve oleh Sam:

1. **David** review playbook dari sisi feasibility teknis. Dia akan menyusun spek implementasi (bukan di dokumen ini — di Claude Code).
2. **Inan** review playbook dari sisi operasional. Apa yang missed dari pengalaman dia.
3. **Sam** review playbook dari sisi otoritas & strategi. Apakah escalation paths sudah pas dengan keinginan dia.
4. Setelah triangulasi, mulai Fase 0 → Fase 1.

Playbook ini adalah dokumen hidup. Update versi (last_updated di frontmatter) saat ada perubahan signifikan. Setiap perubahan di-log ke -> [[log]].

---

> *"Five jobs, one brain" — kalimat itu masalah inti. Playbook ini bukan solusi untuk membuat Inan lebih kuat. Ini struktur untuk membuat sistem lebih kuat, supaya Inan tidak perlu menjadi superhuman.*
