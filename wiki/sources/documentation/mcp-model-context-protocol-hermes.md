---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "Official MCP documentation — connect Hermes to external tool servers (stdio/HTTP), per-server tool filtering, resource/prompt support, quickstart guide"
tags: [mcp, model-context-protocol, hermes-agent, tools, integration, stdio, http]
sources: [https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp]
status: active
confidence: 0.9
---

# MCP (Model Context Protocol) — Hermes Agent

MCP lets Hermes Agent connect to external tool servers — GitHub, databases, filesystems, browser stacks, internal APIs.

## Two Server Types

### Stdio Servers
Local subprocesses over stdin/stdout. Use for local tools:
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
```

### HTTP Servers
Remote MCP servers via HTTP. Use for cloud services.

## Key Capabilities

- **Tool discovery** — automatic registration at startup
- **Per-server filtering** — expose only needed tools
- **Utility wrappers** — MCP resources and prompts when supported

## Install
```bash
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]"
```

## Connections
- [[hermes-agent]] — parent tool
- [[hermes-mcp-integration]] — Hermes-specific MCP setup
- [[mcp-model-context-protocol]] — concept reference
