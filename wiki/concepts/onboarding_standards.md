---
summary: Standards and protocol for onboarding new domains to the Meta-Harness.
tags: [onboarding, standards, domain-onboarding]
updated: 2026-05-07T23:21:39Z
created: 2026-05-07T23:21:39Z
---

# Domain Onboarding Standards

Onboarding a new domain into the Meta-Harness is a structured process designed to ensure that the evolution loop has a stable, measurable, and leak-proof environment for experimentation.

## The Onboarding Protocol

The protocol is defined in `ONBOARDING.md` and follows a Socratic, gate-based workflow.

### 1. Initial Assessment
Evaluate the domain against the **Promising Domain Properties**:
- Long-horizon or multi-step tasks.
- Repeated tasks/episodes.
- Fixed base model.
- Measurable success metric.
- Stable evaluation loop.

### 2. Specification Phase
A `domain_spec.md` must be created, covering:
- **Problem Framing**: Goal, unit of evaluation, fixed components, and budget.
- **Harness Definition**: Interface (Protocol), base class, and validation plan.
- **Evaluation**: Search set, held-out test, primary/secondary metrics, noise, and leakage mitigation.
- **Baselines**: Handwritten baselines and existing state-of-the-art.
- **Experience**: Offline traces and relevant documentation.
- **Online Logging**: Trace storage, metadata, and artifacts.

### 3. Implementation Gate
Do **NOT** start implementation until the `domain_spec.md` is complete and all required fields are filled or marked `unknown`.

## Required Artifacts
- `domain_spec.md`: The single source of truth for the domain.
- `agents/base.py`: The base implementation of the harness.
- `evaluator.py`: The domain-specific implementation of the [[Meta-Harness Evolution Loop]] `Evaluator` protocol.

## Related
- [[Meta-Harness Evolution Loop]]
- [[Hermes Agent Architecture]]
