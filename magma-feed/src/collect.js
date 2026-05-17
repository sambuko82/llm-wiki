import { collectMagmaFeed } from "./collector.js";

const feed = await collectMagmaFeed();
console.log(JSON.stringify(feed, null, 2));
