---
summary: Retrieval-Augmented Generation — the standard stateless document Q&A pattern
tags: [RAG, LLM, architecture, vector-search]
updated: 2026-04-07T20:01:19Z
created: 2026-04-07T20:01:19Z
---

# RAG (Retrieval-Augmented Generation)

## Definition

A pattern where an LLM retrieves relevant document chunks from a vector store at query time, then generates an answer using those chunks as context.

## How It Works

1. User asks a query
2. Query is embedded into a vector
3. Vector DB returns top-k similar document chunks
4. Chunks are injected into the LLM's context window
5. LLM synthesizes an answer

## Strengths

- Simple to implement
- Works with any document collection
- No pre-processing needed beyond chunking + embedding

## Weaknesses (RAG Amnesia)

- **Stateless**: rediscovers knowledge from scratch every query
- **No accumulation**: ask a question requiring synthesis of 5 documents, and it re-derives the connections every time
- **Chunk boundaries**: splitting documents into chunks loses cross-document relationships
- **No persistent synthesis**: insights generated in one query disappear into chat history

## Alternatives

- [[Persistent Knowledge Compilation|wiki/concepts/persistent-knowledge-compilation]] — compile knowledge ahead of time
- [[GraphRAG]] — combine vector search with graph traversal for richer context
- Hybrid approaches (e.g. [[Project Synapse]]) that use RAG as a routing layer into a pre-compiled knowledge graph
