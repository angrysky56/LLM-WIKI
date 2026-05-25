---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Subagent delegation — pattern of spawning child agents to handle subtasks
tags: [delegation, multi-agent, hermes-agent]
sources: 
status: active
confidence: 0.7
---

# Subagent Delegation

Subagent delegation is the pattern where an agent spawns one or more child agents to handle portions of its task. Key characteristics:

- **Isolation** — child agents have fresh context and restricted toolsets
- **Parallelism** — multiple subagents can work simultaneously
- **Bounded context** — each subagent operates within a limited context window
- **Non-durable** — subagents typically cancelled if parent interrupted

In Hermes Agent, delegation is via `delegate_task` which supports:
- Up to 3 concurrent child agents
- Configurable toolsets per subagent
- Isolated terminal session per subagent

## Connections

- [[delegation]] — the broader concept
- [[agentic-hierarchy]] — hierarchical organization of delegated tasks
- [[bounded-structured-memory]] — how subagent state is preserved
- [[hermes-agent]] — framework implementing subagent delegation
