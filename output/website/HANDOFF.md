# Developer Handoff — JVTO Website Content

**Generated**: 2026-05-25
**Source**: llm-wiki vault (page/source/output counts maintained in `wiki/index.md` and `bases/index.base` — not duplicated here)
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

JSON-LD schemas in `output/website/schema/` inject via `<script type="application/ld+json">` in page head — ensure content is from trusted wiki source only.

---

## Policy Bundle Sync

The Policy Bundle is the machine-readable source for checkout, invoice, and WhatsApp policy wording. Use it before editing any policy copy in jvto-web.

| Producer file | jvto-web target | Purpose |
|---|---|---|
| `output/website/policy-bundle/_manifest.json` | `src/data/policy-bundle/_manifest.json` | Sync/version gate |
| `output/website/policy-bundle/policy-bundle.json` | `src/data/policy-bundle/policy-bundle.json` | Full policy registry |
| `output/website/policy-bundle/consumer-bundles.json` | `src/data/policy-bundle/consumer-bundles.json` | Checkout, invoice, WhatsApp entrypoint |
| `output/website/policy-bundle/deprecated-wording-report.json` | `src/data/policy-bundle/deprecated-wording-report.json` | Deprecated wording validation |
| `output/website/policy-bundle/gap-report.json` | `src/data/policy-bundle/gap-report.json` | Compiler health check |

jvto-web sync gate:

```js
manifest.schema_version === "policy-bundle/v1.0" && manifest.clean === true
```

Implementation handoff: `output/website/policy-bundle/JVTO_WEB_SYNC_HANDOFF.md`. Script template: `docs/templates/sync-policy-bundle.mjs`.

---

## Route → Output → Schema Map

### Sitewide

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/` | `website/pages/homepage.md` | `website/schema/homepage-organization-schema.json` | reviewed |
| `/tours` | `website/pages/tours.md` | — | reviewed |
| `/tours/from-surabaya` | `website/pages/surabaya-landing.md` | — | reviewed |
| `/tours/from-bali` | `website/pages/bali-landing.md` | — | reviewed |
| `/destinations` | `website/pages/destinations/hub.md` | — | draft |
| `/contact` | `website/pages/contact.md` | — | draft |
| `/blog` | `website/pages/blog.md` | — | draft |
| `/isic/student-package` | `website/pages/isic-student-package.md` | — | draft |

### Tours — Surabaya Origin (11 SSOT canonical + 1 specialty = 12 routes)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/tours/from-surabaya/bromo-1d1n` | `website/pages/tours/surabaya/bromo-1d1n.md` | `website/schema/bromo-1d1n-schema.json` | draft |
| `/tours/from-surabaya/bromo-2d1n` | `website/pages/tours/surabaya/bromo-2d1n.md` | `website/schema/bromo-2d1n-schema.json` | draft |
| `/tours/from-surabaya/ijen-2d1n` | `website/pages/tours/surabaya/ijen-2d1n.md` | `website/schema/ijen-2d1n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-3d2n` | `website/pages/tours/surabaya/ijen-bromo-madakaripura-3d2n.md` | `website/schema/ijen-bromo-madakaripura-3d2n-schema.json` | draft |
| `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n` | `website/pages/tours/surabaya/bromo-madakaripura-ijen-3d2n.md` | `website/schema/bromo-madakaripura-ijen-3d2n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-4d3n` | `website/pages/tours/surabaya/ijen-bromo-madakaripura-4d3n.md` | `website/schema/ijen-bromo-madakaripura-4d3n-schema.json` | draft |
| `/tours/from-surabaya/tumpak-sewu-bromo-ijen-4d3n` | `website/pages/tours/surabaya/tumpak-sewu-bromo-ijen-4d3n.md` | `website/schema/tumpak-sewu-bromo-ijen-4d3n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n` | `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `website/schema/ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n` | `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `website/schema/ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | draft |
| `/tours/from-surabaya/ijen-bromo-madakaripura-malang-5d4n` | `website/pages/tours/surabaya/ijen-bromo-madakaripura-malang-5d4n.md` | `website/schema/ijen-bromo-madakaripura-malang-5d4n-schema.json` | draft |
| `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n` | `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n.md` | `website/schema/ijen-papuma-tumpak-sewu-bromo-malang-6d5n-schema.json` | draft |
| `/tours/from-surabaya/taman-safari-prigen-bromo-madakaripura-3d2n` **(Specialty)** | `website/pages/tours/surabaya/taman-safari-prigen-bromo-madakaripura-3d2n.md` | `website/schema/taman-safari-prigen-bromo-madakaripura-3d2n-schema.json` | draft |

### Tours — Bali Origin (4 packages)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/tours/from-bali/bromo-ijen-3d2n` | `website/pages/tours/bali/bromo-ijen-3d2n.md` | `website/schema/bali-bromo-ijen-3d2n-schema.json` | draft |
| `/tours/from-bali/ijen-bromo-madakaripura-3d2n` | `website/pages/tours/bali/ijen-bromo-madakaripura-3d2n.md` | `website/schema/bali-ijen-bromo-madakaripura-3d2n-schema.json` | draft |
| `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-4d3n` | `website/pages/tours/bali/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `website/schema/bali-ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | draft |
| `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-5d4n` | `website/pages/tours/bali/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `website/schema/bali-ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | draft |

