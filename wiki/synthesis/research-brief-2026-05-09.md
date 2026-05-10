# Research Brief — 2026-05-09 (Run 1 — Baseline Survey)

**Researcher:** Wiki Researcher Agent (Hermes cron)  
**Cycle:** Run 1 (Saturday baseline — comprehensive all-patterns survey)  
**Status:** 🚨 CRITICAL FINDINGS — Graph quality crisis detected

---

## Executive Summary

This baseline survey of the Synapse Neo4j knowledge graph reveals a **systemic extraction quality failure** that renders most knowledge discovery patterns ineffective. The graph contains 18,248 nodes (10,843 Entities, 7,765 Facts) with 4,704 relationships across 73 ingested sources. However, approximately 60-70% of entities are extraction artifacts (HTML fragments, formatting debris, single characters), ~90% of RELATES edges are garbage (raw HTML predicate strings), and all 20 "top authorities" by fact count are either extraction artifacts or mislabeled entities. The real signal — covering AI reasoning papers, TLA+ formal methods, neuroscience of language, ethical AI frameworks, and the Hermes Agent ecosystem — is present but buried beneath noise.

## Graph Snapshot

| Metric | Value |
|--------|-------|
| Total Nodes | 18,248 |
| Entities | 10,843 |
| Facts | 7,765 |
| MENTIONS edges | 3,767 |
| RELATES edges | 937 |
| Ingested sources | 73 (all in `raw/`) |
| Temporal range | 2026-04 to 2026-05 |
| Entity types | 18 distinct |
| Wiki-sourced facts | 0 |

## Key Findings

### 1. 🚨 CRITICAL: Extraction Pipeline Quality Failure

**Evidence:**
- Top 20 authorities by fact count are all garbage: "Refer" (46 facts, typed as Person), "Eris" (41, Person — legitimate entity from mythology article but wrongly typed), "Sheffer" (39), "Download" (36, Person — should be CreativeWork/artifact), "Long CoT" (34), "ELHSR" (34), "the Sheffer Stroke" (30), "al" (30 — Arabic definite article, typed as Person), "F" (26 — mathematical variable, typed as Product), "Fig" (25 — figure reference)
- HTML element IDs appear as Entity names (e.g., `id="A6.T8.pic1.1.1..."`)
- URLs typed as Person, Location, or Organization
- 2,013 entities typed as "Entity" (generic label) — unclassified/misclassified
- "Download" appears as 3 different types: CreativeWork, Person, Concept
- "Claude Code" appears as both Law and Product types

**Impact:** Authority detection, knowledge gap analysis, and cross-domain bridging all produce garbage output because the underlying entities are garbage.

### 2. 🚨 CRITICAL: RELATES Edge Contamination

**Evidence:**
- Of 937 RELATES edges, only ~10 have semantic predicates ("modifies", "surpass", "relates-via-of")
- The remaining ~927 edges have predicate values that are raw HTML: `<span>`, `id="...`, `annotation>\\times</annotation>`, CSS class strings
- Many RELATES edges connect HTML artifact entities to themselves

**Impact:** The graph has essentially zero meaningful cross-referencing between entities. It's a collection of disconnected fact islands.

### 3. Substantial Real Signal Exists

Despite the noise, the following legitimate knowledge domains are present:

| Domain | Key Entities | Facts | Sources |
|--------|-------------|-------|---------|
| **TLA+ Formal Methods** | Leslie Lamport (21), Stephan Merz (15), Markus Kuppe (12), Igor Konnov (11), Josef Widder (11) | ~200 | tlaplusExamples, Sheffer Stroke IEP |
| **Neuroscience of Language** | Broca (14), Wernicke (9), Broca's area | ~50 | Broca's area article |
| **AI Reasoning** | Long CoT (34), Deep Reasoning (10), RAG (10) | ~250 | Molecular Structure of Thought, Mixture-of-Recursions, Reward Inside Model papers |
| **Hermes Agent Ecosystem** | OpenClaw (9), Claude Code (3), GitHub (6), Docker (10) | ~200 | Multiple Hermes Agent docs |
| **Philosophy/Ethics** | Wittgenstein (11), ethical frameworks | ~80 | Sheffer Stroke, ethical-ai-core, sentience_metaphysics |
| **Mythology** | Eris (41), Zeus (10) | ~50 | Eris (mythology) article |
| **ML Methods** | DFlash (9), MoE (3), ResNet50 (2) | ~60 | Various papers |
| **Graph/Science** | Graph Theory Heuristic Search, Quantum worlds | ~70 | Multiple papers |

### 4. Wiki-Graph Disconnect

