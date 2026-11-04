// Herbaferm chat proxy (Cloudflare Worker). Keeps the model API key on the server.
// Free default: Cloudflare Workers AI (no key). Just run `npx wrangler deploy`.
// Optional: `npx wrangler secret put ANTHROPIC_API_KEY` to use Claude instead.
// Then add this line to site/index.html before the chat script:
//   <script>window.HF_CHAT_ENDPOINT = "https://<your-worker>.workers.dev/";</script>
const ALLOWED_ORIGINS = ["https://herbafermsg.com", "https://www.herbafermsg.com", "https://ernusho.github.io"]; // add your preview URL while testing
const MODEL = "claude-haiku-5-5";
const CF_MODEL = "@cf/meta/llama-3.1-8b-instruct-fp8";
const MAX_MESSAGES = 10;
const MAX_CHARS = 30000; // the first message carries the fact sheet

export default {
  async fetch(request, env) {
    const origin = request.headers.get("origin") || "";
    const ok = ALLOWED_ORIGINS.includes(origin);
    const cors = {
      "access-control-allow-origin": ok ? origin : ALLOWED_ORIGINS[0],
      "access-control-allow-methods": "POST, OPTIONS",
      "access-control-allow-headers": "content-type",
      "vary": "origin",
    };
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (request.method !== "POST" || !ok) return new Response("Not allowed", { status: 403, headers: cors });

    let body;
    try { body = await request.json(); } catch { return new Response("Bad request", { status: 400, headers: cors }); }
    const messages = (body.messages || []).slice(-MAX_MESSAGES)
      .filter(m => (m.role === "user" || m.role === "assistant") && typeof m.content === "string")
      .map(m => ({ role: m.role, content: m.content.slice(0, MAX_CHARS) }));
    if (!messages.length || messages[0].role !== "user") return new Response("Bad request", { status: 400, headers: cors });

    if (!env.ANTHROPIC_API_KEY) {
      if (!env.AI) return new Response("AI error: the AI binding is missing", { status: 502, headers: cors });
      try {
        // the first message carries the fact sheet and rules: send it as the system prompt
        const out = await env.AI.run(CF_MODEL, {
          max_tokens: 400,
          messages: [{ role: "system", content: messages[0].content }, ...messages.slice(1)],
        });
        const text = (out && out.response) || "";
        if (!text) return new Response("AI error: empty reply " + JSON.stringify(out).slice(0, 300), { status: 502, headers: cors });
        return new Response(JSON.stringify({ text }), { headers: { ...cors, "content-type": "application/json" } });
      } catch (e) { return new Response("AI error: " + String((e && e.message) || e), { status: 502, headers: cors }); }
    }

    const res = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "content-type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
      body: JSON.stringify({ model: MODEL, max_tokens: 500, messages }),
    });
    if (!res.ok) return new Response("Upstream error", { status: 502, headers: cors });
    const data = await res.json();
    const text = (data.content || []).filter(b => b.type === "text").map(b => b.text).join("");
    return new Response(JSON.stringify({ text }), { headers: { ...cors, "content-type": "application/json" } });
  },
};
