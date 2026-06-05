---
created: 2026-06-05T08:00:00Z
updated: 2026-06-05T08:00:00Z
type: source
summary: "Lee et al. (Kyung Hee University, 2026) — identifies directional motion blindness in Video-LLMs: most models perform near chance (25%) at distinguishing left/right/up/down motion direction despite strong appearance recognition. The direction binding gap: motion signal remains linearly decodable throughout the pipeline (vision encoder, projector, LLM states) but the readout fails to bind it to the correct answer option. Introduces MODIRECT (dataset family) and DeltaDirect (projector-level motion vector supervision) — improves accuracy from 25.9% to 85.4% on synthetic benchmarks."
tags: [arxiv-2026, video-llms, motion-perception, mechanistic-analysis, evaluation, bounded-representation-capacity, paper-2605-22823]
sources: https://arxiv.org/abs/2605.22823
status: active
confidence: 0.85
---

# Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs (Lee, Lee, Kim, Kim, Chung, Choi — Kyung Hee University / Princeton, May 2026)

**arXiv:** 2605.22823 | **Code:** https://github.com/KHU-VLL/DeltaDirect

## The Problem

Video-LLMs have made rapid progress on temporal video understanding — memory, action recognition, event ordering, long-form reasoning. Yet they fail at a basic perceptual primitive that humans solve instantly and effortlessly: **signed image-plane motion direction**. Given a simple synthetic video of a single object moving left, right, up, or down, most Video-LLMs perform near random chance (25%). The paper calls this **directional motion blindness** and systematically traces where in the pipeline the failure arises.

This is a basic sanity check for video understanding: if a system cannot tell which direction a single moving object travels, what does "video understanding" even mean? The problem is compounded because motion direction is a primitive from which all higher-order motion perception (speed, trajectory, interaction) is built.

## The Core Idea / Method

The paper's contribution is threefold: **diagnosis**, **benchmark**, and **intervention**.

### Diagnosis: the direction binding gap

The authors trace motion direction information through the LLaVA-Video-7B pipeline:

1. **Vision encoder** — linear probe achieves **99.8%** accuracy. The raw visual encoder carries a near-perfect direction signal.
2. **Projector** — linear probe achieves **96.5%**. The vision-language projection does not erase direction.
3. **LLM visual-token states** — linear probe achieves **98.1%**. Direction remains accessible inside the LLM.
4. **LLM readout token** — linear probe achieves **95.3%**. Even the final readout token carries direction.
5. **Multiple-choice QA** — model achieves only **27.6%** (near 25% chance).

**The direction binding gap**: motion direction information is linearly accessible throughout the entire pipeline, but the readout token fails to bind this signal to the prompt-specific answer option. This is not a perceptual failure — it's a readout failure. The same gap persists across architectures (LLaVA-OneVision, VideoChat2, mPLUG-Owl3, VideoLLaMA3, InternVL, Qwen2.5-VL, LLaVA-NeXT) and scales, indicating a shared structural limitation.

Crucially, input-side scaffolds (visual boundary cues, step-by-step location reasoning, coordinate-grid prompts) barely help — best combination reaches only 34.7%. The failure is internal.

### MODIRECT: a controlled dataset family

The paper introduces **MODIRECT** with three subsets:

- **MODIRECT-INST** (100K synthetic training videos) — Primitive-on-Syn domain, diverse QA formats (direction MCQ, open-ended direction, static appearance questions to preserve general recognition)
- **MODIRECT-SYNBENCH** (controlled synthetic evaluation) — 2×2 design over foreground type (Primitive vs. Cutout) and background type (Syn vs. Real): Primitive-on-Syn, Cutout-on-Syn, Primitive-on-Real, Cutout-on-Real
- **MODIRECT-REALBENCH** (real-world evaluation) — curated from Something-Something-v2, TOMATO, KTH

Each video has a single foreground object in one of four signed directions, with randomized start/end positions and answer-option orders to prevent shortcut learning.

### Instruction tuning: what it solves and what it doesn't

Fine-tuning on MODIRECT-INST (Primitive-on-Syn only) substantially improves source-domain accuracy but degrades on more complex domains (especially Cutout-on-Real). Using **difference-in-means concept vectors**, the authors discover that the model learns the *geometry* of motion direction representations (cross-domain cosine similarity is high after tuning), but the *magnitude* of the motion direction concept vector drops sharply on complex domains. Restoring only the magnitude recovers much of the lost accuracy — the problem is a **magnitude deficit**, not a missing representation.

### DeltaDirect: projector-level motion vector supervision

This diagnosis motivates **DeltaDirect**, a training-only auxiliary objective:

- During training, predict normalized 2-D motion vectors from adjacent-frame projector-feature deltas
- The auxiliary branch is **discarded after training** — test-time input format, token sequence, architecture, and decoding are unchanged
- This strengthens the signed displacement signal at the visual-language interface before it enters the LLM

## Results

| Setting | Vanilla | +Instr. Tuning | +DeltaDirect |
|---|---|---|---|
| **MODIRECT-SYNBENCH avg** (synthetic) | 25.9% | 78.9% | **85.4%** |
| — Primitive-on-Syn (source domain) | ~chance | ~90% | ~93% |
| — Cutout-on-Real (hardest OOD) | ~chance | ~70% | ~81% (+11.2pp) |
| **MODIRECT-REALBENCH** (real-world, no real tuning data) | — | — | **+21.9pp** over vanilla baseline |
| **General video benchmarks** (MVBench, NExT-QA, Perception Test, EgoSchema, TGIF-QA, TempCompass, VinoGround, FAVOR-Bench, MotionBench) | — | — | **Preserved or improved** — positive transfer, not overfitting |

