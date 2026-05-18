# JVTO MAGMA Feed

Standalone server-side MAGMA Indonesia/PVMBG collector, cache, REST API, MCP endpoint, and export pipeline for JVTO travel advisory workflows.

Target standalone path: `F:\magma-feed`.

## Commands

```powershell
npm test
npm run collect
npm run export
npm start
npm run sync:wiki
```

Default server: `http://127.0.0.1:8787`.

## REST Endpoints

- `GET /health`
- `GET /api/magma/latest?codes=IJE,BRO`
- `GET /api/magma/volcano/IJE`
- `GET /api/magma/daily?date=YYYY-MM-DD`
- `GET /api/magma/seismic-90d?code=IJE`
- `GET /api/magma/activity-levels`
- `GET /api/magma/eruptions?page=1`
- `GET /api/magma/widget?codes=IJE,BRO`
- `POST /mcp`

## MCP Tools

- `get_latest_volcano_report(code)`
- `get_activity_levels()`
- `get_daily_volcano_summary(date)`
- `get_seismic_90d(code)`
- `get_recent_eruptions(page)`
- `generate_jvto_travel_advisory(code, tourDate, language)`

## Exports

`npm run export` writes:

- `exports/latest.json`
- `exports/widget.json`
- `exports/activity-levels.json`
- `exports/daily-summary.json`
- `exports/seismic-90d.json`
- `exports/eruptions.json`
- `exports/volcano-status.md`

## llm-wiki Consumption

Preferred: `GET http://127.0.0.1:8787/api/magma/latest?codes=IJE,BRO`

Offline-safe: read `F:\magma-feed\exports\latest.json` or `F:\magma-feed\exports\volcano-status.md`.

Detailed contracts live in `docs/`.

## GitHub Prep

Runtime folders are ignored by `.gitignore`: `data/`, `exports/`, and `.codex-run/`.

Before publishing a fresh repo:

```powershell
cd F:\magma-feed
git init
git add .
git commit -m "Initial JVTO MAGMA feed service"
```

## Data Policy

This service cites MAGMA Indonesia/PVMBG as the official source. JVTO output is operational travel advisory copy, not an official emergency instruction.
