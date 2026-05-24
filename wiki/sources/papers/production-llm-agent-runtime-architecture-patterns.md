---
type: paper
summary: A methodology for composing production LLM agent runtime architectures — treating the LLM/software boundary as a first-class design concern
tags: [paper, arxiv, llm-agents, agent-architecture, production-systems]
sources: https://arxiv.org/abs/2605.20173
confidence: 0.8
---

# A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents

## Paper Info
- Authors: Vasundra Srinivasan
- arxiv: 2605.20173
- Published: 2026-05-19
- Categories: cs.AI, cs.SE

## Summary

Production LLM agents operate at the boundary between stochastic model outputs and deterministic software systems. Yet this boundary — how the LLM's outputs are interpreted, constrained, and piped back into the world — is rarely treated as a first-class architectural concern. This paper proposes a systematic methodology for selecting and composing runtime architecture patterns for production LLM agents.

The key insight is that production agent failures (hallucinations, tool misuse, state corruption, non-termination) often don't stem from the model itself but from how the model's outputs are routed, validated, and acted upon. The paper catalogs recurring failure modes and maps them to specific architectural patterns — including guardrail layers, confirmation gates, state machines, and replay buffers.

## Key Findings

- Production LLM agent failures are disproportionately caused by runtime architecture deficiencies, not model capability gaps
- The LLM/software boundary requires its own design methodology, distinct from model selection or prompt engineering
- Recurring runtime patterns can be systematically composed to address specific failure modes
- The methodology provides a decision framework for selecting patterns based on agent task requirements and risk tolerance

## Relevance to Our Work

The [[production-stage-architecture]] synthesis already identifies the production boundary as the locus of self-direction failures. This paper provides an empirical and methodological grounding for that observation — confirming that the boundary between LLM and deterministic software is genuinely under-engineered. The pattern catalog would be valuable input for the [[llm-agent-architecture]] concept page.

Connects to: [[chain-of-thought]] (as a runtime reasoning pattern), [[load-bearing-reasoning]] (the boundary as load-bearing), [[waldis-instructions-shape-language-2026]] (how instructions structure production behavior).

## Connections
- [[llm-agent-architecture]]
- [[production-stage-architecture]]
- [[load-bearing-reasoning]]
- [[chain-of-thought]]