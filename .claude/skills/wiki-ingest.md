---
name: wiki-ingest
description: Ingest a source into the llm-wiki (Workflow 1/4) AND immediately run Workflow 6 on-demand health checks — orphan detection, wikilink resolution, index completeness, log completeness, voice invariant grep — in the same session without a separate prompt. Use any time content from an external source is added or updated in the wiki. Prevents the recurring "run health check" follow-up prompt and catches real errors (orphans, index miscounts, broken links) before commit.
---

## Why this skill exists

Every wiki ingest session historically ends with a second prompt: "run health check." The log shows this pattern across every major ingest:

- `[2026-05-11] ingest | GPX Trail Data` → separate `[2026-05-11] health-check | On-Demand`
- `[2026-05-12] ingest | DB Export` → separate `[2026-05-12] health-check | Weekly`
- `[2026-05-16] ingest | Image Asset Map` → separate `[2026-05-16] health-check | On-Demand`
- `[2026-05-24] ingest | 3D Route Viewer` → **health check never ran** (this session)

Health checks catch real bugs. The `[2026-05-12]` weekly check found `total_pages` overcounted by 2 (38→36) — a silent error that would have accumulated across future ingests. This skill runs the check automatically so it cannot be skipped.

---

## When to trigger

Invoke before any wiki write operation that adds or updates content from an external source:

- "Ingest this URL into the wiki"
- "Add this PDF to the knowledge base"
- "Update the wiki with the new DB export"
- "Integrate [source] into llm-wiki"
- "Record the 3D route viewer feature in the wiki"
- Any sentence with "ingest", "add to wiki", "update wiki", "record in wiki" + a source

Do NOT trigger for:
- Generating output files from existing wiki content → use `wiki-compile` instead
- Fixing a typo in a single wiki page → direct Edit, no ingest workflow
- Running a standalone health check → that is step 5 of this skill, not a separate trigger

---

## Step 1 — Declare source type

Before reading anything, match the source to one ingestion profile from `wiki/ops/ingestion-profiles.md`:

| Profile | Source examples |
|---|---|
| `web-clip` | Firecrawl or Playwright scrape of a live URL |
| `pdf-doc` | Policy doc, travel guide, government PDF |
| `ssot-update` | SSOT JSON, DB export, any structured data export |
| `review-feed` | Trustpilot, Google, TripAdvisor review batch |
| `press-clip` | Detik, Radar Jember, BBKSDA press article |
| `seo-audit` | Ahrefs export, GSC data, keyword/ranking report |
| `feature-data` | GeoJSON, GPX, image asset maps, technical project data |

State the profile before continuing: **"Profile: ssot-update. Reading now."**

---

## Step 2 — Read and extract

Read the source fully before writing anything. Do not start writing until reading is complete.

Extract per the declared profile's targets (see `wiki/ops/ingestion-profiles.md`). Note:
- Facts that contradict existing wiki pages — flag immediately with `> Contradiction with [[page]]: <detail>`
- New entities referenced that have no wiki page — add to gap candidates list
- Claims that update existing pages — record which pages and what changes

---

## Step 3 — Write wiki changes

Follow Workflow 1 steps 3–5 in order:

1. **Create** `wiki/sources/[slug].md` — use `type: source` frontmatter; include key facts, quotes, content angles, cross-references to domain pages
2. **Update** domain pages (destinations, products, people, credentials, content, ops) — add new sections or extend existing tables; do not remove existing content without explicit instruction
3. **Update** `wiki/index.md`:
   - Add source entry in the **Sources** section
   - Update any domain page descriptions if they now have new capabilities (e.g., "· 3D viewer /3d/ijen-crater")
   - Increment `total_pages` by the number of new pages created
   - Update `last_updated` to today's date

---

## Step 4 — Append to log

Prepend a new entry at the top of `wiki/log.md` (newest-first format). Required format:

```
## [YYYY-MM-DD] ingest | [Source Title]

Pages created: [[sources/slug]] (new) — [one-sentence summary].
Pages updated ([N]): [domain pages]. Key additions: [brief].
Pages updated (meta): [[index]] (total_pages X→Y, last_updated YYYY-MM-DD).
```

Also update `last_updated` in `wiki/log.md` frontmatter to today.

---

## Step 5 — Auto-verify (Workflow 6 On-Demand — do not skip)

Run all checks using tools immediately after writing. Do not ask the user to trigger this. Do not self-report — every check must use an actual tool call.

### 5A — Wikilink resolution

For every new `[[wikilink]]` written in this session, confirm the target file exists:

