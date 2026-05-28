---
created: 2026-05-27
updated: 2026-05-27
type: source
summary: "CUA-GYM: agentic pipeline for scalable RLVR training data synthesis for computer-use agents — 32K verified tuples, 110 environments, Qwen3.5-A3B reaches 62.1% OSWorld-Verified"
tags: [rlvr, computer-use-agents, data-synthesis, reinforcement-learning, agentic-ai]
sources: https://arxiv.org/abs/2605.25624
status: active
confidence: high
---

# CUA-GYM: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents

**arXiv:** 2605.25624v1 | **Date:** 2026-05-25 | **Categories:** cs.AI, cs.LG

## Metadata

| Field | Value |
|-------|-------|
| Authors | Bowen Wang, Dunjie Lu, Junli Wang, Tianyi Bai, Shixuan Liu, Zhipeng Zhang, Haiquan Wang, Hao Hu, Tianbao Xie, Shuai Bai, Dayiheng Liu, Que Shen, Junyang Lin, Tao Yu |
| Institution | The University of Hong Kong, Qwen Team (Alibaba), UC San Diego, Tsinghua |
| Dataset | https://huggingface.co/datasets/xlangai/CUA-Gym |
| Code | https://github.com/xlang-ai/CUA-Gym |

## Executive Summary

CUA-GYM solves the RLVR data bottleneck for computer-use agents (CUAs) through an agentic co-generation pipeline that jointly synthesizes task instructions, executable environment states, and verifiable reward functions from a shared topic specification. Three adversarially coupled agents (Generator, Discriminator, Orchestrator) iterate until reward functions distinguish initial from golden states under execution. A final filter combines LLM majority voting and teacher-model rollouts. The pipeline produces 32,112 verified RLVR training tuples across 110 environments (16 real desktop apps, 94 synthesized mock web apps). GSPO-trained Qwen3.5-35B-A3B achieves 62.1% on OSWorld-Verified; the 397B-A17B variant reaches 72.6%. Environment diversity is identified as an independent scaling axis orthogonal to data volume.

## Technical Approach

**Problem:** CUA RLVR requires tuple (t, s, r) — task instruction, executable environment state, reward function. Hand-authoring one tuple takes hours of expert effort. Existing datasets either have high reward fidelity but narrow coverage (hand-curated benchmarks) or broad scale but unreliable verification (LLM-as-judge).

**Solution — Co-generation pipeline:**
1. **Generator agent** writes `initial_setup.py` and `golden_patch.py` to construct paired initial and golden environment states
2. **Discriminator agent** (information-isolated from Generator) writes `reward.py` from task description alone — cannot see Generator's setup scripts
3. **Orchestrator agent** drives iterative rounds until reward function executes and distinguishes the two states
4. **Filter:** LLM majority voting + teacher-model rollouts remove tuples that pass per-task verification but fail under realistic agent behavior

**Environment scaling via CUA-GYM-HUB:** Agentic synthesis pipeline creates self-contained mock web applications from real-world software-use distributions (O*NET occupational taxonomy, Anthropic Economic Index). Each mock supports thousands of distinct tasks.

**Training:** GSPO (Group Relative Policy Optimization) on Qwen3.5 MoE backbones.

**Key architectural insight:** Information barrier between Generator and Discriminator prevents reward hacking — reward must measure task completion, not reconstruction of setup procedure.

## Key Results

- CUA-GYM-A3B (35B): 62.1% on OSWorld-Verified — matches untrained A17B base at ~10× fewer parameters
- CUA-GYM-A17B (397B): 72.6% on OSWorld-Verified — new SOTA for open-source CUAs at scale
- Data scaling: smooth improvement with volume
- Environment diversity scaling: expanding from 10→80 environments yields gains that trajectory volume alone cannot recover
- RL training spontaneously induces multi-action tool calls, compressing trajectories by 33–45%
- Cross-platform transfer: trained checkpoints improve on held-out WebArena (real browser benchmark)

## Wiki Connections

- [[efhf]] — Externalized hypothesis formation via skill documents; CUA-GYM shows environment state is trainable external state with verification gating
- [[agentic-research]] — CUA-GYM is itself an agentic pipeline; the Generator/Discriminator/Orchestrator triad mirrors multi-agent research council
- [[mop-explorer]] — Environment diversity as independent scaling axis parallels capacity planning in bounded representations
- [[verifier-graph]] — Discriminator as isolated reward writer parallels verifier as independent checking authority
- [[bounded-representation-capacity]] — CUA RLVR data has finite verifiable capacity; environment diversity is a capacity axis distinct from data volume

## Related
- [[index]]
- [[sources/papers/cua-gym]]

- [[cua-gym]]

## Key Quotes

> "Performance scales smoothly with both data volume and environment pool size, and expanding the environment pool from 10 to 80 environments yields gains that trajectory volume alone cannot recover, identifying environment diversity as a scaling axis complementary to data volume."

> "RL training spontaneously induces multi-action tool calls, compressing trajectories by 33–45% at matched task performance, an emergent efficiency behavior that parallels the spontaneous emergence of verification and self-reflection observed in reasoning-focused RL."

> "The bottleneck is structural rather than algorithmic. Unlike math or code, where a training instance reduces to a problem statement and a checkable answer, a CUA RLVR instance is a tuple (t, s, r) of task instruction, executable environment state, and reward function, with each component a non-trivial engineering artifact that must work together with the others."