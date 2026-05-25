# Developer Handoff — JVTO Website Content

**Generated**: 2026-05-25
**Source**: llm-wiki vault (69 wiki pages, 23 sources, 122 output files)
**Target**: jvto-web (Next.js 16 + Prisma + NextAuth) at `F:\jvto-web`

---

## How This Works

The llm-wiki is the **content source of truth**. It contains:
- `wiki/` — structured knowledge pages (destinations, products, credentials, content guidelines)
- `output/` — generated artifacts ready for website use (page copy, schemas, FAQs, AEO blocks)

**Workflow**: wiki content → Workflow 5 compilation → output files → developer integrates into jvto-web

Each output file maps to a specific URL on javavolcano-touroperator.com. This document is the complete map.

---

## Content Delivery Pattern

jvto-web uses **Prisma + PostgreSQL** for dynamic content. Two patterns:

1. **DB-driven pages** (tours, destinations, FAQs): Content lives in Prisma models. Output markdown provides the copy to seed/update DB records.
2. **Static/SSG pages** (policy, travel-guide, why-jvto, verify-jvto): Content rendered from page components. Output markdown provides the copy for `page.tsx` or MDX files.

JSON-LD schemas in `output/schema/` inject via `<script type="application/ld+json">` in page head — ensure content is from trusted wiki source only.

---

## Route → Output → Schema Map

### Sitewide

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/` | `website/homepage.md` | `schema/homepage-organization-schema.json` | reviewed |
| `/tours` | `website/tours.md` | — | reviewed |
| `/tours/from-surabaya` | `website/surabaya-landing.md` | — | reviewed |
| `/tours/from-bali` | `website/bali-landing.md` | — | reviewed |
| `/destinations` | `website/destinations/hub.md` | — | draft |
| `/contact` | `website/contact.md` | — | draft |
| `/blog` | `website/blog.md` | — | draft |
| `/isic/student-package` | `website/isic-student-package.md` | — | draft |

### Tours — Surabaya Origin (12 packages)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/tours/from-surabaya/bromo-1d1n` | `website/tours/surabaya/bromo-1d1n.md` | `schema/bromo-1d1n-schema.json` | draft |
| `/tours/from-surabaya/bromo-2d1n` | `website/tours/surabaya/bromo-2d1n.md` | `schema/bromo-2d1n-schema.json` | draft |
| `/tours/from-surabaya/ijen-2d1n` | `website/tours/surabaya/ijen-2d1n.md` | `schema/ijen-2d1n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-3d2n` | `website/tours/surabaya/ijen-bromo-madakaripura-3d2n.md` | `schema/ijen-bromo-madakaripura-3d2n-schema.json` | draft |
| `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n` | `website/tours/surabaya/bromo-madakaripura-ijen-3d2n.md` | `schema/bromo-madakaripura-ijen-3d2n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-4d3n` | `website/tours/surabaya/ijen-bromo-madakaripura-4d3n.md` | `schema/ijen-bromo-madakaripura-4d3n-schema.json` | draft |
| `/tours/from-surabaya/tumpak-sewu-bromo-ijen-4d3n` | `website/tours/surabaya/tumpak-sewu-bromo-ijen-4d3n.md` | `schema/tumpak-sewu-bromo-ijen-4d3n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n` | `website/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `schema/ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n` | `website/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `schema/ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-malang-5d4n` | `website/tours/surabaya/ijen-bromo-madakaripura-malang-5d4n.md` | `schema/ijen-bromo-madakaripura-malang-5d4n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n` | `website/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n.md` | `schema/ijen-papuma-tumpak-sewu-bromo-malang-6d5n-schema.json` | draft |
| `/tours/from-surabaya/taman-safari-prigen-bromo-madakaripura-3d2n` | `website/tours/surabaya/taman-safari-prigen-bromo-madakaripura-3d2n.md` | `schema/taman-safari-prigen-bromo-madakaripura-3d2n-schema.json` | draft |

