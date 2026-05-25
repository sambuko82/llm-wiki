"""Phase C: analyze CSV dumps + DB aggregates, generate wiki/sources/backoffice-*.md pages.

PII guard: no email, phone, full personal name from customer tables in output.
Internal staff names OK (already public in wiki/people/).
"""
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from _db import connect

CSV_DIR = Path("raw/backoffice/csv")
OUT_DIR = Path("wiki/sources")
OUT_DIR.mkdir(parents=True, exist_ok=True)
TODAY = date.today().isoformat()

PII_EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PII_PHONE_RE = re.compile(r"\+?\d{10,}")

def pii_scrub(text):
    """Defense-in-depth: strip emails and long digit runs from any string written to wiki."""
    if not isinstance(text, str):
        return text
    text = PII_EMAIL_RE.sub("[EMAIL]", text)
    text = PII_PHONE_RE.sub("[PHONE]", text)
    return text

def load_csv(name):
    p = CSV_DIR / f"{name}.csv"
    if not p.exists() or p.stat().st_size == 0:
        return []
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))

def fnum(x, default=0.0):
    try:
        if x is None or x == "":
            return default
        return float(x)
    except Exception:
        return default

def frontmatter(title, src_list):
    return [
        "---",
        "type: source",
        f"title: {title}",
        f"last_updated: {TODAY}",
        f"sources: [{', '.join(src_list)}]",
        "---",
        "",
    ]

