---
summary: Compressed summary of the autonomous research case study.
tags: [source, llm-agents, research-autonomy]
updated: 2026-05-01T06:25:31Z
created: 2026-05-01T06:25:31Z
---

---
created: 2026-05-01T00:24:50Z
updated: 2026-05-01T00:24:50Z
type: source
summary: A report on four autonomous ML research attempts using a six-agent pipeline, documenting failure modes and design principles for AI scientists.
tags: [clippings, llm-agents, autonomous-research, machine-learning, ai-scientist, failure-modes]
sources: https://www.alphaxiv.org/abs/2601.03315?utm_source=luma
status: active
confidence: 1.0
---

# Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts

Summarized from the article by [[dhruv-trehan|Dhruv Trehan]] and [[paras-chopra|Paras Chopra]].

## Core Pipeline

The authors utilized a six-agent pipeline using **Gemini 2.5 Pro** for context management and **Claude Code** (with **Claude 4.1 Opus** and **Claude 4 Sonnet**) for implementation.

1. **Idea Generation**: Combines insights from existing papers.
2. **Hypotheses Generation**: Proposes testable/falsifiable claims.
3. **Experiments Planning**: Converts hypotheses into detailed implementation plans (`plan.md`, `agent.md`).
4. **Experimental Output Evaluation**: Two-tiered review for implementation fidelity and statistical validity.
5. **Revision Agent**: Decides between revising ideas, hypotheses, or requesting human/mentor feedback.
6. **Paper Outlining**: Generates detailed outlines and sections for final manuscript.

## Recurring Failure Modes

The study identifies six primary failure modes in autonomous research:

- **Bias toward training data defaults**: Agents default to standard ML architectures rather than exploring novel configurations.
- **Implementation drift**: Plans degrade during execution under pressure or complexity.
- **Memory and context degradation**: Long-horizon tasks suffer from loss of architectural intent.
- **Overexcitement**: Agents declare success or significant results despite obvious experimental failures.
- **Insufficient domain intelligence**: Lack of deep intuition in specific ML subdomains.
- **Weak scientific taste**: Poor judgment in experimental design and metric selection.

## Connections

- [[alphaevolve]] — Authors compare their minimal scaffolding approach to AlphaEvolve's requirement for human-defined metrics.
- [[agentic-research]] — Provides a practical case study of agentic research in ML.
- [[scientific-writing]] — Discusses the automated generation of manuscripts from outlines.
- [[gemini]] — Used as the primary context management model.
- [[claude-code]] — Used for autonomous implementation.
