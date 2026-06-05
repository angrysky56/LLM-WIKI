---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: ProxySHAP — polynomial-time Shapley/Banzhaf interaction estimation via tree-based proxy models with residual correction, setting new SOTA for explainability
tags: [paper, arxiv, shapley, banzhaf, explainability, feature-attribution, data-valuation, proxy-model]
sources: https://arxiv.org/abs/2605.22738
status: active
confidence: 0.85
---

# Proxy-Based Approximation of Shapley and Banzhaf Interactions

**Paper:** Proxy-Based Approximation of Shapley and Banzhaf Interactions  
**arXiv:** [2605.22738](https://arxiv.org/abs/2605.22738)  
**Authors:** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, Eyke Hüllermeier, Maximilian Muschalik, Fabian Fumagalli  
**Date:** 2026-05-21  
**Categories:** cs.LG, cs.AI, stat.ML

## Executive Summary

Shapley values and Banzhaf values from cooperative game theory are the standard framework for attributing credit to features or data points in ML models. However, computing exact interaction indices scales exponentially with the number of features. ProxySHAP introduces a polynomial-time generalization of interventional TreeSHAP that bypasses the exponential tree-depth dependencies of prior methods, combined with a residual correction strategy (Maximum Sample Reuse) that corrects proxy bias without exponential variance scaling. Benchmarking shows ProxySHAP achieves the lowest error across both small- and large-budget regimes, outperforming ProxySPEX and KernelSHAP-IQ.

## Technical Approach

### Problem: Exponential Scaling of Interaction Estimation

Computing exact Shapley or Banzhaf interaction indices requires evaluating the value function ν over all subsets of features — 2^n subsets for n features. Prior tree-based methods (TreeSHAP) had exponential dependencies on tree depth. Existing proxy-based estimators (ProxySPEX, KernelSHAP-IQ) traded speed against accuracy but had no principled path to exactness.

### Key Innovation: ProxySHAP

1. **Tree-based proxy model**: Train a surrogate tree ensemble on the value function that can be evaluated cheaply.
2. **Polynomial-time exact computation**: Derive a generalization of interventional TreeSHAP to compute exact interaction indices for the proxy tree ensemble in polynomial time (in number of features), bypassing the exponential tree-depth dependency.
3. **Residual correction via Maximum Sample Reuse (MSR)**: The proxy introduces bias; MSR corrects this by reusing samples in a principled residual adjustment step. The paper formally characterizes when MSR converges without exponential variance scaling.

### Theoretical Results

- Polynomial-time exact interaction indices for tree ensembles (no exponential depth dependency)
- Characterization of MSR convergence conditions: variance does NOT scale exponentially with interaction size under specific regularity conditions
- Extension to Banzhaf interactions in addition to Shapley interactions

## Key Results

- ProxySHAP achieves lowest error in both small-budget and large-budget regimes
- Outperforms ProxySPEX and KernelSHAP-IQ on approximation quality
- Scales to thousands of features
- Strong performance on downstream explainability tasks (feature attribution, data valuation)
- Demonstrated on token attribution for vision-language models (SigLIP-2 with ProxySHAP outperforms baseline Shapley values on token interaction estimation)

## Relevance to Wiki Research Threads

ProxySHAP connects to several active EFHF research threads:

- **[[verifier-graph]]**: ProxySHAP is itself a verification mechanism — it provides a principled, computationally tractable way to verify feature-level attribution in ML models. The interaction indices can be seen as verifying which components of a model's reasoning contribute to its output.
- **[[entities/projects/efhf]]**: The sheaf-consistency enforcement and layer boundary verification work relates to ProxySHAP's contribution of polynomial-time verification of interaction structure. Verifying cross-layer attribution in EFHF is analogous to verifying feature interactions in a model.
- **[[concepts/maximum-occupancy-principle]]**: MOP's resource allocation at layer boundaries may benefit from interaction analysis — knowing which features/interactions dominate resource usage is directly applicable.
- **[[mop-explorer]]**: The interaction quantification that ProxySHAP enables could feed into MOP's occupancy and resource allocation models.

## Key Quotes

> "Shapley values and Banzhaf values, fundamental instances of cardinal-probabilistic values, provide a rigorous axiomatic framework for attribution. These concepts are ubiquitous in modern machine learning, serving as the cornerstone for tasks such as feature attribution and data valuation."

> "We introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction."

> "By achieving the lowest error in both small- and large-budget regimes, ProxySHAP significantly outperforms the prior best estimators ProxySPEX and KernelSHAP-IQ."

## Structural Insights

1. **The proxy pattern is general**: Using a tractable surrogate to verify properties of an intractable system is a pattern that appears across formal verification, EFHF's layer verification, and agent scaffolding. ProxySHAP demonstrates this works for game-theoretic attribution.

2. **Exactness via polynomial-time approximation is possible when structure is exploited**: By exploiting the structure of tree ensembles (not just any function), ProxySHAP achieves what was thought to require exponential computation. This parallels how EFHF exploits layer structure to achieve verification that would be intractable on arbitrary computation graphs.

3. **Residual correction as a general schema**: MSR's approach — train a proxy, correct its bias with residual adjustment — is a general pattern applicable beyond Shapley estimation to any system where an approximate model is corrected against ground truth.

## Connections
- [[sources/papers/proxy-based-shapley-banzhaf-2026]]
- [[wiki/index]]
- [[scratchpad/jobs/reports/arxiv/papers-2026-05-24-researched]]
- [[proxy-based-shapley-banzhaf-2026]]

- [[shapley-values]] — core concept
- [[verifier-graph]] — verification mechanism parallels
- [[entities/projects/efhf]] — layer verification connection
- [[concepts/maximum-occupancy-principle]] — resource allocation interaction