The key result: DeltaDirect improves real-world motion direction accuracy by 21.9 points **without seeing any real-world videos during tuning**, while preserving or improving general video understanding. When applied during full fine-tuning, DeltaDirect alone yields strong improvements on both motion direction and general video benchmarks, suggesting motion-vector supervision can serve as a useful general training signal.

## Why It Matters

This paper demonstrates that **perceptual primitives are not automatically learned by multimodal architectures**, even when the information is present in the representations. The direction binding gap is a specific, diagnosable, and fixable failure — but fixing it required understanding *where* the bottleneck was (readout binding) and *what kind* of failure it was (magnitude deficit, not missing representation).

For the **bounded-representation-capacity** thread: the model has the capacity to represent motion direction but cannot reliably route this signal to the output. This is a **readout bottleneck** — a bounded capacity to *use* an available representation. The DeltaDirect intervention (strengthening the signal at the projector) shows that routing capacity can be improved by architectural supervision without changing the core architecture.

For **evaluation infrastructure**: the paper's methodology — controlled synthetic diagnosis → intervention → real-world transfer — is a model for how to isolate and fix a specific perceptual primitive. The MODIRECT dataset family provides a controlled testbed for motion direction understanding that disentangles genuine perception from prediction biases.

## Limitations

- **Only tested at single-object, simple-motion scenarios** — real-world video motion direction is entangled with camera motion, occlusion, multiple objects, scale changes, and event semantics. Whether DeltaDirect transfers to multi-object, complex-motion settings is open.
- **LLaVA-Video-7B as primary testbed** — though the binding gap was validated across architectures, the DeltaDirect intervention was only tested on LLaVA-Video. Replication on other backbones would strengthen confidence.
- **8-frame sampling** — the standard 8-frame video input may limit temporal resolution. With higher frame rates, the direction task becomes easier, and the gap may narrow naturally.
- **Synthetic-to-real transfer relies on projector-level signal strengthening** — this may not fix binding gaps for other perceptual primitives (speed, acceleration, trajectory) that don't reduce to simple 2-D displacement.
- **No analysis of why the binding gap exists at the mechanistic level** — concept vector analysis identifies the magnitude deficit but doesn't explain why readout tokens fail to route the signal to the correct vocabulary distribution.

## Connections to Wiki

### Wiki concepts
- [[bounded-representation-capacity]] — The model has the capacity to represent motion direction (linear probes show it) but cannot reliably route it to output. This is a readout-capacity bound, not a representation-capacity bound.
- [[evaluation-infrastructure]] — MODIRECT's controlled 2×2 design (foreground type × background type) is a reference-quality diagnostic benchmark for a single perceptual primitive.
- [[mechanistic-interpretability]] — Concept vector analysis (difference-in-means) localizes the failure to a magnitude deficit in the readout. This is a clean application of MI to a specific perceptual failure.
- [[faithfulness]] — Directional motion blindness is a faithfulness failure: the model knows the direction (decodable) but doesn't say it (readout fails). Structural parallel to Faithful Confidence's finding that LRMs know more than they say.
- [[video-llms]] — Core subject. The paper shows that current Video-LLMs share a structural limitation in motion direction binding.
- [[agent-trust]] — A system that can't reliably report basic motion direction cannot be trusted for downstream tasks that depend on spatial-temporal reasoning.

### Related papers (wiki)
- [[arxiv-2605-30343-reasoning-in-memory-rim]] — RiM also diagnoses a routing bottleneck (intermediate reasoning steps are invisible). Both papers find that the model encodes information it cannot reliably output, but through different mechanisms (latent memory vs. readout binding).
- [[faithful-confidence-lrm-2026]] — FC finds a similar pattern: LRMs encode intrinsic confidence that is not faithfully verbalized. Both failures are *readout-level*, not *representation-level*.
- [[sleep-self-modify-consolidate-2026]] — Sleep's consolidation failure (knowledge in context never makes it to parameters) is structurally analogous to direction binding (direction in representations never makes it to output). Both are routing bottlenecks between representation and action.
- [[forecasting-scientific-progress-ai-2026]] — CUSP found models misestimate their own scientific reasoning reliability. This paper finds models overestimate their own perceptual capabilities.
- [[hll-humanitys-last-line-verification-2026]] — HLL's verification bottleneck applies here: a verifier that checks video-LLM outputs would need access to internal representations, not just final text, to catch directional motion blindness.

### Thread Cross-Cuts
The **readout bottleneck** identified here is a new variant of the bounded-self-model's **introspection axis**: the model cannot introspect on (and therefore cannot correct) its own motion direction representation. The paper's key insight — that signal magnitude at the readout, not signal presence in the representation, is the bottleneck — suggests a general failure mode: bounded models may encode accurate world state but fail at the *last-mile routing* to output. This may be a general property of deep architectures with compressed readout paths.

## Key Quote

> "Motion direction remains linearly accessible from the vision encoder, projector, and LLM hidden states, but the readout fails to bind this signal to the correct verbal answer option, revealing a direction binding gap."

## What To Watch

- **Generalization of the binding gap** — this may not be specific to motion direction. Other perceptual primitives (speed, depth, relative position) may exhibit similar signal-present/readout-failing patterns.
- **DeltaDirect as a general training signal** — motion vector supervision at the projector could be a plug-in improvement for any Video-LLM, similar to how contrastive learning improved vision encoders.
- **Security implications** — perceptual failures that users cannot detect (the model sounds fluent but doesn't understand basic motion direction) create a trust asymmetry.
- **Multi-object and complex-motion extension** — real-world deployment requires handling occluded/tracked objects, camera motion, and multi-object trajectories.
- **Connection to agent systems** — an agent navigating a visual environment that can't reliably report motion direction would make catastrophic navigation errors.