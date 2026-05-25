---
type: source
title: Backoffice — Finance Overview
last_updated: 2026-05-25
sources: [backoffice-mysql]
---

# Backoffice Finance — Live DB Snapshot

Source: live MySQL `u1805424_jvto_clone` (Hostinger). Snapshot 2026-05-25.
All money values are aggregates only; no per-customer detail in this wiki page.
Raw line items live in `raw/backoffice/csv/` (gitignored).

## Totals

- **Bookings tracked:** 1,453
- **Grand total IDR (all-time):** Rp 3,952,749,425
- **Grand total USD (all-time):** $0.00
- **Total recorded cost (COGS):** Rp 100,299,000
- **Avg margin per booking:** Rp 7,656,636 (over 22 bookings with margin populated)
- **Outstanding debt (across all bookings):** Rp 0

## Currency mix

| Currency | Bookings |
|---|---:|
| ? | 1,113 |
| IDR | 340 |

## Booking status distribution

| Status | Count |
|---|---:|
| `booked` | 1,197 |
| `?` | 183 |
| `pending wise` | 72 |
| `pending pay later` | 1 |

## Payment status

| Payment status | Count |
|---|---:|
| `pending` | 1,453 |

## Channel mix (`bookings.channel_tag`)

| Channel | Count |
|---|---:|
| `(none)` | 1,453 |

## Payment method on booking (`bookings.payment_method`)

| Method | Count |
|---|---:|
| `pay later` | 951 |
| `cc` | 281 |
| `(none)` | 169 |
| `wise` | 52 |

## Revenue by month (IDR + other ccy combined for count)

| Month | Bookings | Total IDR | Other ccy (USD etc.) |
|---|---:|---:|---:|
| 2022-07 | 1 | Rp 0 | 7,650,000.00 |
| 2022-08 | 1 | Rp 0 | 3,700,000.00 |
| 2022-11 | 6 | Rp 0 | 49,050,000.00 |
| 2022-12 | 5 | Rp 0 | 67,450,000.00 |
| 2023-01 | 8 | Rp 15,200,000 | 70,285,000.00 |
| 2023-02 | 5 | Rp 0 | 35,110,000.00 |
| 2023-03 | 43 | Rp 0 | 48,100,000.00 |
| 2023-04 | 7 | Rp 27,200,000 | 0.00 |
| 2023-05 | 28 | Rp 20,875,000 | 0.00 |
| 2023-06 | 29 | Rp 0 | 0.00 |
| 2023-07 | 18 | Rp 9,850,000 | 25,650,000.00 |
| 2023-08 | 28 | Rp 7,875,000 | 93,721,500.00 |
| 2023-09 | 31 | Rp 64,335,000 | 148,681,000.00 |
| 2023-10 | 18 | Rp 9,300,000 | 124,803,630.00 |
| 2023-11 | 14 | Rp 0 | 212,789,500.00 |
| 2023-12 | 17 | Rp 16,830,625 | 235,643,000.00 |
| 2024-01 | 24 | Rp 0 | 343,135,800.00 |
| 2024-02 | 21 | Rp 23,840,000 | 147,338,600.00 |
| 2024-03 | 37 | Rp 89,231,300 | 287,589,828.00 |
| 2024-04 | 15 | Rp 48,360,000 | 149,520,001.00 |
| 2024-05 | 54 | Rp 65,932,500 | 534,322,514.00 |
| 2024-06 | 35 | Rp 148,610,000 | 155,546,669.00 |
| 2024-07 | 62 | Rp 169,400,000 | 477,608,013.00 |
| 2024-08 | 49 | Rp 64,000,000 | 455,429,000.00 |
| 2024-09 | 38 | Rp 58,560,000 | 335,103,998.00 |
| 2024-10 | 18 | Rp 17,490,000 | 110,258,000.00 |
| 2024-11 | 21 | Rp 92,235,000 | 139,221,000.00 |
| 2024-12 | 18 | Rp 4,750,000 | 354,889,000.00 |
| 2025-01 | 26 | Rp 112,050,000 | 412,686,051.65 |
| 2025-02 | 18 | Rp 22,030,000 | 317,308,000.00 |
| 2025-03 | 43 | Rp 252,290,000 | 284,777,000.00 |
| 2025-04 | 54 | Rp 212,490,000 | 299,385,500.00 |
| 2025-05 | 63 | Rp 170,590,000 | 272,878,000.00 |
| 2025-06 | 74 | Rp 205,290,000 | 438,166,000.00 |
| 2025-07 | 74 | Rp 160,150,000 | 269,518,000.00 |
| 2025-08 | 53 | Rp 288,550,000 | 203,528,000.00 |
| 2025-09 | 39 | Rp 147,930,000 | 106,151,000.00 |
| 2025-10 | 27 | Rp 111,755,000 | 222,992,000.00 |
| 2025-11 | 30 | Rp 148,280,000 | 126,716,000.00 |
| 2025-12 | 56 | Rp 471,465,000 | 155,819,000.00 |
| 2026-01 | 42 | Rp 154,100,000 | 245,402,000.00 |
| 2026-02 | 45 | Rp 171,590,000 | 225,581,000.00 |
| 2026-03 | 64 | Rp 132,585,000 | 356,427,500.00 |
| 2026-04 | 93 | Rp 237,730,000 | 411,639,500.00 |
| 2026-07 | 1 | Rp 0 | 21,501,000.00 |

## Payment ledger — nominal by payment method

Total payment records: 506

| Method (id) | Method name | Count | Total nominal |
|---|---|---:|---:|
| 3 | Debit/Credit Card | 333 | 1,573,639,000 |
| 2 | PT JAVA VOLCANO RENDEZVOUS | 79 | 247,027,278 |
| 5 | WISE | 35 | 285,428,500 |
| 6 | Bank Transfer | 31 | 373,916,482 |
| 1 | Cash | 27 | 354,667,000 |
| 4 | EDC | 1 | 13,860,000 |

## Invoice history breakdown

Total invoice line items: 1,002

| Line type | Count | Sum line_total |
|---|---:|---:|
| `package` | 871 | 10,035,764,247 |
| `add on` | 131 | 113,813,800 |

## Accounts (chart of accounts in backoffice)

Total account records: 3

| Account | Type | Code |
|---|---|---|
| admin | - | - |
| sam | - | - |
| JVTO | - | - |

## Cross-references

- [[finance/rate-card-package]] — compare template rate card vs realized prices in [[sources/backoffice-pricing]]
- [[sources/backoffice-pricing]] — package_prices vs realized booking totals
- [[sources/backoffice-bookings-ops]] — booking volume drives this revenue
- [[ops/intake-gate]] — Workflow 7 registration for this source
