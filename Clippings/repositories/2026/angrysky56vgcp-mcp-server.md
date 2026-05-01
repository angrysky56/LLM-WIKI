---
title: "angrysky56/vgcp-mcp-server"
source: "https://github.com/angrysky56/vgcp-mcp-server"
author:
published:
created: 2026-05-01
description: "Contribute to angrysky56/vgcp-mcp-server development by creating an account on GitHub."
tags:
  - "clippings"
---
## VGCP MCP Server

**Verifiable Graph Context Protocol** - A Model Context Protocol server that provides DAG-structured reasoning with constraint verification.

## The Constraint Crystallization Principle

```
⧬∞ ⦿ ⫰ ∂ → ⧈

Infinite potential (⧬∞) crystallizes into finite actuality (⦿)
through constraint boundary (∂), producing structured reality (⧈).
```

## What This Does

Instead of treating conversation as a linear log of tokens, VGCP structures reasoning as a **Directed Acyclic Graph (DAG)** where:

- **Nodes** are typed thoughts (premises, warrants, claims, tool calls, etc.)
- **Edges** are explicit causal/support relationships
- **Constraints** are enforced by inspectors before any node is committed

This **architecturally prevents** certain classes of AI errors:

| Problem | VGCP Solution |
| --- | --- |
| Context rot | Load only causal ancestors, not "last N tokens" |
| Hallucinated tool results | Tool causality enforcement |
| Circular reasoning | DAG constraint - topologically impossible |
| "Lost in the middle" | Relevance-weighted traversal |
| No provenance | Every conclusion has explicit causal chain |
| Can't learn from mistakes | Reflexion built-in - failures preserved |

## Installation

```
cd vgcp-mcp-server
npm install
npm run build
```

## Usage with Claude Desktop

Add to your `claude_desktop_config.json with command: node with your path ie /home/<your-username>/.nvm/versions/node/<your-version>/bin/node`:

```
{
  "mcpServers": {
    "vgcp": {
      "command": "node",
      "args": ["/path/to/vgcp-mcp-server/build/index.js"]
    }
  }
}
```

## Tools

### propose\_thought

Add a verified node to the reasoning graph. The Graph Kernel validates constraints before committing.

**Node Types:**

- `PREMISE` - Axiom, fact, or retrieved data (can be root)
- `WARRANT` - Intermediate reasoning step
- `CLAIM` - Conclusion or assertion
- `TOOL_CALL` - Request to execute external function
- `TOOL_RESULT` - Output from tool (requires TOOL\_CALL parent!)
- `CONSTRAINT` - System rule
- `REBUTTAL` - Counter-argument

**Constraints Enforced:**

- **Orphan Prevention**: Non-root nodes must have parents
- **Tool Causality**: TOOL\_RESULT requires TOOL\_CALL parent
- **Acyclicity**: Graph must remain a DAG
- **Type Consistency**: Claims must derive from reasoning

### get\_context

Retrieve the causal ancestors of a node - the "causal light cone" for reasoning.

### get\_reasoning\_chain

Get full provenance path from root to a claim. Shows exactly which premises and reasoning led to a conclusion.

### query\_graph

Search for nodes by content.

### get\_graph\_state

Get complete graph structure (all nodes, edges, metadata).

### clear\_graph

Reset the reasoning graph.

## Example Session

```
1. propose_thought(type: "PREMISE", content: "User wants to find restaurants")
   → n1 created (root)

2. propose_thought(type: "TOOL_CALL", content: "search_restaurants('nearby')", parentIds: ["n1"])
   → n2 created

3. propose_thought(type: "TOOL_RESULT", content: "Found: Pasta Palace, Taco Town", parentIds: ["n2"])
   → n3 created (valid - has TOOL_CALL parent)

4. propose_thought(type: "TOOL_RESULT", content: "Made up data", parentIds: ["n1"])
   → REJECTED: "Hallucination: Tool Result without Tool Call parent"

5. get_reasoning_chain(claimId: "n3")
   → Shows: PREMISE → TOOL_CALL → TOOL_RESULT
```

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

## Future: UI Integration

The groundwork is laid for optional real-time UI visualization where users can observe and interact with the reasoning graph as it builds. See the parent project's `UAVICrystallizer.jsx` for the React component.

## Related

This server implements concepts from the **Unified Architecture for Verifiable Intelligence (UAVI)** synthesis, combining:

- Topological Consciousness Theory (TCT)
- Formalized Generative Architecture (FGA)
- Diagrammatic Reasoning Systems (DRS)
- Verifiable Graph Context Protocol (VGCP)

See: `/home/ty/Repositories/ai_workspace/unified-architecture-synthesis/`

## License

MIT