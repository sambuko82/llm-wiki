---
type: source
title: Teori & Konsep Manajemen Komunikasi — Tour Operator Framework
last_updated: 2026-05-19
sources: []
---

# Teori & Konsep Manajemen Komunikasi

*Source: `E:\Users\JAVA VOLCANO\Downloads\Teori & Konsep Manajemen Komunikasi.md`. Ingested 2026-05-19. Dokumen ini secara eksplisit mereferensikan JVTO sebagai contoh operator.*

---

## Frameworks Extracted

### 1. BANT — Prospect Qualification Framework

Global sales/support standard. Purpose: filter non-buyers sebelum mengalokasikan waktu human support.

| Component | Pertanyaan Kunci | JVTO Application |
|-----------|-----------------|------------------|
| **B — Budget** | Apakah customer punya anggaran sesuai harga paket? | Tanya preferensi hotel (standard vs premium) — proxy budget tanpa tanya langsung "berapa budget Anda?" |
| **A — Authority** | Apakah orang yang chat adalah pengambil keputusan? | "Apakah Anda yang akan memutuskan booking, atau ada anggota keluarga/tim yang perlu dikonsultasikan?" |
| **N — Need** | Apakah mereka butuh tipe tur yang JVTO sediakan? | Adventure (midnight hike Ijen) vs wisata santai? Solo/couple/family/group? Ijen vs Bromo-only? |
| **T — Timeline** | Kapan berangkat? | "Tanggalnya sudah pasti atau masih tentatif?" — flags cold leads yang tidak worth full quote effort |

**Rule:** Kunci 3 items sebelum kirim quotation: **tanggal pasti + jumlah pax + preferensi hotel.** Quotation sebelum 3 items terkunci = pekerjaan berulang (rework).

**BANT × Rules Engine mapping:** B component maps ke STEP 4 classify intent di -> [[ops/2026-05-14-whatsapp-rules-engine]]. Potential field upgrade: tambah `bant_t_confirmed` boolean di `wa_conversations` untuk flag cold vs hot lead.

---

### 2. MECE — Chatbot Menu Design

McKinsey classification principle: Mutually Exclusive (tidak overlap), Collectively Exhaustive (menutupi semua kebutuhan). Prevents menu options dari tumpang tindih.

**JVTO WA auto-reply MECE menu:**
```
[1] Tanya Paket Wisata
[2] Status Booking Aktif
[3] Kemitraan / B2B
```
Rule: customer yang sudah punya booking aktif tidak masuk [1]. B2B partner tidak masuk [1] atau [2]. Setiap pilihan punya jalur follow-up berbeda.

---

### 3. SFC/FCR — Solved on First Contact / First Contact Resolution

Standard global: selesaikan pertanyaan atau masalah customer **pada kontak pertama**. Setiap bolak-balik tambahan = risiko pembatalan naik.

**JVTO implication:** FAQ yang paling sering masuk (jam pickup, apa saja yang termasuk, kondisi medis Ijen, cancellation policy, deposit berapa) harus dijawab **lengkap** di respons pertama. Referensi: -> [[content/faq-master]] dan -> [[content/operational-facts]].

---

### 4. SLA Standards — International Benchmark

| Channel | Response Time | Note |
|---------|--------------|------|
| Instant Messaging (WhatsApp/Live Chat) | Maks **2–5 menit** respons pertama | Biasanya diotomatisasi bot |
| Email Inquiry | Maks **2–4 jam** hari kerja | Untuk draft itinerary awal + quotation |

**JVTO current SLA** (per -> [[ops/2026-05-14-whatsapp-operations-playbook]] §5):
- Channel A (inquiry): <30 menit business hours, <6 jam off-hours (dengan auto-ack)
- JVTO support hours: **08:00–22:00 WIB** daily

Gap vs international benchmark: human SLA 30 menit masih di atas 2-5 menit benchmark. Auto-ack sudah di-plan untuk A1 off-hours — ini yang menutup gap tersebut.

---

### 5. ISO 10002 — Quality Management, Customer Satisfaction

Standar internasional untuk complaint handling. Dalam konteks pra-booking: catat area di website/brosur yang sering memicu pertanyaan repetitif.

**JVTO application:** Track FAQ yang masuk WhatsApp. Pertanyaan yang sama muncul >3× dalam sebulan → tambahkan ke -> [[content/faq-master]] dan kirim proaktif di pre-departure pack. Input ke David untuk upgrade chatbot menu jika perlu.