### Tours — Bali Origin (4 packages)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/tours/from-bali/bromo-ijen-3d2n` | `website/tours/bali/bromo-ijen-3d2n.md` | `schema/bali-bromo-ijen-3d2n-schema.json` | draft |
| `/tours/from-bali/ijen-bromo-madakaripura-3d2n` | `website/tours/bali/ijen-bromo-madakaripura-3d2n.md` | `schema/bali-ijen-bromo-madakaripura-3d2n-schema.json` | draft |
| `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-4d3n` | `website/tours/bali/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `schema/bali-ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | draft |
| `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-5d4n` | `website/tours/bali/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `schema/bali-ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | draft |

### Destinations (5 pages)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/destinations/ijen-crater` | `website/destinations/ijen-crater.md` | `schema/ijen-crater-schema.json` | draft |
| `/destinations/mount-bromo` | `website/destinations/mount-bromo.md` | `schema/mount-bromo-schema.json` | draft |
| `/destinations/tumpak-sewu-waterfall` | `website/destinations/tumpak-sewu-waterfall.md` | `schema/tumpak-sewu-waterfall-schema.json` | draft |
| `/destinations/madakaripura-waterfall` | `website/destinations/madakaripura-waterfall.md` | `schema/madakaripura-waterfall-schema.json` | draft |
| `/destinations/papuma-beach` | `website/destinations/papuma-beach.md` | `schema/papuma-beach-schema.json` | draft |

### Travel Guide (12 pages)

| Route | Output file | AEO block | FAQ block | Status |
|---|---|---|---|---|
| `/travel-guide` | `website/travel-guide/hub.md` | — | — | draft |
| `/travel-guide/faq` | `website/travel-guide/faq.md` | — | `faq/ijen.md` + `faq/bromo.md` + `faq/tumpak-sewu.md` + `faq/madakaripura.md` + `faq/papuma.md` | draft |
| `/travel-guide/best-time-to-visit` | `website/travel-guide/best-time-to-visit.md` | — | — | draft |
| `/travel-guide/booking-information` | `website/travel-guide/booking-information.md` | `aeo/policy-travel-guide.md` | — | draft |
| `/travel-guide/ijen-health-screening` | `website/travel-guide/ijen-health-screening.md` | `aeo/ijen.md` | `faq/ijen.md` | draft |
| `/travel-guide/packing-and-fitness` | `website/travel-guide/packing-and-fitness.md` | — | — | draft |
| `/travel-guide/police-escort-for-groups` | `website/travel-guide/police-escort-for-groups.md` | — | — | draft |
| `/travel-guide/safety-on-tours` | `website/travel-guide/safety-on-tours.md` | — | — | draft |
| `/travel-guide/weather-and-closures` | `website/travel-guide/weather-and-closures.md` | — | — | draft |
| `/travel-guide/bromo-vs-ijen-comparison` | `website/travel-guide/bromo-vs-ijen-comparison.md` | — | — | reviewed |
| `/travel-guide/what-to-pack-bromo-ijen` | `website/travel-guide/what-to-pack-bromo-ijen.md` | — | — | reviewed |
| `/travel-guide/private-vs-shared-tour-comparison` | `website/travel-guide/private-vs-shared-tour-comparison.md` | — | — | reviewed |

### Why JVTO (6 pages)

| Route | Output file | AEO block | Status |
|---|---|---|---|
| `/why-jvto` | `website/why-jvto/hub.md` | `aeo/why-jvto.md` | draft |
| `/why-jvto/our-story` | `website/why-jvto/our-story.md` | — | reviewed |
| `/why-jvto/our-team` | `website/why-jvto/our-team.md` | — | reviewed |
| `/why-jvto/the-jvto-difference` | `website/why-jvto/the-jvto-difference.md` | — | reviewed |
| `/why-jvto/reviews` | `website/why-jvto/reviews.md` | — | reviewed |
| `/why-jvto/community-standards` | `website/why-jvto/community-standards.md` | — | draft |

