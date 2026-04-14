---
summary: Discovering closed-form mathematical expressions from data — approaches include genetic programming, neural-guided search, and gradient-optimized EML trees that are complete by construction
tags: [machine-learning, mathematics, symbolic-regression, formula-discovery, neuro-symbolic]
updated: 2026-04-14T08:16:05Z
created: 2026-04-14T08:16:05Z
---

# Symbolic Regression

Symbolic regression (SR) discovers closed-form mathematical expressions from numerical data, unlike standard regression which fits parameters within a fixed functional form. The goal is to find both the *structure* and *parameters* of the governing equation.

## Approaches

**Genetic programming (GP):** Evolves expression trees via mutation and crossover. Heterogeneous grammar with many operator types. Tools: PySR (SymbolicRegression.jl), AI Feynman.

**Neural-guided search:** Uses neural networks to bias the search over expression space. Deep symbolic regression uses risk-seeking policy gradients to explore.

**EML-based gradient optimization:** The [[eml-operator]] enables a fundamentally different approach — parameterized binary trees of identical nodes are optimized via standard gradient descent (Adam). Leaf weights are softmax-distributed over $\{1, x, f\}$ choices. When the underlying law is elementary, trained weights snap to exact values, yielding closed-form recovery with MSE at machine epsilon. See [[odrzywolek-eml-2026]].

## Key Advantage of EML for SR

Traditional SR searches over heterogeneous grammars ($+, -, \times, /, \sin, \cos, \exp, \ldots$) and must choose which operators to include — risking incompleteness. The EML "master formula" is **complete by construction**: a depth-$n$ binary tree contains all possible elementary formulas up to $2^n$ leaves and $5 \times 2^n - 6$ parameters. The search space is regular, uniform, and amenable to continuous optimization rather than combinatorial search.

## Current Limitations

Blind recovery success degrades with tree depth: 100% at depth 2, ~25% at depth 3–4, <1% at depth 5. Finding the correct basin of attraction from random initialization remains the core challenge. However, when the correct basin is reached (e.g., via perturbation from true weights), convergence is 100% even at depths 5–6.

## Connections

- [[eml-operator]] — the single-operator basis enabling gradient-based SR
- [[odrzywolek-eml-2026]] — source paper with training experiments
- [[alphaevolve]] — evolutionary approach to discovering mathematical structures
- [[mcp-logic]] — verification of discovered formulas
