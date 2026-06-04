---
created: 2026-06-03
updated: 2026-06-25
type: concept
summary: Large language models extended to process and reason about video input — temporal understanding, motion perception, and visual-language integration at video scale
tags: [video-llm, vision-language, temporal-reasoning, multimodal]
sources: [https://arxiv.org/abs/2605.22823]
status: active
confidence: 0.8
---

# Video LLM

A Video LLM is a large language model that has been extended to process video input — sequences of frames with temporal structure — and generate text outputs (descriptions, answers, actions) based on both visual and temporal understanding.

## Architecture

Video-LLMs follow a pipeline architecture:

1. **Vision encoder**: Processes individual frames (typically a frozen image encoder like ViT or CLIP)
2. **Projector**: Maps vision encoder outputs to LLM input space
3. **LLM**: Receives visual tokens + text tokens, generates text outputs
4. **Temporal modeling**: How the system handles motion, change, and time (often implicit in how frame sequences are processed)

The key architectural challenge is that the projector must preserve temporal information from video frames so that the LLM can reason about motion and change.

## The Direction Binding Gap Problem

The DeltaDirect paper (arXiv:2605.22823) discovered a striking failure mode: state-of-the-art Video-LLMs perform at near-random chance (~25%) on the elementary task of identifying **signed motion direction** (which way an object is moving: left/right/up/down), despite near-perfect performance on object color and appearance recognition.

Key finding: motion direction information is **linearly decodable** at every stage of the pipeline (vision encoder: 99.8%, projector: 96.5%, LLM hidden states: 98.1%), yet the final answer is near-chance. The failure is at the **readout-to-verbal-binding** step — the model fails to connect the available motion signal to the correct answer option.

This is called the **direction binding gap**: the signal exists but isn't bound to the response.

## DeltaDirect Solution

The paper introduces DeltaDirect, a projector-level auxiliary training objective that:

- Predicts normalized 2-D motion vectors from adjacent-frame projector-feature deltas
- Uses analytically available motion vectors from synthetic videos as supervision
- Strengthens signed displacement cues at the visual-language interface before they enter the LLM
- Is discarded at inference time (no test-time change to model or decoding)

Results:
- Motion direction accuracy: 25.9% → 85.4% on synthetic benchmarks
- +21.9 percentage points on real-world benchmarks (zero-shot)
- No degradation on standard video-understanding benchmarks

## The Magnitude Deficit

An important finding: the out-of-domain failure (e.g., primitive shapes on synthetic backgrounds → cutout objects on real backgrounds) is **not** a missing geometry. After instruction tuning, concept vectors (motion direction representations) have high alignment across domains (cosine similarity). But on harder domains, their **magnitude drops sharply**.

Restoring just the magnitude recovers much of the lost accuracy. This is the **magnitude deficit**: the model learns what "rightward" looks like but the signal is too weak to read out reliably in new domains.

## Zero-Shot Transfer from Synthetic Supervision

A notable result: synthetic-only training (on simple geometric primitives) transfers to real-world videos (+21.9pp on real benchmarks without real-world training data). This suggests the motion-direction geometry is generalizable when representation strength is preserved.

## Key Architectural Insights

1. **The interface (projector) is the bottleneck, not the encoder or LLM.** Vision encoders preserve direction nearly perfectly. Projectors preserve it well. LLMs internally decode it. The failure is at the readout-to-verbal-binding step.

2. **Projector-level intervention is sufficient.** DeltaDirect doesn't touch the vision encoder or LLM — only the projector training objective. The visual-language interface is where directional motion signals need strengthening.

3. **Synthetic instruction tuning teaches geometry, not amplitude.** Models learn the structure of motion direction but the signal weakens in new domains. Fixing magnitude recovers performance.

## Connections
- [[wiki/index]]
- [[concepts/vision-language-alignment]]
- [[concepts/video-llm]]
- [[concepts/motion-understanding]]
- [[concepts/maximum-occupancy-principle]]
- [[log]]
- [[concepts/video-llm]]

- [[vision-language-alignment]] — alignment between visual and language representations
- [[motion-understanding]] — temporal dynamics and motion perception
- [[delta-direct]] — the specific paper with directional motion blindness findings
- [[probing-analysis]] — linear probing as diagnostic technique for representation analysis
- [[concepts/maximum-occupancy-principle]] — the readout token as a binding bottleneck (MOP analogy)

## Open Questions

1. **Other binding gaps**: Direction binding is one failure mode. What other elementary visual features (speed, depth, occlusion direction) have similar decoupled patterns?
2. **General projector training**: Can the DeltaDirect auxiliary objective be generalized to other motion understanding tasks beyond directional motion?
3. **Magnitude restoration**: What training or architectural changes prevent magnitude collapse in out-of-domain settings?
4. **Video-LLM scaling**: How do motion understanding capabilities scale with model size and training data? Are frontier models already solving this?