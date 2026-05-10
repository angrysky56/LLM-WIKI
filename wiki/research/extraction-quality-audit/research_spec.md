# Extraction Quality Audit — Research Spec

**Project Slug:** `extraction-quality-audit`  
**Status:** Active  
**Created:** 2026-05-09  
**Researcher:** Wiki Researcher Agent  
**Parent Brief:** [[research-brief-2026-05-09]]

---

## Problem Framing

### Goal
Audit, quantify, and remediate the extraction quality failure in the Synapse Neo4j knowledge graph. The graph contains 10,843 entities and 7,765 facts, but preliminary analysis (Research Brief 2026-05-09) found that 60-70% of entities are extraction artifacts (HTML fragments, formatting debris, single characters) and ~99% of RELATES edges are garbage.

### Scope
- **In scope**: Entity name quality audit, entity type correctness, RELATES edge quality, garbage pattern catalog, purge scripts
- **Out of scope**: Synapse pipeline code changes, embedding re-generation, wiki page content fixes

### Fixed Components
- Neo4j database: `synapse` at `bolt://localhost:7687`
- Entity labels: Entity, Fact
- Relationship types: MENTIONS, RELATES

## Research Design

### Phase 1: Garbage Catalog
Catalog all garbage entity patterns:

1. **HTML/XML artifacts**: Entity names containing `<`, `>`, `id=`, `class=`, `span`, `div`, `<td>`, `</tr>`
2. **URL artifacts**: Entity names starting with `http://` or `https://`
3. **Formatting artifacts**: Entity names matching "Fig", "Figure", "Table", "Section", "Appendix", "Download", "Refer", "Note", "See", "Ref", "References", "et al", "et al.", "Ibid"
4. **Single-character/minimal entities**: Entity names ≤ 2 characters that aren't known abbreviations
5. **Math/LaTeX fragments**: Entity names containing `\\`, `\math`, `\times`, `\sum`, `\int`
6. **Numeric-only strings**: Pure numbers typed as Person/Organization/etc.
7. **File paths**: Entity names containing `/` that aren't URLs

**Query design:**
```cypher
// HTML artifacts
MATCH (e:Entity) WHERE e.name CONTAINS '<' OR e.name CONTAINS '>' RETURN count(e)

// URL artifacts
MATCH (e:Entity) WHERE e.name STARTS WITH 'http' RETURN count(e)

// Formatting words
MATCH (e:Entity) WHERE e.name IN ['Fig','Figure','Table','Section','Appendix','Download','Refer','Note','See','Ref','References','et al','et al.','Ibid'] RETURN count(e)
```

### Phase 2: Type Correctness Audit
Identify entities with clearly wrong type assignments:
- "Download" typed as Person → should be CreativeWork or Organization
- HTML IDs typed as Person → should be deleted
- URLs typed as Person/Location → should be deleted or recategorized
- "Claude Code" typed as Law → should be Product
- "F" typed as Product → mathematical notation, should be Concept or deleted

### Phase 3: RELATES Edge Audit
- Count edges with semantic vs. non-semantic predicates
- Catalog all non-semantic predicate patterns
- Identify self-referencing RELATES edges
- Sample meaningful RELATES edges for quality assessment

### Phase 4: Purge and Rebuild
- Delete identified garbage entities (preserve Facts, they link to real entities too)
- Delete all non-semantic RELATES edges
- Run entity re-count to measure cleanup effectiveness
- Generate post-cleanup statistics

### Phase 5: Wiki Re-Ingestion
- Identify all pages in `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`
- Ingest un-ingested pages into the graph
- Cross-reference wiki entities with graph entities

## Success Criteria

| Criterion | Current | Target | Measurement |
|-----------|---------|--------|-------------|
| Garbage entity % | ~60-70% | <10% | Entity name pattern scan |
| Meaningful RELATES % | ~1% | >80% | Predicate semantic check |
| Entity type correctness | ~50% | >90% | Manual sample audit |
| Wiki-sourced facts | 0 | >500 | Count facts WHERE source STARTS WITH 'wiki/' |
| Real entities with ≥5 facts | ~15 | >50 | Count after garbage purge |
| Cross-domain bridges | 0 | >20 | Bridge query after cleanup |

## Budget

| Phase | Cycles | Description |
|-------|--------|-------------|
| Phase 1: Garbage Catalog | 1 | Run detection queries, measure scope |
| Phase 2: Type Correctness | 1 | Identify misclassified entities |
| Phase 3: RELATES Edge Audit | 1 | Quality assessment of edges |
| Phase 4: Purge | 1 | Execute deletions, verify |
| Phase 5: Wiki Re-Ingestion | 2 | Ingest wiki pages, cross-reference |
| **Total** | **6 cycles** | Graduate to synthesis after cleanup verified |

## Verification

After each phase:
1. Run pre/post entity count comparison
2. Sample 20 random entities to verify quality improvement
3. Re-run authority detection to verify real entities now top the list

## Dependencies

- Neo4j write access for purge operations
- Synapse wiki_ingest_raw for wiki re-ingestion
- Librarian agent for wiki page identification

## Risks

- **Fact integrity**: Deleting garbage entities may affect Fact counts if those Facts only link to garbage entities — those Facts should also be reviewed
- **Embedding index**: Entity deletions leave orphaned embeddings — vector indexes may need rebuild
- **Cascade effects**: Other agents (Librarian, Meta-Analyst) may have cached references to garbage entities
