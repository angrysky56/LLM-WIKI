---
summary: IR and indexing theory applied to LLM-WIKI: TOC vs conceptual index, controlled vocabulary, thesaurus relationships, HITS on wikilinks, mere mentions, and GAAC clustering for wiki health
tags: [indexing, information-retrieval, controlled-vocabulary, thesaurus, HITS, PageRank, clustering, GAAC, wiki-organization, synthesis]
updated: 2026-04-11T04:47:47Z
created: 2026-04-11T04:47:47Z
---

# Wiki Indexing Theory — Implications for LLM-WIKI

**Type:** Synthesis  
**Source:** NotebookLM notebook `information-retrieval-indexing-toc` (17 sources on IR and indexing theory)  
**Confidence:** 0.92 — established IR theory applied to our specific system  

---

## The Central Distinction: TOC vs. Index

Professional information science draws a hard line between two navigation paradigms:

| | Table of Contents | Back-of-Book Index |
|---|---|---|
| **Organises by** | Physical structure (position in document) | Intellectual concept (meaning, regardless of position) |
| **Order** | Sequential — mirrors document flow | Alphabetical / associative — mirrors concept space |
| **Created by** | Mechanical extraction of headings | Human intellectual analysis of content |
| **Question answered** | "What is in this document and where?" | "Where is this concept discussed?" |

**Our `wiki/index.md` is a TOC in disguise.** It lists pages in creation/alphabetical order with one-line summaries. It answers "what pages exist" but not "where is the concept of X discussed across pages." A genuine conceptual index would be a separate structure.

---

## The Open Indexing Problem

The notebook distinguishes **closed indexing** (back-of-book, finished once) from **open indexing** (database/periodical, never finished). Our wiki is open — new pages are added every session. Open indexing has a specific failure mode the book identifies: **inconsistent terminology over time**, because different indexers (or the same indexer in different sessions) apply different terms to the same concept.

The canonical solution is a **controlled vocabulary**: a structured list where each concept has one preferred term, with USE/UF (equivalence), BT/NT (hierarchical), and RT (associative) relationships explicitly defined.

**Our current tag system is an informal, uncontrolled vocabulary.** Tags like `embeddings`, `embedding`, `vector-embedding`, and `vector-search` are all in use with no declared relationship between them. This is the open indexing consistency failure.

---

## Thesaurus Relationships Mapped to Wiki Structures

The three thesaurus relationship types map onto structures we already partially have:

| Relationship | Thesaurus notation | Our current equivalent | Gap |
|---|---|---|---|
| **Equivalence** | USE / Used From (UF) | None | Tags are not deduplicated or aliased |
| **Hierarchical** | BT (Broader Term) / NT (Narrower Term) | None | No taxonomy — `vector-search` has no explicit BT of `retrieval` |
| **Associative** | RT (Related Term) — always bidirectional | Wikilinks — but not enforced as reciprocal | Links often aren't two-way |

**POPSI's Classaurus** is the most interesting precedent: it includes equivalence and hierarchical relationships but *intentionally excludes* associative ones, letting document content define associations dynamically through permutation. The wiki mirrors this: the tag taxonomy should handle equivalence and hierarchy; wikilinks should handle association.

**POPSI's DEAP categories** map cleanly onto our page type system:

| POPSI | Our page type |
|---|---|
| Discipline (D) | Domain tag (e.g., `information-retrieval`, `knowledge-management`) |
| Entity (E) | `wiki/entities/` — tools, people, projects |
| Action (A) | Process pages (ingest, retrieve, synthesize) — currently under-represented |
| Property (P) | Frontmatter fields (confidence, status, tags) |

We have no explicit Action-type pages. Processes like "how ingestion works" or "how retrieval works" are scattered across entity and concept pages rather than being first-class citizens.

---

## PageRank and HITS on the Wikilink Graph

The notebook covers both PageRank (random surfer steady-state) and HITS (hub/authority mutual reinforcement). Both are directly applicable to our wikilink graph.

**HITS is the more useful model for our wiki:**

- **Authorities** = pages that many other pages link *to* — the canonical reference nodes. In our wiki: `[[neo4j]]`, `[[project-synapse]]`, `[[rag]]`. High-authority pages deserve the richest, most carefully maintained content.
- **Hubs** = pages that link *to* many good authorities — navigational aggregators. In our wiki: `[[synapse-llm-wiki-operating-guide]]`, `[[synapse-retrieval-architecture]]`. Hubs are most useful to agents starting cold.

