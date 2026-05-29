---
summary: 3 papers from 2026-05-21 batch: VPO (diversity RL for test-time search), DeltaDirect (directional motion blindness fix), Recuriosity (persistent 3D world model for exploration)
tags: [arxiv, daily-report]
updated: 2026-05-23T14:30:00Z
created: 2026-05-23T14:30:00Z
---

# arxiv Report — 2026-05-23

## Papers Processed

3 papers selected from the 2026-05-21 arXiv batch, processed via MCP search + curl PDF download + parallel subagent research. All PDFs downloaded successfully (200 status each).

| # | Paper | arXiv ID | Primary Category | Core Finding |
|---|-------|----------|------------------|--------------|
| 1 | **Vector Policy Optimization (VPO)** | 2605.22817 | cs.LG | Replaces GRPO's scalar reward collapse with vector-valued + stochastic scalarization → diverse candidate pools that unlock evolutionary test-time search |
| 2 | **DeltaDirect** | 2605.22823 | cs.CV | Directional motion blindness in Video-LLMs is a readout binding failure; projector-level auxiliary objective fixes magnitude deficit for +59.5pp accuracy |
| 3 | **Recuriosity** | 2605.22814 | cs.LG | Curiosity-driven 3D exploration fails without persistent world model; online 3DGS + episodic RGB transformer solves local-loop collapse and generalizes zero-shot |

## Theme: Test-Time Computation and Persistent State as Bottlenecks

This batch converges on two related themes: **what search/processing does at test time**, and **what internal state mechanisms models need to support it**. Both VPO and Recuriosity diagnose a failure that occurs at evaluation time due to missing structure in the model's learned representations — scalar collapse in VPO's case, amnesiac world models in Recuriosity's. DeltaDirect is superficially about video perception, but the structural diagnosis (signal present but not bound to correct output) echoes the same pattern as VPO: the bottleneck is readout binding, not representation quality.

These papers collectively say: **frontier capabilities depend on internal scaffolding** — diversity-preserving output distributions, persistent world models, correct readout binding — that can't be fixed by scaling alone.

## Paper Summaries

### 1. VPO: Vector Policy Optimization (2605.22817)

**Problem**: Standard LLM post-training optimizes a single scalar reward → policy collapses to a narrow high-probability mode → candidate pools become near-duplicates → test-time search (best@k, AlphaEvolve) can't extract value from additional samples. GRPO models literally cannot solve certain evolutionary search problems at any candidate budget.

**Key insight**: Real-world rewards are naturally vector-valued (per-test-case correctness, multi-criterion ratings, per-hop scores). VPO exploits this by replacing fixed-weight scalarization `w* · r` with **stochastic scalarization via Dirichlet sampling**. The set-level reward = `E_w[max_{y∈S} w·r(x,y)]` — this rewards the model for spanning the Pareto frontier across diverse reward trade-offs rather than collapsing to a single point.

**Architecture**:
- **Multi-answer chains**: model generates m candidates in a single autoregressive rollout with delimiter tokens, each attending to prior candidates — in-context exploration
- **Stochastic scalarization**: Dirichlet-sampled weightings instead of fixed weights; gradient through max ensures each candidate specializes to a different region of reward space
- GRPO advantage estimator replaced at both the candidate-generation and advantage-computation steps

**Results**: On LiveCodeBench, VPO matches or beats GRPO on pass@k/best@k across 4 tasks; the gap widens with search budget. Critically, VPO unlocks evolutionary search problems that GRPO cannot solve at any candidate count. For code generation AlphaEvolve-style search, VPO models find solutions GRPO models completely miss.

**Wiki connections:** [[agentic-research]], [[efhf]], [[maximum-occupancy-principle]], [[verifier-graph]]

### 2. DeltaDirect: Directional Motion Blindness in Video-LLMs (2605.22823)

**Problem**: Video-LLMs — including GPT-4o (43.3%) and Gemini 2.5 Flash (53.5%) — perform near chance on signed motion direction (left/right/up/down) despite near-perfect appearance recognition. Accuracy ~25% even on single-object videos.

