"""Dump full schema (no data) for all tables → raw/backoffice/schema/full-schema.sql."""
import json
from pathlib import Path
from datetime import datetime
from _db import connect

INV = Path("raw/backoffice/_inventory.json")
OUT = Path("raw/backoffice/schema/full-schema.sql")

def main():
    data = json.load(open(INV))
    conn = connect()
    cur = conn.cursor()
    lines = [
        f"-- Backoffice schema dump",
        f"-- Source: u1805424_jvto_clone @ MariaDB 10.11 (Hostinger)",
        f"-- Generated: {datetime.utcnow().isoformat()}Z",
        f"-- Tables: {len(data)}",
        f"-- No data — schema only — safe to commit",
        f"",
        f"SET FOREIGN_KEY_CHECKS=0;",
        f"",
    ]
    for t in sorted(data, key=lambda x: x["name"]):
        name = t["name"]
        try:
            cur.execute(f"SHOW CREATE TABLE `{name}`")
            row = cur.fetchone()
            ddl = row.get("Create Table") or row.get("Create View") or ""
            lines.append(f"-- ---- {name} ({t['rows_actual']} rows, {t['bucket']}) ----")
            lines.append(f"DROP TABLE IF EXISTS `{name}`;")
            lines.append(ddl + ";")
            lines.append("")
        except Exception as e:
            lines.append(f"-- ERROR dumping {name}: {e}")
            lines.append("")
    lines.append("SET FOREIGN_KEY_CHECKS=1;")
    conn.close()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({sum(1 for l in lines if l.startswith('CREATE'))} CREATE statements, {len(lines)} lines)")

if __name__ == "__main__":
    main()
