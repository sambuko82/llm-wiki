"""Shared DB connection helper for backoffice extraction scripts."""
import pymysql
from pathlib import Path

ENV_PATH = Path("f:/BACK OFFICE/new-backoffice/.env")

def _load_env():
    cfg = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip().strip('"').strip("'")
    return cfg

def connect():
    cfg = _load_env()
    return pymysql.connect(
        host=cfg["DB_HOST"],
        port=int(cfg.get("DB_PORT", 3306)),
        user=cfg["DB_USERNAME"],
        password=cfg["DB_PASSWORD"],
        database=cfg["DB_DATABASE"],
        connect_timeout=20,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

if __name__ == "__main__":
    c = connect()
    cur = c.cursor()
    cur.execute("SELECT DATABASE() AS db, VERSION() AS ver")
    print(cur.fetchone())
    c.close()
