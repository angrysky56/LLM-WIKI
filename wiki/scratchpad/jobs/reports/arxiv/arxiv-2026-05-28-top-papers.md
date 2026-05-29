# arXiv Daily Report — 2026-05-28

## Papers Processed

### 2605.28807 — Calibrating Conservatism for Scalable Oversight (CCO)

**Finding**: Calibrated Collective Oversight (CCO) uses Conformal Decision Theory to calibrate a conservatism penalty for agentic AI systems. Aggregates diverse overseer signals (smaller models, heuristics, uncertainty estimates) into Δ(s,a) measuring deviation from conservative baseline. The conformal controller adjusts λ online: λₜ₊₁ = λₜ + η(ℓₜ − α), ensuring long-run loss rate converges to user-specified α with finite-time bounds and no distributional assumptions. On SWE-bench: weaker overseer constrains adversarially misaligned stronger agent; on MACHIAVELLI: substantially reduces ethical violations while preserving reward. Key theorem: CCO decision family is eventually safe — beyond a conservatism threshold, agent always selects baseline action.

**Wiki path**: `wiki/sources/papers/calibrating-conservatism-scalable-oversight-2026.md`

---

### 2605.28816 — Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**Finding**: Multi-agent video world model supporting arbitrary agent counts with permutation symmetry. Two key innovations: (1) **Simplex Rotary Agent Encoding** — extends 3D RoPE by placing agents at simplex vertices in rotary angle space; parameter-free, permutation-symmetric, generalizes from 2 to 4 players without retraining. (2) **Sparse Hub Attention** — learnable hub tokens mediate cross-agent communication; reduces attention cost from O(agents²) to O(agents). Distilled teacher→student with KV caching enables real-time 24-FPS interactive rollout. Solves the structural limitations of prior work (Solaris): quadratic dense attention and learned per-slot IDs that break permutation symmetry.

**Wiki path**: `wiki/sources/papers/gamma-world-multi-agent-world-modeling-2026.md`

---

### 2605.28814 — Self-Improving Language Models with Bidirectional Evolutionary Search (BES)

**Finding**: BES addresses two fundamental limitations of tree search / best-of-N: (1) sparse verification signal, (2) candidate confinement to model distribution. Forward search uses four evolution operators (combination, translocation, deletion, crossover) inspired by sexual reproduction — recombines parts of different trajectories to reach low-probability correct solutions. Backward search recursively decomposes task into checkable sub-goals, providing dense intermediate feedback. Theorems: expansion-only candidates confined to narrow entropy shell; evolution operators escape it; backward decomposition exponentially reduces required samples. On post-training tasks where GRPO/MaxRL/Tree-GRPO fail, BES consistently finds improvements; on inference benchmarks, outperforms OpenEvolve, GEPA, ShinkaEvolve.

**Wiki path**: `wiki/sources/papers/bidirectional-evolutionary-search-bes-2026.md`

---

## Cross-Paper Theme: Constraint Satisfaction Under Distribution Shift

**Unifying finding**: All three papers address agents operating under constraints where naive optimization fails — either because the agent's distribution doesn't contain good solutions (BES), because the agent may be misaligned (CCO), or because multiple agents must maintain consistency without centralized coordination (Gamma-World).

| System | Constraint Type | Mechanism |
|--------|----------------|-----------|
| CCO | Oversight constraint (weaker supervising stronger) | Calibrated conservatism penalty with conformal adjustment |
| Gamma-World | Permutation symmetry + real-time compute | Simplex encoding + sparse hub attention |
| BES | Verification signal sparsity + distribution confinement | Evolution operators + backward goal decomposition |

**Design principle**: When your optimization target (utility, generation quality, consistency) can fail due to factors outside the agent's control (misalignment, multi-agent interference, distribution mismatch), the solution is not more optimization — it's constraint-aware optimization that relaxes under safety and tightens under risk.

---

## Next Cycle Search Direction

- **Evolutionary recombination for LLM training data**: BES's success with crossover/combination operators suggests papers on population-based training for LLMs, genetic algorithm approaches to training data curation
- **Conformal methods for AI safety**: CCO's CDT application is novel; papers on conformal prediction for LLM calibration, tail-risk control in agentic systems
- **Permutation-symmetric architectures**: Gamma-World's simplex encoding is parameter-free; papers on symmetric neural networks, equivariant architectures for multi-agent systems
- **Backward decomposition for verification**: BES's recursive sub-goal generation; papers on step-wise verification, compositional correctness for LLMs
- **Papers worth revisiting**: HarnessAPI (2605.22733, MCP unified endpoints) — not yet processed; LCGuard (2605.22786, multi-agent KV sharing safety) — safety in multi-agent communication; OmniVerifier-M1 (2605.28805, multimodal meta-verification) — related to CCO's verification approach

---

## Related
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-28-top-papers]]
- [[wiki/index]]

## Deliverables

| Type | Path |
|------|------|
| CCO source page | `wiki/sources/papers/calibrating-conservatism-scalable-oversight-2026.md` |
| Gamma-World source page | `wiki/sources/papers/gamma-world-multi-agent-world-modeling-2026.md` |
| BES source page | `wiki/sources/papers/bidirectional-evolutionary-search-bes-2026.md` |
| This report | `wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-05-28-top-papers.md` |