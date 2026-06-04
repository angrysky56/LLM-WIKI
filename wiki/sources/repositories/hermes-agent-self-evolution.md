---
summary: NousResearch/hermes-agent-self-evolution — DSPy + GEPA evolutionary self-improvement for Hermes Agent skills. Phase 1 (skill files) shipping, Phases 2-5 planned (tool descs, prompts, code, continuous loop). ~$2-10/run, MIT.
tags: [source, hermes-agent, dspy, gepa, self-improvement, prompt-evolution, repository]
updated: 2026-06-04T12:35:00Z
created: 2026-06-04T12:35:00Z
---

---
created: 2026-06-04T00:00:00Z
updated: 2026-06-04T00:00:00Z
type: source
summary: "NousResearch/hermes-agent-self-evolution — DSPy + GEPA-based evolutionary self-improvement for Hermes Agent. Phase 1 (skill files) is shipped; later phases target tool descriptions, system prompts, and code. ~$2-10/run via API, no GPU. MIT licensed."
tags: [source, hermes-agent, dspy, gepa, self-improvement, prompt-evolution, repository]
sources: https://github.com/NousResearch/hermes-agent-self-evolution
status: active
confidence: 0.95
---

# hermes-agent-self-evolution

Evolutionary self-improvement toolkit for [[hermes-agent]] using [[dspy|DSPy]] + [[gepa|GEPA]] (Genetic-Pareto Prompt Evolution). Optimizes skills, tool descriptions, system prompts, and (eventually) tool code via reflective evolutionary search over execution traces. No GPU training required — pure API calls, ~$2-10 per optimization run.

## How it works

The optimizer reads execution traces to understand *why* things fail (not just that they failed), then proposes targeted textual mutations. The pipeline:

```
current skill/prompt/tool ──► generate eval dataset
                                       │
                                       ▼
                                GEPA optimizer ◄── execution traces
                                       │                    ▲
                                       ▼                    │
                                candidate variants ──► evaluate
                                       │
                                constraint gates (tests, size, benchmarks)
                                       │
                                       ▼
                                best variant ──► PR against hermes-agent
```

GEPA is the ICLR 2026 Oral prompt-evolution paper; the integration is MIT licensed.

## Phased plan

| Phase | Target | Engine | Status |
|-------|--------|--------|--------|
| 1 | Skill files (`SKILL.md`) | DSPy + GEPA | ✅ Implemented |
| 2 | Tool descriptions | DSPy + GEPA | 🔲 Planned |
| 3 | System prompt sections | DSPy + GEPA | 🔲 Planned |
| 4 | Tool implementation code | Darwinian Evolver | 🔲 Planned |
| 5 | Continuous improvement loop | Automated pipeline | 🔲 Planned |

Engines used:
- **DSPy + GEPA** — reflective prompt evolution over execution traces (MIT)
- **Darwinian Evolver** — git-based code evolution, AGPL v3 (called as external CLI)

## Quick start

```bash
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"
export HERMES_AGENT_REPO=~/.hermes/hermes-agent

# Synthetic eval data
python -m evolution.skills.evolve_skill --skill github-code-review --iterations 10 --eval-source synthetic

# Or real session history from Claude Code / Copilot / Hermes
python -m evolution.skills.evolve_skill --skill github-code-review --iterations 10 --eval-source sessiondb
```

## Guardrails (must pass for every variant)

1. **Full test suite** — `pytest tests/ -q` 100% pass
2. **Size limits** — Skills ≤ 15KB, tool descriptions ≤ 500 chars
3. **Caching compatibility** — no mid-conversation mutations
4. **Semantic preservation** — purpose must not drift
5. **PR review** — all changes via human review, never direct commit

## Why it matters for this vault

This is *self-hostable* agent improvement. Skills in this vault ([[hermes-agent]], [[ingest]], [[librarian]], [[researcher]], [[news]], [[arxiv]], [[insights]]) are the kind of artifact this tool is designed to evolve. Phase 1 already supports iterating any of them by name.

## Connections

- [[hermes-agent]] — the tool that ships these optimizations
- [[dspy]] — declarative LM program framework
- [[gepa]] — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)
- [[entities/projects/darwinian-evolver]] — code-evolution engine used in Phase 4
- [[concepts/prompt-evolution]] — the underlying technique
- [[concepts/agent-self-improvement]] — broader category

## Caveats

- Only Phase 1 is shipping; Phases 2-5 are roadmap, not implemented.
- "Real session history" eval source requires a session DB with the right shape — verify before relying on it.
- Guardrail #1 (full test suite) is the strongest constraint; skills without tests will fail to evolve.
