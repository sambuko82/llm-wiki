const ENTITY_MAP = {
  amp: "&",
  lt: "<",
  gt: ">",
  quot: "\"",
  apos: "'",
  nbsp: " ",
  deg: "°"
};

export function decodeHtml(value = "") {
  return String(value)
    .replace(/&#(\d+);/g, (_, code) => String.fromCharCode(Number(code)))
    .replace(/&#x([0-9a-f]+);/gi, (_, code) => String.fromCharCode(parseInt(code, 16)))
    .replace(/&([a-z]+);/gi, (_, key) => ENTITY_MAP[key] ?? `&${key};`);
}

export function stripTags(value = "") {
  return decodeHtml(String(value).replace(/<br\s*\/?>/gi, "\n").replace(/<[^>]*>/g, " "))
    .replace(/\s+/g, " ")
    .trim();
}

export function splitParagraphList(value = "") {
  const withBreaks = decodeHtml(String(value).replace(/<br\s*\/?>/gi, "\n"));
  return withBreaks
    .replace(/<[^>]*>/g, " ")
    .split(/\n+|(?=\s*\d+[.)]\s+)/)
    .map((item) => item.replace(/^\s*\d+[.)]\s*/, "").replace(/\s+/g, " ").trim())
    .filter(Boolean);
}

export function matchOne(html, pattern, fallback = "") {
  const match = pattern.exec(html);
  return match ? stripTags(match[1]) : fallback;
}

export function attrValue(tag, attr) {
  const pattern = new RegExp(`${attr}=["']([^"']+)["']`, "i");
  const match = pattern.exec(tag);
  return match ? decodeHtml(match[1]).trim() : "";
}
