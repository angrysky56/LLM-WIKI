---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Single-agent execution pattern — one agent, one task, no delegation
tags: [agent-skill, skill, agentic]
sources: 
status: active
confidence: 1.0
---

# Single-Agent Pattern

> [!TIP]
> **Use when**: A task is atomic, sequential, or small enough that one agent can complete it without breaking down work.

## When to Use

Single-agent is the right default when:
- The task has a clear, linear solution path
- No sub-specialization is needed (no "research this while writing that")
- Tool access is straightforward (no need to route between different capability domains)
- The task fits in one agent activation

## When NOT to Use

Reaching for multi-agent when single-agent is sufficient adds:
- Coordination overhead (carryover, deconfliction, merging)
- Context fragmentation across agent memories
- Scheduler complexity

## Patterns

### Linear Single-Agent
```
Agent → Tool → Tool → Tool → Done
```
Task completes in one pass. Example: fetch a paper, write a summary, done.

### Iterative Single-Agent (ReAct)
```
Agent → Reason → Act → Observe → Reason → Act → ...
```
Use when the solution path is not known upfront. The agent iteratively tries approaches until a stopping condition is met. See [[agentic-react]].

## Connections
- [[agents/skills/supervisor-delegation]]
- [[agents/skills/single-agent]]
- [[agents/skills/agentic-decision-tree]]
- [[index]]
- [[agents/skills/agentic-multiagent]]
- [[agents/skills/supervisor-orchestrator]]
- [[single-agent]]

- [[agentic-react]] — iterative variant
- [[agentic-decision-tree]] — routing to single vs multi
- [[supervisor-delegation]] — when to escalate from single to multi
- [[supervisor-orchestrator]] — orchestrating multiple agents