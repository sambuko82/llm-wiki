import { DEFAULT_VOLCANO_CODES } from "./config.js";
import { generateTravelAdvisory } from "./advisory.js";

export const MCP_TOOLS = [
  {
    name: "get_latest_volcano_report",
    description: "Get the latest cached MAGMA/PVMBG volcano report for a JVTO destination code.",
    inputSchema: {
      type: "object",
      properties: {
        code: { type: "string", enum: DEFAULT_VOLCANO_CODES }
      },
      required: ["code"]
    },
    annotations: { readOnlyHint: true, destructiveHint: false }
  },
  {
    name: "get_activity_levels",
    description: "Get the latest cached MAGMA/PVMBG national volcano activity level table.",
    inputSchema: { type: "object", properties: {} },
    annotations: { readOnlyHint: true, destructiveHint: false }
  },
  {
    name: "get_daily_volcano_summary",
    description: "Get MAGMA/PVMBG daily volcano summary for a YYYY-MM-DD date.",
    inputSchema: {
      type: "object",
      properties: {
        date: { type: "string", pattern: "^\\d{4}-\\d{2}-\\d{2}$" }
      },
      required: ["date"]
    },
    annotations: { readOnlyHint: true, destructiveHint: false }
  },
  {
    name: "get_seismic_90d",
    description: "Get cached 90-day seismic chart data and summary for a JVTO volcano code.",
    inputSchema: {
      type: "object",
      properties: {
        code: { type: "string", enum: DEFAULT_VOLCANO_CODES }
      },
      required: ["code"]
    },
    annotations: { readOnlyHint: true, destructiveHint: false }
  },
  {
    name: "get_recent_eruptions",
    description: "Get recent MAGMA/PVMBG eruption information from the cached eruption page.",
    inputSchema: {
      type: "object",
      properties: {
        page: { type: "number", minimum: 1, default: 1 }
      }
    },
    annotations: { readOnlyHint: true, destructiveHint: false }
  },
  {
    name: "generate_jvto_travel_advisory",
    description: "Generate a JVTO guest-facing travel advisory from the latest cached MAGMA/PVMBG report.",
    inputSchema: {
      type: "object",
      properties: {
        code: { type: "string", enum: DEFAULT_VOLCANO_CODES },
        tourDate: { type: "string" },
        language: { type: "string", enum: ["en", "id"] }
      },
      required: ["code"]
    },
    annotations: { readOnlyHint: true, destructiveHint: false }
  }
];

export async function handleMcpRequest(body, feedProvider) {
  const request = Array.isArray(body) ? body : [body];
  const responses = [];

  for (const message of request) {
    responses.push(await handleSingle(message, feedProvider));
  }

  return Array.isArray(body) ? responses : responses[0];
}

async function handleSingle(message, feedProvider) {
  const { id, method, params = {} } = message;

  try {
    if (method === "initialize") {
      return result(id, {
        protocolVersion: params.protocolVersion || "2025-06-18",
        serverInfo: { name: "jvto-magma-feed", version: "0.1.0" },
        capabilities: { tools: {} }
      });
    }

    if (method === "tools/list") {
      return result(id, { tools: MCP_TOOLS });
    }

    if (method === "tools/call") {
      return result(id, await callTool(params.name, params.arguments || {}, feedProvider));
    }

    return error(id, -32601, `Unsupported MCP method: ${method}`);
  } catch (err) {
    return error(id, -32000, err.message);
  }
}

async function callTool(name, args, feedProvider) {
  const feed = await feedProvider();
  const code = String(args.code || "").toUpperCase();

  if (name === "get_latest_volcano_report") return content(feed.latest?.[code] || null);
  if (name === "get_activity_levels") return content(feed.activityLevels || null);
  if (name === "get_daily_volcano_summary") {
    if (feed.dailySummary?.date === args.date) return content(feed.dailySummary);
    throw new Error(`No cached daily summary found for ${args.date}; refresh collector or use the REST endpoint.`);
  }
  if (name === "get_seismic_90d") return content(feed.seismic90d?.[code] || null);
  if (name === "get_recent_eruptions") {
    const page = Math.max(1, Number(args.page || 1) || 1);
    if (feed.recentEruptions?.page === page) return content(feed.recentEruptions);
    throw new Error(`No cached eruption page found for page ${page}; refresh collector or use the REST endpoint.`);
  }
  if (name === "generate_jvto_travel_advisory") {
    const report = feed.latest?.[code];
    if (!report) throw new Error(`No cached report found for ${code}`);
    return {
      content: [{ type: "text", text: generateTravelAdvisory(report, args) }]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
}

function content(data) {
  return {
    content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
    structuredContent: data
  };
}

function result(id, value) {
  return { jsonrpc: "2.0", id, result: value };
}

function error(id, code, message) {
  return { jsonrpc: "2.0", id, error: { code, message } };
}
