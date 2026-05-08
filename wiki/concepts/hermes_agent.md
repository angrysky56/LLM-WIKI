---
summary: Architectural overview of the Hermes Agent framework.
tags: [hermes, architecture, agentic-ai]
updated: 2026-05-07T23:21:28Z
created: 2026-05-07T23:21:28Z
---

# Hermes Agent Architecture

The Hermes Agent is a modular, multi-platform autonomous agent framework designed by Nous Research. It is built to be "profile-aware" and "platform-agnostic," meaning the same core logic can drive a CLI, a Discord bot, or a VS Code extension.

## Core Subsystems

### 1. Agent Loop (`run_agent.py`)
The `AIAgent` class is the central orchestrator. It handles:
- **Provider Selection**: Mapping model names to API modes (OpenAI, Anthropic, Codex).
- **Prompt Construction**: Building system prompts from `SOUL.md`, `MEMORY.md`, and active skills.
- **Tool Dispatch**: Executing tools and returning results to the LLM.
- **Context Management**: Summarizing history when context window limits are reached.

### 2. Tool System (`tools/registry.py`)
Hermes uses a decentralized tool registry. Any Python file in `tools/` can register itself at import time. 
- **Backends**: Supports local, Docker, SSH, and Modal environments.
- **MCP Support**: Dynamically loads tools from Model Context Protocol (MCP) servers.

### 3. Session Persistence
Uses SQLite with FTS5 for full-text search. Sessions are isolated by "profiles," allowing multiple instances of the agent to run independently on the same machine.

## Integration for Meta-Harness
The Meta-Harness interfaces with Hermes via the `AIAgent` library directly. 
- **Wrapper**: `src/meta_harness/wrapper.py` wraps `AIAgent` to capture structured evolution results.
- **Discovery**: The harness uses `discover_mcp_tools()` to ensure it has access to formal verification (e.g., `mcp-logic`).

## Design Principles
- **Prompt Stability**: The system prompt remains fixed during a conversation to avoid cache misses.
- **Observable Execution**: All tool calls are logged and visible to the user/harness.
- **Interruptible**: Long-running tasks can be cancelled gracefully.

## Related
- [[Meta-Harness Evolution Loop]]
- [[Domain Onboarding Standards]]
