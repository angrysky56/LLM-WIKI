---
updated: 2026-05-17T17:56:49Z
created: 2026-05-17T17:56:49Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Hermes delegation patterns — when to use delegate_task (parallel research, code review, multi-file work) vs execute_code, cronjob, or direct tools. Critical: subagents get zero parent context, must be fully self-contained.
tags: [hermes-agent, delegation, parallel, subagents, workflow]
sources: https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns
status: reference
confidence: 0.95
---

## Core Insight

delegate_task is for reasoning-heavy parallel subtasks where isolated context and restricted toolsets prevent main-conversation flooding. It is synchronous within the parent turn — if the parent is interrupted, active children are cancelled. For durable work that must outlive the turn, use cronjob or terminal(background=True) instead.

## Key Claims

| Use delegate_task | Don't use delegate_task |
|-----------------|----------------------|
| Parallel research (3 concurrent) | Single tool call → use tool directly |
| Code review with fresh context | Mechanical multi-step → execute_code |
| Multi-file refactoring | Tasks needing user clarify → cronjob/background |
| Research synthesis | Long-running durable tasks → terminal(background=True) |

**Critical:** Subagents have ZERO context from parent. Pass everything in goal+context fields.

## Connections
- [[index]]
- [[sources/documentation/delegation-parallel-work]]
- [[delegation-parallel-work]]

- [[hermes-agent]] — parent system
- [[create-custom-subagents]] — related subagent pattern (but Claude Code specific)
- [[profiles]] — multiple independent Hermes agents
