---
created: 2026-06-03
updated: 2026-06-26
type: concept
summary: MCP — an open standard protocol for connecting AI assistants to external tools, data sources, and services via a structured client-server architecture
tags: [mcp, tool-interfaces, protocol, ai-interoperability]
sources: https://modelcontextprotocol.io, https://github.com/modelcontextprotocol
status: active
confidence: 0.85
---


# MCP (Model Context Protocol)

MCP (Model Context Protocol) is an open standard protocol for connecting AI assistants to external tools, data sources, and services. It defines how an AI model can discover available tools, call them with structured arguments, and receive results back — enabling interoperability between AI systems and the broader software ecosystem.

## What It Is

MCP follows a client-server architecture:

- **MCP Servers**: Lightweight programs that expose a set of tools and resources via the MCP specification. Each server exposes a specific capability domain (e.g., filesystem access, database queries, code execution, messaging).
- **MCP Clients**: AI assistants or platforms that connect to one or more MCP servers to access external capabilities.

The protocol specifies:
- **Tool discovery**: Servers advertise available tools with their parameter schemas
- **Tool invocation**: Clients call tools with typed arguments and receive structured results
- **Resource access**: Servers can expose read-only resources (files, database records)
- **Sampling**: Servers can request the AI model to perform inference on their behalf (extended capability)

## Why It Matters

Without a standard protocol, every AI-tool integration requires custom code:

| Problem | Without MCP | With MCP |
|---------|-------------|----------|
| Tool discovery | Hardcoded per-integration | Automatic via server advertisement |
| Authentication | Custom per-tool | Reused across servers |
| Error handling | Inconsistent | Standardized |
| Adding new tools | Code change required | Server-side config change only |

MCP makes AI systems modular: add capabilities by connecting new servers, not by modifying the model's code.

## Hermes Agent MCP Integration

[[Hermes Agent]] supports both connecting to MCP servers and acting as an MCP server itself. This bidirectional support means:

**Connecting to servers**: Hermes can use tools from external MCP servers by configuring them in `config.yaml`:

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
```

**Acting as a server**: `hermes mcp serve` exposes messaging tools to external MCP clients (Claude Code, Cursor, Codex):

| Tool | Purpose |
|------|---------|
| `conversations_list` | List active conversations |
| `messages_send` | Send messages to any platform |
| `channels_list` | Browse available targets |
| `permissions_list_open` | Pending approval requests |
| `permissions_respond` | Allow/deny approvals |

## MCP in the LLM-WIKI Stack

Several MCP servers are operational in the LLM-WIKI ecosystem:

- **mcp-logic** (Prover9/Mace4): First-order logic verification — EFHF Layer 3
- **project-synapse**: Neo4j knowledge graph operations
- **verifier-graph**: Verification graph operations
- **advanced-reasoning**: Extended reasoning traces
- **local-repl**: Local code execution

The [[mcp-logic]] server is particularly central: it implements EFHF Layer 3 verification, proving theorems and finding counterexamples using Prover9 and Mace4.

## Connections
- [[concepts/agentic-reasoning]]
- [[concepts/maximum-occupancy-principle]]
- [[wiki/index]]
- [[concepts/mcp]]
- [[sources/repositories/gbrain]]
- [[log]]
- [[sources/papers/xu-envfactory-2026]]
- [[concepts/mcp-model-context-protocol]]
- [[mcp-model-context-protocol]]

- [[mcp-logic]] — MCP server for first-order logic verification
- [[efhf]] — MCP servers implement the EFHF layers (L3: mcp-logic)
- [[concepts/maximum-occupancy-principle]] — MCP enables agents to discover and use external tools for exploration
- [[hermes-agent]] — implements full MCP client + server capability
- [[autonomous-agents]] — autonomous agents rely on MCP as the standard tool interface protocol

- [[agentic-reasoning]]
## Limitations

- MCP servers are trusted components — no sandboxing by default. A malicious or buggy MCP server can compromise the AI system.
- Server availability and latency affect AI system reliability.
- Tool result interpretation is model-side; MCP specifies the wire format but not the semantics of tool results.
- [[mcp]]