---

### 6. GDPR & UU PDP — Data Privacy Rule

**Rule:** Tidak meminta data sensitif (paspor, kondisi medis, ukuran sepatu) sebelum customer:
1. Melakukan pembayaran DP, **ATAU**
2. Menyetujui Privacy Policy Confirmation secara eksplisit

**JVTO compliance:** Formulir ukuran sepatu, alergi makanan, data paspor → hanya setelah DP diterima (via My Booking Portal To-Do checklist). Kondisi medis Ijen dikumpulkan via Dr. Irwandanu -> [[people/dr-ahmad-irwandanu]] sebagai bagian screening, bukan via sales chat. Sesuai -> [[sources/jvto-policy-pack-v6]] Policy 3.

---

## 4-Stage Pre-Booking Communication Funnel

```
[Triage] → [Discovery] → [Proposal] → [Urgency/Closing]
```

| Stage | Tujuan | SOP Kunci |
|-------|--------|-----------|
| **1. Triage** | Saring spam, kelompokkan minat | Automated welcome message + kumpulkan data esensial (Nama, Destinasi, Tanggal, Pax) |
| **2. Discovery** | Kunci detail spesifik via BANT | Staf **dilarang** kirim quotation sebelum 3 komponen terkunci: tanggal pasti, jumlah pax, preferensi hotel/fasilitas |
| **3. Proposal** | Solusi konkret, **max 2 opsi** | Max 2 variasi (mis. Paket Standard vs Paket Premium). Lebih dari 2 opsi = Analysis Paralysis → tunda pemesanan |
| **4. Urgency/Closing** | Konversi penawaran → DP | Time-Limit Booking: tenggat validitas harga + batas kuota permit. Automated 24-hr reminder sebelum kuota hangus |

**Analysis Paralysis rule:** max 2 proposal options. Untuk JVTO ini sangat relevan di Ijen high season — kuota permit BBKSDA terbatas = natural scarcity anchor untuk urgency closing yang tidak terasa pushy.

---

## 6-Stage Customer Journey Funnel

```
[Awareness] → [Consideration] → [Conversion] → [Pre-departure] → [On-tour] → [Post-tour]
```

| Stage | Digital System | Deliverable | JVTO Mapping |
|-------|---------------|-------------|--------------|
| **1. Awareness** | Meta Ads, SEO, Trustpilot/Google widget | Traffic ke website | — |
| **2. Consideration** | WA Chatbot (auto-ack), CRM lead capture | Lead profile: nama, WA, tanggal tentatif | Inan / Bot — Flow A1-A2 |
| **3. Conversion** | Booking engine, Midtrans/Stripe, e-permit | E-Voucher PDF, NP permits, Travel Credit Ledger | Sam/Inan — Flow A4-A5 |
| **4. Pre-departure** | Automated WA/email H-7 & H-1, Google Forms post-DP | Digital Welcome Pack, Passenger Manifest | Inan — Flow B |
| **5. On-tour** | WA Group (guide + back-office + tamu), BMKG/MAGMA feed | Health Screening Pass, Schedule Alerts, Incident Report | Tour Leader + Inan |
| **6. Post-tour** | Automated feedback trigger (24hr post-tour), CRM retargeting | Verified Review (Trustpilot/Google), CRM tag `Alumni - Promoter` | Customer Relations |

Template scripts per stage: -> [[ops/canned-responses]]

---

## Content Angles untuk JVTO

1. **Permit scarcity = natural urgency anchor** — Ijen kuota BBKSDA terbatas (terutama blue fire season Juli–Agustus). Time-Limit Booking terasa organik, tidak manipulatif.
2. **Medical screening = BANT Need signal** — customer yang tanya detail skrining = high-intent buyer; customer yang resistensi = potential N=No, flag awal.
3. **Police-led founder = Authority differentiator** — dalam BANT Authority check: "Saya bisa hubungkan dengan Sam (pendiri, Tourist Police aktif) untuk konfirmasi ini" = credibility, bukan bottleneck.
4. **100% private = eliminasi satu dimensi keputusan** — tidak ada opsi "gabung group" → natural MECE simplification, mendukung max-2-opsi proposal rule.
5. **All-inclusive pricing = SFC tool** — kutip harga final sekali (tidak ada add-on tersembunyi) → kurangi follow-up "apa yang sudah include?" Ini juga mendukung JVTO claim C3.
