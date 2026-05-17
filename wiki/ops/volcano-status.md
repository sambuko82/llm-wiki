---
type: ops
title: Volcano Status Tracker
last_updated: 2026-05-17
sources: [magma-bromo-2026-05-16, magma-ijen-2026-05-16]
---

# Volcano Status Tracker

*Updated each time a new MAGMA Indonesia daily activity report is ingested (Workflow 4, `magma-report` profile). Always check this page before generating output that references crater access, tour operations, or closures.*

**Source**: MAGMA Indonesia (magma.esdm.go.id) — official Pusat Vulkanologi dan Mitigasi Bencana Geologi (PVMBG), ESDM.

---

## Current Status — As of 2026-05-16

| Volcano | Alert Level | JVTO Operational Status | Exclusion Zone | Last report |
|---|---|---|---|---|
| **Gunung Bromo** | **Level II — Waspada** | ⚠️ Restricted — see note below | 1 km radius from active crater | 2026-05-16 (00:00–24:00 WIB) |
| **Kawah Ijen** | **Level I — Normal** | ✅ Open — standard operations | None (500 m camping restriction only) | 2026-05-16 (00:00–24:00 WIB) |

---

## Gunung Bromo — Detail (2026-05-16)

**Alert level**: Level II Waspada (Elevated)  
**Source**: https://magma.esdm.go.id/v1/gunung-api/laporan/315742  
**Visual**: White gas/steam, thin to thick, 50–600 m from summit. Clear to rainy. Light wind SE/S/SW/W.  
**Seismicity**: 3× far tectonic earthquakes (amp 6–19 mm, S-P 22–27 s, duration 60–110 s); 1× continuous tremor (amp 0.5–1 mm, dominant 0.5 mm).  
**VONA**: Not issued (Level II does not trigger VONA by default).

**Official recommendations**:
1. Do not enter within 1 km radius of the active crater of Gunung Bromo.
2. Beware of sudden phreatic eruptions that occur without prior volcanic symptoms (community, traders, tourists, climbers, and tour operators).

**JVTO operational implication**:
- Penanjakan sunrise viewpoint (~5 km from crater) is outside the exclusion zone — accessible as normal.
- Caldera floor descent and crater rim approach are restricted (within 1 km). Jeep ride to the crater base area: confirm with BBKSDA/park authority whether the standard parking area falls within the exclusion arc.
- Plan-B framework activates for any itinerary segment within the exclusion zone.
- Any output/ file describing "visiting the crater lip" or "walking to the crater" for Bromo should be flagged as potentially stale until Level II is resolved.

---

## Kawah Ijen — Detail (2026-05-16)

**Alert level**: Level I Normal  
**Source**: https://magma.esdm.go.id/v1/gunung-api/laporan/315786  
**Visual**: White thin gas/steam, 50–100 m from summit. Cloudy to rainy. Light eastward wind.  
**Temperature**: 22–26°C, humidity 62–77%.  
**Seismicity**: 2× shallow volcanic earthquakes (amp 3–4 mm, duration 8–10 s); 1× local tectonic (amp 4 mm, S-P 10 s, duration 40 s); 3× far tectonic (amp 8–20 mm, S-P 25–36 s, duration 86–132 s); 1× continuous tremor (amp 0.5–2 mm, dominant 1 mm).

**Official recommendations**:
1. Do not descend to or approach the Kawah Ijen crater lake floor.
2. Do not overnight/camp within 500 m of the crater.
3. Beware of CO2 gas flow along the Banyupait–Banyuputih river.
4. Beware of toxic gas around the crater area.

**JVTO operational implication**:
- Level I Normal — standard JVTO Ijen operations proceed.
- Continuous tremor (dominant 1 mm) and gas advisory are the permanent hydrothermal baseline at Ijen — these do NOT signal elevated risk; they are normal conditions.
- BBKSDA SE.1658/KSA.9/2024 health-screening coordination applies regardless of alert level (rule is regulatory, not alert-triggered).
- Gas masks provided by JVTO as standard inclusion.
- Sulfur miner operations unaffected.

---

## Alert Level Reference

| Level | Indonesian term | JVTO operational status | Standard action |
|---|---|---|---|
| Level I | Normal | ✅ Standard operations | No change |
| Level II | Waspada | ⚠️ Monitor + Plan-B ready | Communicate exclusion zone to guests; activate Plan-B for affected segments |
| Level III | Siaga | ❌ Tours suspended to restricted zone | Contact all upcoming guests; issue Travel Credit per policy |
| Level IV | Awas | ❌ Tours suspended — full area | Issue Travel Credits; await PVMBG all-clear |

---

## Update Instructions

When a new MAGMA daily report is ingested:
1. Update the Current Status table above (date, level, status, exclusion zone)
2. Replace the detail section for that volcano
3. Update `wiki/destinations/[volcano].md` → `## Current Status` section
4. Update `wiki/content/operational-facts.md` → alert level fields
5. If level changes (up or down), grep `output/` for the volcano name and flag affected files

-> [[destinations/kawah-ijen]] | -> [[destinations/mount-bromo]] | -> [[content/operational-facts]] | -> [[ops/ingestion-profiles]]
