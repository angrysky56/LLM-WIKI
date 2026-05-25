---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: Durable SQLite-backed task board for coordinating multiple Hermes profiles — dispatchers spawn workers with kanban_* tools, CLI for humans/automation
tags: [hermes-agent, kanban, multi-agent, orchestration, cron, tasks]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
status: active
confidence: 0.95
---

# Kanban (Multi-Agent Board) | Hermes Agent

## Core Concept

Hermes Kanban is a durable task board shared across all Hermes profiles. It enables multiple named agents to collaborate without fragile in-process subagent swarms. Every task is a row in `~/.hermes/kanban.db`; every handoff is readable and writable by anyone; every worker is a full OS process with its own identity.

## Two Surfaces

The board has two front doors backed by the same `~/.hermes/kanban.db`:

| Surface | Who | Interface |
|---------|-----|-----------|
| **Agents** | AI models driving work | `kanban_*` toolset: `kanban_show`, `kanban_list`, `kanban_complete`, `kanban_block`, `kanban_heartbeat`, `kanban_comment`, `kanban_create`, `kanban_link`, `kanban_unblock` |
| **Humans/CLI** | You, scripts, cron | `hermes kanban …` CLI, `/kanban …` slash command, dashboard |

Both surfaces route through the same `kanban_db` layer — reads see a consistent view, writes can't drift.

## Workloads Kanban Covers

- **Research triage** — parallel researchers + analyst + writer, human-in-the-loop
- **Scheduled ops** — recurring daily briefs building a journal over weeks
- **Digital twins** — persistent named assistants (`inbox-triage`, `ops-review`) accumulating memory over time
- **Engineering pipelines** — decompose → implement in parallel worktrees → review → iterate → PR
- **Fleet work** — one specialist managing N subjects (50 social accounts, 12 monitored services)

## Dispatcher Spawning

The dispatcher spawns each worker with `kanban_*` tools already in its schema. Orchestrator profiles can also enable the `kanban` toolset explicitly. The model reads and routes tasks by calling tools directly — not by shelling out to `hermes kanban`.

## Workers Interacting with the Board

Workers interact through tool calls (not CLI). Key operations:
- `kanban_list` — see available tasks
- `kanban_show` — get full task details
- `kanban_heartbeat` — signal alive (prevents circuit breaker timeout)
- `kanban_complete` — mark done and record result
- `kanban_block` / `kanban_unblock` — manage blockers
- `kanban_comment` — add notes/debug info
- `kanban_create` — add new tasks
- `kanban_link` / `kanban_unlink` — connect related tasks

## Circuit Breaker Pattern

Workers that fail to heartbeat within the configured timeout are assumed dead. The circuit breaker unblocks their tasks and makes them available for retry by other workers.

## Connections

- [[hermes-agent]] — parent system
- [[scheduled-tasks-cron-hermes-agent]] — related cron feature
- [[profiles-running-multiple-agents]] — related multi-profile feature