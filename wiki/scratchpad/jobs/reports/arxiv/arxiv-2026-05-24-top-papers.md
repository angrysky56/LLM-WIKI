---
summary: 3 papers from 2026-05-24 run: ConvexTok (LP tokenization), AwareVLN (sparse self-aware VLN), AlphaProof Nexus (Lean formal proof search)
tags: [arxiv, daily-report]
updated: 2026-05-24T08:35:00Z
created: 2026-05-24T08:35:00Z
---

# arxiv Report — 2026-05-24

## Papers Processed

3 papers selected from the 2026-05-21 submission batch (2026-05-24 discovery run), processed via arXiv API search + curl PDF download + direct wiki page writing.

|| # | Paper | arXiv ID | Primary Category | Core Finding |
|---|-------|----------|------------------|--------------|
| 1 | **ConvexTok** | 2605.22821 | cs.CL | LP-based global tokeniser construction replaces greedy BPE; certifies tokenizers are within 1% of optimal compression |
| 2 | **AwareVLN** | 2605.22816 | cs.RO | Sparse self-aware reasoning at key navigation nodes — the model autonomously decides when to reason about its own state and task progress without 3D sensors |
| 3 | **AlphaProof Nexus** | 2605.22763 | cs.AI | LLM + Lean formal proof search on open Erdős problems; basic LLM+Ralph loop matched full RL agent on all 9 Erdős solutions |

## Theme: Verification, Boundedness, and the Shift Toward Simple Agentic Loops

This batch converges on three related ideas:

1. **Formal verification as a structural component**: ConvexTok's LP lower bound and AlphaProof Nexus's Lean compiler both provide *falsifiable, automatic* verification that prevents downstream failures. The convex relaxation gives a provable gap certificate; the Lean compiler gives a hard step-by-step check. Both eliminate the need for trusted human review at the output stage.

2. **Sparse reasoning triggers**: AwareVLN's insight — that a VLM-based agent should *decide for itself* when to engage in structured reasoning rather than doing so at fixed intervals — parallels VPO's vector-valued rewards (last batch) and DeltaDirect's projector-level auxiliary objective (last batch): the bottleneck is not whether the model *can* do something, but whether it does it at the right times with the right resource allocation.

3. **Simple loops beat specialized systems as LLMs improve**: AlphaProof Nexus's most striking result is that a basic LLM+Ralph loop (no RL, no evolutionary coordination, no AlphaProof) solved all 9 Erdős problems the full system did, at higher per-problem cost. This is a strong data point for the thesis that [[agentic-research]] has been tracking: when general-purpose LLMs become capable enough, the marginal value of specialist trained modules decreases. The harness becomes less necessary.

## Paper Summaries

### 1. ConvexTok: Tokenisation via Convex Relaxations (2605.22821)

**Problem**: BPE and Unigram are greedy — they make locally optimal merge decisions without considering the resulting vocabulary as a whole. Finding a truly optimal tokeniser is NP-hard.

**Key innovation**: Formulate tokeniser construction as an integer program, relax to a linear program (LP), solve with standard convex optimisation tools. The LP solution is near-integral at practical vocabulary sizes and provides a lower bound on achievable compression.

**Results**: At common vocabulary sizes, all tokenisers (BPE, Unigram, ConvexTok variants) are within 1% of optimal per the LP bound. The Bias rounding scheme consistently outperforms all others on intrinsic metrics (compression rate, vocabulary utilisation, Rényi entropy). Det rounding performs best on bits-per-byte for downstream language modeling.

**Wiki connections:** [[mop-explorer]], [[verifier-graph]], [[efhf]]

### 2. AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation (2605.22816)

**Problem**: VLM-based VLN methods predict actions end-to-end but have no self-awareness — they cannot reason about their own spatial state, task progress, or alignment with instructions. Explicit map-based approaches require 3D sensors and SLAM, which limit vision-language pretraining.

**Key innovation**: A sparse self-aware reasoning mechanism that triggers structured analysis only at key navigation decision nodes. The model autonomously decides when to engage in reasoning. A progress-division data engine generates training data for task progress analysis and high-level planning.

**Results**: Significantly outperforms prior VLN state-of-the-art across Habitat simulator benchmarks. Can recognise and correct its own navigation errors — "I went the wrong way" followed by planned backtracking.

**Wiki connections:** [[efhf]], [[maximum-occupancy-principle]], [[verifier-graph]], [[agentic-research]]

### 3. AlphaProof Nexus: Advancing Mathematics Research with AI-Driven Formal Proof Search (2605.22763)

**Problem**: LLM natural language proofs contain logical hallucinations requiring expensive expert review. Hallucination cascades limit the complexity of tasks delegable to AI.

**Key innovation**: Generate proofs in Lean (formal language with mechanical step-by-step verification). Full-featured agent coordinates subagents via evolutionary algorithm + AlphaProof RL prover. Basic agent uses LLM + Lean alternating in a Ralph loop — no specialist training required.

**Results**: Full agent: 9/353 open Erdős problems solved (two open 56 years), 44/492 OEIS conjectures proved, active research in combinatorics/optimization/graph theory/algebraic geometry/quantum optics. **Critical finding**: Basic agent solved all 9 same Erdős problems, at higher per-problem cost (~$$100-500/problem). This is interpreted as evidence that "simple agentic loops" increasingly replace specialist trained systems as LLMs improve.

**Wiki connections:** [[verifier-graph]], [[mop-explorer]], [[agentic-research]], [[efhf]], [[sheaf-consistency-enforcer]]

## Wiki Updates

- New source pages: 3
  - `wiki/sources/papers/tokenisation-convex-relaxations-2026.md`
  - `wiki/sources/papers/awarevln-self-aware-vision-language-navigation-2026.md`
  - `wiki/sources/papers/alphaproof-nexus-formal-proof-search-2026.md`
- Tags added: `tokenisation`, `convex-optimization`, `vocabulary-learning`, `bpe`, `vision-language-navigation`, `self-awareness`, `embodied-ai`, `formal-proof`, `lean`, `alphaproof`, `agentic-reasoning`, `mathematics`, `verifier`, `Ralph-loop`, `llm`
- Total wiki pages: ~317 (up from ~314)

## Notes

- **arXiv API**: Search via API succeeded with no rate limiting issues
- **PDF download**: All 3 PDFs downloaded successfully via curl (200 status each)
- **No MCP fallback needed**: API behaved normally throughout
- **Theme continuation from last batch**: "layer-boundary failures" (last batch) → "verification and boundedness" (this batch). Both are about what structural scaffolding enables frontier capabilities.
- **AlphaProof Nexus basic/full result** is a significant data point: the harness value-add decreases as base LLMs improve — the same conclusion reached by MOSS (last batch) from the self-evolution angle

## Next Run
- **Schedule**: 2026-05-26 8:20AM
- **Potential theme**: Continued exploration/completion scaffolding (Recuriosity, VPO), formal verification integration (AlphaProof Nexus), and tool-use / API / MCP infrastructure papers (HarnessAPI seen in batch)