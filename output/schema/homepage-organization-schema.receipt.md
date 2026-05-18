---
output_date: 2026-05-18
schema_file: homepage-organization-schema.json
profile: schema (Organization + TravelAgency)
---

# Verification Receipt — homepage-organization-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| `logo` | `https://javavolcano-touroperator.com/assets/img/jvto-color.png` | trust-signals.md (ssot-image-asset-map) | 2026-05-18 | Low |
| `foundingDate` | `2016` (PT incorporation, AHU registry) | legal-licenses.md §Business Registration | — | None |
| `ratingValue` (Organization) | `4.8` | trust-signals.md:114 §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (cross-platform) | `164` (51 TP + 92 Google + 21 TA) | trust-signals.md:115 §Schema Canonical Values | 2026-05-18 | **High** |
| `telephone` | `+6282244788833` | trust-signals.md:117 | — | Low |
| `email` | `hello@javavolcano-touroperator.com` | trust-signals.md:118 | — | Low |
| `streetAddress` | `Jl. Khairil Anwar No.102 A, Badean` | trust-signals.md:119 | — | Low |
| `postalCode` | `68214` | trust-signals.md:121 | — | None |
| NIB identifier | `1102230032918` | trust-signals.md:122 | — | None |
| HPWKI identifier | `AHU-0001072.AH.01.07.TAHUN 2024` | trust-signals.md:123 | — | Low |
| ISIC identifier | `259268` | trust-signals.md:124 | — | Low |
| `sameAs` (8 URLs) | All confirmed Live ✅ | trust-signals.md §Social Media Profiles | 2026-05-09 | Low |

## Drift status

- `reviewCount=164` live verified **2026-05-18** via JVTO homepage widget — all platforms confirmed unchanged.
- No stale flags triggered.
- Next recommended live check: before **2026-06-18**.

## Omissions (not invented)

- `foundingDate` — resolved 2026-05-18: `2016` = PT incorporation (AHU). `2015` = guesthouse era. `2023` = TDUP license. Schema uses 2016 (legal entity founding).
- `priceRange` — not verified from packages-full-pricing.md in this pass. Add separately if needed.
- Klook / Booking.com `sameAs` entries — marked ⚠️ Unverified in trust-signals.md. Excluded.
