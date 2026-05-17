---
updated: 2026-05-17T17:56:52Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Hermes subagent delegation via delegate_task — spawns isolated child AIAgent instances with own context, toolsets, and terminal. Up to 3 concurrent by default. CRITICAL: children get zero parent conversation context.
tags: [hermes-agent, delegate_task, subagents, parallel, isolation]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
status: reference
confidence: 0.95
---

## Core Insight

delegate_task spawns isolated child AIAgent instances with restricted toolsets, independent terminal sessions, and fresh conversations. Only the final summary returns to parent. The critical constraint: subagents start with ZERO knowledge of parent conversation — the parent must pass ALL context in goal+context fields.

## Key Claims

| Feature | Detail |
|---------|--------|
| **Single task** | delegate_task(goal, context, toolsets) |
| **Parallel batch** | delegate_task(tasks=[...]) — up to 3 concurrent by default |
| **Context isolation** | No parent history, tool calls, or prior discussion |
| **Toolsets** | Restrict which tools child can use |
| **Orchestrator role** | Can use delegate_task to spawn own workers (max_spawn_depth config) |
| **Synchronous** | Parent turn interruption cancels active children |

Bad: `delegate_task(goal="Fix the error")` — child doesn't know what error.
Good: `delegate_task(goal="Fix TypeError in api/handlers.py", context="Line 47: 'NoneType' has no attribute 'get'. parse_body() returns None when Content-Type is missing.")` — fully self-contained.

## Connections

- [[hermes-agent]] — parent system
- [[delegation]] — broader delegation patterns guide
