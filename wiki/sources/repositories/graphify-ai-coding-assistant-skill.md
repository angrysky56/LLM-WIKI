---
updated: 2026-05-17T17:56:15Z
created: 2026-05-17T17:56:15Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Graphify is an AI coding assistant skill for Hermes that maps codebases to knowledge graphs via AST analysis, enabling semantic queries about code structure and relationships.
tags: [graphify, ai-coding-assistant, knowledge-graph, ast, code-analysis, hermes-skill]
sources: (unknown — file from raw/)
status: reference
confidence: 0.8
---

## Core Insight

Graphify transforms codebases into queryable knowledge graphs using AST analysis — functions, classes, imports, and relationships become nodes and edges in Neo4j, enabling natural-language queries like "what functions call this module?" or "show me the call graph for feature X."

## Key Claims

| Capability | Description |
|-----------|-------------|
| **AST parsing** | Extracts functions, classes, imports as structured nodes |
| **Graph storage** | Neo4j-backed with Cypher query support |
| **Semantic queries** | Natural language questions over code structure |
| **Integration** | MCP server for Hermes Agent |

## Connections
- [[sources/repositories/graphify-ai-coding-assistant-skill]]
- [[sources/papers/code-as-agent-harness]]
- [[wiki/index]]
- [[graphify-ai-coding-assistant-skill]]

- [[neo4j]] — graph backend for code knowledge
- [[entities/tools/hermes-agent]] — Graphify runs as a skill within Hermes
- [[codebase-inspection]] — related code analysis capability
