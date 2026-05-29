---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: Run multiple independent Hermes agents on the same machine — each with its own config, API keys, memory, sessions, skills, and gateway state
tags: [hermes-agent, profiles, multi-agent, configuration]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
status: active
confidence: 0.95
---

# Profiles: Running Multiple Agents

## Core Concept

A profile is a separate Hermes home directory. Each profile gets its own directory containing its own `config.yaml`, `.env`, `SOUL.md`, memories, sessions, skills, cron jobs, and state database.

Profiles let you run separate agents for different purposes — a coding assistant, a personal bot, a research agent — without mixing up Hermes state.

## Quick Start

```bash
hermes profile create coder       # creates profile + "coder" command alias
coder setup                       # configure API keys and model
coder chat                         # start chatting
```

That's it. `coder` is now its own Hermes profile with its own config, memory, and state.

## Profile Structure

Each profile lives in `~/.hermes/profiles/<name>/` and contains:
- `config.yaml` — agent configuration
- `.env` — API keys and secrets
- `SOUL.md` — identity and principles
- `memories/` — persistent memory files
- `sessions/` — conversation history (SQLite)
- `skills/` — available skills
- `cron/` — scheduled jobs

## Profile Commands

- `hermes profile create <name>` — create new profile
- `hermes profile list` — show all profiles
- `hermes profile remove <name>` — delete a profile
- `<name> chat` — start agent with that profile
- `<name> setup` — configure the profile
- `<name> gateway start` — start the gateway for this profile

## Use Cases

- **Separate work/personal contexts** — different models, different system prompts
- **Specialized agents** — coding, research, inbox triage as distinct profiles
- **Fleet management** — one dashboard for all profiles

## Connections
- [[sources/documentation/scheduled-tasks-cron-hermes-agent]]
- [[sources/documentation/kanban-multi-agent-board-hermes-agent]]
- [[sources/documentation/profiles-running-multiple-agents]]
- [[wiki/index]]
- [[profiles-running-multiple-agents]]

- [[hermes-agent]] — parent system
- [[kanban-multi-agent-board-hermes-agent]] — task coordination across profiles
- [[scheduled-tasks-cron-hermes-agent]] — scheduling for profile-bound tasks