---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: Schedule automated tasks with natural language, manage with one cron tool, attach skills, deliver to origin/platform/local
tags: [hermes-agent, cron, scheduling, automation, tasks]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
status: active
confidence: 0.95
---

# Scheduled Tasks (Cron) | Hermes Agent

## Core Concept

Schedule tasks to run automatically with natural language or cron expressions. Hermes exposes cron management through a single `cronjob` tool with action-style operations instead of separate schedule/list/remove tools.

## Capabilities

Cron jobs can:
- Schedule one-shot or recurring tasks
- Pause, resume, edit, trigger, and remove jobs
- Attach zero, one, or multiple skills to a job
- Deliver results back to the origin chat, local files, or configured platform targets
- Run in fresh agent sessions with the normal static tool list
- Run in **no-agent mode** — a script on a schedule, its stdout delivered verbatim, zero LLM involvement

## Cron Tool Actions

Single `cronjob` tool with action-style operations:
- `create` — schedule a new job
- `pause` / `resume` — control execution
- `edit` — modify schedule or parameters
- `trigger` — fire immediately
- `remove` — delete a job
- `list` — view scheduled jobs

## No-Agent Mode

Scripts can run on a schedule with zero LLM involvement. The script's stdout is delivered verbatim to the configured destination. Useful for:
- Data collection scripts
- System monitoring
- Automated reports

## Safety

Cron-run sessions cannot recursively create more cron jobs. Hermes disables cron management tools inside cron executions to prevent runaway scheduling loops.

## Connections
- [[wiki/index]]
- [[sources/documentation/scheduled-tasks-cron-hermes-agent]]
- [[sources/documentation/kanban-multi-agent-board-hermes-agent]]
- [[sources/documentation/profiles-running-multiple-agents]]
- [[scheduled-tasks-cron-hermes-agent]]

- [[hermes-agent]] — parent system
- [[kanban-multi-agent-board-hermes-agent]] — task coordination for scheduled jobs
- [[profiles-running-multiple-agents]] — profile-bound scheduled tasks