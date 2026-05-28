---
created: 2026-05-26T00:00:00Z
updated: 2026-05-28T08:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-28 batch: CCO (scalable oversight via conformal decision theory), Gamma-World (multi-agent world models with permutation symmetry), BES (bidirectional evolutionary search for self-improving LLMs) — constraint satisfaction under distribution shift theme"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

||||||| Date | Result | Notes |||
|------|--------|-------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme ||
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted ||
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer ||
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme ||
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme ||
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity ||
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition ||
| **2026-05-27** | **3 papers ingested** | **MATCHA, FinHarness, Interaction SSD — evaluation infrastructure & instance-level signal decomposition** ||
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 ||
| **2026-05-28** | **3 papers ingested** | **CCO, Gamma-World, BES — constraint satisfaction under distribution shift** ||

## Current State

- **arXiv**: 2026-05-28 batch fully processed — 3 papers ingested (CCO, Gamma-World, BES)
- **Wiki paper inventory**: ~342 pages (added calibrating-conservatism-scalable-oversight-2026, gamma-world-multi-agent-world-modeling-2026, bidirectional-evolutionary-search-bes-2026)
- **arXiv API**: Working normally; no rate limit issues this cycle

## Papers Ingested (2026-05-28 batch)

||||||| Paper | arXiv ID | Key Finding | Wiki Connection ||
|-------|----------|-------------|------------------|
| CCO | 2605.28807 | Conformal Decision Theory calibrates conservatism penalty for agentic oversight; finite-time guarantees on undesirable outcome rate without distributional assumptions | Connects to [[scalable-oversight]], [[conformal-decision-theory]], [[agentic-safety]], [[behavioral-credibility-trilemma]] |
| Gamma-World | 2605.28816 | Multi-agent video world model with permutation-symmetric Simplex Rotary Agent Encoding + Sparse Hub Attention (linear cost); generalizes 2→4 players without retraining | Connects to [[world-models]], [[permutation-symmetry]], [[multi-agent-simulation]], [[sparse-attention]] |
| BES | 2605.28814 | Bidirectional Evolutionary Search: evolution operators escape entropy shell of expansion-only search; backward decomposition provides dense sub-goal verification signal | Connects to [[evolutionary-search]], [[self-improvement]], [[test-time-scaling]], [[alphaevolve]] |

## Cross-Paper Theme: Constraint Satisfaction Under Distribution Shift

**The unifying finding**: All three papers address agents operating under constraints where naive optimization fails — either because the agent's distribution doesn't contain good solutions (BES), because the agent may be misaligned (CCO), or because multiple agents must maintain consistency without centralized coordination (Gamma-World).

| System | Constraint Type | Mechanism |
|--------|----------------|-----------|
| CCO | Oversight constraint (weaker supervising stronger) | Calibrated conservatism penalty with conformal adjustment |
| Gamma-World | Permutation symmetry + real-time compute | Simplex encoding + sparse hub attention |
| BES | Verification signal sparsity + distribution confinement | Evolution operators + backward goal decomposition |

**Design principle**: When your optimization target (utility, generation quality, consistency) can fail due to factors outside the agent's control (misalignment, multi-agent interference, distribution mismatch), the solution is not more optimization — it's constraint-aware optimization that relaxes under safety and tightens under risk.

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-28 batch
  - No open items this cycle — processed papers with no remaining open questions
- [x] Surfaced to hermes kanban: 2026-05-28 cycle check (2026-05-28)
  - Self-answer: carryover explicitly states "No open items this cycle" — nothing to surface per protocol
  - Resolved: no kanban task creation needed

## Notes for Next Run

- **Conformal Decision Theory for safety**: CCO applies CDT to agentic oversight — first practical application of CDT beyond theoretical frameworks; worth monitoring for follow-up papers
- **Permutation symmetry in neural networks**: Gamma-World's parameter-free simplex encoding suggests broader applications; watch for papers on equivariant architectures for multi-agent settings
- **Evolutionary search + self-improvement**: BES's success on hard reasoning tasks where GRPO fails suggests evolutionary approaches to training data generation; connect to [[alphaevolve]] and population-based training literature
- **Backward decomposition for verification**: BES's recursive sub-goal generation provides dense feedback; cross-reference with CODESKILL's hybrid reward mechanism (both address sparse verification differently)
- **Papers worth revisiting**: LCGuard (2605.22786, multi-agent KV sharing safety) — connects to Gamma-World's multi-agent consistency; HarnessAPI (2605.22733, MCP unified endpoints) — not yet processed; OmniVerifier-M1 (2605.28805, multimodal meta-verifier) — related verification approach
- **CCO + Behavioral Credibility Trilemma**: Both address oversight of capable agents; Trilemma proves H+C+A structurally impossible; CCO provides working construction for the H+C corner — cross-reference in [[agentic-safety]]