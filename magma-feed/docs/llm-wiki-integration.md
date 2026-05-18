# llm-wiki Integration

`F:\magma-feed` is the source of truth for MAGMA/PVMBG ingestion. `llm-wiki` should consume output, not embed scraper logic.

## Preferred Runtime Path

```powershell
cd F:\magma-feed
npm run collect
npm start
```

Then `llm-wiki` can fetch:

```http
GET http://127.0.0.1:8787/api/magma/latest?codes=IJE,BRO
GET http://127.0.0.1:8787/api/magma/widget?codes=IJE,BRO
```

## Offline-Safe Path

Run:

```powershell
cd F:\magma-feed
npm run export
```

Then read:

- `F:\magma-feed\exports\latest.json`
- `F:\magma-feed\exports\widget.json`
- `F:\magma-feed\exports\volcano-status.md`

## Optional Copy Into llm-wiki

`npm run sync:wiki` copies `exports/volcano-status.md` to:

```text
E:\Users\JAVA VOLCANO\llm-wiki\wiki\ops\volcano-status.md
```

Override target root with:

```powershell
$env:JVTO_LLM_WIKI_PATH = "E:\Users\JAVA VOLCANO\llm-wiki"
npm run sync:wiki
```

This is intentionally manual. The default flow keeps `llm-wiki` as a consumer only.