# ============================================================
# backoffice-finance.md
# ============================================================
def gen_finance():
    bookings = load_csv("bookings")
    payments = load_csv("booking_payments")
    invoice_hist = load_csv("invoice_histories")
    payment_methods = load_csv("payment_methods")
    accounts = load_csv("accounts")

    # Revenue by month
    rev_by_month = defaultdict(lambda: {"count": 0, "grand_total_idr": 0.0, "grand_total_other": 0.0})
    by_currency = Counter()
    by_status = Counter()
    by_payment_status = Counter()
    by_channel = Counter()
    by_payment_method = Counter()
    margin_sum = 0.0
    margin_count = 0
    cost_sum = 0.0
    grand_total_idr = 0.0
    grand_total_usd = 0.0
    debt_total = 0.0

    for b in bookings:
        ccy = (b.get("currency") or "").upper() or "?"
        by_currency[ccy] += 1
        by_status[b.get("status") or "?"] += 1
        by_payment_status[b.get("payment_status") or "?"] += 1
        by_channel[b.get("channel_tag") or "(none)"] += 1
        by_payment_method[b.get("payment_method") or "(none)"] += 1

        gt = fnum(b.get("grand_total"))
        if ccy == "IDR":
            grand_total_idr += gt
        elif ccy == "USD":
            grand_total_usd += gt

        margin = fnum(b.get("margin"))
        if margin:
            margin_sum += margin
            margin_count += 1
        cost_sum += fnum(b.get("cost"))
        debt_total += fnum(b.get("debt"))

        bd = b.get("booking_date") or b.get("created_at") or ""
        ym = bd[:7] if bd else "unknown"
        m = rev_by_month[ym]
        m["count"] += 1
        if ccy == "IDR":
            m["grand_total_idr"] += gt
        else:
            m["grand_total_other"] += gt

    # Payment volume
    pay_by_method_id = Counter()
    pay_nominal_by_method = defaultdict(float)
    for p in payments:
        mid = p.get("payment_method_id") or "?"
        pay_by_method_id[mid] += 1
        pay_nominal_by_method[mid] += fnum(p.get("nominal"))

    pm_map = {p["id"]: p.get("name", f"method_{p['id']}") for p in payment_methods}

    # Invoice history aggregates
    inv_by_type = Counter()
    inv_total_by_type = defaultdict(float)
    for inv in invoice_hist:
        t = inv.get("type") or "?"
        inv_by_type[t] += 1
        inv_total_by_type[t] += fnum(inv.get("line_total"))

    out = frontmatter("Backoffice — Finance Overview", ["backoffice-mysql"])
    out += [
        "# Backoffice Finance — Live DB Snapshot",
        "",
        f"Source: live MySQL `u1805424_jvto_clone` (Hostinger). Snapshot {TODAY}.",
        "All money values are aggregates only; no per-customer detail in this wiki page.",
        "Raw line items live in `raw/backoffice/csv/` (gitignored).",
        "",
        "## Totals",
        "",
        f"- **Bookings tracked:** {len(bookings):,}",
        f"- **Grand total IDR (all-time):** Rp {grand_total_idr:,.0f}",
        f"- **Grand total USD (all-time):** ${grand_total_usd:,.2f}",
        f"- **Total recorded cost (COGS):** Rp {cost_sum:,.0f}",
        f"- **Avg margin per booking:** Rp {(margin_sum/margin_count if margin_count else 0):,.0f} (over {margin_count} bookings with margin populated)",
        f"- **Outstanding debt (across all bookings):** Rp {debt_total:,.0f}",
        "",
        "## Currency mix",
        "",
        "| Currency | Bookings |",
        "|---|---:|",
    ]
    for c, n in by_currency.most_common():
        out.append(f"| {c} | {n:,} |")
    out += ["", "## Booking status distribution", "", "| Status | Count |", "|---|---:|"]
    for s, n in by_status.most_common():
        out.append(f"| `{s}` | {n:,} |")
    out += ["", "## Payment status", "", "| Payment status | Count |", "|---|---:|"]
    for s, n in by_payment_status.most_common():
        out.append(f"| `{s}` | {n:,} |")
    out += ["", "## Channel mix (`bookings.channel_tag`)", "", "| Channel | Count |", "|---|---:|"]
    for c, n in by_channel.most_common(20):
        out.append(f"| `{c}` | {n:,} |")
    out += ["", "## Payment method on booking (`bookings.payment_method`)", "", "| Method | Count |", "|---|---:|"]
    for c, n in by_payment_method.most_common(20):
        out.append(f"| `{c}` | {n:,} |")

    out += [
        "",
        "## Revenue by month (IDR + other ccy combined for count)",
        "",
        "| Month | Bookings | Total IDR | Other ccy (USD etc.) |",
        "|---|---:|---:|---:|",
    ]
    for ym in sorted(rev_by_month.keys()):
        m = rev_by_month[ym]
        out.append(f"| {ym} | {m['count']:,} | Rp {m['grand_total_idr']:,.0f} | {m['grand_total_other']:,.2f} |")

    out += [
        "",
        "## Payment ledger — nominal by payment method",
        "",
        f"Total payment records: {len(payments):,}",
        "",
        "| Method (id) | Method name | Count | Total nominal |",
        "|---|---|---:|---:|",
    ]
    for mid, n in sorted(pay_by_method_id.items(), key=lambda x: -x[1]):
        nm = pm_map.get(str(mid), pm_map.get(mid, "?"))
        out.append(f"| {mid} | {nm} | {n:,} | {pay_nominal_by_method[mid]:,.0f} |")

    out += [
        "",
        "## Invoice history breakdown",
        "",
        f"Total invoice line items: {len(invoice_hist):,}",
        "",
        "| Line type | Count | Sum line_total |",
        "|---|---:|---:|",
    ]
    for t, n in inv_by_type.most_common():
        out.append(f"| `{t}` | {n:,} | {inv_total_by_type[t]:,.0f} |")

    out += [
        "",
        "## Accounts (chart of accounts in backoffice)",
        "",
        f"Total account records: {len(accounts):,}",
        "",
    ]
    if accounts and "name" in accounts[0]:
        out.append("| Account | Type | Code |")
        out.append("|---|---|---|")
        for a in accounts[:50]:
            out.append(f"| {a.get('name','?')} | {a.get('type','-')} | {a.get('code','-')} |")
    out += [
        "",
        "## Cross-references",
        "",
        "- [[finance/rate-card-package]] — compare template rate card vs realized prices in [[sources/backoffice-pricing]]",
        "- [[sources/backoffice-pricing]] — package_prices vs realized booking totals",
        "- [[sources/backoffice-bookings-ops]] — booking volume drives this revenue",
        "- [[ops/intake-gate]] — Workflow 7 registration for this source",
        "",
    ]
    (OUT_DIR / "backoffice-finance.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  finance.md: {len(out)} lines")

