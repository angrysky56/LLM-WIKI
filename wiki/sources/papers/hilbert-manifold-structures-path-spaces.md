---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "Path spaces on tame two-level manifolds are Hilbert manifolds — Floer homology gains a solid analytical foundation via the tameness condition, which is closed under composition."
tags: [paper, arxiv, mathematics, symplectic-geometry, floer-theory, hilbert-manifolds, infinite-dimensional-manifolds, tameness]
related:
  - concepts/symplectic-geometry
  - concepts/infinite-dimensional-manifolds
  - concepts/attractor-dynamics
---

# Hilbert Manifold Structures on Path Spaces

**arXiv:** [2507.03782](https://arxiv.org/abs/2507.03782) | **Authors:** Urs Frauenfelder, Joa Weber (Universität Augsburg, UNICAMP) | **Date:** July 4, 2025 | **Subject:** math.SG (Symplectic Geometry)

## Overview

In Floer theory, gradient flow lines live on *two-level manifolds* — spaces like "W^{1,2} loops ∩ W^{2,2} loops" where the two regularity levels have different topological and analytical properties. This paper asks: does the space of paths between two points on such a two-level manifold itself have the structure of a Hilbert manifold?

The answer requires a new condition called **tameness**. Without it, the question is open. With it, the path space is guaranteed to be a C^1 Hilbert manifold — and the tameness condition is closed under composition, making it a robust and usable class.

## Two-Level Manifolds

A **two-level manifold** is a pair (X1, X2) where X2 ⊂ X1 are Hilbert manifolds modeled on Hilbert spaces H2 ⊂ H1 with dense, compact inclusion. X1 is the "weak" level (less regular), X2 is the "strong" level (more regular).

Typical example in Floer theory:
- X1 = W^{1,2}(R, M) — once-differentiable loops, L^2 derivative
- X2 = W^{2,2}(R, M) — twice-differentiable loops, stronger topology

The two levels have different topologies — the inclusion is compact but dense, so they differ substantially.

## The Problem: Exponential Map Fails

In finite dimensions, constructing a Hilbert manifold structure on a path space uses the exponential map. In infinite dimensions this breaks down because the exponential map doesn't behave well when you have multiple levels of different regularity. The authors had to find a different approach.

## Tameness

A C^2 map φ: U1 ⊂ H1 → H1 is **(H1, H2)-tame** if:
1. Its restriction to U2 = U1 ∩ H2 takes values in H2 and is C^2 as a map to H2
2. For every x ∈ U1 there is a neighborhood W_x and constant κ > 0 such that for all y ∈ W_x ∩ H2 and ξ, η ∈ H2:

$$\|d^2\phi\|_y(\xi, \eta)\|_2 \leq \kappa\left(|\xi|_1|\eta|_2 + |\xi|_2|\eta|_1 + |y|_2|\xi|_1|\eta|_1\right)$$

This estimate controls how the second derivative behaves across the two levels.

**Key theorem (Theorem 2.5): The composition of two tame maps is tame.**

This is the critical property. Because tameness is closed under composition, you can build up complicated two-level manifolds from simple tame transition maps and stay in the tame category.

A **tame two-level manifold** is one whose entire atlas consists of tame transition maps. The pair (X1, X2) becomes a tame (H1, H2)-two-level manifold.

**Example (Lemma 2.14):** The loop space ΛR of any smooth finite-dimensional manifold M is a tame two-level manifold. The transition map induced by a C∞ diffeomorphism φ: R → R is tame — the proof uses Sobolev embedding W^{1,2}(S^1, R) ↪ C^0(S^1, R) to control derivatives.

## Main Results

**Theorem A:** The path space P_{x^- x^+} = W^{1,2}(R, H1) ∩ L^2(R, H2) of a tame two-level manifold has the structure of a C^1 Hilbert manifold.

**Theorem B:** The weak tangent bundle E → P over the path space is also a C^1 Hilbert manifold.

**Theorem C (parametrized):** The same results hold for asymptotically constant parametrized tame maps — needed for the time-dependent gradient flow equations that appear in Floer theory.

## Why This Matters for Floer Theory

Floer homology constructs a homology from the moduli space of gradient flow lines of a functional A on a two-level manifold X. The flow equation is:

$$\partial_s u + \nabla A(u) = 0$$

In the two-level setting, ∇A(x) ∈ TxX1 but not necessarily ∈ TxX2 — the gradient is "unregularized" in Floer's sense. Interpreted as a section of the weak tangent bundle:

```
E
 ↓
P  →  F(u) = ∂_s u + ∇A(u) = 0
```

If P and E are C^1 manifolds, one can take the differential of this section at a zero u and study the resulting operator — which is what you need for Conley theory, Fredholm theory, and ultimately the construction of the homology groups. Without the manifold structure, the whole analytical apparatus breaks down.

This paper shows that under the tameness condition, the manifold structure *does* exist, giving Floer theory a solid foundation for this class of problems.

## Mathematical Context

- **Lang's approach** to Hilbert manifolds uses the exponential map (standard reference: Lang's book on differential geometry). The authors note their complementary approach avoids the exponential map's problems in the multi-level case.
- **Hofer-Wysocki-Zehnder** have worked on polyfold theory, which also deals with Fredholm problems on infinite-dimensional spaces without smooth manifold structure — but from a different angle. This paper's approach is more classical.
- The dense inclusion H2 ⊂ H1 being compact is assumed in Theorem A but not needed for Theorem B, broadening applicability.

## Connections

- [[concepts/symplectic-geometry]] — Floer theory lives in symplectic geometry; path spaces on symplectic manifolds are the primary application
- [[concepts/infinite-dimensional-manifolds]] — the main technical contribution: how to construct Hilbert manifold structure when the standard exponential map fails
- [[concepts/attractor-dynamics]] — gradient flow lines as trajectories in a two-level system, the equilibrium analysis in Floer theory parallels attractor dynamics in dynamical systems