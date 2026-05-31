---
type: source
title: Google Business Profile Media — 87 Items (2026-05)
last_updated: 2026-05-26
sources: []
profile: custom
platform: google-maps
media_count: 87
photos: 79
videos: 8
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/index]
---

# Google Business Profile Media — 87 Items

*Source: Google Business Profile API export (`raw/google profile media.json`).*

**87 media items**: 79 PHOTO + 8 VIDEO
**Categories**: 85 ADDITIONAL + 1 COVER + 1 PROFILE
**Date range**: earliest timestamps show 1970-01-01 (epoch default for older uploads) → 2026-03-08

All items are owner-uploaded (not guest photos). Guest review photos live in the review JSON files — see [[sources/google-maps-reviews-api-2026]].

## Relationship to Existing Image Assets

- [[sources/ssot-image-asset-map]] catalogs 54 images on javavolcano-touroperator.com (crew portraits, field ops, credentials, health screening, heritage)
- This GMB media set is the Google-side catalog — some overlap expected but URLs differ (lh3.googleusercontent.com vs javavolcano-touroperator.com/uploads/)
- GMB photos influence Google Maps listing appearance and local SEO

## Extraction Notes

- Each item has `name`, `mediaFormat`, `googleUrl` (full-size), `thumbnailUrl`, `createTime`, `dimensions`
- `locationAssociation.category`: ADDITIONAL (standard), COVER (listing banner), PROFILE (avatar)
- Video items include both `thumbnailUrl` and playback URL

-> [[sources/ssot-image-asset-map]] | -> [[sources/google-maps-reviews-api-2026]]
