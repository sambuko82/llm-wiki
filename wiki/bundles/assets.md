---
type: ops
title: Asset Bundle — Index
last_updated: 2026-06-01
sources: [ssot-image-asset-map, google-profile-media-2026, gpx-destination-data]
owner: wiki-llm
stale_after_days: 120
bundle: assets
---

# Asset Bundle — Index

**Scope:** image proof, proof-file usage, page usage, alt text, visual evidence.

Thin navigation page. File ownership in -> [[ops/bundle-taxonomy]] §6. Pipeline status in -> [[ops/transformation-map]].

## Wiki sources

- -> [[sources/ssot-image-asset-map]] — 54 images across 14 groups
- -> [[sources/google-profile-media-2026]] — 87 GMB items (79 photos + 8 videos)
- -> [[sources/gpx-destination-data]] — 5 GPX recordings (Ijen, Bromo, Tumpak Sewu, Madakaripura, Papuma)
- -> [[people/crew-registry]] §"Image Assets" + §"KTA Card Images" — shared with People domain

## Raw sources

- `raw/jvto_image_asset_map.json`
- `raw/JVTO SSOT Image Asset Map.md`
- `raw/JVTO SSOT Image Inventory.md`
- `raw/google profile media.json` (also Review Bundle)
- `raw/Kawah_Ijen_Volcano.gpx`
- `raw/Gunung_Bromo.gpx`
- `raw/Air_Terjun_Tumpak_Sewu.gpx`
- `raw/Madakaripura_Waterfalls.gpx`
- `raw/Pantai_dan_Tanjung_Papuma.gpx`

## Wiki workspace

- `wiki/assets/` — empty scaffold created 2026-06-01 (Phase 2). Future home for asset-bundle-owned wiki pages (e.g. proof-file usage index, alt-text registry, page-usage map). Content migration deferred to a later sprint.

## Compiled output

**None yet.** Future path: `output/asset-bundle/`.

## Compiler

**Not built.** Planned: alt-text + page-usage validators feeding into image-proof JSON.

## Consumers (planned)

- jvto-web image refs (replace hardcoded asset paths)
- JSON-LD `ImageObject` schema
- AEO proof blocks (image-backed claims)
- Trust Bundle (visual evidence layer)

## Status

**FUTURE (P4-tie).** Sources catalogued in `wiki/sources/`; no dedicated wiki workspace populated; no compiler; no output.

## Pending follow-up (deferred)

- Move `wiki/sources/{ssot-image-asset-map,google-profile-media-2026,gpx-destination-data}.md` → `wiki/assets/` (content migration, deferred).
- `proof-file-usage.md`, `page-usage-map.md`, `alt-text-registry.md` (3 of the 8 deferred index/merge pages — separate sprint).
