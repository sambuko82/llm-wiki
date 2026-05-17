export const MAGMA_BASE_URL = process.env.MAGMA_BASE_URL || "https://magma.esdm.go.id";

export const DEFAULT_VOLCANO_CODES = (process.env.MAGMA_CODES || "IJE,BRO")
  .split(",")
  .map((code) => code.trim().toUpperCase())
  .filter(Boolean);

export const CACHE_TTL_MS = Number(process.env.MAGMA_CACHE_TTL_MS || 60 * 60 * 1000);
export const LOOKBACK_DAYS = Number(process.env.MAGMA_LOOKBACK_DAYS || 7);
export const CACHE_PATH = process.env.MAGMA_CACHE_PATH || new URL("../data/magma-cache.json", import.meta.url);

export const VOLCANO_NAMES = {
  IJE: "Ijen",
  BRO: "Bromo"
};

export const USER_AGENT =
  process.env.MAGMA_USER_AGENT ||
  "JVTO-MAGMA-Feed/0.1 (+https://javavolcano-touroperator.com; source attribution: MAGMA Indonesia/PVMBG)";