**The mutual reinforcement insight:** a page becomes a better authority by being linked from better hubs; a page becomes a better hub by linking to better authorities. This means: **agent-facing orientation pages (hubs) should preferentially link to the most information-dense entity/concept pages (authorities)**, not to each other.

**Practical implication:** run HITS on the wikilink adjacency matrix periodically. Pages scoring high on authority signal that their content is load-bearing — high value to maintain and deepen. Pages scoring high on hub signal they're navigation layers — their job is comprehensive linking, not deep content.

---

## The "Mere Mentions" Problem

Professional indexers filter out *mere mentions* — passing references that provide no substantive information. The example given: indexing "Winston Churchill" because the text says "But John Major was no Winston Churchill" — the page number gives the reader nothing useful about Churchill.

**We have this problem with wikilinks.** A `[[neo4j]]` link in the sentence "unlike Neo4j, which stores X..." carries very different retrieval weight than `[[neo4j]]` in a section explicitly discussing Neo4j's architecture. The linter treats both identically.

**Professional practice distinction:**
- **Substantive discussion** → index it (= weight the wikilink)
- **Mere mention / passing reference** → don't index it (= don't add wikilink, or weight low)

**Implication for us:** wikilinks in `## Connections` sections are deliberate associative pointers — high weight. Wikilinks embedded in body prose are often mere mentions — lower retrieval weight. The wiki_adapter's `get_wikilink_neighbors` could be enhanced to weight by section context.

---

## Clustering for Wiki Health

The notebook covers both K-means and Hierarchical Agglomerative Clustering (HAC). For our wiki:

- **K-means** requires pre-specifying K — bad fit. We don't know how many topic clusters we have.
- **GAAC** (Group-Average HAC) is recommended as avoiding chaining, outlier sensitivity, and inversions — the preferred algorithm when N is small enough to afford O(N²).

At 27 pages, N² = 729 operations — trivially fast. **GAAC on our page embeddings would surface:**
- Pages too similar → candidate for merging (or one is redundant)
- Pages in the same cluster that don't link to each other → missing wikilinks
- Isolated pages in their own singleton cluster → orphans with no natural home

This is a natural addition to the `generate_insights` pipeline in the Zettelkasten engine.

---

## Concrete Improvements for LLM-WIKI

In priority order:

**1. `wiki/concepts/tag-taxonomy.md` — controlled vocabulary**  
Define preferred tags with USE/UF (equivalence) and BT/NT (hierarchical) relationships. Every new page checks against it. Solves the open indexing consistency problem.

**2. Conceptual index separate from TOC**  
`wiki/index.md` stays as TOC. Add `wiki/concept-index.md` — a hand-maintained and auto-generated map of concepts to pages, regardless of page structure. Allows "where is X discussed?" queries without relying on search.

**3. Reciprocal wikilink enforcement in lint**  
If page A links to page B, `wiki_lint` should flag if B doesn't link back to A (unless the link is clearly a mere mention). Thesaurus RT relationships are always bidirectional.

**4. HITS scoring in Zettelkasten engine**  
Compute hub and authority scores on the wikilink adjacency matrix. Surface high-authority pages for content deepening; ensure high-hub pages have comprehensive link coverage.

**5. Section-weighted wikilinks in `get_wikilink_neighbors`**  
Links found in `## Connections` sections score higher than links in body prose. Operationalises the "mere mentions" filter without removing links.

**6. GAAC clustering in `generate_insights`**  
Run GAAC on page embeddings to find natural topic clusters. Flag similar pages as merge candidates; flag same-cluster pairs with no link as missing connections.

---

## Connections

- [[synapse-retrieval-architecture]] — the retrieval pipeline these improvements feed into
- [[graphrag]] — graph-based retrieval; HITS directly applicable
- [[zettelkasten-engine]] — where clustering and HITS scoring should be implemented
- [[project-synapse]] — the system being improved
- [[llm-wiki-pattern]] — the base pattern this extends
- [[edm-framework]] — parallel: EDM's future vectors as a citation PageRank analogue
