import { copyFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";

const wikiRoot = process.env.JVTO_LLM_WIKI_PATH || "E:\\Users\\JAVA VOLCANO\\llm-wiki";
const source = new URL("../exports/volcano-status.md", import.meta.url);
const target = join(wikiRoot, "wiki", "ops", "volcano-status.md");

await mkdir(dirname(target), { recursive: true });
await copyFile(source, target);
console.log(`Synced ${source.pathname} to ${target}`);
