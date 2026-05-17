import { MAGMA_BASE_URL, USER_AGENT } from "./config.js";
import { parseActivityLevels, parseDailySummary, parseReportDetail, parseSearchResults, summarizeSeismicChart } from "./parser.js";

const HIGHCHARTS_SIGNATURE = "8c93bcd1b2982612f94bd2a5af8b1f2434afd753ad8383ea9d3fde1d9df577ea";

export async function fetchLatestReport(code, start, end, fetchImpl = fetch) {
  const searchUrl = `${MAGMA_BASE_URL}/v1/gunung-api/laporan/search/q?code=${encodeURIComponent(code)}&start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`;
  const searchHtml = await fetchText(searchUrl, fetchImpl);
  const [latest] = parseSearchResults(searchHtml);
  if (!latest) {
    throw new Error(`No MAGMA report found for ${code} between ${start} and ${end}`);
  }
  return fetchReportDetail(latest.sourceUrl, fetchImpl);
}

export async function fetchReportDetail(sourceUrl, fetchImpl = fetch) {
  const html = await fetchText(sourceUrl, fetchImpl);
  return parseReportDetail(html, sourceUrl);
}

export async function fetchActivityLevels(fetchImpl = fetch) {
  const url = `${MAGMA_BASE_URL}/v1/gunung-api/tingkat-aktivitas`;
  return parseActivityLevels(await fetchText(url, fetchImpl));
}

export async function fetchDailySummary(date, fetchImpl = fetch) {
  const url = `${MAGMA_BASE_URL}/v1/gunung-api/laporan-harian/${encodeURIComponent(date)}`;
  return parseDailySummary(await fetchText(url, fetchImpl), url);
}

export async function fetchSeismic90d(report, fetchImpl = fetch) {
  if (!report?.sourceUrl || !report?.reportId) {
    throw new Error("A report with sourceUrl and reportId is required for seismic chart fetch");
  }

  const session = {};
  const detailResponse = await fetchImpl(report.sourceUrl, {
    headers: {
      "user-agent": USER_AGENT,
      accept: "text/html"
    }
  });

  if (!detailResponse.ok) {
    throw new Error(`MAGMA detail fetch failed ${detailResponse.status} for ${report.sourceUrl}`);
  }

  collectCookies(session, detailResponse.headers);
  const detailHtml = await detailResponse.text();
  const token = /<meta name="csrf-token" content="([^"]+)"/i.exec(detailHtml)?.[1];
  if (!token) throw new Error(`Could not find CSRF token for report ${report.reportId}`);

  const body = new URLSearchParams({ id: report.reportId });
  const chartResponse = await fetchImpl(`${MAGMA_BASE_URL}/v1/json/highcharts?signature=${HIGHCHARTS_SIGNATURE}`, {
    method: "POST",
    headers: {
      "user-agent": USER_AGENT,
      accept: "application/json, text/javascript, */*; q=0.01",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-csrf-token": token,
      "x-requested-with": "XMLHttpRequest",
      cookie: cookieHeader(session)
    },
    body
  });

  if (!chartResponse.ok) {
    throw new Error(`MAGMA highcharts fetch failed ${chartResponse.status} for report ${report.reportId}`);
  }

  const chart = await chartResponse.json();
  return {
    sourceReportId: report.reportId,
    volcanoCode: report.volcanoCode,
    sourceUrl: report.sourceUrl,
    raw: chart,
    summary: summarizeSeismicChart(chart),
    fetchedAt: new Date().toISOString()
  };
}

async function fetchText(url, fetchImpl) {
  const response = await fetchImpl(url, {
    headers: {
      "user-agent": USER_AGENT,
      accept: "text/html,application/xhtml+xml"
    }
  });
  if (!response.ok) throw new Error(`MAGMA fetch failed ${response.status} for ${url}`);
  return response.text();
}

function collectCookies(session, headers) {
  const cookies = typeof headers.getSetCookie === "function" ? headers.getSetCookie() : splitSetCookie(headers.get("set-cookie"));
  for (const cookie of cookies) {
    const [pair] = cookie.split(";");
    const [name, value] = pair.split("=");
    if (name && value) session[name.trim()] = value.trim();
  }
}

function cookieHeader(session) {
  return Object.entries(session)
    .map(([name, value]) => `${name}=${value}`)
    .join("; ");
}

function splitSetCookie(value) {
  if (!value) return [];
  return value.split(/,(?=\s*[^;,]+=)/g);
}
