---
created: 2026-05-25
updated: 2026-05-25
type: source
summary: MCP server bridging local AI agents to Google Colab browser sessions via uvx
tags: [mcp, google-colab, tooling, python, ai-infrastructure]
sources: https://github.com/googlecolab/colab-mcp
status: reference
confidence: 0.95
---

# googlecolab/colab-mcp

An MCP server that bridges local AI agents (Claude Code, Gemini CLI, Windsurf) to a live Google Colab session in the browser. Enables running Python code in Colab's environment with GPU/TPU access from any MCP-compatible local agent.

## Core Functionality

- Executes code in a Colab notebook from the local agent
- Requires client support for `notifications/tools/list_changed`
- Client must be running locally on the user's device

## Setup

```json
{
  "mcpServers": {
    "colab-mcp": {
      "command": "uvx",
      "args": ["git+https://github.com/googlecolab/colab-mcp"],
      "timeout": 30000
    }
  }
}
```

Requires `uv` package manager (`pip install uv`). Googlers may need `--index https://pypi.org/simple`.

## Compatibility

Requires MCP clients that support:
- `notifications/tools/list_changed` protocol
- Local device execution

Verified compatible clients: **Gemini CLI**, **Claude Code**, **Windsurf**

## Notes

- Not accepting external contributions (no bandwidth for PR review)
- Uses GitHub Discussions for feature requests and issue discussion
- Do not open issues directly — discussions are the entry point for all requests

## Connections
- [[index]]
- [[sources/repositories/googlecolab-colab-mcp]]
- [[googlecolab-colab-mcp]]

- Related: [[mcp]] (MCP protocol generally)
- Related: [[google-colab]] (the target runtime)