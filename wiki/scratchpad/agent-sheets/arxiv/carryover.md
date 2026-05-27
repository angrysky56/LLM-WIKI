---
created: 2026-05-26T00:00:00Z
updated: 2026-05-27T14:45:00Z
type: report
summary: "arxiv agent carryover — 2026-05-27 batch: MATCHA (evaluation metrics), FinHarness (inline agent safety), Interaction SSD (annotation moderation) — evaluation infrastructure & instance-level signal decomposition theme"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

|||||| Date | Result | Notes ||
|------|--------|-------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme ||
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted ||
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer ||
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme ||
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme ||
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity ||
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition ||
| **2026-05-27** | **3 papers ingested** | **MATCHA, FinHarness, Interaction SSD — evaluation infrastructure & instance-level signal decomposition** ||
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |  |

## Current State

- **arXiv**: 2026-05-27 batch fully processed — 3 papers ingested, 6 papers examined
- **arXiv API**: Hit rate limit on API queries; worked around by using wiki_fetch_url on arxiv.org/abs/ pages + PDF extraction via PyMuPDF
- **Wiki paper inventory**: ~339 pages (added matcha, finharness, semantic-gradients-interactions-ssd)
- **Note**: arXiv API remains heavily rate-limited; wiki_fetch_url workaround effective but slower

## Papers Ingested (2026-05-27 batch)

|||||| Paper | arXiv ID | Key Finding | Wiki Connection ||
|-------|----------|-------------|------------------|
| MATCHA | 2605.27345 | Dual-view contrastive metric: rewards proximity to gold text + penalizes counterfactual contradiction distance; +18.38% over ROUGE-L, +20.82% over BERTScore on TruthfulQA | Connects to [[llm-evaluation]], [[bert-score]], [[semantic-similarity]], [[contradiction-detection]] |
| FinHarness | 2605.27333 | Inline safety harness: Query Monitor + Tool Monitor + Cascade Module; ASR 38.3% → 15.0%, 4.7× fewer advanced-judge calls | Connects to [[llm-agents]], [[inline-monitoring]], [[agentic-safety]], [[cascade-routing]] |
| Interaction SSD | 2605.27322 | Extends supervised semantic differential with interaction term for moderation analysis; annotator racial identity moderates hate-speech judgment semantics | Connects to [[semantic-differential]], [[annotation-bias]], [[moderation-analysis]] |

## Cross-Paper Theme: Evaluation Infrastructure & Instance-Level Signal Decomposition

**The unifying finding**: All papers deal with evaluation infrastructure — whether for LLMs (metrics, safety harnesses) or annotation methodology (moderation effects). Instance-level decomposition of signals continues as the dominant pattern.

| System | Decomposition Unit | Signal | Key Mechanism |
|--------|-------------------|--------|---------------|
| MATCHA | Evaluation instance (correct vs incorrect) | Contrastive signal | Dual-view: proximity + counterfactual distance |
| FinHarness | Trajectory step (per-step risk cumulant) | Inline safety evidence | Cascade routing with bounded recall |
| Interaction SSD | Semantic gradient (moderated) | Interaction term | Back-projected conditional gradients |
| Real Images | Lexical judgment (concrete vs abstract) | Visual evidence calibration | Probing + canonical correlation analysis |
| Chartographer | Chart-question-answer tuple | Counterfactual variation | Reverse-engineer → execute → derive answers |

**Design principle**: Instance-level decomposition of evaluation signals — whether evaluating correctness, safety, or semantic meaning — enables routing correct signals where coarse granularity would fail.

## Notable Mentions (Same Batch)

- **Real Images, Worse Judgments** (2605.27315): VLMs perform worse with real-image context when visual evidence is least relevant; probing reveals spurious visual cue sensitivity
- **Chartographer** (2605.27311): Counterfactual chart generation for VLM evaluation; reveals failures hidden by single-chart performance; same first author as Real Images
- **When Does Demographic Information Help?** (2605.27313): Demographics help only in specific data regimes; gated demographic residual model

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-27 batch
  - No open items this cycle — processed papers with no remaining open questions

## Notes for Next Run

- **arXiv API rate limit**: Continue using wiki_fetch_url workaround; consider batching via arxiv.org/list pages for broader coverage when API is unavailable
- **Counterfactual evaluation**: MATCHA + Chartographer both use counterfactual generation as evaluation technique — worth a synthesis note on counterfactual evaluation methodology
- **Inline vs post-hoc safety**: FinHarness + Boiling the Frog both argue for inline positioning; cross-reference these in [[agentic-safety]]
- **Semantic moderation**: Interaction SSD + Demographic Information paper (2605.27313) both examine annotator identity moderation — connect in [[annotation-bias]]
- **VLM evaluation**: Real Images + Chartographer = Yifan Jiang's two-paper arc on VLM evaluation; worth a synthesis note
- **Papers worth revisiting**: LCGuard (2605.22786, multi-agent KV sharing safety), HarnessAPI (2605.22733, MCP+HTTP unified endpoints)
- **SAE for alignment**: Prior cycle's Alignment Tampering + SAERL suggest SAE features could probe alignment-relevant model internals — bookmark for future cross-synthesis