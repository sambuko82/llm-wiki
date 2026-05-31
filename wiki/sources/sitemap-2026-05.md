---
type: source
title: JVTO Website Sitemap — May 2026
last_updated: 2026-05-12
sources: []
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/credentials/trust-signals, wiki/index, wiki/ops/package-readiness-compiler-spec, wiki/products/packages-overview, wiki/seo/redirect-map, wiki/website/schema-templates]
---

# JVTO Website Sitemap — May 2026

**File**: `raw/sitemap.xml`
**Format**: XML sitemap (Sitemaps Protocol 0.9)
**Extracted**: 2026-05-12
**Most recent lastmod in file**: 2026-05-12 (`/travel-guide/best-time-to-visit`)
**Total indexed URLs**: 44

---

## What This Source Is

Live XML sitemap from javavolcano-touroperator.com. Provides the authoritative inventory of all public-facing pages, their last-modified timestamps, change frequency, and crawl priority. Use this to resolve disputes about what pages exist and to identify the site's content architecture.

---

## Site Architecture (6 main sections)

| Section | Hub URL | Sub-pages | Notes |
|---|---|---|---|
| **Why JVTO** | `/why-jvto` | 5 | Includes community-standards |
| **Verify JVTO** | `/verify-jvto` | 4 | Trust verification hub |
| **Travel Guide** | `/travel-guide` | 8 | Operational guides |
| **Policy** | `/policy` | 3 | Booking, inclusions, privacy |
| **Destinations** | `/destinations` | 5 | All 5 destinations live |
| **Tours** | `/tours` | 16 tour pages | 12 Surabaya + 4 Bali |

Plus: `/` (homepage), `/contact`, `/blog`, `/isic/student-package`

---

## Live Tour Pages (16 confirmed)

### From Surabaya (12 pages)

| Slug | Duration | lastmod |
|---|---|---|
| `bromo-1d1n` | 1D1N | 2026-04-13 |
| `bromo-2d1n` | 2D1N | 2026-04-13 |
| `ijen-2d1n` | 2D1N | 2026-04-13 |
| `ijen-bromo-madakaripura-3d2n` | 3D2N | 2026-04-24 |
| `bromo-madakaripura-ijen-3d2n` | 3D2N | 2026-04-24 |
| `taman-safari-prigen-bromo-madakaripura-3d2n` | 3D2N | 2026-04-13 |
| `ijen-papuma-tumpak-sewu-bromo-4d3n` | 4D3N | 2026-04-24 |
| `ijen-bromo-madakaripura-4d3n` | 4D3N | 2026-04-24 |
| `tumpak-sewu-bromo-ijen-4d3n` | 4D3N | 2026-04-13 |
| `ijen-bromo-madakaripura-malang-5d4n` | 5D4N | 2026-04-13 |
| `ijen-papuma-tumpak-sewu-bromo-5d4n` | 5D4N | 2026-04-24 |
| `ijen-papuma-tumpak-sewu-bromo-malang-6d5n` | 6D5N | 2026-04-13 |

### From Bali (4 pages)

| Slug | Duration | lastmod |
|---|---|---|
| `bromo-ijen-3d2n` | 3D2N | 2026-03-31 |
| `ijen-bromo-madakaripura-3d2n` | 3D2N | 2026-03-31 |
| `ijen-papuma-tumpak-sewu-bromo-4d3n` | 4D3N | 2026-03-31 |
| `ijen-papuma-tumpak-sewu-bromo-5d4n` | 5D4N | 2026-03-31 |

**Package count resolution**: 12 Surabaya + 4 Bali = **16 live tour pages**. This independently corroborates SSOT §9_1 and §13 (which said 16 = 12+4), resolving the contradiction against SSOT §meta/§6_1 (which said 15 = 11+4). The 12th Surabaya package is `taman-safari-prigen-bromo-madakaripura-3d2n` (Taman Safari Prigen — a wildlife/safari park in Prigen, East Java).

---

## Notable Pages by Section

### `/verify-jvto` — Trust Verification Hub

Dedicated section for prospect trust-building:

| Sub-page | URL slug | Purpose (inferred) |
|---|---|---|
| Legal | `/verify-jvto/legal` | NIB, TDUP, KBLI, license verification |
| Press Recognition | `/verify-jvto/press-recognition` | Media mentions, guidebook coverage |
| History & Artifacts | `/verify-jvto/history-artifacts` | Founding story, historical evidence |
| Police Safety | `/verify-jvto/police-safety` | POLPAR credentials, SPRIN documentation |

All lastmod 2026-05-08. -> [[credentials/trust-signals]]

### `/isic/student-package`

ISIC student package has its own dedicated hub page at `/isic/student-package` — separate from the `/tours/` path hierarchy. Confirms ISIC is positioned as a distinct product line, not a sub-variant of the standard tour catalog. lastmod 2026-05-08.

### `/why-jvto/community-standards`

Dedicated community standards page. Content not ingested; page exists and was last updated 2026-03-19.

### `/travel-guide/best-time-to-visit`

Most recently modified page in the sitemap: lastmod **2026-05-12** (today). Updated same day as this ingest — treat as freshest content on site.

---

## Priority and Change Frequency Signals

| Priority | Change freq | URLs |
|---|---|---|
| 1.0 | yearly | Homepage |
| 0.9 | weekly | `/destinations`, `/tours`, `/tours/from-surabaya`, `/tours/from-bali` |
| 0.8 | weekly | All 16 individual tour pages |
| 0.8 | monthly | All other pages (why-jvto, verify-jvto, travel-guide, policy, destinations sub-pages) |
| 0.7 | weekly | Bali tour pages only |

Destinations hub and tours hub are the site's highest-priority commercial pages after the homepage.

---

## Destination Slugs (canonical on-site)

| Destination | Site URL slug | Wiki page |
|---|---|---|
| Kawah Ijen | `ijen-crater` | [[destinations/kawah-ijen]] |
| Mount Bromo | `mount-bromo` | [[destinations/mount-bromo]] |
| Madakaripura | `madakaripura-waterfall` | [[destinations/madakaripura]] |
| Tumpak Sewu | `tumpak-sewu-waterfall` | [[destinations/tumpak-sewu]] |
| Papuma Beach | `papuma-beach` | [[destinations/papuma-beach]] |

Note: site uses `ijen-crater` not `kawah-ijen` as URL slug.

---

## Key Facts for Wiki Use

- **16 live tour pages confirmed** — sitemap resolves package count contradiction in favor of SSOT §9_1/§13
- **`taman-safari-prigen-bromo-madakaripura-3d2n`** is a live Surabaya package (Taman Safari Prigen + Bromo + Madakaripura, 3D2N)
- **Verify JVTO** is a dedicated trust verification section (4 sub-pages) — signals website's transparency-first positioning
- **ISIC** has its own landing page separate from /tours/ — distinct product positioning
- **Blog** exists at `/blog`
- **`best-time-to-visit`** was updated 2026-05-12 — freshest page on site at time of ingest
