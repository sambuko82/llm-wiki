# JVTO Web Policy Bundle Sync Handoff

**Status**: ready for jvto-web implementation
**Producer repo**: `E:\Users\JAVA VOLCANO\llm-wiki`
**Producer output**: `output/website/policy-bundle/`
**Recommended jvto-web target**: `src/data/policy-bundle/`

---

## Purpose

Use this bundle as the canonical policy source for jvto-web checkout, invoice, and WhatsApp consumers. Do not copy policy wording manually into UI components, invoice templates, or WhatsApp reply code if the same wording exists in this bundle.

## Source Flow

```text
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
checkout / invoice / WhatsApp consumers
```

## Required Gate

jvto-web sync must read `_manifest.json` before copying files.

Required:

```js
manifest.schema_version === "policy-bundle/v1.0"
manifest.clean === true
```

Refuse sync if:

- `_manifest.json` is missing.
- `schema_version` is not exactly `policy-bundle/v1.0`.
- `clean` is not `true`.
- Any required JSON file is missing.
- `consumer-bundles.json` does not contain `checkout`, `invoice`, and `whatsapp`.
- `deprecated-wording-report.json.summary.total_findings !== 0`.
- `gap-report.json.summary.errors !== 0`.

## Required Files

| File | Use in jvto-web |
|---|---|
| `_manifest.json` | Sync/version gate |
| `policy-bundle.json` | Full policy domain map |
| `consumer-bundles.json` | Primary app entrypoint for checkout, invoice, WhatsApp |
| `deprecated-wording-report.json` | Fails deprecated policy wording before consumer use |
| `gap-report.json` | Fails compiler policy errors before consumer use |

## Consumer Mapping

| jvto-web consumer | JSON path | Expected use |
|---|---|---|
| Checkout | `consumer-bundles.json.checkout` | Terms, booking path, payment, anti-fraud microcopy |
| Invoice | `consumer-bundles.json.invoice` | Payment rules and deadline wording |
| WhatsApp | `consumer-bundles.json.whatsapp` | Booking path and Ijen health-screening reply source |

## Recommended Commands

From llm-wiki:

```powershell
python scripts\compile_policy_bundle.py --write --strict
```

From jvto-web, after implementing the sync script:

```bash
npm run sync:policy-bundle
```

Suggested `package.json` script:

```json
{
  "scripts": {
    "sync:policy-bundle": "node scripts/sync-policy-bundle.mjs"
  }
}
```

## Implementation Notes

- Keep this separate from Package Readiness sync: `src/data/package-readiness/` and `src/data/policy-bundle/` should be sibling folders.
- Treat `consumer-bundles.json` as the app-facing file. `policy-bundle.json` is the full registry for debugging, admin UI, and audits.
- If checkout/invoice/WhatsApp need shorter copy, derive it inside jvto-web from the consumer bundle, but keep the compiled evidence text as the source.
- If sync fails, fix llm-wiki source or compiler output first. Do not bypass by hardcoding replacement policy text in jvto-web.

