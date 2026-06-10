---
summary: Context optimization layer for LLM applications — compress tool outputs, logs, files, and RAG chunks before they reach the model
tags: [source, llm, context-optimization, compression, mcp]
updated: 2026-06-10T16:49:34Z
created: 2026-06-10T16:49:34Z
---

# Headroom — Context Optimization Layer for LLMs

**Source:** Headroom is a context optimization layer for LLM applications. It compresses tool outputs, logs, files, and RAG chunks before they reach the model, achieving 60–95% fewer tokens while preserving answer quality.

**Key Features:**
- **Compression pipeline:** Per-content-type compressors for JSON, code, logs, diffs, and text
- **Multiple delivery modes:** Python package (`headroom-ai`), TypeScript package, OpenAI/Anthropic-compatible HTTP proxy, and MCP server (tools: `headroom_compress`, `headroom_retrieve`, `headroom_stats`)
- **Local-first:** Apache 2.0 license, runs entirely locally
- **Deployed as:** Library, proxy server, or MCP server depending on use case

**Relevance:** Directly applicable to context window management in LLM applications, especially for agentic systems where tool output volume is high.

## Connections
- [[context-windowing]] — managing LLM context limits
- [[mcp-server]] — Model Context Protocol integration
- [[token-efficiency]] — reducing token consumption