### Verify JVTO (5 pages)

| Route | Output file | Status |
|---|---|---|
| `/verify-jvto` | `website/verify-jvto/hub.md` | draft |
| `/verify-jvto/legal` | `website/verify-jvto/legal.md` | draft |
| `/verify-jvto/police-safety` | `website/verify-jvto/police-safety.md` | draft |
| `/verify-jvto/press-recognition` | `website/verify-jvto/press-recognition.md` | draft |
| `/verify-jvto/history-artifacts` | `website/verify-jvto/history-artifacts.md` | draft |

### Policy (4 pages)

| Route | Output file | Status |
|---|---|---|
| `/policy` | `website/policy/hub.md` | draft |
| `/policy/booking-payment-cancellation` | `website/policy/booking-payment-cancellation.md` | draft |
| `/policy/inclusions-exclusions` | `website/policy/inclusions-exclusions.md` | draft |
| `/policy/privacy` | `website/policy/privacy.md` | draft |

---

## Missing Pages (no output file yet)

### Ready to generate (wiki content available)

| Target route | Wiki source | Notes |
|---|---|---|
| `/team` | `wiki/people/crew-registry.md` + `wiki/people/agung-sambuko.md` | Team hub page — jvto-web has `/team` route |
| `/team/[slug]` | `wiki/people/crew-registry.md` | Individual crew member pages — jvto-web has `/team/[slug]` route |
| `/tours/student-package/[slug]` x6 | `wiki/products/packages-full-pricing.md` | 6 student packages with pricing — jvto-web has route |
| `/travel-guide/bromo-ijen-itinerary-guide` | `wiki/products/packages-itineraries.md` | Silo 4 content — itinerary comparison |
| `/travel-guide/surabaya-vs-bali-starting-point` | `wiki/sources/route-data-csv.md` + destination pages | Silo 4 content |

### Partially sourceable (wiki content needs expansion)

| Target route | Wiki source | Blocker |
|---|---|---|
| `/travel-guide/permit-requirements-east-java` | `wiki/credentials/legal-licenses.md` | Permit detail thin — needs BBKSDA/TNBTS fee tables |
| `/travel-guide/sulfur-mining-cultural-guide` | `wiki/destinations/kawah-ijen.md` | Cultural context section thin — needs Osing/sulfur mining source |
| `/travel-guide/best-time-to-visit` (expansion) | `wiki/content/operational-facts.md` | Seasonal weather data thin |

### Blocked (missing external sources)

| Target route | Blocker | Action needed |
|---|---|---|
| `/travel-guide/bromo-ijen-status-today` | PVMBG MAGMA feed not accessible | Need alternative volcano status source |
| `/travel-guide/yadnya-kasada-2026` | Tengger calendar data not in wiki | Need to ingest Kasada dates/cultural context |
| `/markets/singapore` | No SG-specific logistics data | Need flight routes, visa info, AirAsia/Scoot schedules |
| `/markets/malaysia` | No MY-specific logistics data | Need flight routes, halal food notes |
| `/travel-guide/from-singapore-to-bromo-guide` | Same as above | Same as above |
| `/travel-guide/from-malaysia-to-bromo-guide` | Same as above | Same as above |

---

## Schema Files

22 JSON-LD schema files in `output/schema/`, each with a `.receipt.md` verification file:

- **1 Organization schema** — homepage
- **16 TouristTrip schemas** — tour detail pages (12 Surabaya + 4 Bali)
- **5 TouristAttraction schemas** — destination pages

**Important**: Schema files contain trust signal values (reviewCount, ratingValue, NIB). These MUST match the canonical values in `wiki/credentials/trust-signals.md`. Current canonical values:
- Trustpilot: 4.8 / 51 reviews
- Google Maps: 4.90 / 92 reviews
- TripAdvisor: 4.95 / 21 reviews
- NIB: 1102230032918

---

## AEO Blocks (10 files)

