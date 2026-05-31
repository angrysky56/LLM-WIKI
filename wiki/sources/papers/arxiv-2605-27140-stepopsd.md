---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "StepOPSD uses step-aware credit redistribution for agent RL, decomposing trajectories into action-centered segments and achieving top results on ALFWorld Heat (79.1%), PickTwo (95.0%)"
tags: [paper, arxiv, reinforcement-learning, llm-agents, credit-assignment, distillation]
---

# StepOPSD: Step-Aware Online Preference Distillation for Agent Reinforcement Learning

**Paper:** [arXiv:2605.27140](https://arxiv.org/abs/2605.27140)
**Authors:** Yanfei Zhang (Independent Researcher), Xu Lin (Tencent), Chenglin Wu (DeepWisdom)

## Overview

StepOPSD is a post-rollout preference self-distillation framework for multi-turn LLM agents that takes the **agent step** as the unit of credit redistribution, addressing credit-assignment mismatch in trajectory-level RL.

## Problem

- Rewards are sparse and trajectory-level
- Success often hinges on a few local decisions
- Existing OPD treats heterogeneous agent trajectories as monolithic strings rather than causal interaction units

## Method

1. Decomposes trajectories into **action-centered step segments**
2. Rescores under hindsight-enriched teacher contexts
3. Converts token-level log-probability gaps into **sign-preserving advantage shaping** with a normalized per-step credit budget
4. GRPO update with step-aware redistribution

## Results (ALFWorld + Search-Qa with Qwen3-1.7B and Qwen2.5-3B-Instruct)

- **ALFWorld Heat: 79.1%** (1st place)
- **PickTwo: 95.0%** (1st place)
- **Search-QA TriviaQA: 61.6%** (1st place)
- **HotpotQA: 40.4%** (tied-best)

## Key Insight: Two-Knob Law

- Smaller αclip acts as a broadly stabilizing **local trust region**
- Optimal global mixing strength λmix remains **task-dependent**

## Tags
- reinforcement-learning
- llm-agents
- credit-assignment
- preference-distillation
- multi-turn-agents