---
created: 2026-05-25
updated: 2026-05-26
type: concept
summary: Mathematical framework for systems that evolve over time according to deterministic rules — differential equations, iterated maps, attractors, bifurcations
tags: [dynamical-systems, mathematics, complexity, attractor-dynamics, systems-theory]
sources: []
status: active
confidence: 0.75
---

# Dynamical Systems

## Definition

A dynamical system is a mathematical framework for describing systems that evolve over time according to deterministic rules. The system state at any moment determines the state at the next moment via a fixed transformation rule. The field spans continuous systems (differential equations) and discrete systems (iterated maps), and encompasses deterministic and stochastic variants.

The core object is the **flow**: a function mapping initial conditions + time → current state. Understanding flows means understanding fixed points, cycles, chaos, and the transition between these regimes.

## Core Concepts

### State Space and Phase Space

The **state space** (or phase space) is the set of all possible system states — each point corresponds to a complete specification of the system. For a simple harmonic oscillator, the phase space is 2D (position × velocity). For an LLM's hidden state, the phase space is extremely high-dimensional — the geometry of this space is what attractor dynamics studies.

### Attractors

An **attractor** is a set of states toward which nearby states evolve under the system dynamics. Types include:

- **Point attractors**: Stable equilibria (system settles to one state)
- **Limit cycles**: Periodic oscillation (system enters a loop)
- **Quasi-periodic attractors**: Toroidal motion on multiple incommensurate frequencies
- **Strange attractors**: Chaotic motion — deterministic but unpredictable over long horizons

The **basin of attraction** is the set of all initial states that eventually converge to a given attractor. The structure of basins — how they partition state space, their boundaries, their fractal dimension — determines the system's qualitative behavior.

### Bifurcations

A **bifurcation** occurs when a small parameter change causes a qualitative shift in the system's behavior — a fixed point appears or disappears, a cycle emerges or dissolves, or chaotic dynamics emerge. Bifurcation theory studies these transitions as control parameters vary.

The canonical example is the logistic map x_{n+1} = rx_n(1-x_n), where varying r produces period-doubling cascades leading to chaos. Real systems often exhibit similar pathways to chaos through period-doubling.

### Sensitivity and Chaos

**Sensitivity to initial conditions** — the hallmark of chaos — means that arbitrarily small differences in initial state produce exponentially diverging trajectories. The **Lyapunov exponent** quantifies this divergence rate. Positive Lyapunov exponents indicate chaos.

This is relevant to transformer dynamics: attention mechanisms and nonlinearities create sensitive dependence on initial activations, suggesting that the "energy landscape" metaphor may have quantitative content beyond metaphor.

## Relevance to AI/ML

### Attractor Dynamics in Neural Networks

Hopfield networks established the attractor model for neural computation — memories as energy minima, recall as attractor settlement. Modern transformers extend this: attention dynamics implement a form of generalized Hopfield network (the IDP framework, Linderman et al. 2022).

The key question is whether the attractor landscape of large transformers is rich enough to support the reasoning-as-attractor-settlement model, or whether the state space geometry is too high-dimensional for classical attractor theory to apply directly.

### Dynamical Systems View of Learning

Training dynamics can be studied as a dynamical system — the parameter trajectory as a flow in weight space. The loss landscape, flat minima, and mode collapse are all dynamical phenomena. Gradient descent with momentum can be analyzed as a second-order dynamical system; learning rate schedules create bifurcations in the training dynamics.

### Reasoning as Dynamical Process

Chain-of-thought reasoning can be modeled as a trajectory through state space, with each reasoning step moving the system toward an attractor representing the answer. Shorthand-for-thought may involve pre-formed attractor basins — compressed representations that allow faster settlement to correct answers.

The open question: Is the attractor landscape of transformer reasoning constructed during training (making it substrate-dependent), or does it reflect general dynamical properties of high-dimensional nonlinear systems (suggesting substrate-independence)?

## Connections
- [[log]]
- [[concepts/attractor-dynamics]]
- [[concepts/dynamical-systems]]
- [[index]]
- [[concepts/systems-theory]]
- [[dynamical-systems]]

- [[attractor-dynamics]]: the neural network instantiation of dynamical systems theory
- [[systems-theory]]: broader framing of interconnected components
- [[complexity]]: dynamical systems at the edge of chaos
- [[emergence]]: attractor reorganization as emergence mechanism
- [[shorthand-for-thought]]: reasoning as attractor settlement
- [[neural-interpretability]]: geometry of transformer state spaces

## Open Questions

1. **Quantitative validity**: Does low-dimensional attractor theory apply to high-dimensional transformer state spaces, or only as qualitative metaphor? The energy landscape picture is compelling but may not have rigorous quantitative content for transformers.

2. **Bifurcations in training**: Can mode collapse and other training failures be understood as bifurcations in the learning dynamics? What are the control parameters, and can they be monitored?

3. **Reasoning trajectory geometry**: Can we characterize the geometry of "reasoning trajectories" in activation space? Do successful chains of thought share geometric properties?

4. **Attractor stability and reliability**: How does the reliability of LLM reasoning relate to the stability of the underlying attractor landscape? Are failures due to basin boundary effects (sensitive dependence on initial activation patterns)?