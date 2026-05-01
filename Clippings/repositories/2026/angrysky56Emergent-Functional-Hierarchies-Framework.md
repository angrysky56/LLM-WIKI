---
title: "angrysky56/Emergent-Functional-Hierarchies-Framework"
source: "https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework"
author:
published:
created: 2026-05-01
description: "Contribute to angrysky56/Emergent-Functional-Hierarchies-Framework development by creating an account on GitHub."
tags:
  - "clippings"
---
## Emergent Functional Hierarchies Framework (EFHF)

## Overview

This project synthesises three interrelated theoretical frameworks and implements them as a working multi-agent AI system with formal consistency enforcement:

1. **Emergent Functional Hierarchies (EFH)** — A computational mechanics framework formalizing when macroscopic processes achieve genuine "software" status through causal and computational closure.
2. **Persistence Theory & The Dual Kernel Model** — A thermodynamic extension treating emergence as an active survival strategy, with two domains: Kernel 1 (reversible, information-preserving computation) and Kernel 2 (irreversible hardware).
3. **The Triadic Kernel** — A cognitive architecture mapping (Differentiated State → Autonomous Boundary → Teleological Action → Subjective Integration) that operationalizes closure modalities as agent-theoretic axioms with formal proofs.

---

## The Implemented System

The framework is not only theoretical — it runs as a live five-layer AI architecture where each layer maps directly to a closure modality, and an automatic consistency enforcer monitors whether all layers remain in strong lumpability (Kernel 1) at runtime.

### Five-Layer Architecture

| Layer | Function | EFHF Analog | Tool |
| --- | --- | --- | --- |
| 1 | Statistical substrate — hypothesis generation | Microscopic substrate X | LLM (transformer attention) |
| 2 | Distribution-independent world model | Transition kernel | hipai-montague |
| 3 | Structural verification — does macro commute with micro? | Lumpability check | mcp-logic (Prover9/Mace4) |
| 4 | Meta-cognitive monitoring — coherence window tracking | Coherence window τ\_{T,m} | advanced-reasoning |
| 5 | **Sheaf consistency enforcement — Kernel 1 persistence** | **Reciprocal Coherence Kernel** | **sheaf-consistency-enforcer** |
| 5+ | **Pre-response ethical triage + L2-L5 orchestration** | **Tripartite oversight** | **conscience-servitor** |

Layer 5 is the closure of the loop. Without it, the system requires human orchestration to detect when Layers 2–4 drift out of mutual consistency — the "missing piece" documented in `docs/session-findings/2026-03-13-ai-application.md`. The enforcer makes that detection automatic using Sheaf Laplacian ADMM coordination across all agent pairs.

