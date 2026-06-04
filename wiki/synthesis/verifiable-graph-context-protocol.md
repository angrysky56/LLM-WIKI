---
created: 2026-05-21
updated: 2026-05-21
type: synthesis
summary: VGCP — DAG-structured reasoning with constraint-verified node commitment via a Graph Kernel (∂)
tags: [verification, reasoning, graph, constraint-satisfaction, dag, tool-calling, provenance]
sources: [/home/ty/Repositories/ai_workspace/angrysky56vgcp-mcp-server/]
status: active
confidence: 0.9
---



# Verifiable Graph Context Protocol (VGCP)

## Core Thesis

Conversation is not a linear token log — it is a directed acyclic graph (DAG) of typed thoughts connected by explicit causal and support relationships. VGCP enforces this structurally: every node added to the graph must satisfy constraint invariants before commitment. The result is reasoning with provenance — every conclusion carries its full causal chain.

## The Constraint Crystallization Principle

```
⧬∞ ⦿ ⫰ ∂ → ⧈

Infinite potential (⧬∞) crystallizes into finite actuality (⦿)
through constraint boundary (∂), producing structured reality (⧈).
```

This is the semantic meaning of the Graph Kernel (∂): constraint boundaries are not restrictions but *generators* of structure. The DAG emerges because constraints carve a path through infinite possibility.

## Node Types

| Type | Role | Can be root? |
|
|
|
-|
| `PREMISE` | Axiom, fact, retrieved data | Yes |
| `WARRANT` | Intermediate reasoning step | No |
| `CLAIM` | Conclusion or assertion | No |
| `TOOL_CALL` | Request to execute external function | No |
| `TOOL_RESULT` | Output from a tool call | No (requires TOOL_CALL parent) |
| `CONSTRAINT` | System rule | Yes |
| `REBUTTAL` | Counter-argument | No |

## The Four Constraints

### 1. Orphan Prevention
Non-root nodes must have at least one parent. A `CLAIM` without a `WARRANT` or `PREMISE` is rejected. This enforces that no conclusion floats without derivation.

### 2. Tool Causality
`TOOL_RESULT` nodes require a `TOOL_CALL` parent. This prevents hallucinated tool outputs — the agent cannot assert a result it never actually called. A tool result without a tool call parent is architecturally impossible.

### 3. Acyclicity
The graph must remain a DAG. No cycles. This is enforced topologically — if adding an edge would create a cycle, it is rejected. Circular reasoning is not just discouraged; it is impossible.

### 4. Type Consistency
Claims must derive from reasoning. A `CLAIM` whose ancestors contain no `WARRANT` or `PREMISE` is type-inconsistent. This goes beyond syntax into semantics — the shape of the derivation must match the type of the conclusion.

## What Verification Entails

VGCP's theory of verification is grounded in constraint satisfaction, not output matching. Verification is not "does this look right" — it is "was this derived correctly through a valid causal chain." The four constraints are the preconditions for validity, not the outputs.

This means:
- **Hallucination is structurally prevented**, not statistically reduced. A tool result without a tool call parent cannot enter the graph — there is no pathway for fabricated evidence.
- **Provenance is automatic.** Every `CLAIM` has an explicit chain: `PREMISE → ... → WARRANT → CLAIM`. You can trace any conclusion back to its roots.
- **Context rot is prevented.** The graph is not a sequence window — it is a causal structure. Loading context means retrieving causal ancestors, not "last N tokens."

## Key Caveats

**The graph is only as good as its node typing.** If a `PREMISE` contains false information, the downstream `CLAIM` will be validly derived but false. VGCP does not solve truth at the input — it only ensures that reasoning from inputs follows the constraint rules.

**TOOL_RESULT requires honest tooling.** The constraint assumes tool calls produce如实 results. If a tool lies (returns fabricated data), the `TOOL_RESULT` enters the graph with a valid parent but an invalid content. VGCP constrains structure, not content fidelity.

**Boundary of the graph.** External knowledge (user input, web retrieval) enters as `PREMISE` nodes. Whether those premises are accurate depends on the retrieval mechanism, not the graph. VGCP provides the reasoning layer; it does not guarantee the inputs.

## Relationship to Related Concepts

- **[[causal-reasoning]]** — VGCP is a formalization of causal reasoning: every edge is a causal or support relation, not an association.
- **[[chain-of-thought]]** — CoT is linear; VGCP is graph-structured. CoT allows circular paths; VGCP prohibits them structurally.
- **[[concepts/load-bearing-reasoning]]** — Load-bearing reasoning identifies which inference steps are essential; VGCP makes that explicit via the causal chain in every `CLAIM`.
- **[[agentic-research]]** — Tool calling in agents is where VGCP's `TOOL_RESULT` constraint matters most — hallucinated tool outputs are the primary failure mode in deep research.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌────────────┐
│   LLM       │ --> │ Graph Kernel │ --> │   Ledger   │
│ (Generator) │     │     (∂)      │     │   (DAG)    │
└─────────────┘     └──────────────┘     └────────────┘
     ↑                    │
     │                    ▼
     │              ┌──────────┐
     └────────────  │ Inspectors│
                    └──────────┘
                    - Orphan Prevention
                    - Tool Causality
                    - Acyclicity
                    - Type Consistency
```

The Graph Kernel (∂) is the constraint enforcement layer. Inspectors validate each proposed node against all four constraints before committing to the Ledger (the DAG itself).

## Implementation

**Repo:** `angrysky56vgcp-mcp-server` at `/home/ty/Repositories/ai_workspace/angrysky56vgcp-mcp-server/`

The MCP server exposes six tools for managing the reasoning graph:
- `propose_thought` — add a node (with constraint validation)
- `get_context` — retrieve causal ancestors of a node
- `get_reasoning_chain` — trace full provenance from root to a claim
- `query_graph` — search nodes by content
- `get_graph_state` — retrieve full graph structure
- `clear_graph` — reset (used for fresh sessions)

## Open Questions

- **Node type granularity** — Are there edge cases where a node genuinely satisfies all four constraints but is still epistemically unsound? VGCP doesn't yet have a fifth constraint for semantic coherence.
- **Subgraph partitioning** — Large graphs may need subgraphs with independent constraint scopes. Currently the architecture is monolithic.
- **Temporal reasoning** — VGCP encodes causal structure, not temporal order. Two nodes can be causally related without temporal ordering (e.g., parallel derivation chains). This is handled by the DAG structure but not explicitly formalized.

## Connections
- [[wiki/index]]
- [[synthesis/verifiable-graph-context-protocol]]
- [[verifiable-graph-context-protocol]]

→ [[causal-reasoning]], [[chain-of-thought]], [[concepts/load-bearing-reasoning]], [[agentic-research]], [[project-synapse]], [[markovian-dev-agency]]
