---
updated: 2026-05-17T17:56:13Z
created: 2026-05-17T17:56:13Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Gemma 4 family from Google — 9.6GB e4b variant with 128K context, supports vision/audio/code/agentic tools across Ollama, Claude Code, OpenClaw, Hermes, Codex.
tags: [gemma, google, llm, multimodal, ollama, agentic]
sources: https://ollama.com/library/gemma4
status: reference
confidence: 0.95
---

## Core Insight

Gemma 4 delivers frontier-level performance at each size tier, designed for reasoning, agentic workflows, coding, and multimodal understanding. Available sizes range from 7.2GB (e2b) to 20GB (31b), with 128K-256K context windows, all supporting text+image input.

## Key Claims

| Model | Size | Context | Notes |
|-------|------|---------|-------|
| gemma4:latest/e4b | 9.6GB | 128K | Flagship variant |
| gemma4:e2b | 7.2GB | 128K | Smaller variant |
| gemma4:26b | 18GB | 256K | Larger variant |
| gemma4:31b | 20GB | 256K | Largest variant |
| gemma4:31b-cloud | — | 256K | Cloud variant |

Tool support: vision, thinking, audio, cloud, e2b, e4b, 26b, 31b variants.

## Connections
- [[sources/articles/truth-emotion-sacred-agem-analysis]]
- [[index]]
- [[sources/articles/frank-einstein-gemma-truth-emotion-sacred]]
- [[sources/documentation/acp-editor-integration-hermes-agent]]
- [[sources/articles/gemma4]]
- [[gemma4]]

- [[ollama]] — the runtime used for Gemma 4
- [[hermes-agent]] — Hermes can run Gemma 4 via `ollama launch hermes --model gemma4`
