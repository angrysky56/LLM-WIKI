---
created: 2026-05-11
updated: 2026-05-23T08:55:00Z
type: entity
summary: Nous Research's open-source AI agent framework — multi-platform, provider-agnostic, skill-powered, with delegation, goals, cron, and memory systems
tags: ['hermes', 'agent-framework', 'nous-research', 'delegation', 'goals', 'cron', 'multi-agent']
sources: []
status: active
confidence: 0.95
---

# Hermes Agent

**Type:** Tool/Framework  
**Source:** https://github.com/NousResearch/hermes-agent  
**Docs:** https://hermes-agent.nousresearch.com/docs/

An open-source AI agent framework by Nous Research. Runs in terminal, messaging platforms (Discord, Telegram, Slack, etc.), and IDEs. Provider-agnostic — works with OpenRouter, Anthropic, OpenAI, DeepSeek, MiniMax, and 15+ other providers.

## Core Features

### Delegation (`delegate_task`)
Spawns isolated child agents for parallel workstreams. Children get fresh conversation + restricted toolsets + own terminal session. Default flat (no nested delegation), up to 3 concurrent. Not durable — interrupt cancels children.

→ See [[subagent-delegation]]

### Persistent Goals (`/goal`)
Standing objective that survives across turns. After each turn, a judge model evaluates `done` vs `continue`. Auto-continues up to 20 turns (configurable). Conservative judge — only marks done when explicitly confirmed.

→ See [[persistent-goals-hermes-agent]]

### Cron Jobs
Durable scheduled tasks via `cronjob` tool. Schedules: duration (`"30m"`), cron expression (`"0 9 * * *"`), or ISO timestamp. Per-job model override, skills, delivery target. Immune to parent-turn interrupts.

→ See: `hermes cron` CLI

### Memory
Persistent cross-session memory. SOUL.md at slot #1 defines identity. User profile and agent state persist across sessions.

### Skills
Self-improving — persist reusable procedures as skill documents that load into future sessions. Skill lifecycle managed by Curator (auto-archives stale, pins important, tracks use counts).

## Architecture

| Layer | Component |
|---|---|
| Core | AIAgent conversation loop, context compression, model routing |
| Tools | Tool registry + toolsets (web, terminal, file, delegation, etc.) |
| Gateway | Multi-platform adapters (Discord, Telegram, Slack, etc.) |
| Scheduler | Cron job runner |
| Memory | SOUL.md, user profile, session store |

## Multi-Agent Integration

Hermes supports multi-agent coordination via:
- **`delegate_task`** for parallel workers within a session
- **`cronjob`** for durable background workers that survive session boundaries
- **Markovian carryover** (via skill) for bounded forward-state so workers can resume after context reset

The bounded-servitors framework ([[bounded-structured-memory]]) extends Hermes with:
- Per-agent vault workspaces under `LLM-WIKI/wiki/agents/`
- Markovian carryover template for session continuity
- Manager synthesizes carryovers into `now.md`

## Connections
- [[concepts/swe-bench]]
- [[concepts/persistent-goals-hermes-agent]]
- [[concepts/llm-agent-architecture]]
- [[entities/tools/isabelle-hol]]
- [[sources/documentation/hermes-path-forward]]
- [[entities/tools/hermes-agent]]
- [[entities/tools/isabelle]]
- [[sources/documentation/scheduled-tasks-cron-hermes-agent]]
- [[concepts/agentic-hierarchy]]
- [[sources/documentation/event-hooks-hermes-agent]]
- [[sources/repositories/gbrain]]
- [[sources/repositories/graphify-ai-coding-assistant-skill]]
- [[concepts/kanban]]
- [[sources/documentation/codegraph-hermes-phase1-implementation]]
- [[concepts/mcp-model-context-protocol]]
- [[sources/documentation/subagent-delegation-hermes-agent]]
- [[sources/articles/hermes-openclaw-paperclip-stack]]
- [[concepts/markovian-carryover]]
- [[sources/documentation/kanban-multi-agent-board-hermes-agent]]
- [[sources/repositories/openclaw]]
- [[concepts/multi-agent-llm-systems]]
- [[sources/documentation/create-custom-subagents]]
- [[concepts/subagent-delegation]]
- [[sources/documentation/profiles-running-multiple-agents]]
- [[concepts/multi-agent-coordination]]
- [[sources/articles/choosing-right-agentic-design-pattern]]
- [[concepts/bounded-structured-memory]]
- [[entities/projects/markovian-dev-agency]]
- [[wiki/index]]
- [[concepts/hermes-agent-skills]]
- [[sources/documentation/paperclip-hermes-adapter]]
- [[sources/documentation/hermes-mcp-integration]]
- [[concepts/delegation]]
- [[sources/documentation/acp-editor-integration-hermes-agent]]
- [[concepts/profiles]]
- [[concepts/agents]]
- [[sources/documentation/automate-anything-with-cron]]
- [[concepts/meta_harness_loop]]
- [[sources/documentation/persistent-goals-hermes-agent]]
- [[log]]
- [[sources/repositories/codegraph]]
- [[sources/articles/gemma4]]
- [[entities/projects/meta-harness]]
- [[concepts/autonomous-ai-agents]]
- [[concepts/code-agent]]
- [[sources/repositories/get-shit-done]]
- [[sources/repositories/symbiotic-ai]]
- [[sources/documentation/delegation-parallel-work]]
- [[soul]]

- [[persistent-goals-hermes-agent]] — /goal feature summary
- [[subagent-delegation]] — delegate_task mechanics
- [[bounded-structured-memory]] — layered memory architecture
- [[markovian-carryover]] — forward-state skill for agent continuity
- [[hermes-agent]] — skill documentation
- [[markovian-dev-agency]] — runs on Hermes as execution framework

- [[domain-onboarding-standards]]
- [[isabelle]]
- [[swe-bench]]
- [[multi-agent-coordination]]
- [[hermes_agent]]
- [[meta-harness]]
- [[agents]]
- [[domain-onboarding-standards]]
- [[autonomous-ai-agents]]
- [[isabelle-hol]]
- [[mcp-model-context-protocol]]
- [[code-agent]]
- [[multi-agent-llm-systems]]
- [[hermes-agent-skills]]
- [[profiles]]
- [[llm-agent-architecture]]
- [[kanban]]
- [[delegation]]
- [[meta_harness_loop]]
- [[agentic-hierarchy]]