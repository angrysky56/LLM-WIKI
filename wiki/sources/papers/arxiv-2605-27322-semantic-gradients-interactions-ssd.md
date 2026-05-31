---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "Interaction SSD extends Supervised Semantic Differential to model how semantic meaning varies across moderator groups (e.g., annotator racial identity moderating hate-speech judgments)"
tags: [paper, arxiv, nlp, hate-speech, semantic-differential, moderation]
---

# Semantic Gradients Interactions in SSD: A Case Study in Racial Identity and Hate Speech

**Paper:** [arXiv:2605.27322](https://arxiv.org/abs/2605.27322)
**Authors:** Felix Ostrowicki (Independent Researcher), Hubert Plisiecki (IDEAS Research Institute)

## Overview

Introduces **interaction SSD**, an extension of Supervised Semantic Differential (SSD) that models how semantic meaning varies across moderators (groups, traits, conditions), making this variation testable and interpretable.

## Method

The model estimates:
- A **main semantic gradient** (overall structure)
- An **interaction gradient** (how the gradient differs across groups)
- **Conditional gradients** at substantively meaningful moderator values

All interpretable through standard SSD tools (nearest-neighbor retrieval, clustering, representative text snippets).

## Application

Tested on UC Berkeley Measuring Hate Speech corpus to examine whether annotator racial identity moderates hate-speech judgments of comments targeting people of color.

## Key Finding

The interaction model detects a significant moderation effect:
- Shared gradient contrasts dehumanizing hostility with counter-speech
- Interaction gradient reveals smaller group-linked differences in which semantic cues predict hate-speech ratings

## Tags
- semantic-differential
- hate-speech-detection
- moderation
- interpretability
- interaction-effects