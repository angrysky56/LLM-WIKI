---
updated: 2026-05-17T17:57:43Z
created: 2026-05-17T17:57:43Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: OpenClaw — personal AI assistant via messaging channels (WhatsApp, Telegram, Discord, Slack, etc.), runs locally, supports voice/canvas. Gateway as control plane, assistant as product.
tags: [openclaw, ai-assistant, messaging, telegram, discord, local]
sources: https://github.com/openclaw/openclaw
status: reference
confidence: 0.9
---

## Core Insight

OpenClaw is a personal AI assistant you run on your own devices — answers on channels you already use (WhatsApp, Telegram, Discord, Slack, iMessage, Signal, etc.), speaks and listens on macOS/iOS/Android, renders a live Canvas. The Gateway is just the control plane; the product is the always-on assistant.

## Key Claims

| Feature | Detail |
|---------|--------|
| **Channels** | WhatsApp, Telegram, Slack, Discord, Signal, iMessage, IRC, Teams, Matrix, Feishu, LINE, WeChat, QQ, and 15+ more |
| **Runtime** | Node 24 (recommended) or Node 22.16+ |
| **Install** | `npm install -g openclaw@latest` then `openclaw onboard --install-daemon` |
| **Daemon** | Runs as launchd/systemd user service — stays running |
| **Model-agnostic** | OpenAI, Claude, any Ollama model, and more |
| **`ollama launch`** | Works with OpenClaw: `ollama launch openclaw --model gemma4` |

OpenClaw as the execution layer in a stack: Hermes (memory) + OpenClaw (execution) + Paperclip (management).

## Connections
- [[sources/repositories/gbrain]]
- [[sources/articles/hermes-openclaw-paperclip-stack]]
- [[sources/repositories/openclaw]]
- [[sources/repositories/paperclip]]
- [[index]]
- [[sources/documentation/hermes-mcp-integration]]
- [[sources/documentation/acp-editor-integration-hermes-agent]]
- [[openclaw]]

- [[ollama]] — supports Ollama launched models
- [[paperclip]] — orchestration layer
- [[hermes-agent]] — memory layer in integrated stack
