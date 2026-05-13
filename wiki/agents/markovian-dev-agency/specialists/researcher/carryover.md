## CarryoverState

### Established
- [Issue-001] 115 garbage entities, 203 generic untyped `Entity` nodes — Synapse problem
- [Context] Synapse MCP uses Neo4j for graph storage + ChromaDB for embeddings
- [Context] qwen3-embedding:4b model produces 2560-dim vectors; EMBEDDING_DIMENSION=2560 required in MCP config

### Open
- [Issue-001] Could research: Neo4j schema enforcement patterns, ingest sanitization best practices, garbage cleanup strategies
- [Potential] Researcher could investigate what other Synapse users have done for similar issues

### Heading
- [Intent] Available for pattern research if diagnostician needs background info
- [Ready for] Research ingest sanitization, Neo4j constraint patterns, migration strategies for large graphs

## Last Session Notes

Researcher not yet activated. Only diagnostic investigation happened. Available for background research if needed during Issue-001 investigation.