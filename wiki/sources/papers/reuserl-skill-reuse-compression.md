---
created: 2026-06-01T00:00:00Z
updated: 2026-06-01T00:00:00Z
type: source
summary: "ReuseRL grounds agentic RL in the Minimum Description Length principle — extracts a shared skill dictionary from successful trajectories and adds a segmentation-cost penalty, proving that structural compressibility (not raw brevity) drives generalization. PAC-Bayes bound on the MDL penalty."
tags: [agentic-rl, skill-discovery, compression, mdl-principle, pac-bayes, skill-dictionary, structural-compressibility, bpe-merging, reasoning-collapse, paper-2605-31509]
sources: https://arxiv.org/abs/2605.31509
status: active
confidence: high
---

# ReuseRL: Skill Reuse as Compression in Agentic RL (Xu et al., 2026)

## Definition

**ReuseRL** is a method for training LLM agents with reinforcement learning that augments the standard GRPO objective with a **structural-compressibility penalty** derived from the **Minimum Description Length (MDL)** principle. A shared skill dictionary is extracted online from successful trajectories (via greedy BPE-style merging), and the cost of segmenting a trajectory under that dictionary is added as a trajectory-level penalty — so the policy is rewarded for behaviour that **decomposes into reusable skills**, not merely for being short.

The central claim: agents generalize better when their successful trajectories are *structurally compressible* — built from a small set of reusable abstract patterns — and pure length penalties fail because they penalise necessary search and produce **collapsing** policies.

## Key Idea

- **Reasoning collapse** in agentic RL is reframed: it's not that policies form shortcuts, it's that they form *idiosyncratic* shortcuts that complete training tasks without composing into reusable skills.
- **Compact, repeated solution patterns are desirable** for generalisation. The difficulty is distinguishing reusable compression from raw brevity.
- **Structural compressibility** = degree to which successful behaviour, as a sequence of abstract skills, is built by composing a small set of reusable patterns.
- Connects to **hierarchical RL's options framework** (Sutton et al. 1999), **MDL** (Rissanen 1978; Grünwald 2007), and **BPE-based action tokenisation** (PRISE, SkillVLA).
- The pure round-length penalty is a *degenerate fixed-code* segmentation cost (Proposition 1) — it cannot tell reusable routines from wasted steps.

## Methodology

- **Skill dictionary extraction**: greedy BPE-style merging over successful trajectories — frequent sub-sequences become skill tokens.
- **E-step / M-step alternation**: E-step assigns trajectory segments to dictionary skills; M-step updates the dictionary. The pure round-length penalty emerges as the degenerate case where the dictionary is a singleton.
- **Trajectory penalty** = segmentation cost of the trajectory under the current dictionary, used as a per-trajectory regulariser on the GRPO objective.
- **Theorem 3 (PAC-Bayes bound)**: trajectory-level MDL generalisation bound. The bound shows that the dictionary learned from a sample of `m` successful trajectories generalises with a rate controlled by the dictionary's description length and `m`.
- **Proposition 4** extends the bound to the *universal* dictionary setting.

## Key Findings

Across **ALFWorld**, **TextWorld-Cooking**, and **Countdown-Stepwise**:

| Metric | GRPO | Pure Len. | SegCost (buf) | SegCost (no-buf) |
|--------|------|-----------|---------------|------------------|
| ALFWorld IID — Success length, steps | 15.3 | 8.7 | 9.3 | 8.4 |
| ALFWorld IID — Invalid % | 23.5 | 1.4 | 1.8 | 3.9 |
| ALFWorld IID — Repeat % | 40.4 | 9.4 | 14.4 | 9.9 |
| TW-Cooking — Burned failures % | 21.1 | 74.0 | 3.3 | 9.7 |
| Countdown — 0-RESET success % | 58.0 | 82.0 | 80.3 | **99.9** |
| Countdown — MUL/DIV ops % | 3.1 | 6.8 | 10.9 | 5.5 |

Critical observations:
- **Pure length penalty collapses** on TW-Cooking (74% burned failures) because it under-explores — necessary search steps are penalised uniformly.
- **SegCost without buffer** fails on Countdown's 0-RESET condition because the per-trajectory dictionary doesn't accumulate across runs.
- **SegCost with global success buffer** wins on every benchmark, validating the cross-trajectory accumulation hypothesis.
- **Unifying interpretation**: SkillRL and ERL are shown to be *implicit, partial MDL minimisers* — ReuseRL makes the compression objective explicit and isolation-clean.

## Limitations

- The result is in a *self-contained* RL loop; experience-augmented methods (SkillRL, ERL) are deliberately omitted, so the standalone impact of MDL is clean but the combination is untested.
- ALFWorld's only failure mode is timeout, so the win there is an efficiency gain rather than a robustness one.
- The bound is on successful trajectories only — doesn't address when to terminate skill extraction.

## Connections

### Wiki concepts
- [[agentic-research]] — ReuseRL is a method for training LLM-based research and decision agents
- [[reinforcement-learning]] — ReuseRL is an agentic-RL method
- [[agentic-reasoning]] — the failure mode ReuseRL targets is reasoning collapse
- [[bounded-representation-capacity]] — ReuseRL's MDL penalty is a structural regulariser on the policy's effective representation
- [[length-generalization]] — ReuseRL's compression objective is a generalization-bound regulariser
- [[compression]] — MDL penalty as a structural regulariser

### Related papers (wiki)
- [[skillopt-self-evolving-2026]] — text-space skill optimizer (complementary: optimises skill *content*, not the *use* of skills)
- [[skill-consumption-2026]] — SkillLens: full lifecycle of model-generated skills (ReuseRL's compression objective complements SkillLens's negative-transfer analysis)
- [[codeskill]] — RL-trained skill management policy (RL on the skill system itself, vs ReuseRL's compression penalty on trajectories)
- [[muse-autoskill]] — skill-level memory accumulation across tasks (ReuseRL provides a theoretical account of *why* skill accumulation helps)
- [[stepopsd]] — step-aware credit redistribution within GRPO (orthogonal improvement: credit assignment vs structural compression)
- [[akbe]] — on-policy probing of tool-use boundary (also adds structure to RL training)
- [[xu-envfactory-2026]] — synthetic MCP environments for agentic RL (the testbed layer that ReuseRL's compression penalty can ride on)
- [[arxiv-2605-27366-muse-autoskill]] — same lineage of skill-memory work
- [[ctx2skill]] — self-evolving multi-agent framework for skill discovery (complementary discovery mechanism)

### Cross-paper theme
ReuseRL extends the **2026-05-26 skill theme** (SkillOpt, SkillLens) by adding a *theoretical* anchor: structural compressibility is what makes skill accumulation generalise. The earlier papers describe *what skills are* and *how to optimise them*; ReuseRL provides the *generalisation theorem*.
