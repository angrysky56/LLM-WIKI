---
created: 2026-05-09T18:00:00Z
updated: 2026-05-09T18:00:00Z
type: synthesis
summary: Week 1 quality audit — Orphans and Misclassifications in the LLM-WIKI knowledge graph
tags: [librarian-report, quality-audit, orphans, misclassifications, week-1]
confidence: 0.95
---

# Librarian Report — 2026-05-09 (Week 1: Orphans + Misclassifications)

**Cycle**: Week 1 of 4 (Orphans + Misclassifications)
**Graph snapshot**: 10,483 Entity nodes, 7,765 Fact nodes, 3,767 MENTIONS, 937 RELATES
**Database**: synapse (Neo4j 2026.04.0 Enterprise)

---

## Executive Summary

The LLM-WIKI knowledge graph is in a **pre-quality state**. Two systemic failures dominate:

1. **Catastrophic orphan rate**: 68% of all entities (7,133/10,483) have zero connections — no Fact mentions them, no entity relates to them. Ten of eighteen entity types have orphan rates exceeding 95%.

2. **Person misclassification pandemic**: An estimated ~46% of "Person" nodes are not people. They are LaTeX math fragments, HTML/SVG rendering markup, API calls, code variables, and URLs. The extraction pipeline labeled them `Person` and (in many cases) Facts dutifully linked to them, amplifying the contamination.

**Single highest-impact action**: Fix the `Person` type classifier in the extraction pipeline. This simultaneously reduces orphan count (many false-Persons are orphans), improves MENTIONS quality, and shrinks the graph by ~1,100 garbage nodes.

---

## Finding 1: Catastrophic Orphan Rate (68% Overall)

### WHAT
7,133 entities have zero MENTIONS and zero RELATES connections — 68% of the entity catalog.

### WHY this matters
An orphan entity is dead weight. It was extracted from source text but never integrated into the knowledge fabric. It cannot be found via graph traversal, cannot receive insight generation, and represents wasted extraction compute. The graph is not "sparse but growing" — it has absorption states where entire entity types are born orphans and stay that way.

### Distribution by type

| Type | Total | Orphans | Orphan % |
|------|-------|---------|----------|
| MonetaryValue | 796 | 796 | **100%** |
| TemporalEntity | 552 | 552 | **100%** |
| Location | 374 | 374 | **100%** |
| CreativeWork | 350 | 350 | **100%** |
| Organization | 1,966 | 1,960 | **99.7%** |
| Entity (generic) | 2,013 | 1,980 | **98.4%** |
| Method | 89 | 86 | **96.6%** |
| Product | 184 | 87 | **47.3%** |
| Person | 2,839 | 725 | **25.5%** |
| Quantity | 76 | 62 | **81.6%** |
| Law | 64 | 28 | **43.8%** |
| Event | 40 | 27 | **67.5%** |
| Concept | 1,133 | 106 | **9.4%** |

### HOW
```cypher
MATCH (e:Entity) WHERE NOT (e)-[:RELATES]-() AND NOT ()-[:MENTIONS]->(e)
RETURN e.type, count(e) AS orphan_count ORDER BY orphan_count DESC
```
Sample size: full graph (10,483 entities). Confidence: 0.99.

### Category breakdown of orphan types

**DELETE candidates** (extraction noise, zero semantic value):
- Generic `Entity` type orphans: numbers ("five", "thousands", "10-15"), stopgap words, surface-form strings like "3\\.", "10\\. Verification"
- `MonetaryValue` orphans: all 796 are numeric dollar amounts with no context — "$50M", "$1.2B" — extracted but never linked back to what they quantify
- `TemporalEntity` orphans: all 552 are dates/timestamps extracted in isolation

