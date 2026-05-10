---
summary: A* heuristic search applied to market pivot graphs with forward-projected goals — Path Coherence Ratio quantifies structural efficiency; cross-validated against geometric (channel) and stochastic (√σ) goal sources
tags: [trading, indicators, graph-theory, a-star, isotropic-coordinate-system, pine-script, square-root-system]
updated: 2026-05-09T02:11:26Z
created: 2026-05-09T02:11:26Z
---

# A-Star Structural Pathfinding

Adaptation of A* heuristic search ([wiki/sources](../sources/articles/) — see raw ingestion *Graph Theory Heuristic Search Algorithm (A-Star) Applied in Trading*) into a market-structure indicator. Implemented as `astar_structural_pathfinder.pine` (ST-EP07) inside the [[square-root-system]].

## Why the naive port fails

A direct port of A* over a pivot graph — start at oldest pivot, end at newest pivot, find cheapest path — collapses into a glorified zigzag smoother. The heuristic `h(n) = distance to most-recent-pivot` carries no forward information, so the search is purely backward-looking. The first attempt (`pine-scripts/Astar.pine`) had this defect: a "Target Anchor" label that just sat on the most recent pivot, and a regime color that was effectively a path-integrated slope. Visually plausible, no actionable edge.

## The fix — forward-projected goals

A* requires three things: start, **forward** goal, and admissible heuristic. In market structure those become:

- **Start**: oldest pivot in the active graph window
- **Goal**: a synthetic node placed at `bar_index + N`, `price = projected_level` — *forward in time*
- **Heuristic h(n)**: ICS straight-line distance from any node to the goal, admissible by construction (Euclidean in σ-normalized log-price space cannot exceed any actual graph path)

Edges go forward in time only — `j_bar > curr_bar` — so the search routes through historical pivots as structural waypoints en route to the forward goal. The optimal path's cost relative to the direct heuristic is the **Path Coherence Ratio (PCR)**:

$$\text{PCR} = \frac{g^*_{\text{path}}}{h_{\text{direct}}(\text{start}, \text{goal})}$$

By admissibility, PCR ≥ 1. PCR ≈ 1 means structure has been navigating in a near-σ-straight line toward the goal — clean impulse. PCR ≫ 1 means many pivots between start and goal, lots of zigzag relative to net σ-progress — chaotic / consolidation.

## Two goal sources, cross-validated

The indicator runs A* four times per pivot update: bull/bear × channel/√σ.

**Channel goal (geometric).** Linear regression of log-price over a lookback, projected forward by `i_fwdBars`, with channel walls at ±k·stdev(residuals). Says: *"if established structure persists, price would be here."*

**√σ goal (stochastic).** `close × exp(±k·σ·√fwdBars)` — diffusion-physics extension. Says: *"by random-walk reach expectations, this is the typical envelope."*

Two derived metrics emerge from the four costs:

**Consensus PCR per direction** — `(pcr_chan + pcr_sqrt) / 2`. Both paths cheap → high-conviction direction.

**Goal Divergence** — `D = (pcr_chan − pcr_sqrt) / (pcr_chan + pcr_sqrt) ∈ [−1, +1]`. The asymmetry between geometric and stochastic difficulty:

- `D ≈ 0` — geometry and physics agree. Honest trend.
- `D > 0` — channel cost > √cost = structure *lagging* physics = **compression** = stored energy
- `D < 0` — channel cost < √cost = structure *ahead of* physics = **overextension** = mean-reversion risk

This frame mirrors the [[market-cognitive-dissonance]] indicator's belief-vs-reaction tension, but expressed in path-cost space — which makes it complementary, not redundant. They frequently agree; when they disagree, the disagreement itself is an interpretable signal.

## Adaptive gating — single-neuron perceptron

Pine Script is not a neural-network runtime, so "neural adaptive threshold" honestly means:

**Layer 1: online perceptron.** Six inputs `[pcr_bull, pcr_bear, |D_bull|, |D_bear|, σ-pctile, asymmetry]` rescaled to [0,1], passed through sigmoid to produce an actionability score. Weights updated each bar by gradient descent against a delayed supervisor: realized signed σ-move at +N bars confirms or refutes the prediction implied by past asymmetry. Standard logistic regression, online, transparent.

**Layer 2: Hebbian threshold drift.** Score threshold drifts toward the running centroid of scores that historically preceded confirmed signals. Self-calibrates as regime shifts.

If a real neural network is wanted, the practical architecture is Pine emits features + outcomes via webhook → Python pipeline trains offline (TimesFM is the natural fit) → learned weights bake back into Pine perceptron initial values periodically. Pine stays the runtime; Python does the training.

## Signal taxonomy

Six gated signals, all subject to cooldown:

- **IMPULSE BULL/BEAR** — low PCR + strong asymmetry → clean directional path
- **COMPRESSION BULL/BEAR** — D > threshold → energy stored, breakout candidate
- **OVEREXTENSION BULL/BEAR** — D < threshold → trend stretched beyond physics
- **CONSOLIDATION** — both PCRs high → no clean direction

## Connections

- Foundation: [[isotropic-coordinate-system|ICS]], Yang-Zhang σ — same substrate as [[square-root-system]]
- Psychological parallel: [[market-cognitive-dissonance]]
- Methodological cousin: ST-EP06 Isotropic Trend Lines (longest-monotonic-segment is a one-scale analog of pivot-graph PCR)
- Forward extension: hand learned perceptron weights to TimesFM for proper sequence-modeled gating

## Status

v1 written 2026-05-08. Pending live validation by Ty across multiple symbols/timeframes. Open questions: marker frequency calibration, whether REVERSAL CANDIDATE deserves its own signal class (currently subsumed by overextension + asymmetry sign-flip detection), and whether multi-scale consensus across pivot-validation-lookbacks {3, 7, 13} adds enough signal to justify the 3× cost.
