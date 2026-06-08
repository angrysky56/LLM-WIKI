---
created: 2026-06-06
type: source
status: active
sources: https://arxiv.org/abs/2605.22738
confidence: 0.85
---

# Proxy-Based Approximation of Shapley and Banzhaf Interactions

> **Source:** arXiv:2605.22738

## Summary

This paper introduces **ProxySHAP**, a method for efficiently approximating Shapley and Banzhaf interaction indices (higher-order feature attributions) for tree ensemble models. Current estimators for higher-order interactions trade off between speed and accuracy; ProxySHAP reconciles the sample efficiency of tree-based proxy models with principled consistency via residual correction.

### Key Contributions

1. **ProxySHAP algorithm** — Uses a tree-based proxy model for fast initial approximation, then applies residual correction (Maximum Sample Reuse / MSR) to correct proxy bias without exponential variance scaling.

2. **Polynomial-time TreeSHAP extension** — Derives a polynomial-time generalization of interventional TreeSHAP that computes exact interaction indices for tree ensembles, bypassing exponential tree-depth dependencies in prior methods.

3. **Theoretical analysis** — Characterizes conditions under which MSR corrects proxy bias without variance explosion.

4. **State-of-the-art results** — Demonstrates superior approximation quality including large-scale applications with thousands of features.

## Connections

- Related to [[shapley-values]] and [[shap]] for feature attribution
- Extends [[interventional-treeshap]] to interaction indices
- Shares lineage with [[banzhaf-index]] for cooperative game theory
- Relevant to [[explainable-ai]] and model interpretability
