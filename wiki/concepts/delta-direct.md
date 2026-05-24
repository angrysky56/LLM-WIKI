---
created: 2026-06-17
updated: 2026-06-17
type: concept
summary: DeltaDirect — directional motion blindness in Video-LLMs (deltadirect-directional-motion-blindness-video-llms-2026)
tags: [video-llm, motion-understanding, vision-language-alignment, alignment-failure]
sources: https://arxiv.org/abs/deltadirect
status: reference
confidence: 0.8
---

# DeltaDirect

**DeltaDirect** (directional motion blindness) is a failure mode identified in Video-LLMs where models fail to represent directional motion direction — the distinction between an object moving left-to-right versus right-to-left. The phenomenon is documented in the DeltaDirect paper (2026).

## Key Findings

- Video-LLMs exhibit systematic blindness to motion direction despite training on directional motion data
- The failure is attributed to spatial attention bias where semantic content dominates over temporal dynamics
- Probing analysis reveals linear representation collapse along the motion direction axis

## Connections

- [[video-llm]] — the system class this failure appears in
- [[motion-understanding]] — the capability dimension affected
- [[vision-language-alignment]] — the alignment problem this exposes
- [[probing-analysis]] — the diagnostic technique used to identify it
- [[deltadirect-directional-motion-blindness-video-llms-2026]] — the primary source paper

## Notes

This is a stub concept page referencing the DeltaDirect directional motion blindness paper. The stub exists to anchor wikilinks from concept pages that reference this research finding.