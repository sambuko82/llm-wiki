---
type: ops
title: JVTO WhatsApp Rules Engine
last_updated: 2026-05-14
sources: [2026-05-14-whatsapp-operations-playbook, wa-pro-crm-api]
---

# JVTO WhatsApp Rules Engine

> Dokumen ini adalah **logika eksekusi murni**. Tidak ada penjelasan filosofi.
> Untuk konteks & alasan, baca dulu -> [[ops/2026-05-14-whatsapp-operations-playbook]].
> Audiens: AI yang menjalankan classifier/router, David yang membangun sistem, Inan/staf yang perlu rujukan cepat.

---

## STEP 1 — Receive Message

**Input** (dari webhook WA Pro CRM):
```
{
  number_key,         // identifikasi nomor JVTO mana yang menerima
  from,               // nomor pengirim (628xxxx@s.whatsapp.net)
  body,               // teks pesan
  type,               // conversation | imageMessage | audioMessage | etc
  media_url,          // jika ada
  timestamp
}
```

**Action:** simpan ke `wa_messages` dengan `direction=in`. Jangan respond apa pun di step ini.

---

## STEP 2 — Identify JVTO Number (Inbox Router)

Lookup `number_key` ke tabel:

| number_key | Inbox | Default Channel |
|---|---|---|
| (kunci nomor 1) | `customer` | tergantung Step 3 |
| (kunci nomor 2) | `b2b_partner` | `window` |
| (kunci nomor 3) | `internal_ops` | `vendor_crew` |

**Jika number_key tidak dikenal:** log error, alert Inan, stop.

---

## STEP 3 — Identify Channel (Phone Number Lookup)

Hanya berlaku untuk inbox = `customer`. Untuk inbox lain, channel sudah ditentukan di Step 2.

Cek `from` dalam urutan berikut. **Pakai first-match**, jangan teruskan.

| Urutan | Lookup | Jika ketemu, channel = |
|---|---|---|
| 1 | `klook_bookings.guest_phone` WHERE `tour_date >= today() - 30` | `klook` |
| 2 | `bookings.customer_phone` WHERE `status='active'` AND `tour_date BETWEEN today() AND today()+90` | `jvto_post_booking` |
| 3 | `bookings.customer_phone` WHERE `tour_date < today() - 14` | `jvto_returning` |
| 4 | Tidak ada match | `jvto_inquiry` |

**Output:** set `wa_conversations.channel`.

---

## STEP 4 — Identify State

Lookup state berdasarkan channel.

### Jika channel = `klook`
| Kondisi | State |
|---|---|
| Tour belum dilaksanakan & belum ada interaksi | `klook_booked` |
| Tour belum dilaksanakan & sudah ada interaksi | `klook_pre_tour` |
| Tour hari ini | `klook_d_day` |
| Tour sedang berjalan (hari pickup → hari drop) | `klook_in_tour` |
| Tour selesai <14 hari | `klook_post_tour` |
| Tour selesai >14 hari | `klook_archive` |

### Jika channel = `jvto_post_booking`
| Kondisi | State |
|---|---|
| Booking dibuat, tour > H+7 | `pre_tour_prep` |
| Tour H-7 hingga H-1 | `pre_tour_active` |
| Tour H-0 (hari ini) | `d_day` |
| Tour sedang berjalan | `in_tour` |
| Tour selesai, <H+2 | `post_tour` |
| Tour selesai, H+2 hingga H+14 | `review_window` |
| Tour selesai, >H+14 | `archive` |

### Jika channel = `jvto_inquiry`
| Kondisi | State |
|---|---|
| Pesan pertama (tidak ada `wa_conversations` row sebelumnya) | `cold` |
| Sudah ada balasan dari Inan/Sam, belum quote | `qualified` |
| Quotation sudah dikirim, belum konfirmasi | `quoted` |
| Customer respond minat lanjut | `negotiating` |
| DP diterima | → transition ke channel `jvto_post_booking` state `pre_tour_prep` |
| Tidak respond >7 hari di stage qualified/quoted | `lost` |

