# MAGMA Feed API Contract

Base URL local default: `http://127.0.0.1:8787`.

All public responses are JVTO operational data derived from MAGMA Indonesia/PVMBG. They must not be presented as official emergency instructions.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/health` | Service status. |
| `GET` | `/api/magma/latest?codes=IJE,BRO` | Latest cached reports by volcano code. |
| `GET` | `/api/magma/volcano/:code` | Single latest cached report. |
| `GET` | `/api/magma/daily?date=YYYY-MM-DD` | MAGMA daily summary for a date. Uses cache when date matches. |
| `GET` | `/api/magma/seismic-90d?code=IJE` | 90-day seismic chart summary and raw chart data. |
| `GET` | `/api/magma/activity-levels` | National activity level table. |
| `GET` | `/api/magma/eruptions?page=1` | Recent eruption timeline page. |
| `GET` | `/api/magma/widget?codes=IJE,BRO` | Small advisory widget payload for JVTO pages. |
| `POST` | `/mcp` | JSON-RPC MCP endpoint. |

## Stale Cache Contract

When MAGMA collection fails but cache exists, API responses keep serving cached data with:

- `stale: true`
- `staleReason`
- `servedAt`
- existing `fetchedAt` from the last successful collection

Consumers should display `last checked` or `fetchedAt` and link to the original MAGMA report.

## Stable Volcano Codes

| Code | Volcano |
|---|---|
| `IJE` | Ijen |
| `BRO` | Bromo |
