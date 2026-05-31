---
type: source
title: Backoffice — Bookings & Ops
last_updated: 2026-05-25
sources: [backoffice-mysql]
owner: wiki-llm
stale_after_days: 90
pages_updated: []
---

# Backoffice — Bookings & Operational Patterns

Snapshot 2026-05-25. 1,453 bookings tracked.

## Headline metrics

- **Total bookings:** 1,453
- **Total pax served (all-time, sum):** 4,709
- **Avg lead time (booking_date → travel_date_start):** 36.6 days (n=1401)
- **Avg trip duration:** 3.42 days (n=1422)
- **Bookings with police escort:** 9 (0.6%)
- **Bookings with ISIC purchase:** 1 (0.1%)
- **Guide/driver assignments tracked:** 2,105
- **Car assignments:** 1,065
- **Hotel assignments:** 2,487
- **Jeep assignments:** 98

## Pax distribution per booking

| Pax per booking | Count |
|---:|---:|
| 1 | 47 |
| 2 | 694 |
| 3 | 155 |
| 4 | 162 |
| 5 | 78 |
| 6 | 53 |
| 7 | 18 |
| 8 | 26 |
| 9 | 8 |
| 10 | 20 |
| 11 | 8 |
| 12 | 6 |
| 13 | 7 |
| 14 | 5 |
| 15 | 5 |
| 16 | 3 |
| 17 | 2 |
| 18 | 2 |
| 19 | 1 |
| 20 | 2 |
| 21 | 2 |
| 23 | 1 |
| 25 | 2 |
| 27 | 2 |
| 31 | 1 |
| 34 | 1 |
| 40 | 1 |

## Bookings by month

| Month | Bookings | Total pax |
|---|---:|---:|
| 2022-07 | 1 | 3 |
| 2022-08 | 1 | 1 |
| 2022-11 | 6 | 35 |
| 2022-12 | 5 | 24 |
| 2023-01 | 8 | 21 |
| 2023-02 | 5 | 25 |
| 2023-03 | 43 | 274 |
| 2023-04 | 7 | 25 |
| 2023-05 | 28 | 126 |
| 2023-06 | 29 | 104 |
| 2023-07 | 18 | 88 |
| 2023-08 | 28 | 128 |
| 2023-09 | 31 | 139 |
| 2023-10 | 18 | 79 |
| 2023-11 | 14 | 63 |
| 2023-12 | 17 | 78 |
| 2024-01 | 24 | 108 |
| 2024-02 | 21 | 59 |
| 2024-03 | 37 | 163 |
| 2024-04 | 15 | 54 |
| 2024-05 | 54 | 147 |
| 2024-06 | 35 | 85 |
| 2024-07 | 62 | 174 |
| 2024-08 | 49 | 179 |
| 2024-09 | 38 | 108 |
| 2024-10 | 18 | 46 |
| 2024-11 | 21 | 66 |
| 2024-12 | 18 | 99 |
| 2025-01 | 26 | 149 |
| 2025-02 | 18 | 73 |
| 2025-03 | 43 | 158 |
| 2025-04 | 54 | 144 |
| 2025-05 | 63 | 124 |
| 2025-06 | 74 | 195 |
| 2025-07 | 74 | 147 |
| 2025-08 | 53 | 160 |
| 2025-09 | 39 | 74 |
| 2025-10 | 27 | 85 |
| 2025-11 | 30 | 67 |
| 2025-12 | 56 | 196 |
| 2026-01 | 42 | 117 |
| 2026-02 | 45 | 131 |
| 2026-03 | 64 | 169 |
| 2026-04 | 93 | 213 |
| 2026-07 | 1 | 6 |

## Top 30 template packages (by booking volume)

| template_package_id | Bookings |
|---|---:|
| (none) | 1,453 |

## Agents / sales channels (`bookings.agent_id`)

| Agent id | Name | Bookings |
|---|---|---:|
| 2 | JVTO | 955 |
| 1 | TWT | 304 |
| (none) | - | 170 |
| 4 | Union | 12 |
| 3 | DH Trans | 9 |
| 6 | Igo Tours | 2 |
| 5 | Java Land Tour | 1 |

## Cross-references
- [[sources/backoffice-finance]] — revenue derived from these bookings
- [[sources/backoffice-staff]] — guide/driver assignments via `book_guide_drivers`
- [[sources/backoffice-pricing]] — packages booked
