import { getCachedOrFresh } from "./collector.js";
import { writeExports } from "./exporter.js";

const feed = await getCachedOrFresh();
const result = await writeExports(feed);
console.log(`Wrote MAGMA exports to ${result.outputDir}`);
for (const file of result.files) console.log(`- ${file}`);
