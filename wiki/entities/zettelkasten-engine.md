---
summary: Autonomous pattern detection and insight synthesis engine within Project Synapse
tags: [component, AI, pattern-detection, insight-generation]
updated: 2026-04-07T20:36:21Z
created: 2026-04-07T20:36:21Z
---

# Zettelkasten Engine

The autonomous insight generation component of [[Project Synapse]].

## What It Does

- Runs pattern detection algorithms over the [[Neo4j]] knowledge graph
- Uses community detection, centrality analysis, and semantic clustering
- Generates confidence-scored hypotheses about connections between concepts
- Creates auditable reasoning trails linking insights to supporting evidence

## Method

Based on Niklas Luhmann's Zettelkasten method:
- **Atomic notes**: each insight is self-contained with a unique ID
- **Explicit linking**: insights connect to evidence via `SUPPORTED_BY` relationships
- **Emergent structure**: patterns surface bottom-up from the graph topology
- **Continuous expansion**: new ingests trigger re-evaluation of existing patterns

## Integration

Insights are stored as `Zettel` nodes in Neo4j with vector embeddings, enabling semantic search over generated hypotheses — not just raw facts.
