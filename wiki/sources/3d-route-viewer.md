---
type: source
title: "3D Route Viewer — Mapbox Interactive Fly-Through (2026-05)"
last_updated: 2026-05-24
source_files:
  - F:/jvto-web/public/routes/index.json
  - F:/jvto-web/public/routes/ijen-crater.geojson
  - F:/jvto-web/public/routes/mount-bromo.geojson
  - F:/jvto-web/public/routes/madakaripura-waterfall.geojson
  - F:/jvto-web/public/routes/papuma-beach.geojson
  - F:/jvto-web/public/routes/tumpak-sewu-waterfall.geojson
feature_url_pattern: /3d/{slug}
branch: design/sam
component: src/components/Route3DViewer.tsx
page: src/app/3d/[slug]/page.tsx
---

# 3D Route Viewer — Mapbox Interactive Fly-Through

Interactive 3D route viewer built for `jvto-web` (Next.js 16). Users can fly through all 5 destinations in a cinematic Mapbox 3D animation. Built on `design/sam` branch, committed 2026-05-24.

## What It Is

A fullscreen page at `/3d/{slug}` for each destination. Features:

- **Mapbox GL JS v3** — satellite-streets-v12 style, raster-dem terrain (mapbox.mapbox-terrain-dem-v1), terrain exaggeration 1.6×, fog
- **Cinematic fly-through** — third-person follow camera (250 m offset behind head), `easeTo` camera smoothing at 30 fps, exponential bearing smoothing (lerp 0.12), pitch easing 60°–78° based on terrain gradient
- **Progress-aware stats card** — live km and elevation gain update during playback (AllTrails-style), LIVE badge while playing
- **SVG elevation chart** — hover-scrub synced to map marker, blue gradient area with darker "done" overlay
- **GeoJSON trail layers** — `route` (full green) + `route-done` (blue progress slice), updated 60 fps

## Feature URLs

| Destination | URL |
|---|---|
| Kawah Ijen (Ijen Crater) | /3d/ijen-crater |
| Mount Bromo | /3d/mount-bromo |
| Madakaripura Waterfall | /3d/madakaripura-waterfall |
| Papuma Beach | /3d/papuma-beach |
| Tumpak Sewu Waterfall | /3d/tumpak-sewu-waterfall |

## Route Statistics

Data from `F:/jvto-web/public/routes/index.json` — GeoJSON processed from AllTrails GPX files (same source as `raw/*.gpx` in this wiki).

| Slug | Length km | Elev Gain m | Elev Min m | Elev Max m | GPX Points |
|---|---|---|---|---|---|
| ijen-crater | 8.98 | 797 | 1,872 | 2,379 | 673 |
| mount-bromo | 5.31 | 351 | 2,120 | 2,277 | 809 |
| madakaripura-waterfall | 3.71 | 492 | 555 | 824 | 417 |
| papuma-beach | 4.40 | 335 | 0 | 86 | 169 |
| tumpak-sewu-waterfall | 0.72 | 63 | 508 | 568 | 125 |

These numbers match the AllTrails GPX summaries in each destination's `## Trail Data` section — the GeoJSON is derived from the same raw files.

## Tech Stack

- `src/components/Route3DViewer.tsx` — main component (client, fullscreen + embedded modes)
- `src/components/ElevationChart.tsx` — hand-rolled SVG chart (Haversine distance, ResizeObserver, pointer events)
- `src/app/3d/[slug]/page.tsx` — RSC page outside `(website)` route group (true fullscreen, no Navbar/Footer)
- `@turf/turf` — lineSliceAlong, along, bearing, destination, bbox, length
- `mapbox-gl` — Mapbox GL JS v3

## Data Provenance

- GPX source: AllTrails community-recorded trails (same as `raw/*.gpx` in llm-wiki)
- Processing: GPX → GeoJSON (coordinates: `[lon, lat, elevation_m]`) stored in `F:/jvto-web/public/routes/`
- `index.json`: pre-computed stats (bbox, start/end coords, point count, all elevation metrics)
- Each GeoJSON: one FeatureCollection with one LineString Feature + name/slug/description/source properties

## Viewer Entry Points

The `/3d/[slug]` pages are pre-rendered by `generateStaticParams` (all 5 slugs at build time). Entry via:

- "View 3D Route" CTA pill on destination detail pages (wired to destinations with GPX route data)
- Direct URL

-> [[destinations/kawah-ijen]] | -> [[destinations/mount-bromo]] | -> [[destinations/madakaripura]] | -> [[destinations/papuma-beach]] | -> [[destinations/tumpak-sewu]]
