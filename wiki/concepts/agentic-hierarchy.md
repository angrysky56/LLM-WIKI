---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Agentic hierarchy — organizational structure of multi-level AI agents with different levels of agency
tags: [multi-agent, hierarchy, delegation, architecture]
sources: 
status: stub
confidence: 0.3
---

# Agentic Hierarchy

Agentic hierarchy refers to organizational structures where AI agents operate at different levels of abstraction and authority. Patterns include:

- **Supervisor-worker** — supervisor decomposes tasks, workers execute
- **Manager-specialist** — manager coordinates specialists with domain expertise
- **Orchestrator-delegator** — orchestrator decides what to delegate, delegators manage execution
- **Recursive decomposition** — agents can decompose their own tasks into sub-tasks

Key challenges:
- Maintaining coherence across hierarchical levels
- Proper credit assignment and blame
- Information flow up and down the hierarchy

## Connections

- [[multi-agent-llm-systems]] — systems built with agentic hierarchies
- [[delegation]] — the act of assigning subtasks down the hierarchy
- [[onboarding-standards]] — how new agents are integrated into the hierarchy
- [[hermes-agent]] — framework supporting hierarchical agent patterns
