---
summary: chopratejas/headroom — context compression library/proxy/MCP server for LLM agents. 60-95% token reduction on tool outputs, logs, files, RAG chunks, and conversation history. 6 algorithms, local-first, reversible. Sits between agent tool calls and the LLM context window.
tags: [headroom, context-compression, token-reduction, mcp-server, agent-infrastructure, llm-inference, rag]
updated: 2026-06-03T12:57:01Z
created: 2026-06-03T12:57:01Z
---

---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "chopratejas/headroom — context compression library/proxy/MCP server for LLM agents. 60-95% token reduction on tool outputs, logs, files, RAG chunks, and conversation history. 6 algorithms, local-first, reversible. Sits between agent tool calls and the LLM context window."
tags: [headroom, context-compression, token-reduction, mcp-server, agent-infrastructure, llm-inference, rag]
sources:
  - https://github.com/chopratejas/headroom
status: active
confidence: 0.85
---

# chopratejas/headroom — Context Compression Layer for AI Agents

**Repository**: https://github.com/chopratejas/headroom
**Author**: chopratejas
**Captured**: 2026-06-03
**Archived**: `Clippings/repositories/2026/chopratejasheadroom Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server..md` (14KB)

## What It Does

Headroom compresses everything an AI agent reads — **tool outputs, logs, RAG chunks, files, and conversation history** — before it reaches the LLM. Same answers, fraction of the tokens.

The tagline "60–95% fewer tokens" is backed by a live demo figure: 10,144 → 1,260 tokens (12.4% of original) on a FATAL-pattern detection task, with the FATAL still found.

## The Three Modes

| Mode | Interface | Use case |
| --- | --- | --- |
| **Library** | `compress(messages)` in Python or TypeScript | Inline in any app |
| **Proxy** | Sits between agent and LLM API | Drop-in front of OpenAI/Anthropic/local |
| **MCP server** | Exposes compression as a tool | Any MCP-compatible agent |

The same engine, three different access patterns. Library mode is for explicit, controllable use; proxy mode is for transparent always-on compression; MCP mode is for agent-driven selective compression (the agent decides which tool calls to compress).

## The 6 Algorithms

Six compression algorithms are exposed, presumably with different tradeoffs along:

- Lossiness (reversible vs lossy)
- Compression ratio (60% vs 95%)
- Latency cost
- Suitability for code vs prose vs structured data

(The full algorithm list is in the GitHub repo; this summary captures the existence of the algorithmic diversity, not the per-algorithm details.)

## Agent Compatibility

Headroom is presented as agent-agnostic. The compatibility matrix lists supported integrations (specific names not captured in the README excerpt, but the framing is "any agent that produces tool outputs, logs, or RAG chunks").

## How It Compares

The README's "Compared to" section positions Headroom against:

- **Naive truncation** — Headroom is structure-aware, not just first-N-tokens
- **Context summarization** — Headroom is *lossless on the relevant* content, not lossy-summary
- **Other compression libraries** — Headroom is agent-shaped (tool-output-aware), not just text-shaping
- **RAG chunking** — Headroom compresses *after* RAG has produced chunks; it is the second compression stage

## When to Use vs When to Skip

- **Use** when: agent context is being filled by tool outputs, logs, or RAG chunks; cost matters; long-running agent sessions are filling the context window; you want to preserve retrieval accuracy.
- **Skip** when: the agent is short-running and context fits trivially; the LLM is local and token cost is zero; the agent's value is in producing long-form generation rather than reading long tool output.

## Reversibility Claim

The README emphasizes "reversible" as a feature. This means the compression can be undone — the original content can be reconstructed from the compressed form. This is a load-bearing property for any compression that an agent might use during a session, because the agent might need the *full* original content (not the compressed form) to act on it.

## Local-First

The architecture is local-first — compression happens on the agent's machine, not via a cloud API. This matters for:

- **Privacy** — tool outputs and logs do not leave the local machine
- **Latency** — no network round-trip
- **Cost** — no per-token compression cost

## Connections

- [[entities/tools/headroom]] — entity page for the tool (TODO: create)
- [[concepts/context-compression]] — concept page for the technique (TODO: create)
- [[concepts/llm-inference]] — the inference context window is the constraint being optimized
- [[concepts/rag]] — Headroom compresses RAG chunks as a second stage
- [[concepts/model-serving]] — proxy mode sits in the model-serving path
- [[concepts/quantization]] — analogous technique for model weights; Headroom is a "quantization for context" in spirit
- [[concepts/bounded-rationality]] — context compression is a form of bounded-rationality engineering

## Why This Matters for the LLM-WIKI

The LLM-WIKI is a knowledge compilation system that already does *some* of what Headroom does — the [[mop-edm-cognitive-architecture|MOP-EFHF]] synthesis and [[edm-framework|EDM]] invalidation pipeline are *semantic* compression, not *token* compression. Headroom is a **complementary** layer that operates at the byte/token level, not the semantic level.

A potential integration: route large raw-ingestion files through Headroom's proxy mode before they hit the `wiki_ingest_raw` MCP, so the ingest pipeline sees a compressed (but reversible) form. The 60-95% token reduction would translate directly to reduced LLM cost on the ingest side. Worth a [[synthesis/_briefs/headroom-llm-wiki-integration|synthesis brief]].

## Methodological Note

This is a **third-party tool README**, not an AGEM corpus or a research paper. The pattern: capture the *existence* of the tool, the *position* in the agent infrastructure landscape, the *integration potential* with the LLM-WIKI, and the *cited comparisons* to existing techniques. The full technical detail is in the GitHub repo and `headroom-docs.vercel.app`.
