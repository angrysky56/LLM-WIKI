---
updated: 2026-05-21T17:09:44Z
created: 2026-05-21T17:09:44Z
---

---
created: 2026-05-21
updated: 2026-05-21
type: source
summary: Autonomous LLM framework that runs the full research pipeline — literature review, experimentation, report writing — with human feedback at each stage.
tags: [llm-agents, autonomous-research, ai-for-science, agentic-ai]
sources: https://arxiv.org/abs/2501.04227
status: active
confidence: 0.9
---

# Agent Laboratory: Using LLM Agents as Research Assistants

**Authors:** Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum

**Submitted:** 8 Jan 2025 (v1), last revised 17 Jun 2025 (v2)
**Subjects:** Human-Computer Interaction, Artificial Intelligence, Computation and Language, Machine Learning (cs.HC, cs.AI, cs.CL, cs.LG)

## Core Insight

Agent Laboratory is the first fully autonomous end-to-end research pipeline — accept a research idea → run literature review → run experiments → write the paper — producing both a code repository and a research report. It achieves an **84% cost reduction** compared to prior autonomous research methods.

## Key Claims

| Claim | Evidence |
|-------|----------|
| o1-preview produces best research outcomes | Survey of multiple LLMs, human assessments |
| Generated ML code achieves SOTA performance | Benchmarked against existing methods |
| Human feedback at each stage significantly improves quality | Iterative evaluation with researchers |
| 84% cost reduction vs prior autonomous methods | Direct cost comparison |

## Architecture

Three-stage pipeline:
1. **Literature Review** — agent searches and synthesizes relevant prior work
2. **Experimentation** — agent writes and executes code, iterates on results
3. **Report Writing** — agent produces a full research paper

Human researchers provide feedback at each stage boundary, guiding the direction.

## Significance

The paper demonstrates that LLM agents can go from research idea to published-quality paper with minimal human input, primarily for cost reduction and acceleration. The 84% cost decrease is the most cited result — suggesting autonomous research could become economically viable at scale.

## Connections

- [[llm-agents]] — core capability
- [[autonomous-research]] — related research direction
- [[ai-for-science]] — domain of application

## Open Questions

- How does the framework handle novel/out-of-distribution research ideas vs. incremental improvements?
- The survey-based evaluation is small (n=?); how robust are the findings?
- Code quality: SOTA on what benchmarks, in what domains?
- What is the actual wall-clock time from idea → submitted paper?
