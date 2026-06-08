---
updated: 2026-05-17T17:58:14Z
created: 2026-05-17T17:58:14Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: hermes_local adapter — runs Hermes Agent locally for Paperclip with persistent sessions, multi-provider routing, 30+ tools, and filesystem checkpoints.
tags: [paperclip, hermes-agent, adapter, local, multi-provider]
sources: https://docs.paperclip.ing/#/reference/adapters/hermes-local
status: reference
confidence: 0.9
---

## Core Insight

The `hermes_local` adapter runs full Hermes Agent on the same machine as Paperclip — giving you persistent memory, 30+ tools, 80+ skills, multi-provider routing (Anthropic, OpenRouter, OpenAI, Nous, Codex, ZAI, Kimi, MiniMax), and filesystem checkpoints. Sessions persist across heartbeats via `hermes --resume`.

## Key Claims

| Field | Default | Notes |
|-------|---------|-------|
| `model` | `anthropic/claude-sonnet-4` | In `provider/model` format |
| `toolsets` | all | terminal, file, web, browser, code_execution, vision, mcp, creative, productivity |
| `persistSession` | `true` | Resume via Hermes `--resume` |
| `checkpoints` | `false` | Filesystem rollback safety |
| `timeoutSec` | `300` | Execution timeout |
| `provider` | auto-detected | openrouter, nous, openai-codex, zai, kimi-coding, minimax, minimax-cn |

Skills merge from Paperclip-managed (UI-togglable) and Hermes-native (`~/.hermes/skills/`, read-only, always loaded).

## Connections
- [[wiki/index]]
- [[sources/documentation/paperclip-hermes-adapter]]
- [[sources/documentation/paperclip-api]]
- [[sources/repositories/paperclip]]
- [[paperclip-hermes-adapter]]

- [[entities/tools/hermes-agent]] — the agent being adapter
- [[paperclip]] — parent orchestration system
