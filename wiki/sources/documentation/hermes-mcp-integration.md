---
summary: Hermes Agent MCP integration: consuming external tools, acting as an MCP server for messaging, per-server filtering, sampling, dynamic discovery
tags: [hermes-agent, mcp, model-context-protocol, tool-integration, configuration]
updated: 2026-05-07T16:47:13Z
created: 2026-05-07T16:47:13Z
---

# Hermes MCP (Model Context Protocol) Integration

**Source:** [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
**Type:** Documentation — Hermes Agent feature

## Summary

Hermes Agent can both **connect to** external MCP servers (consuming their tools) and **act as** an MCP server itself (exposing messaging capabilities to other agents). The integration supports stdio and HTTP transports, per-server tool filtering, dynamic tool discovery, and sampling (MCP servers requesting LLM inference from Hermes).

## Key Features

### Connecting to MCP Servers
- **Stdio**: Local subprocess over stdin/stdout (`command`, `args`, `env`)
- **HTTP**: Remote endpoint (`url`, `headers`)
- **Tool naming**: `mcp_<server_name>_<tool_name>` to prevent collisions
- **Utility wrappers**: `list_resources`, `read_resource`, `list_prompts`, `get_prompt` when supported
- **Per-server filtering**: `include` (whitelist), `exclude` (blacklist), `enabled: false` (disable)
- **Dynamic discovery**: Server can push `notifications/tools/list_changed` for automatic re-registration

### Hermes as MCP Server (`hermes mcp serve`)
Exposes 10 messaging tools to external MCP clients (Claude Code, Cursor, Codex):

| Tool | Purpose |
|---|---|
| `conversations_list` | List active conversations across platforms |
| `conversation_get` | Get detailed info on one conversation |
| `messages_read` | Read recent message history |
| `attachments_fetch` | Extract media from messages |
| `events_poll` | Poll for new events (non-blocking) |
| `events_wait` | Long-poll until next event (near-real-time) |
| `messages_send` | Send messages to any platform |
| `channels_list` | Browse available targets |
| `permissions_list_open` | Pending approval requests |
| `permissions_respond` | Allow/deny approvals |

### MCP Sampling
MCP servers can request LLM inference from Hermes via `sampling/createMessage`. Configurable per-server: model override, token caps, rate limiting (RPM), tool-loop depth limits.

## Configuration Example

```yaml
mcp_servers:
  project-synapse:
    command: uv
    args:
      - --directory
      - /path/to/project-synapse-mcp
      - run
      - python
      - -m
      - synapse_mcp.server
    env:
      NEO4J_URI: bolt://localhost:7687
      EMBEDDING_PROVIDER: ollama
      OLLAMA_EMBED_MODEL: qwen3-embedding:4b
      EMBEDDING_DIMENSION: "2560"
```

## Relevance to LLM-WIKI
Project Synapse, ast-asg, mcp-logic, advanced-reasoning, verifier-graph, and local-repl are all MCP servers configured under Hermes. The embedding dimension mismatch fix was directly informed by understanding how env vars flow through MCP config.