### Jika channel = `window`
| Kondisi | State |
|---|---|
| Inquiry / request availability | `b2b_inquiry` |
| Quotation/availability dikirim | `b2b_quoted` |
| Confirm booking | `b2b_confirmed` |
| Tour berjalan | `b2b_in_execution` |
| Tour selesai | `b2b_reconciliation` |

### Jika channel = `vendor_crew`
| Kondisi | State |
|---|---|
| Dispatch baru dikirim, belum confirm | `dispatch_sent` |
| Vendor/crew confirm | `confirmed` |
| Briefing dikirim H-1 | `briefed` |
| Tour berjalan | `executing` |
| Selesai | `done` |

**Output:** set `wa_conversations.state`.

---

## STEP 5 — Classify Intent

Kirim ke LLM classifier (Haiku 4.5) dengan prompt:

```
System: Klasifikasi pesan WhatsApp masuk untuk JVTO tour operator.
Context: channel={channel}, state={state}, language_hint={detected_language}.
Output JSON:
{
  intent: "<slug from taxonomy>",
  confidence: 0.0-1.0,
  risk_level: "low" | "medium" | "high",
  language: "id" | "en" | "ms" | "de" | "fr" | "other",
  urgency: "low" | "medium" | "high"
}
```

Taksonomi intent — lihat Section "Intent Taxonomy" di bawah.

**Output:** set `wa_messages.intent_classified`, `confidence`, `risk_level`.

---

## STEP 6 — Determine Action

Action ditentukan oleh tabel `(channel, intent, confidence, risk_level)`:

### Master Action Table

| channel | intent_pattern | confidence | risk | action |
|---|---|---|---|---|
| `jvto_inquiry` | `inq_first_touch` | any | low | `auto_ack` (jika off-hours) atau `escalate_inan` (jika business hours) |
| `jvto_inquiry` | `inq_pricing*` | any | high | `escalate_sam` |
| `jvto_inquiry` | `inq_availability` | any | medium | `escalate_inan` |
| `jvto_inquiry` | `inq_custom_request` | any | high | `escalate_sam` |
| `jvto_post_booking` | `pb_faq_*` | ≥0.85 | low | `auto_reply` |
| `jvto_post_booking` | `pb_faq_*` | <0.85 | low | `draft_for_inan` |
| `jvto_post_booking` | `pb_change_*` | any | high | `escalate_inan_or_sam` |
| `jvto_post_booking` | `pb_logistics_*` | ≥0.85 | low | `auto_reply_db_grounded` |
| `jvto_post_booking` | `pb_in_tour_*` | any | high | `escalate_inan_urgent` |
| `jvto_post_booking` | `pb_complaint` | any | high | `escalate_sam_urgent` |
| `klook` | `klook_faq_*` | ≥0.85 | low | `auto_reply` |
| `klook` | `klook_faq_*` | <0.85 | low | `draft_for_inan` |
| `klook` | `klook_change_*` | any | medium | `auto_reply_redirect_klook` |
| `klook` | `klook_refund_*` | any | high | `auto_reply_redirect_klook` |
| `klook` | `klook_complaint` | any | high | `escalate_inan` |
| `klook` | `klook_logistics_*` | ≥0.85 | low | `auto_reply_db_grounded` |
| `window` | * | any | * | `draft_for_inan_b2b` |
| `vendor_crew` | `confirm_received` | high | low | `auto_log_confirm` |
| `vendor_crew` | `unavailable` | any | high | `alert_inan_urgent` |
| `vendor_crew` | `briefing_confirm` | high | low | `auto_log_confirm` |
| `vendor_crew` | `emergency` | any | high | `alert_inan_and_sam_urgent` |
| any | confidence <0.5 | * | * | `escalate_inan` (fallback) |

### Action Definitions