**ENRICH candidates** (valid concepts, just unlinked):
- `Organization` orphans: real entities (Obsidian, GitHub, Slack, MCP, JavaScript, Wikipedia) that should be linked — they were extracted but the Fact pipeline never connected them
- `Person` orphans: 725 people who were extracted but never mentioned in a Fact (subset may be misclassified non-people)
- `Concept` orphans: 106 — the lowest orphan rate, but includes raw URLs, SVG filenames, and markdown fragments

**INVESTIGATE**: The "Entity" generic type (1,980 orphans) is a catch-all that should not exist. The extraction pipeline should never emit a bare `Entity` label — all entities should have a specific type.

---

## Finding 2: Person Misclassification Pandemic (~46% False)

### WHAT
Of 2,839 `Person`-typed entities, only ~1,520 (53.5%) match a `FirstName LastName` pattern. The remaining ~1,319 are overwhelmingly NOT people.

### WHY this matters
The Person type is the **most connected type** in the graph — 90.6% of all MENTIONS relationships point to Person nodes (3,412/3,767). When 46% of Person nodes are misclassified, every downstream operation is contaminated: graph traversals hit garbage, insight generation sees "people" who are really $\sin{x} = \cos(x - \pi/2)$, and the entire semantic fabric is compromised.

### Categories of misclassified "Persons"

| Category | Examples | Est. Count |
|----------|----------|------------|
| **LaTeX math** | `\sin{x}=\cos(x-\pi/2)$`, `\sigma{(x)}=1/(1+e^{-x})$`, `\alpha_{i}+\beta_{i}+\gamma_{i}=1$` | ~400 |
| **HTML/SVG markup** | `<span id="A6.T8.pic1...">`, `translate(0,4866.75)"><g fill="#000000"`, `width="71.88"><span` | ~300 |
| **Code/API fragments** | `= tl.zeros([BLOCK_M`, `Config(BLOCK_M=64`, `= database.top_k(k=10` | ~150 |
| **URLs** | `https://mistral.ai/news/ministraux](...)`, `David East](https://x.com/_davideast` | ~100 |
| **Technology terms** | `npm`, `Vite`, `Git`, `GPU`, `FFN`, `RL`, `Repo`, `KB`, `GB` | ~80 |
| **Abbreviations** | `NAND`, `ToM`, `MoR`, `ELHSR`, `A1` | ~50 |
| **Single names (ambiguous)** | `John`, `Mary`, `Adam`, `Ryan`, `Kim`, `Wu`, `Chan`, `Ray` | ~100 |
| **Other garbage** | `\u2023`, `b.`, `al`, `^23`, `K$`, `1.9ms`, `max` | ~139 |

### HOW
```cypher
MATCH (e:Entity) WHERE e.type = 'Person'
  AND (e.name =~ '^[A-Z]{2,5}$'
    OR e.name =~ '.*[.](svg|png|jpg|pdf|html|json|xml)$'
    OR e.name =~ '^[0-9].*'
    OR e.name CONTAINS 'http'
    OR size(e.name) <= 2)
RETURN e.name
```
Plus manual sampling of 100 Person names. Confidence: 0.85 (estimates are approximate; a full audit would require systematic classification of all 2,839 Person nodes).

### Ripple effect
The Person misclassification doesn't just bloat the graph — it **skews the MENTIONS distribution**. Facts are structured to primarily reference Persons, so when a Fact about GPU optimization mentions `BLOCK_K=64`, the pipeline labels it a Person and creates a MENTIONS edge. This means the Fact-MENTIONS-Person axis is largely content-free for the 1,319 misclassified nodes.

---

## Finding 3: Extreme Person-Centric Topology

### WHAT
90.6% of all MENTIONS relationships point to Person nodes. The remaining entity types are virtually invisible to the Fact layer.

### WHY this matters
This is not a knowledge graph — it's a **person index**. The extraction pipeline (or Fact generation logic) has an implicit bias: entities are Persons unless proven otherwise. Organization, Location, CreativeWork, Product — the types that make a knowledge graph rich — are systematically excluded from the Fact layer.

### MENTIONS distribution by entity type

