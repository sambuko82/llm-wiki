---
output_date: 2026-05-25
schema_file: homepage-organization-schema.json
profile: schema (Organization + TravelAgency)
---

# Verification Receipt — homepage-organization-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| `logo` | `https://javavolcano-touroperator.com/assets/img/jvto-color.png` | trust-signals.md (ssot-image-asset-map) | 2026-05-18 | Low |
| `foundingDate` | `2016` (PT incorporation, AHU registry) | legal-licenses.md §Business Registration | — | None |
| `ratingValue` (Organization) | `4.8` | trust-signals.md:114 §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (cross-platform) | `195` (51 TP + 123 Google + 21 TA) | trust-signals.md:115 §Schema Canonical Values | 2026-05-26 (API) | **High** |
| `telephone` | `+6282244788833` | trust-signals.md:117 | — | Low |
| `email` | `hello@javavolcano-touroperator.com` | trust-signals.md:118 | — | Low |
| `streetAddress` | `Jl. Khairil Anwar No.102 A, Badean` | trust-signals.md:119 | — | Low |
| `postalCode` | `68214` | trust-signals.md:121 | — | None |
| NIB identifier | `1102230032918` | trust-signals.md:122 | — | None |
| HPWKI identifier | `AHU-0001072.AH.01.07.TAHUN 2024` | trust-signals.md:123 | — | Low |
| ISIC identifier | `259268` | trust-signals.md:124 | — | Low |
| `sameAs` (8 URLs) | All confirmed Live ✅ | trust-signals.md §Social Media Profiles | 2026-05-09 | Low |
| `priceRange` | `IDR 1,000,000 – IDR 6,050,000 per person` | packages-full-pricing.md | 2026-05-18 | Low |

## Drift status

- `reviewCount=195` updated 2026-06-01 from `trust-signals.md §Schema Canonical Values` (Google moved 92→123 on 2026-05-26 via API; cross-platform total now 51+123+21=195). Previous stale value 164 closed.
- Next recommended live check: before **2026-06-26**.

## Omissions (not invented)

- `foundingDate` — resolved 2026-05-18: `2016` = PT incorporation (AHU). `2015` = guesthouse era. `2023` = TDUP license. Schema uses 2016 (legal entity founding).
- `priceRange` — added 2026-05-18: `IDR 1,000,000` (bromo-1d1n 11+ pax) to `IDR 6,050,000` (ijen-papuma-tumpak-sewu-bromo-malang-6d5n 2 pax). Sourced from packages-full-pricing.md §Canonical.
- Klook / Booking.com `sameAs` entries — marked ⚠️ Unverified in trust-signals.md. Excluded.
