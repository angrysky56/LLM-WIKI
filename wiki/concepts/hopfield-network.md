---
summary: Recurrent neural network with associative memory, energy-based stable states, content-addressable retrieval
tags: [neural-networks, associative-memory, dynamical-systems, hopfield]
updated: 2026-05-23T21:26:33Z
created: 2026-05-23T21:26:33Z
sources: []
status: active
confidence: 0.8
type: concept
---

# Hopfield Network

*Stub — needs real content*

A Hopfield network is a recurrent artificial neural network with associative (content-addressable) memory properties, first described by John Hopfield in 1982.

## Key Properties

- **Energy function:** Stable states correspond to minima of a Lyapunov function
- **Content-addressable:** Retrieving a memory from a partial cue
- **Capacity:** ~0.14N memories in the classic model; improved bounds via $\frac{N}{6\log(N)}$ for exact convergence

## Connection to Transformers

Modern transformer attention mechanisms can be framed as generalizations of Hopfield network dynamics. See [[betteti-baggio-bullo-zampieri-idp-hopfield-2025]] for the IDP extension that connects to dynamic self-attention.


## Connections
- [[log]]
- [[concepts/hopfield-network]]
- [[concepts/attractor-dynamics]]
- [[concepts/criticality]]
- [[sources/papers/betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[wiki/index]]
- [[concepts/hopfield-network]]


- [[attractor-dynamics]]