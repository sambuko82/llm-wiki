import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { CACHE_PATH } from "./config.js";

export async function readCache(path = CACHE_PATH) {
  try {
    const data = await readFile(toPath(path), "utf8");
    return JSON.parse(data);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

export async function writeCache(cache, path = CACHE_PATH) {
  const target = toPath(path);
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, `${JSON.stringify(cache, null, 2)}\n`, "utf8");
  return cache;
}

export function isFresh(cache, ttlMs) {
  if (!cache?.fetchedAt) return false;
  return Date.now() - new Date(cache.fetchedAt).getTime() < ttlMs;
}

function toPath(pathOrUrl) {
  return pathOrUrl instanceof URL ? fileURLToPath(pathOrUrl) : pathOrUrl;
}
