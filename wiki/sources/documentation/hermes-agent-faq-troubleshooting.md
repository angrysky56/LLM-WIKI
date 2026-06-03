
---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "Official Hermes Agent FAQ — providers (OpenRouter, Nous Portal, OpenAI, Anthropic, Google, MiniMax, local), Windows/WSL2, Termux, Chrome control, OAuth, MCP, troubleshooting"
tags: [hermes-agent, documentation, faq, troubleshooting, providers, wsl2, termux]
sources: https://hermes-agent.nousresearch.com/docs/reference/faq
status: active
confidence: 0.9
---

# Hermes Agent FAQ & Troubleshooting

Quick answers for common Hermes Agent questions.

## Supported LLM Providers

- **OpenRouter** — recommended for flexibility (hundreds of models)
- **Nous Portal** — Nous Research's own endpoint
- **OpenAI** — GPT-5.4, GPT-5-codex, GPT-4.1, GPT-4o
- **Anthropic** — Claude via direct API, OAuth, OpenRouter, or proxy
- **Google** — Gemini via `gemini` provider, `google-gemini-cli` OAuth, or OpenRouter
- **z.ai / ZhipuAI** — GLM models
- **Kimi / Moonshot AI**
- **MiniMax** — global and China endpoints
- **Local models** — via Ollama, vLLM, llama.cpp, SGLang

## Platform Support

### Windows / WSL2
Not natively Windows — requires Unix-like environment. WSL2 recommended. Install via:
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### WSL2 → Windows Chrome
Prefer MCP bridge (`chrome-devtools-mcp`) over `/browser connect` for reliability across WSL2/Windows boundary.

### Android / Termux
Tested Termux install path available.

## OAuth & Authentication

`hermes auth add anthropic` for direct Anthropic OAuth.

## Connections
- [[hermes-agent]] — primary entity
- [[hermes-mcp-integration]] — MCP setup guide
- [[mcp-model-context-protocol]] — MCP protocol reference
- [[scheduled-tasks-cron-hermes-agent]] — cron setup
