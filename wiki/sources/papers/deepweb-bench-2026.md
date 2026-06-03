
---
created: 2026-05-21T16:51:00Z
updated: 2026-05-21T16:51:00Z
type: source
summary: "DeepWeb-Bench: deep research benchmark where derivation/calibration failures (70%+) dominate over retrieval failures (12-14%); cross-model agreement rho=0.61"
tags: [paper, benchmark, deep-research, agentic-AI, evaluation, cs-AI]
sources: https://arxiv.org/abs/2605.21482
status: active
confidence: high
---

# DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation

**Authors**: Sixiong Xie, Zhuofan Shi, Haiyang Shen, et al.

## Core Insight

Frontier deep research products score high on existing benchmarks, making capability differentiation impossible. DeepWeb-Bench is designed to be **substantially harder** than current frontier — difficulty comes from three properties: each task requires **(1) massive evidence collection, (2) cross-source reconciliation, and (3) long-horizon multi-step derivation**. Four capability families: Retrieval, Derivation, Reasoning, Calibration.

## Key Findings

| Finding | Detail |
|---------|--------|
| Retrieval is NOT the bottleneck | Retrieval failures account for only 12–14% of errors |
| Derivation + calibration dominate | >70% of errors come from derivation failures and calibration failures |
| Strong vs weak models fail differently | Strong models: incomplete derivation. Weak models: hallucinated precision |
| Cross-model agreement is low | rho = 0.61; per-case disagreement reaches 18.8 percentage points |
| Models exhibit genuine domain specialization | No single model dominates across all capability families |

## Benchmark Design

- Every reference answer has a **source-provenance record** with four disclosure levels
- Cross-source checks where available — scores auditable against underlying evidence
- Three difficulty axes: evidence volume × source multiplicity × derivation depth
- Nine frontier models evaluated; public release includes data, rubrics, evaluation code

## Why This Matters

1. **Hallucination is not primarily a retrieval problem** — the field has focused on RAG/retrieval as the hallucination fix; this shows derivation and calibration are far larger sources of error
2. **Calibration failures** — models fail to correctly estimate their own confidence/accuracy on derived conclusions; this maps onto the [[absence-of-worst-case-metric]] problem: they don't know what they got wrong
3. **Cross-model specialization** — rho=0.61 means models are not interchangeable; they have distinct capability profiles that benchmark averaging obscures
4. **Agentic research connection** — deep research is the primary use case for agentic AI; this benchmark isolates exactly where current agents fail (derivation, not retrieval)

## Connections
- [[sources/papers/deepweb-bench-2026]]
- [[wiki/index]]
- [[deepweb-bench-2026]]

- [[agentic-research]] — DeepWeb-Bench is the evaluation substrate for autonomous research agents
- [[graphrag]] — graph traversal helps with cross-source reconciliation but not derivation depth
- [[futuresim-adaptive-agents]] — FutureSim showed best frontier agents only 25% accurate on temporal world modeling; DeepWeb-Bench reveals where that failure comes from (derivation, not retrieval)
- [[spin-vs-substrate]] — calibration failure is a spin-vs-substrate problem: the model reports one thing but the operational performance (derived answer accuracy) is something else
- [[autosci-memory-centric-research-lifecycle]] — AutoSci's SciFlow harness addresses derivation failures via structured state/context/verification guarantees; SciMem's Trust Guard addresses calibration failures with independent content validation

## Caveats

- Work in Progress (27 pages, 10 figures, 4 tables per arXiv comment)
- Benchmark difficulty may favor models with specific training backgrounds; cross-domain generalization needs scrutiny