| action | Apa yang terjadi |
|---|---|
| `auto_ack` | Kirim template ack langsung. Tidak ada AI generation. Lihat template `ack_off_hours_*` |
| `auto_reply` | AI generate balasan dengan template + grounding wiki, kirim langsung |
| `auto_reply_db_grounded` | AI generate balasan dengan data dari DB (pickup time, location, dll). Tidak ada open-ended LLM generation. |
| `auto_reply_redirect_klook` | Kirim template fixed: "Untuk perubahan/refund, mohon hubungi Klook CS di [link]" |
| `draft_for_inan` | AI generate draft. Kirim ke Telegram Inan untuk approve/edit/reject. |
| `draft_for_inan_b2b` | Sama seperti `draft_for_inan` tapi tone B2B. SLA approval lebih longgar (2 jam). |
| `escalate_inan` | Notif Telegram Inan: "Pesan baru butuh kamu lihat. Channel: X, intent: Y." Tidak ada draft. |
| `escalate_inan_urgent` | Sama tapi prioritas tinggi, notif berbeda (suara, pin). |
| `escalate_sam` | Notif Telegram Sam: "Pesan butuh keputusan kamu." |
| `escalate_sam_urgent` | Prioritas tinggi ke Sam. |
| `escalate_inan_or_sam` | Notif keduanya. Yang respond duluan ambil. |
| `alert_inan_urgent` | Khusus vendor/crew issue. Bunyi alarm. |
| `alert_inan_and_sam_urgent` | Emergency level. Bunyi alarm ke keduanya. |
| `auto_log_confirm` | Tidak ada outbound. Update DB: vendor/crew confirmed. |

---

## STEP 7 — Execute & Log

Setiap action yang menghasilkan outbound, log:
- `wa_messages` row dengan `direction=out`, `sender_type=ai|inan|sam|system`
- `wa_drafts` row jika draft (status=pending/approved/edited/rejected)
- `wa_conversations.last_outbound_at` update

**Sebelum kirim outbound, cek hard rules** (Section "Hard Rules" di bawah). Kalau ada satu pun melanggar → stop, escalate.

---

## TIME WINDOWS

### Business Hours
- **Senin–Sabtu**: 08:00–22:00 WIB (UTC+7)
- **Minggu**: 09:00–20:00 WIB
- **Hari libur nasional Indonesia**: 09:00–18:00 (fallback)

### Off-hours = di luar di atas.

### Inan's Working Hours (assumed)
- **Senin–Sabtu**: 08:00–20:00 WIB
- **Minggu**: 09:00–18:00 WIB
- Pesan masuk di luar window ini = `auto_ack` (untuk customer channel), queue untuk pagi (untuk vendor/crew).

### SLA per state

| channel + state | Target FRT (P50) | Target FRT (P95) |
|---|---|---|
| `jvto_inquiry` cold (business hours) | 15 menit | 1 jam |
| `jvto_inquiry` cold (off-hours) | 2 menit (auto_ack) | 12 jam (substantive) |
| `jvto_post_booking` pre_tour_prep | 30 menit | 2 jam |
| `jvto_post_booking` pre_tour_active (H-7 sd H-1) | 15 menit | 1 jam |
| `jvto_post_booking` d_day / in_tour | 5 menit | 30 menit |
| `klook` * | 1 jam | 4 jam |
| `klook` d_day | 15 menit | 1 jam |
| `window` * | 2 jam business | 12 jam |
| `vendor_crew` confirm follow-up | 30 menit | 4 jam |

---

## INTENT TAXONOMY (Seed)

### Inbox: customer / Channel: jvto_inquiry
- `inq_first_touch` — Pesan pertama, masih umum
- `inq_pricing_general` — "Berapa harga tour Bromo?"
- `inq_pricing_specific` — "Untuk 4 pax 3D2N berapa total?"
- `inq_availability` — "Tanggal X tersedia tidak?"
- `inq_itinerary_request` — "Boleh kirim itinerary?"
- `inq_inclusions` — "Apa saja yang termasuk?"
- `inq_custom_request` — "Bisa kustomisasi paket?"
- `inq_payment` — "Cara bayar bagaimana?"
- `inq_credentials` — "JVTO terdaftar atau tidak?"

