# LLM-Wiki Domain Restructure — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize llm-wiki into domain-separated folders (website, whatsapp, seo, finance) so each workstream has its own namespace in both wiki/ and output/.

**Architecture:** Centralized wiki/ and output/ roots stay. Shared knowledge (destinations, products, people, credentials, reviews, sources) stays at wiki root. Domain-specific content moves into wiki/{domain}/ subfolders. Output artifacts consolidate under output/{domain}/. Finance domain created from raw/FINANCE/ data.

**Tech Stack:** Git (file moves), PowerShell/Bash (cross-reference updates), Python (Excel ingestion for finance)

**Spec:** `docs/superpowers/specs/2026-05-25-llm-wiki-domain-restructure-design.md`

---

### Task 1: Create Directory Structure

**Files:**
- Create directories in wiki/ and output/

- [ ] **Step 1: Create wiki domain directories**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
mkdir -p wiki/website wiki/whatsapp wiki/seo wiki/finance wiki/marketing wiki/analytics wiki/internal-ops
```

- [ ] **Step 2: Create output domain directories**

```bash
mkdir -p output/whatsapp output/marketing output/finance
```

Note: `output/website/` already exists (will be reorganized in Task 4). `output/social/` and `output/_archive/` already exist.

- [ ] **Step 3: Verify directories exist**

```bash
ls -d wiki/website wiki/whatsapp wiki/seo wiki/finance output/whatsapp output/marketing output/finance
```

Expected: All 7 directories listed.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "scaffold: create domain directories for wiki and output restructure"
```

---

### Task 2: Move wiki/content/ → wiki/website/

Move all 8 files from `wiki/content/` to `wiki/website/`. This renames the "content" domain to "website" since all files are website-specific knowledge.

**Files:**
- Move: `wiki/content/brand-voice.md` → `wiki/website/brand-voice.md`
- Move: `wiki/content/copy-bank.md` → `wiki/website/copy-bank.md`
- Move: `wiki/content/faq-master.md` → `wiki/website/faq-master.md`
- Move: `wiki/content/aeo-claims.md` → `wiki/website/aeo-claims.md`
- Move: `wiki/content/schema-templates.md` → `wiki/website/schema-templates.md`
- Move: `wiki/content/query-hero-claim.md` → `wiki/website/query-hero-claim.md`
- Move: `wiki/content/operational-facts.md` → `wiki/website/operational-facts.md`
- Move: `wiki/content/hotels.md` → `wiki/website/hotels.md`

- [ ] **Step 1: Git mv all 8 files**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
git mv wiki/content/brand-voice.md wiki/website/brand-voice.md
git mv wiki/content/copy-bank.md wiki/website/copy-bank.md
git mv wiki/content/faq-master.md wiki/website/faq-master.md
git mv wiki/content/aeo-claims.md wiki/website/aeo-claims.md
git mv wiki/content/schema-templates.md wiki/website/schema-templates.md
git mv wiki/content/query-hero-claim.md wiki/website/query-hero-claim.md
git mv wiki/content/operational-facts.md wiki/website/operational-facts.md
git mv wiki/content/hotels.md wiki/website/hotels.md
```

- [ ] **Step 2: Verify wiki/content/ is empty and wiki/website/ has 8 files**

```bash
ls wiki/content/ 2>/dev/null && echo "ERROR: content/ not empty" || echo "OK: content/ empty/gone"
ls wiki/website/ | wc -l
```

Expected: `OK: content/ empty/gone`, count = 8.

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "restructure: move wiki/content/ → wiki/website/ (8 files)"
```

---

### Task 3: Move wiki/ops/ WhatsApp Files → wiki/whatsapp/

Extract 3 WhatsApp-specific files from `wiki/ops/` into `wiki/whatsapp/`. Rename to remove date prefixes.

**Files:**
- Move: `wiki/ops/2026-05-14-whatsapp-operations-playbook.md` → `wiki/whatsapp/operations-playbook.md`
- Move: `wiki/ops/2026-05-14-whatsapp-rules-engine.md` → `wiki/whatsapp/rules-engine.md`
- Move: `wiki/ops/canned-responses.md` → `wiki/whatsapp/canned-responses.md`

- [ ] **Step 1: Git mv 3 files**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
git mv "wiki/ops/2026-05-14-whatsapp-operations-playbook.md" wiki/whatsapp/operations-playbook.md
git mv "wiki/ops/2026-05-14-whatsapp-rules-engine.md" wiki/whatsapp/rules-engine.md
git mv wiki/ops/canned-responses.md wiki/whatsapp/canned-responses.md
```

- [ ] **Step 2: Verify**

```bash
ls wiki/whatsapp/
```

Expected: `canned-responses.md  operations-playbook.md  rules-engine.md`

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "restructure: move WhatsApp ops → wiki/whatsapp/ (3 files)"
```

