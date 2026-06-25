# OKF — Open Knowledge Framework Concepts

Structured **concept records** for the JVTO knowledge catalog. Each concept is a typed
entity (not narrative wiki copy) with a stable `id`, a `type`, a canonical `resource`,
and review/visibility metadata. Concepts are referenced by domain wiki pages and by
compiled outputs; they are the single source of truth for "what is this entity and what
may we claim about it."

## Concept frontmatter schema

| Field | Meaning |
|---|---|
| `id` | Stable path-like identifier, mirrors the file path under `okf/` (e.g. `references/stefan-loose-indonesien-guidebook`). |
| `type` | Concept type — one of `Reference`, `Partner`, `Credential`, `Organization`. |
| `title` | Human-readable title. |
| `description` | One-line summary of what the concept is and what it supports. |
| `resource` | Canonical external URL for the concept. |
| `status` | `draft` \| `reviewed` \| `deprecated`. |
| `visibility` | `public` \| `internal`. |
| `last_verified` | ISO date the record was last checked. |
| `tags` | Classification tags. |

## Concept types — what they mean

- **Reference** — an independent third-party mention or citation. Supports historical
  continuity / recognition. **Not** an endorsement, rating, partnership, or certification.
- **Partner** — an active commercial or institutional relationship (requires evidence).
- **Credential** — a license, certification, or formal qualification (requires a verifiable issuer).
- **Organization** — an organizational entity (e.g. JVTO itself, an authority).

> Do not promote a `Reference` to `Partner`/`Credential` without independent evidence of a
> current relationship. A historical mention is not an endorsement.

## Concepts

- `references/stefan-loose-indonesien-guidebook` — **Reference**. Stefan Loose Reiseführer
  Indonesien: mit Reiseatlas (ISBN-10 3770167651 · ISBN-13 9783770167654, p. 287).
