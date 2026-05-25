---
type: ops
title: Backoffice MySQL Extraction Playbook
last_updated: 2026-05-25
sources: [backoffice-mysql]
---

# Backoffice Extraction Playbook

How to re-extract live data from the backoffice MySQL DB into `raw/backoffice/` and refresh `wiki/sources/backoffice-*.md`.

## What this is

Pipeline that reads the live JVTO backoffice (Laravel app at `f:/BACK OFFICE/new-backoffice`, MariaDB 10.11 on Hostinger) and produces:

1. **Raw layer (gitignored)** — `raw/backoffice/csv/*.csv`, `raw/backoffice/dumps/*.sql`. Full data, contains PII.
2. **Schema layer (commit-safe)** — `raw/backoffice/schema/full-schema.sql`. DDL only, no rows.
3. **Manifest (commit-safe)** — `raw/backoffice/_manifest.md`. Table inventory + classification.
4. **Wiki summaries (commit-safe)** — `wiki/sources/backoffice-*.md`. Aggregate stats, no PII.

## When to re-run

- After significant backoffice activity (≥100 new bookings or month boundary).
- Before generating finance reports or pricing analysis.
- On demand for ad-hoc analytics requests.

Snapshot date is encoded in `last_updated` of each generated page.

## Pipeline steps

All scripts live in `scripts/` and use `scripts/_db.py` for connection (reads `.env` from backoffice app).

```bash
cd e:/Users/JAVA VOLCANO/llm-wiki

# 1. Inventory tables + classify
python scripts/inventory.py
# → raw/backoffice/_inventory.json

# 2. Build manifest markdown
python scripts/build_manifest.py
# → raw/backoffice/_manifest.md

# 3. Dump schema (commit-safe)
python scripts/dump_schema.py
# → raw/backoffice/schema/full-schema.sql

# 4. Dump data to CSV (gitignored — PII)
python scripts/dump_data.py
# → raw/backoffice/csv/<table>.csv

# 5. Generate wiki/sources/backoffice-*.md
python scripts/analyze.py
# → 8 pages under wiki/sources/

# 6. PII guard (must show 0 hits)
grep -rE "@[a-zA-Z0-9._%+-]+\.(com|id|net|org|co)" wiki/sources/backoffice-*.md
grep -rE "\+?62[0-9]{9,}|\+?[0-9]{11,}" wiki/sources/backoffice-*.md
```

End-to-end runtime: ~3 minutes for ~63k rows across 148 non-empty tables.

## Generated pages

| Page | Domain | Source tables |
|---|---|---|
| [[sources/backoffice-schema]] | meta | INFORMATION_SCHEMA + FK web + 210-table inventory |
| [[sources/backoffice-finance]] | finance | bookings, booking_payments, invoice_histories, payment_methods, accounts |
| [[sources/backoffice-pricing]] | pricing | package_prices, packages, price_plans, bookings (realized) |
| [[sources/backoffice-bookings-ops]] | bookings | bookings, book_*, agents |
| [[sources/backoffice-staff]] | people | guide_drivers, crew_roles, review_guides, book_guide_drivers |
| [[sources/backoffice-vendors]] | vendors | vendors, vendor_categories, hotels, cars |
| [[sources/backoffice-master-data]] | reference | accounts, payment_methods, crew_roles, booking_categories, … |
| [[sources/backoffice-whatsapp]] | whatsapp | wa_chats, wa_chat_summaries, wa_chat_categories, wa_logs |

## PII handling rules

| Layer | Allowed | Forbidden |
|---|---|---|
| `raw/backoffice/csv/` | Everything (full DB) | n/a — gitignored, never pushed |
| `raw/backoffice/schema/` | DDL, table comments | No data |
| `raw/backoffice/_manifest.md` | Table names, row counts | No row content |
| `wiki/sources/backoffice-*.md` | Aggregate stats, internal staff names (already public in `wiki/people/`), template prices, anonymized rankings | Customer name/email/phone/address, payment references, bank account numbers, license/KTP numbers, individual messages |

The `pii_scrub()` helper in `scripts/analyze.py` provides defense-in-depth on any free-text field written to wiki.

## Connection config

DB credentials live in `f:/BACK OFFICE/new-backoffice/.env`:

- `DB_HOST=153.92.9.37` (Hostinger remote)
- `DB_PORT=3306`
- `DB_DATABASE=u1805424_jvto_clone`
- `DB_USERNAME=u1805424_jvto_clone`
- `DB_PASSWORD=` *(in .env, never commit)*

If remote MySQL is blocked (Hostinger IP whitelist), fallback:
1. SSH tunnel: `ssh -L 3306:localhost:3306 user@server.hostinger.com`, then change `DB_HOST=127.0.0.1` in a local override.
2. Run dump on Hostinger SSH, scp the CSVs back.

## Cross-references

- [[ops/intake-gate]] — Workflow 7 universal raw intake gate (registration target)
- [[ops/ingestion-profiles]] — Workflow 4 typed source handlers (db-export type)
- [[sources/backoffice-schema]] — entry point for all backoffice DB exploration
- [[finance/rate-cards]] — manual rate card SSOT to reconcile against `backoffice-pricing`
