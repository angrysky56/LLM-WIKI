
---
title: "A critical initialization for biological neural networks"
source: https://www.nature.com/articles/s41586-026-10528-1
created: 2026-05-24
type: source
tags: [neuroscience, initialization, criticality, symmetric-matrix, working-memory, power-law]
summary: "Brain spontaneous activity follows dynamics from a critically normalized random symmetric matrix (spectral radius ≈ 1), producing a power-law variance spectrum (exponent ~2/3) that matches cortical and brainwide recordings (observed: 0.7–0.85). CA1 hippocampus is an exception, optimized for information storage over long-timescale coordination."
---

## Paper Metadata

| Field | Value |
|-------|-------|
| Published | Nature (2026) |
| DOI | s41586-026-10528-1 |
| Subjects | Neuroscience, neural initialization, criticality, working memory |

## Core Finding

Brain spontaneous activity follows dynamics governed by a **critically normalized random symmetric matrix** — the spectral radius is tuned to ≈ 1. This single initialization condition produces:

- **Power-law variance spectrum** with exponent ~2/3
- **High-dimensional global activity modes** that persist across brainwide recordings
- **Long timescales** suitable for zero-shot working memory tasks

## Key Results

### Power-law exponents match theory to data
- **Cortical 2p recordings**: exponent 0.7–0.85
- **Brainwide ephys recordings**: exponent 0.7–0.85
- **Theory (symmetric critically normalized)**: exponent 2/3

### CA1 hippocampus is different
Hippocampal CA1 shows exponent 0.4–0.5 — faster decay, resembling an efficient uncorrelated code optimized for **information storage capacity** rather than long-timescale coordination.

### Symmetric vs non-symmetric matters
- **Symmetric** matrices → real eigenvalues → relaxation dynamics → stable representations over time
- **Non-symmetric** matrices → complex eigenvalues → rotational dynamics → information rotates through state space, harder to read out later
- The brain's spontaneous activity has near-zero complex eigenvalue components → symmetric connectivity dominates

### Computational implications
Critically normalized symmetric dynamics solve:
- **Delayed binary classification** (simple working memory)
- **Zero-shot working memory** (1,000 training → 1,000 arbitrary test inputs) — requires recalling features of arbitrary random inputs, which humans can do

Echo-state networks (nonlinear, non-symmetric) struggle to maintain more than ~0.5s of memory due to chaotic dynamics not being robust to noise.

## Mechanistic Model

1. Interaction matrix **A** = symmetric random matrix with uniformly distributed positive entries (excitatory connections)
2. Subtract the mean → implements global inhibitory feedback (stabilizes dynamics)
3. Scale so **largest eigenvalue = 1** → critically normalized
4. Linear dynamics: `dx/dt = -x + Ax + noise`
5. Covariance spectrum follows power-law with exponent 2/3 (Wigner semicircle connection)

The critical normalization can be achieved through **self-tuning**: an initially unstable system scales down via pruning/rescaling until stable.

## Why This Matters for AI/ML

1. **Initialization matters**: Good initializations directly satisfy temporal requirements of many computational tasks — this provides a biological grounding for why.
2. **Symmetric > non-symmetric for memory**: If you need stable long-timescale representations, symmetric connectivity is superior.
3. **Power-law dimensionality**: ~1,500 dimensions needed to account for 50% of variance in a 10,000-neuron population (2/3 power-law) vs ~3 dimensions (4/3 power-law from non-symmetric/chaotic).
4. **Spontaneous activity as scaffold**: The brain's rest state may be a pre-tuned reservoir ready for arbitrary tasks — readout/feedforward connections learn, but the dynamical substrate is already optimal.

## Connections

- [[initialization]] — theory meets practice in neural network initialization
- [[emergence]] — macroscopic brainwide modes emerging from microscopic pairwise interactions
- [[working-memory]] — zero-shot working memory task performance
- [[criticality]] — critical normalization as self-organized state
- [[activation-steering]] — eigenmode-guided steering as analogous mechanism

## Limitations

- Model is linear (nonlinear effects not captured)
- CA1 exception not fully explained by current model
- Connectivity is random — structured connectivity effects need further study
