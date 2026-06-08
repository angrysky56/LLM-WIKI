---
updated: 2026-05-17T17:56:11Z
created: 2026-05-17T17:56:11Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Hermes supports three hook systems — Gateway hooks (async event handlers in ~/.hermes/hooks/), Plugin hooks (ctx.register_hook()), and Shell hooks (config.yaml scripts) — all non-blocking.
tags: [hermes-agent, hooks, gateway, plugin, shell, lifecycle]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks
status: reference
confidence: 0.95
---

## Core Insight

Hermes has three independent hook systems that run custom code at lifecycle points without blocking the agent pipeline: Gateway hooks (async event handlers registered via HOOK.yaml + handler.py), Plugin hooks (ctx.register_hook() in plugins), and Shell hooks (scripts in config.yaml). All errors are caught and logged — nothing crashes the agent.

## Key Claims

| Hook System | Registration | Runs In | Use Case |
|------------|-------------|---------|----------|
| **Gateway Hooks** | `~/.hermes/hooks/<name>/HOOK.yaml` + `handler.py` | Gateway only | Logging, alerts, webhooks |
| **Plugin Hooks** | `ctx.register_hook()` in plugin code | CLI + Gateway | Tool interception, metrics, guardrails |
| **Shell Hooks** | `hooks:` block in `~/.hermes/config.yaml` | CLI + Gateway | Drop-in scripts for blocking, auto-format, context injection |

Gateway events include: `gateway:startup`, `agent:start`, `agent:end`, `agent:step`, `command:*`, `tool:*`, `error:*`.

## Connections
- [[sources/documentation/event-hooks-hermes-agent]]
- [[wiki/index]]
- [[event-hooks-hermes-agent]]

- [[entities/tools/hermes-agent]] — parent system
- [[webhook-subscriptions]] — webhook delivery pattern related to gateway hooks
