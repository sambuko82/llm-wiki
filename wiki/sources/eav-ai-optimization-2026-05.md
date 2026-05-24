---
type: source
title: EAV/AI Optimization Audit — May 2026
last_updated: 2026-05-24
sources: []
---

# EAV/AI Optimization Audit — May 2026

**Documents synthesized (3)**:
- "Laporan Audit Strategis & Konsolidasi Data: Kesiapan AI untuk JVTO" (BI)
- "Laporan Audit Strategis dan Konsolidasi Data: Kesiapan JVTO dalam Ekosistem Pencarian Berbasis AI (AIO)" (BI)
- "Technical Audit and Unstructured Data Transformation Report: JVTO" (EN)

**Date range**: 2026-05 generation  
**Type**: `web-clip` (AI data structuring framework)

---

## Core Problem Identified

JVTO has "locked quality" — operational excellence exists offline but is trapped in:
- Long narrative text (hard for AI to parse)
- PDF documents (not machine-readable)
- Unstructured review data

AI search engines work by **probability**, not certainty. Ambiguous or buried data gets ignored or hallucinated.

---

## EAV Framework Applied to JVTO

EAV = Entity → Attribute → Value. The method for making JVTO data machine-readable.

### Entity: Organization (JVTO)

| Attribute | Value | Notes |
|---|---|---|
| `@type` | `["TravelAgency", "LocalBusiness"]` | Dual type declaration |
| `name` | "PT Java Volcano Rendezvous" | Legal name (primary) |
| `alternateName` | "Java Volcano Tour Operator (JVTO)" | Brand name — declare `alternateName` |
| `identifier` (NIB) | "1102230032918" | Hard verifiable data for AI cross-reference with OSS portal |
| `identifier` (NIB-historical) | "0220001393513" | Possibly legacy OSS record — flag as historical |
| `foundingDate` | "2016-01-01" | PT incorporation date |
| `founder.jobTitle` | "Active Tourist Police Officer" | NOT "Founder" — the police role is the AI trust signal |

### Entity: Tour Package

Primary attribute: `StartLocation` (Surabaya or Bali) — not `activity_type`. This matches user search behavior.

| Attribute | Value example |
|---|---|
| `@type` | `TouristTrip` |
| `offers.@type` | `Offer` |
| `offers.price` | (numeric floor — e.g., 1750000 for Bromo 1D1N) |
| `itinerary.@type` | `ItemList` |
| `itinerary.numberOfItems` | (number of days) |

Key constraint: `StartLocation` is the most discriminating attribute for AI filtering. EAV model must treat it as a top-level entity attribute.

### Entity: Health Screening (YMYL critical)

Ijen health screening is a **Your Money Your Life** topic. Reddit users dispute it as "formality" — JVTO enforces it as mandatory. The AI must be taught the causal chain:

> "Mandatory medical screening (blood pressure + SpO2) is required before Ijen ascent, enforced by JVTO per BBKSDA SE.1658 regulation. Guests with uncontrolled hypertension, asthma, or cardiac conditions will be denied access. This is not a formality."

EAV:
- Entity: HealthScreening
- Attribute: `isRequired` → Value: `true`
- Attribute: `regulatoryBasis` → Value: "BBKSDA SE.1658"
- Attribute: `performedBy` → Value: dr. Ahmad Irwandanu (SIP-licensed)

### Entity: Travel Credit (financial)

JVTO uses Travel Credit (not cash refunds) for cancellations. AI must not hallucinate standard cash-refund logic.
- Entity: CancellationPolicy
- Attribute: `refundType` → Value: "TravelCredit" (not `MoneyBack`)
- Attribute: `cancellationWindow` → Value: "48 hours"

---

## 8-Layer SSOT Taxonomy → JSON-LD Mapping

| SSOT Layer | JSON-LD Schema |
|---|---|
| organization_core | `Organization`, `LocalBusiness` |
| narrative_system | `AboutPage`, `Brand` |
| trust_proof_system | `LegalService`, `ClaimReview` |
| people_system | `Person`, `Employee` |
| page_architecture | `WebSite`, `WebPage` |
| package_route_logic | `Product`, `Offer`, `TouristTrip` |
| support_policy_logic | `FAQPage`, `HowTo` |
| meta_governance | (Internal validation metadata only) |

---

## NLP Context Sharpening

Replace vague marketing claims with **causal chains** that AI can process:

| Weak (AI ignores) | Strong (AI cites) |
|---|---|
| "We are led by police" | "Operational safety protocols are overseen by an active Tourist Police Officer (Pam Obvit), ensuring risk mitigation standards exceed civilian operators." |
| "We do health screening" | "Mandatory pre-ascent medical screening (blood pressure + SpO2) is enforced per BBKSDA Regulation SE.1658. Guests failing thresholds are denied access." |
| "Private tours" | "Every booking is exclusively private — dedicated vehicle, driver, and licensed guide. No shared groups ever." |

---

## Technical Audit: StartLocation as Primary Attribute

The EAV model for tour packages must treat:
- `StartLocation` as the highest-level discriminator (Surabaya or Bali)
- Duration (1D1N through 6D5N) as secondary
- `Destination` as tertiary

Current JVTO site taxonomy correctly mirrors this (Surabaya hub = 12 packages, Bali hub = 4). The EAV schema should replicate this hierarchy.

---

-> [[sources/geo-aeo-strategy-2026-05]] | -> [[ops/geo-aeo-strategy]] | -> [[content/aeo-claims]] | -> [[credentials/trust-signals]]
