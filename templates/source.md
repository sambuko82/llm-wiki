---
type: source
title: <!-- Source title with version/date, e.g., "JVTO_FINAL_CLEAN_SSOT.json v6.0 — Source Summary" -->
slug: <slug-used-in-other-pages-frontmatter-sources-field>
last_updated: YYYY-MM-DD
original_url: <!-- if web-clipped -->
ingested: YYYY-MM-DD
format: <!-- json | web-clip | gpx | pdf | other -->
location: raw/<filename>
sources: [<self-slug>]
# For sources used by many wiki pages, track which pages enrich from this source:
# pages_updated: [page1, page2, ...]
---

# Source: <Source Name>

## Metadata

- **File**: `raw/<filename>`
- **Size**: ~X KB
- **Format**: <!-- JSON / GPX / Markdown / PDF / etc. -->
- **Source URL** (if applicable): <!-- -->
- **Capture date**: <!-- -->
- **Capture method**: <!-- e.g., Obsidian Web Clipper, manual download, AllTrails export -->

## Role in Vault

<!-- Two roles to clarify: -->
<!-- 1. Is this source CANONICAL for structured facts? Or AUXILIARY (voice/tone exemplar, soft data)? -->
<!-- 2. What category of wiki pages enriches from this source? -->

## Authority Status

<!-- One sentence: e.g., "Treat as ground truth for X, Y, Z. For W, defer to [[sources/other]]." -->

## Structured Content Map

<!-- For multi-section sources (e.g., SSOT JSON with 13 domains): map each section to wiki areas. -->

| Wiki area | Source path / section | Key fields |
|---|---|---|
| <!-- [[destinations/*]] --> | <!-- e.g., §9_4 destination_entity_summaries --> | <!-- ai_summary, schema_type --> |

## Key Facts Extracted (verbatim)

<!-- Pull 5–15 ground-truth facts directly from the source. These become citations. -->

| Fact | Value | Source path |
|---|---|---|
| <!-- e.g., NIB --> | <!-- 1102230032918 --> | <!-- §1_1 --> |

## Voice / Style Patterns (if source is a voice exemplar)

<!-- Skip if not a voice source. Otherwise: 3–5 patterns observed. -->

## Internal Contradictions (flagged for source revision)

<!-- If the source contradicts itself across sections, flag with > Contradiction in section X vs Y -->

## Content Angles This Source Unlocks

<!-- 3–5 specific things future content production can extract from this source. -->

## Provenance Chain

`raw/<filename>` → this summary → downstream wiki pages (see `pages_updated` in frontmatter).
