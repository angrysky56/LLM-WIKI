---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "FINHARNESS: An inline safety harness for finance LLM agents with three components (QUERY MONITOR, TOOL MONITOR, CASCADE) that cuts attack success rate from 38.3% to 15%"
tags: [paper, arxiv, llm-agents, finance, safety, security]
---

# FINHARNESS: An Inline Lifecycle Safety Harness for Finance LLM Agents

**Paper:** [arXiv:2605.27333](https://arxiv.org/abs/2605.27333)
**Authors:** Haoxuan Jia, Yang Liu, Bin Chong, Yingguang Yang, Yancheng Chen, Jiayu Liang, Qian Li, Hanning Lu, Kefu Xu, Chongyang Zhang, Hao Peng, Philip S. Yu

## Overview

FINHARNESS is an inline safety harness for finance LLM agents that wraps the agent end-to-end with three components to prevent prompt-induced unauthorized actions while approving legitimate business workflows.

## Three Core Components

1. **QUERY MONITOR** — Fuses single-turn intent with cross-turn drift detection
2. **TOOL MONITOR** — Evaluates each prospective tool call before execution
3. **CASCADE** — Integrates per-step risk and adaptively routes verification between lightweight and advanced-tier LLM judges

## Key Problem

- Boundary filters miss irreversible mid-trajectory tool calls
- Post-hoc LLM judges audit only after termination (too late + linear cost scaling with trace length)
- Finance agents: long plausible-looking trajectories can end in irreversible transfers or leaked KYC records

## Results

- On FINVAULT dataset: cuts ASR from **38.3% → 15.0%**
- Preserves benign approval: 41.1% → 39.3%
- Uses **4.7× fewer** advanced-judge calls than always-advanced ablation

## Tags
- llm-agents
- finance-safety
- prompt-injection
- tool-use
- cascading-verification