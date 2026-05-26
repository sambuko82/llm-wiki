# Schema Verification Receipt — Student Packages (6)

Generated: 2026-05-26. Profile: `schema` compilation.

## Files generated

| File | URL | Duration | Low price | High price |
|------|-----|----------|-----------|------------|
| `student-bromo-ijen-3d2n-schema.json` | `/tours/student-package/bromo-ijen-3d2n` | P3D | 2,050,000 | 5,400,000 |
| `student-bromo-ijen-3d2n-to-bali-schema.json` | `/tours/student-package/bromo-ijen-3d2n-to-bali` | P3D | 2,050,000 | 5,400,000 |
| `student-ijen-bromo-3d2n-bali-schema.json` | `/tours/student-package/ijen-bromo-3d2n` | P3D | 1,900,000 | 2,900,000 |
| `student-ijen-bromo-madakaripura-night-market-4d3n-schema.json` | `/tours/student-package/ijen-bromo-madakaripura-night-market-4d3n` | P4D | 2,700,000 | 6,500,000 |
| `student-ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-4d3n` | P4D | 2,900,000 | 7,150,000 |
| `student-ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-5d4n` | P5D | 3,050,000 | 4,050,000 |

## Canonical value verification

| Schema field | Value used | Source | Verified date | Drift risk |
|---|---|---|---|---|
| `ratingValue` (Trustpilot) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| NIB identifier | `1102230032918` | credentials/legal-licenses | static | None |
| ISIC Provider ID | `259268` | credentials/legal-licenses | static | Low |

## Price verification

All prices cross-checked against `wiki/products/packages-full-pricing.md` §Student Packages:

- `bromo-ijen-3d2n` + `bromo-ijen-3d2n-to-bali`: solo 5,400,000 → 11+ 2,050,000. ✓ Match.
- `ijen-bromo-3d2n` (Bali): 2 pax 2,900,000 → 11+ 1,900,000. No solo tier. ✓ Match.
- `ijen-bromo-madakaripura-night-market-4d3n`: solo 6,500,000 → 11+ 2,700,000. ✓ Match.
- `ijen-papuma-tumpak-sewu-bromo-4d3n`: solo 7,150,000 → 11+ 2,900,000. ✓ Match.
- `ijen-papuma-tumpak-sewu-bromo-5d4n`: 2 pax 4,050,000 → 11+ 3,050,000. No solo tier. ✓ Match.

## Student-specific schema additions

All student schemas include:
- `"touristType": "International students with verified ISIC card"`
- `"eligibleCustomerType": "Student"` in offers
- ISIC Provider ID 259268 referenced in description
- `reviewCount=51` — same as canonical packages (reviews are for the operator, not the tier)

## Next refresh

- `reviewCount`: before **2026-06-18** (monthly check)
- Prices: after any student pricing update in `packages-full-pricing.md`
