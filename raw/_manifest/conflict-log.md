# Conflict Log

*Tracked data conflicts between sources. Do NOT overwrite existing data automatically.*

---

| ID | Detected | Claim A | Source A | Claim B | Source B | Status | Affects Claims | Evidence Weight | Resolution |
|----|----------|---------|---------|---------|---------|--------|----------------|-----------------|------------|
| CONF-001 | 2026-05-11 | Stefan Loose 2016, ISBN 9783770167654 | wiki/sources/why-jvto-trust-architecture | Stefan Loose 2018, ISBN 978-3-7701-7881-0 | raw audit documents + JVTO Verification Dossier p.10 (shows "Year: 2018") | resolved 2026-06-25 | C9 | A: weight 2 (JVTO internal) vs B: weight 7+8 (unverified note + AI dossier) | **Resolved (owner decision 2026-06-25).** Canonical bibliographic reference = Amazon product listing https://www.amazon.de/-/en/Stefan-Loose-Reisef%C3%BChrer-Indonesien-Reiseatlas/dp/3770167651 → ISBN-10 3770167651, ISBN-13 9783770167654 (valid normalization), title "Stefan Loose Reiseführer Indonesien: mit Reiseatlas", p. 287. The 2018 / 978-3-7701-7881-0 / DuMont Reiseverlag values came from internal strategy docs only and are dropped unless a physical imprint/copyright page supports them. Year/publisher/edition not asserted. See DEC-001 (updated) + okf/references/stefan-loose-indonesien-guidebook. |
| CONF-002 | 2026-05-11 | Madakaripura main curtain ~100m | wiki/sources/ssot-v6 (§9_4) | Madakaripura total height ~200m | indonesia.travel | open | C5 | A: weight 5 (structured dataset) vs B: weight 4 (reputable source) | Under reconciliation — both values cited with attribution |
| CONF-003 | 2026-05-11 | Active NIB 1102230032918 | wiki/credentials/legal-licenses | Historical NIB 0220001393513 | audit documents | open | C8 | A: weight 1 (official authority) vs B: weight 7 (unverified) | Blocked — requires OSS portal verification |

---

*Format: Add new rows. Never delete resolved conflicts — mark status as "resolved" with resolution date and outcome.*