| Entity Type | Mentioned Entities | Mention Count |
|-------------|-------------------|---------------|
| Person | 2,114 | 3,412 |
| Product | 97 | 180 |
| Law | 36 | 76 |
| Concept | 10 | 29 |
| Event | 13 | 18 |
| Quantity | 14 | 17 |
| Language | 3 | 12 |
| Organization | 6 | 11 |
| Method | 3 | 6 |
| Technology | 1 | 2 |
| Entity (generic) | 1 | 1 |
| Programming Language | 1 | 1 |
| Library | 1 | 1 |
| Algorithm | 1 | 1 |

Only 6 of 1,966 Organizations are mentioned by Facts. Only 1 of 2,013 generic Entities. The graph's only functional pathway is Person→Fact→Person.

### HOW
```cypher
MATCH (f:Fact)-[m:MENTIONS]->(e:Entity)
RETURN e.type, count(DISTINCT e) AS mentioned_entities, count(m) AS mention_count
ORDER BY count(m) DESC
```
Confidence: 0.99.

---

## Finding 4: The "Entity" Generic Type Is a Dumping Ground

### WHAT
2,013 entities have `type = 'Entity'` — a generic label that provides no type information. 98.4% of these are orphans.

### WHY this matters
A type system where the most common label is "unspecified" is not a type system — it's a failure of classification. The Entity bucket contains: numbers (1, 2, 3…), tool names (Obsidian), quantities (five, thousands), and surface-form strings. These should have been classified as Quantity, Product, or discarded as noise.

### HOW
```cypher
MATCH (e:Entity) WHERE e.type = 'Entity' RETURN e.name LIMIT 30
```
Sample: "five", "Obsidian", "thousands", "three", "10-15", "two", "5", "Hotkeys". Confidence: 0.90.

**Fix**: Add a post-extraction classifier pass. If an entity's name is numeric, classify as Quantity. If it matches known tool names, classify as Product. If it's a stopword/number-word, discard.

---

## Comparison to Previous Reports

**First report — no baseline.** This establishes baseline metrics:
- Orphan rate: 68%
- Person misclassification rate: ~46%
- Entity type diversity: 18 types, but only 3 are functionally alive (Person, Concept, Law)
- Total entities: 10,483

---

## Cumulative Coverage Tracker

| Cycle | Entity Types Audited | Issue Categories | New Orphan Types Found |
|-------|---------------------|-----------------|----------------------|
| Week 1 (2026-05-09) | All 18 | Orphan, Misclassification | 10 nearly-total-orphan types |

---

## Recommendations

### Immediate (this cycle)
1. **Tag the 1,319 likely-misclassified Person nodes** with `original_label: 'Person'` and a proposed reclassification. Create a migration Cypher script.
2. **Purge the 796 MonetaryValue orphans** — they are $ amounts with zero context and zero connections.
3. **Purge the 552 TemporalEntity orphans** — isolated dates with no semantic anchor.

### This week
4. Reclassify the ~400 math-formula Persons as `Concept` or `Formula` (new type).
5. Reclassify the ~300 HTML/SVG Persons as extraction noise — delete them.
6. Run the "Entity" generic-type orphans through a reclassification pass.

### Next cycle (Week 2: Duplicates + Stale)
7. After the Person purge, re-run duplicate detection — many current Person duplicates may be math-fragment variants.
8. Check stale Fact nodes — do Facts point to now-deleted entities?

---

## Next Cycle Target

**Week 2: Duplicates + Stale** — but with a twist. Given the severity of orphan/misclassification issues, Week 2 should include:
- Duplicate detection across Person (post-cleanup)
- Stale Fact detection (Facts that mention only orphan entities)
- A first pass at the Organization type — can we recover and link the 1,960 orphan Organizations?

---

*Generated by Wiki Librarian, Cycle 1. Query runtime: ~30s. Full results archived at `~/Repositories/ai_workspace/wiki-librarian-lab/data/`.*
