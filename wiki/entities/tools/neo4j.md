---
summary: Graph database providing vector search, fulltext indexing, and relationship traversal
tags: [database, graph, vector-search, infrastructure]
updated: 2026-04-07T20:36:04Z
created: 2026-04-07T20:36:04Z
---

# Neo4j

Graph database used as the knowledge backbone of [[Project Synapse]].

## Role in This System

- Stores entities, facts, and relationships as a connected graph
- Native **VECTOR** type (2026.x) for embedding storage and ANN semantic search
- Fulltext indexes for BM25 keyword search
- Graph traversal for discovering non-obvious connections between concepts

## Key Cypher Patterns Used

- `db.index.vector.queryNodes()` — ANN vector search over entity/fact embeddings
- `db.index.fulltext.queryNodes()` — BM25 keyword search
- Variable-length path matching — `(a)-[*1..N]-(b)` for connection exploration
- `MERGE` with `ON CREATE / ON MATCH` — idempotent upserts with timestamps

## Version

Running Neo4j 2026.x with Cypher 25 syntax. Local embeddings via sentence-transformers or Ollama — no paid API keys required.

## Connections

- [[project-synapse]] — the MCP server using this as its graph backend
- [[obsidian]] — the human-readable layer sitting above this graph layer
- [[zettelkasten-engine]] — runs pattern detection directly over this graph
- [[graphrag]] — the retrieval paradigm implemented using this database
- [[hilbert-hotel-graph-architecture]] — thought experiment: immutable nodes + lazy offset protocols for infinite graph operations
