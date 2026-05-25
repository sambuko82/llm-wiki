---
type: ops
title: Ingestion Profiles — Workflow 4
last_updated: 2026-05-25
sources: [llm-kb-tooling-guide]
---

# Ingestion Profiles

*Workflow 4: declare source type before beginning Workflow 1 step 1.*

Select the profile matching your source. The profile supplies type-specific extraction targets and the wiki pages most likely to need updating. All other Workflow 1 steps remain unchanged.

---

## web-clip

**What it is:** Article, blog post, or web page saved via Obsidian Web Clipper or manually pasted.

**Raw slug:** `YYYY-MM-DD-[site]-[topic].md` (e.g., `2026-05-11-detik-polpar-coverage.md`)

**Extract:**
- Voice/tone exemplars and verbatim quotable phrases
- Claims that corroborate or contradict existing wiki facts
- Any new statistics, ratings, or credentials mentioned

**Wiki pages to update:** `sources/[slug]`, `website/copy-bank` (if new voice exemplars found), relevant `destinations/` or `credentials/` pages if new facts surface

---

## pdf-doc

**What it is:** PDF document — policy pack, government regulation, certificate, or report.

**Raw slug:** `[doc-name]-v[N].md` (e.g., `jvto-policy-pack-v6.md`)

**Extract:**
- Structured facts, policy text verbatim, credential details
- Version delta from prior version if updating an existing source
- Any new license numbers, dates, or named officials

**Wiki pages to update:** `sources/[slug]`, `credentials/legal-licenses`, `credentials/trust-signals`, `products/packages-overview` (if pricing or inclusions changed)

---

## ssot-update

**What it is:** A new version of the JVTO SSOT JSON (canonical structured data, 13 domains).

**Raw slug:** `ssot-v[N].md` (e.g., `ssot-v7.md`)

**Extract:**
- Full diff against prior SSOT version — note every changed field
- New or removed packages, pricing changes, credential updates, personnel changes

**Wiki pages to update:** All domain pages — treat as a full wiki audit. Update `overview`, `products/packages-overview`, all `destinations/`, `people/`, `credentials/`, and `index`. Create `sources/ssot-v[N]` and add a deprecation note to the prior SSOT source page.

---

## review-feed

**What it is:** A new batch of Trustpilot reviews (or other platform) since the last ingest.

**Raw slug:** `[platform]-reviews-YYYY.md` (e.g., `trustpilot-reviews-2027.md`)

**Extract:**
- New reviews not already in `reviews/trustpilot-compilation` — cross-check by reviewer name and date
- Guide and driver names mentioned — add to crew name index if new
- Rating delta from previous ingest
- Any new complaint patterns or standout praise patterns

**Wiki pages to update:** `sources/[slug]`, `reviews/trustpilot-compilation`, `reviews/review-patterns`, `credentials/trust-signals` (update rating and review count)

---

## press-clip

**What it is:** News article, guidebook mention, or media coverage of JVTO.

**Raw slug:** `[outlet]-YYYY-MM-DD.md` (e.g., `kompas-2026-03-15.md`)

**Extract:**
- Publication name, date, journalist name if given
- Key quote verbatim in original language
- Topic: police-led, safety, destination feature, or award
- Whether it is independent or paid placement

**Wiki pages to update:** `sources/[slug]`, `credentials/trust-signals`, `credentials/press-coverage` (create this page if it does not exist — it is a tracked gap page)

---

## seo-audit

**What it is:** Structured SEO audit document with keyword data, technical findings, competitor analysis, schema requirements, and action items.

**Raw slug:** `seo-audit-YYYY-MM.md` (e.g., `seo-audit-2026-05.md`)

**Extract:**
- Technical issues (severity, fix description, responsible party: wiki vs dev)
- Keyword targets (term, difficulty, opportunity score, recommended page)
- Competitor intelligence (tier, domain, key strengths)
- Content gaps (topic, format, priority, recommended URL)
- Schema requirements (page type, required JSON-LD fields)
- Action items (QW quick-wins and SI strategic investments, numbered)
- Data discrepancies found (audit values vs wiki canonicals)

**Wiki pages to update:** `sources/[slug]`, `seo/seo-strategy` (create if not exists), `seo/competitors` (create if not exists), `seo/redirect-map` (create if not exists), `ops/compilation-profiles` (add schema profile), `website/brand-voice` (add meta description formula), `credentials/trust-signals` (add social URLs)

---

## finance-spreadsheet

**What it is:** Excel (.xlsx) cost breakdown for a tour package.

**Extraction targets:**
- Per-day cost items (crew, vehicle, accommodation, activities, other)
- Pax tier pricing (1-pax, 2-pax, 3-pax columns or similar)
- Total COGS per pax tier
- Selling price per pax tier (if present)
- Component category subtotals

**Wiki pages to update:**
- [[finance/package-costs]] — add/update row for this package
- [[finance/profit-analysis]] — recalculate margins if selling price available
- [[products/packages-full-pricing]] — cross-reference pricing consistency

**Output naming:** N/A (data goes into wiki, not output)
