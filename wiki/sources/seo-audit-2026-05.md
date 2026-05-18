---
type: source
title: JVTO SEO Audit — May 2026
last_updated: 2026-05-17
sources: []
---

# SEO Audit — May 2026

**Document**: JVTO SEO Audit Full Site Review  
**Date**: 2026-05-17  
**Mode**: Whitehat organic growth audit  
**Data sources**: Direct site fetch · Live SERP analysis · Competitor mapping  
**Limitation**: Ahrefs MCP blocked at current plan tier — keyword volumes are estimated, not measured. See Appendix A of audit for detail.

---

## Audit Verdict

**Strong foundation, critical execution issues holding back rankings.**

JVTO has best-in-class trust and content assets (police credentials, verified reviews, structured destination data). The primary leak is the **legacy Laravel URL structure still indexed alongside the new Next.js SSOT routing** — Google sees two competing JVTO sites at the same domain.

---

## Critical Technical Findings

| # | Issue | Severity | Fix owner |
|---|---|---|---|
| T1 | Dual-URL problem: legacy Laravel routes (`/about`, `/faq`, `/reviews`, `/packages/surabaya/3d2n/{N}`, etc.) indexed alongside new SSOT routes | **Critical** | Dev (Next.js middleware 301 redirects) |
| T2 | `legacy.javavolcano-touroperator.com` subdomain serving images — extra DNS lookup, crawl confusion | High | Dev (migrate images to main domain) |
| T3 | `java-tour.com` listed on Facebook — potential content cannibalization | High | Sam (decision: redirect or canonical) |
| T4 | Footer destination links all → `/destinations` hub instead of `/destinations/{slug}` — link equity not flowing to destination pages | **Critical** | Dev (1 hour fix) |
| T5 | Meta description template literal: "From-surabaya" not humanized on `/tours/from-surabaya`, `/tours/from-bali`, `/packages/yogyakarta` | High | Dev (30 min fix) |
| T6 | No FAQPage schema — "Quick Answers" sections on tour pages not marked up | High | Dev (2 hours) |
| T7 | No TouristTrip schema on tour pages | High | Dev (4 hours) |
| T8 | Organization/TravelAgency JSON-LD incomplete — no ISIC, INDECON, HPWKI identifiers | High | Dev (2 hours) |

---

## On-Page Positives (already working)

Canonical tags ✅ · Open Graph ✅ · Twitter cards ✅ · robots meta ✅ · Title length ✅ · H1 uniqueness ✅ · HTTPS ✅ · Mobile viewport ✅ · WebP images ✅ · Next.js image optimization ✅

---

## Keyword Findings

### JVTO already ranks #1 for:
- "tourist police bromo tour"
- "licensed bromo tour operator indonesia tourist police"

**These validate the C1/C5 content strategy. Scale this pattern.**

### Priority keyword targets

See [[ops/seo-strategy]] for the full 15-term table with difficulty ratings. High-priority uncontested terms:
- `ijen health certificate` — Low difficulty, JVTO most authoritative
- `BBKSDA SE 1658` — Very Low difficulty, JVTO only source
- `madakaripura waterfall tour` — Medium difficulty, strong opportunity
- `bromo ijen status today` — Low difficulty, update-frequency moat

### Competitive positioning

OTAs (Klook, GetYourGuide, Viator, Tripadvisor) + aged-domain operators (bromotour.com since 1998, tourmountbromo.com 10+ years) own the high-volume commercial SERPs. Head-on competition is 12-18 months. Fast wins: long-tail + branded + intent-rich queries. See [[ops/competitors]] for full tier map.

---

## Schema Requirements (per page type)

| Page type | Required JSON-LD |
|---|---|
| All pages | `Organization` / `TravelAgency` (global) |
| `/tours/{slug}` | `TouristTrip` + `FAQPage` + `AggregateRating` + `BreadcrumbList` |
| `/destinations/{slug}` | `TouristAttraction` + `BreadcrumbList` |
| `/why-jvto/reviews` | `Organization` with `aggregateRating` + `review` array |
| `/travel-guide/{slug}` | `Article` + `FAQPage` (if applicable) |
| `/verify-jvto/*` | `Organization` with `identifier` (NIB, TDUP) + `memberOf` (HPWKI, INDECON) |

Full schema spec: [[content/schema-templates]] (to be created).

---

## Data Discrepancies Found (audit vs wiki canonical)

| Discrepancy | Audit value | Wiki canonical | Action |
|---|---|---|---|
| D1: TouristTrip `reviewCount` | `47` (stale) | `51` per [[reviews/trustpilot-compilation]] (verified 2026-05-09) | Always pull from wiki, never hardcode |
| D2: Organization `ratingValue` | `4.9` (ambiguous — no platform stated) | Trustpilot: 4.8 · Google: 4.90 · TripAdvisor: 4.95 | Declare platform in schema; see schema canonical values in [[credentials/trust-signals]] |
| D3: Package count in title tag suggestion | `16` | Wiki canonical 15 (SSOT §meta), sitemap confirms 16 live | Resolve in favor of 16 (sitemap-verified) |
| D4: INDECON URL in sameAs | `https://ahu.go.id/...` (placeholder) | Live URL confirmed: https://www.indecon.id/spotlight-networks/java-volcano-tour-operator | Use wiki value |
| D5: Organization `reviewCount: 164` | 164 (cross-platform total) | 51 TP + 92 Google + 21 TA = 164 ✅ | Correct — but this number drifts; schema must be dynamic or regularly regenerated |

---

## Content Gap Map

Full silo + gap table: [[ops/seo-strategy]].

### Silo 3 (Regulatory + Safety — uncontested moat):
- Most pages already have wiki source material
- `bromo-ijen-status-today` needs a replacement live source — MAGMA feed not active; consider PVMBG/BBKSDA direct monitoring
- `yadnya-kasada-2026` and `permit-requirements-east-java` still need source ingest

### Silo 4 (Pre-purchase planning):
- `bromo-vs-ijen-comparison` fully sourceable from existing wiki pages
- `what-to-pack-bromo-ijen` fully sourceable from [[sources/jvto-travel-guide-en]] §6
- Geographic landing pages need new source material (flight data, local logistics per market)

---

## Off-Page / Backlink Notes

- INDECON spotlight URL confirmed live with backlink ([[credentials/legal-licenses]])
- Detik.com press coverage is the highest-authority external link — pursue more
- ISIC.org partner page at isic.org/discounts/?providerId=259268 — verify JVTO is listed with backlink
- Government domains (.go.id) are the strongest backlink opportunity — BBKSDA, POLRI institutional features

---

## Quick Wins Not in Wiki Scope (Dev Handoffs)

See [[ops/redirect-map]] for the 301 redirect table. All other QW items (footer fix, meta description template, schema embed, GSC submission) are `jvto-web` tasks.

---

## Source Status

This source summary was created from the uploaded audit document. The audit itself lacked Ahrefs data; exact keyword volumes are estimated. When Ahrefs MCP access is restored, this audit's estimates can be quantified. Key operational guidance (redirect map, schema spec, competitor table, content silo map) is valid regardless of volume precision.

-> [[ops/seo-strategy]] | -> [[ops/competitors]] | -> [[ops/redirect-map]] | -> [[ops/compilation-profiles]] | -> [[credentials/trust-signals]]
