---
created: 2026-06-03
updated: 2026-06-09
type: concept
summary: Evolutionary optimization algorithms using covariance matrix adaptation — black-box optimization for neural network training and architecture search
tags: [evolutionary-algorithms, optimization, black-box-optimization, cma-es, neuroevolution]
sources: https://arxiv.org/abs/1604.00772 (CMA-ES survey)
status: active
confidence: 0.85
---

# Evolutionary Strategies

**Also known as:** CMA-ES (Covariance Matrix Adaptation Evolution Strategy), Natural Evolution Strategies (NES)

## What It Is

Evolutionary strategies (ES) are a class of black-box optimization algorithms inspired by biological evolution. They maintain a population of candidate solutions, mutate them probabilistically, select the fittest, and iterate. Unlike gradient-based optimization, ES requires no gradient information — only the objective function value.

The key innovation in modern ES (particularly CMA-ES) is **covariance matrix adaptation**: the algorithm learns a second-order model of the fitness landscape, enabling efficient exploration in correlated high-dimensional spaces.

## CMA-ES: The Standard

The Covariance Matrix Adaptation Evolution Strategy (CMA-ES) is the most widely used ES algorithm for continuous optimization. It maintains:
- **Mean vector μ**: current estimate of the optimum
- **Covariance matrix C**: describes the shape of the search distribution

At each iteration:
1. Sample λ offspring from N(μ, C)
2. Evaluate fitness for each offspring
3. Update μ toward the best offspring (weighted mean)
4. Update C to increase likelihood of successful steps (natural gradient)

The covariance matrix adaptation automatically discovers correlations in the fitness landscape — if the optimum lies along a ridge, C will elongate in that direction without manual tuning.

## Why It Matters

ES is a practical alternative to gradient-based methods when:
- **No gradients available**: Reinforcement learning rewards, black-box simulations
- **Non-convex, multi-modal landscapes**: Local optima traps gradient methods; ES explores more broadly
- **Discrete or combinatorial structure**: Gradient-free handling of architecture choices

The connection to [[ml-evolution]]: ES is the primary algorithm for evolving neural network architectures and hyperparameters. RZ-NAS, LLaMA-NAS, and similar architecture search methods use ES to explore the design space efficiently.

## Natural Evolution Strategies (NES)

NES reformulates ES as gradient estimation on a parameterized distribution over solutions. The fitness gradient with respect to the distribution parameters is computed via the likelihood ratio trick:

∇_θ E_{θ}[f(x)] = E_{θ}[f(x) ∇_θ log p(x|θ)]

This allows gradient-based optimization of the search distribution itself — combining the benefits of evolution with gradient-based efficiency.

## Applications to LLM Alignment

ES has been explored as an alternative to RLHF for alignment:
- **Gradient-free alignment**: Instead of backpropagating through a reward model, directly evolve the policy toward high-reward regions
- **Avoids reward hacking**: Without a differentiable reward model, the agent cannot exploit gradient signals to artificially inflate rewards
- **Main limitation**: Sample efficiency is far lower than gradient-based methods; requires many environment interactions

The connection to [[group-relative-policy-optimization]]: GRPO can be viewed as a simplified, group-relative variant of ES where the "population" is a group of samples from the same policy.

## Connections
- [[concepts/neural-architecture-search]]
- [[concepts/swe-bench]]
- [[concepts/evolutionary-strategies]]
- [[concepts/rz-nas]]
- [[concepts/scaling-laws]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[concepts/group-relative-policy-optimization]]
- [[concepts/qes]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[concepts/essa]]
- [[concepts/ml-evolution]]
- [[wiki/index]]
- [[concepts/maximum-occupancy-principle]]
- [[concepts/parameter-efficient-fine-tuning]]
- [[concepts/collm-nas]]
- [[log]]
- [[evolutionary-strategies]]

- [[ml-evolution]] — ES is the optimization engine for neural architecture search
- [[maximum-occupancy-principle]] — MOP's path entropy maximization can be expressed as an evolutionary objective: maximize diversity of visited states
- [[group-relative-policy-optimization]] — GRPO as group-relative ES variant
- [[scaling-laws]] — ES has been used to study how architecture choices interact with model scale
- [[swe-bench]] — ES for code agent task optimization (evolving prompts or tool-use strategies)
- Concept: [[ml-evolution-benchmarking-protocol]]

- [[parameter-efficient-fine-tuning]]
- [[essa]]
- [[collm-nas]]
- [[rz-nas]]
- [[neural-architecture-search]]
- [[qes]]