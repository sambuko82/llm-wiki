# MCP Tools

Endpoint: `POST http://127.0.0.1:8787/mcp`

The server exposes a small read-only tool surface, so it uses one tool per action.

| Tool | Input | Output |
|---|---|---|
| `get_latest_volcano_report` | `{ "code": "IJE" }` | Latest cached normalized report. |
| `get_activity_levels` | `{}` | National MAGMA activity level table. |
| `get_daily_volcano_summary` | `{ "date": "2026-05-17" }` | Cached daily summary for matching date. |
| `get_seismic_90d` | `{ "code": "IJE" }` | 90-day seismic summary and raw chart. |
| `get_recent_eruptions` | `{ "page": 1 }` | Cached recent eruption timeline items. |
| `generate_jvto_travel_advisory` | `{ "code": "BRO", "tourDate": "2026-05-20", "language": "en" }` | Guest-facing JVTO advisory text with PVMBG attribution. |

The MCP tools are intended for internal agent workflows: guest briefing, drafting WhatsApp/email copy, updating advisory pages, and monitoring status changes.
