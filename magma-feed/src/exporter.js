import { mkdir, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { DEFAULT_VOLCANO_CODES } from "./config.js";
import { buildWidget } from "./advisory.js";

const ROOT_DIR = dirname(fileURLToPath(new URL("../package.json", import.meta.url)));
export const DEFAULT_EXPORT_DIR = new URL("../exports", import.meta.url);

export async function writeExports(feed, outputDir = DEFAULT_EXPORT_DIR) {
  const dirPath = fileURLToPath(outputDir);
  await mkdir(dirPath, { recursive: true });

  const files = buildExportPayloads(feed);
  await Promise.all(
    Object.entries(files).map(([name, value]) =>
      writeFile(join(dirPath, name), typeof value === "string" ? value : `${JSON.stringify(value, null, 2)}\n`, "utf8")
    )
  );

  return {
    outputDir: dirPath,
    files: Object.keys(files).map((name) => join(dirPath, name))
  };
}

export function buildExportPayloads(feed) {
  const codes = feed.codes?.length ? feed.codes : DEFAULT_VOLCANO_CODES;
  return {
    "latest.json": {
      source: feed.source,
      fetchedAt: feed.fetchedAt,
      stale: Boolean(feed.stale),
      staleReason: feed.staleReason || "",
      reports: feed.latest || {}
    },
    "widget.json": {
      source: feed.source,
      fetchedAt: feed.fetchedAt,
      stale: Boolean(feed.stale),
      items: buildWidget(feed, codes)
    },
    "activity-levels.json": feed.activityLevels || null,
    "daily-summary.json": feed.dailySummary || null,
    "seismic-90d.json": feed.seismic90d || {},
    "eruptions.json": feed.recentEruptions || null,
    "volcano-status.md": renderVolcanoStatusMarkdown(feed, codes)
  };
}

export function renderVolcanoStatusMarkdown(feed, codes = DEFAULT_VOLCANO_CODES) {
  const lines = [
    "# JVTO Volcano Travel Advisory Snapshot",
    "",
    `Generated: ${feed.fetchedAt || new Date().toISOString()}`,
    `Source: ${feed.source || "MAGMA Indonesia / PVMBG"}`,
    "",
    "> JVTO uses this as an operational travel advisory. It is not an official emergency instruction. Always follow MAGMA Indonesia/PVMBG and local authority updates.",
    "",
    "| Code | Volcano | Status | Latest report | Period | Visitor implication | Source |",
    "|---|---|---|---|---|---|---|"
  ];

  for (const code of codes) {
    const report = feed.latest?.[code];
    lines.push(
      [
        code,
        escapeCell(report?.name || code),
        escapeCell(report?.statusLevel || "Unknown"),
        escapeCell(report?.reportDate || ""),
        escapeCell(report?.period || ""),
        escapeCell(report?.recommendations?.[0] || "Follow latest PVMBG/MAGMA guidance."),
        report?.sourceUrl ? `[MAGMA report](${report.sourceUrl})` : ""
      ].join(" | ").replace(/^/, "| ").replace(/$/, " |")
    );
  }

  lines.push("", "## Seismic 90-Day Summary", "");
  for (const code of codes) {
    const summary = feed.seismic90d?.[code]?.summary;
    if (!summary) {
      lines.push(`- ${code}: no cached 90-day seismic summary.`);
      continue;
    }
    const totals = (summary.series || [])
      .filter((series) => Number(series.total90) > 0)
      .map((series) => `${series.name} ${series.total90}`)
      .join(", ");
    lines.push(`- ${code}: ${summary.days} days until ${summary.lastDate}; ${totals || "no non-zero events in cached series"}.`);
  }

  lines.push("", "## Recent Eruptions", "");
  const eruptions = feed.recentEruptions?.items || [];
  if (!eruptions.length) {
    lines.push("- No cached recent eruption items.");
  } else {
    for (const eruption of eruptions.slice(0, 10)) {
      lines.push(`- ${[eruption.dateLabel, eruption.time, eruption.volcanoName].filter(Boolean).join(" ")}: ${eruption.information}`);
    }
  }

  lines.push("", `Project root: ${ROOT_DIR}`, "");
  return `${lines.join("\n")}\n`;
}

function escapeCell(value) {
  return String(value || "").replace(/\|/g, "\\|").replace(/\s+/g, " ").trim();
}
