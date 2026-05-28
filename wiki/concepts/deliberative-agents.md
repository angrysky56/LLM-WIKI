---
created: 2026-07-28
updated: 2026-07-28
type: concept
summary: Deliberative agents — agent architectures that use explicit planning and world-model reasoning to select actions
tags: [agent-architectures, deliberative, planning, reasoning]
sources: []
status: stub
confidence: 0.3
---

# Deliberative Agents

Deliberative agents use explicit symbolic planning and world-model simulation to select actions, as opposed to reactive agents that map stimuli directly to responses.

## Key Characteristics

- **Explicit goal representation**: Maintains a symbolic model of the goal state
- **World-model simulation**: Simulates action outcomes before execution
- **Plan decomposition**: Breaks high-level goals into sub-tasks hierarchically
- **Replanning**: Revises plans when simulation reveals unexpected states

## Relationship to Other Agent Types

See [[agent-architectures]] for the full taxonomy comparison with reactive, hybrid, and meta-cognitive agents.

## See Also
- [[log]]
- [[concepts/hybrid-agents]]
- [[concepts/deliberative-agents]]
- [[index]]
- [[concepts/agents]]
- [[deliberative-agents]]

- [[agentic-planner]]: the planning subsystem within deliberative agents
- [[world-model]]: the simulation substrate for deliberation
- [[agents]]: parent concept for agent taxonomy
- [[hybrid-agents]]