# JVTO MAGMA Feed

Server-side collector for MAGMA Indonesia / PVMBG volcano reports, built for JVTO travel advisory use.

## Run

```bash
cd magma-feed
npm test
npm run collect
npm start
```

Default API URL: `http://127.0.0.1:8787`

## REST Endpoints

- `GET /health`
- `GET /api/magma/latest?codes=IJE,BRO`
- `GET /api/magma/volcano/IJE`
- `GET /api/magma/daily?date=YYYY-MM-DD`
- `GET /api/magma/seismic-90d?code=IJE`
- `GET /api/magma/widget?codes=IJE,BRO`

## MCP Endpoint

`POST /mcp` accepts JSON-RPC tool calls for:

- `get_latest_volcano_report`
- `get_activity_levels`
- `get_daily_volcano_summary`
- `get_seismic_90d`
- `generate_jvto_travel_advisory`

All tools are read-only and should be backed by the JVTO API/cache, not browser-side scraping.

## Notes

- MAGMA detail pages are HTML, not public JSON.
- The 90-day highcharts endpoint requires a fresh page request, MAGMA session cookie, and CSRF token.
- Public copy must cite MAGMA/PVMBG as the official source and frame output as JVTO travel advisory, not official emergency instruction.
