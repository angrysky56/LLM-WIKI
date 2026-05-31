---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: Calibrated Collective Oversight (CCO) uses conformal decision theory to calibrate AI conservatism, enabling weaker overseers to constrain stronger agents with formal guarantees.
tags: [paper, arxiv, research, AI-safety, scalable-oversight, RLHF, agentic-AI]
---

# Calibrating Conservatism for Scalable Oversight (CCO)

**arXiv:** [2605.28807](https://arxiv.org/abs/2605.28807) | **Authors:** Overman, Bayati (Stanford GSB) | **Date:** 2026-05-28

## Overview

Agentic AI systems capable of autonomous planning pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed their own capabilities? CCO introduces Calibrated Collective Oversight, which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline.

## Core Mechanism

Inspired by [[attainable-utility-preservation]], CCO enables **collective conservatism**: actions face a penalty proportional to overseer concern. High-utility actions are still selected when overseers find them unobjectionable, and overridden only when concern accumulates. The key innovation is **online calibration using Conformal Decision Theory**, ensuring undesirable outcomes remain below a user-specified target threshold with finite-time bounds and no distributional assumptions.

## Results

- Modified SWE-bench: weaker overseers successfully constrain an adversarially misaligned stronger agent
- MACHIAVELLI: CCO substantially reduces ethical violations while preserving reward
- Empirical violation rates closely match specified targets

## Why It Matters

Unlike prior scalable oversight work (debate, iterated amplification), CCO provides formal safety guarantees and is designed for sequential, agentic settings rather than single-turn interactions.

## Related

- [[scalable-oversight]] — general research area
- [[attainable-utility-preservation]] — foundational method inspiring CCO
- [[conformal-decision-theory]] — calibration mechanism
- [[agentic-AI-safety]] — deployment context
- [[adversarial-alignment]] — misalignment threat model