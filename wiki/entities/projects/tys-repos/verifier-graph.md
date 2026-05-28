---
created: 2026-05-01T07:06:23Z
updated: 2026-05-01T07:06:23Z
type: entity
summary: DAG-structured reasoning provenance MCP server (Verifier Graph).
tags: [verification, graph, evaluator]
sources: []
status: active
confidence: 1.0
---

# Verifier-Graph (VGCP-MCP-Server)

**Verifier-Graph** is an MCP server developed by [[tyler-hall|Ty]] that maintains a Directed Acyclic Graph (DAG) of reasoning provenance. It ensures that every claim made by an AI system can be traced back to its premises via a "causal light cone."

## Core Concepts
- **Reasoning DAG**: Represents the logical flow of thoughts and assertions.
- **Causal Light Cone**: The set of ancestor nodes that provide the necessary context for a given claim.
- **Structural Validation**: Ensures that reasoning follows valid topological and logical constraints.

## Tools
- `propose_thought`: Add a verified node to the reasoning DAG.
- `get_reasoning_chain`: Trace the provenance path from premises to a conclusion.
- `get_context`: Retrieve the causal ancestors for a specific node.

## Connections
- [[sources/papers/proxy-based-shapley-banzhaf-2026]]
- [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]]
- [[entities/projects/tys-repos/verifier-graph]]
- [[sources/papers/cua-gym]]
- [[log]]
- [[sources/papers/vector-policy-optimization-vpo-2026]]
- [[sources/papers/tokenisation-convex-relaxations-2026]]
- [[synthesis/seg-scientist-agent-design]]
- [[sources/papers/behavioral-credibility-trilemma]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-22-top-papers]]
- [[sources/papers/awarevln-self-aware-vision-language-navigation-2026]]
- [[sources/papers/safectrl-rl]]
- [[sources/papers/boiling-frog-agentic-safety-2026]]
- [[sources/papers/shannon-scaling-law-2026]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-23-top-papers]]
- [[index]]
- [[sources/papers/codeskill]]
- [[sources/papers/forecasting-scientific-progress-ai-2026]]
- [[sources/papers/legalsearch-r1]]
- [[sources/papers/alphaproof-nexus-formal-proof-search-2026]]
- [[entities/projects/tys-repos]]
- [[verifier-graph]]
- [[recuriosity-episodic-context-3d-exploration-2026]]
- [[efhf]] — Provides reasoning provenance for the entire stack.
- [[agem]] — Used to track the "evolution" of agent thoughts.
- [[tys-repos]] — Part of Ty's repository collection.
- [[entities/people/tyler-hall]] — Creator of Verifier-Graph.

- [[recuriosity-episodic-context-3d-exploration-2026]]