import test from "node:test";
import assert from "node:assert/strict";
import { handleMcpRequest } from "../src/mcp.js";

const feed = {
  latest: {
    IJE: {
      volcanoCode: "IJE",
      name: "Ijen",
      statusLevel: "Level I (Normal)",
      reportDate: "Sabtu - 16 Mei 2026",
      period: "00:00-24:00 WIB",
      visual: "Asap putih tipis.",
      recommendations: ["Tidak turun ke dasar kawah."]
    }
  },
  seismic90d: {
    IJE: { summary: { lastDate: "2026-05-16", series: [] } }
  },
  activityLevels: { counts: { "Level I (Normal)": 43 } },
  dailySummary: { date: "2026-05-17", rows: [] },
  recentEruptions: { page: 1, items: [{ volcanoName: "Lewotobi Laki-laki" }] }
};

test("MCP tools/list returns read-only tools", async () => {
  const response = await handleMcpRequest(
    { jsonrpc: "2.0", id: 1, method: "tools/list" },
    async () => feed
  );

  assert.equal(response.result.tools.length, 6);
  assert.equal(response.result.tools[0].annotations.readOnlyHint, true);
});

test("MCP eruption tool returns cached eruption page", async () => {
  const response = await handleMcpRequest(
    {
      jsonrpc: "2.0",
      id: 3,
      method: "tools/call",
      params: {
        name: "get_recent_eruptions",
        arguments: { page: 1 }
      }
    },
    async () => feed
  );

  assert.equal(response.result.structuredContent.items[0].volcanoName, "Lewotobi Laki-laki");
});

test("MCP advisory tool uses cached report", async () => {
  const response = await handleMcpRequest(
    {
      jsonrpc: "2.0",
      id: 2,
      method: "tools/call",
      params: {
        name: "generate_jvto_travel_advisory",
        arguments: { code: "IJE", tourDate: "2026-05-20", language: "en" }
      }
    },
    async () => feed
  );

  assert.match(response.result.content[0].text, /JVTO travel advisory for Ijen/);
  assert.match(response.result.content[0].text, /MAGMA Indonesia \/ PVMBG/);
});
