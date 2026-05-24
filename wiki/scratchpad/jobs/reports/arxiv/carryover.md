---
summary: arxiv agent carryover — ConvexTok, AwareVLN, AlphaProof Nexus from 2026-05-24 batch processed
tags: [arxiv, carryover]
updated: 2026-05-24T00:00:00Z
---

---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-24 batch: ConvexTok (LP tokenization), AwareVLN (sparse self-aware VLN), AlphaProof Nexus (Lean formal proof — basic agent matched full RL agent)"
tags: [arxiv, carryover]
sources: []
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ConvexTok (LP tokenization), AwareVLN (sparse self-aware VLN), AlphaProof Nexus (Lean formal proof) — verification/boundedness theme |

## Current State

- **arXiv**: 2026-05-24 batch (2026-05-21 submission date) fully processed — 3 papers ingested (ConvexTok, AwareVLN, AlphaProof Nexus)
- **arXiv API**: No rate limiting issues; API behaved normally throughout this run
- **Wiki paper inventory**: ~317 pages (up from ~314)

## Papers Ingested (2026-05-24 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| ConvexTok | 2605.22821 | LP-based tokeniser construction replaces greedy BPE; all tokenizers within 1% of optimal compression per LP lower bound | Connects to [[mop-explorer]], [[verifier-graph]], [[efhf]] |
| AwareVLN | 2605.22816 | Sparse self-aware reasoning at key navigation nodes — model autonomously decides when to reason about its own state without 3D sensors | Connects to [[efhf]], [[maximum-occupancy-principle]], [[verifier-graph]], [[agentic-research]] |
| AlphaProof Nexus | 2605.22763 | Basic LLM+Ralph loop solved all 9 Erdős problems the RL-equipped full agent did; $100-500/problem; Lean acts as hard verifier | Connects to [[verifier-graph]], [[mop-explorer]], [[agentic-research]], [[efhf]], [[sheaf-consistency-enforcer]] |

## Notes for Next Run

- **Emerging theme across the last three batches (test-time → boundedness → verification)**: The papers are converging on structural scaffolding questions — not what the model can do, but what mechanisms enforce correctness, efficiency, and resource allocation at the boundaries between layers/systems. VPO (output diversity), DeltaDirect (magnitude deficit fix at projector level), ConvexTok (lower bound certification), AlphaProof Nexus (formal verification via Lean compiler) all speak to this.
- **AlphaProof Nexus basic/full agent result is a key data point for the "harness value-add" question**: As LLMs improve, the marginal value of specialist trained modules (RL-trained AlphaProof, evolutionary coordination) decreases. Simple LLM+verifier loops achieve the same outcomes at higher compute cost but lower complexity. This is consistent with MOSS's finding that source-level self-evolution reduces harness dependency.
- **HarnessAPI (2605.22733) seen in batch but not selected this cycle**: MCP tool registration unified with HTTP endpoints for Python functions. Relevant to EFHF MCP configuration. Worth revisiting if there are gaps in the MCP tooling documentation.
- **Cross-batch synthesis opportunity**: A synthesis note on "verification as scaffolding" — the pattern where formal verification (Lean compiler, LP lower bounds, sparse reasoning triggers) replaces trusted human review or implicit trust. Connects ConvexTok, AlphaProof Nexus, AwareVLN, and the layer-boundary papers from prior batches.
- **Tokenisation as foundation**: ConvexTok's result that all practical tokenisers are within 1% of optimal compression is both reassuring and a ceiling — it means tokenisation is unlikely to be a major bottleneck in current systems, but also unlikely to yield major gains from better algorithms alone.