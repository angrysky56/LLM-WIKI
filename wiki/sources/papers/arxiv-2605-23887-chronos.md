---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "CHRONOS: Temporal-aware multi-agent coordination for data marketplaces with three layers addressing stale index shortcuts, Shapley pricing under distribution shift, and DP budget coordination"
tags: [paper, arxiv, multi-agent, temporal-knowledge-graphs, privacy, data-marketplace]
---

# CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces

**Paper:** [arXiv:2605.23887](https://arxiv.org/abs/2605.23887)
**Author:** Joydeep Chandra (BNRIST, Tsinghua University)

## Overview

CHRONOS addresses three coupled failures in temporal knowledge-graph (KG) data marketplaces with static designs:

1. **Stale hybrid index shortcuts** reduce recall as edges evolve
2. **Stationary Shapley pricing** misattributes value after distribution shifts
3. **Uncoordinated agents** over-consume shared differential-privacy (DP) budget

## Three-Layer Architecture

### Layer 1: T-LEGEND (Indexing)
- Applies neural-ODE temporal decay to shortcut edges
- Per-query expected recall-loss bound: O(PqλΔt)
- ODE-certified monotone-envelope guarantee reducing bound looseness to 1.8–3.2× observed loss

### Layer 2: Event-Conditioned MPV (Valuation)
- Conditions Shapley valuation on BOCPD-detected changepoints
- Finite-sample error guarantees under coalition sampling and DP noise

### Layer 3: Temporal Coordinator (Scheduling)
- Uses EXP3-IX over three scheduling actions
- Achieves O(√T log T) regret
- Enforces (εtotal, δtotal)-DP via moments accounting

## Results

- **0.937 recall@10**
- **2.74 queries/s**
- **P50 latency: 161 ms**
- Total ε=4.25 at δ=10⁻⁶ under standard zCDP composition
- Scales to 500 sellers

## Tags
- temporal-knowledge-graphs
- multi-agent-systems
- differential-privacy
- shapley-valuation
- data-marketplaces
- neural-ode