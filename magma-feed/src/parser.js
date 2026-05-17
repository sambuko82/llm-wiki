import { attrValue, matchOne, splitParagraphList, stripTags } from "./html.js";

export function parseReportDetail(html, sourceUrl = "") {
  const title = matchOne(html, /<title>\s*([\s\S]*?)<\/title>/i);
  const statusLevel = matchOne(html, /<span class="badge[^"]*">\s*([\s\S]*?)<\/span>/i);
  const cardTitle = matchOne(html, /<h5 class="card-title[^"]*">\s*([\s\S]*?)<\/h5>/i, title);
  const author = matchOne(html, /Dibuat oleh,\s*([^<]+)<\/p>/i);
  const imageTag = /<img class="img-fluid"[^>]+>/i.exec(html)?.[0] || "";
  const imageUrl = attrValue(imageTag, "src");
  const reportId = /\/laporan\/(\d+)/.exec(sourceUrl)?.[1] || /data:\s*\{id:\s*'(\d+)'/.exec(html)?.[1] || "";
  const volcanoCode = /MAG_CODE='([^']+)'/.exec(html)?.[1] || "";

  const geo = /Gunung Api\s+(.+?)\s+terletak di Kab\\Kota\s+(.+?)\s+dengan posisi geografis di Latitude\s+(-?\d+(?:\.\d+)?)&deg;LU,\s+Longitude\s+(-?\d+(?:\.\d+)?)&deg;BT\s+dan memiliki ketinggian\s+(\d+)\s+mdpl/i.exec(html);

  const [, nameFromTitle = "", datePart = "", periodPart = ""] =
    /Laporan Aktivitas Gunung Api -\s*(.+?),\s*(.+?),\s*periode\s*(.+)$/i.exec(title) || [];

  const visual = sectionParagraph(html, "Pengamatan Visual");
  const climate = sectionParagraph(html, "Klimatologi");
  const notes = sectionParagraph(html, "Keterangan Lainnya");
  const recommendationsHtml = sectionParagraphHtml(html, "Rekomendasi");

  return {
    sourceUrl,
    reportId,
    volcanoCode,
    name: geo?.[1]?.trim() || nameFromTitle.trim(),
    statusLevel,
    period: periodPart.trim(),
    reportDate: datePart.trim(),
    title: cardTitle,
    author,
    location: geo?.[2]?.trim() || "",
    lat: geo ? Number(geo[3]) : null,
    lon: geo ? Number(geo[4]) : null,
    elevation: geo ? Number(geo[5]) : null,
    visual,
    climate,
    seismic: parseSeismic(html),
    recommendations: splitParagraphList(recommendationsHtml),
    notes,
    imageUrl,
    fetchedAt: new Date().toISOString()
  };
}

export function parseSearchResults(html) {
  const items = [];
  const itemPattern = /<div class="timeline-item">\s*<div class="timeline-time">\s*<small>([\s\S]*?)<\/small>[\s\S]*?<p class="timeline-title">([\s\S]*?)<\/p>\s*<p class="timeline-author">([\s\S]*?)<\/p>[\s\S]*?<p>([\s\S]*?)<\/p>\s*<a href="([^"]+)" class="card-link">/gi;
  let match;

  while ((match = itemPattern.exec(html))) {
    const titleHtml = match[2];
    const authorText = stripTags(match[3]);
    const authorMatch = /Dibuat oleh\s+(.+?)\s+-\s+(.+)$/i.exec(authorText);
    items.push({
      period: stripTags(match[1]),
      name: matchOne(titleHtml, /<a[^>]*>([\s\S]*?)<\/a>/i),
      statusLevel: matchOne(titleHtml, /<span class="badge[^"]*">([\s\S]*?)<\/span>/i),
      author: authorMatch?.[1]?.trim() || "",
      reportDate: authorMatch?.[2]?.trim() || "",
      summary: stripTags(match[4]),
      sourceUrl: match[5],
      reportId: /\/laporan\/(\d+)/.exec(match[5])?.[1] || ""
    });
  }

  return items;
}

