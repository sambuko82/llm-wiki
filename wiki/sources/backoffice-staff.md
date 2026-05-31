---
type: source
title: Backoffice — Staff (Guides & Drivers)
last_updated: 2026-05-25
sources: [backoffice-mysql]
owner: wiki-llm
stale_after_days: 90
pages_updated: []
---

# Backoffice Staff — Guide / Driver Roster

Snapshot 2026-05-25. 74 crew records (50 soft-deleted).
Internal use only — names appear in [[people/guides]] and [[people/drivers]].
License numbers, KTP, emails, phones are in the raw layer (`raw/backoffice/csv/guide_drivers.csv`) — not echoed here.

## Headline

- **Total crew records:** 74
- **Active (not soft-deleted):** 24
- **Marked as driver (`is_driver=1`):** 35
- **Marked as Ijen-certified (`is_ijen=1`):** 5
- **With `guide_license` populated:** 56
- **With `driver_license` populated:** 56
- **With `ktp` populated:** 54
- **Avg star rating:** 5.00 (over 46 rated)
- **Avg rate (IDR/trip):** 241,667 (over 24 with rate)

## Crew level distribution (`crew_level`)

| Level | Count |
|---|---:|
| `(none)` | 39 |
| `green` | 16 |
| `red` | 15 |
| `yellow` | 4 |

## New role distribution (`new_role`)

| Role | Count |
|---|---:|
| `(none)` | 50 |
| `Outsource` | 8 |
| `Escort Guide (Junior)` | 5 |
| `Escort Guide (Senior)` | 4 |
| `Only Driver` | 4 |
| `Driver cum guide` | 3 |

## Role assignment via `crew_id`

| Role (crew_roles.id) | Role name | Count |
|---|---|---:|
| (none) | - | 31 |
| 0 | - | 22 |
| 1 | role_1 | 3 |
| 2 | role_2 | 2 |
| 3 | role_3 | 1 |
| 7 | role_7 | 1 |
| 8 | role_8 | 1 |
| 6 | role_6 | 1 |
| 4 | role_4 | 1 |
| 13 | role_13 | 1 |
| 10 | role_10 | 1 |
| 5 | role_5 | 1 |
| 9 | role_9 | 1 |
| 12 | role_12 | 1 |
| 15 | - | 1 |
| 21 | - | 1 |
| 14 | role_14 | 1 |
| 20 | - | 1 |
| 19 | - | 1 |
| 18 | - | 1 |

## Assignment volume (top 30 most-deployed crew)

Total assignment records: 2,105.

| Crew id | Name | Assignments |
|---|---|---:|
| ? | - | 2105 |

## Review signal

- **Internal `review_guides` rows:** 10

## Cross-references
- [[people/guides]] — public guide bios
- [[people/drivers]] — public driver roster
- [[sources/backoffice-bookings-ops]] — booking volume that drives assignments
