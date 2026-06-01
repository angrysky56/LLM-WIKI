---
created: 2026-06-01T09:15:00Z
updated: 2026-06-01T09:15:00Z
type: synthesis
summary: "Three papers on AI agent safety, capability, and training — distributed attack defense, skill reuse as compression, and reward model routing."
tags: [AI-agents, safety-monitoring, reinforcement-learning, skill-reuse, distributed-attacks, MDL, agentic-RL]
sources:
  - arxiv:2605.31509  # ReuseRL — Skill Reuse as Compression
  - arxiv:2605.31468  # Stateful Online Monitoring (distributed agent attacks)
  - arxiv:2605.31593  # ARTEMIS distributed agent attack
---

# Agent Safety, Capability & Training — Three-Paper Synthesis

**Date:** 2026-06-01  
**Papers:** 2605.31509 · 2605.31468 · 2605.31593

---

## Paper 1: Stateful Online Monitoring Catches Distributed Agent Attacks (2605.31468)

**Authors:** Davis Brown et al. — UPenn / CMU  
**Venue:** arXiv preprint, June 2026

### Core Problem
Standard safety monitors score **one agent transcript at a time** — structurally blind to misuse that is distributed across many user accounts. Real-world attack案例 (Anthropic November 2025 disclosure): attackers used an external orchestrator to split a harmful cyber-espionage campaign into "small, seemingly innocent" defensive tasks across 30 global victims, each looking benign in isolation.

### Key Contribution — The Attack
First fully general **distributed agent attack**, built on the ARTEMIS multi-agent scaffold. A weak supervisor (gpt-oss-120b, 0% direct solve rate) orchestrates stronger subagents (gpt-5.2) that receive narrow, disguised task descriptions. Each subagent context is individually benign; together they complete the full exploit. Results:
- **Evasion:** caught only ~20% as often as prior agent attacks at modest FPR
- **Capability:** distributed attack reaches 36–40% solve rate on Cybench (vs 0% direct for weak supervisor)
- **Attack stages:** sequential decomposition attacks are caught at "obtaining access" stage; distributed attacks can complete the *entire exploit* before detection

### Key Contribution — The Defense
**Online stateful monitor** — clusters embedding-similarity across *many* user transcripts in real-time using stream clustering. Only rare suspicious clusters escalate to an LLM cross-context reasoner.

**Algorithm:**
1. Standard monitor scores incoming request `x_t` → suspiciousness score `s_t`
2. Embed `x_t` → `e_t`
3. Match to nearest cluster centroid (or open new cluster if similarity < τ_route)
4. Accumulate cross-session evidence in cluster buffer; when threshold exceeded → cross-context LM review

**Results (simulated datacenter traffic):**
- At 10× benign background: 81–87% campaign recall at 2.35–3.09% FPR (vs 75% at 2.72% for standard monitor)
- At 100× benign: 65.8% recall at 1.47% FPR (vs 55% for standard monitor at same FPR)
- Time-to-detect: stateful reduces TTD99 from 37.2 to 25.4 harmful steps at 100× background
- **Negligible latency overhead for ~99% of traffic** — only tail cases call the cross-context LLM

**Redteaming (2 months, 6 redteamers, >100K attacks):**  
Surprise finding — the defense also catches standard jailbreaks because attackers reuse attack variants across accounts. Four attack families emerged: monitor-context poisoning, sequential decomposition, distributed agent attacks, and semantic-cover jailbreaks.

---

## Paper 2: Skill Reuse as Compression in Agentic RL (2605.31509)

**Authors:** Zhikun Xu, Yu Feng, Jacob Dineen et al. — ASU / UPenn / USC  
**Venue:** arXiv:2605.31509, submitted 29 May 2026

### Core Problem
LLM agents trained with RL (GRPO) often entrench **brittle, task-specific shortcuts** — they solve training tasks but reason poorly in-distribution and collapse out-of-distribution ("reasoning collapse"). The question: what structural property distinguishes shortcuts that generalize from those that don't?

### Core Hypothesis
**Structural compressibility:** agents generalize better when their successful trajectories are built by composing a **small set of reusable abstract skill patterns**, rather than idiosyncratic one-off action sequences. Formalized via the **Minimum Description Length (MDL) principle**.