---

### Task 4: Move wiki/ops/ SEO Files → wiki/seo/

Extract 5 SEO/strategy files from `wiki/ops/` into `wiki/seo/`.

**Files:**
- Move: `wiki/ops/seo-strategy.md` → `wiki/seo/seo-strategy.md`
- Move: `wiki/ops/geo-aeo-strategy.md` → `wiki/seo/geo-aeo-strategy.md`
- Move: `wiki/ops/competitors.md` → `wiki/seo/competitors.md`
- Move: `wiki/ops/why-jvto-architecture.md` → `wiki/seo/why-jvto-architecture.md`
- Move: `wiki/ops/redirect-map.md` → `wiki/seo/redirect-map.md`

- [ ] **Step 1: Git mv 5 files**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
git mv wiki/ops/seo-strategy.md wiki/seo/seo-strategy.md
git mv wiki/ops/geo-aeo-strategy.md wiki/seo/geo-aeo-strategy.md
git mv wiki/ops/competitors.md wiki/seo/competitors.md
git mv wiki/ops/why-jvto-architecture.md wiki/seo/why-jvto-architecture.md
git mv wiki/ops/redirect-map.md wiki/seo/redirect-map.md
```

- [ ] **Step 2: Verify wiki/ops/ only has 3 meta files remaining**

```bash
ls wiki/ops/
```

Expected: `compilation-profiles.md  health-checks.md  ingestion-profiles.md` (only these 3 remain).

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "restructure: move SEO/strategy ops → wiki/seo/ (5 files)"
```

---

### Task 5: Reorganize output/ — Consolidate Website Artifacts

Merge `output/schema/`, `output/faq/`, `output/aeo/` under `output/website/`. Wrap existing website page copy in `output/website/pages/` subfolder.

**Strategy:** Rename `output/website/` to temp, create new structure, move temp into `pages/`, then move sibling folders in.

