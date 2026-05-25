---
type: ops
title: Universal Raw Intake Gate — Classification & Routing System
last_updated: 2026-05-25
sources: []
---

# Universal Raw Intake Gate

*Workflow 7: Every new raw item passes through this gate before ingestion. The gate classifies, routes, and prepares items — it does NOT generate final output.*

---

## Trigger

Place any new file in `raw/_inbox/`. Run: "Process inbox" or "Intake gate".

## Pipeline

1. **Identify** file type + source type + content intent
2. **Match** against existing wiki domains, categories, tags
3. **Route** to correct raw subfolder + wiki target + output target
4. **Extract** key facts, numbers, claims
5. **Check** duplicates, conflicts, verification needs
6. **Card** — generate intake card
7. **Manifest** — update raw/_manifest/ files

## Source Types

| Type | Description |
|------|-------------|
| web-clip | Article/blog from Obsidian Web Clipper |
| pdf-doc | PDF policy, regulation, certificate, report |
| review-feed | Trustpilot/Google/TripAdvisor review batch |
| press-clip | News/media coverage |
| seo-audit | SEO audit document |
| finance-spreadsheet | Excel cost breakdown |
| route-expense | Per-route operational cost data |
| trip-expense | Actual trip expense record |
| chat-backup | WhatsApp/chat export |
| customer-inquiry | Customer question/lead |
| ops-note | Internal operational note |
| sop-source | Standard operating procedure source |
| regulation-source | Government regulation/policy |
| incident-dataset | Safety incident or complaint data |
| url-list | List of URLs for crawling/reference |
| proof-asset | Photo/screenshot of credential/document |
| api-feedback | API integration issue/feedback |
| booking-data | Booking records/statistics |
| vendor-data | Vendor/partner information |
| db-export | Live database dump (SQL DDL, CSV rows, table inventory) — backoffice MySQL or equivalent |

## Domain Routing

| Domain | Wiki Target | Output Target |
|--------|-----------|---------------|
| destinations | wiki/destinations/ | output/website/pages/ |
| products | wiki/products/ | output/website/pages/tours/ |
| finance | wiki/finance/ | output/finance/ |
| operations | wiki/ops/ | output/ops/ (internal) |
| whatsapp | wiki/whatsapp/ | output/whatsapp/ |
| credentials | wiki/credentials/ | output/website/pages/verify-jvto/ |
| reviews | wiki/reviews/ | output/website/faq/, output/website/aeo/ |
| website | wiki/website/ | output/website/pages/ |
| seo | wiki/seo/ | output/website/pages/travel-guide/ |
| integrations | wiki/integrations/ | output/integrations/ (internal) |
| people | wiki/people/ | output/website/pages/team/ |
| sources | wiki/sources/ | no output |
| marketing | wiki/marketing/ | output/marketing/ |
| analytics | wiki/analytics/ | no output (internal) |
| internal-ops | wiki/internal-ops/ | output/ops/ (internal) |

## Visibility Rules

| Level | Meaning |
|-------|---------|
| public | Safe for website, SEO, customer-facing |
| internal | JVTO ops only — costs, margins, SOPs, vendor terms |
| hybrid | Wiki knowledge is internal, some output may be public |
| sensitive | Legal, medical, safety — requires human approval |
| public_sensitive | Public but with verification gate (credentials, regulations) |
| internal_pii | Internal only AND contains PII (customer emails/phones, payment refs, KTP) — must be gitignored at raw layer; wiki summaries must be aggregate-only |

## Evidence Weighting (descending authority)

1. Official government/authority source
2. JVTO verified internal operational record
3. Direct vendor/partner confirmation
4. Reputable news/media source
5. Structured dataset (DB export, SSOT JSON)
6. Customer review/chat
7. Unverified note
8. AI-generated summary

## Manifest Files

| File | Purpose |
|------|---------|
| `raw/_manifest/raw-files-index.csv` | Master index of all raw files |
| `raw/_manifest/ingest-status.csv` | Ingestion status per file |
| `raw/_manifest/source-url-index.csv` | URL sources for web clips |
| `raw/_manifest/decision-queue.md` | Items needing human decision |
| `raw/_manifest/sitemap-proposals.md` | Proposed new website URLs |
| `raw/_manifest/category-registry.yml` | Category taxonomy for raw item classification |
| `raw/_manifest/tag-registry.yml` | Cross-cutting tags for multi-domain items |
| `raw/_manifest/evidence-registry.yml` | Evidence items supporting C1-C9 claims |
| `raw/_manifest/conflict-log.md` | Detected data conflicts between sources |
| `raw/_manifest/recommendation-log.md` | Proposed changes from intake processing |