### Inbox: customer / Channel: jvto_post_booking
- `pb_faq_pickup_time` — "Jam berapa pickup?"
- `pb_faq_what_to_bring` — "Apa yang harus saya bawa?"
- `pb_faq_dress_code`
- `pb_faq_weather`
- `pb_faq_difficulty`
- `pb_faq_meal`
- `pb_faq_screening` — "Skrining medis bagaimana?"
- `pb_logistics_pickup_location`
- `pb_logistics_driver_contact`
- `pb_change_date` — request perubahan
- `pb_change_pax` — request perubahan pax
- `pb_in_tour_request` — request saat in-tour (extra stop, dll)
- `pb_complaint`

### Inbox: customer / Channel: klook
- `klook_faq_pickup_time`
- `klook_faq_pickup_location`
- `klook_faq_what_to_bring`
- `klook_faq_dress_code`
- `klook_faq_duration`
- `klook_faq_meal`
- `klook_faq_weather`
- `klook_faq_difficulty`
- `klook_faq_screening`
- `klook_logistics_d_day`
- `klook_change_date` — auto-redirect
- `klook_refund_request` — auto-redirect
- `klook_complaint` — escalate

### Inbox: b2b_partner / Channel: window
- `window_availability_check`
- `window_quote_request`
- `window_confirm_booking`
- `window_change_request`
- `window_invoice_query`
- `window_payment_status`
- `window_relationship` — small talk, holiday greeting, dll

### Inbox: internal_ops / Channel: vendor_crew
- `confirm_received` — vendor balas confirm room/seat
- `unavailable` — vendor reject
- `briefing_confirm` — crew confirm briefing received
- `emergency` — anything urgent
- `question` — vendor/crew tanya detail

---

## TEMPLATES

Template disimpan di `wa_templates` table. Setiap template punya: `intent_slug`, `language`, `body_md`, `variables`. Variabel diganti saat eksekusi.

### `ack_off_hours_jvto_inquiry` (EN)
```
Hi, thanks for reaching out to JVTO. Our team replies within business hours (08:00–22:00 WIB / UTC+7). 

You'll get a substantive reply within {eta_hours} hours.

Meanwhile, our packages are here: https://javavolcano-touroperator.com/tours

— JVTO
```

### `ack_off_hours_jvto_inquiry` (ID)
```
Halo, terima kasih sudah menghubungi JVTO. Tim kami membalas pada jam kerja (08:00–22:00 WIB).

Kami akan balas detail dalam {eta_hours} jam.

Sambil menunggu, lihat paket tur kami: https://javavolcano-touroperator.com/tours

— JVTO
```

### `klook_faq_pickup_time` (EN)
```
Hi {name}, your pickup time for {tour_name} on {tour_date} is {pickup_time} at {pickup_location}.

Your driver is {driver_name} (contact: {driver_phone}).

Anything else you need to know before the tour?

— Inan, JVTO
```

### `klook_change_redirect` (EN)
```
Hi {name}, for booking changes or refunds, please contact Klook customer service directly:
https://www.klook.com/contact-us

This is because your booking was processed via Klook's system. They'll be able to help you faster than us.

— Inan, JVTO
```

### `pb_d_day_morning` (EN)
```
Hi {name}, today is the day! Your driver {driver_name} ({driver_phone}) will pick you up at {pickup_time} at {pickup_location}.

Travel safely, have an amazing time at {destination_name}. We're here if you need anything during the tour.

— JVTO
```

(Templates lain disusun saat implementation phase per intent di taksonomi.)

---

## HARD RULES (Never Cross These)