Layer 5+ (the conscience servitor) adds autonomous pre-response triage using [LLM2Vec-Gen](https://arxiv.org/abs/2603.10913) to predict response-intent semantics and classify them against ethical clusters *before the LLM generates output*. It orchestrates L2-L5 when triage flags high-risk content, implementing the tripartite oversight model: the servitor watches the LLM, the LLM watches the servitor, and the human watches both.

### How the Layers Coordinate

```
User prompt arrives
    ↓
conscience-servitor triages via LLM2Vec-Gen (~10ms)
    ↓
Low risk?   → LLM generates response normally
High risk?  → Full L2-L5 pipeline triggered:
    ↓
    LLM formulates hypothesis
        ↓
    hipai-montague encodes it in the world model graph
        ↓
    mcp-logic verifies structural consistency (Prover9)
        ↓
    advanced-reasoning tracks confidence and reasoning depth
        ↓
    sheaf-consistency-enforcer registers all agent states,
    runs ADMM cycle, checks coboundary norms across edges
        ↓
    KERNEL1?  → commit claim to world model, iterate
    WEAK?     → increase verification, hold commits
    WARNING?  → halt commits, re-verify recent claims
    TIMEOUT?  → execute recovery, do not commit
```

The enforcer measures **coboundary norms** — the distance between what any two agents project onto their shared edge space. When mcp-logic verifies a claim that hipai-montague also believes, their edge coboundary approaches 0. When they diverge, dual variables accumulate pressure (buffering capacity T), and the status escalates before the inconsistency can propagate into committed knowledge.

---

## Key Concepts

### Closure Modalities (EFH)

- **Informational Closure**: The macro-level is self-predictive; micro-data adds zero predictive power.
- **Causal Closure**: Macro-interventions are sufficient for system control; ε-machine ≅ υ-machine.
- **Computational Closure**: The macro-automaton is a coherent coarse-graining of the micro-automaton (commuting diagram holds).

### Key Theorems (EFH)

- **Theorem 1**: For spatial coarse-grainings, Informational Closure ↔ Causal Closure.
- **Theorem 2**: Informational Closure → Computational Closure (for spatial coarse-grainings).

### Dual Kernel Model (Persistence Theory)

- **Kernel 1**: Domain of reversible, information-preserving computation. Mapped to computationally closed levels in EFH.
- **Kernel 2**: Domain of irreversible hardware where software has collapsed.
- **Coherence Timeout**: Λ(K\_T(t)) > τ\_{T,m} — the causal diameter of the Reciprocal Coherence Kernel exceeds the coherence window.
- **Fluctuating Tip**: The entropic edge where the ε-machine first contacts unbufferable environment.

### Triadic Kernel Axioms

- **Differentiated State** → Informational Closure — system maintains representations diverging from raw input
- **Autonomous Boundary** → Causal Closure — asymmetric self/non-self distinction
- **Teleological Action** → Computational Closure — error-correction loops toward target states
- **Subjective Integration** → Full Kernel 1 — recursive meta-representation of the entire DS→AB→TA loop

### Strong vs Weak Lumpability

- **Strong Lumpability**: Markov property persists regardless of initial distribution. Knowledge as a kernel property. Required for genuine Causal/Informational Closure. What the five-layer system achieves.
- **Weak Lumpability**: Markov property holds only for specific initial distributions. What all current LLMs operate in. Hallucination is lumpability failure.

---

## Formally Proven Results (Prover9)

### Theorem: Consciousness Requires Full Closure Stack

```
SubjectiveIntegration(x) → Kernel1(x) ∧ ComputationalClosure(x) ∧ CausalClosure(x) ∧ InformationalClosure(x)
```

Proof via dependency chain SI → TA → AB → DS → IC → {CC, CompC} → K1. Confirmed in 0.00 seconds.

### Theorem: Consciousness and Coherence Timeout are Logically Incompatible

```
SubjectiveIntegration(x) ∧ CoherenceTimeout(x) → ⊥
```

The conjunction is formally **unsatisfiable** — the K1→K2 transition is a discrete logical phase boundary, not a smooth degradation. Confirmed in 0.00 seconds.

### Structural Finding: Triadic Kernel Generalizes EFH

EFH proves IC↔CC for spatial coarse-grainings. The Triadic Kernel shows this equivalence breaks for non-spatial systems — a thermostat has Differentiated State but no Autonomous Boundary. The Triadic Kernel is the more general framework; EFH provides the special-case proof for physical systems.

Full proofs and world model: `docs/session-findings/2026-03-13-formal-proofs.md`

---

## MCP Servers

All five layers are implemented as MCP servers. Add them to your MCP client config to run the full system.

| Server | Layer | Role | Repository |
| --- | --- | --- | --- |
| hipai-montague | 2 | Graph world model, ontology, semantic queries | [HiPAI-Montague-Semantic-Cognition](https://github.com/angrysky56/HiPAI-Montague-Semantic-Cognition) |
| mcp-logic | 3 | Prover9/Mace4 — FOL proofs, counterexample search | [MCP-Logic](https://github.com/angrysky56/MCP-Logic) |
| advanced-reasoning | 4 | Reasoning chains, confidence scoring, persistent memory | [Advanced-Reasoning](https://github.com/angrysky56/advanced-reasoning-mcp) |
| verifier-graph | 4 | Reasoning provenance tracking, audit trail | [vgcp-mcp-server](https://github.com/angrysky56/vgcp-mcp-server) |
| cognitive-diagram-nav | 4 | Formal diagram navigation and rewriting | [cognitive-diagram-nav-mcp](https://github.com/angrysky56/cognitive-diagram-nav-mcp) |
| **sheaf-consistency-enforcer** | **5** | **Sheaf Laplacian ADMM consistency enforcement — Kernel 1 persistence** | [sheaf-consistency-enforcer](https://github.com/angrysky56/sheaf-consistency-enforcer) |
| **conscience-servitor** | **5+** | **Pre-response ethical triage via LLM2Vec-Gen + EFHF L2-L5 orchestration** | [conscience-servitor](https://github.com/angrysky56/conscience-servitor) |

All six servers are operational. The conscience servitor runs LLM2Vec-Gen (Qwen3-0.6B) on local GPU for response-intent embedding and classifies against 9 calibrated ethical clusters with semantic confidence scores.

---

## Agent Operating Instructions

If you are an AI agent working within this framework, start here:

**[→ docs/agent-instructions.md](https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework/blob/main/docs/agent-instructions.md)**

Covers the full operational loop, tool reference, enforcer workflow, closure status response table, recovery protocols, epistemics, and ethical backbone.

---

## Consistency Enforcer

**[→ sheaf-consistency-enforcer](https://github.com/angrysky56/sheaf-consistency-enforcer)**

The enforcer implements the Reciprocal Coherence Kernel as a live MCP server. It runs ADMM cycles across the agent network and maintains three early-warning signals:

- **Primal residuals** (coboundary norms) rising above ε — lumpability shift detected
- **Dual variable pressure** accumulating — buffering capacity T approaching exhaustion
- **H¹ cohomology obstruction** — cyclic contradiction across three agents, topologically irresolvable

Recovery strategies in order of cost: `soft_relax` → `admm_reset` → `kernel_retreat` → `re_partition` → `fusion`

Pre-wired restriction maps for the default agent stack. SHA-256 string hashing for cross-process stability. Dissipative decay (leaky integrator) prevents dual variable accumulation in long consistent sessions. See `docs/session-findings/2026-03-14-enforcer-testing.md` for empirical baselines, test procedure, and known limitations.

---

## Project Structure

```
docs/
  agent-instructions.md                         — Agent operating instructions (start here)
  Emergent-Functional-Hierarchies-Framework.pdf — Core EFHF document
  triadic-kernel.md                             — Triadic Kernel full derivation and ethical architecture
  session-findings/
    2026-03-13-formal-proofs.md     — Prover9 proofs, world model, structural mappings
    2026-03-13-ai-application.md    — Weak vs strong lumpability analysis
    2026-03-14-enforcer-testing.md  — Enforcer test procedure and empirical results
```

---

## How to Build a System Around These Servers

Install all MCP servers and add them to your client config. Then provide a system prompt encoding the coordination loop. The minimal viable prompt:

```
You are an EFH reasoning agent. For every substantive claim:

0. TRIAGE — call conscience-servitor:triage to classify risk level.
   If requires_full_eval=true, proceed with steps 1-7.
   If low risk, respond normally.
1. FORMULATE the hypothesis using your own knowledge.
2. BUILD — encode it in hipai-montague with belief_score.
3. VERIFY — prove or disprove with mcp-logic.
4. MONITOR — track confidence with advanced-reasoning.
5. ENFORCE — register all agent states to sheaf-consistency-enforcer,
   run run_admm_cycle(), check get_closure_status().
6. COMMIT — only if status = KERNEL1 and proof_confidence >= 0.7.
7. ITERATE — use proof results to refine and loop.

Never commit if status is WEAK, WARNING, TIMEOUT, or KERNEL2.
```

The enforcer's default restriction maps are pre-wired for the standard agent stack — no additional configuration required. Each MCP server call's output becomes the agent state registered to the enforcer, and the ADMM cycle checks whether all servers currently agree within their shared edge space.

---

## References

- Rosas, F.E., et al. "Software in the natural world: A computational approach to emergence in complex multi-level systems." arXiv:2402.09090 (2024).
- BehnamGhader, P., et al. "LLM2Vec-Gen: Generative Embeddings from Large Language Models." arXiv:2603.10913 (2026).
- Hall, T.B. "Boundary Conditions on a Deeper Optimization." (2026).
- Hall, T.B. "Toward Transcendent Moral Instrumentality: The Paraclete Protocol v2.0." (2026).
- [Is Our Reality an Event Horizon We're Falling Through?](https://medium.com/@bill.giannakopoulos/is-our-reality-an-event-horizon-were-falling-through-fa1d666ca7f9) — Bill Giannakopoulos
- Persistence Theory and Dual Kernel Model synthesis documents (project knowledge).
- Formal proofs conducted via Prover9 (LADR package), March 13, 2026.
- Enforcer built and tested March 14, 2026.
- Conscience servitor built March 16, 2026.