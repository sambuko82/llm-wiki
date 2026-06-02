---
type: receipt
title: evidenceRegistry.ts — Generation + Deployment Receipt
generated: 2026-05-27
generator: Cowork (JVTO Business Exposure Engine mode)
output_file: F:\jvto-web\src\data\evidenceRegistry.ts
reference_copy: (this receipt is the wiki-side reference)
operating_principle: JVTO Business Exposure Engine — owner-approved data is LOCKED, not audited
---

# evidenceRegistry.ts — Receipt

## What was produced

**File**: `F:\jvto-web\src\data\evidenceRegistry.ts`
**Size**: ~410 lines, ~16 KB
**Type**: TypeScript module exporting typed evidence array + helper functions

## What it contains

20 evidence items across 7 categories, each with: ID, title, description, identifier (where applicable), date, authority, SHA-256 hash (where applicable), file URLs, external verification URLs, supported claims (C1-C9), wiki source page, recommended placements, costly-signal weight.

| Category | Count | Examples |
|---|---|---|
| legal | 3 | NIB, TDUP, AHU |
| police | 2 | SPRIN POLPAR, SPRIN WAL-TRAVEL |
| medical | 2 | Dr. Irwandanu SIP, BBKSDA SE.1658 |
| partners | 3 | HPWKI, INDECON, ISIC |
| history | 3 | Booking.com 2015 award + shipping label, Stefan Loose |
| press | 4 | Detik, Radar Jember ×2, BBKSDA |
| reviews | 3 | Google, Trustpilot, TripAdvisor |

## Helpers exported

- `evidenceByCategory(category)` — filter by category
- `evidenceByClaim(claim)` — filter by supported claim (C1-C9)
- `evidenceByPlacement(placement)` — filter by recommended placement
- `topEvidenceForClaim(claim)` — highest costly-signal-weight evidence for a claim (for AuthorityShield)
- `evidenceStats()` — aggregate stats (total, with hash, by category, under reconciliation)

## How it feeds the site

| Component / page | Reads via |
|---|---|
| `/verify-jvto` hub | `evidenceByPlacement('verify-jvto')` |
| `/verify-jvto/legal` | `evidenceByCategory('legal')` |
| `/verify-jvto/police-safety` | `evidenceByCategory('police')` |
| `/verify-jvto/history-artifacts` | `evidenceByCategory('history')` + select press |
| `/verify-jvto/press-recognition` | `evidenceByCategory('press')` |
| AuthorityShield component | `topEvidenceForClaim('C1')` or `topEvidenceForClaim('C5')` |
| ForensicGallery component | `evidenceRegistry` (all items with hash + previewUrl) |
| Per-package trust block | `evidenceByPlacement('package')` |
| Homepage trust strip | `evidenceByPlacement('homepage')` |
| Crew page trust badges | `evidenceByPlacement('team')` |

## Owner-approved LOCKED items (Business Exposure Engine)

These items are **locked business assets** as of 2026-05-27 — internal audit/reconciliation does NOT apply:

| Item | Locked data |
|---|---|
| Stefan Loose guidebook | ISBN `978-3-7701-7881-0`, published `2018-07-05`, publisher DuMont Reiseverlag, 4th Edition, page 287, 772 pages, German |
| NIB | `1102230032918` (canonical) — legacy 0220001393513 not in registry |
| Madakaripura framing | "tallest waterfall in Java" approved for public use |

Wiki note added at `wiki/credentials/press-coverage.md` documenting the lock.

## Schema integration

The existing `src/lib/schemas/entityGraph.ts` already has Stefan Loose as `subjectOf > Book` with the correct ISBN at lines 124-153. No schema upgrade required.

The Booking.com 2015 award is in the `award` array at entityGraph.ts:60. Strategic consideration (not executed): per the SEO doc, a separate `Booking.com Traveller Review Award 2025` may exist as a fresh award eligible for current data — owner to confirm before adding.

## Voice invariant compliance

| Rule | Compliance |
|---|---|
| No "blue fire guaranteed" | ✅ Not in file |
| No "mandatory health screening" without qualifier | ✅ BBKSDA SE.1658 entry uses "conditional" framing |
| No fabricated dates | ✅ All dates trace to wiki sources |
| Founder framing | ✅ "active Tourist Police officer" used in police entries |
| Price format IDR | N/A (no prices in this file) |

## Next concrete exposure deliverables (queued, not executed)

Based on Business Exposure Engine principle — exposure tools that take owner-locked data and project it externally:

1. **Booking.com Traveller Review Award 2025 schema** — separate from 2015 plaque; requires owner confirmation on whether JVTO holds the 2025 award
2. **Authority Shield component refresh** — point existing `src/components/website/AuthorityShield.tsx` + `src/components/why/AuthorityShield.tsx` at `topEvidenceForClaim('C1')` instead of hardcoded values
3. **ForensicGallery wiring** — feed component from `evidenceRegistry` so /verify-jvto pages render dynamically
4. **/verify-jvto/legal page content** — pulls from `evidenceByCategory('legal')`, displays cards with SHA-256 + external verification links
5. **Crew Person schema** — per SEO doc, Person + jobTitle + knowsAbout for top crew (Gufron senior volcano guide, etc.) to expose Expertise signals
6. **5 blog content priorities** from the user's Tab 3 (Blog & Ads Support Board) — each blog has customer fear + JVTO advantage + CTA tied to a package/claim

## Files in this exposure cycle (today)

| Path | Status |
|---|---|
| `F:\jvto-web\public\llms.txt` | Deployed (overwrote outdated SSOT v3 version, backup at .bak.2026-05-27) |
| `F:\jvto-web\public\llms-full.txt` | Deployed (new) |
| `F:\jvto-web\src\data\evidenceRegistry.ts` | Deployed (new) |
| `E:\...\llm-wiki\wiki\credentials\press-coverage.md` | Updated with owner-locked notice |
| `E:\...\llm-wiki\output\website\llms.txt` | Reference (matches deployed) |
| `E:\...\llm-wiki\output\website\llms-full.txt` | Reference (matches deployed) |
| `E:\...\llm-wiki\output\website\2026-05-27-llms-files-receipt.md` | Provenance receipt |
| `E:\...\llm-wiki\output\website\2026-05-27-evidence-registry-receipt.md` | This file |

---

*Receipt end. Exposure cycle 1 of JVTO Business Exposure Engine in progress.*
