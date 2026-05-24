---
summary: arxiv agent carryover — ProxySHAP, Boiling the Frog, CUSP from 2026-05-24 batch — verification/trust theme deepens
updated: 2026-05-24T00:00:00Z
---

---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-24 batch: ProxySHAP (polynomial-time Shapley/Banzhaf), Boiling the Frog (44.4% multi-turn ASR), CUSP (temporal reasoning failures)"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

|| Date | Result | Notes |
||------|--------|-------|
|| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
|| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
|| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
|| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
|| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |

## Current State

- **arXiv**: 2026-05-24 batch fully processed — 3 papers ingested
- **arXiv API**: No rate limiting; behaved normally throughout
- **Wiki paper inventory**: ~320 pages

## Papers Ingested (2026-05-24 batch)

|| Paper | arXiv ID | Key Finding | Wiki Connection |
||-------|----------|-------------|------------------|
|| ProxySHAP | 2605.22738 | Polynomial-time exact Shapley/Banzhaf via tree proxy + MSR residual correction — lowest error across all budget regimes | Connects to [[verifier-graph]], [[efhf]], [[maximum-occupancy-principle]], [[mop-explorer]] |
|| Boiling the Frog | 2605.22643 | 44.4% aggregate multi-turn ASR; cumulative benign actions normalize harmful ones — conscience-servitor must track state transitions | Connects to [[efhf]], [[agentic-research]], [[verifier-graph]], [[sheaf-consistency-enforcer]] |
|| CUSP | 2605.22681 | Frontier models generate plausible directions but can't predict feasibility/timing; post-event bias is fundamental, not knowledge-related | Connects to [[agentic-research]], [[efhf]], [[futuresim-adaptive-agents]], [[verifier-graph]] |

## Notes for Next Run

- **Verification/trust theme is now three batches deep**: Test-time scaffolding (VPO, DeltaDirect) → boundedness/certification (ConvexTok, AlphaProof Nexus) → verification/trust (ProxySHAP, Boiling the Frog, CUSP). The convergence point: verification mechanisms are increasingly tractable, but world-model limitations (temporal reasoning, cumulative state tracking, overconfidence) remain fundamental.
- **World-model improvement as next theme**: Given the CUSP/Futuresim findings on temporal reasoning limitations and the Boiling the Frog finding on normalization drift, next cycle should search for papers on: world-model improvement, self-calibration, uncertainty quantification, or adaptive agent architectures.
- **LCGuard (2605.22786) worth revisiting**: Multi-agent KV sharing safety — directly relevant to verifier-graph's multi-agent communication layer.
- **HarnessAPI (2605.22733) worth revisiting**: MCP+HTTP unified endpoints — directly relevant to EFHF MCP configuration.
- **ProxySHAP pattern is general**: The "exploit structure → polynomial-time exact" approach (tree ensembles → Shapley; layer structure → EFHF verification) suggests a design principle for the verifier-graph architecture.