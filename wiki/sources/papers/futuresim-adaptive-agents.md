---
summary: FutureSim replays real-world news chronologically to evaluate agent world-modelling; best frontier agent achieves only 25% accuracy, exposing severe gaps in open-ended temporal adaptation.
tags: [arxiv, cs.LG, AI agents, benchmarking, temporal reasoning, world models]
updated: 2026-05-17T18:17:45Z
---

# FutureSim: Replaying World Events to Evaluate Adaptive Agents

**arXiv:** [2605.15188](https://arxiv.org/abs/2605.15188) | **Category:** cs.LG | **Submitted:** 2026-05-14

## Core Insight

FutureSim evaluates agents in a grounded temporal simulation that replays real-world news events in chronological order — agents must forecast events before their knowledge cutoff while receiving the ground-truth timeline as context. The benchmark exposes a stark capability gap: the best frontier agent scores only 25% accuracy, and several agents perform *worse than random guessing* (negative Brier skill score). This reveals that current agents fail at open-ended temporal adaptation in the real world, not just on synthetic benchmarks.

## Key Claims

| Claim | Evidence | Implication |
|-------|----------|-------------|
| Best agent at 25% accuracy on 3-month forecast | Frontier agents on Jan–Mar 2026 events | Current agents are poor at open-ended world modelling |
| Several agents have negative Brier skill scores | Brier skill < 0 vs. no-prediction baseline | Some agents actively degrade predictions vs. ignorance |
| Clear capability separation between agents | Different Brier scores across providers | The benchmark discriminates meaningfully between systems |
| Grounded temporal simulation reveals real-world gaps | Real news articles replayed chronologically | Lab benchmarks underestimate real-world agent limitations |

## Authors

Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab

## Metadata

- **arXiv ID:** 2605.15188
- **Primary categories:** cs.LG, cs.AI, cs.CL
- **Submitted:** 2026-05-14
- **PDF:** https://arxiv.org/pdf/2605.15188

## Connections

- [[agentic-research]] — connection to open-ended temporal adaptation research
- [[llm-evaluation]] — benchmark design and evaluation methodology

## Open Questions

- Does retrieval-augmented search during simulation improve forecast accuracy?
- What memory and reasoning mechanisms would close the 25% gap?
- How does the Brier skill score evolve over longer simulation periods (6 months, 1 year)?
- Can agents learn to use the chronological replay signal to update beliefs?
