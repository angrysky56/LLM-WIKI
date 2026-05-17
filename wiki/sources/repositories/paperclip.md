---
updated: 2026-05-17T17:58:15Z
created: 2026-05-17T17:58:15Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Paperclip — open-source orchestration for AI companies. Task manager + org charts + budgets + governance + agent coordination. Bring your own agents (OpenClaw, Claude Code, Codex, etc.).
tags: [paperclip, orchestration, zero-human-company, autonomous, multi-agent]
sources: https://github.com/paperclipai/paperclip
status: reference
confidence: 0.9
---

## Core Insight

Paperclip is "the company" to OpenClaw's "employee" — a Node.js + React orchestrator that runs a team of AI agents toward business goals. It provides task management, org charts, budgets, governance, and coordination. If an agent can receive a heartbeat, it's "hired."

## Key Claims

| Feature | Detail |
|---------|--------|
| **Core metaphor** | Task manager + org chart + budget tracker for AI agents |
| **Agent support** | OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP — any agent that takes heartbeats |
| **Atomic execution** | Task checkout and budget enforcement prevent double-work and runaway spend |
| **Persistent state** | Agents resume same context across heartbeats, not restart from scratch |
| **Goal alignment** | Tasks carry full goal ancestry — agents know what AND why |
| **Multi-company** | One deployment, many companies, complete data isolation |
| **Governance** | Board approves hires/strategy, can override/pause/terminate any agent |
| **Cost control** | Monthly budgets per agent; agents stop when over budget |

## Connections

- [[openclaw]] — the "employee" agent in the stack
- [[paperclip-api]] — API reference
- [[paperclip-company-spec]] — package format
- [[paperclip-hermes-adapter]] — Hermes integration
