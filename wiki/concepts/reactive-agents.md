---
created: 2026-07-28
updated: 2026-07-28
type: concept
summary: Reactive agents — agent architectures that use direct stimulus-response mapping without explicit planning
tags: [agent-architectures, reactive, stimulus-response, behavior]
sources: []
status: stub
confidence: 0.3
---

# Reactive Agents

Reactive agents select actions through direct mapping from current perception to response, without explicit planning or world-model simulation.

## Key Characteristics

- **Direct perception-action mapping**: Current state directly selects the next action
- **No explicit goal representation**: Does not maintain a symbolic model of the goal
- **No simulation**: Acts immediately based on environmental input
- **Fast response**: No deliberation overhead — responds in one forward pass

## Relationship to Other Agent Types

See [[agent-architectures]] for the full taxonomy comparison with deliberative, hybrid, and meta-cognitive agents.

## See Also
- [[concepts/hybrid-agents]]
- [[wiki/index]]
- [[concepts/agents]]
- [[log]]
- [[concepts/reactive-agents]]
- [[reactive-agents]]

- [[agentic-react]]: the ReAct implementation of reactive planning
- [[agents]]: parent concept for agent taxonomy
- [[hybrid-agents]]