**Root cause — the direction binding gap**: Motion direction is linearly decodable at 99.8% from vision encoder states, 96.5% from projector, 98.1% from LLM hidden states, 95.3% from final readout token. The signal is all there; it just fails to bind to the correct verbal answer option. Probing accuracy >> QA accuracy = binding gap.

**Key structural insight**: OOD generalization failure (synthetic → real) is a **magnitude deficit**, not a geometry loss. After instruction tuning, concept vectors maintain good cosine similarity across domains — geometry is preserved — but their magnitude collapses. Restoring magnitude recovers performance.

**DeltaDirect fix**: Training-only projector-level auxiliary objective predicting normalized 2D motion vectors from adjacent-frame feature deltas. Auxiliary head discarded at inference — zero test-time overhead. MoDirect dataset family for instruction tuning and evaluation.

**Results**: 25.9% → 85.4% on MoDirect-SynBench; +21.9pp zero-shot on real-world video without real-world training data; no degradation on standard video understanding benchmarks.

**Wiki connections:** [[agentic-research]], [[efhf]], [[verifier-graph]], [[sheaf-consistency-enforcer]]

### 3. Recuriosity: Episodic Context and Persistent Worlds for 3D Exploration (2605.22814)

**Problem**: Curiosity-driven RL fails in photorealistic 3D environments because agents become trapped in local loops — they receive fresh novelty rewards for revisited areas that are actually known-confirmed. This is the **amnesiac exploration failure**: forward model has no spatial persistence, so revisiting produces spurious false-positive novelty signals.

**Key insight**: Effective curiosity requires both (1) a **persistent world model** — continuously updated reconstruction that can distinguish "actually novel" from "already-seen-but-rendered-differently" — and (2) an **episodic trajectory history** that lets the agent plan toward novel regions even when they require traversing already-visited areas to reach.

**Architecture**:
- **Persistent 3DGS forward model**: online 3D Gaussian Splatting initialized from each RGB-D frame, rendered from any query pose via differentiable rasterization. Curiosity reward = discrepancy between rendered and observed RGB.
- **Episodic RGB transformer policy**: sequence model over full RGB observation history. Maintains episodic context to enable backtracking strategies and planning toward unexplored branches.
- **Training**: PPO + random action regularization (15% random actions to prevent loop lock-in). Curiosity reward from 3DGS renderer.

**Results**: HM3D (800 scenes): 74.94% exploration completeness vs 69.68% best baseline. Zero-shot Gibson and AI-generated worlds (World Labs). Downstream fine-tuning (apple-picking, image-goal navigation) outperforms from-scratch training in sparse-reward regimes. Both persistence ablation and episodic context ablation show necessary-but-not-sufficient contributions.

**Wiki connections:** [[agentic-research]], [[efhf]], [[mop-explorer]], [[maximum-occupancy-principle]]

## Wiki Updates

- New source pages: 3
  - `wiki/sources/papers/vector-policy-optimization-vpo-2026.md`
  - `wiki/sources/papers/deltadirect-directional-motion-blindness-video-llms-2026.md`
  - `wiki/sources/papers/recuriosity-episodic-context-3d-exploration-2026.md`
- Tags added: `vpo`, `grpo-drop-in`, `reward-diversity`, `test-time-search`, `inference-scaling`, `multi-objective-rl`, `alphaevolve`, `pass@k`, `directional-motion-blindness`, `video-llm`, `direction-binding-gap`, `projector-training`, `curiosity-driven-exploration`, `3DGS`, `world-model`, `episodic-memory`, `habitat`, `zero-shot-generalization`
- Total wiki pages: 311 (up from 308)

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-23-top-papers]]

- [[arxiv-2026-05-23-top-papers]]

## Jobs Sheet

- **Status**: complete
- **arXiv API**: MCP search succeeded (no rate limit today)
- **PDF download**: all 3 succeeded via curl (200 each)
- **Next run**: 2026-05-24 8:20AM
