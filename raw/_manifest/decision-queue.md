# Decision Queue

*Items requiring human decision before processing. Intake gate adds items here when `human_decision_required = true`. Review weekly.*

---

| ID | Date | Type | Description | Impact | Source | Status | Resolution |
|----|------|------|-------------|--------|--------|--------|------------|
| DQ-001 | 2026-05-11 | conflict | Stefan Loose year/ISBN — 2016 vs 2018 dispute. Dossier (AI, weight 8) uses 2018. | press-coverage accuracy | CONF-001 | pending | Blocked — requires physical book check by Sam |
| DQ-002 | 2026-05-11 | conflict | Madakaripura height — ~100m (SSOT v6, weight 5) vs ~200m (indonesia.travel, weight 4) | destination page accuracy | CONF-002 | pending | Under reconciliation — both values cited with attribution |
| DQ-003 | 2026-05-11 | conflict | Historical NIB 0220001393513 — legacy OSS record, not canonical active license | credential accuracy | CONF-003 | pending | Blocked — requires OSS portal verification |
| DQ-004 | 2026-05-25 | safety | Ijen safety incidents URL (/travel-guide/ijen-safety-incidents) — content includes named fatalities | sensitive public content | REC-009 | pending | Human approval required before publishing |
| DQ-005 | 2026-05-25 | safety | Buleleng Hiace Fatality — referenced in ijen-safety-protocol but NOT in Tourist Accidents Excel | incident data accuracy | REC-010 | pending | Sam to confirm/deny before adding to incident registry |

---

## Types

| Type | Description |
|------|-------------|
| conflict | Data conflict between sources (mirrored from conflict-log.md) |
| new_category | Proposed category requiring human approval |
| new_url | Proposed public URL with sensitivity gate |
| credential | Credential verification requiring external check |
| safety | Safety-sensitive content requiring editorial review |
| pricing | Price/cost data requiring owner verification |
| entity | New entity requiring classification approval |
| claim | Claim modification or new claim proposal |

## Status Values

| Status | Meaning |
|--------|---------|
| pending | Awaiting human review |
| in_review | Under active consideration |
| approved | Decision made — execute |
| rejected | Decision made — do not execute |
| deferred | Postponed to future sprint |

*Format: Add new rows. Never delete resolved items — mark status as approved/rejected with resolution date and outcome.*
