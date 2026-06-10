---
summary: Quantized Evolution Strategies bridges neural architecture search, discrete optimization, and LLM fine-tuning through shared combinatorial optimization over quantized parameter spaces
tags: [insights, zettelkasten, evolution-strategies, quantization, nas, fine-tuning, optimization]
updated: 2026-06-10T12:25:39Z
created: 2026-06-10T12:25:39Z
---

## Core Synthesis

Quantized Evolution Strategies (QES) sits at the intersection of neural architecture search (NAS) methods like RZ-NAS and LLM-NAS, combinatorics (multiplication principle for genotype encoding), and LLM fine-tuning. The bridge is the **discrete optimization of continuous representations**—QES applies evolutionary search in quantized (discrete) parameter spaces, which is structurally identical to how NAS explores architecture configurations and how fine-tuning navigates the discrete decision space of model adaptation strategies.

## The Triad

1. **NAS (RZ-NAS, LLM-NAS)** — searches discrete architecture configurations
2. **Quantized Evolution Strategies** — optimizes in discrete parameter subspaces
3. **LLM Fine-Tuning** — navigates adaptation strategy space as discrete choices

## Novel Connection

The shared substrate is discrete optimization over combinatorially large spaces. QES may be the methodological Rosetta Stone that connects architecture search to fine-tuning strategy selection, suggesting that fine-tuning itself is a form of architecture search in weight-space.

## Cross-Links

- [[quantization]] — Model quantization techniques
- [[neural-architecture-search]] — NAS methodology
