---
type: ops
title: Compilation Profiles — Workflow 5
last_updated: 2026-05-26
sources: [llm-kb-tooling-guide, seo-audit-2026-05, guardian-authority-framework-2026-05]
owner: wiki-llm
stale_after_days: 120
---

# Compilation Profiles

*Workflow 5: state "Use the [profile] profile" before any content generation request.*

Each profile specifies which wiki pages to read, the output format, voice constraints, and the filename convention for saving to `output/`. Always cite the wiki source for every claim in the generated output.

---

## aeo

**Purpose:** Answer Engine Optimization — structured Q&A blocks for AI search ingestion.

**Draw from:** `website/aeo-claims`, `website/faq-master`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- One Q&A pair per block
- Question: ≤15 words, direct (e.g., "Is Java Volcano Tour Operator licensed?")
- Answer: ≤40 words, citable, starts with a direct claim
- Use the NLP atom structure from `website/aeo-claims` (C1–C9) as the template

**Forbidden:** hedging language ("may", "might", "could"), invented statistics, unsourced credential claims

**Output filename:** `output/aeo-YYYY-MM-DD-[topic].md`

---

## website-copy

**Purpose:** Hero paragraphs, section copy, and body text for javavolcano-touroperator.com.

**Draw from:** `website/copy-bank`, `website/brand-voice`, `destinations/[relevant]`, `products/packages-overview`

**Format:**
- Style A voice (direct, evidence-led — see `website/brand-voice` §Style-A)
- Hero: one punchy sentence + one credibility sentence
- Body: 2–4 sentences per paragraph, no bullet lists in hero sections
- All claims must trace to a wiki source; no invented statistics

**Forbidden:** invented statistics, passive voice in hero copy, "safety-focused guide" (use "Tourist Police officer"), superlatives without evidence

**Meta description**: Use the 3-part formula from [[website/brand-voice]] §Meta Description Formula: `[Format + Duration + Highlights] · [Differentiator] · [Trust signal or price hook]`. Max 160 characters. No first-person. For SEO-optimized title tags, see [[seo/seo-strategy]] §Title Tag Rewrites.

**Output filename:** `output/copy-YYYY-MM-DD-[page].md`

---

## faq

**Purpose:** FAQ pages — AEO-compatible, human-readable.

**Draw from:** `website/faq-master`, `products/packages-overview`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- H3 question heading
- Prose answer: 2–5 sentences, direct, citable
- Each answer ends with a trust signal where relevant (NIB, Trustpilot rating, doctor name)
- Answers must be self-contained — no reliance on adjacent questions for context

**Forbidden:** rhetorical questions, "great question!", invented pricing

**Output filename:** `output/faq-YYYY-MM-DD-[topic].md`

---

## social

**Purpose:** Social media captions, story copy, short-form posts.

**Draw from:** `website/copy-bank`, `reviews/trustpilot-compilation` (for verbatim quotes), `website/brand-voice`

**Format:**
- Style B voice (warmer, still direct — see `website/brand-voice` §Style-B)
- Quote-led: open with a verbatim review excerpt, cite reviewer name if given; or
- Claim-led: open with the strongest differentiator for this post's topic
- ≤280 characters for Twitter/X; ≤150 words for Instagram caption
- End with a call to action or question

**Forbidden:** invented quotes, hashtag spam (≤3 hashtags per post)

**Output filename:** `output/social-YYYY-MM-DD-[topic].md`

---

## schema

**Purpose:** Generate validated JSON-LD structured data blocks for use in the live website. The wiki is the source of truth for all numeric values — never hardcode from memory or prior examples.

**Draw from:** `credentials/legal-licenses`, `credentials/trust-signals` (§Schema Canonical Values), `website/faq-master`, `products/packages-overview`, `products/packages-full-pricing`, `reviews/trustpilot-compilation`, `reviews/google-tripadvisor-2026`

**Output types** (select the type requested):

