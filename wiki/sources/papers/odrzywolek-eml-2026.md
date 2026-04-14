---
summary: Odrzywołek (2026) — discovery of the EML operator eml(x,y)=exp(x)−ln(y), a single binary primitive generating all elementary functions from constant 1, with applications to symbolic regression via gradient-trainable binary trees
tags: [mathematics, operator-theory, symbolic-regression, sheffer-stroke, neuro-symbolic, analog-computing]
updated: 2026-04-14T08:15:09Z
created: 2026-04-14T08:15:09Z
---

# All Elementary Functions from a Single Operator

**Author:** Andrzej Odrzywołek (Jagiellonian University)
**Source:** [arXiv:2603.21852v2](https://arxiv.org/html/2603.21852v2)
**Published:** 2026

## Core Discovery

The paper establishes that a single binary operator:

$$\operatorname{eml}(x,y) = \exp(x) - \ln(y)$$

paired with the constant $1$, is sufficient to reconstruct *all* standard elementary functions — arithmetic ($+, -, \times, /$), exponentiation, roots, trigonometric/hyperbolic functions and their inverses, and constants ($e, \pi, i$). This is the continuous-domain analogue of the [[sheffer-stroke]] (NAND gate) for Boolean logic.

## Key Results

**Completeness:** Every function on a scientific calculator can be expressed as nested applications of `eml` to `1` and input variables. The grammar is trivially context-free: $S \to 1 \mid \operatorname{eml}(S,S)$.

**Concrete examples:**
- $e^x = \operatorname{eml}(x, 1)$
- $e = \operatorname{eml}(1, 1)$
- $\ln(z) = \operatorname{eml}(1, \operatorname{eml}(\operatorname{eml}(1, z), 1))$

**Reduction sequence:** The paper traces progressive calculator reduction — from 36 primitives (Table 1) through Wolfram's 7-primitive set, down through Calc 3/2/1/0 configurations, to EML's 3 primitives (operator + constant + variable). No further reduction in operator count is possible.

**Cousins:** Two related operators were also discovered:
- EDL: $\operatorname{edl}(x,y) = \exp(x)/\ln(y)$ with constant $e$
- $-\operatorname{eml}(y,x) = \ln(x) - \exp(y)$ with constant $-\infty$

**Symbolic regression:** EML trees serve as trainable circuits — parameterized binary trees where leaf weights are optimized via Adam, then "snapped" to exact binary values. At depth 2, blind recovery succeeds 100% of runs; ~25% at depths 3–4. When correct basin is found, MSE drops to machine epsilon squared ($\sim 10^{-32}$).

## Method

Discovery used systematic ablation testing with numeric bootstrapping verification. Algebraically independent transcendental constants (Euler-Mascheroni $\gamma$, Glaisher-Kinkelin $A$) were substituted for variables, and candidate expressions were evaluated numerically. Under the Schanuel conjecture, coincidental equality is vanishingly unlikely, making this a reliable sieve. Verification was done symbolically in Mathematica and numerically across C, NumPy, PyTorch, and mpmath.

## Complexity

EML representations range from depth 1 ($e^x$) to depth 8 (multiplication). The unoptimized compiler produces large RPN programs (e.g., $K=83$ for subtraction), but direct exhaustive search finds substantially shorter forms (e.g., $K=11$).

**Caveat:** Internal computations require complex arithmetic (principal branch of $\ln$) — trigonometric functions and $\pi$ are generated via Euler's formula. Works cleanly in Mathematica, NumPy, PyTorch, and IEEE754 C; requires care in pure Python/Julia and Lean 4.

## Open Questions

- Does a binary Sheffer exist that generates constants from arbitrary input (no distinguished constant needed)?
- A ternary candidate $T(x,y,z) = e^x / \ln(x) \times \ln(z) / e^y$ with $T(x,x,x) = 1$ is under investigation.
- Can a univariate Sheffer serve simultaneously as a neural activation function and elementary function generator?
- A purely real-domain continuous Sheffer appears impossible — complex intermediates seem unavoidable.

## Connections

- [[eml-operator]] — concept page with use cases and architectural implications
- [[symbolic-regression]] — gradient-based formula discovery from data
- [[sheffer-stroke]] — the Boolean logic analogue (NAND gate)
- [[mcp-logic]] — potential integration point for native continuous math in automated reasoning
- [[neo4j]] — graph structures for representing EML binary trees

## Repository

[SymbolicRegressionPackage](https://github.com/VA00/SymbolicRegressionPackage) — includes EML compiler (Python), Mathematica verification, Rust reimplementation, and training experiments.
Zenodo archive: [10.5281/zenodo.19183008](https://doi.org/10.5281/zenodo.19183008)