```
Glob: wiki/[folder]/[slug].md  (exact path for each new link target)
```

A `[[sources/3d-route-viewer]]` link requires a file at `wiki/sources/3d-route-viewer.md`. Any missing file is a 🔴 error — fix before commit.

**Tool**: `Glob` with the exact expected path per new wikilink.

### 5B — Orphan detection

For every **new page** created this session, confirm it has at least one inbound link from a non-index/log content page:

```
Grep wiki/ for [[new-page-slug]] across all .md files, exclude index.md and log.md
```

Zero inbound links = orphan. Fix by adding `→ [[new-page]]` on the most relevant existing page (source pages: destination pages; destination pages: overview or products page). If no obvious parent exists, flag to user as 🟡 risk.

**Tool**: `Grep` — pattern `\[\[sources/slug\]\]` (or the page's path), path `wiki/`, file type `md`.

### 5C — Index completeness

Confirm `total_pages` in `wiki/index.md` matches actual file count:

```
Glob: wiki/**/*.md  → count results → subtract 2 (index.md + log.md)
Read: wiki/index.md frontmatter → check total_pages value
```

If counts differ, correct `total_pages` in `wiki/index.md` and record the fix in the verification report. The `[2026-05-12]` session found a silent +2 overcount by exactly this check.

**Tool**: `Glob` for file count, `Read` for frontmatter value.

### 5D — Log completeness

Confirm the new source has a log entry:

```
Grep wiki/log.md for the source slug or title added in step 4
```

Missing log entry = 🟡 risk. Fix by appending the entry from step 4.

**Tool**: `Grep` — search `wiki/log.md` for the source slug.

### 5E — Voice invariant check

Grep every file written or edited this session for forbidden phrases:

| Grep pattern | Rule |
|---|---|
| `(?i)blue fire guaranteed` | Natural phenomenon — conditional framing only |
| `(?i)100% blue fire` | Same |
| `(?i)mandatory health screening` | Must include conditional qualifier |
| `(?i)JVTO provides police escort` | Must include group-size/formal-request context |

**Tool**: `Grep` with `output_mode: content`, case-insensitive, across each edited file path.

---

## Step 6 — Report and commit

After all five checks, output a verification summary:

```
VERIFICATION REPORT
-------------------
5A Wikilink resolution:  [N broken / CLEAN]
5B Orphan detection:     [N orphans / CLEAN]
5C Index completeness:   [total_pages X — MATCH / MISMATCH → corrected to Y]
5D Log completeness:     [FOUND / MISSING → added]
5E Voice invariants:     [N violations / CLEAN]

Errors (🔴): [count]   Risks (🟡): [count]
```

Resolve all 🔴 errors before commit. 🟡 risks may be committed with a note in the log. Then commit:

```
git add wiki/sources/[slug].md wiki/destinations/*.md wiki/index.md wiki/log.md
git commit -m "ingest | [Source Title]"
```

---

## Tools required

| Tool | Role | Used in step |
|---|---|---|
| `Read` | Read source files and existing wiki pages | 2, 3, 5C |
| `Write` | Create new wiki source pages | 3 |
| `Edit` | Update existing wiki pages (domain pages, index, log) | 3, 4 |
| `Glob` | Count `.md` files for index completeness; confirm file paths for wikilink resolution | 5A, 5C |
| `Grep` | Orphan detection, log completeness, voice invariant check | 5B, 5D, 5E |
| `Bash` | `git add` + `git commit` at step 6 | 6 |
| `WebFetch` | **Enhancement**: fetch live URLs for `web-clip` profile ingests; monthly credential verification (Trustpilot count, NIB status) | 2 (web-clip only) |
| `mcp__plugin_playwright_playwright__browser_snapshot` | **Enhancement**: scrape JS-rendered pages that WebFetch cannot reach (Trustpilot review listings, live sitemaps) | 2 (review-feed only) |

---

## Self-check: did the verification actually run?

Before closing, confirm:

- [ ] `wiki/sources/[slug].md` created with `type: source` frontmatter
- [ ] All relevant domain pages updated (not just index + log)
- [ ] `Glob` was called for file count — not estimated
- [ ] `Grep` was called at least once for orphan or invariant check — not self-reported
- [ ] `total_pages` in `wiki/index.md` matches actual Glob count
- [ ] `wiki/log.md` has new entry dated today at the top
- [ ] All 🔴 errors resolved before commit
- [ ] Committed with `ingest | [Source Title]` message

If Grep and Glob were never called, the verification did not run. Do not report PASS.
