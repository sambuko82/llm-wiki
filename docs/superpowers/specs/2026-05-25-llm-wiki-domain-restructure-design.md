# LLM-Wiki Domain Restructure — Design Spec

**Date**: 2026-05-25
**Status**: Approved
**Scope**: Full restructure of llm-wiki — wiki/, output/, all folders
**Goal**: Domain-separated structure supporting website, WhatsApp, finance, marketing, analytics, and internal-ops workstreams

---

## Problem

Current structure mixes website content, WhatsApp operations, and SEO strategy in flat folders (`content/`, `ops/`). No namespace for finance data (15 tour package cost spreadsheets + 5 rate cards in `raw/FINANCE/`). As new domains are added (marketing campaigns, analytics, internal SOPs), the flat structure won't scale.

## Approach

Full domain separation. Both `wiki/` and `output/` get domain subfolders. Shared knowledge (destinations, products, people, credentials, reviews, sources) stays at wiki root since it's referenced across all domains.

---

## Target Structure

### output/ — Generated Artifacts by Domain

```
output/
  website/                         # javavolcano-touroperator.com
    pages/                         # Page copy (← existing output/website/*)
      homepage.md
      contact.md
      tours.md
      bali-landing.md
      surabaya-landing.md
      blog.md
      isic-student-package.md
      team.md
      destinations/                # hub + 5 destination pages
      tours/                       # bali/ student/ surabaya/
      policy/                      # 4 policy pages
      team/                        # 15 team member pages
      travel-guide/                # 11 guide pages
      verify-jvto/                 # 5 trust hub pages
      why-jvto/                    # 6 why pages
    schema/                        # JSON-LD (← from output/schema/)
    faq/                           # FAQ (← from output/faq/)
    aeo/                           # AEO snippets (← from output/aeo/)
    HANDOFF.md                     # Updated route map
  social/                          # Cross-domain social content
  whatsapp/                        # WA dashboard output (future)
  marketing/                       # Campaign output (future)
  finance/                         # Profit reports, custom tour quotes
  _archive/                        # Superseded files
```

### wiki/ — Knowledge by Domain

```
wiki/
  # ─── SHARED CORE (cross-domain, heavily cross-linked) ───
  destinations/                    # 5 pages: kawah-ijen, mount-bromo, tumpak-sewu, madakaripura, papuma-beach
  products/                        # packages-full-pricing, packages-itineraries, packages-overview
  people/                          # crew-registry, agung-sambuko, dr-ahmad-irwandanu
  credentials/                     # legal-licenses, medical-screening, police-integration, trust-signals, press-coverage
  reviews/                         # trustpilot-compilation, trustpilot-all-reviews, google-tripadvisor-2026, review-patterns
  sources/                         # 23 source summary pages (immutable references)

  # ─── DOMAIN-SPECIFIC ───
  website/                         # ← RENAMED from content/
    brand-voice.md
    copy-bank.md
    faq-master.md
    aeo-claims.md
    schema-templates.md
    query-hero-claim.md
    operational-facts.md
    hotels.md

  whatsapp/                        # ← EXTRACTED from ops/
    operations-playbook.md         # was: ops/2026-05-14-whatsapp-operations-playbook.md
    rules-engine.md                # was: ops/2026-05-14-whatsapp-rules-engine.md
    canned-responses.md            # was: ops/canned-responses.md

  seo/                             # ← EXTRACTED from ops/
    seo-strategy.md
    geo-aeo-strategy.md
    competitors.md
    why-jvto-architecture.md
    redirect-map.md

  finance/                         # NEW — ingested from raw/FINANCE/
    rate-cards.md                  # Consolidated: crew (5 roles), vehicles (6 types), accommodation (21 hotels), activities (26 items), other costs (10 items)
    package-costs.md               # Per-package cost breakdown from 15 .xlsx files
    profit-analysis.md             # Margin analysis, cost drivers, pricing recommendations
    custom-tour-builder.md         # Template for building custom tours from rate cards

  marketing/                       # FUTURE — campaigns, ad copy, email sequences
  analytics/                       # FUTURE — SEO metrics, review tracking, competitor intel
  internal-ops/                    # FUTURE — SOPs, training, crew schedules

  # ─── META (domain-agnostic workflows) ───
  ops/
    ingestion-profiles.md          # Stays
    compilation-profiles.md        # Stays
    health-checks.md               # Stays

  overview.md
  index.md
  log.md
```

### raw/ — No Changes

`raw/` is immutable source material. `raw/FINANCE/` stays as-is. Wiki finance pages reference it via source links.

---

## File Move Map

### wiki/content/ → wiki/website/

| From | To |
|------|-----|
| `content/brand-voice.md` | `website/brand-voice.md` |
| `content/copy-bank.md` | `website/copy-bank.md` |
| `content/faq-master.md` | `website/faq-master.md` |
| `content/aeo-claims.md` | `website/aeo-claims.md` |
| `content/schema-templates.md` | `website/schema-templates.md` |
| `content/query-hero-claim.md` | `website/query-hero-claim.md` |
| `content/operational-facts.md` | `website/operational-facts.md` |
| `content/hotels.md` | `website/hotels.md` |

