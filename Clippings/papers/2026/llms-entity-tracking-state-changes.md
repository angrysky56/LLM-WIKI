---
created: 2026-05-29
type: paper
source: arXiv
url: https://arxiv.org/abs/2605.30233
paper_id: 2605.30233
authors:
  - Zilu Tang
  - Qiao Zhao
  - Gabriel Franco
  - Derry Wijaya
  - Aaron Mueller
  - Sebastian Schuster
  - Najoung Kim
venue: ICML main conference 2026
summary: "LMs don't track entity states incrementally — they aggregate all relevant information in parallel at the final token once the query is evident. REMOVE uses a fragile global suppression tag, revealing failure modes that mechanistic analysis predicts."
---

# Do Language Models Track Entities Across State Changes?

**arXiv:** [2605.30233](https://arxiv.org/abs/2605.30233) | **PDF:** [2605.30233v1](https://arxiv.org/pdf/2605.30233v1)

Tang, Zhao, Franco, Wijaya, Mueller, Schuster, Kim — ICML 2026

## Abstract

Entity tracking (ET) — maintaining coherent entity state representations across context with natural-language state-changing operations — is a fundamental reasoning skill. Prior work studied entity binding *without* state changes. This paper investigates ET under realistic multi-operation conditions.

**Core finding:** LMs aggregate all relevant information **in parallel at the final token** once the query becomes evident. They solve a fundamentally sequential task with a non-sequential strategy.

**Operation breakdown:**
- `PUT` — direct write of entity state
- `REMOVE` — global suppression tag (fragile, predicts failure modes)
- `MOVE` — relocation between containers

**Mechanistic fix:** Nullifying the REMOVE global suppression tag partially recovers performance. Demonstrates behavioral–mechanistic synergy: behavioral failures prompt hypotheses; mechanistic insights predict missing failure modes.

## Why This Matters

The finding challenges assumptions that LMs perform incremental state tracking. The fragile global REMOVE mechanism is a specific, actionable target for mechanistic debugging and model improvement.

## Source

[[wiki/sources/papers/llms-entity-tracking-state-changes]]