"""Peek columns + sample row for a list of tables."""
import sys
from _db import connect

TABLES = sys.argv[1:] if len(sys.argv) > 1 else [
    "bookings", "booking_payments", "invoice_histories",
    "guide_drivers", "cars", "vendors", "hotels",
    "tw_calculations", "tw_calculation_details",
    "wa_chats", "wa_chat_summaries",
    "package_prices",
]

def main():
    conn = connect()
    cur = conn.cursor()
    for t in TABLES:
        try:
            cur.execute(f"""
                SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_COMMENT
                FROM information_schema.COLUMNS
                WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME=%s
                ORDER BY ORDINAL_POSITION
            """, (t,))
            cols = cur.fetchall()
            print(f"\n## {t}  ({len(cols)} columns)")
            for c in cols:
                k = c["COLUMN_KEY"] or "  "
                cmt = f"  -- {c['COLUMN_COMMENT']}" if c['COLUMN_COMMENT'] else ""
                print(f"  {k:3} {c['COLUMN_NAME']:35} {c['DATA_TYPE']:12} {c['IS_NULLABLE']}{cmt}")
        except Exception as e:
            print(f"\n## {t}  ERROR: {e}")
    conn.close()

if __name__ == "__main__":
    main()
