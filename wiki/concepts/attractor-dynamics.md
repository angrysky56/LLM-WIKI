---
created: 2026-05-25
updated: 2026-07-03
type: concept
summary: How dynamical systems settle into stable states — attractor basins, state convergence in neural networks, energy landscapes, and connection to emergence and neural interpretability
tags: [dynamical-systems, neural-networks, attractors, emergence, energy-landscape]
sources: []
status: active
confidence: 0.75
---

# Attractor Dynamics

## Definition

Attractor dynamics describe how the state of a dynamical system evolves toward stable configurations — attractors — and how the geometry of the system's state space determines which attractors are reached from which starting conditions. An attractor is a state (or set of states) that the system tends toward over time; the basin of attraction is the region of state space that leads to that attractor.

In the canonical formulation: a system has an energy function (Lyapunov function for stable systems), and attractors correspond to energy minima. The system evolves by descending the energy landscape — moving toward lower-energy configurations until it settles into a local or global minimum.

## Why It Matters in Neural Networks

Attractor dynamics are central to understanding neural network behavior:

1. **Hopfield networks** (see [[hopfield-network]]) are the canonical model: content-addressable memory via energy minima as attractors. The network state relaxes to the nearest stored pattern.

2. **Attention mechanisms** in transformers can be viewed as generalizations of Hopfield network dynamics (see [[betteti-baggio-bullo-zampieri-idp-hopfield-2025]]). The attention pattern determines which states attract the current context.

3. **Reasoning as attractor settlement**: Chain-of-thought reasoning can be viewed as the model settling into an attractor that represents the conclusion. The CoT tokens are the path through state space to the attractor state. [[Shorthand-for-thought]] may be about which attractor basins are pre-formed (compressed) vs. traversed explicitly.

4. **Representation geometry** (from [[neural-interpretability]]): concepts that are geometrically close in activation space may share attractor basins — accessing one retrieves similar states.

## Connection to Emergence

[[Emergence]] has an attractor-dynamics interpretation: emergent capabilities appear when the model's parameter space crosses a threshold that reorganizes the energy landscape, creating new attractors (capable reasoning paths) or draining basins of attraction (failure modes disappear). The phase transition in capability is a topological change in the energy landscape.

This connects to [[computational-irreducibility]]: if the energy landscape is complex, you cannot predict which attractor the system will reach without running it. The only way to know what the model will do is to simulate it — which is what [[neural-interpretability]]'s empirical approach acknowledges.

## Attractor Types

1. **Point attractors**: Single stable state (Hopfield memory)
2. **Cyclic attractors**: Periodic orbits (oscillatory dynamics)
3. **Quasi-periodic attractors**: Complex but bounded orbits
4. **Strange attractors**: Chaotic, fractal geometry (Lorenz, turbulence)

In LLMs, reasoning traces may correspond to movement through a state space with:
- Point attractors for factual recall (the answer is a fixed point)
- Cyclic or quasi-periodic for reasoning loops (deliberation cycles)
- Strange attractors for creative generation (divergent exploration)

## Criticality and Attractor Basin Geometry

The concept of criticality connects to attractor dynamics: a system at criticality has a specific balance between stability (deep attractors) and flexibility (shallow basins that allow exploration). Critical initialization in neural networks (see [[critical-initialization-biological-neural-networks]]) may correspond to a specific geometry of the energy landscape that balances expressivity and reliability.

## Connections
- [[concepts/dynamical-systems]]
- [[wiki/index]]
- [[log]]
- [[concepts/betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[concepts/attractor-dynamics]]
- [[concepts/attractor-dynamics]]

- [[emergence]] — emergent capabilities may be reorganizations of the energy landscape creating/destroying attractor basins
- [[neural-interpretability]] — representation geometry maps the structure of attractor basins in activation space
- [[hopfield-network]] — canonical model; energy-based attractors
- [[dynamical-systems]] — the mathematical framework; attractor dynamics is the core phenomenon
- [[computational-irreducibility]] — complex attractor landscapes make prediction require simulation
- [[shorthand-for-thought]] — pre-formed attractor basins for reasoning; which basins exist determines what's accessible without explicit traversal

## Open Questions

1. **Can we map the attractor landscape of a large language model?** If attractor basins correspond to reasoning paths, mapping them would reveal the model's "cognitive geography" — what it can reach easily vs. with difficulty.

2. **What is the relationship between attention attractors and token prediction?** Does attention structure determine basin geometry in token-space? This connects to how [[shorthand-for-thought]] compresses reasoning paths.

3. **Basin engineering**: If we can understand the attractor landscape, can we modify it — create new basins for desired behaviors, drain basins for failure modes?

4. **Relationship to RLHF**: Does RLHF modify the energy landscape (shaping attractors) or just the starting conditions (where the model begins in state space)?

## Limitations

- Most attractor theory is proven for low-dimensional systems; high-dimensional neural network state spaces behave differently
- The energy function for transformer models is not well-defined, so the "landscape" metaphor is qualitative
- Attractor dynamics in continuous-time dynamical systems vs. discrete token-step models may require different formalisms