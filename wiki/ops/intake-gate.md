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

## Visibility Rules

| Level | Meaning |
|-------|---------|
| public | Safe for website, SEO, customer-facing |
| internal | JVTO ops only — costs, margins, SOPs, vendor terms |
| hybrid | Wiki knowledge is internal, some output may be public |
| sensitive | Legal, medical, safety — requires human approval |
| public_sensitive | Public but with verification gate (credentials, regulations) |

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

## Rules

- Never treat every raw item as website content
- Raw data → wiki/SSOT first → then output
- Do not invent facts, prices, dates, regulations
- If confidence < 70%, mark needs_review
- New category proposals require human approval
- Sensitive claims (price, legal, medical, safety, credential) require verification before output

-> [[ops/ingestion-profiles]] | -> [[ops/compilation-profiles]]