Answer Engine Optimization snippets for AI search citation. Each file contains structured Q&A blocks optimized for LLM extraction.

| AEO file | Target page | Integration |
|---|---|---|
| `aeo/why-jvto.md` | `/why-jvto` | Overlay — add as hidden/structured data for AI crawlers |
| `aeo/policy-travel-guide.md` | `/policy` + `/travel-guide` | Overlay |
| `aeo/ijen.md` | `/destinations/ijen-crater` | Overlay |
| `aeo/bromo.md` | `/destinations/mount-bromo` | Overlay |
| `aeo/tumpak-sewu.md` | `/destinations/tumpak-sewu-waterfall` | Overlay |
| `aeo/madakaripura.md` | `/destinations/madakaripura-waterfall` | Overlay |
| `aeo/papuma.md` | `/destinations/papuma-beach` | Overlay |
| `aeo/bbksda-regulations-ijen.md` | `/travel-guide/bbksda-regulations-ijen` | Overlay |
| `aeo/bbksda-regulations-bromo.md` | `/travel-guide/bbksda-regulations-bromo` | Overlay |
| `aeo/ijen-gas-mask-equipment.md` | `/travel-guide/ijen-gas-mask-equipment` | Overlay |

---

## FAQ Blocks (8 files)

Destination-specific FAQ content for the `/travel-guide/faq` page and individual destination FAQs.

| FAQ file | Section |
|---|---|
| `faq/ijen.md` | Ijen-specific questions |
| `faq/bromo.md` | Bromo-specific questions |
| `faq/tumpak-sewu.md` | Tumpak Sewu questions |
| `faq/madakaripura.md` | Madakaripura questions |
| `faq/papuma.md` | Papuma questions |
| `faq/bbksda-regulations-ijen.md` | Ijen regulations |
| `faq/bbksda-regulations-bromo.md` | Bromo regulations |
| `faq/ijen-gas-mask-equipment.md` | Gas mask/equipment |

---

## SEO Quick Wins (from wiki/ops/seo-strategy.md)

Dev-actionable items. See `wiki/ops/seo-strategy.md` for full details.

| # | Action | Owner | Status |
|---|---|---|---|
| QW-1 | 301 redirects — legacy to SSOT routes | Dev | See `wiki/ops/redirect-map.md` |
| QW-3 | Fix meta description "From-surabaya" to "Surabaya" | Dev | Template bug |
| QW-5 | Organization/TravelAgency JSON-LD globally | Dev | Schema in `schema/homepage-organization-schema.json` |
| QW-6 | FAQPage JSON-LD on tour pages | Dev | Generate from FAQ blocks |
| QW-7 | TouristTrip + AggregateRating on tour pages | Dev | Schema files ready |
| QW-8 | Title tag rewrites (top 10) | Dev | See seo-strategy Title Tags section |
| QW-12 | BreadcrumbList schema on subpages | Dev | Template-level |

---

## Content Status Summary

| Status | Count | Meaning |
|---|---|---|
| reviewed | 12 files | Copy-checked, ready for site use |
| draft | 44 files | Generated from wiki, not yet reviewed |

**To publish a draft page**: Review against `wiki/content/brand-voice.md` voice guidelines + verify trust signal values against `wiki/credentials/trust-signals.md`.

---

## Key Wiki Reference Files for Dev

| Wiki page | What it provides |
|---|---|
| `wiki/ops/redirect-map.md` | 301 redirect mapping (legacy to new routes) |
| `wiki/ops/seo-strategy.md` | Keyword targets, title tags, quick wins |
| `wiki/content/schema-templates.md` | Schema.org field requirements per page type |
| `wiki/content/brand-voice.md` | Voice guidelines + meta description formula |
| `wiki/products/packages-full-pricing.md` | All pricing data (22 packages, all pax tiers) |
| `wiki/sources/wa-pro-crm-api.md` | WhatsApp API reference |
| `wiki/sources/gpx-destination-data.md` | Geo coordinates for all 5 destinations |
