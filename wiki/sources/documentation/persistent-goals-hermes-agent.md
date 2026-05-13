---
created: 2026-05-11
type: source
summary: "/goal slash command — standing goal + auto-continuation loop with judge model, inspired by Codex CLI's Ralph loop
tags: [hermes, goals, persistence, ralph-loop, delegate-task, mini-max]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
status: active
confidence: 0.9
---

# Persistent Goals — Hermes Agent

`/goal` sets a **standing objective** that survives across turns. After every turn, a lightweight judge model checks whether the goal is satisfied. If not, Hermes auto-feeds a continuation prompt back into the same session and keeps working — until the goal is achieved, you pause/clear it, or the turn budget runs out.

## Core Mechanics

- **Judge model** evaluates `done` vs `continue` after each turn using strict JSON output: `{"done": bool, "reason": "string"}`
- **Fail-open**: judge errors → treated as `continue` (never blocks progress)
- **Turn budget**: default 20 turns (`goals.max_turns` in config), auto-pauses when hit
- **Preemption**: user messages always take priority over continuation loop

## Commands

| Command | Effect |
|---|---|
| `/goal <text>` | Set/replace goal, kicks off first turn immediately |
| `/goal status` | Show goal, status, turns used |
| `/goal pause` | Stop auto-continuation without clearing |
| `/goal resume` | Resume loop, resets turn counter |
| `/goal clear` | Drop goal entirely |

## Goal vs delegate_task

| | `/goal` | `delegate_task` |
|---|---|---|
| Context | Shared with main session | Fresh isolated conversation |
| Persistence | Survives turns, bounded iterations | Single turn, bounded by parent |
| Use for | Multi-step tasks in same session | Parallel isolated workers |
| Judge | Yes — automatic continuation check | No — returns summary when done |

## Key Insight: Ralph Loop

The judge is deliberately **conservative** — only marks `done` when the response explicitly confirms completion or the final deliverable is clearly produced. Unachievable/blocked goals are treated as DONE with a block reason to avoid burning budget.

This is inspired by Codex CLI's `/goal` (Eric Traut, OpenAI), but the implementation is independent and adapted to Hermes architecture.

## Connections

- [[subagent-delegation]] — parallel isolated workers via delegate_task
- [[markovian-carryover]] — bounded forward-state for session continuity
- [[bounded-structured-memory]] — layered memory architecture this fits within
- [[hermes-agent]] — framework entity page