### Destinations (5 pages)

| Route | Output file | Schema | Status |
|---|---|---|---|
| `/destinations/ijen-crater` | `website/pages/destinations/ijen-crater.md` | `website/schema/ijen-crater-schema.json` | draft |
| `/destinations/mount-bromo` | `website/pages/destinations/mount-bromo.md` | `website/schema/mount-bromo-schema.json` | draft |
| `/destinations/tumpak-sewu-waterfall` | `website/pages/destinations/tumpak-sewu-waterfall.md` | `website/schema/tumpak-sewu-waterfall-schema.json` | draft |
| `/destinations/madakaripura-waterfall` | `website/pages/destinations/madakaripura-waterfall.md` | `website/schema/madakaripura-waterfall-schema.json` | draft |
| `/destinations/papuma-beach` | `website/pages/destinations/papuma-beach.md` | `website/schema/papuma-beach-schema.json` | draft |

### Travel Guide (12 pages)

| Route | Output file | AEO block | FAQ block | Status |
|---|---|---|---|---|
| `/travel-guide` | `website/pages/travel-guide/hub.md` | — | — | draft |
| `/travel-guide/faq` | `website/pages/travel-guide/faq.md` | — | `website/faq/ijen.md` + `website/faq/bromo.md` + `website/faq/tumpak-sewu.md` + `website/faq/madakaripura.md` + `website/faq/papuma.md` | draft |
| `/travel-guide/best-time-to-visit` | `website/pages/travel-guide/best-time-to-visit.md` | — | — | draft |
| `/travel-guide/booking-information` | `website/pages/travel-guide/booking-information.md` | `website/aeo/policy-travel-guide.md` | — | draft |
| `/travel-guide/ijen-health-screening` | `website/pages/travel-guide/ijen-health-screening.md` | `website/aeo/ijen.md` | `website/faq/ijen.md` | draft |
| `/travel-guide/packing-and-fitness` | `website/pages/travel-guide/packing-and-fitness.md` | — | — | draft |
| `/travel-guide/police-escort-for-groups` | `website/pages/travel-guide/police-escort-for-groups.md` | — | — | draft |
| `/travel-guide/safety-on-tours` | `website/pages/travel-guide/safety-on-tours.md` | — | — | draft |
| `/travel-guide/weather-and-closures` | `website/pages/travel-guide/weather-and-closures.md` | — | — | draft |
| `/travel-guide/bromo-vs-ijen-comparison` | `website/pages/travel-guide/bromo-vs-ijen-comparison.md` | — | — | reviewed |
| `/travel-guide/what-to-pack-bromo-ijen` | `website/pages/travel-guide/what-to-pack-bromo-ijen.md` | — | — | reviewed |
| `/travel-guide/private-vs-shared-tour-comparison` | `website/pages/travel-guide/private-vs-shared-tour-comparison.md` | — | — | reviewed |

### Why JVTO (6 pages)

| Route | Output file | AEO block | Status |
|---|---|---|---|
| `/why-jvto` | `website/pages/why-jvto/hub.md` | `website/aeo/why-jvto.md` | draft |
| `/why-jvto/our-story` | `website/pages/why-jvto/our-story.md` | — | reviewed |
| `/why-jvto/our-team` | `website/pages/why-jvto/our-team.md` | — | reviewed |
| `/why-jvto/the-jvto-difference` | `website/pages/why-jvto/the-jvto-difference.md` | — | reviewed |
| `/why-jvto/reviews` | `website/pages/why-jvto/reviews.md` | — | reviewed |
| `/why-jvto/community-standards` | `website/pages/why-jvto/community-standards.md` | — | draft |

### Verify JVTO (5 pages)

| Route | Output file | Status |
|---|---|---|
| `/verify-jvto` | `website/pages/verify-jvto/hub.md` | draft |
| `/verify-jvto/legal` | `website/pages/verify-jvto/legal.md` | draft |
| `/verify-jvto/police-safety` | `website/pages/verify-jvto/police-safety.md` | draft |
| `/verify-jvto/press-recognition` | `website/pages/verify-jvto/press-recognition.md` | draft |
| `/verify-jvto/history-artifacts` | `website/pages/verify-jvto/history-artifacts.md` | draft |

### Policy (4 pages)