## Rules

- Never treat every raw item as website content
- Raw data → wiki/SSOT first → then output
- Do not invent facts, prices, dates, regulations
- If confidence < 70%, mark needs_review
- New category proposals require human approval
- Sensitive claims (price, legal, medical, safety, credential) require verification before output

## Correlation, Conflict, and Recommendation Layer

Before classifying any raw item as `unknown`, the gate must perform correlation against existing infrastructure.

### Pre-Classification Correlation

Check every raw item against:
1. `category-registry.yml` — does an existing category fit?
2. `tag-registry.yml` — which cross-cutting tags apply?
3. Existing wiki pages — does a target page already exist?
4. Existing output files — has this content been generated before?
5. `source-url-index.csv` — is this URL already indexed?
6. `raw-files-index.csv` — is this filename already tracked?

### Duplicate Detection

Before creating any new entry:
- Check `source-url-index.csv` for matching URLs
- Check `raw-files-index.csv` for matching filenames or content descriptions
- If duplicate found: link to existing entry, do NOT create new one
- If partial match: note overlap in intake card, propose merge or update

### Supporting Evidence Detection

When a raw item corroborates an existing claim (C1-C9):
- Add to `evidence-registry.yml` with appropriate evidence weight (1-8)
- Link to the claim it supports
- Do NOT create a new wiki page — evidence goes in the registry
- Update the source wiki page only if the evidence adds new facts

### Conflict Detection

When a raw item contradicts an existing claim:
- Add to `conflict-log.md` with both claims, sources, and evidence weights
- Compare authority: official > JVTO internal > vendor > media > dataset > review > note > AI
- Do NOT overwrite existing data automatically
- Mark `human_decision_required = true` if the conflict affects: prices, legal, medical, safety, credential, review rating, or operational decision-making
- Add to `decision-queue.md` for human resolution

### New Tag Proposal

Propose a new tag (NOT a new category) when:
- Existing categories fit the content domain
- A cross-cutting label is missing that would aid future correlation
- The tag applies to 3+ existing wiki pages
- Add proposal to `recommendation-log.md`, type = `new_tag`

### New Category Proposal

Propose a new category ONLY when:
- No existing category covers >50% of the content
- The closest 3 existing categories are documented in the proposal
- The overlap percentage with each is calculated
- `human_decision_required = true`
- Add proposal to `recommendation-log.md`, type = `new_category`

### New Wiki Page Proposal

Propose a new wiki page ONLY when:
- Knowledge strength is sufficient (evidence weight ≥ 3 — vendor/partner or higher)
- The content is not merely supporting evidence for an existing page
- A clear wiki target path is identified
- Add proposal to `recommendation-log.md`, type = `new_page`

### New Website URL Proposal

Propose a new public URL ONLY when:
- Public search intent exists (SEO/GEO/AEO value)
- The content has traveler education, trust-building, or conversion value
- Add to `sitemap-proposals.md` with proposed URL, target keyword, and justification
- `human_decision_required = true` for: legal, medical, safety, fatal accident, or official policy pages
- Add proposal to `recommendation-log.md`, type = `new_url`

### Internal Routing Rule

Data in these domains defaults to `internal` visibility:
- **finance** — costs, margins, rate cards, vendor terms
- **operations** — SOPs, crew schedules, internal workflows
- **whatsapp** — automation rules, canned responses, CRM logic
- **integrations** — API keys, Klook/ISIC integration details
- **internal-ops** — training materials, briefing documents

Do NOT force a website route for internal-only data. Route to wiki domain page and internal output target.

### Evidence Weighting

When multiple sources support different claims, prefer:
1. Official government/authority source
2. JVTO verified internal operational record
3. Direct vendor/partner confirmation
4. Reputable news/media source
5. Structured dataset (DB export, SSOT JSON)
6. Customer review/chat
7. Unverified note
8. AI-generated summary

Do NOT decide by source count alone. Prefer higher-authority, more recent, more specific, and more directly relevant sources.

-> [[ops/ingestion-profiles]] | -> [[ops/compilation-profiles]]
