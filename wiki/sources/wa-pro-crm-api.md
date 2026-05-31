---
type: source
title: WhatsApp Pro CRM — REST API v1 Documentation
last_updated: 2026-05-25
sources: [API_Documentation_JVTO.pdf]
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/index, wiki/whatsapp/operations-playbook, wiki/whatsapp/rules-engine]
---

# WhatsApp Pro CRM — REST API v1

**Source**: `raw/API_Documentation_JVTO.pdf` (4 pages)
**Type**: `pdf-doc` (operational API reference)
**System**: WA Dashboard at `wa-dashboard.javavolcano-touroperator.com`

> **Security note**: API keys and number keys exist in the raw PDF. NOT reproduced here. Credentials managed via the WA Dashboard admin panel.

---

## Architecture

- **Base URL**: `https://wa-dashboard.javavolcano-touroperator.com/api/v1`
- **Auth method**: `api_key` + `number_key` in request body (not headers)
- Legacy endpoints (`/api/v1/send/text`, `/api/v1/send/media`) use header `Authorization: Bearer <api_key>` — migration to body-auth v1 recommended

---

## Endpoints

| Method | Path | Function |
|---|---|---|
| POST | `/api/v1/checking_key` | Validate API key |
| POST | `/api/v1/send_message` | Send text message |
| POST | `/api/v1/send_image_url` | Send image via URL (optional caption, `separate_caption` flag) |
| POST | `/api/v1/send_file_url` | Send file/document/video via URL (auto-detects type from extension) |
| POST | `/api/v1/groups` | List WhatsApp groups |
| POST | `/api/v1/send_template` | Send templated message with dynamic variables |

---

## Error Codes

| Code | Status | Description |
|---|---|---|
| 200 | Success | Message sent |
| 1002 | Invalid API Key | `api_key` not found |
| 1003 | Invalid Number Key | `number_key` invalid |
| 1004 | Not Connected | WhatsApp not connected |
| 1005 | Fatal Error | Send failure — check error detail |
| 1006 | Other Error | Missing fields or other error |

---

## Webhook (Incoming Messages)

Webhook URL configured per number in dashboard. Payload sent automatically on incoming message.

**Supported message types**:
- `conversation` — text message (`data.text`)
- `imageMessage` — image with optional caption (`data.media.url`, `data.text`)
- `audioMessage` — voice note/audio (`data.media.seconds`, `data.media.ptt`)
- `documentMessage` — file/document (`data.media.filename`, `data.media.fileSize`)
- `locationMessage` — location share (`data.location.latitude/longitude/name/address`)
- `contactMessage` — contact card (`data.contact.displayName`, `data.contact.vcard`)

Each webhook payload includes: `event: "message"`, `data.from`, `data.fromMe`, `data.id`, `data.timestamp`, `data.type`.

---

## Relevance to Wiki

- Feeds [[whatsapp/operations-playbook]] — this is the API that powers WhatsApp automation
- Template endpoint enables canned responses from [[whatsapp/canned-responses]]
- Webhook types inform what the WA rules engine can react to
- `send_template` with `variables` supports personalized booking confirmations, itinerary reminders
- File/image sending supports post-booking asset delivery (vouchers, maps, medical screening reminders)
