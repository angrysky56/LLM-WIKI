---
created: 2026-05-23
updated: 2026-05-23
type: source
summary: "DeltaDirect: Video-LLMs suffer directional motion blindness — near-chance on signed motion direction despite strong appearance recognition. Introduces MoDirect dataset and DeltaDirect projector auxiliary objective that improves accuracy from 25.9% to 85.4% on synthetic benchmarks and +21.9pp on real-world motion."
tags: [video-llm, motion-understanding, vision-language, benchmarking, probing, direction-binding-gap, projector-training, mcp-logic, efhf, mop-explorer, agentic-research, verifier-graph, graphrag, maximum-occupancy-principle, sheaf-consistency-enforcer]
sources: https://arxiv.org/abs/2605.22823, https://github.com/KHU-VLL/DeltaDirect
status: active
confidence: 1.0
---

# DeltaDirect: Directional Motion Blindness in Video-LLMs

**Paper:** [arXiv:2605.22823v1](https://arxiv.org/abs/2605.22823) — "Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs"
**Authors:** Jongseo Lee, Sooa Kim, Hyuntak Lee, Sunghun Kim, Jihoon Chung, Jinwoo Choi (KHU + Princeton)
**Published:** 21 May 2026

---

## Executive Summary

This paper identifies **directional motion blindness** in Video-LLMs: despite near-perfect object color/appearance recognition, state-of-the-art Video-LLMs perform at near-random chance (~25%) on the elementary task of identifying which direction (left/right/up/down) a simple object is moving. The key finding is that this is **not** a perception failure — motion direction remains linearly decodable from vision encoder, projector, and LLM hidden states — but a **direction binding gap**: the model fails to connect the available motion signal to the correct verbal answer option. The paper introduces MoDirect (a controlled dataset family) and DeltaDirect (a projector-level auxiliary objective) that improves motion direction accuracy from 25.9% to 85.4% on the synthetic benchmark and by +21.9pp on real-world benchmarks without seeing real-world training data.

---

## Technical Approach

### The Direction Binding Gap

The authors trace motion direction information through the Video-LLM pipeline using linear probing. They find:

- **Vision encoder output:** 99.8% probe accuracy on motion direction
- **Projector output:** 96.5% probe accuracy
- **LLM hidden states (visual token positions):** 98.1% probe accuracy
- **Final readout token (used for answer prediction):** 95.3% probe accuracy

Yet the actual MCQ accuracy stays near 25% (chance). This decoupled pattern — decodable representations but wrong answer — is the **direction binding gap**.

> "Although motion direction is linearly accessible from the vision encoder, projector, and LLM hidden states, the readout fails to bind this signal to the correct verbal answer option."

### MoDirect Dataset Family

A controlled 2×2 dataset design across two axes:

| Axis | Values |
|------|--------|
| **Foreground** | Primitive (geometric shapes) / Cutout (segmented real-world objects) |
| **Background** | Synthetic (uniform color) / Real (natural scenes) |

Subsets:
- **MoDirect-Inst:** Instruction tuning subset (Primitive-on-Syn only)
- **MoDirect-SynBench:** 4 synthetic domains for controlled evaluation
- **MoDirect-RealBench:** Real-world videos from Something-Something-v2, TOMATO, KTH

### DeltaDirect: Projector-Level Auxiliary Objective

DeltaDirect adds a training-only auxiliary branch that predicts **normalized 2-D motion vectors** from **adjacent-frame projector-feature deltas**. The MVP (Motion Vector Prediction) head is discarded at inference time — no change to model architecture, token sequence, or decoding.

Key design:
- Predicts signed 2D displacement (dx, dy) from frame-to-frame projector feature differences
- Uses analytically available motion vectors from synthetic videos as supervision
- Strengthens signed displacement cues at the visual-language interface before they enter the LLM

### Concept Vector Analysis: The Magnitude Deficit

The authors use **difference-in-means** motion direction concept vectors to analyze why instruction tuning on the simplest domain (Primitive-on-Syn) doesn't generalize to harder domains:

- After instruction tuning, concept vectors are **well-aligned across domains** (high cosine similarity)
- But on complex domains (Cutout-on-Real), their **magnitude drops sharply**
- **Restoring just the magnitude** of the concept vector recovers much of the lost accuracy

This reveals the OOD failure is not a missing geometry but a **magnitude deficit** — the model learns the motion direction structure but the signal is too weak to read out reliably across domains.

---

## Key Results

| Setting | Baseline | + Instruction Tuning | + DeltaDirect |
|---------|----------|---------------------|---------------|
| MoDirect-SynBench (avg) | 25.9% | ~70% | **85.4%** |
| Cutout-on-Real | near-chance | degraded | **+11.2pp over inst.-tuning** |
| MoDirect-RealBench (zero-shot) | near-chance | — | **+21.9pp over vanilla** |

DeltaDirect preserves or improves performance on standard video-understanding benchmarks (ActivityNet, MSRVTT, etc.).

---

## Key Quotes

> "Despite rapid progress on temporal understanding, we find that many Video-LLMs fail at a much simpler temporal primitive: signed image-plane motion direction."

> "Motion direction remains linearly accessible from the vision encoder, projector, and LLM hidden states, but the readout fails to bind this signal to the correct verbal answer option."

> "The out-of-domain failure is not due to a missing motion direction geometry, but to a magnitude deficit: the model learns the motion direction structure, but the signal is too weak to be reliably read out across domains."

> "DeltaDirect uses analytically available 2-D motion vectors only as training-time supervision on projector-feature deltas, without changing the test-time input or decoding pipeline."

---

## Relevance to EFHF / AGEM / MOP Research Connections

| Connection | Relevance |
|------------|-----------|
| **[[efhf]]** | DeltaDirect exemplifies diagnosis-driven intervention at a specific architectural interface — the projector. The EFHF layered architecture (sensory → projection → LLM) mirrors the identified breakdown point where signal is present but unbound. |
| **[[mop-explorer]]** | The magnitude deficit finding suggests MOP could benefit from analyzing representation strength alongside representation geometry. The OOD generalization failure is a case where structural alignment (cosine similarity) is preserved but intensity (magnitude) collapses. |
| **[[agentic-research]]** | DeltaDirect is a case study in agentic diagnosis: the pipeline systematically traced the failure mode (binding gap) before designing intervention, rather than blindly scaling data or parameters. |
| **[[verifier-graph]]** | The paper's methodology (probing at each pipeline stage → isolating the failure point → designing targeted fix) parallels verifier-graph reasoning: establishing which nodes/edges are functional before proposing corrections. |
| **[[mcp-logic]]** | The concept vector analysis (difference-in-means) is a formal probing technique — DeltaDirect's diagnostic pipeline could be formalized as a proof/verification sequence in the MCP logic layer. |
| **[[graphrag]]** | MoDirect provides structured motion-direction benchmarks that could enrich graphrag retrieval evaluation — temporal/directional understanding is a known weakness in RAG over video content. |
| **[[maximum-occupancy-principle]]** | The readout token represents a bottleneck — the "maximum occupancy" of binding capacity for directional signals. DeltaDirect effectively increases the effective bandwidth of motion-direction information through the projector interface. |
| **[[sheaf-consistency-enforcer]]** | The magnitude deficit across domains (Primitive-on-Syn → Cutout-on-Real) suggests a consistency failure in how motion-direction signals are locally normalized. Sheaf-consistency enforcement across domain patches could address this. |

---

## Structural Insights

1. **The interface is the bottleneck, not the encoder.** Vision encoders preserve direction nearly perfectly. Projectors preserve it well. LLMs internally decode it. The failure is entirely at the **readout-to-verbal-binding** step — a classic cross-modality binding problem.

2. **Synthetic instruction tuning teaches geometry, not amplitude.** Models learn what "rightward" looks like in feature space (good alignment) but the signal weakens in new domains (magnitude collapse). Fixing magnitude recovers performance.

3. **Projector-level intervention is sufficient.** DeltaDirect doesn't touch the vision encoder or LLM. It only modifies the projector training objective. This is an important architectural insight: the visual-language interface is where directional motion signals need strengthening.

4. **Zero-shot real-world transfer is achievable with synthetic supervision.** +21.9pp on real benchmarks without any real-world training data is a strong result for the synthetic-only training regime, suggesting the motion-direction geometry learned on primitives generalizes when the representation strength is preserved.

5. **The MCQ binding design controls for position aliases.** By randomizing answer option order per-example, the paper ensures the model must bind direction-to-option-text rather than exploiting fixed letter-correspondence shortcuts.

---

## Connections

- [[video-llm]]
- [[motion-understanding]]
- [[vision-language-alignment]]
- [[probing-analysis]]
- [[mcp-logic]]
- [[efhf]]