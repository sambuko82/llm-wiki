# Intake Audit — 2026-05-25

*Automated audit of raw file coverage against manifest indices.*

---

## Summary

| Metric | Count |
|--------|-------|
| Total raw files (excl. _inbox, _manifest) | 57 |
| Indexed in raw-files-index.csv | 57 |
| Tracked in ingest-status.csv | 57 |
| Source URLs in source-url-index.csv | 57 |
| Files in _inbox (pending) | 0 |

## Coverage

| Check | Status |
|-------|--------|
| All raw files indexed | PASS (57/57) |
| All raw files tracked | PASS (57/57) |
| Inbox empty | PASS (0 pending) |
| Manifest files present | PASS (10 files) |

## File Types Breakdown

| Type | Count |
|------|-------|
| .md (Markdown) | 23 |
| .xlsx (Excel) | 15 |
| .json (JSON) | 9 |
| .gpx (GPS tracks) | 5 |
| .csv (CSV data) | 2 |
| .pdf (PDF) | 1 |
| .xml (XML) | 1 |
| .html (HTML) | 1 |

## Directory Distribution

| Directory | Count |
|-----------|-------|
| raw/ (root) | 37 |
| raw/FINANCE/ | 15 |
| raw/FINANCE/rate_cards/ | 5 |

## Manifest Registry Counts

| Registry | Entries |
|----------|---------|
| category-registry.yml | 29 categories |
| tag-registry.yml | 35 tags |
| evidence-registry.yml | 14 evidence items (C1-C9) |
| conflict-log.md | 3 open conflicts |
| recommendation-log.md | 7 entries (2 done, 5 pending) |

## Open Conflicts

| ID | Subject | Status |
|----|---------|--------|
| CONF-001 | Stefan Loose year/ISBN | open — blocked on physical book check |
| CONF-002 | Madakaripura height | open — under reconciliation |
| CONF-003 | Second NIB 0220001393513 | open — blocked on OSS portal |

## Pending Recommendations

| ID | Type | Status |
|----|------|--------|
| REC-003 | new_page (permit-requirements cross-refs) | pending |
| REC-004 | new_page (rate-cards source link) | pending |
| REC-005 | update (batch-log 37 raw files) | pending |
| REC-006 | new_tag (ferry-crossing) | pending |
| REC-007 | new_tag (taman-safari) | pending |

---

*Next audit: run after next ingest batch or weekly health check.*