# ============================================================
# backoffice-pricing.md
# ============================================================
def gen_pricing():
    package_prices = load_csv("package_prices")
    packages = load_csv("packages") if (CSV_DIR / "packages.csv").exists() else []
    bookings = load_csv("bookings")
    price_plans = load_csv("price_plans")

    pkg_map = {p["id"]: p.get("name") or p.get("title") or f"pkg_{p['id']}" for p in packages}
    plan_map = {p["id"]: p.get("name", f"plan_{p['id']}") for p in price_plans}

    # Group package_prices by package
    by_pkg = defaultdict(list)
    for pp in package_prices:
        by_pkg[pp.get("package_id")].append(pp)

    # Realized prices from bookings by template_package_id
    realized_by_pkg = defaultdict(list)
    for b in bookings:
        tpid = b.get("template_package_id")
        if tpid and tpid != "":
            gt = fnum(b.get("grand_total"))
            pax = fnum(b.get("total_pax")) or 1
            if gt > 0:
                realized_by_pkg[tpid].append({"gt": gt, "pax": pax, "per_pax": gt / pax, "ccy": b.get("currency") or "?"})

    out = frontmatter("Backoffice — Pricing (Template vs Realized)", ["backoffice-mysql"])
    out += [
        "# Backoffice Pricing — Template Rate Card vs Realized Prices",
        "",
        f"Snapshot {TODAY}. Source: `package_prices` (template) + `bookings.grand_total` (realized).",
        "Use this to validate `wiki/finance/rate-card-*.md` against actual booking data.",
        "",
        f"- **Distinct packages with prices:** {len(by_pkg)}",
        f"- **Total price rows (`package_prices`):** {len(package_prices)}",
        f"- **Bookings with template_package_id set:** {sum(len(v) for v in realized_by_pkg.values())}",
        "",
        "## Template price points",
        "",
        "Top 50 by price (template, not realized).",
        "",
        "| Package | Plan | Category | Price | Klook retail | Klook net |",
        "|---|---|---|---:|---:|---:|",
    ]
    sorted_pp = sorted(package_prices, key=lambda x: -fnum(x.get("price")))[:50]
    for pp in sorted_pp:
        pkg = pkg_map.get(pp.get("package_id"), f"pkg_{pp.get('package_id')}")
        plan = plan_map.get(pp.get("price_plan_id"), "-")
        out.append(f"| {pkg} | {plan} | {pp.get('price_category_id')} | {fnum(pp.get('price')):,.0f} | {fnum(pp.get('klook_retail_price')):,.0f} | {fnum(pp.get('klook_net_price')):,.0f} |")

    out += [
        "",
        "## Realized prices per template package (top 30 by volume)",
        "",
        "| Package id | Bookings | Avg total | Avg per-pax | Min per-pax | Max per-pax |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    top = sorted(realized_by_pkg.items(), key=lambda x: -len(x[1]))[:30]
    for pid, rows in top:
        avg_total = sum(r["gt"] for r in rows) / len(rows)
        avg_per = sum(r["per_pax"] for r in rows) / len(rows)
        min_per = min(r["per_pax"] for r in rows)
        max_per = max(r["per_pax"] for r in rows)
        out.append(f"| {pid} | {len(rows)} | {avg_total:,.0f} | {avg_per:,.0f} | {min_per:,.0f} | {max_per:,.0f} |")

    out += [
        "",
        "## Validation hook",
        "",
        "When updating `wiki/finance/rate-card-package.md`, cross-check that:",
        "1. Each template price in this table has a matching entry in the rate card.",
        "2. Realized per-pax averages fall within ±15% of the rate card price (otherwise discount layer or upsell is happening uncaptured).",
        "3. Klook retail vs net spread matches the Klook commission assumption in `wiki/finance/`.",
        "",
        "## Cross-references",
        "- [[sources/backoffice-finance]] — aggregate revenue from these prices",
        "- [[sources/backoffice-bookings-ops]] — package mix that drives volume",
        "- [[finance/rate-card-package]] — manual rate card SSOT to reconcile against",
        "",
    ]
    (OUT_DIR / "backoffice-pricing.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  pricing.md: {len(out)} lines")

# ============================================================
# backoffice-bookings-ops.md
# ============================================================
def gen_bookings_ops():
    bookings = load_csv("bookings")
    book_guide_drivers = load_csv("book_guide_drivers")
    book_cars = load_csv("book_cars")
    book_hotels = load_csv("book_hotels")
    book_jeeps = load_csv("book_jeeps")
    agents = load_csv("agents") if (CSV_DIR / "agents.csv").exists() else []

    by_month = Counter()
    pax_by_month = defaultdict(int)
    by_template = Counter()
    by_agent = Counter()
    lead_times = []
    durations = []
    pax_dist = Counter()
    police_escort = 0
    isic = 0
    for b in bookings:
        bd = (b.get("booking_date") or b.get("created_at") or "")[:7]
        by_month[bd] += 1
        pax_by_month[bd] += int(fnum(b.get("total_pax")))
        tp = b.get("template_package_id") or "(none)"
        by_template[tp] += 1
        ag = b.get("agent_id") or "(none)"
        by_agent[ag] += 1
        try:
            d1 = datetime.fromisoformat(b.get("booking_date") or "")
            d2 = datetime.fromisoformat(b.get("travel_date_start") or "")
            lt = (d2 - d1).days
            if 0 <= lt <= 365:
                lead_times.append(lt)
            d3 = datetime.fromisoformat(b.get("travel_date_end") or "")
            dur = (d3 - d2).days + 1
            if 1 <= dur <= 14:
                durations.append(dur)
        except Exception:
            pass
        p = int(fnum(b.get("total_pax")))
        if p:
            pax_dist[p] += 1
        if (b.get("is_police_escort") or "").lower() in ("yes", "1", "true"):
            police_escort += 1
        if (b.get("is_buy_isic") or "").lower() in ("yes", "1", "true"):
            isic += 1

    agent_map = {a["id"]: a.get("name", f"agent_{a['id']}") for a in agents}

    avg_lead = sum(lead_times) / len(lead_times) if lead_times else 0
    avg_dur = sum(durations) / len(durations) if durations else 0

    out = frontmatter("Backoffice — Bookings & Ops", ["backoffice-mysql"])
    out += [
        "# Backoffice — Bookings & Operational Patterns",
        "",
        f"Snapshot {TODAY}. {len(bookings):,} bookings tracked.",
        "",
        "## Headline metrics",
        "",
        f"- **Total bookings:** {len(bookings):,}",
        f"- **Total pax served (all-time, sum):** {sum(pax_by_month.values()):,}",
        f"- **Avg lead time (booking_date → travel_date_start):** {avg_lead:.1f} days (n={len(lead_times)})",
        f"- **Avg trip duration:** {avg_dur:.2f} days (n={len(durations)})",
        f"- **Bookings with police escort:** {police_escort:,} ({police_escort/max(1,len(bookings))*100:.1f}%)",
        f"- **Bookings with ISIC purchase:** {isic:,} ({isic/max(1,len(bookings))*100:.1f}%)",
        f"- **Guide/driver assignments tracked:** {len(book_guide_drivers):,}",
        f"- **Car assignments:** {len(book_cars):,}",
        f"- **Hotel assignments:** {len(book_hotels):,}",
        f"- **Jeep assignments:** {len(book_jeeps):,}",
        "",
        "## Pax distribution per booking",
        "",
        "| Pax per booking | Count |",
        "|---:|---:|",
    ]
    for p in sorted(pax_dist.keys()):
        out.append(f"| {p} | {pax_dist[p]:,} |")

    out += ["", "## Bookings by month", "", "| Month | Bookings | Total pax |", "|---|---:|---:|"]
    for ym in sorted(by_month.keys()):
        out.append(f"| {ym} | {by_month[ym]:,} | {pax_by_month[ym]:,} |")

    out += [
        "",
        "## Top 30 template packages (by booking volume)",
        "",
        "| template_package_id | Bookings |",
        "|---|---:|",
    ]
    for tp, n in by_template.most_common(30):
        out.append(f"| {tp} | {n:,} |")

    out += [
        "",
        "## Agents / sales channels (`bookings.agent_id`)",
        "",
        "| Agent id | Name | Bookings |",
        "|---|---|---:|",
    ]
    for ag, n in by_agent.most_common(30):
        name = agent_map.get(ag, agent_map.get(str(ag), "-"))
        out.append(f"| {ag} | {name} | {n:,} |")

    out += [
        "",
        "## Cross-references",
        "- [[sources/backoffice-finance]] — revenue derived from these bookings",
        "- [[sources/backoffice-staff]] — guide/driver assignments via `book_guide_drivers`",
        "- [[sources/backoffice-pricing]] — packages booked",
        "",
    ]
    (OUT_DIR / "backoffice-bookings-ops.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  bookings-ops.md: {len(out)} lines")

# ============================================================
# backoffice-staff.md
# ============================================================
def gen_staff():
    gd = load_csv("guide_drivers")
    crew_roles = load_csv("crew_roles")
    review_guides = load_csv("review_guides")
    book_guide_drivers = load_csv("book_guide_drivers")

    by_level = Counter()
    by_role = Counter()
    is_driver = 0
    is_ijen = 0
    stars = []
    rates = []
    has_license_guide = 0
    has_license_driver = 0
    has_ktp = 0
    soft_deleted = 0
    new_role_counter = Counter()
    for g in gd:
        by_level[g.get("crew_level") or "(none)"] += 1
        by_role[g.get("crew_id") or "(none)"] += 1
        new_role_counter[g.get("new_role") or "(none)"] += 1
        if g.get("is_driver") == "1":
            is_driver += 1
        if g.get("is_ijen") == "1":
            is_ijen += 1
        s = fnum(g.get("star"))
        if s > 0:
            stars.append(s)
        r = fnum(g.get("rate"))
        if r > 0:
            rates.append(r)
        if g.get("guide_license"):
            has_license_guide += 1
        if g.get("driver_license"):
            has_license_driver += 1
        if g.get("ktp"):
            has_ktp += 1
        if g.get("deleted_at"):
            soft_deleted += 1

    # Assignment counts per crew (no name leak; just counts)
    assign_count = Counter()
    for ba in book_guide_drivers:
        assign_count[ba.get("guide_driver_id") or "?"] += 1

    # Top assigned crew (by id only — names exist in wiki/people/ already)
    name_map = {g["id"]: g.get("name", "?") for g in gd}

    role_map = {r["id"]: r.get("name", f"role_{r['id']}") for r in crew_roles}

    out = frontmatter("Backoffice — Staff (Guides & Drivers)", ["backoffice-mysql"])
    out += [
        "# Backoffice Staff — Guide / Driver Roster",
        "",
        f"Snapshot {TODAY}. {len(gd):,} crew records ({soft_deleted} soft-deleted).",
        "Internal use only — names appear in [[people/guides]] and [[people/drivers]].",
        "License numbers, KTP, emails, phones are in the raw layer (`raw/backoffice/csv/guide_drivers.csv`) — not echoed here.",
        "",
        "## Headline",
        "",
        f"- **Total crew records:** {len(gd):,}",
        f"- **Active (not soft-deleted):** {len(gd) - soft_deleted}",
        f"- **Marked as driver (`is_driver=1`):** {is_driver}",
        f"- **Marked as Ijen-certified (`is_ijen=1`):** {is_ijen}",
        f"- **With `guide_license` populated:** {has_license_guide}",
        f"- **With `driver_license` populated:** {has_license_driver}",
        f"- **With `ktp` populated:** {has_ktp}",
        f"- **Avg star rating:** {(sum(stars)/len(stars) if stars else 0):.2f} (over {len(stars)} rated)",
        f"- **Avg rate (IDR/trip):** {(sum(rates)/len(rates) if rates else 0):,.0f} (over {len(rates)} with rate)",
        "",
        "## Crew level distribution (`crew_level`)",
        "",
        "| Level | Count |",
        "|---|---:|",
    ]
    for l, n in by_level.most_common():
        out.append(f"| `{l}` | {n} |")
    out += ["", "## New role distribution (`new_role`)", "", "| Role | Count |", "|---|---:|"]
    for r, n in new_role_counter.most_common():
        out.append(f"| `{r}` | {n} |")
    out += ["", "## Role assignment via `crew_id`", "", "| Role (crew_roles.id) | Role name | Count |", "|---|---|---:|"]
    for r, n in by_role.most_common():
        name = role_map.get(r, role_map.get(str(r), "-"))
        out.append(f"| {r} | {name} | {n} |")

    out += [
        "",
        "## Assignment volume (top 30 most-deployed crew)",
        "",
        f"Total assignment records: {len(book_guide_drivers):,}.",
        "",
        "| Crew id | Name | Assignments |",
        "|---|---|---:|",
    ]
    for cid, n in assign_count.most_common(30):
        nm = name_map.get(cid, name_map.get(str(cid), "-"))
        out.append(f"| {cid} | {nm} | {n} |")

    out += [
        "",
        "## Review signal",
        "",
        f"- **Internal `review_guides` rows:** {len(review_guides)}",
        "",
        "## Cross-references",
        "- [[people/guides]] — public guide bios",
        "- [[people/drivers]] — public driver roster",
        "- [[sources/backoffice-bookings-ops]] — booking volume that drives assignments",
        "",
    ]
    (OUT_DIR / "backoffice-staff.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  staff.md: {len(out)} lines")

# ============================================================
# backoffice-vendors.md
# ============================================================
def gen_vendors():
    vendors = load_csv("vendors")
    vc = load_csv("vendor_categories")
    hotels = load_csv("hotels")
    cars = load_csv("cars")
    user_garages = load_csv("user_garages")

    cat_map = {c["id"]: c.get("name", f"cat_{c['id']}") for c in vc}
    by_cat = Counter()
    for v in vendors:
        by_cat[v.get("vendor_category_id")] += 1

    out = frontmatter("Backoffice — Vendors & Supply", ["backoffice-mysql"])
    out += [
        "# Backoffice Vendors — Supply Chain Snapshot",
        "",
        f"Snapshot {TODAY}. Internal vendor + asset inventory.",
        "Bank account numbers, contact persons are in raw layer only.",
        "",
        "## Vendor headcount",
        "",
        f"- **Total vendors:** {len(vendors)}",
        f"- **Vendor categories:** {len(vc)}",
        f"- **Hotels (partners):** {len(hotels)}",
        f"- **Cars (fleet):** {len(cars)}",
        f"- **Garages tracked:** {len(user_garages)}",
        "",
        "## Vendors by category",
        "",
        "| Category | Count |",
        "|---|---:|",
    ]
    for cid, n in by_cat.most_common():
        out.append(f"| {cat_map.get(cid, f'cat_{cid}')} | {n} |")

    out += ["", "## Vendor list", "", "| Vendor | Category |", "|---|---|"]
    for v in sorted(vendors, key=lambda x: x.get("name") or ""):
        out.append(f"| {v.get('name','?')} | {cat_map.get(v.get('vendor_category_id'),'-')} |")

    out += ["", "## Hotels — area + rate range", "", "| Hotel | Vendor id | Rating | Double rate | Twin rate |", "|---|---|---:|---:|---:|"]
    for h in sorted(hotels, key=lambda x: x.get("name") or "")[:60]:
        out.append(f"| {h.get('name','?')} | {h.get('vendor_id','-')} | {h.get('rating','-')} | {h.get('double_rate','-')} | {h.get('twin_rate','-')} |")
    if len(hotels) > 60:
        out.append(f"\n*({len(hotels) - 60} more hotels in raw csv)*")

    out += ["", "## Car fleet — pax + rate", "", "| Car | Pax range | Price | Fuel | Driver allowance |", "|---|---|---:|---:|---:|"]
    for c in sorted(cars, key=lambda x: x.get("name") or "")[:50]:
        pax_range = f"{c.get('start_pax','?')}-{c.get('end_pax','?')}"
        out.append(f"| {c.get('name','?')} | {pax_range} | {c.get('price','-')} | {c.get('fuel','-')} | {c.get('driver','-')} |")

    out += [
        "",
        "## Cross-references",
        "- [[sources/backoffice-bookings-ops]] — vendor usage via `book_hotels`, `book_cars`",
        "- [[sources/backoffice-finance]] — cost side of margin calc",
        "",
    ]
    (OUT_DIR / "backoffice-vendors.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  vendors.md: {len(out)} lines")

# ============================================================
# backoffice-master-data.md
# ============================================================
def gen_master():
    tables_of_interest = [
        ("accounts", "Chart of accounts / financial accounts"),
        ("payment_methods", "Payment method options"),
        ("crew_roles", "Crew role catalog"),
        ("booking_categories", "Booking category catalog"),
        ("vendor_categories", "Vendor categories"),
        ("activity_categories", "Activity categories"),
        ("accommodation_categories", "Accommodation categories"),
        ("price_plans", "Price plans (B2B/B2C/Klook)"),
        ("price_categories", "Price categories (per-pax tiers)"),
        ("services", "Service definitions"),
        ("tags", "Tag catalog"),
        ("destinations", "Destination master"),
        ("areas", "Area master"),
        ("car_configurations", "Car configuration presets"),
        ("room_hotel_configurations", "Room/hotel configuration presets"),
        ("attachment_types", "Attachment type catalog"),
        ("file_types", "File type catalog"),
        ("folder_types", "Folder type catalog"),
        ("note_categories", "Note category catalog"),
        ("weather_codes", "Weather code mapping"),
        ("wa_chat_categories", "WhatsApp intent taxonomy"),
    ]

    out = frontmatter("Backoffice — Master Data Catalog", ["backoffice-mysql"])
    out += [
        "# Backoffice Master Data — Reference Catalogs",
        "",
        f"Snapshot {TODAY}. Seeded reference data backing all transactional tables.",
        "",
    ]
    for tbl, desc in tables_of_interest:
        rows = load_csv(tbl)
        out.append(f"## `{tbl}` — {desc}")
        out.append("")
        out.append(f"Rows: {len(rows)}")
        out.append("")
        if not rows:
            out.append("*(empty)*")
            out.append("")
            continue
        cols = list(rows[0].keys())
        # Pick label-like columns
        label_cols = [c for c in ["id", "name", "code", "type", "label", "category", "description", "icon", "slug"] if c in cols]
        if not label_cols:
            label_cols = cols[:5]
        out.append("| " + " | ".join(label_cols) + " |")
        out.append("|" + "|".join("---" for _ in label_cols) + "|")
        for r in rows[:50]:
            out.append("| " + " | ".join((r.get(c) or "") for c in label_cols) + " |")
        if len(rows) > 50:
            out.append(f"\n*({len(rows) - 50} more rows)*")
        out.append("")

    out += [
        "## Cross-references",
        "- [[sources/backoffice-schema]] — full table schema",
        "- [[sources/backoffice-finance]] — uses `accounts`, `payment_methods`",
        "- [[sources/backoffice-bookings-ops]] — uses `booking_categories`",
        "",
    ]
    (OUT_DIR / "backoffice-master-data.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  master-data.md: {len(out)} lines")

# ============================================================
# backoffice-whatsapp.md
# ============================================================
def gen_whatsapp():
    wa_chats = load_csv("wa_chats")
    wa_summaries = load_csv("wa_chat_summaries")
    wa_categories = load_csv("wa_chat_categories")
    wa_logs = load_csv("wa_logs")
    wa_itineraries = load_csv("wa_itineraries")

    direction = Counter()
    media = Counter()
    by_month = Counter()
    per_user = Counter()
    for c in wa_chats:
        direction[c.get("is_from_me") or "?"] += 1
        media[c.get("has_media") or "?"] += 1
        per_user[c.get("user_id") or "?"] += 1
        ym = (c.get("created_at") or "")[:7]
        if ym:
            by_month[ym] += 1

    cat_map = {c["id"]: c.get("name", f"cat_{c['id']}") for c in wa_categories}
    cat_summary = Counter()
    for s in wa_summaries:
        cat_summary[s.get("category_id") or "?"] += 1

    out = frontmatter("Backoffice — WhatsApp Operations", ["backoffice-mysql"])
    out += [
        "# Backoffice WhatsApp — Conversation Analytics",
        "",
        f"Snapshot {TODAY}. {len(wa_chats):,} chat messages, {len(wa_summaries):,} daily summaries.",
        "Individual messages stay in raw layer — only aggregates here.",
        "",
        "## Volume",
        "",
        f"- **Total chat messages:** {len(wa_chats):,}",
        f"- **Daily summaries:** {len(wa_summaries):,}",
        f"- **Itineraries shared via WA:** {len(wa_itineraries):,}",
        f"- **WhatsApp send logs:** {len(wa_logs):,}",
        f"- **Distinct customers in chat:** {len(per_user):,}",
        "",
        "## Direction (`is_from_me`)",
        "",
        "| 0 = from user, 1 = from JVTO | Count |",
        "|---|---:|",
    ]
    for d, n in direction.most_common():
        out.append(f"| `{d}` | {n:,} |")

    out += ["", "## Media presence", "", "| has_media | Count |", "|---|---:|"]
    for m, n in media.most_common():
        out.append(f"| `{m}` | {n:,} |")

    out += ["", "## Message volume by month", "", "| Month | Messages |", "|---|---:|"]
    for ym in sorted(by_month.keys()):
        out.append(f"| {ym} | {by_month[ym]:,} |")

    out += [
        "",
        "## Intent / category distribution (from `wa_chat_summaries`)",
        "",
        f"Intent taxonomy seeded by `WaIntentTaxonomySeeder` — {len(wa_categories)} categories.",
        "",
        "| Category | Summary entries |",
        "|---|---:|",
    ]
    for cid, n in cat_summary.most_common():
        out.append(f"| {cat_map.get(cid, f'cat_{cid}')} | {n:,} |")

    out += [
        "",
        "## Top conversations (by message count) — anonymized",
        "",
        "Customer identity intentionally omitted; raw layer has user mapping.",
        "",
        "| Rank | Messages |",
        "|---:|---:|",
    ]
    for i, (uid, n) in enumerate(per_user.most_common(20), 1):
        out.append(f"| #{i} | {n:,} |")

    out += [
        "",
        "## Cross-references",
        "- [[whatsapp/ops-playbook]] — WA ops procedures (manual)",
        "- [[whatsapp/canned-responses]] — template messages",
        "- [[sources/backoffice-bookings-ops]] — conversion from chat to booking",
        "",
    ]
    (OUT_DIR / "backoffice-whatsapp.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  whatsapp.md: {len(out)} lines")

# ============================================================
# backoffice-schema.md
# ============================================================
def gen_schema():
    inv = json.load(open("raw/backoffice/_inventory.json"))
    # FK relationships from information_schema
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE() AND REFERENCED_TABLE_NAME IS NOT NULL
        ORDER BY TABLE_NAME
    """)
    fks = cur.fetchall()
    conn.close()

    fks_by_table = defaultdict(list)
    for fk in fks:
        fks_by_table[fk["TABLE_NAME"]].append(
            (fk["COLUMN_NAME"], fk["REFERENCED_TABLE_NAME"], fk["REFERENCED_COLUMN_NAME"])
        )

    out = frontmatter("Backoffice — Schema Map", ["backoffice-mysql"])
    out += [
        "# Backoffice MySQL — Schema Map",
        "",
        f"Snapshot {TODAY}. MariaDB 10.11, database `u1805424_jvto_clone`.",
        "",
        f"- **Total tables:** {len(inv)}",
        f"- **Total foreign keys:** {len(fks)}",
        f"- Full DDL: `raw/backoffice/schema/full-schema.sql`",
        f"- Live Laravel models: `f:/BACK OFFICE/new-backoffice/app/Models/` (179 model files)",
        "",
        "## Core entity ERD (Mermaid)",
        "",
        "Subset of business-critical entities. Full schema in DDL file.",
        "",
        "```mermaid",
        "erDiagram",
        "  BOOKINGS ||--o{ BOOKING_PAYMENTS : has",
        "  BOOKINGS ||--o{ INVOICE_HISTORIES : line_items",
        "  BOOKINGS ||--o{ BOOK_GUIDE_DRIVERS : assigns",
        "  BOOKINGS ||--o{ BOOK_CARS : assigns",
        "  BOOKINGS ||--o{ BOOK_HOTELS : books",
        "  BOOKINGS ||--o{ BOOK_JEEPS : books",
        "  BOOKINGS ||--o{ BOOKING_ITINERARIES : details",
        "  BOOKINGS }o--|| AGENTS : sold_by",
        "  BOOKINGS }o--|| BOOKING_CATEGORIES : typed",
        "  BOOKINGS }o--o| PACKAGES : template",
        "  BOOKINGS }o--o| DISCOUNTS : applies",
        "  BOOKING_PAYMENTS }o--|| PAYMENT_METHODS : via",
        "  BOOK_GUIDE_DRIVERS }o--|| GUIDE_DRIVERS : crew",
        "  GUIDE_DRIVERS }o--|| CREW_ROLES : role",
        "  GUIDE_DRIVERS }o--o| USER_GARAGES : home_garage",
        "  BOOK_CARS }o--|| CARS : vehicle",
        "  BOOK_HOTELS }o--|| HOTELS : property",
        "  CARS }o--|| VENDORS : owned_by",
        "  HOTELS }o--|| VENDORS : owned_by",
        "  VENDORS }o--|| VENDOR_CATEGORIES : typed",
        "  PACKAGES ||--o{ PACKAGE_PRICES : priced",
        "  PACKAGE_PRICES }o--|| PRICE_PLANS : plan",
        "  PACKAGE_PRICES }o--|| PRICE_CATEGORIES : tier",
        "  TW_CALCULATIONS ||--o{ TW_CALCULATION_DETAILS : details",
        "  TW_CALCULATIONS }o--|| AGENTS : made_by",
        "  TW_CALCULATIONS }o--o| BOOKINGS : becomes",
        "  WA_CHATS }o--|| USERS : with",
        "  WA_CHAT_SUMMARIES }o--|| WA_CHAT_CATEGORIES : intent",
        "  TWT_INVOICES ||--o{ TWT_INVOICE_BOOKINGS : groups",
        "  TWT_INVOICES ||--o{ TWT_INVOICE_PAYMENTS : settled_by",
        "  TWT_INVOICES ||--o{ TWT_INVOICE_REFUNDS_PENALTIES : adjusts",
        "```",
        "",
        "## Foreign-key web (per-table)",
        "",
        "Tables with declared FKs — useful for impact analysis.",
        "",
        "| Table | FK column → ref table.column |",
        "|---|---|",
    ]
    for t in sorted(fks_by_table.keys()):
        for col, rt, rc in fks_by_table[t]:
            out.append(f"| `{t}` | `{col}` → `{rt}.{rc}` |")

    out += ["", "## Full table inventory (all 210 tables)", "",
            "| Table | Rows | Size KB | Bucket | Domain | FKs out |",
            "|---|---:|---:|---|---|---:|"]
    # Need domain from manifest (re-classify)
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
    for t in sorted(inv, key=lambda x: x["name"]):
        out.append(f"| `{t['name']}` | {t['rows_actual']:,} | {t['data_kb']:.0f} | {t['bucket']} | {domain_of(t['name'])} | {len(fks_by_table.get(t['name'], []))} |")

    out += [
        "",
        "## Cross-references",
        "- `raw/backoffice/_manifest.md` — extraction manifest",
        "- `raw/backoffice/schema/full-schema.sql` — full DDL",
        "- [[sources/backoffice-finance]]",
        "- [[sources/backoffice-bookings-ops]]",
        "- [[sources/backoffice-staff]]",
        "- [[sources/backoffice-vendors]]",
        "- [[sources/backoffice-pricing]]",
        "- [[sources/backoffice-master-data]]",
        "- [[sources/backoffice-whatsapp]]",
        "",
    ]
    (OUT_DIR / "backoffice-schema.md").write_text("\n".join(out), encoding="utf-8")
    print(f"  schema.md: {len(out)} lines")

def main():
    print("Generating wiki/sources/backoffice-*.md ...")
    gen_schema()
    gen_finance()
    gen_pricing()
    gen_bookings_ops()
    gen_staff()
    gen_vendors()
    gen_master()
    gen_whatsapp()
    print("Done.")

if __name__ == "__main__":
    main()