| Type | Use for | Required draw-from fields |
|---|---|---|
| `Organization` / `TravelAgency` | Global header on every page | legal-licenses (NAP, NIB, HPWKI, ISIC), trust-signals (review counts, sameAs URLs) |
| `TouristTrip` + `AggregateRating` | Per tour page | packages-full-pricing (price, currency), faq-master (for FAQ block), trust-signals (reviewCount, ratingValue) |
| `FAQPage` | Per tour page or destination page | faq-master (draw relevant questions for that page) |
| `TouristAttraction` | Per destination page | destinations/{slug} (elevation, location, description) |
| `BreadcrumbList` | All sub-pages | sitemap-2026-05 (URL structure) |

**Verification step** (mandatory — run Grep before finalizing):

1. Extract every numeric value from the generated JSON-LD
2. Grep `wiki/credentials/trust-signals.md` §Schema Canonical Values for each numeric field
3. Confirm: `reviewCount` matches current canonical, `ratingValue` matches platform specified, credential IDs are exact
4. If any value doesn't match the wiki canonical: fix before writing output

**Forbidden:**
- Hardcoded `reviewCount` values not verified against [[reviews/trustpilot-compilation]]
- `ratingValue: 4.9` without specifying which platform (Google Maps is 4.90, Trustpilot is 4.8 — they are not interchangeable in schema)
- Placeholder URLs like `https://ahu.go.id/...` — use the verified URL from [[credentials/legal-licenses]]

**Currency format**: `"priceCurrency": "IDR"`, price in full integer (e.g. `2450000` not `2.45M`)

**Review count refresh trigger**: Schema output becomes stale whenever the health check detects new reviews. Re-generate affected schema files after any `review-feed` ingest.

**Output filename convention:** `output/schema/[page-slug]-schema.json`

---

## slide-deck

**Purpose:** Marp-compatible markdown slide decks for presentations or pitches.

**Draw from:** `wiki/overview` by default + any domain pages specified in the request

**Format:**
- Marp frontmatter: `marp: true`, `theme: default`
- One claim per slide — no bullet walls
- Each slide: headline + ≤30 words of supporting text + one evidence anchor (source, stat, or quote)
- Title slide and summary slide required in every deck

**Forbidden:** slides with >3 bullet points, unsourced claims, placeholder images

**Output filename:** `output/slides-YYYY-MM-DD-[topic].md`

---

## custom-tour-quote

**Purpose:** Build a custom tour cost estimate from rate cards.

**Input requirements:** Destination list, duration (days/nights), pax count, hotel tier preference, any special activity requests.

**Draw from:**
- [[finance/rate-cards]] — all cost components
- [[finance/package-costs]] — reference similar packages for sanity check
- [[products/packages-itineraries]] — route/timing templates
- [[destinations/*]] — activity options per destination

**Output format:** Itemized cost table → COGS → suggested selling price with markup.

**Output filename:** `output/finance/quote-{destination-slug}-{duration}.md`

**Verification:** Total COGS must equal sum of all line items. Cross-check vehicle/hotel rates against rate-cards.md.

---

## Definition of Done: Trust Fortress Ready

*From [[sources/guardian-authority-framework-2026-05]] §6. Quality gate for all content pages — applies across multiple profiles.*

A page is "Trust Fortress Ready" when it satisfies all 4 layers:

- [ ] **Human Layer**: Content is medically and operationally factual, uses "Safety-Led" brand voice ([[website/brand-voice]]), leads with a clear CTA
- [ ] **Trust Layer**: Page features "Trust Strip" (License number, Police-led badge) and links to the Forensic Verify cluster (/verify-jvto)
- [ ] **Machine Layer**: Schema.org markup (FAQPage/TourPackage/TouristAttraction) is nested, title/meta tags are locked, and an Answer Block is optimized for RAG extraction
- [ ] **Operational Layer**: Verified against SSOT for data drift — all numeric values match [[credentials/trust-signals]] §Schema Canonical Values
