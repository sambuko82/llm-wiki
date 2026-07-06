---
name: xlsx-extraction-dry-run
enabled: true
event: bash
pattern: python.*\.xlsx|openpyxl.*glob
action: warn
---

⚠️ **Excel extraction detected.**

Before bulk-extracting data from multiple .xlsx files:

1. **Read 1 sample file first** — understand column structure, header positions, data layout
2. **Check for format variations** — not all spreadsheets have the same layout (learned from JVTO finance: 2 of 15 files had completely different formats)
3. **Validate extracted totals** — cross-check against known values (e.g., selling prices from DB)
4. **Handle missing data gracefully** — mark as "—" not zero; document gaps in Data Quality Notes

Prevents the 4-iteration extraction cycle that happened with raw/FINANCE/*.xlsx.