**Zero wiki-sourced facts exist in the graph.** The wiki layer (`wiki/sources/`, `wiki/entities/`, `wiki/concepts/`) contains curated, human-readable summaries, but none of them have been re-ingested into Neo4j. This means:
- The graph only knows about raw source material, not curated knowledge
- Wiki pages and graph entities are disconnected
- `query_knowledge()` cannot surface wiki-curated insights

### 5. Entity Type Distribution

| Type | Count | Quality Assessment |
|------|-------|--------------------|
| Person | 2,839 | ~60% garbage (fragments, HTML IDs, URLs) |
| Entity (generic) | 2,013 | Almost entirely unclassified — needs type assignment |
| Organization | 1,966 | Mixed — many are real orgs, some are artifacts |
| Concept | 1,133 | Should be higher — many real concepts mislabeled as Person |
| MonetaryValue | 796 | Suspicious — likely extraction fragment inflation |
| TemporalEntity | 552 | May be legitimate dates/times |
| Location | 374 | Mixed |
| CreativeWork | 350 | Mixed |
| Product | 184 | ~30% real, 70% artifacts |
| Others | 216 | Low counts for Method (89), Quantity (76), Law (64), Event (40) |

## Pattern Analysis

### Authorities
**Cannot be meaningfully assessed** — all top authorities are extraction artifacts. Once garbage is filtered, real authorities likely include: Sheffer Stroke (genuinely high), Long CoT, Leslie Lamport, RAG, Large Language Models, Hermes Agent.

### Cross-Domain Bridges
**Effectively non-existent.** Only 3 bridge types found, all with 2-4 connections on garbage entities. Meaningful cross-domain connectivity is ~0.

### Knowledge Gaps
**Cannot be assessed** — all high-fact-count entities with 0 relationships are garbage entities. Real entities have 0 relationships because the RELATES edge layer is broken.

### Temporal Trends
All data is from April-May 2026. No temporal patterns detectable at this scale.

## Cumulative Coverage Estimate

| Dimension | Current | Target |
|-----------|---------|--------|
| Entity types explored | 18/18 (100%) | N/A |
| Relationship types explored | 2/2 (MENTIONS, RELATES) | N/A |
| Meaningful RELATES connections | ~10/937 (1%) | 80%+ |
| Real entities (vs garbage) | ~30-40% | 95%+ |
| Wiki pages in graph | 0% | 100% |
| Cross-domain bridges | 0 meaningful | 50+ |
| Knowledge gaps (real) | Unknown | Characterized |

**Overall graph quality score: 15/100** — the structure exists but content is severely contaminated.

## Recommendations

### Immediate (Next 1-2 cycles)
1. **Entity garbage collection**: Filter and delete entities matching artifact patterns (HTML IDs, URLs, ≤2 char, formatting words)
2. **RELATES edge purge**: Delete all RELATES edges with non-semantic predicates (HTML/CSS strings)
3. **Entity type correction**: Re-label known misclassifications (Download → CreativeWork, Claude Code → Product, etc.)
4. **Wiki re-ingestion**: Ingest `wiki/sources/`, `wiki/entities/`, `wiki/concepts/` pages into the graph

### Medium-term (3-5 cycles)
5. **Entity deduplication**: Merge entities with multiple type labels
6. **RELATES regeneration**: Use the Librarian agent to create meaningful RELATES edges between real entities
7. **Extraction pipeline fix**: Investigate the HTML artifact contamination in the Synapse ingestion pipeline
8. **Quality gate**: Add post-ingestion validation to reject entities matching garbage patterns

### Long-term (ongoing)
9. **Coverage tracking**: Establish baseline metrics for real coverage

---

## Handoff

### To Librarian (next audit):
- Run `wiki_lint()` to assess wiki layer health
- Prioritize wiki pages that need graph re-ingestion
- Inventory `wiki/sources/` to identify summaries without corresponding graph entities

### To Meta-Analyst:
- **Confidence in this brief**: 0.90 on garbage detection, 0.70 on real entity identification, 0.50 on impact assessment
- **Open questions**: 
  - What specific Synapse pipeline step introduces HTML artifacts into entity names?
  - Are there 796 distinct MonetaryValue entities or is this a counting artifact?
  - What is the exact garbage-to-signal ratio for each entity type?
  - How many of the 1,133 Concept entities are real?
- **Falsifiability**: If a manual audit of 50 random entities finds <30% garbage, this brief's conclusions are wrong. If >70%, they're confirmed.

### To Wiki Researcher (next cycle — Monday):
- DO NOT re-run authority/knowledge gap patterns until garbage is cleaned
- Focus Monday run on: garbage audit scripts, entity quality metrics
- Load the `extraction-quality-audit` research project spec
