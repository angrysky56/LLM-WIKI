---
summary: 3 papers from 2026-05-20 batch: EqR (attractor-based reasoning), DeepWeb-Bench (derivation > retrieval failure), hyperparameter transfer (embedding LR)
tags: [arxiv, daily-report]
updated: 2026-05-21T16:53:33Z
created: 2026-05-21T16:53:33Z
---

---
created: 2026-05-21T10:00:00Z
updated: 2026-05-21T16:55:00Z
type: report
summary: "3 papers from 2026-05-20 arXiv batch: Equilibrium Reasoners (attractor-based test-time scaling), DeepWeb-Bench (derivation > retrieval as failure mode), hyperparameter transfer (embedding LR is the key)"
tags: [arxiv, daily-report]
sources: []
status: active
confidence: high
---

# arxiv Report — 2026-05-21

## Papers Processed

**3 new papers ingested** from the 2026-05-20 arXiv batch.

All three were found via arXiv search after the previous run was rate-limited. MCP server PDF conversion failed for two papers (structural parsing error `'NoneType' object has no attribute 'tables'`); bypassed using `wiki_fetch_url` on arXiv abstract pages, which succeeded and ingested content to Neo4j.

| # | Paper | arXiv ID | Primary Category | Core Finding |
|---|-------|----------|------------------|--------------|
| 1 | **Equilibrium Reasoners (EqR)** | 2605.21488 | cs.LG | Learned attractor landscapes enable test-time compute scaling without external verifiers — 2.6% → 99% on Sudoku-Extreme by unrolling 40K equivalent layers |
| 2 | **DeepWeb-Bench** | 2605.21482 | cs.AI | Deep research benchmark where derivation + calibration failures account for >70% of errors (retrieval is only 12–14%); cross-model agreement rho=0.61 |
| 3 | **Kalra & Barkeshli** | 2605.21486 | cs.LG | μP's advantage over standard parameterization stems almost entirely from maximizing embedding layer LR — embedding LR is a bottleneck in SP that induces training instabilities |

## Thematic Threads

### Thread 1: Reasoning as Dynamical Systems

EqR connects a growing cluster: [[chen-molecular-cot-2026]] (three-bond CoT structure), [[self-prompting-via-production-stage-architecture]] (self-directed compute as attractor navigation), [[bae-mor-2025]] (Mixture of Recursions as multi-scale attractor traversal). The attractor perspective provides a **mechanistic lens** for what "thinking longer" actually does — not just more computation, but navigation toward solution-aligned fixed points in latent space.

### Thread 2: Derivation > Retrieval as Agent Failure Mode

DeepWeb-Bench confirms and extends FutureSim's finding: the bottleneck in agentic deep research is not retrieval (12–14% of errors) but **derivation and calibration** (>70%). This is consistent with [[spin-vs-substrate]] — models fail to correctly trace the logical consequences of retrieved evidence, not the retrieval itself. This has direct implications for [[agentic-research]] tool design: retrieval is largely solved; derivation and calibration are the open problems.

### Thread 3: Embedding Layer as Training Stability Bottleneck

Kalra & Barkeshli reframes a component that was previously underappreciated. If the embedding LR is the primary source of μP's transfer advantage over SP, this is a simple fix with large-scale consequences for LLM training stability and hyperparameter extrapolability.

## Wiki State

- **New source pages**: `wiki/sources/papers/equilibrium-reasoners-eqr-2026.md`, `wiki/sources/papers/deepweb-bench-2026.md`, `wiki/sources/papers/kalra-barkeshli-hyperparameter-transfer-2026.md`
- **Graph ingestion**: 79 total nodes, 30 total edges added across 3 papers
- **Archived**: All three to `Clippings/papers/2026/`
- **Total wiki pages**: 302 (up from 299)

## Connections Summary

| New Paper | Connects To |
|-----------|-------------|
| EqR | [[chen-molecular-cot-2026]], [[self-prompting-via-production-stage-architecture]], [[bae-mor-2025]], [[load-bearing-reasoning]] |
| DeepWeb-Bench | [[agentic-research]], [[futuresim-adaptive-agents]], [[spin-vs-substrate]], [[graphrag]] |
| Kalra & Barkeshli | [[ml-evolution]], [[superbpe]], [[eml-operator]] |

## Jobs Sheet Update

- **Status**: complete
- **arXiv rate limit**: resolved — rate-limited run preceded successful search
- **MCP conversion note**: PDF conversion via arxiv-mcp-server unreliable for some papers; `wiki_fetch_url` on abstract pages is the working fallback
- **Next run**: daily at 10:00 UTC
