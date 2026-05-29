# arxiv papers — 2026-05-23 researched

---
### 2605.22823 — DeltaDirect: Directional Motion Blindness in Video-LLMs
**Single paragraph:** Video-LLMs suffer from "directional motion blindness" — near-random accuracy on identifying which direction (left/right/up/down) an object moves despite near-perfect appearance recognition. The failure is not perceptual but a "direction binding gap": motion direction is linearly decodable from internal states (99.8% probe accuracy) but fails to be correctly bound to verbal answer options. DeltaDirect introduces a projector-level auxiliary objective predicting 2D motion vectors from adjacent-frame feature deltas, improving accuracy from 25.9% to 85.4% on synthetic benchmarks and +21.9pp zero-shot on real-world video without real-world training data. Key structural finding: out-of-domain failure is a magnitude deficit (concept vector magnitude drops) not a geometry loss (alignment is preserved), and restoring magnitude recovers performance.

**One key finding:** The direction binding gap is a readout-level failure, not an encoder or projector failure — and the fix is a training-only auxiliary objective at the projector that strengthens signed displacement signals before they enter the LLM, without any inference-time overhead.

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/arxiv/papers-2026-05-23-researched]]

- [[papers-2026-05-23-researched]]
