---
summary: RAG enhanced with graph traversal for richer context beyond vector similarity
tags: [RAG, graph, vector-search, architecture]
updated: 2026-04-07T20:36:31Z
created: 2026-04-07T20:36:31Z
---

# GraphRAG

An extension of [[RAG]] that combines vector similarity search with graph traversal.

## How It Differs from Standard RAG

Standard RAG retrieves isolated document chunks by vector similarity. GraphRAG adds a second step: after finding the nearest vectors, it **traverses the graph** around those nodes to pull in related context that vector search alone would miss.

## Key Insight

From Neo4j's research: the most valuable context often comes not from the direct vector-match nodes, but from the **shortest paths between** top-match nodes — the graph structure connecting them reveals relationships that embedding similarity cannot capture.

## Pattern

1. Embed the query
2. ANN vector search → top-k nodes
3. Graph traversal from those nodes (neighbors, shortest paths, community)
4. Combine all context into LLM prompt
5. Generate answer

## Implementation in [[project-synapse]]

- `query_semantic` handles step 2 (vector ANN)
- `explore_connections` handles step 3 (graph traversal)
- `query_hybrid` combines vector + fulltext BM25 for step 2

## Connections

- [[rag]] — the baseline this extends
- [[project-synapse]] — implements this pattern with Neo4j
- [[neo4j]] — the graph database powering traversal
- [[edm-framework]] — citation networks as a domain where GraphRAG is directly applicable
- [[persistent-knowledge-compilation]] — complementary: GraphRAG retrieves; compilation pre-synthesises