### wiki/ops/ → split across domains

| From | To | Domain |
|------|-----|--------|
| `ops/2026-05-14-whatsapp-operations-playbook.md` | `whatsapp/operations-playbook.md` | whatsapp |
| `ops/2026-05-14-whatsapp-rules-engine.md` | `whatsapp/rules-engine.md` | whatsapp |
| `ops/canned-responses.md` | `whatsapp/canned-responses.md` | whatsapp |
| `ops/seo-strategy.md` | `seo/seo-strategy.md` | seo |
| `ops/geo-aeo-strategy.md` | `seo/geo-aeo-strategy.md` | seo |
| `ops/competitors.md` | `seo/competitors.md` | seo |
| `ops/why-jvto-architecture.md` | `seo/why-jvto-architecture.md` | seo |
| `ops/redirect-map.md` | `seo/redirect-map.md` | seo |
| `ops/ingestion-profiles.md` | `ops/ingestion-profiles.md` | meta (stays) |
| `ops/compilation-profiles.md` | `ops/compilation-profiles.md` | meta (stays) |
| `ops/health-checks.md` | `ops/health-checks.md` | meta (stays) |

### output/ reorganization

| From | To |
|------|-----|
| `output/schema/*` | `output/website/schema/*` |
| `output/faq/*` | `output/website/faq/*` |
| `output/aeo/*` | `output/website/aeo/*` |
| `output/website/*` (existing page copy) | `output/website/pages/*` |
| `output/social/*` | `output/social/*` (stays) |
| `output/_archive/*` | `output/_archive/*` (stays) |

---

## Cross-Reference Updates Required

1. **`wiki/index.md`** — Full rewrite: add finance, seo, whatsapp sections. Update all moved page paths.
2. **`wiki/log.md`** — No changes (historical record, append-only).
3. **`CLAUDE.md`** — Update Directory Structure section with new layout.
4. **`output/HANDOFF.md`** — Update all output file paths.
5. **All wiki pages** — Find/replace:
   - `[[content/` → `[[website/`
   - `[[ops/2026-05-14-whatsapp-operations-playbook]]` → `[[whatsapp/operations-playbook]]`
   - `[[ops/2026-05-14-whatsapp-rules-engine]]` → `[[whatsapp/rules-engine]]`
   - `[[ops/canned-responses]]` → `[[whatsapp/canned-responses]]`
   - `[[ops/seo-strategy]]` → `[[seo/seo-strategy]]`
   - `[[ops/geo-aeo-strategy]]` → `[[seo/geo-aeo-strategy]]`
   - `[[ops/competitors]]` → `[[seo/competitors]]`
   - `[[ops/why-jvto-architecture]]` → `[[seo/why-jvto-architecture]]`
   - `[[ops/redirect-map]]` → `[[seo/redirect-map]]`
6. **Compilation profiles** — Update any profile that references `content/` or `ops/` paths.

---

## Finance Domain — New Pages

### wiki/finance/rate-cards.md
- Ingest all 5 rate card JSONs into structured tables
- Sections: Crew Roles, Vehicles, Accommodation, Activities, Other Costs
- All prices in IDR
- Source: `raw/FINANCE/rate_cards/*.json`

### wiki/finance/package-costs.md
- Ingest 15 Excel files → per-package cost breakdown
- Columns: package name, duration, COGS per pax tier (1 pax, 2 pax, 3 pax, etc.), component breakdown (crew %, vehicle %, accommodation %, activities %, other %)
- Cross-reference with `[[products/packages-full-pricing]]`
- Source: `raw/FINANCE/*.xlsx`

### wiki/finance/profit-analysis.md
- Derived from package-costs data
- Sections: margin by package, cost driver analysis, most/least profitable packages, seasonal impact, optimization opportunities
- Updated after each pricing change

### wiki/finance/custom-tour-builder.md
- Template for composing custom itineraries from rate cards
- Formula: `COGS = Σ(crew_days × rate) + Σ(vehicle_days × rate) + Σ(accommodation_nights × rate) + Σ(activities × qty) + Σ(other × qty)`
- Markup guidelines by pax count and season
- Example: build a 3D2N custom Ijen-Bromo with budget hotel tier

---

## Ingestion Profile Addition

Add `finance-spreadsheet` type to `ops/ingestion-profiles.md`:
- **Extraction targets**: per-day cost breakdown, pax tier pricing, component categories
- **Wiki pages to update**: `finance/package-costs.md`, `finance/profit-analysis.md`, `products/packages-full-pricing.md`

---

## Compilation Profile Addition

Add `custom-tour-quote` profile to `ops/compilation-profiles.md`:
- **Input**: destination list, duration, pax count, hotel tier, special requests
- **Output**: itemized cost breakdown + suggested selling price
- **Save to**: `output/finance/quote-{slug}.md`

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Broken cross-references after move | Grep all `[[` links before and after. Automated find/replace. |
| Git history fragmented by moves | Use `git mv` to preserve history. Single commit per domain move. |
| Excel ingestion lossy | Read sample .xlsx first. Validate against known selling prices on website. |
| Future domain creep | Pattern is clear: add `wiki/{domain}/` + `output/{domain}/`. No structural changes needed. |
