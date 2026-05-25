"""Generate raw/backoffice/_manifest.md from _inventory.json."""
import json
from pathlib import Path
from datetime import date

INV = Path("raw/backoffice/_inventory.json")
OUT = Path("raw/backoffice/_manifest.md")

# Domain assignment by name pattern (extraction targeting)
def domain_of(name):
    n = name.lower()
    if any(k in n for k in ["wa_", "whatsapp"]): return "whatsapp"
    if any(k in n for k in ["invoice", "payment", "debt", "expense", "account", "twt_"]): return "finance"
    if any(k in n for k in ["book", "booking"]): return "bookings"
    if any(k in n for k in ["guide", "driver", "crew", "user", "agent"]): return "people"
    if any(k in n for k in ["car", "jeep", "vehicle"]): return "vehicles"
    if any(k in n for k in ["hotel", "room", "accommodat"]): return "hotels"
    if any(k in n for k in ["activity", "destination", "package", "tour", "itinerary", "itineraries"]): return "products"
    if any(k in n for k in ["vendor", "supplier"]): return "vendors"
    if any(k in n for k in ["review", "rating"]): return "reviews"
    if any(k in n for k in ["media", "image", "file", "attachment", "document", "banner"]): return "media"
    return "misc"

def main():
    data = json.load(open(INV))
    by_bucket = {"business": [], "sensitive": [], "framework": []}
    for t in data:
        t["domain"] = domain_of(t["name"])
        by_bucket[t["bucket"]].append(t)

    today = date.today().isoformat()
    out = []
    out.append("---")
    out.append("type: source")
    out.append("title: Backoffice MySQL — Inventory & Extraction Manifest")
    out.append(f"last_updated: {today}")
    out.append("sources: [backoffice-mysql]")
    out.append("---")
    out.append("")
    out.append("# Backoffice MySQL Inventory")
    out.append("")
    out.append(f"- **DB:** `u1805424_jvto_clone` @ MariaDB 10.11 (Hostinger)")
    out.append(f"- **Snapshot:** {today}")
    out.append(f"- **Total tables:** {len(data)}")
    out.append(f"- **Total rows:** {sum(t['rows_actual'] for t in data if t['rows_actual']>0):,}")
    out.append("")
    out.append("## Bucket summary")
    out.append("")
    out.append("| Bucket | Count | Treatment |")
    out.append("|---|---|---|")
    out.append(f"| business | {len(by_bucket['business'])} | Full extract → dumps/ + csv/ + wiki summary |")
    out.append(f"| sensitive | {len(by_bucket['sensitive'])} | Full extract local; wiki = aggregate only; customer slice May 2026+ |")
    out.append(f"| framework | {len(by_bucket['framework'])} | Skip (Laravel internals) |")
    out.append("")

    # Domain breakdown
    out.append("## Domain breakdown (business + sensitive)")
    out.append("")
    by_domain = {}
    for t in data:
        if t["bucket"] == "framework": continue
        by_domain.setdefault(t["domain"], []).append(t)
    out.append("| Domain | Tables | Rows |")
    out.append("|---|---|---|")
    for d in sorted(by_domain.keys()):
        tbls = by_domain[d]
        rows = sum(x["rows_actual"] for x in tbls if x["rows_actual"]>0)
        out.append(f"| {d} | {len(tbls)} | {rows:,} |")
    out.append("")

    # Top 30 tables
    out.append("## Top tables by row count")
    out.append("")
    out.append("| Table | Rows | Size KB | Bucket | Domain |")
    out.append("|---|---:|---:|---|---|")
    top = sorted(data, key=lambda x: x["rows_actual"], reverse=True)[:40]
    for t in top:
        if t["rows_actual"] <= 0: continue
        out.append(f"| `{t['name']}` | {t['rows_actual']:,} | {t['data_kb']:.0f} | {t['bucket']} | {t['domain']} |")
    out.append("")

    # Full table per bucket
    for bucket in ["business", "sensitive", "framework"]:
        out.append(f"## All {bucket} tables")
        out.append("")
        out.append("| Table | Rows | Domain |")
        out.append("|---|---:|---|")
        for t in sorted(by_bucket[bucket], key=lambda x: x["name"]):
            out.append(f"| `{t['name']}` | {t['rows_actual']:,} | {t.get('domain','-')} |")
        out.append("")

    out.append("## Extraction plan")
    out.append("")
    out.append("- **Schema dump:** all 210 tables → `raw/backoffice/schema/full-schema.sql` (commit-safe)")
    out.append("- **Data dump:** business + sensitive (non-framework) → `raw/backoffice/dumps/<table>.sql` (gitignored)")
    out.append("- **CSV export:** business + sensitive → `raw/backoffice/csv/<table>.csv` (gitignored)")
    out.append("- **Customer slice:** sensitive tables with `created_at` column → filter `WHERE created_at >= '2026-05-01'` for wiki aggregation only")
    out.append("- **Wiki layer:** aggregate stats only; no email/phone/full name leak; see PII guard in extraction script")
    out.append("")

    Path(OUT).write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT} ({len(out)} lines)")

if __name__ == "__main__":
    main()
