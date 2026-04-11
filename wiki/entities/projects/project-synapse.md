---
summary: Graph-backed MCP server providing semantic search, knowledge synthesis, and wiki bridge
tags: [project, MCP, Neo4j, architecture, core]
updated: 2026-04-07T20:01:48Z
created: 2026-04-07T20:01:48Z
---

# Project Synapse

Autonomous Knowledge Synthesis and Inference Engine — the graph-backed backbone of this wiki.

## What It Is

An MCP server that combines:
- **[[Neo4j]]** graph database with native vector indexes for semantic search
- **Montague Grammar** parser for formal semantic analysis
- **[[Zettelkasten Engine]]** for autonomous pattern detection and insight generation
- **Wiki adapter** bridging the Obsidian vault with the knowledge graph

## Role in This Wiki

Project Synapse solves the scaling limitations of the [[LLM Wiki Pattern|wiki/sources/llm-wiki-pattern]]:

| Karpathy Pattern | Project Synapse |
|---|---|
| index.md for page lookup | Vector ANN search over Neo4j |
| No cross-document graph | Full entity-relationship graph |
| Conflict resolution by LLM judgment | Timestamped nodes + confidence scores |
| Git for rollback | Git + graph versioning |

## Architecture

```
Raw Source → Semantic Pipeline → Neo4j (entities, facts, embeddings)
                                    ↕
                              Wiki Adapter
                                    ↕
                          Obsidian Vault (Markdown)
```

## Key Tools

- `wiki_ingest_raw` — reads raw files, runs semantic pipeline, stores in graph
- `wiki_write_page` / `wiki_read_page` — CRUD on wiki Markdown pages
- `query_knowledge` — vector semantic search over the graph
- `explore_connections` — graph traversal for hidden relationships
- `wiki_lint` — health check for orphans, broken links, missing frontmatter

## Connections

- [[neo4j]] — the graph/vector storage layer
- [[obsidian]] — the human-readable wiki output layer
- [[zettelkasten-engine]] — the autonomous insight synthesis component
- [[rag]] — the stateless baseline this system supersedes
- [[graphrag]] — the graph-retrieval paradigm this implements
- [[persistent-knowledge-compilation]] — the core architectural philosophy
- [[llm-wiki-pattern]] — the Karpathy pattern this extends