- [ ] **Step 1: Rename existing output/website/ to temp**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
git mv output/website output/_website-temp
```

- [ ] **Step 2: Create new output/website/ directory**

```bash
mkdir output/website
```

- [ ] **Step 3: Move temp into output/website/pages/**

```bash
git mv output/_website-temp output/website/pages
```

- [ ] **Step 4: Move schema, faq, aeo under output/website/**

```bash
git mv output/schema output/website/schema
git mv output/faq output/website/faq
git mv output/aeo output/website/aeo
```

- [ ] **Step 5: Move HANDOFF.md into output/website/**

```bash
git mv output/HANDOFF.md output/website/HANDOFF.md
```

- [ ] **Step 6: Verify output/ structure**

```bash
ls output/
ls output/website/
ls output/website/pages/ | head -5
```

Expected:
- `output/`: `_archive/  finance/  marketing/  social/  website/  whatsapp/`
- `output/website/`: `HANDOFF.md  aeo/  faq/  pages/  schema/`
- `output/website/pages/`: `bali-landing.md  blog.md  contact.md  ...`

- [ ] **Step 7: Commit**

```bash
git add -A && git commit -m "restructure: consolidate output/ — schema/faq/aeo under website/, page copy into pages/"
```

---

### Task 6: Update Cross-References — content/ → website/

Replace all `[[content/` wikilinks with `[[website/` across wiki/ and output/ files. Skip `wiki/log.md` (historical, append-only).

**Files to update** (based on grep results):

Wiki files:
- `wiki/people/dr-ahmad-irwandanu.md`
- `wiki/overview.md`
- `wiki/website/brand-voice.md` (was content/, self-references)
- `wiki/website/operational-facts.md`
- `wiki/website/schema-templates.md`
- `wiki/website/copy-bank.md`
- `wiki/seo/seo-strategy.md` (was ops/)
- `wiki/seo/geo-aeo-strategy.md`
- `wiki/ops/compilation-profiles.md`
- `wiki/sources/eav-ai-optimization-2026-05.md`
- `wiki/sources/geo-aeo-strategy-2026-05.md`
- `wiki/sources/why-jvto-trust-architecture.md`

Output files:
- `output/website/pages/homepage.md`
- `output/website/pages/bali-landing.md`
- `output/website/pages/surabaya-landing.md`
- `output/website/pages/verify-jvto/hub.md`
- `output/website/faq/bromo.md`
- `output/website/faq/ijen.md`
- `output/website/faq/madakaripura.md`
- `output/website/faq/papuma.md`
- `output/website/faq/tumpak-sewu.md`
- `output/website/aeo/why-jvto.md`
- `output/website/aeo/policy-travel-guide.md`

- [ ] **Step 1: Run find-and-replace across wiki/ (excluding log.md)**

Use a script to replace `[[content/` with `[[website/` in all .md files under `wiki/` except `wiki/log.md`:

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
grep -rl '\[\[content/' wiki/ --include='*.md' | grep -v 'wiki/log.md' | xargs sed -i 's/\[\[content\//[[website\//g'
```

- [ ] **Step 2: Run find-and-replace across output/**

```bash
grep -rl '\[\[content/' output/ --include='*.md' | xargs sed -i 's/\[\[content\//[[website\//g'
```

- [ ] **Step 3: Verify no remaining content/ references (outside log.md)**

```bash
grep -r '\[\[content/' wiki/ --include='*.md' -l | grep -v 'wiki/log.md'
grep -r '\[\[content/' output/ --include='*.md' -l
```

Expected: Both return empty (no matches).

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "restructure: update cross-references [[content/...]] → [[website/...]]"
```

---

### Task 7: Update Cross-References — ops/ → whatsapp/ and seo/

Replace moved ops/ wikilinks. Must be surgical — `[[ops/ingestion-profiles]]`, `[[ops/compilation-profiles]]`, `[[ops/health-checks]]` must NOT change (they stay in ops/).

**Replacements:**

| Old | New |
|-----|-----|
| `[[ops/seo-strategy]]` | `[[seo/seo-strategy]]` |
| `[[ops/geo-aeo-strategy]]` | `[[seo/geo-aeo-strategy]]` |
| `[[ops/competitors]]` | `[[seo/competitors]]` |
| `[[ops/why-jvto-architecture]]` | `[[seo/why-jvto-architecture]]` |
| `[[ops/redirect-map]]` | `[[seo/redirect-map]]` |
| `[[ops/2026-05-14-whatsapp-operations-playbook]]` | `[[whatsapp/operations-playbook]]` |
| `[[ops/2026-05-14-whatsapp-rules-engine]]` | `[[whatsapp/rules-engine]]` |
| `[[ops/canned-responses]]` | `[[whatsapp/canned-responses]]` |

Skip `wiki/log.md` (historical).

- [ ] **Step 1: Replace SEO references (5 patterns)**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
find wiki/ output/ -name '*.md' ! -path 'wiki/log.md' | xargs sed -i \
  -e 's/\[\[ops\/seo-strategy\]\]/[[seo\/seo-strategy]]/g' \
  -e 's/\[\[ops\/seo-strategy\]/[[seo\/seo-strategy]/g' \
  -e 's/\[\[ops\/geo-aeo-strategy\]\]/[[seo\/geo-aeo-strategy]]/g' \
  -e 's/\[\[ops\/geo-aeo-strategy\]/[[seo\/geo-aeo-strategy]/g' \
  -e 's/\[\[ops\/competitors\]\]/[[seo\/competitors]]/g' \
  -e 's/\[\[ops\/competitors\]/[[seo\/competitors]/g' \
  -e 's/\[\[ops\/why-jvto-architecture\]\]/[[seo\/why-jvto-architecture]]/g' \
  -e 's/\[\[ops\/why-jvto-architecture\]/[[seo\/why-jvto-architecture]/g' \
  -e 's/\[\[ops\/redirect-map\]\]/[[seo\/redirect-map]]/g' \
  -e 's/\[\[ops\/redirect-map\]/[[seo\/redirect-map]/g'
```

- [ ] **Step 2: Replace WhatsApp references (3 patterns)**

```bash
find wiki/ output/ -name '*.md' ! -path 'wiki/log.md' | xargs sed -i \
  -e 's/\[\[ops\/2026-05-14-whatsapp-operations-playbook\]\]/[[whatsapp\/operations-playbook]]/g' \
  -e 's/\[\[ops\/2026-05-14-whatsapp-operations-playbook\]/[[whatsapp\/operations-playbook]/g' \
  -e 's/\[\[ops\/2026-05-14-whatsapp-rules-engine\]\]/[[whatsapp\/rules-engine]]/g' \
  -e 's/\[\[ops\/2026-05-14-whatsapp-rules-engine\]/[[whatsapp\/rules-engine]/g' \
  -e 's/\[\[ops\/canned-responses\]\]/[[whatsapp\/canned-responses]]/g' \
  -e 's/\[\[ops\/canned-responses\]/[[whatsapp\/canned-responses]/g'
```

- [ ] **Step 3: Verify — only ops/ingestion-profiles, ops/compilation-profiles, ops/health-checks remain as ops/ links**

```bash
grep -r '\[\[ops/' wiki/ --include='*.md' -l | grep -v 'wiki/log.md' | sort
```

Expected: Only files referencing `[[ops/ingestion-profiles]]`, `[[ops/compilation-profiles]]`, or `[[ops/health-checks]]` should appear. Verify by spot-checking:

```bash
grep -r '\[\[ops/' wiki/ --include='*.md' | grep -v 'wiki/log.md' | grep -v 'ingestion-profiles' | grep -v 'compilation-profiles' | grep -v 'health-checks'
```

Expected: Empty (no matches). If any remain, they are missed replacements — fix manually.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "restructure: update cross-references [[ops/...]] → [[seo/...]] and [[whatsapp/...]]"
```

---

### Task 8: Update Frontmatter Type Fields

Files moved from `content/` had `type: content`. Files moved from `ops/` had `type: ops`. Update to reflect new domain.

- [ ] **Step 1: Update wiki/website/ files — type content → website**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
find wiki/website/ -name '*.md' | xargs sed -i 's/^type: content$/type: website/'
```

- [ ] **Step 2: Update wiki/whatsapp/ files — type ops → whatsapp**

```bash
find wiki/whatsapp/ -name '*.md' | xargs sed -i 's/^type: ops$/type: whatsapp/'
```

- [ ] **Step 3: Update wiki/seo/ files — type ops → seo**

```bash
find wiki/seo/ -name '*.md' | xargs sed -i 's/^type: ops$/type: seo/'
```

- [ ] **Step 4: Verify**

```bash
grep -r '^type:' wiki/website/ wiki/whatsapp/ wiki/seo/
```

Expected: All show `type: website`, `type: whatsapp`, or `type: seo` respectively.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "restructure: update frontmatter type fields for moved files"
```

---

### Task 9: Rewrite wiki/index.md

Full rewrite of index.md to reflect new folder structure. Add sections for website/, whatsapp/, seo/, finance/. Update all page paths.

**File:** Modify `wiki/index.md`

- [ ] **Step 1: Read current index.md to understand full structure**

Read the file in full. Note all sections and entries.

- [ ] **Step 2: Rewrite index.md**

Key changes:
- Rename "## Ops & Workflows" section → split into:
  - `## Website` — 8 pages (brand-voice, copy-bank, faq-master, aeo-claims, schema-templates, query-hero-claim, operational-facts, hotels)
  - `## SEO & Strategy` — 5 pages (seo-strategy, geo-aeo-strategy, competitors, why-jvto-architecture, redirect-map)
  - `## WhatsApp` — 3 pages (operations-playbook, rules-engine, canned-responses)
  - `## Finance` — 4 pages (rate-cards, package-costs, profit-analysis, custom-tour-builder) — mark as "NEW, pending ingestion"
  - `## Workflows (Meta)` — 3 pages (ingestion-profiles, compilation-profiles, health-checks)
- Update all `[[content/...]]` → `[[website/...]]` in descriptions
- Update all `[[ops/...]]` → appropriate domain paths in descriptions
- Update `total_pages` count in frontmatter

- [ ] **Step 3: Verify no broken links remain in index**

```bash
grep '\[\[content/' wiki/index.md
grep '\[\[ops/' wiki/index.md | grep -v 'ingestion-profiles\|compilation-profiles\|health-checks'
```

Expected: Both return empty.

- [ ] **Step 4: Commit**

```bash
git add wiki/index.md && git commit -m "restructure: rewrite wiki/index.md for domain-separated structure"
```

---

### Task 10: Update CLAUDE.md — Directory Structure

Update the `## Directory Structure` section in `CLAUDE.md` to reflect new layout. Also update Workflow references if any point to old paths.

**File:** Modify `CLAUDE.md` (project root)

- [ ] **Step 1: Read current CLAUDE.md directory structure section**

- [ ] **Step 2: Replace the directory structure block**

New structure:

```
llm-wiki/
raw/                  # Immutable source docs. LLM reads, NEVER writes here.
  FINANCE/            # Tour package cost spreadsheets + rate card JSONs
Clippings/            # Web clips from Obsidian Web Clipper. Treat as sources.
templates/            # Obsidian page templates
output/               # LLM-generated artifacts, organized by domain.
  website/            # All website artifacts
    pages/            # Page copy (homepage, tours, destinations, etc.)
    schema/           # JSON-LD structured data
    faq/              # FAQ answer pages
    aeo/              # AEO snippets
  social/             # Social media posts
  whatsapp/           # WA dashboard output
  marketing/          # Campaign output
  finance/            # Profit reports, custom tour quotes
  _archive/           # Superseded files
wiki/
    overview.md       # Master synthesis
    index.md          # Content catalog — AI entry point
    log.md            # Append-only operations log
    destinations/     # One page per destination
    reviews/          # Review compilations + pattern analysis
    products/         # Tour packages, pricing, itineraries
    people/           # Founder, doctor, guides, drivers
    credentials/      # Licenses, safety compliance, trust signals
    sources/          # One summary page per ingested raw source
    website/          # Brand voice, FAQ master, AEO claims, copy bank, schemas
    seo/              # SEO strategy, GEO/AEO, competitors, redirect map
    whatsapp/         # WA ops playbook, rules engine, canned responses
    finance/          # Rate cards, package costs, profit analysis, custom tour builder
    marketing/        # Future: campaigns, ad copy
    analytics/        # Future: metrics, tracking
    internal-ops/     # Future: SOPs, training
    ops/              # Meta-workflows: ingestion, compilation, health checks
CLAUDE.md             # This file
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md && git commit -m "restructure: update CLAUDE.md directory structure for domain separation"
```

---

### Task 11: Update output/website/HANDOFF.md

Update all output file paths in the route map. Every path changed because page copy moved from `output/website/` to `output/website/pages/` and sibling folders (schema, faq, aeo) moved under `output/website/`.

**File:** Modify `output/website/HANDOFF.md`

- [ ] **Step 1: Read current HANDOFF.md**

- [ ] **Step 2: Update all path references**

Replacements needed:
- All `website/` paths in the table → `website/pages/` (e.g., `website/homepage.md` → `website/pages/homepage.md`)
- All `schema/` paths → `website/schema/` (e.g., `schema/homepage-organization-schema.json` → `website/schema/homepage-organization-schema.json`)
- All `faq/` paths → `website/faq/`
- All `aeo/` paths → `website/aeo/`
- Update the header to reflect new structure

- [ ] **Step 3: Verify no old paths remain**

```bash
grep -E '^\| .* \| (website|schema|faq|aeo)/' output/website/HANDOFF.md | grep -v 'website/pages\|website/schema\|website/faq\|website/aeo'
```

Expected: Empty (all paths updated).

- [ ] **Step 4: Commit**

```bash
git add output/website/HANDOFF.md && git commit -m "restructure: update HANDOFF.md paths for consolidated output/website/"
```

---

### Task 12: Update Ingestion & Compilation Profiles

Add `finance-spreadsheet` ingestion profile. Add `custom-tour-quote` compilation profile. Update any path references in existing profiles.

**Files:**
- Modify: `wiki/ops/ingestion-profiles.md`
- Modify: `wiki/ops/compilation-profiles.md`

- [ ] **Step 1: Read both profile files**

- [ ] **Step 2: Update path references in compilation-profiles.md**

Replace any `[[content/brand-voice]]` → `[[website/brand-voice]]` and `[[ops/seo-strategy]]` → `[[seo/seo-strategy]]` references. (May already be done by Task 6/7, but verify.)

- [ ] **Step 3: Add finance-spreadsheet ingestion profile to ingestion-profiles.md**

Append a new profile section:

```markdown
### finance-spreadsheet

**Source type**: Excel (.xlsx) cost breakdown for a tour package.
**Extraction targets**:
- Per-day cost items (crew, vehicle, accommodation, activities, other)
- Pax tier pricing (1-pax, 2-pax, 3-pax columns or similar)
- Total COGS per pax tier
- Selling price per pax tier (if present)
- Component category subtotals

**Wiki pages to update**:
- [[finance/package-costs]] — add/update row for this package
- [[finance/profit-analysis]] — recalculate margins if selling price available
- [[products/packages-full-pricing]] — cross-reference pricing consistency

**Output naming**: N/A (data goes into wiki, not output)
```

- [ ] **Step 4: Add custom-tour-quote compilation profile to compilation-profiles.md**

Append a new profile section:

```markdown
### custom-tour-quote

**Purpose**: Build a custom tour cost estimate from rate cards.
**Input requirements**: Destination list, duration (days/nights), pax count, hotel tier preference, any special activity requests.
**Draw from**:
- [[finance/rate-cards]] — all cost components
- [[finance/package-costs]] — reference similar packages for sanity check
- [[products/packages-itineraries]] — route/timing templates
- [[destinations/*]] — activity options per destination

**Output format**: Itemized cost table → COGS → suggested selling price with markup.
**Output filename**: `output/finance/quote-{destination-slug}-{duration}.md`
**Verification**: Total COGS must equal sum of all line items. Cross-check vehicle/hotel rates against rate-cards.md.
```

- [ ] **Step 5: Commit**

```bash
git add wiki/ops/ingestion-profiles.md wiki/ops/compilation-profiles.md && git commit -m "restructure: add finance profiles to ingestion and compilation workflows"
```

---

### Task 13: Finance Ingestion — Rate Cards

Ingest all 5 rate card JSONs from `raw/FINANCE/rate_cards/` into a single wiki page.

**Files:**
- Create: `wiki/finance/rate-cards.md`
- Source: `raw/FINANCE/rate_cards/*.json` (5 files, already read — data in spec)

- [ ] **Step 1: Create wiki/finance/rate-cards.md**

Build page with frontmatter and 5 tables:

```markdown
---
type: finance
title: JVTO Rate Cards — Cost Component Reference
last_updated: 2026-05-25
sources: [finance-rate-cards]
---

# Rate Cards

*Consolidated cost components for all JVTO tour packages. All prices in IDR. Source: `raw/FINANCE/rate_cards/*.json`.*

## Crew Roles

| Role | Rate/Day (IDR) |
|------|----------------|
| Escort Guide (Senior) | 275,000 |
| Escort Guide (Junior) | 250,000 |
| Driver cum Guide | 250,000 |
| Escort Guide | 250,000 |
| Driver Only | 200,000 |

## Vehicles

| Type | Capacity | Rate/Day (IDR) |
|------|----------|----------------|
| MPV | 1–3 pax | 250,000 |
| Innova | 3 pax | 350,000 |
| Hiace | 4–9 pax | 1,100,000 |
| Hiace Premio | 4–9 pax | 1,300,000 |
| Mini Bus (Elf) | 10–13 pax | 1,350,000 |
| Medium Bus | 27–35 pax | 1,800,000 |

## Accommodation

| Hotel | Location | Rate Range (IDR) |
|-------|----------|-----------------|
| ARTOTEL Cabin Bromo | Bromo | 1,150,000 |
| Artha Cottage | — | 467,500–595,000 |
| Aston Banyuwangi | Banyuwangi | 525,000–625,000 |
| Atria Malang | Malang | 350,000–610,000 |
| Baobab Safari Resort | Prigen | 1,500,000–4,700,000 |
| Baratha Hotel | — | 175,000–625,000 |
| Bromo Terrace | Bromo | 300,000–1,350,000 |
| Doho Homestay | — | 150,000–440,000 |
| Grand Padis Hotel | — | 300,000–735,000 |
| Harris Hotel Satelit | Surabaya | 350,000–1,420,000 |
| Holiday Inn Express Surabaya | Surabaya | 350,000–550,000 |
| Hotel 88 Kedungsari | Surabaya | 330,000 |
| Hotel Santika Banyuwangi | Banyuwangi | 300,000–990,000 |
| Joglo Kecombrang Bromo | Bromo | 300,000–950,000 |
| Lava View Lodge | Bromo | 250,000–2,762,500 |
| Luminor Hotel | — | 250,000–500,000 |
| Manis Ae Cabin Bromo | Bromo | 350,000–2,220,000 |
| Riverside Homestay | — | 200,000–562,500 |
| Shanaya Resort Malang | Malang | 695,000–5,200,000 |
| THE 1O1 Malang OJ | Malang | 300,000–800,000 |
| Whiz Prime Malang | Malang | 200,000–517,000 |
| Whizz Bromo | Bromo | 200,000–550,000 |
| Yanto Homestay Tumpak Sewu | Lumajang | 350,000–550,000 |
```

Note: Full room-level detail is in `raw/FINANCE/rate_cards/Copy of accommodation-rate-card.json`. This page shows summary ranges. Add a collapsible per-hotel room table if granular lookup needed.

Continue with Activities and Other Costs tables (26 + 10 items from the JSON files already read).

- [ ] **Step 2: Add source page wiki/sources/finance-rate-cards.md**

```markdown
---
type: source
title: JVTO Rate Cards (Finance)
last_updated: 2026-05-25
sources: []
---

# Finance Rate Cards

*Source summary for `raw/FINANCE/rate_cards/` — 5 JSON files containing JVTO's internal cost components.*

**Files:**
- `Copy of crew-roles-rate-card.json` — 5 crew role daily rates
- `Copy of vehicle-rate-card.json` — 6 vehicle types with capacity + daily rate
- `Copy of accommodation-rate-card.json` — 23 hotels, 100+ room configurations
- `Copy of activities-rate-card.json` — 26 activity/ticket/meal costs
- `Copy of other-activities-rate-card.json` — 10 operational costs (fuel, toll, ferry, etc.)

**Key facts:**
- All prices in IDR
- Crew rates range 200,000–275,000/day
- Vehicle costs scale 250,000 (MPV) to 1,800,000 (Medium Bus) per day
- Police Escort is highest single cost: 2,000,000 per engagement
- Some hotels have weekday/weekend/high-season rate tiers (Lava View Lodge, Manis Ae, THE 1O1, Shanaya)

-> [[finance/rate-cards]] | -> [[finance/package-costs]]
```

- [ ] **Step 3: Commit**

```bash
git add wiki/finance/rate-cards.md wiki/sources/finance-rate-cards.md && git commit -m "ingest: finance rate cards — crew, vehicles, accommodation, activities, other costs"
```

---

### Task 14: Finance Ingestion — Package Costs from Excel

Ingest 15 Excel files from `raw/FINANCE/` into `wiki/finance/package-costs.md`. Requires reading .xlsx files.

**Files:**
- Create: `wiki/finance/package-costs.md`
- Source: 15 `.xlsx` files in `raw/FINANCE/`

- [ ] **Step 1: Extract Excel data using Python**

The Read tool cannot parse .xlsx. Use Python to extract structured data:

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
python3 -c "
import openpyxl, json, glob, os

results = []
for f in sorted(glob.glob('raw/FINANCE/*.xlsx')):
    wb = openpyxl.load_workbook(f, data_only=True)
    ws = wb.active
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append([str(c) if c is not None else '' for c in row])
    results.append({'file': os.path.basename(f), 'rows': data[:50]})
    wb.close()

print(json.dumps(results, indent=2, ensure_ascii=False))
" > /tmp/finance-extract.json
```

If `openpyxl` is not installed: `pip install openpyxl` first.

- [ ] **Step 2: Review extracted data**

Read `/tmp/finance-extract.json` to understand the spreadsheet structure (column headers, cost categories, pax tiers).

- [ ] **Step 3: Create wiki/finance/package-costs.md**

Build a summary table with one row per package. Columns: Package Name, Duration, COGS/pax (2 pax), Selling Price/pax (2 pax), Margin %. Add detail sections per package if data permits.

Frontmatter:
```markdown
---
type: finance
title: JVTO Package Cost Breakdown
last_updated: 2026-05-25
sources: [finance-rate-cards, db-export-2026-05]
---
```

- [ ] **Step 4: Commit**

```bash
git add wiki/finance/package-costs.md && git commit -m "ingest: finance package cost breakdowns from 15 Excel files"
```

---

### Task 15: Finance — Profit Analysis & Custom Tour Builder

Create remaining finance wiki pages. These are derived from rate-cards and package-costs data.

**Files:**
- Create: `wiki/finance/profit-analysis.md`
- Create: `wiki/finance/custom-tour-builder.md`

- [ ] **Step 1: Create wiki/finance/profit-analysis.md**

Frontmatter:
```markdown
---
type: finance
title: JVTO Profit Analysis
last_updated: 2026-05-25
sources: [finance-rate-cards, db-export-2026-05]
---
```

Content sections:
- **Margin by Package** — table: package name, COGS, selling price, margin %, ranked by profitability
- **Cost Driver Analysis** — which cost category dominates: accommodation vs transport vs crew vs activities
- **Most Profitable Packages** — top 5 with why (short duration? budget hotels? high markup?)
- **Least Profitable Packages** — bottom 5 with improvement suggestions
- **Optimization Opportunities** — vendor negotiation targets, route efficiency, hotel tier optimization

Cross-links: `-> [[finance/rate-cards]] | -> [[finance/package-costs]] | -> [[products/packages-full-pricing]]`

- [ ] **Step 2: Create wiki/finance/custom-tour-builder.md**

Frontmatter:
```markdown
---
type: finance
title: Custom Tour Cost Builder
last_updated: 2026-05-25
sources: [finance-rate-cards]
---
```

Content sections:
- **Formula**: `COGS = Σ(crew × days × rate) + Σ(vehicle × days × rate) + Σ(hotel_nights × rate) + Σ(activities) + Σ(other_costs)`
- **Step-by-step**: 1. Pick destinations → 2. Map route + days → 3. Select vehicle tier → 4. Select hotel tier → 5. List activities → 6. Add operational costs → 7. Calculate COGS → 8. Apply markup
- **Markup Guidelines**: table by pax count (1 pax = higher %, 4+ pax = lower %) and season
- **Worked Example**: 3D2N Ijen-Bromo budget tier for 2 pax — line by line

Cross-links: `-> [[finance/rate-cards]] | -> [[finance/package-costs]] | -> [[products/packages-itineraries]]`

- [ ] **Step 3: Commit**

```bash
git add wiki/finance/profit-analysis.md wiki/finance/custom-tour-builder.md && git commit -m "create: finance profit analysis + custom tour builder pages"
```

---

### Task 16: Final Verification

Comprehensive check that no broken cross-references remain and structure is clean.

- [ ] **Step 1: Check for orphaned content/ references (outside log.md)**

```bash
cd "E:/Users/JAVA VOLCANO/llm-wiki"
grep -r '\[\[content/' wiki/ output/ --include='*.md' | grep -v 'wiki/log.md'
```

Expected: Empty.

- [ ] **Step 2: Check for orphaned ops/ references to moved files (outside log.md)**

```bash
grep -r '\[\[ops/' wiki/ output/ --include='*.md' | grep -v 'wiki/log.md' | grep -v 'ingestion-profiles\|compilation-profiles\|health-checks\|volcano-status'
```

Expected: Empty. (`volcano-status` is a dead link noted in log — acceptable.)

- [ ] **Step 3: Verify wiki/ folder structure**

```bash
find wiki/ -type d | sort
```

Expected directories:
```
wiki/
wiki/analytics
wiki/credentials
wiki/destinations
wiki/finance
wiki/internal-ops
wiki/marketing
wiki/ops
wiki/people
wiki/products
wiki/reviews
wiki/seo
wiki/sources
wiki/website
wiki/whatsapp
```

- [ ] **Step 4: Verify output/ folder structure**

```bash
find output/ -type d | sort
```

Expected directories:
```
output/
output/_archive
output/finance
output/marketing
output/social
output/website
output/website/aeo
output/website/faq
output/website/pages
output/website/pages/destinations
output/website/pages/policy
output/website/pages/team
output/website/pages/tours
output/website/pages/tours/bali
output/website/pages/tours/student
output/website/pages/tours/surabaya
output/website/pages/travel-guide
output/website/pages/verify-jvto
output/website/pages/why-jvto
output/website/schema
output/whatsapp
```

- [ ] **Step 5: Count files to ensure nothing lost**

```bash
find wiki/ -name '*.md' | wc -l
find output/ -name '*.md' -o -name '*.json' | wc -l
```

Compare against pre-restructure counts:
- wiki/: ~67 .md files (should be ~67 + 4 new finance + 1 new source = ~72)
- output/: ~122 files (same count, just moved)

- [ ] **Step 6: Update wiki/log.md — append restructure entry**

```markdown
## [2026-05-25] restructure | Domain separation

Full restructure of wiki/ and output/ into domain-separated folders.

**Wiki moves:**
- `content/` → `website/` (8 files: brand-voice, copy-bank, faq-master, aeo-claims, schema-templates, query-hero-claim, operational-facts, hotels)
- `ops/` split: 3 files → `whatsapp/`, 5 files → `seo/`, 3 files stay in `ops/`

**Output moves:**
- `schema/`, `faq/`, `aeo/` → consolidated under `output/website/`
- Existing `output/website/*` → `output/website/pages/`

**New domains:**
- `wiki/finance/` — 4 pages (rate-cards, package-costs, profit-analysis, custom-tour-builder)
- `wiki/sources/finance-rate-cards.md` — source summary for raw/FINANCE/ rate cards
- Empty placeholders: `wiki/marketing/`, `wiki/analytics/`, `wiki/internal-ops/`, `output/whatsapp/`, `output/marketing/`, `output/finance/`

**Cross-references:** All `[[content/...]]` → `[[website/...]]`, all moved `[[ops/...]]` → `[[seo/...]]` or `[[whatsapp/...]]`. `wiki/log.md` unchanged (historical).
```

- [ ] **Step 7: Commit**

```bash
git add -A && git commit -m "restructure: final verification + log entry for domain separation"
```

---

### Task 17: Update CLAUDE.md Current Sprint

Update the Current Sprint section in CLAUDE.md to reflect completed restructure and set next task.

**File:** Modify `CLAUDE.md`

- [ ] **Step 1: Update Current Sprint**

```markdown
## Current Sprint

**Last completed:** Domain restructure — wiki/ and output/ reorganized into domain-separated folders (website, whatsapp, seo, finance). Finance rate cards ingested. 15 package cost Excel files ingested. Cross-references updated across ~30 files.
**Completed date:** 2026-05-25
**Next task:** Validate finance/profit-analysis.md against known selling prices on website. Then expand Silo 3 thin wiki pages (permit-requirements-east-java, sulfur-mining-cultural-guide, best-time-to-visit expansion).
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md && git commit -m "update sprint: domain restructure complete, next is finance validation + Silo 3"
```