Sistem AI **tidak boleh pernah** melakukan hal berikut tanpa otorisasi manusia:

1. **Quote price.** Kalau intent berhubungan dengan harga, **selalu** escalate ke Sam atau pakai template fixed dari `wa_templates` yang sudah di-approve.
2. **Confirm room availability** untuk vendor. Hanya manusia yang baru saja cek kapasitas vendor yang boleh.
3. **Change booking date.** Hanya Inan/Sam yang otorisasi.
4. **Change booking pax.** Sama seperti di atas.
5. **Process refund** atau cancellation. Selalu escalate ke Sam.
6. **Make promises** yang tidak ada di template (mis. "kami akan tambahkan...", "untuk Anda gratis...").
7. **Reply to complaints** secara otomatis. Selalu escalate.
8. **Send anything to B2B (Window)** tanpa approval Inan/Sam.
9. **Reply to messages with attachments** (gambar tiket, paspor, dokumen) — selalu escalate karena kemungkinan konteks penting.
10. **Reply when sentiment negatif terdeteksi** — escalate ke Inan/Sam.
11. **Reply ke nomor yang tidak terdaftar di Step 3 lookup** untuk inbox `b2b_partner` atau `internal_ops`.
12. **Reply outside language coverage** — kalau bahasa selain ID/EN/MS dan confidence rendah, escalate.

Setiap pelanggaran = sistem stop dan escalate.

---

## ESCALATION DESTINATIONS

| Trigger | Destination | Channel |
|---|---|---|
| `escalate_inan` | Inan | Telegram bot @JVTOInanBot, channel #wa-queue |
| `escalate_inan_urgent` | Inan | Telegram + push notification + sound |
| `escalate_sam` | Sam | Telegram bot @JVTOSamBot, channel #wa-decisions |
| `escalate_sam_urgent` | Sam | Telegram + push + sound |
| `alert_inan_and_sam_urgent` | Inan + Sam | Both, with siren |
| Hard rule violation | Both | Both with detail "rule violated: X" |

Format escalation message:
```
[CHANNEL] {channel_name}
[FROM] {customer_name or phone}
[STATE] {state}
[INTENT] {intent} (confidence {conf})
[URGENCY] {urgency}
[LAST 3 MESSAGES]:
  {msg1}
  {msg2}
  {msg3}
[ACTION NEEDED] {auto-detected suggestion}
```

---

## FALLBACK BEHAVIOR

Kalau apapun gagal:
- Classifier gagal → action = `escalate_inan` dengan label `unclassified`.
- DB query gagal → log error, kirim `auto_ack` generic, escalate Inan.
- LLM API down → semua incoming → `escalate_inan` dengan label `ai_unavailable`. Inan handle manual sampai service kembali.
- WA Pro CRM send API gagal → retry 3x dengan exponential backoff. Setelah gagal final → alert Inan via Telegram langsung.

**Aturan emas:** Sistem tidak boleh diam. Kalau bingung, eskalasi. Lebih baik Inan terganggu sekali daripada customer didiamkan.

---

## REVIEW & DRIFT DETECTION

Mingguan, auto-generate report:
- 20 sample auto-reply random → manual review untuk brand voice compliance.
- Draft approval rate per intent.
- Reject rate per intent (kalau >15% → re-prompt atau matikan intent itu).
- Hard rule violations (harusnya 0 — kalau ada, post-mortem).
- Customer complaint atau negative review yang menyebut komunikasi (proxy: ada miss).

Threshold untuk **matikan auto-reply intent**:
- Reject rate >15% selama 1 minggu → fallback ke `draft_for_inan`.
- Hard rule violation ≥1 dalam minggu → fallback ke `draft_for_inan` + post-mortem.
- Negative customer feedback yang specifically menyebut auto-reply → review immediately.

---

## VERSION

- v1.0 — 2026-05-14 (initial seed)
- Future versions: append change log here, increment last_updated di frontmatter.
