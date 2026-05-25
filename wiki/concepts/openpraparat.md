---
created: 2026-05-25
updated: 2026-06-19
type: concept
summary: "Guideless artificial life model combining Tierra gene mechanics with 3D virtual creatures; no fitness function; emergent reproduction via mutation + natural selection"
tags: [artificial-life, open-ended-evolution, emergence, neural-networks, self-replication, natural-selection, research]
sources: [[utimula-openpraparat-2025]]
status: reference
confidence: 0.9
---

# OpenPRAPARAT (Utimula 2025)

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

## Solution: The OpenPRAPARAT Model

Incorporate Tierra's template-matching gene mechanism and cellular automaton state rules into cells that move freely in 3D space, creating a search for **persistent patterns** (à la Conway's Game of Life) rather than optimizing a human-defined objective.

### Architecture

The model combines:
- **Tierra's gene mechanism** — template-matching for heritable traits
- **Karl Sims' 3D creatures** — high-dimensional morphology and behavior
- **Cellular automaton state rules** — governing cell-level dynamics
- **No fitness function** — evolution is guideless, driven by natural selection alone

### Key Results

- **Emergent reproduction** via binary fission, budding, and protective organs
- **Energy transport networks** arising from mutation and natural selection
- **Self-replication** without predefined fitness
- Maintains 3D morphological/behavioral freedom throughout

## Connections

### Related Concepts
- [[open-ended-evolution]] — the broader property OpenPRAPARAT demonstrates
- [[emergence]] — key property demonstrated by guideless evolutionary dynamics
- [[artificial-life]] — the field this work belongs to

### Related Projects
- [[alphaevolve]] — AlphaEvolve also uses evolutionary search without fitness functions
- [[minimal-generative-architectures]] — minimal architectures enabling emergent behavior

### Key Pages in This Vault
- [[utimula-openpraparat-2025]] — source paper summary
