---
summary: Project page for verifier-graph.
tags: [projects, ty-repo, provenance]
updated: 2026-05-01T07:06:30Z
created: 2026-05-01T07:06:30Z
---

---
created: 2026-05-01T07:06:23Z
updated: 2026-05-01T07:06:23Z
type: entity
summary: DAG-structured reasoning provenance MCP server (Verifier Graph).
tags: [projects, ty-repo, angrysky56, provenance, graph-theory, reasoning, mcp]
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
- [[efhf]] — Provides reasoning provenance for the entire stack.
- [[agem]] — Used to track the "evolution" of agent thoughts.
- [[tys-repos]] — Part of Ty's repository collection.
