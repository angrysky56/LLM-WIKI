---
summary: AGEM 1-iter exploration of wiki/concepts/persistent-knowledge-compilation.md — cleaned duplicate Connections sections, added 3 new sections (Invalidation/EDM Lens, PKC in Agent World Models, Failure Modes), answered all 3 open questions, added 4 new open questions, expanded wikilink network from ~15 to ~30.
tags: [agem, persistent-knowledge-compilation, pkc, llm-wiki, wiki-curation, agent-world-models, iter1, edm-framework]
updated: 2026-06-03T12:57:00Z
created: 2026-06-03T12:57:00Z
---

---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "AGEM 1-iter exploration of wiki/concepts/persistent-knowledge-compilation.md — cleaned duplicate Connections sections, added 3 new sections (Invalidation/EDM Lens, PKC in Agent World Models, Failure Modes), answered all 3 open questions, added 4 new open questions, expanded wikilink network from ~15 to ~30."
tags: [agem, persistent-knowledge-compilation, pkc, llm-wiki, wiki-curation, agent-world-models, iter1, edm-framework]
sources:
  - http://localhost:5173/
status: active
confidence: 0.9
---

# AGEM Wiki Introduction — Prior to Synapse Fixes (PKC Exploration)

**Source**: AGEM Interface (localhost:5173) chat export
**Engine**: AGEM stack (Mace4, sheaf-consistency-enforcer, ADMM, formula-evaluator) **+** `project-synapse` MCP (22 tools)
**Captured**: 2026-06-03
**Archived**: `Clippings/articles/2026/AGEM wiki introduction prior to synapse fixes.md` (22KB)
**Target file explored**: [[concepts/persistent-knowledge-compilation]]
**Iteration state**: 1, nascent, NORMAL, CDP 1.99, 134 nodes, 549 edges, 8 communities

> **Note on this source**: this is an **AGEM + LLM-WIKI cross-system** run — the agent loaded the project's Synapse MCP tools and used them to explore, then expand, an existing wiki concept page. The mode is "wiki curation via AI assistant" rather than "raw file ingestion."

## What It Is

A 1-iteration AGEM run that used the `project-synapse` MCP to:

1. Read the existing [[concepts/persistent-knowledge-compilation|PKC concept page]]
2. Explore related concept pages and the structural health of the wiki
3. **Edit the PKC page** to fix structural issues, add new sections, answer open questions, and expand the wikilink network

The title's "prior to synapse fixes" is a retrospective flag — this run happened *before* a round of bug fixes to the Synapse MCP (referenced in the most recent carryover note about the `SynapseMCPServer` → `SynapseServer` class-name patch).

## Changes Made to the PKC Page

### 1. Structural cleanup

- Removed the **duplicate `## Connections` sections** that were present (the original page had two, with different formatting)
- Fixed frontmatter: added `created`, `status: active`, `confidence: 0.9`, and a proper `tags` list
- Fixed source-file paths to point to actual existing pages in `wiki/sources/papers/` and `wiki/synthesis/`

### 2. Three new sections added

- **`## Invalidation and the EDM Lens`** — substantive treatment of how the [[edm-framework]] disruption score is the operational signal for when a compiled base needs updating. Links the ID/OOD/convergent taxonomy directly to PKC's failure modes.
- **`## PKC in Agent World Models`** — incorporates the [[cognitive-world-models-for-llm-agents]] discovery (2026-06-26 report) which positions PKC as Layer 3 of the four-layer cognitive world model for text-based agents. This is a *new* role for PKC beyond static knowledge bases.
- **`## Failure Modes`** — explicit list of five failure modes with counters: staleness, garbage accumulation, saturation, contradiction drift, manual-maintenance break. Each counter references a real vault mechanism.

### 3. All three open questions answered with concrete mechanisms

| Original Question | Answer |
| --- | --- |
| "How to handle contradictions without human arbitration?" | SSL `logical.contradictions` field + [[sheaf-consistency-enforcer]] coboundary monitoring + [[mcp-logic]] consistency check + Markovian `divergence_signal`. Detection, not resolution; flagged traceable inconsistency, not silent picking-a-side. |
| "At what scale does compilation cost exceed query-time RAG cost?" | Crossover happens at ~N=3 queries for typical personal knowledge work (per [[llm-wiki-pattern]] observation); LLM-WIKI itself is the running proof (5 months, 1,326 pages, N>>3, faster than equivalent RAG). **Saturation caveat added**: duplicate-detection rate is the soft signal. |
| "Can compilation be made incremental enough to be real-time?" | Three-level answer: per-document ingest already real-time; background synthesis real-time; query-time incremental re-compilation gated by [[mop-edm-cognitive-architecture|MOP-EFHF]] Kernel 1 closure is the convergence direction. Bottleneck is LLM synthesis latency (~5 min), not the logic. |

### 4. Four new open questions added for the next iteration

Non-text modalities, compilable vs uncompilable domains, cross-vault PKC, PKC-as-a-service.

### 5. Wikilink network expanded from ~15 to ~30 outbound links

Added: `edm-framework`, `causal-state-edm-ood-isomorphism`, `mop-edm-cognitive-architecture`, `bounded-structured-memory`, `markovian-carryover`, `bounded-memory-budget-optimization`, `bounded-rationality`, `agent-native-design`, `mop-explorer`, `meta-harness`, `sources/papers/ramirez-ruiz-mop-2024`, `sources/papers/kim-ahn-edm-2026`, `synthesis/wiki-indexing-theory`, `extraction-quality-audit`, and the four agent sheets (`librarian-agent`, `researcher-agent`, `insights-agent`, `news-agent`). This addresses the HITS finding that PKC was theoretically central but topologically peripheral.

### 6. Empirical Anchors section added

Cites the LLM-WIKI itself, GoodRobot (the counterexample), bounded-memory-budget-optimization (QES/ESSA/LLaMA-NAS), the Memory Curse paper, and the MOP-EDM synthesis as Prover9-verified.

## The After-State

The PKC page is now the formal central node for the PKC concept — it has the theoretical grounding (MOP/EDM/EFHF), the operational mechanism (SSL + Markovian + sheaf-enforcer), the empirical evidence (this vault), the failure modes with counters, and answered open questions. The HITS analysis next cycle should surface it as a load-bearing authority, and the next researcher/insights cycle will be able to use the answered questions to generate new synthesis without re-doing the work.

## Connections

- [[concepts/persistent-knowledge-compilation]] — the page that was edited
- [[entities/projects/agem-interface]] — the engine
- [[sources/articles/agem-logic-test-1]] — sister validation run
- [[sources/articles/agem-cycle-failures-iter3]] — sister 3-cycle run
- [[entities/projects/project-synapse]] — the MCP that was used to explore the wiki
- [[wiki/agents/ingest-agent]] — sister agent sheet

## Methodological Note

This run demonstrates the **AGEM-as-wiki-curator** pattern: rather than just ingesting raw files into the wiki, AGEM + Synapse MCP can be used to **edit existing concept pages** with structural cleanup, answer-questions-from-context, and cross-link expansion. The Synapse MCP's `wiki_search`, `wiki_read_page`, `wiki_write_page`, and `query_knowledge` tools are the read/write surface; AGEM provides the iterative refinement loop. This is a different ingestion mode from the file-based runs in the rest of the trilogy.
