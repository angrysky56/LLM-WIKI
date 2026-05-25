---
created: 2026-05-17
updated: 2026-05-29
type: concept
summary: The use of autonomous LLM agents to execute stages of the scientific research workflow, from idea generation to manuscript writing
tags: [agentic-research, ai-agents, scientific-research, automation]
sources: []
status: active
confidence: 0.8
---


# Agentic Research

**Agentic Research** refers to the paradigm of using autonomous AI agents to perform complex, multi-stage scientific research tasks. Unlike static automation, agentic systems use reasoning models to make decisions about experimental planning, implementation, and evaluation.

## Key Components

A typical agentic research pipeline involves specialized modules:
- **Ideation**: Synthesizing existing knowledge into new research directions.
- **Planning**: Converting abstract ideas into executable experimental steps.
- **Execution**: Writing and running code to test hypotheses (e.g., using [[claude-code]]).
- **Evaluation**: Critically reviewing experimental results for validity and significance.
- **Synthesis**: Compiling findings into a structured manuscript or technical report.

## Challenges and Failure Modes

As documented in [[why-llms-arent-scientists-yet]], current agentic research systems face significant hurdles:
- **Implementation Drift**: The execution diverging from the original research intent.
- **Context Degradation**: Loss of coherence across long-horizon research tasks.
- **Scientific Taste**: The difficulty of training agents to recognize high-value research directions over trivial ones.
- **Open-Ended Temporal Adaptation**: [[futuresim-adaptive-agents|FutureSim]] shows frontier agents score only 25% on real-world event forecasting; several perform worse than random guessing, indicating severe world-modelling gaps.

## Connections

- [[alphaevolve]] — An early framework for autonomous discovery.
- [[why-llms-arent-scientists-yet]] — A case study documenting failure modes in this field.
- [[momoa-researcher]] — A multi-agent research framework.
- [[gemini]] — Long-context model used for research orchestration.
- [[claude-code]] — Agentic tool used for autonomous implementation.
- [[is-grep-all-you-need]] — Grep vs. vector retrieval in agentic search; harness choice dominates retrieval choice across Claude Code, Codex, Gemini CLI.
- [[futuresim-adaptive-agents]] — Temporal world event simulation exposing severe agent adaptation gaps.
- Concept: [[agentic-design-picker]]
- Concept: [[ai-scientific-discovery]]
- Concept: [[autonomous-research]]
- Concept: [[code-agent]]
- Concept: [[efhf]]
- Concept: [[multi-agent-llm-systems]]
- Concept: [[recuriosity-episodic-context-3d-exploration-2026]]
- Concept: [[self-correction]]
- Concept: [[tools]]
- Concept: [[tys-repos]]

