---
summary: Controlled vocabulary for wiki tags — preferred terms with USE/UF equivalence, BT/NT hierarchy, and RT associative relationships
tags: [meta, controlled-vocabulary, indexing, tag-taxonomy, reference]
updated: 2026-04-11T04:48:34Z
created: 2026-04-11T04:48:34Z
---

# Tag Taxonomy — Controlled Vocabulary

**Type:** Reference — open indexing consistency control  
**Status:** active — update as new concepts enter the wiki  
**Note:** This is the wiki's controlled vocabulary. Before tagging any page, check here for the preferred term. If a concept isn't listed, add it with its relationships.

---

## Notation

- **USE** → redirect to preferred term (equivalence — non-preferred)
- **UF** → Used For (equivalence — preferred term lists its aliases)
- **BT** → Broader Term (hierarchical — more general)
- **NT** → Narrower Term (hierarchical — more specific)
- **RT** → Related Term (associative — always add reciprocally)

---

## Preferred Terms

### information-retrieval
- UF: `IR`, `search`, `retrieval`
- NT: `vector-search`, `keyword-search`, `graphrag`, `hybrid-search`
- RT: `knowledge-management`, `indexing`

### vector-search
- BT: `information-retrieval`
- UF: `semantic-search`, `ANN-search`, `embedding-search`
- NT: `vector-index`
- RT: `embeddings`, `cosine-similarity`

### keyword-search
- BT: `information-retrieval`
- UF: `fulltext-search`, `BM25`, `text-search`
- RT: `inverted-index`

### hybrid-search
- BT: `information-retrieval`
- UF: `hybrid-RAG`, `HybridRAG`
- RT: `RRF`, `vector-search`, `keyword-search`

### graphrag
- BT: `information-retrieval`
- UF: `graph-RAG`, `Graph-RAG`, `knowledge-graph-retrieval`
- RT: `neo4j`, `knowledge-graph`, `wikilinks`

### embeddings
- UF: `embedding`, `vector-embedding`, `dense-vectors`
- RT: `vector-search`, `sentence-transformers`, `ollama`

### knowledge-management
- UF: `PKM`, `personal-knowledge-management`, `KM`
- NT: `wiki`, `zettelkasten`, `para`
- RT: `information-retrieval`, `obsidian`

### knowledge-graph
- UF: `KG`, `graph-database`
- RT: `neo4j`, `graphrag`, `entities`, `relationships`

### indexing
- UF: `index`, `index-construction`
- NT: `inverted-index`, `controlled-vocabulary`, `thesaurus`
- RT: `information-retrieval`, `knowledge-management`

### controlled-vocabulary
- BT: `indexing`
- UF: `taxonomy`, `vocabulary-control`
- NT: `thesaurus`, `tag-taxonomy`
- RT: `indexing`, `tags`

### methodology
- UF: `method`, `framework`, `process`
- NT: `design-thinking`, `para`, `zettelkasten`

### agent
- UF: `AI-agent`, `LLM-agent`
- RT: `MCP`, `tool`, `workflow`

### synthesis
- UF: `cross-domain-synthesis`, `insight`
- RT: `zettelkasten`, `generate-insights`

### meta
- UF: `system`, `self-referential`
- RT: `agent`, `workflow`, `schema`

### science-of-science
- UF: `scientometrics`, `bibliometrics`
- RT: `EDM`, `citation-network`, `disruption`

### citation-network
- BT: `science-of-science`
- UF: `citation-graph`, `reference-network`
- RT: `EDM`, `graphrag`

---

## USE References (non-preferred → preferred)

| Tag used | USE instead |
|---|---|
| `embedding` | `embeddings` |
| `vector-embedding` | `embeddings` |
| `semantic-search` | `vector-search` |
| `ANN` | `vector-search` |
| `fulltext-search` | `keyword-search` |
| `graph-RAG` | `graphrag` |
| `PKM` | `knowledge-management` |
| `KG` | `knowledge-graph` |
| `taxonomy` | `controlled-vocabulary` |
| `scientometrics` | `science-of-science` |
| `bibliometrics` | `science-of-science` |
| `method` | `methodology` |

---

## Connections

- [[wiki-indexing-theory]] — theoretical basis for this document
- [[synapse-llm-wiki-operating-guide]] — references this for tag guidance
