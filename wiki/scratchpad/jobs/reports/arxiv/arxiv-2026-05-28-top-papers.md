# arXiv Daily Report — 2026-05-28

## Papers Processed

### 2605.25920 — LegalSearch-R1: Temporal Consistency in Legal Agentic Search

**Finding**: RL-trained legal agent (7B, GRPO) with dual RAG+web architecture enforcing temporal statute indexing. Outperforms SOTA deep research agents and specialized legal LLMs by 12.9-29.8%, with 57.7-80.3% gains on temporal consistency. Core problem: legal LLMs suffer temporal bias anchored to training cutoff, and search agents rarely incorporate temporal constraints. Solution pairs local statute RAG (precise article matching with version-controlled amendment indexing) with online web search, trained on temporally-indexed data spanning multiple amendment periods. Key principle: lex retro non agit — applicable law must match temporal context of each case.

**Wiki path**: `wiki/sources/papers/legalsearch-r1.md`

---

### 2605.25739 — The Behavioral Credibility Trilemma

**Finding**: Proved fundamental impossibility in RL with confidence-gated autonomy: no agent can simultaneously maximize helpfulness (H), calibration (C), and full autonomy (A) when tasks exceed reliable competence. Root cause: any non-affine approval gate destroys strict properness of scoring rules, causing systematic confidence inflation. The principal's optimal oversight rule is necessarily non-affine — making the impossibility unconditional and optimizer-independent. Resolution pathways: commitment (principal commits to rule) or domain separation (agent operates only where competence exceeds threshold). 540-config experiment confirms all 5 pre-registered hypotheses (effect sizes d=1.10-5.32). EU AI Act Article 14 implicitly mandates H+C at cost of A.

**Wiki path**: `wiki/sources/papers/behavioral-credibility-trilemma.md`

---

### 2605.25430 — CODESKILL: Self-Evolving Skills for Coding Agents

**Finding**: RL-trained skill management policy for coding agents — learns to extract, evolve, and maintain procedural skills from trajectories rather than relying on fixed prompts or heuristics. Two granularity levels: task-level (high-level strategies) and event-driven (local guidance for recurring execution events). GRPO training with hybrid reward: sparse verifiable task feedback + dense rubric-based skill quality from LLM-as-judge. On EnvBench, SWE-Bench Verified, Terminal-Bench 2: +9.69 over no-skill, +4.01 over strongest prompt-based baselines (~33% and ~11% relative gains). Skill bank stays compact while performance scales. Key insight: static skill injection doesn't always work — skill usefulness depends on task fit, requiring adaptive management.

**Wiki path**: `wiki/sources/papers/codeskill.md`

---

## Cross-Paper Theme: Confidence Calibration Under Capacity Constraints

**Unifying finding**: All three papers deal with agents that must reason about their own reliability under capacity constraints — and each arrives at a different resolution strategy.

| System | Calibration Mechanism | Capacity Constraint | Enforcement |
|--------|----------------------|-------------------|-------------|
| LegalSearch-R1 | Temporal context identification | Statute knowledge bounded by amendment coverage | Version-controlled RAG with temporal validity windows |
| Behavioral Credibility Trilemma | Confidence-report scoring (strictly proper) | Agent competence bounded by task difficulty | Non-affine gate destroys calibration → three resolution corners |
| CODESKILL | Hybrid reward (sparse + dense) | Skill bank must stay compact | Add/merge/drop skill management policy |

**Design principle**: When an agent must reason about its own reliability, calibration is not a property you can add post-hoc — it must be architecturally enforced. LegalSearch-R1 enforces it at the retrieval level (temporal indexing); Trilemma shows it's structurally impossible to enforce simultaneously with autonomy and helpfulness; CODESKILL enforces it through adaptive skill bank management that balances density against compactness.

---

## Next Cycle Search Direction

- **Model editing / knowledge unlearning**: Trilemma's behavioral unlearning suggests papers on targeted knowledge erasure in LLMs — particularly inference-time unlearning without parameter changes (bridges with SafeCtrl-RL from last batch)
- **Temporal reasoning in LLMs**: LegalSearch-R1's temporal bias finding suggests papers on time-sensitive knowledge, statute amendment tracking, legal knowledge versioning
- **Calibrated confidence in RL agents**: Papers on proper scoring rules for RL, confidence elicitation in agentic systems, calibration-aware training signals
- **Adaptive skill management**: CODESKILL's learnable policy approach suggests papers on skill compression, skill transfer, skill bank optimization for agentic systems
- **Papers worth revisiting**: HarnessAPI (2605.22733, MCP unified endpoints) — not yet processed; LCGuard (2605.22786, multi-agent KV sharing safety) — safety in multi-agent communication

---

## Deliverables

| Type | Path |
|------|------|
| LegalSearch-R1 source page | `wiki/sources/papers/legalsearch-r1.md` |
| Behavioral Credibility Trilemma source page | `wiki/sources/papers/behavioral-credibility-trilemma.md` |
| CODESKILL source page | `wiki/sources/papers/codeskill.md` |
| This report | `wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-05-28-top-papers.md` |
| Updated carryover | `wiki/scratchpad/jobs/reports/arxiv/carryover.md` |