---
summary: Project page for Project Synapse MCP.
tags: [projects, ty-repo, knowledge-management]
updated: 2026-05-01T07:19:08Z
created: 2026-05-01T07:19:08Z
---

---
created: 2026-05-01T07:19:02Z
updated: 2026-05-01T07:19:02Z
type: entity
summary: Autonomous Knowledge Synthesis Engine with LLM-WIKI integration.
tags: [projects, ty-repo, angrysky56, knowledge-graph, neo4j, obsidian, zettelkasten, synapse]
status: active
confidence: 1.0
---

# Project-Synapse-MCP

**Project-Synapse-MCP** is an autonomous knowledge synthesis engine developed by [[tyler-hall|Ty]]. It is the core system used to maintain the **LLM-WIKI**. It combines a Neo4j graph database with an Obsidian Markdown vault to create a persistent, compounding knowledge base.

## Core Pillars
- **Neo4j Knowledge Graph**: Stores entities, facts, and vector embeddings. Supports hybrid search (BM25 + Vector) and graph traversal.
- **LLM-WIKI Integration**: Bridges the graph with a human-readable Obsidian vault. Implements automatic indexing, activity logging, and vault health checks (linting).
- **Semantic Pipeline**: Uses Montague Grammar for formal semantic analysis and NLP for entity extraction.
- **Autonomous Synthesis**: Features a Zettelkasten engine that identifies patterns and generates insights from the knowledge graph.

## Key Tools
- `wiki_fetch_url`: Automated web research (fetch -> clean -> ingest -> archive).
- `query_knowledge`: Semantic search with reasoning trails.
- `generate_insights`: Pattern detection across the entire graph.
- `wiki_lint`: Vault integrity monitoring.

## Theoretical Foundation
- **Montague Grammar**: Compositional semantics.
- **Zettelkasten**: Atomic linked notes.
- **Karpathy LLM-WIKI**: Persistent knowledge compilation.
- **Memex**: Associative knowledge trails.

## Connections
- [[efhf]] — Synapse is the "World Model" and "Persistence" layer of the broader architecture.
- [[tys-repos]] — The primary tool for managing Ty's project ecosystem.
- [[tyler-hall]] — Creator and architect.
