---
type: paper
summary: Post-training VLMs with decoupled perception and reasoning modules improves visual task performance — challenging the long-CoT assumption
tags: [paper, arxiv, vlm, computer-vision, post-training, chain-of-thought]
sources: https://arxiv.org/abs/2605.20177
confidence: 0.8
---

# From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models

## Paper Info
- Authors: Juncheng Wu, Hardy Chen, Haoqin Tu
- arxiv: 2605.20177
- Published: 2026-05-19
- Categories: cs.CL, cs.CV

## Summary

Recent advances in vision-language models (VLMs) emphasize long chain-of-thought reasoning as a path to better visual understanding. This paper presents a counterintuitive finding: long CoT reasoning during post-training actually *hurts* VLM performance on visual tasks. The authors demonstrate that perception (visual feature extraction) and reasoning (the inferential chain over those features) have incompatible training dynamics — forcing them to share a training regime degrades both.

The proposed solution is a decoupling strategy: train the perception module and the reasoning module separately with task-specific objectives, then compose them at inference time. This allows each module to be optimized for its own function without interference. Results show significant improvements on standard VQA, visual reasoning, and spatial understanding benchmarks.

## Key Findings

- Long CoT during VLM post-training degrades visual task performance — a significant negative result
- Perception and reasoning have conflicting training dynamics; coupling them causes interference
- Decoupled training (separate modules, composed at inference) outperforms all coupled baselines
- The improvement is most pronounced on tasks requiring precise spatial reasoning and fine-grained visual discrimination

## Relevance to Our Work

The wiki's VLM research thread has been tracking chain-of-thought as a key reasoning pattern. This paper provides an important corrective: CoT is not unconditionally beneficial for VLMs. For our [[chain-of-thought]] concept page, this adds a nuanced boundary condition — CoT helps reasoning tasks but hurts perceptual ones. Also relevant to [[titans]] research (test-time memory), as the decoupling mechanism has implications for how VLMs should allocate compute at inference time.

## Connections
- [[index]]
- [[sources/papers/decoupling-perception-reasoning-vlm-post-training]]
- [[decoupling-perception-reasoning-vlm-post-training]]
- [[chain-of-thought]]
- [[titans-test-time-memory]]
- [[vlm]]