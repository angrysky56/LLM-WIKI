
---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "Official Hermes Agent documentation — install, configure, skills system, MCP, profiles, cron, delegation, kanban"
tags: [hermes-agent, documentation, install, skills, mcp, profiles, cron, delegation]
sources: [https://hermes-agent.nousresearch.com/docs]
status: active
confidence: 0.9
---

# Hermes Agent Documentation

The self-improving AI agent built by Nous Research. Core features:

## Install (Linux/macOS/WSL2)
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## Core Concepts

### Skills System
Hermes creates skills from experience, improves them during use. Skills live in `~/.hermes/skills/` and are written in YAML + markdown.

### MCP (Model Context Protocol)
Connect external tool servers (GitHub, filesystems, browsers) via MCP. Configure in `~/.hermes/config.yaml`.

### Profiles
Run multiple named agents with isolated configurations. Each profile has its own skills/, plugins/, cron/, memories/.

### Cron / Scheduled Tasks
Schedule agent tasks with cron syntax. Jobs defined in `~/.hermes/cron/jobs.json`.

### Delegation
Delegate tasks to subagents via `delegate_task`. Subagents run as independent OS processes.

### Kanban
SQLite-backed task board for multi-agent coordination. Shared across all profiles via `~/.hermes/kanban.db`.

## Connections
- [[hermes-agent]] — entity page
- [[hermes-mcp-integration]] — MCP setup
- [[hermes-agent-faq-troubleshooting]] — FAQ
- [[mcp-model-context-protocol]] — protocol reference
- [[scheduled-tasks-cron-hermes-agent]] — cron guide
- [[create-custom-subagents]] — subagent creation
