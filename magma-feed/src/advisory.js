const CORE_RESTRICTIONS = {
  IJE: {
    en: "Do not descend to or approach the Kawah Ijen crater lake floor; do not camp within 500 m of the crater.",
    id: "Jangan turun atau mendekati dasar danau Kawah Ijen; jangan bermalam/berkemah dalam radius 500 m dari kawah."
  },
  BRO: {
    en: "Do not enter within 1 km of Bromo's active crater while Level II restrictions remain in place.",
    id: "Jangan memasuki area dalam radius 1 km dari kawah aktif Bromo selama pembatasan Level II masih berlaku."
  }
};

export function buildWidget(feed, codes) {
  return codes.map((code) => {
    const report = feed.latest?.[code];
    return {
      code,
      name: report?.name || code,
      statusLevel: report?.statusLevel || "Unknown",
      reportDate: report?.reportDate || "",
      period: report?.period || "",
      coreRestriction: restrictionFor(code, "en", report),
      sourceUrl: report?.sourceUrl || "",
      lastChecked: feed.fetchedAt,
      stale: Boolean(feed.stale)
    };
  });
}

export function generateTravelAdvisory(report, options = {}) {
  const language = (options.language || "en").toLowerCase();
  const tourDate = options.tourDate || "your tour date";
  const restriction = restrictionFor(report.volcanoCode, language, report);
  const officialSource = "MAGMA Indonesia / PVMBG";

  if (language.startsWith("id")) {
    return [
      `Advisory JVTO untuk ${report.name} (${tourDate})`,
      `Status resmi terakhir: ${report.statusLevel}, laporan ${report.reportDate}, periode ${report.period}.`,
      `Implikasi tamu: ${restriction}`,
      `Ringkasan visual: ${report.visual}`,
      `Sumber resmi: ${officialSource}. JVTO menggunakan informasi ini sebagai travel advisory operasional, bukan pengganti instruksi resmi darurat.`
    ].join("\n\n");
  }

  return [
    `JVTO travel advisory for ${report.name} (${tourDate})`,
    `Latest official status: ${report.statusLevel}, report date ${report.reportDate}, period ${report.period}.`,
    `Guest implication: ${restriction}`,
    `Visual summary: ${report.visual}`,
    `Official source: ${officialSource}. JVTO uses this as an operational travel advisory, not a replacement for official emergency instructions.`
  ].join("\n\n");
}

function firstRecommendation(report) {
  return report?.recommendations?.[0] || "Follow the latest MAGMA Indonesia / PVMBG recommendation.";
}

function restrictionFor(code, language, report) {
  const localized = CORE_RESTRICTIONS[code];
  if (!localized) return firstRecommendation(report);
  return localized[language.startsWith("id") ? "id" : "en"];
}
