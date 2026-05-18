import http from "node:http";
import { URL } from "node:url";
import { CACHE_TTL_MS, DEFAULT_VOLCANO_CODES } from "./config.js";
import { getCachedOrFresh } from "./collector.js";
import { fetchDailySummary, fetchRecentEruptions } from "./magma-client.js";
import { buildWidget } from "./advisory.js";
import { handleMcpRequest } from "./mcp.js";

const PORT = Number(process.env.PORT || 8787);
const HOST = process.env.HOST || "127.0.0.1";

let feedPromise = null;

async function getFeed() {
  if (!feedPromise) {
    feedPromise = getCachedOrFresh({ ttlMs: CACHE_TTL_MS }).finally(() => {
      feedPromise = null;
    });
  }
  return feedPromise;
}

const server = http.createServer(async (req, res) => {
  try {
    await route(req, res);
  } catch (error) {
    sendJson(res, 500, {
      error: error.message,
      servedAt: new Date().toISOString()
    });
  }
});

async function route(req, res) {
  const url = new URL(req.url, `http://${req.headers.host || `${HOST}:${PORT}`}`);

  if (req.method === "GET" && url.pathname === "/health") {
    sendJson(res, 200, { ok: true, service: "jvto-magma-feed", time: new Date().toISOString() });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/latest") {
    const feed = await getFeed();
    const codes = parseCodes(url);
    sendJson(res, 200, {
      source: feed.source,
      fetchedAt: feed.fetchedAt,
      stale: Boolean(feed.stale),
      reports: Object.fromEntries(codes.map((code) => [code, feed.latest?.[code] || null]))
    });
    return;
  }

  if (req.method === "GET" && url.pathname.startsWith("/api/magma/volcano/")) {
    const code = url.pathname.split("/").pop().toUpperCase();
    const feed = await getFeed();
    sendJson(res, feed.latest?.[code] ? 200 : 404, {
      report: feed.latest?.[code] || null,
      stale: Boolean(feed.stale),
      fetchedAt: feed.fetchedAt
    });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/daily") {
    const date = url.searchParams.get("date") || new Date().toISOString().slice(0, 10);
    const feed = await getFeed();
    if (feed.dailySummary?.date === date) {
      sendJson(res, 200, {
        dailySummary: feed.dailySummary,
        stale: Boolean(feed.stale),
        fetchedAt: feed.fetchedAt
      });
      return;
    }

    sendJson(res, 200, {
      dailySummary: await fetchDailySummary(date),
      stale: false,
      fetchedAt: new Date().toISOString()
    });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/activity-levels") {
    const feed = await getFeed();
    sendJson(res, feed.activityLevels ? 200 : 404, {
      activityLevels: feed.activityLevels || null,
      stale: Boolean(feed.stale),
      fetchedAt: feed.fetchedAt
    });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/eruptions") {
    const page = Math.max(1, Number(url.searchParams.get("page") || 1) || 1);
    const feed = await getFeed();
    if (feed.recentEruptions?.page === page) {
      sendJson(res, 200, {
        recentEruptions: feed.recentEruptions,
        stale: Boolean(feed.stale),
        fetchedAt: feed.fetchedAt
      });
      return;
    }

    sendJson(res, 200, {
      recentEruptions: await fetchRecentEruptions(page),
      stale: false,
      fetchedAt: new Date().toISOString()
    });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/seismic-90d") {
    const code = (url.searchParams.get("code") || DEFAULT_VOLCANO_CODES[0]).toUpperCase();
    const feed = await getFeed();
    sendJson(res, feed.seismic90d?.[code] ? 200 : 404, {
      seismic90d: feed.seismic90d?.[code] || null,
      stale: Boolean(feed.stale),
      fetchedAt: feed.fetchedAt
    });
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/magma/widget") {
    const feed = await getFeed();
    sendJson(res, 200, { items: buildWidget(feed, parseCodes(url)) });
    return;
  }

  if (req.method === "POST" && url.pathname === "/mcp") {
    const body = await readJson(req);
    sendJson(res, 200, await handleMcpRequest(body, getFeed));
    return;
  }

  sendJson(res, 404, { error: "Not found" });
}

function parseCodes(url) {
  const raw = url.searchParams.get("codes");
  return (raw ? raw.split(",") : DEFAULT_VOLCANO_CODES).map((code) => code.trim().toUpperCase()).filter(Boolean);
}

async function readJson(req) {
  const chunks = [];
  for await (const chunk of req) chunks.push(chunk);
  return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}");
}

function sendJson(res, statusCode, payload) {
  res.writeHead(statusCode, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "access-control-allow-origin": process.env.CORS_ALLOW_ORIGIN || "*"
  });
  res.end(`${JSON.stringify(payload, null, 2)}\n`);
}

server.listen(PORT, HOST, () => {
  console.log(`JVTO MAGMA feed listening on http://${HOST}:${PORT}`);
});
