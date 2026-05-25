"""Phase A: inventory all tables with row counts, size, classification."""
import json
import re
import sys
from pathlib import Path
from _db import connect

OUT_JSON = Path("raw/backoffice/_inventory.json")

FRAMEWORK_PATTERNS = [
    r"^migrations$", r"^password_reset", r"^sessions$", r"^cache",
    r"^jobs$", r"^job_batches$", r"^failed_jobs$",
    r"^personal_access_tokens$", r"^telescope_",
    r"^notifications$", r"^oauth_", r"^websockets_",
]

SENSITIVE_PATTERNS = [
    r"^users$", r"^customers?$", r"^bookings?$", r"^booking_",
    r"^book_", r"^invoice", r"^twt_invoice", r"^payment", r"^debt_",
    r"^identity_card", r"^addresses?$", r"^contacts?$",
]

def classify(name):
    for p in FRAMEWORK_PATTERNS:
        if re.search(p, name, re.I):
            return "framework"
    for p in SENSITIVE_PATTERNS:
        if re.search(p, name, re.I):
            return "sensitive"
    return "business"

def main():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT TABLE_NAME, TABLE_ROWS, DATA_LENGTH, INDEX_LENGTH, TABLE_COMMENT
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = DATABASE()
        ORDER BY TABLE_NAME
    """)
    tables = []
    for row in cur.fetchall():
        name = row["TABLE_NAME"]
        # Real row count (TABLE_ROWS is approx for InnoDB)
        try:
            cur.execute(f"SELECT COUNT(*) AS c FROM `{name}`")
            real_count = cur.fetchone()["c"]
        except Exception as e:
            real_count = -1
        tables.append({
            "name": name,
            "rows_approx": row["TABLE_ROWS"],
            "rows_actual": real_count,
            "data_kb": round((row["DATA_LENGTH"] or 0) / 1024, 1),
            "index_kb": round((row["INDEX_LENGTH"] or 0) / 1024, 1),
            "comment": row["TABLE_COMMENT"] or "",
            "bucket": classify(name),
        })
    conn.close()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(tables, indent=2), encoding="utf-8")
    print(f"Wrote {len(tables)} table records to {OUT_JSON}")
    # Summary
    from collections import Counter
    c = Counter(t["bucket"] for t in tables)
    print("Buckets:", dict(c))
    total_rows = sum(t["rows_actual"] for t in tables if t["rows_actual"] > 0)
    print(f"Total rows: {total_rows:,}")

if __name__ == "__main__":
    main()