export function parseActivityLevels(html) {
  const counts = {};
  const countPattern = /<h1>\s*(\d+)\s*<\/h1>\s*<p>\s*(Level\s+[IVX]+\s*\([^)]+\))\s*<\/p>/gi;
  let countMatch;
  while ((countMatch = countPattern.exec(html))) {
    counts[countMatch[2]] = Number(countMatch[1]);
  }

  const volcanoes = [];
  const linkPattern = /([^<>\n]+?)\s+-\s*([^<>\n]+?)\s*<a href="([^"]+\/laporan\/(\d+)\?signature=[^"]+)"/gi;
  let linkMatch;
  while ((linkMatch = linkPattern.exec(html))) {
    const prefix = html.slice(0, linkMatch.index);
    volcanoes.push({
      name: stripTags(linkMatch[1]),
      province: stripTags(linkMatch[2]),
      statusLevel: latestLevelBefore(prefix),
      sourceUrl: linkMatch[3],
      reportId: linkMatch[4]
    });
  }

  return {
    counts,
    volcanoes,
    fetchedAt: new Date().toISOString()
  };
}

export function parseDailySummary(html, sourceUrl = "") {
  const title = matchOne(html, /<h6 class="slim-pagetitle">\s*([\s\S]*?)<\/h6>/i);
  const rows = [];
  const rowPattern = /<tr>\s*<td>\s*\d+\s*<\/td>\s*<td>([\s\S]*?)<\/td>\s*<td>([\s\S]*?)<\/td>\s*<td>([\s\S]*?)<\/td>\s*<td>([\s\S]*?)<\/td>\s*<\/tr>/gi;
  let match;

  while ((match = rowPattern.exec(html))) {
    rows.push({
      name: stripTags(match[1]),
      visual: splitParagraphList(match[2]).join(" "),
      seismic: extractListItems(match[3]),
      recommendations: extractListItems(match[4])
    });
  }

  return {
    sourceUrl,
    title,
    date: /(\d{4}-\d{2}-\d{2})/.exec(sourceUrl)?.[1] || "",
    rows,
    fetchedAt: new Date().toISOString()
  };
}

export function summarizeSeismicChart(chart) {
  const categories = chart?.categories || [];
  const lastDate = categories[categories.length - 1] || "";
  const series = (chart?.series || []).map((item) => {
    const data = Array.isArray(item.data) ? item.data.map(Number) : [];
    return {
      name: item.name,
      color: item.color,
      total90: data.reduce((sum, value) => sum + value, 0),
      latest: data[data.length - 1] ?? 0
    };
  });

  return {
    lastDate,
    days: categories.length,
    series
  };
}

function sectionParagraph(html, heading) {
  return stripTags(sectionParagraphHtml(html, heading));
}

function sectionParagraphHtml(html, heading) {
  const pattern = new RegExp(`<h6 class="slim-card-title">\\s*${escapeRegExp(heading)}\\s*<\\/h6>\\s*<p>([\\s\\S]*?)<\\/p>`, "i");
  return pattern.exec(html)?.[1] || "";
}

function parseSeismic(html) {
  const match = /<h6 class="slim-card-title">\s*Pengamatan Kegempaan\s*<\/h6>([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/i.exec(html);
  if (!match) return [];

  const seismic = [];
  const paragraphPattern = /<p>([\s\S]*?)<\/p>/gi;
  let paragraph;
  while ((paragraph = paragraphPattern.exec(match[1]))) {
    const text = stripTags(paragraph[1]);
    if (text) seismic.push(text);
  }
  return seismic;
}

function extractListItems(html) {
  const items = [];
  const itemPattern = /<li>([\s\S]*?)<\/li>/gi;
  let match;
  while ((match = itemPattern.exec(html))) {
    items.push(stripTags(match[1]).replace(/^\d+[.)]\s*/, ""));
  }
  return items;
}

function latestLevelBefore(prefix) {
  const levels = ["Level IV (Awas)", "Level III (Siaga)", "Level II (Waspada)", "Level I (Normal)"];
  let latest = "";
  let latestIndex = -1;
  for (const level of levels) {
    const index = prefix.lastIndexOf(level);
    if (index > latestIndex) {
      latest = level;
      latestIndex = index;
    }
  }
  return latest;
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
