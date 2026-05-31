---
type: source
title: Backoffice — WhatsApp Operations
last_updated: 2026-05-25
sources: [backoffice-mysql]
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/sources/backoffice-mysql]
---

# Backoffice WhatsApp — Conversation Analytics

Snapshot 2026-05-25. 5,547 chat messages, 640 daily summaries.
Individual messages stay in raw layer — only aggregates here.

## Volume

- **Total chat messages:** 5,547
- **Daily summaries:** 640
- **Itineraries shared via WA:** 2,985
- **WhatsApp send logs:** 3,608
- **Distinct customers in chat:** 159

## Direction (`is_from_me`)

| 0 = from user, 1 = from JVTO | Count |
|---|---:|
| `1` | 3,516 |
| `0` | 2,031 |

## Media presence

| has_media | Count |
|---|---:|
| `0` | 5,041 |
| `1` | 506 |

## Message volume by month

| Month | Messages |
|---|---:|
| 2025-05 | 3,464 |
| 2025-06 | 2,083 |

## Intent / category distribution (from `wa_chat_summaries`)

Intent taxonomy seeded by `WaIntentTaxonomySeeder` — 26 categories.

| Category | Summary entries |
|---|---:|
| Jadwal Perjalanan | 161 |
| Percakapan Kosong | 108 |
| Informasi Perjalanan | 96 |
| Konfirmasi Booking | 90 |
| Koordinator Lokasi | 31 |
| Masalah Pembayaran | 24 |
| Umpan Balik Klien | 22 |
| Hadiah dan Promo | 18 |
| Perencanaan Perjalanan | 16 |
| Konfirmasi Jadwal | 15 |
| Pesanan Produk | 15 |
| Pengembalian Dana | 8 |
| Permintaan Informasi | 6 |
| Kendala Pembayaran | 5 |
| Dukungan Teknis | 3 |
| Penawaran Kerja Sama | 3 |
| Permintaan Produk | 3 |
| Permintaan Khusus | 3 |
| Pilihan Menu | 3 |
| Berbagi Dokumen | 2 |
| Permintaan Desain | 2 |
| Pelunasan Produk | 2 |
| Panduan Drone | 1 |
| Undangan Gathering | 1 |
| Daftar Pesanan | 1 |
| Insiden Perjalanan | 1 |

## Top conversations (by message count) — anonymized

Customer identity intentionally omitted; raw layer has user mapping.

| Rank | Messages |
|---:|---:|
| #1 | 1,131 |
| #2 | 276 |
| #3 | 181 |
| #4 | 161 |
| #5 | 97 |
| #6 | 94 |
| #7 | 90 |
| #8 | 86 |
| #9 | 77 |
| #10 | 75 |
| #11 | 69 |
| #12 | 68 |
| #13 | 68 |
| #14 | 67 |
| #15 | 64 |
| #16 | 63 |
| #17 | 63 |
| #18 | 62 |
| #19 | 61 |
| #20 | 60 |

## Cross-references
- [[whatsapp/ops-playbook]] — WA ops procedures (manual)
- [[whatsapp/canned-responses]] — template messages
- [[sources/backoffice-bookings-ops]] — conversion from chat to booking
