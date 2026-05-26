# Reference: Python Extraction Scripts

7 scripts under `scripts/` form the backoffice MySQL extraction pipeline. They connect to the JVTO backoffice database (MariaDB 10.11 at Hostinger), extract schema and data, and generate wiki source pages with PII scrubbed.

## Prerequisites

- Python 3.x
- `pymysql` package (`pip install pymysql`)
- Access to the backoffice `.env` file at `f:/BACK OFFICE/new-backoffice/.env` (contains DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
- Network access to the Hostinger MySQL server

## Pipeline Phases

The scripts run in three phases:

```
Phase A: inventory.py          → raw/backoffice/_inventory.json
Phase B: dump_schema.py        → raw/backoffice/schema/full-schema.sql
         dump_data.py          → raw/backoffice/csv/*.csv  (gitignored)
         build_manifest.py     → raw/backoffice/_manifest.md
Phase C: analyze.py            → wiki/sources/backoffice-*.md  (8 pages)
```

Utility: `peek.py` (ad-hoc column inspection, any phase)

## Script Reference

### `_db.py` — Shared DB Connection

Reads database credentials from the `.env` file and returns a `pymysql` connection with `DictCursor`.

```python
from _db import connect
conn = connect()
```

- **Env file path**: `f:/BACK OFFICE/new-backoffice/.env`
- **Required env vars**: `DB_HOST`, `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE`
- **Optional env var**: `DB_PORT` (default: 3306)
- **Charset**: `utf8mb4`
- **Connect timeout**: 20 seconds

### `inventory.py` — Phase A: Table Inventory

Connects to the database, enumerates all tables, counts rows, measures size, and classifies each table into one of three buckets.

```bash
cd scripts && python inventory.py
```

**Output**: `raw/backoffice/_inventory.json` — array of objects with fields:
- `name`: table name
- `rows_actual`: row count
- `size_kb`: table size in KB
- `bucket`: `framework` | `sensitive` | `business`

**Classification rules**:
- `framework`: Laravel infrastructure (migrations, sessions, cache, jobs, telescope, etc.)
- `sensitive`: tables containing customer PII (bookings, customers, invoices, payments, identity_card, etc.)
- `business`: everything else (packages, destinations, hotels, activities, etc.)

### `dump_schema.py` — Phase B1: Schema Export

Dumps `SHOW CREATE TABLE` DDL for all 210 tables. No data, safe to commit.

```bash
cd scripts && python dump_schema.py
```

**Output**: `raw/backoffice/schema/full-schema.sql`

### `dump_data.py` — Phase B2: CSV Data Export

Exports table data as CSV files. Framework tables are skipped. Empty tables are skipped.

```bash
cd scripts && python dump_data.py
```

**Output**: `raw/backoffice/csv/{table_name}.csv` (one file per non-empty, non-framework table)

**PII handling**: Raw CSV layer is gitignored entirely. PII minimization happens at the wiki layer (Phase C) where `analyze.py` aggregates and scrubs before writing to `wiki/sources/`.

### `build_manifest.py` — Phase B3: Manifest Generation

Generates a human-readable manifest from `_inventory.json`. Assigns each table to a domain (whatsapp, finance, bookings, people, vehicles, hotels, products, vendors, reviews, media, misc) by name pattern matching.

```bash
cd scripts && python build_manifest.py
```

**Output**: `raw/backoffice/_manifest.md` — grouped by bucket (business/sensitive/framework) with domain tags.

### `peek.py` — Utility: Column Inspector

Shows column metadata and a sample row for specified tables. Useful for ad-hoc exploration before writing extraction queries.

```bash
cd scripts && python peek.py bookings hotels package_prices
# No arguments = inspect default set of 12 key tables
cd scripts && python peek.py
```

**Output**: Prints to stdout. For each table: column name, data type, nullable, key status, and column comment.

**Default tables** (when no arguments): bookings, booking_payments, invoice_histories, guide_drivers, cars, vendors, hotels, tw_calculations, tw_calculation_details, wa_chats, wa_chat_summaries, package_prices.

### `analyze.py` — Phase C: Wiki Source Page Generator

Reads CSV dumps and runs live DB aggregation queries. Produces 8 wiki source pages under `wiki/sources/backoffice-*.md` with PII scrubbed.

```bash
cd scripts && python analyze.py
```

**Output pages**:

| Wiki page | Content |
|-----------|---------|
| `backoffice-schema` | 210-table inventory, Mermaid ERD, FK web |
| `backoffice-finance` | Revenue by month, currency mix, payment methods, debt |
| `backoffice-pricing` | Template vs realized pricing per package |
| `backoffice-bookings-ops` | Booking volume, pax distribution, lead time, channels |
| `backoffice-staff` | Crew levels, roles, licenses, star ratings, deployment counts |
| `backoffice-vendors` | Vendor categories, hotel partners, car fleet |
| `backoffice-master-data` | Reference catalogs (accounts, roles, categories, etc.) |
| `backoffice-whatsapp` | Conversation analytics, message direction/media breakdown |

**PII defense-in-depth**: `analyze.py` strips emails and phone numbers from all output using regex patterns. Customer names are never written to wiki pages — only aggregate counts and staff names (already public in `wiki/people/`).

## Security Notes

- The `.env` file contains production database credentials. Never commit it.
- `raw/backoffice/dumps/` and `raw/backoffice/csv/` are gitignored (contain PII).
- `raw/backoffice/_inventory.json` and `raw/backoffice/_export_summary.json` are also gitignored.
- Only `raw/backoffice/schema/` (DDL, no data) and `raw/backoffice/_manifest.md` are safe to commit.

## Related

- [Reference: Wiki Structure](reference-wiki-structure.md) — where the output pages live in the wiki
- [wiki/internal-ops/backoffice-extraction.md](../wiki/internal-ops/backoffice-extraction.md) — the operational playbook for running extractions
- [wiki/sources/backoffice-schema.md](../wiki/sources/backoffice-schema.md) — entry point for all backoffice DB questions
