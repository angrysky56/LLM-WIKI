---
summary: Neo4j 2026.04.0: vector-3.0 quantization fix, io_uring async I/O, GenAI plugin token functions, Cypher 25 GQL alignment
tags: [neo4j, release-notes, vector-index, genai-plugin, cypher, gql, io_uring]
updated: 2026-05-07T16:46:17Z
created: 2026-05-07T16:46:17Z
---

# Neo4j 2026.04.0 Release Notes

**Source:** [neo4j.com/release-notes](https://neo4j.com/release-notes/database/neo4j-2026-04-0/) (2026-04-23)
**Type:** Release notes — database server

## Highlights Relevant to LLM-WIKI/Synapse

### Vector Index Fix
- **vector-3.0 bug fix**: Quantized data was correctly *written* during index population but wasn't *used* at query time. This meant vector indexes behaved as unquantized, using more memory than necessary. Fixed — no index rebuild needed. **This directly affects Synapse's `fact_embedding`, `entity_embedding`, `zettel_embedding` indexes.**

### Performance
- **io_uring async I/O**: Early support for Linux async I/O on page evictor and checkpointer (`server.memory.pagecache.async` setting). Higher I/O throughput.
- **ID generator optimization**: Faster reuse of deleted IDs, less store file growth, reduced lock contention.

### GenAI Plugin 2026.04.0
- New: `GENAI_AZURE_OPENAI_BASE_URL` config for custom Azure endpoints
- New: `ai.text.chunkByTokenLimit()` — split text into chunks within token limits
- New: `ai.text.countToken()` — estimate token count of input strings

### Cypher 25 (GQL alignment)
- `IS LABELED` / `IS NOT LABELED` predicates (GQL equivalents of `IS`/`IS NOT`)
- `FOR` statement (GQL equivalent of `UNWIND`)
- `SHORTEST` memory usage reduced

### Neo4j-admin
- `database copy` and `import` now support `--compress` with `--target-format=backup`
- Composite keys in import can now use INTEGER types (previously forced STRING)

### GDS 2026.04.0
Compatible release of Graph Data Science library.

## Action Items
- Vector-3.0 fix is automatically applied; no migration needed
- Consider enabling `server.memory.pagecache.async` for io_uring if on Linux 5.1+
- GenAI plugin token functions may simplify chunking for embedding pipelines
