---
created: 2026-05-06T21:50:58Z
updated: 2026-05-06T21:50:58Z
type: concept
summary: A framework for interpretability that distinguishes between tokens necessary for a conclusion (load-bearing) and those that serve as statistical noise reduction (scaffolding).
tags: [interpretability, causal-mediation, mech-interp, reasoning]
sources: [Pearl (2001), Conmy et al. (2023), Shorthand for Thought (2026)]
status: active
confidence: 1.0
---

# Load-bearing Reasoning

Load-bearing Reasoning is an interpretability frame that shifts the focus from the total state of a model to the specific "topology" of dependencies that drive a conclusion. It distinguishes between the essential computational path and the probabilistic artifacts of the model's emission policy.

## Key Taxonomy

### 1. Load-bearing Tokens (Irreducible)
A token or reasoning step is **load-bearing** if a counterfactual change to it (intervention) would significantly alter the model's final conclusion. These represent the "irreducible" logical chain of the problem.
- **Analytical Tool**: **Causal Scrubbing** (Conmy et al.) or **Causal Mediation Analysis** (Pearl).
- **Paraclete Focus**: These are the steps that must be formally verified in [[isabelle]].

### 2. Scaffolding Tokens (Calibration)
A token is **scaffolding** if it serves as statistical calibration to settle a noisy inference distribution. These are "thinking out loud" steps that do not strictly change the logical path but improve the model's ability to stay on it.
- **Example**: "Let's think step by step," "Wait, let me see."
- **Analytical Tool**: Entropy-guided filtering (see [[supertokens]]).

## Applications in HiPAI
The Paraclete EBE chain (`check_action` → `calibrate_belief` → `escalate_block`) is a native **Load-bearing Network**.
- **Inside HiPAI**: Using [[isabelle]] to prove formal invariants (no loops, valid terminal states).
- **Around HiPAI**: Running causal mediation on tool-use traces to identify exploratory vs. redundant calls.

## Connections
- Source: [[shorthand-for-thought]]
- Concept: [[chain-of-thought]]
- Concept: [[supertokens]]
- Project: [[hipai-montague]]
