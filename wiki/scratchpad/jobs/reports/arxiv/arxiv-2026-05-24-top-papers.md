---
created: 2026-05-24
updated: 2026-06-27
type: report
summary: arxiv daily report — Proxy-Based Approximation of Shapley and Banzhaf Interactions
tags: [arxiv, report]
---

# arxiv Report — 2026-05-24

## Papers Processed

### 1. *Proxy-Based Approximation of Shapley and Banzhaf Interactions* (arxiv:2605.22738)
- **Why selected**: Connects to EFHF's verification threads — ProxySHAP achieves polynomial-time exact interaction indices by exploiting tree ensemble structure, paralleling how EFHF exploits layer structure for tractable verification. MSR residual correction is a general schema for proxy-to-exact recovery.
- **Status**: ingested → wiki/sources/papers/proxy-based-shapley-banzhaf-2026.md
- **Wiki connections**: efhf, verifier-graph, maximum-occupancy-principle, mop-explorer

### 2. *Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety* (arxiv:2605.22643)
- **Why selected**: Directly quantifies the incremental harm failure mode that EFHF's conscience-servitor layer is designed to address. Shows 44.4% aggregate ASR with multi-turn stateful attacks — confirming that pre-response ethical review must track cumulative state, not just individual outputs.
- **Status**: ingested → wiki/sources/papers/boiling-frog-agentic-safety-2026.md
- **Wiki connections**: efhf, agentic-research, verifier-graph, sheaf-consistency-enforcer

### 3. *Forecasting Scientific Progress with Artificial Intelligence* (arxiv:2605.22681)
- **Why selected**: CUSP benchmark reveals temporal reasoning as a core capability gap — models generate plausible directions but fail at feasibility prediction and timing. Consistent with agentic research "scientific taste" failure and with Futuresim findings. Key data point for the world-model limitations question.
- **Status**: ingested → wiki/sources/papers/forecasting-scientific-progress-ai-2026.md
- **Wiki connections**: agentic-research, efhf, futuresim-adaptive-agents, verifier-graph

## Wiki Updates
- New pages: 3 (proxy-based-shapley-banzhaf-2026.md, boiling-frog-agentic-safety-2026.md, forecasting-scientific-progress-ai-2026.md)
- Tags added: paper, arxiv, shapley-values, agentic-safety, benchmark, scientific-ai, forecasting

## Notes
- **Common theme**: All three papers address **verification and trust** at different levels:
  - ProxySHAP: verifying feature-level attribution (game-theoretic verification)
  - Boiling the Frog: verifying agentic state transitions (multi-turn safety verification)
  - CUSP: verifying scientific forecasting reliability (temporal prediction verification)
- This continues and deepens the **scaffolding/verification/boundedness** theme from prior batches
- **arXiv API**: behaved normally; no rate limiting events
- **PDF storage**: 3 PDFs downloaded to /home/ty/Documents/paper-research/
- **Carryover theme update**: The scaffolding→verification thread is now three batches deep. The convergence point is that verification mechanisms (formal, statistical, state-based) are increasingly tractable, but world-model limitations (temporal reasoning, cumulative state tracking, overconfidence) remain fundamental gaps. Next batch should explore papers on world-model improvement or self-calibration.

## Related
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-24-top-papers]]
- [[wiki/index]]

- [[arxiv-2026-05-24-top-papers]]

## Papers Worth Revisiting
- HarnessAPI (2605.22733): MCP tool registration unified with HTTP endpoints — relevant to EFHF MCP configuration. Not selected this cycle due to lower novelty vs. the verification theme but still worth a quick pass.
- LCGuard (2605.22786): Latent Communication Guard for Safe KV Sharing in Multi-Agent — relevant to verifier-graph and multi-agent EFHF communication. Could connect to Boiling the Frog's multi-agent safety findings.