| Route | Output file | Status |
|---|---|---|
| `/policy` | `website/pages/policy/hub.md` | draft |
| `/policy/booking-payment-cancellation` | `website/pages/policy/booking-payment-cancellation.md` | draft |
| `/policy/inclusions-exclusions` | `website/pages/policy/inclusions-exclusions.md` | draft |
| `/policy/privacy` | `website/pages/policy/privacy.md` | draft |

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
| `/travel-guide/best-time-to-visit` (expansion) | `wiki/website/operational-facts.md` | Seasonal weather data thin |

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

22 JSON-LD schema files in `output/website/schema/`, each with a `.receipt.md` verification file:

- **1 Organization schema** — homepage
- **16 TouristTrip schemas** — tour detail pages (12 Surabaya + 4 Bali)
- **5 TouristAttraction schemas** — destination pages

**Important**: Schema files contain trust signal values (reviewCount, ratingValue, NIB). These MUST match the canonical values in `wiki/credentials/trust-signals.md`. Current canonical values:
- Trustpilot: 4.8 / 51 reviews
- Google Maps: 4.9 / 123 reviews
- TripAdvisor: 4.95 / 21 reviews
- Cross-platform total: 195
- NIB: 1102230032918

---

## AEO Blocks (10 files)

Answer Engine Optimization snippets for AI search citation. Each file contains structured Q&A blocks optimized for LLM extraction.

| AEO file | Target page | Integration |
|---|---|---|
| `website/aeo/why-jvto.md` | `/why-jvto` | Overlay — add as hidden/structured data for AI crawlers |
| `website/aeo/policy-travel-guide.md` | `/policy` + `/travel-guide` | Overlay |
| `website/aeo/ijen.md` | `/destinations/ijen-crater` | Overlay |
| `website/aeo/bromo.md` | `/destinations/mount-bromo` | Overlay |
| `website/aeo/tumpak-sewu.md` | `/destinations/tumpak-sewu-waterfall` | Overlay |
| `website/aeo/madakaripura.md` | `/destinations/madakaripura-waterfall` | Overlay |
| `website/aeo/papuma.md` | `/destinations/papuma-beach` | Overlay |
| `website/aeo/bbksda-regulations-ijen.md` | `/travel-guide/bbksda-regulations-ijen` | Overlay |
| `website/aeo/bbksda-regulations-bromo.md` | `/travel-guide/bbksda-regulations-bromo` | Overlay |
| `website/aeo/ijen-gas-mask-equipment.md` | `/travel-guide/ijen-gas-mask-equipment` | Overlay |

---

## FAQ Blocks (8 files)

Destination-specific FAQ content for the `/travel-guide/faq` page and individual destination FAQs.

| FAQ file | Section |
|---|---|
| `website/faq/ijen.md` | Ijen-specific questions |
| `website/faq/bromo.md` | Bromo-specific questions |
| `website/faq/tumpak-sewu.md` | Tumpak Sewu questions |
| `website/faq/madakaripura.md` | Madakaripura questions |
| `website/faq/papuma.md` | Papuma questions |
| `website/faq/bbksda-regulations-ijen.md` | Ijen regulations |
| `website/faq/bbksda-regulations-bromo.md` | Bromo regulations |
| `website/faq/ijen-gas-mask-equipment.md` | Gas mask/equipment |

---

## SEO Quick Wins (from wiki/seo/seo-strategy.md)

Dev-actionable items. See `wiki/seo/seo-strategy.md` for full details.

| # | Action | Owner | Status |
|---|---|---|---|
| QW-1 | 301 redirects — legacy to SSOT routes | Dev | See `wiki/seo/redirect-map.md` |
| QW-3 | Fix meta description "From-surabaya" to "Surabaya" | Dev | Template bug |
| QW-5 | Organization/TravelAgency JSON-LD globally | Dev | Schema in `website/schema/homepage-organization-schema.json` |
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

**To publish a draft page**: Review against `wiki/website/brand-voice.md` voice guidelines + verify trust signal values against `wiki/credentials/trust-signals.md`.

---

## Key Wiki Reference Files for Dev

| Wiki page | What it provides |
|---|---|
| `wiki/seo/redirect-map.md` | 301 redirect mapping (legacy to new routes) |
| `wiki/seo/seo-strategy.md` | Keyword targets, title tags, quick wins |
| `wiki/website/schema-templates.md` | Schema.org field requirements per page type |
| `wiki/website/brand-voice.md` | Voice guidelines + meta description formula |
| `wiki/products/packages-full-pricing.md` | All pricing data (22 packages, all pax tiers) |
| `wiki/sources/wa-pro-crm-api.md` | WhatsApp API reference |
| `wiki/sources/gpx-destination-data.md` | Geo coordinates for all 5 destinations |
