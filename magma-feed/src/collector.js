import { CACHE_TTL_MS, DEFAULT_VOLCANO_CODES, LOOKBACK_DAYS } from "./config.js";
import { isFresh, readCache, writeCache } from "./cache.js";
import { todayRange } from "./dates.js";
import { fetchActivityLevels, fetchDailySummary, fetchLatestReport, fetchSeismic90d } from "./magma-client.js";

export async function collectMagmaFeed(options = {}) {
  const codes = options.codes || DEFAULT_VOLCANO_CODES;
  const now = options.now || new Date();
  const { start, end } = todayRange(options.lookbackDays ?? LOOKBACK_DAYS, now);
  const latest = {};
  const seismic90d = {};
  const errors = [];

  for (const code of codes) {
    try {
      const report = await fetchLatestReport(code, start, end, options.fetchImpl);
      latest[code] = report;
      try {
        seismic90d[code] = await fetchSeismic90d(report, options.fetchImpl);
      } catch (error) {
        errors.push({ scope: "seismic90d", code, message: error.message });
      }
    } catch (error) {
      errors.push({ scope: "latest", code, message: error.message });
    }
  }

  let activityLevels = null;
  try {
    activityLevels = await fetchActivityLevels(options.fetchImpl);
  } catch (error) {
    errors.push({ scope: "activityLevels", message: error.message });
  }

  let dailySummary = null;
  try {
    dailySummary = await fetchDailySummary(end, options.fetchImpl);
  } catch (error) {
    errors.push({ scope: "dailySummary", date: end, message: error.message });
  }

  const feed = {
    source: "MAGMA Indonesia / PVMBG",
    fetchedAt: new Date().toISOString(),
    range: { start, end },
    codes,
    latest,
    seismic90d,
    activityLevels,
    dailySummary,
    errors,
    stale: false
  };

  if (options.write !== false) await writeCache(feed, options.cachePath);
  return feed;
}

export async function getCachedOrFresh(options = {}) {
  const cache = await readCache(options.cachePath);
  if (isFresh(cache, options.ttlMs ?? CACHE_TTL_MS)) return cache;

  try {
    return await collectMagmaFeed(options);
  } catch (error) {
    if (!cache) throw error;
    return {
      ...cache,
      stale: true,
      staleReason: error.message,
      servedAt: new Date().toISOString()
    };
  }
}
