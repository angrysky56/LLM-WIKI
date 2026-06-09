---
created: 2026-06-03
updated: 2026-06-25
type: concept
summary: Understanding motion and temporal dynamics in visual data — the elementary primitives of motion, direction binding, and the magnitude deficit problem in visual reasoning
tags: [motion-understanding, temporal-reasoning, video-understanding, computer-vision]
sources: [https://arxiv.org/abs/2605.22823]
status: active
confidence: 0.8
---

# Motion Understanding

Motion understanding is the capability to perceive, track, and reason about how objects move over time. In visual AI, it is one of the most challenging capabilities — despite excellent performance on static visual recognition (object type, color, texture), even state-of-the-art models fail on elementary motion tasks.

## The Elementary Motion Primitives

The DeltaDirect paper (arXiv:2605.22823) identifies **signed motion direction** as a fundamental motion primitive: determining which way (left/right/up/down) an object is moving in the image plane. This is a simpler question than tracking, speed estimation, or 3D motion reconstruction — yet current Video-LLMs fail at near-random chance on it.

Other elementary motion primitives:
- **Object presence over time**: Is the object in frame at time T vs T+n?
- **Motion existence**: Is there motion at all? (binary)
- **Motion direction**: Which way? (the DeltaDirect focus)
- **Motion speed**: How fast? (quantitative or qualitative)
- **Trajectory shape**: Straight, curved, oscillatory?

## Directional Motion Blindness

The key finding from DeltaDirect: despite near-perfect appearance recognition, Video-LLMs are at **near-random chance (~25%)** on signed motion direction. The model can identify what the object is (color, shape, type) but cannot tell which direction it's moving.

Critically, this is **not** a perception failure. Using linear probing on model hidden states:

| Stage | Direction Probe Accuracy |
|-------|--------------------------|
| Vision encoder output | 99.8% |
| Projector output | 96.5% |
| LLM hidden states (visual tokens) | 98.1% |
| Final readout token | 95.3% |
| Actual MCQ accuracy | ~25% |

The signal is present throughout the pipeline — the model sees the motion. The failure is at the **binding** step: connecting the motion signal to the correct verbal answer option.

## The Direction Binding Gap

The gap between decodable representations (95%+ probe accuracy) and poor task performance (25%) is the **direction binding gap**. The model has the information but fails to use it for the task.

This is a cross-modal binding problem: motion information must be bound to language (the answer choices: "left", "right", "up", "down"). The binding fails even though both representations are individually strong.

## The Magnitude Deficit

The OOD failure pattern (from simple synthetic training to complex real-world) reveals a specific mechanism:

1. After instruction tuning, motion direction concept vectors have **high alignment** across domains (high cosine similarity) — the model learns what "rightward" means
2. On harder domains (cutout objects on real backgrounds), the **magnitude of the representation drops sharply** — the signal weakens
3. **Restoring just the magnitude** recovers much of the lost accuracy

This is the **magnitude deficit**: the model learns the geometry of motion direction but the signal is too weak to read out reliably in new settings. It's not a structural failure (the geometry is right) but an intensity failure (the signal is too weak).

## Projector-Level Intervention

DeltaDirect's solution targets the projector (vision-language interface):

- **DeltaDirect auxiliary objective**: Predict 2D motion vectors from adjacent-frame projector feature deltas
- **Training only**: The auxiliary head is discarded at inference — no test-time change
- **Result**: Motion direction accuracy 25.9% → 85.4% on synthetic, +21.9pp zero-shot on real

The intervention is at the projector level because that's where the direction signal is processed before entering the LLM. Strengthening the signal at that interface improves binding.

## Connection to EFHF Architecture

The [[entities/projects/efhf]] layered architecture (sensory → projection → LLM) mirrors the identified breakdown point:

- Sensory layer: Vision encoder — preserves motion nearly perfectly
- Projection layer: Projector — well, but can be improved with auxiliary objectives
- LLM layer: Processes visual tokens — internally decodes direction well
- Readout: Fails to bind direction to verbal answer

The **interface is the bottleneck**, not the underlying representations. This is the same pattern EFHF identifies for the LLM/software boundary in production agents: failures concentrate at the interface, not in the components.

## Connection to MOP

The readout token acts as a bottleneck for directional motion signals — analogous to **maximum occupancy** for information bandwidth. DeltaDirect effectively increases the effective bandwidth of motion-direction information through the projector interface.

## Connections
- [[concepts/video-llm]]
- [[concepts/motion-understanding]]
- [[wiki/index]]
- [[concepts/vision-language-alignment]]
- [[log]]
- [[concepts/motion-understanding]]

- [[video-llm]] — Video-LLMs as the system for motion understanding
- [[vision-language-alignment]] — the alignment problem that motion understanding exposes

- [[probing-analysis]] — linear probing as the diagnostic technique
- [[entities/projects/efhf]] — interface as the bottleneck, not the components

## Open Questions

1. **Other magnitude deficits**: What other capabilities have the property that geometry is learned but magnitude collapses OOD?
2. **General motion projector training**: Can DeltaDirect-style auxiliary objectives be generalized to other motion tasks (speed, depth, 3D motion)?
3. **Temporal resolution**: Do models need more frame-level temporal resolution to capture faster motions?
4. **Real-world magnitude restoration**: Can we prevent magnitude collapse in OOD settings without extensive real-world data?