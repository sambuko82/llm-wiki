# JVTO Web Policy Bundle Sync Handoff (v2)

**Status**: ready for jvto-web implementation
**Producer repo**: `E:\Users\JAVA VOLCANO\llm-wiki`
**Producer output**: `output/website/policy-bundle/`
**Recommended jvto-web target**: `src/data/policy-bundle/`
**Schema**: `policy-bundle/v2.0`

---

## Purpose

Use this bundle as the canonical policy source for all jvto-web policy surfaces. Do not copy
policy wording manually into UI components, invoice/e-voucher templates, or customer-support reply
code if the same wording exists in this bundle. v2 adds the **Lifetime Package Guarantee**
cancellation domain (YAML-canonical), plus two machine-facing artifacts: `decision-matrix.json`
(rule-engine-ready outcomes) and `customer-copy.json` (canonical copy blocks).

## Source Flow

```text
wiki/policies/cancellation-package-credit.yml   (canonical cancellation logic)
wiki/ops/policy-source-ownership.md
wiki/products/packages-overview.md
wiki/website/faq-master.md
        |
        v
scripts/compile_policy_bundle.py --write --strict
        |
        v
output/website/policy-bundle/
        |
        v
jvto-web/scripts/sync-policy-bundle.mjs
        |
        v
jvto-web/src/data/policy-bundle/
        |
        v
policy page / checkout / booking portal / e-voucher / invoice / FAQ / customer support
```

## Required Gate

jvto-web sync must read `_manifest.json` before copying files.

Required:

```js
manifest.schema_version === "policy-bundle/v2.0"
manifest.clean === true
```

Refuse sync if:

- `_manifest.json` is missing.
- `schema_version` is not exactly `policy-bundle/v2.0`.
- `clean` is not `true`.
- Any required JSON file is missing.
- `consumer-bundles.json` does not contain the required consumers (`website_checkout`,
  `booking_portal`, `e_voucher`, `invoice`, `policy_page`, `faq`, `customer_support`).
- `deprecated-wording-report.json.summary.total_findings !== 0`.
- `gap-report.json.summary.errors !== 0`.

## Required Files

| File | Use in jvto-web |
|---|---|
| `_manifest.json` | Sync/version gate; carries `cancellation_policy_version` + `cancellation_policy_hash` |
| `policy-bundle.json` | Full policy domain map (cancellation domain also carries `canonical_policy` + `customer_copy`) |
| `consumer-bundles.json` | Per-surface entrypoint (grouped by controlled consumer ID) |
| `decision-matrix.json` | Rule-engine-ready outcomes — consumed by the cancellation engine; never recomputed in the UI |
| `customer-copy.json` | Canonical customer-facing copy blocks for all policy surfaces |
| `deprecated-wording-report.json` | Fails deprecated policy wording before consumer use |
| `gap-report.json` | Fails compiler policy errors before consumer use |

## Consumer Mapping (controlled IDs)

| jvto-web surface | JSON path | Expected use |
|---|---|---|
| Policy page | `consumer-bundles.json.policy_page` | Full binding cancellation/Package-Credit rules |
| Checkout | `consumer-bundles.json.website_checkout` | Terms, website-only booking, payment, cancellation summary, anti-fraud |
| Booking portal | `consumer-bundles.json.booking_portal` | Personalized eligibility + cancellation rules |
| E-Voucher | `consumer-bundles.json.e_voucher` | Package entitlement summary + policy version |
| Invoice | `consumer-bundles.json.invoice` | Payment rules + cancellation reference |
| FAQ | `consumer-bundles.json.faq` | Plain-language examples |
| Customer support | `consumer-bundles.json.customer_support` | **Read-only** reply source (never books) |

> WhatsApp is intentionally not a booking consumer. WhatsApp/email are support channels only;
> the `customer_support` bundle is read-only.

## Recommended Commands

From llm-wiki:

```powershell
python scripts\compile_policy_bundle.py --write --strict
```

From jvto-web, after implementing the sync script:

```bash
npm run sync:policy-bundle
```

## Implementation Notes

- Treat `consumer-bundles.json` + `customer-copy.json` as the app-facing files. `policy-bundle.json`
  is the full registry for debugging/admin/audits.
- `decision-matrix.json` is the single source of cancellation outcomes. The website (and the Laravel
  backend) must consume it and never recompute refund/credit outcomes independently.
- If sync fails, fix llm-wiki source or compiler output first. Do not bypass by hardcoding
  replacement policy text in jvto-web.
