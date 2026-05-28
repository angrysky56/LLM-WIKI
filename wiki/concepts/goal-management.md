---
summary: Goal management — maintaining, prioritizing, and persisting agent goals across reasoning steps and sessions
tags: [goal-management, agents, planning, bounded-rationality, persistence, metacognition]
updated: 2026-05-28T18:31:34Z
---

---
created: 2026-08-23
updated: 2026-08-23
type: concept
summary: Goal management — maintaining, prioritizing, and persisting agent goals across reasoning steps and sessions
tags: [goal-management, agents, planning, bounded-rationality, persistence, metacognition]
sources: []
status: active
confidence: 0.7
---

# Goal Management

Goal management is the agent design pattern concerned with maintaining, prioritizing, and persisting goals across reasoning steps, tool calls, and sessions. It addresses a fundamental problem: an agent's reasoning process is stateless between calls, but the tasks it pursues are not.

## The Core Problem

LLM inference is stateless by design — each call starts fresh except for what appears in the context window. Real-world tasks require the agent to:

1. **Hold goals across turns** — remember what it's trying to accomplish when the conversation resumes hours later
2. **Prioritize among competing goals** — handle subtasks, side tasks, and interruptions without losing the primary objective
3. **Detect goal completion or failure** — recognize when a goal has been achieved or is no longer viable
4. **Persist goal state across sessions** — resume work after the agent is restarted or context is reset

## Relationship to Planning

Goal management is the persistence layer that planning operates on top of. Planning generates a sequence of steps toward a goal; goal management tracks which goals are active, how they're progressing, and when to escalate or abandon them.

The distinction:
- **Planning** = "What actions should I take to achieve X?"
- **Goal management** = "Which goals am I pursuing, in what priority, and what is their current status?"

## Key Components

### Goal State Machine

Goals typically cycle through states:

```
PENDING → ACTIVE → BLOCKED → COMPLETED/ABANDONED
                ↘ PAUSED ↗
```

| State | Meaning |
|-------|---------|
| PENDING | Goal exists but not yet being worked on |
| ACTIVE | Goal is currently being pursued |
| BLOCKED | Goal cannot proceed — waiting on dependency or resource |
| PAUSED | Goal deliberately suspended (user interrupted, higher priority) |
| COMPLETED | Goal achieved |
| ABANDONED | Goal given up (invalid, impossible, superseded) |

### Priority and Preemption

Agents operating under [[bounded-rationality]] cannot hold all goals in active pursuit simultaneously. Goal management requires:

- **Priority ranking** — which goal matters most right now
- **Preemption** — when a high-priority goal can interrupt a lower one
- **Non-preemptive holds** — pausing a goal without losing its state

### Horizon and Timeout

Goals should have:
- **Temporal horizon** — how far ahead the goal extends (subtask vs. project vs. mission)
- **Timeout conditions** — when to give up if progress stalls
- **Deadline awareness** — sensitivity to externally-imposed time constraints

This connects to [[epistemic-energy]]: when energy is depleted, lower-priority goals should be shed before higher ones.

## Hermes Agent Implementation

The [[hermes-agent]] system implements goal management through [[markovian-carryover]]. At session boundary, the agent writes a carryover state that includes:

- Active goals and their current status
- Priority ordering
- What blocked or paused each goal
- Next actions for each active goal

This allows the agent to resume with full context after a reset, without requiring the full conversation history.

The [[persistent-goals-hermes-agent]] stub page covers the specific implementation details — this page covers the general concept.

## Connections to Other Concepts

- [[planning]] — goal management persists what planning generates
- [[bounded-rationality]] — the resource constraints that force goal prioritization
- [[hermes-meta-cognition]] — goal management is a metacognitive function
- [[epistemic-energy]] — energy depletion determines which goals to shed
- [[multi-agent-llm-systems]] — in multi-agent systems, goal management must coordinate across agents with different goal states
- [[bounded-structured-memory]] — the memory architecture that supports persistent goal state

## Open Questions

- How should goal hierarchies be represented — tree, DAG, or flat priority list?
- When should subgoals be promoted to top-level goals vs. remaining subordinate?
- How does goal management interact with goal drift — the tendency for successful completion to expand scope?
