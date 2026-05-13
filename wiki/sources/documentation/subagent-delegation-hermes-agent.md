---
created: 2026-05-11
type: source
summary: "delegate_task tool — isolated subagent spawning, batch parallelism, depth limits, model override, and durability tradeoffs
tags: [hermes, delegation, delegate-task, subagent, parallelism, mini-max]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
status: active
confidence: 0.95
---

# Subagent Delegation — Hermes Agent

`delegate_task` spawns child AIAgent instances with isolated context, restricted toolsets, and their own terminal sessions. Each child works independently — only its final summary enters the parent's context.

## Single vs Batch

**Single task:**
```python
delegate_task(
    goal="Debug why tests fail",
    context="Error: assertion in test_foo.py line 42",
    toolsets=["terminal", "file"]
)
```

**Parallel batch** (up to 3 concurrent by default):
```python
delegate_task(tasks=[
    {"goal": "Research topic A", "toolsets": ["web"]},
    {"goal": "Research topic B", "toolsets": ["web"]},
    {"goal": "Fix the build", "toolsets": ["terminal", "file"]}
])
```

Default concurrency: 3, configurable via `delegation.max_concurrent_children` or `DELEGATION_MAX_CONCURRENT_CHILDREN` env var.

## Critical: Fresh Context

> Subagents start with a **completely fresh conversation**. Zero knowledge of parent's history, prior tool calls, or pre-delegation discussion. Parent must pass **everything** the subagent needs via `goal` + `context`.

```python
# BAD — subagent has no idea what "the error" is
delegate_task(goal="Fix the error")

# GOOD — full context passed
delegate_task(
    goal="Fix the TypeError in api/handlers.py",
    context="""File api/handlers.py has a TypeError on line 47:
    'NoneType' object has no attribute 'get'.
    The function process_request() receives a dict from parse_body(),
    but parse_body() returns None when Content-Type is missing.
    Project at /home/user/myproject, Python 3.11."""
)
```

## Depth & Orchestration

| Role | Behavior | Default |
|---|---|---|
| `leaf` (default) | Cannot delegate further | Default |
| `orchestrator` | Retains delegation toolset, can spawn workers | Gated by `max_spawn_depth` (default 1 = flat) |

`max_spawn_depth` default is 1 (flat). Raise to 2+ to enable nested orchestration. With `max_spawn_depth: 3` and `max_concurrent_children: 3`, tree can reach 27 concurrent leaves — cost multiplies per level.

## Model Override

```yaml
delegation:
  model: "google/gemini-flash-2.0"
  provider: "openrouter"
```

If omitted, subagents use the parent's model. With MiniMax subscription (1500 calls/5hrs), use MiniMax as delegate model too.

## Durability Warning

> `delegate_task` is **synchronous within the parent turn** — not durable. If parent is interrupted (new message, /stop, /new), all active children are cancelled and in-progress work is discarded.

For **durable long-running work** that must survive interrupts, use `cronjob` (action=create) instead.

## Toolset Restrictions

Subagents cannot use:
- `delegation` (leaf) — blocked; retained for orchestrators
- `clarify` — cannot ask user
- `memory` — no writes to shared persistent memory
- `code_execution` — should reason step-by-step
- `send_message` — no cross-platform side effects

## Timeout

Default child timeout: **600 seconds** (10 min). Timer resets on every API call or tool call. Configure via `delegation.child_timeout_seconds`.

Diagnostic dump on zero-call timeout: structured log written to `~/.hermes/logs/subagent-timeout-<session>-<timestamp>.log`.

## vs execute_code

| Factor | `delegate_task` | `execute_code` |
|---|---|---|
| Reasoning | Full LLM loop | Just Python execution |
| Context | Fresh isolated conversation | No conversation |
| Tool access | All non-blocked tools | 7 tools via RPC |
| Parallelism | 3 concurrent by default | Single script |
| Best for | Tasks needing judgment | Mechanical pipelines |

Rule of thumb: use `delegate_task` when the subtask requires reasoning/judgment; use `execute_code` for mechanical data processing.

## Connections

- [[persistent-goals-hermes-agent]] — /goal for standing objectives vs delegation for parallel workers
- [[bounded-structured-memory]] — layered architecture context
- [[markovian-carryover]] — carryover context injection pattern for subagents
- [[hermes-agent]] — framework entity page