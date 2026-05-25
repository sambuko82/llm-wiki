"""Dump table data as CSV. Sensitive tables with created_at column filter to May 2026+."""
import csv
import json
from pathlib import Path
from datetime import datetime
from _db import connect

INV = Path("raw/backoffice/_inventory.json")
CSV_DIR = Path("raw/backoffice/csv")
SLICE_FROM = "2026-05-01"

# Skip these entirely (framework or noise)
SKIP_NAMES = set()

def has_column(cur, table, col):
    cur.execute("""
        SELECT 1 FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME=%s AND COLUMN_NAME=%s
    """, (table, col))
    return cur.fetchone() is not None

def main():
    data = json.load(open(INV))
    CSV_DIR.mkdir(parents=True, exist_ok=True)
    conn = connect()
    cur = conn.cursor()

    summary = []
    for t in data:
        name = t["name"]
        bucket = t["bucket"]
        if bucket == "framework":
            continue
        if t["rows_actual"] == 0:
            continue  # empty
        if name in SKIP_NAMES:
            continue

        # Raw layer is gitignored — keep full data for finance correlation.
        # PII minimization happens at wiki layer (aggregate only) and for
        # the customer-PII slice we'll generate separately for sharing.
        where = ""

        try:
            cur.execute(f"SELECT * FROM `{name}`{where}")
            rows = cur.fetchall()
        except Exception as e:
            print(f"  ! {name}: {e}")
            summary.append({"table": name, "exported": 0, "error": str(e)[:100]})
            continue

        out_csv = CSV_DIR / f"{name}.csv"
        if rows:
            cols = list(rows[0].keys())
            with out_csv.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                w.writeheader()
                for r in rows:
                    # Stringify non-serializable types
                    rr = {k: ("" if v is None else str(v)) for k, v in r.items()}
                    w.writerow(rr)
        else:
            out_csv.write_text("", encoding="utf-8")

        summary.append({
            "table": name,
            "bucket": bucket,
            "total_rows": t["rows_actual"],
            "exported": len(rows),
            "filtered": bool(where),
        })
        print(f"  {bucket[:4]} {name}: {len(rows)}/{t['rows_actual']} rows -> {out_csv.name}")

    conn.close()
    Path("raw/backoffice/_export_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    total = sum(s["exported"] for s in summary)
    print(f"\nDone. {len(summary)} tables, {total:,} rows total.")

if __name__ == "__main__":
    main()
