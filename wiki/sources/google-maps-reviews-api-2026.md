---
type: source
title: Google Maps Reviews — API Export (123 reviews, 2026-05)
last_updated: 2026-05-26
sources: []
profile: review-feed
platform: google-maps
review_count: 123
computed_avg: 4.89
date_range: 2018-12-14 to 2026-05-22
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/index, wiki/people/crew-registry, wiki/products/packages-overview, wiki/reviews/google-tripadvisor-2026, wiki/reviews/review-patterns]
---

# Google Maps Reviews — API Export

*Source: Google Business Profile API export, 3 paginated JSON files (`raw/google review page [1-3].json`). 123 reviews with full comment text, owner replies, and reviewer media.*

**Key stats:**
- **123 reviews** | all 123 have owner replies
- **Rating distribution**: 115×5★, 5×4★, 2×3★, 0×2★, 1×1★
- **Computed average**: (575+20+6+0+1) / 123 = **4.89**
- **Date range**: 2018-12-14 → 2026-05-22
- **Google-displayed**: 4.9 (confirm from GMB dashboard — Google uses weighted formula)

> Supersedes DB-sourced data in [[sources/db-export-2026-05]] for Google review content. API data has full text + replies for all 123 vs DB excerpt-only for 92.

## Crew Distribution

All 14 existing crew members appear in reviews:

| Crew | Role | Reviews | 5★ |
|------|------|---------|-----|
| Gufron | Guide | 16 | 16 |
| Fredi | Driver | 15 | 13 |
| Rendi | Guide | 14 | 14 |
| Kiki | Guide | 12 | 12 |
| Boy | Guide | 9 | 7 |
| Yandi | Driver | 9 | 9 |
| Anjas | Guide | 8 | 7 |
| Yusuf | Driver | 7 | 7 |
| Pras | Driver | 6 | 6 |
| Fauzi | Guide | 5 | 5 |
| Holili | Driver | 4 | 4 |
| Taufik | Guide | 4 | 4 |
| Joyo | Driver | 3 | 3 |
| Dika | Driver | 2 | 2 |
| *(generic/no name)* | — | 43 | — |

**Total crew-tagged**: 114 mentions across 80 reviews. 43 reviews praise the tour without naming specific crew.

## Destination/Package Distribution

| Destination combo | Reviews | Likely package(s) |
|---|---|---|
| Bromo + Ijen | 16 | `bromo-madakaripura-ijen-3d2n`, `bali/bromo-ijen-3d2n` |
| Bromo + Ijen + Tumpak Sewu | 5 | `tumpak-sewu-bromo-ijen-4d3n` |
| Ijen only | 5 | `ijen-2d1n` |
| Bromo + Ijen + Madakaripura | 4 | `ijen-bromo-madakaripura-3d2n`, `ijen-bromo-madakaripura-4d3n` |
| Bromo + Ijen + Papuma + Tumpak Sewu | 4 | `ijen-papuma-tumpak-sewu-bromo-4d3n` |
| Bromo only | 4 | `bromo-1d1n`, `bromo-2d1n` |
| Mixed/unspecified | ~85 | Various or not identifiable from text |

## Non-5★ Review Summary

| Star | Reviewer | Date | Key feedback |
|---|---|---|---|
| 4★ | KX han | 2025-10-01 | Guide equipment issue (hiking poles not prepared) |
| 4★ | Rai Y | 2025-06-22 | Accommodation: thin walls (Baratha), no hot water (Joglo Kecombrang) |
| 4★ | Zohar Kritzer | 2024-02-24 | Hotel needs renovation (Grand Whiz), driver English limited |
| 4★ | Anna Saba | 2024-08-06 | Positive overall, no specific complaints |
| 4★ | Ayu Lestari | 2019-04-02 | No comment text |
| 3★ | Jacqueline Perdula | 2024-06-04 | Schedule too tight, <3h sleep, concerned about guide working conditions |
| 3★ | EL HIDAYAT | 2018-12-14 | No comment text |
| 1★ | Disna Sari | 2025-03-11 | "Unfriendly service" (Bahasa: "Pelayanan Tidak ramah") — single sentence |

## Extraction Notes

- All reviews include `reviewId`, `reviewer.displayName`, `starRating`, `comment`, `createTime`, `updateTime`
- Owner replies stored in `reviewReply.comment` with `reviewReplyState: APPROVED`
- Some reviews include `reviewMediaItems` with `thumbnailUrl` (guest-uploaded photos/videos)
- Several reviews are in Spanish, French, Dutch, Russian, Chinese — Google provides both original and translated text

-> [[reviews/google-tripadvisor-2026]] | -> [[people/crew-registry]] | -> [[products/packages-overview]] | -> [[credentials/trust-signals]]
