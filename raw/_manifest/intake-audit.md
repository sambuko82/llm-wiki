# Intake Audit — 2026-05-25 (refresh)

*Automated audit of raw file coverage against manifest indices. Previous audit dated 2026-05-25 (pre-backoffice) showed 57 raw files.*

---

## Summary

| Metric | Count | Δ vs prior |
|--------|------:|------:|
| Total raw files (excl. _inbox, _manifest, backoffice csv/dumps) | 64 | +7 |
| Indexed in `raw-files-index.csv` | 64 | +7 |
| Tracked in `ingest-status.csv` | 64 | +7 (was 61 — backfilled R062-R064) |
| Source URLs in `source-url-index.csv` | 64 | +7 (was 57 — backfilled R058-R064) |
| Files in `_inbox/` (pending) | 0 | 0 |

## Coverage

| Check | Status |
|-------|--------|
| All raw files indexed | PASS (64/64) |
| All raw files tracked in ingest-status | PASS (64/64) — fixed gap during this audit |
| All raw files have source-url-index row | PASS (64/64) — fixed gap during this audit |
| Inbox empty | PASS (0 pending) |
| Manifest files present | PASS (10 files) |
| Future-dated entries | FIXED — 4 entries dated 2026-05-26 corrected to 2026-05-25 |
| New taxonomy entries (`db-export`, `internal_pii`) | DOCUMENTED in `wiki/ops/intake-gate.md` |
| PII leak check on `wiki/sources/backoffice-*.md` | PASS — 0 emails, 0 phone numbers |
| Backoffice raw layer gitignored | PASS — `raw/backoffice/csv/`, `dumps/`, `_inventory.json`, `_export_summary.json` |

## File Types Breakdown

| Type | Count |
|------|-------|
| .md (Markdown) | 25 |
| .xlsx (Excel) | 17 |
| .json (JSON) | 10 |
| .gpx (GPS tracks) | 5 |
| .pdf (PDF) | 2 |
| .csv (CSV data) | 2 |
| .xml (XML) | 1 |
| .sql (SQL DDL) | 1 *(new — backoffice schema)* |
| .html (HTML) | 1 |

## Directory Distribution

| Directory | Count | Notes |
|-----------|------:|-------|
| `raw/` (root) | 37 | unchanged |
| `raw/FINANCE/` | 15 | unchanged |
| `raw/FINANCE/rate_cards/` | 5 | unchanged |
| `raw/backoffice/` | 2 (committed) | `_manifest.md` + `schema/full-schema.sql` |
| `raw/backoffice/csv/` | 148 (gitignored) | PII layer, not counted toward indexed total |
| `raw/backoffice/dumps/` | 0 currently | reserved for SQL dumps; gitignored |

## Manifest Registry Counts

| Registry | Entries | Δ |
|----------|---------|---|
| category-registry.yml | 29 categories | 0 |
| tag-registry.yml | 35 tags | 0 (REC-006 / REC-007 still pending) |
| evidence-registry.yml | 18 evidence items E001-E018 (C1-C9) | +4 (E015-E018 added 2026-05-25/26) |
| conflict-log.md | 3 open conflicts | 0 |
| recommendation-log.md | 14 entries (5 done, 9 pending) | +4 (REC-011..REC-014) |
| claim-registry.yml | 9 claims (C1-C9) | NEW |
| entity-registry.yml | 50 entities (ENT-001-ENT-050) | NEW |
| decision-queue.md | 5 items (DQ-001-DQ-005) | NEW (seeded from CONF + REC) |

## Open Conflicts

| ID | Subject | Status |
|----|---------|--------|
| CONF-001 | Stefan Loose year/ISBN (2016 vs 2018) | open — blocked on physical book check |
| CONF-002 | Madakaripura height (~100m vs ~200m) | open — under reconciliation |
| CONF-003 | Second NIB 0220001393513 | open — blocked on OSS portal |

No new conflicts detected from backoffice extraction. Realized pricing vs template rate-cards comparison may surface CONF-004+ once REC-012 executes.

## Governance Layer Counts

| Check | Count | Notes |
|-------|------:|-------|
| Claims registered (claim-registry.yml) | 9 | C1-C9, all verified |
| Entities registered (entity-registry.yml) | 50 | ENT-001–ENT-050 across 10 types |
| Decision queue items (decision-queue.md) | 5 | DQ-001–DQ-005 (3 conflicts + 2 safety) |
| Entity proposals pending | 0 | No pending entity proposals |
| Claim proposals pending | 0 | All 9 claims registered |
| Website URL proposals (sitemap-proposals.md) | 0 | No pending proposals |
| Internal output proposals (rec-log type=new_page) | 3 | REC-003, REC-008, REC-013 |
| Unknown classifications | 0 | All 64 raw files classified |

## Pending Recommendations

| ID | Type | Status | Notes |
|----|------|--------|-------|
| REC-003 | new_page (permit-requirements cross-refs) | pending | link from destination pages |
| REC-004 | new_page (rate-cards source link) | pending | inbound link from finance/rate-cards |
| REC-005 | update (batch-log 37 raw files) | pending | low priority |
| REC-006 | new_tag (ferry-crossing) | pending | |
| REC-007 | new_tag (taman-safari) | pending | |
| REC-008 | new_page (safety-incidents) | pending | low priority unless /safety page built |
| REC-009 | new_url (Silo 3 ijen-safety-incidents) | pending | `human_decision_required` — named fatalities |
| REC-010 | update (Buleleng Hiace verification) | pending | `human_decision_required` |
| REC-012 | update (validate rate-cards vs backoffice-pricing) | pending | **next sprint priority** |
| REC-013 | new_page (whatsapp/conversation-analytics) | pending | distilled from backoffice-whatsapp |

## What changed in this audit

1. **Backfilled `ingest-status.csv`** with R062 (backoffice schema), R063 (manifest), R064 (CSVs).
2. **Backfilled `source-url-index.csv`** with R058-R064 (Ijen safety + verification dossier + safety protocol + backoffice triplet) — these were ingested but never had source-url rows added.
3. **Fixed 4 future-dated entries** (ingest_date 2026-05-26 → 2026-05-25). Today is 2026-05-25 per session memory; previous dates were off-by-one.
4. **Added 2 new taxonomy values** to `wiki/ops/intake-gate.md`: source_type `db-export`, visibility `internal_pii`.
5. **Logged 4 new recommendations** (REC-011 through REC-014) capturing the taxonomy update, finance/pricing reconciliation, conversation-analytics opportunity, and audit verification.
6. **Wiki/sources catalog**: 40 pages now (was 32). 8 new backoffice-* pages from this week's extraction.

## Outstanding signals

- `wiki/sources/` (40 pages) is the only domain growing faster than weekly health-check cadence can audit. Consider extending Workflow 6 with a quarterly "sources lint" pass that checks each `sources/*.md` for: (a) inbound wikilink count, (b) `last_updated` freshness, (c) source-url-index parity.
- Backoffice extraction introduces a new ingestion *cadence* concept: same source (DB) re-extracted periodically. Current intake-gate spec assumes one-shot files. May warrant a `freshness_policy` column in raw-files-index.csv (one-shot | weekly | monthly | quarterly | on-demand).

---

*Next audit: run after next ingest batch or weekly health check. Scheduled trigger: any `raw/_inbox/` file landing, or manual "intake audit" command.*
