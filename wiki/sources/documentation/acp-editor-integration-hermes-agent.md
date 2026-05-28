---
updated: 2026-05-17T17:55:36Z
created: 2026-05-17T17:55:36Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Hermes Agent can run as an ACP server, letting VS Code, Zed, and JetBrains editors communicate over stdio with full Hermes tool access.
tags: [hermes-agent, acp, editor-integration, vscode, zed, jetbrains]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/acp
status: reference
confidence: 0.95
---

## Core Insight

ACP (Agent Client Protocol) is the integration layer that makes Hermes behave like an editor-native coding agent. Running `hermes acp` exposes a curated toolset (file tools, terminal, browser, memory, skills, vision) over stdio JSON-RPC to compatible editors — VS Code (via ACP Client extension), Zed, and JetBrains all supported.

## Key Claims

| Claim | Detail |
|-------|--------|
| **Launch commands** | `hermes acp`, `hermes-acp`, or `python -m acp_adapter` |
| **Install** | `pip install -e '.[acp]'` — adds `agent-client-protocol` dependency |
| **Session binding** | Editor cwd bound to Hermes task ID, so file/terminal tools run relative to workspace |
| **Approvals** | Dangerous terminal commands route back to editor as approval prompts (allow once/always/deny) |
| **Registry manifest** | `acp_registry/agent.json` advertises the agent to editors |
| **Config** | Uses same `~/.hermes/.env`, `config.yaml`, skills, and state.db as CLI mode |
| **Excluded features** | Messaging delivery and cronjob management not available in ACP mode |

## Connections
- [[index]]
- [[sources/documentation/acp-editor-integration-hermes-agent]]
- [[acp-editor-integration-hermes-agent]]

- [[hermes-agent]] — parent system
- [[openclaw]] — also supports `ollama launch` integration pattern
- [[gemma4]] — Ollama-compatible model usable in Hermes ACP context
