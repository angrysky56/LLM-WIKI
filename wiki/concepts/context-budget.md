---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: Token-ceiling utility that caps returned text at a hard limit to prevent oversized tool responses from blowing agent context; the central scaling bottleneck for any agentic knowledge management system
tags: [context-management, llm, infrastructure, response-budgeting, agent-architecture]
sources: [https://docs.anthropic.com (response_budget pattern)]
status: active
confidence: 0.8
---

# Context Budget

A token-ceiling utility that caps LLM tool responses at a hard character limit (e.g., `MAX_RESPONSE_CHARS = 4000` ≈ 1000 tokens) with clean spillover truncation. Prevents oversized responses from flooding agent context — the central scaling bottleneck for any agentic knowledge management system.

## Pattern

The `response_budget.py` pattern used in [[entities/projects/project-synapse]] implements the pattern: a utility that accepts a response string and a ceiling, and returns either the full response if under the ceiling or a truncated prefix with a continuation marker if over. This is distinct from semantic summarization — it's purely a structural budget cap.

## Why it matters

When an agent queries a large vault (1,200+ pages), naive aggregation of results can produce multi-thousand-token tool responses that consume most of the context window before the agent can act. Context budgeting forces the pipeline to truncate at a known-safe boundary, preserving space for agent reasoning.

## Connections

- [[entities/projects/project-synapse]] — implements context budgeting in `response_budget.py`
- [[concepts/context-window]] — the resource being budgeted
- [[wiki/sources/articles/synapse-wiki-scaling-walkthrough]] — source page