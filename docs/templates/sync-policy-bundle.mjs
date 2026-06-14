#!/usr/bin/env node
// Template for jvto-web/scripts/sync-policy-bundle.mjs.
// Adjust LLM_WIKI_ROOT if jvto-web stores the llm-wiki path differently.

import { copyFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const REQUIRED_SCHEMA = "policy-bundle/v1.0";
const REQUIRED_CONSUMERS = ["checkout", "invoice", "whatsapp"];
const REQUIRED_FILES = [
  "_manifest.json",
  "policy-bundle.json",
  "consumer-bundles.json",
  "deprecated-wording-report.json",
  "gap-report.json",
];

const repoRoot = process.cwd();
const llmWikiRoot =
  process.env.LLM_WIKI_ROOT || "E:\\Users\\JAVA VOLCANO\\llm-wiki";
const sourceDir = path.join(llmWikiRoot, "output", "website", "policy-bundle");
const targetDir = path.join(repoRoot, "src", "data", "policy-bundle");

async function readJson(filePath) {
  return JSON.parse(await readFile(filePath, "utf8"));
}

function fail(message) {
  throw new Error(`[sync-policy-bundle] ${message}`);
}

async function main() {
  const manifest = await readJson(path.join(sourceDir, "_manifest.json"));
  if (manifest.schema_version !== REQUIRED_SCHEMA) {
    fail(`schema_version mismatch: expected ${REQUIRED_SCHEMA}, got ${manifest.schema_version}`);
  }
  if (manifest.clean !== true) {
    fail("manifest.clean is not true");
  }

  const consumerBundles = await readJson(path.join(sourceDir, "consumer-bundles.json"));
  for (const consumer of REQUIRED_CONSUMERS) {
    if (!consumerBundles[consumer]) {
      fail(`consumer-bundles.json missing ${consumer}`);
    }
  }

  const deprecatedReport = await readJson(path.join(sourceDir, "deprecated-wording-report.json"));
  if (deprecatedReport.summary?.total_findings !== 0) {
    fail("deprecated-wording-report has findings");
  }

  const gapReport = await readJson(path.join(sourceDir, "gap-report.json"));
  if (gapReport.summary?.errors !== 0) {
    fail("gap-report has errors");
  }

  await mkdir(targetDir, { recursive: true });
  for (const file of REQUIRED_FILES) {
    await copyFile(path.join(sourceDir, file), path.join(targetDir, file));
  }

  console.log(
    `[sync-policy-bundle] copied ${REQUIRED_FILES.length} files to ${path.relative(repoRoot, targetDir)}`
  );
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});

