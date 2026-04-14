---
summary: Utimula (2025) — guideless ALife model combining Tierra gene mechanics with 3D virtual creatures; no fitness function; emergent reproduction (binary fission, budding), protective organs, and energy transport networks via mutation + natural selection
tags: [artificial-life, open-ended-evolution, emergence, neural-networks, self-replication, natural-selection]
updated: 2026-04-14T19:14:15Z
created: 2026-04-14T19:14:15Z
---

# Guideless Artificial Life Model (OpenPraparat)

**Author:** Keishu Utimula
**Source:** [MIT Press — Artificial Life 31(1)](https://direct.mit.edu/artl/article/31/1/31/127798)
**Published:** 2025-02-25
**Code:** [OpenPraparat on GitHub](https://github.com/A5size/OpenPraparat) (MIT License)

## Problem

Three foundational ALife lineages each solve part of the puzzle but not all:

- **Tierra / cellular automata** — handle reproduction, development, and individual interactions compositely via self-replicating code, but are severely limited in morphological/behavioral freedom
- **Karl Sims' virtual creatures** — high morphological/behavioral DOF in 3D, but reproduction is via genetic algorithms (requiring predefined fitness functions), and development/interactions are studied only independently
- **Lenia** — extends cellular automata to continuous space with 8 of 9 evolutionary abilities, but self-replication remains elusive

No prior model integrates all three capabilities (reproduction + development + individual interactions) with high morphological freedom *and* no fitness function.

## Solution: The OpenPraparat Model

Incorporate Tierra's template-matching gene mechanism and cellular automaton state rules into cells that move freely in 3D space, creating a search for **persistent patterns** (à la Conway's Game of Life) rather than optimizing a human-defined objective.

### Architecture

Each cell has:
- A **book** (gene string, 64-character alphabet) and **bookmarker** (promoter/read position) — analogous to DNA + promoter
- A **feedforward neural network** (1 hidden layer, weights encoded in the book) controlling behavior: energy transfer, spring length modulation, predation, light emission, communication
- **Four gene-driven actions:** EXPANSION (cell division), CONNECTION, DISCONNECTION, TRANSITION (bookmarker update)
- An **advance** mechanism for finite repetition of gene programs

Environment: 3D terrain field with a swaying sun as sole energy source. Energy metabolism drives natural selection — cells die when energy drops below threshold. Four independent fields with different mutation rates are periodically mixed.

### Key Design Decisions

- **No fitness function** — evolution proceeds entirely by mutation + natural selection
- **No predefined creature forms** — persistent patterns are interpreted as creatures by observers
- Neural network parameters are **genetically encoded** but operate **independently** from gene-driven actions during runtime, enabling flexible responses to environment
- Hebb-like learning rule ($\Delta s = 0.1$) for inter-cell communication coupling strength

## Emergent Results

### Dumbbell-Shaped Creatures (~15M steps)
Evolved from single cells. Reproduce via binary fission (resembling sea anemone division). Evolved **protective white cells** — temporary organs generated during division to prevent predation by increasing connection count. Confirmed experimentally: removing protector generation from the book caused extinction when competing against protector-equipped variants.

### Reticulated Creatures (~200M steps)
Multi-cell networks with efficient energy distribution. Reproduce via **budding/spore-like** mechanism — neural network controls spring contraction until bond breaks, launching offspring away from parent body. Exhibit punctuated equilibrium: long stasis periods followed by rapid capability acquisition (energy transport emerged suddenly after ~20M steps of no change).

### Book Evolution
Active regions of the evolved book constitute only ~1.7% of total length. ~97.5% of the book appears derived from the initial seed, but active regions are almost entirely *novel* mutations — the functional genome was effectively rewritten while structural DNA remained as scaffolding.

## Connections

- [[maximum-occupancy-principle]] — MOP's path-entropy maximization provides a theoretical framework for why guideless systems explore diverse survival strategies; OpenPraparat is empirical evidence of this principle in action
- [[eml-operator]] — the "persistent pattern search" philosophy parallels EML's minimal-primitive approach: both seek what emerges from the simplest possible generative rules
- [[sheffer-stroke]] — conceptual parallel: minimal computational primitives (4 gene actions) generating complex emergent behavior
- [[efhf]] — the book/bookmarker mechanism could be modeled as an epsilon machine with causal states; energy transport emergence as a phase transition is a lumpability event
- [[alphaevolve]] — evolutionary code discovery, but OpenPraparat evolves the *organisms* rather than the *algorithms*

## Open Questions

- No sexual reproduction observed — only asexual
- No vertical growth or active locomotion evolved
- Field size limits biodiversity (single-species dominance)
- Computational cost: ~2-3 months per simulation on 4 cores
- Impact of parameter choices (cell radius, hidden layer size, terrain shape) on evolutionary direction unexplored