### Method — ReuseRL
1. **Skill projection:** map raw trajectories → sequence of atomic skills (deterministic rule-based verb mapping; small alphabet: 5–26 skills per environment)
2. **Dictionary extraction (E-step):** from successful batch, extract shared skill dictionary via **greedy BPE-style merging** — minimize two-part MDL cost: dictionary storage cost + average segmentation cost
3. **Segmentation cost (M-step):** per-trajectory penalty = `seg(s, C) / T` — fraction of dictionary phrases needed to cover the skill sequence. Reusable subroutines = low cost; idiosyncratic waste = high cost
4. **PAC-Bayes generalization bound** connecting empirical compressibility to expected description length on future successful trajectories

### Key Insight
**Pure round-length penalty = degenerate fixed-code segmentation cost** under a frozen singleton-only dictionary. Uniform brevity cannot distinguish sequences with equal raw length but different compositional structure.

### Results (ALFWorld, TextWorld-Cooking, Countdown-Stepwise)
- **ALFWorld IID/OOD:** 97.14% / 93.28% SC@7 (vs 96.43% / 91.79% pure-round-length; 84.29% / 79.85% vanilla GRPO)
- **TextWorld-Cooking:** 81.73% Pass@1 (vs 64.03% pure-round-length — pure round length *falls below* GRPO due to cookbook-literal shortcut)
- **Countdown-Stepwise:** 80.37% Pass@1 (vs 77.02% pure-round-length; 68.46% vanilla GRPO)
- ReuseRL consistently outperforms both vanilla GRPO and pure-round-length baseline; largest gains where uniform brevity is actively destructive

### Connections
- SkillRL and ERL can be reinterpreted as implicit, partial MDL minimizers
- Compression operates at **behavioral level** (skill sequence structure), not token/length level (unlike LAPO, Short-RL, CIB)

---

## Paper 3: ARTEMIS Distributed Agent Attack (2605.31593) — [Appears to be the attack component of paper 1]

**Core content already covered in Paper 1's summary.** The attack scaffold uses a multi-agent orchestrator that receives full task objective, delegates to subagents with narrow non-cyber framing, and combines partial results via a verifier tool.

---

## Cross-Cutting Themes

### 1. Distributed / Coordinated Agent Misuse is the Frontier Threat
Both the attack paper and the defense paper focus on the same phenomenon: **multi-account, multi-agent coordination** to hide harmful objectives. Standard per-transcript safety monitoring is structurally inadequate. The Stateful Online Monitor is the first systematic defense.

### 2. Compression as a Unifying Principle
Two very different papers both arrive at compression as a key idea:
- **ReuseRL:** MDL-based compression of skill sequences → better generalization via reusable patterns
- **Stateful Monitor:** embedding-space clustering of agent transcripts → catches distributed attacks via cross-account pattern detection

### 3. Structure Over Raw Length
Both works make the same point from different angles:
- ReuseRL: pure round-length is a degenerate fixed-code compression; structural compressibility matters more than raw brevity
- Stateful Monitor: per-transcript scores miss coordinated patterns; aggregate cross-context structure reveals attacks

### 4. Real-World Attack Sophistication
The attack is not theoretical — Anthropic disclosed a live distributed agent attack in November 2025 targeting 30 global victims with Claude Code. Academic literature was "behind" (quoted from the paper), confirming that this is not a greenfield threat model.

---

## Open Questions

1. **Scalability of stateful monitoring:** Performance degrades as benign background grows very large (100× vs 10×). How does this scale to millions of daily active users?
2. **MDL generalization beyond tabular tasks:** ReuseRL tested on ALFWorld, TextWorld-Cooking, Countdown — all have well-defined skill alphabets. How does this extend to open-ended agentic tasks where skill projection is ambiguous?
3. **ReuseRL ↔ Stateful Monitor integration?** Could segmentation cost serve as an additional signal in the stateful monitor's clustering pipeline?
4. **Redteaming gap:** The Stateful Monitor's cross-context reasoner is still an LLM — can adaptive attackers generate sufficiently diverse sub-tasks to split clusters while keeping each benign?

---

## Key References

- ARTEMIS multi-agent scaffold [Lin et al., 2025]
- GRPO training [Shao et al., 2024, DeepSeekMath]
- SkillRL, ERL (experience-augmented skill consolidation)
- Cybench [Zhang et al., 2024], BountyBench [Zhang et al., 2025]
- Anthropic November 2025 threat disclosure (distributed agent attack case study)