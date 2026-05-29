# Researcher Discovery Report — 2026-05-21

## Discovery Cycle
- Topics researched: 3
- New pages created: 3
- Pages updated: 0
- Cross-links added: 9 (conceptual via new pages)

## New Entries

### 1. [[inference-time-compute-scaling]]
**Test-time compute scaling** — the frontier axis of LLM capability beyond training compute. Covers:
- Best-of-N (BoN) sampling with reward model selection
- Process vs outcome reward models (PRM vs ORM)
- Key results: ELHSR, SD-Search, OpenDeepThink
- Diminishing returns curve and economic tradeoff
- Open questions: optimal budget allocation, PRM reliability, when to use dense vs scaled inference

*Why this matters*: The wiki had reward-modeling mentions and scattered references to "inference-time compute" but no coherent concept page synthesizing the field. This is now a first-class concept.

### 2. [[mixture-of-experts]]
**MoE architectures** — sparse conditional computation enabling massive parameters with fraction of per-token FLOPs. Covers:
- Definition: router + N experts, top-k activation
- Dense vs MoE tradeoff: memory same, compute lower
- Key systems: Mixtral 8x7B, Grok-1, DBRX
- Routing dynamics: load balancing, expert collapse, communication overhead
- Open questions: optimal expert count, fine-tuning MoE, integration with inference-time scaling

*Why this matters*: The wiki had no dedicated MoE concept page despite it being a core architectural variant in every frontier model (Mixtral, Grok, DBRX, Switch Transformers). The "scaling law" and "architectural developments" gaps are directly addressed.

### 3. [[process-reward-model]]
**Process Reward Models** — step-level scoring for precise credit assignment. Covers:
- PRM vs ORM: step-level vs trajectory-level scoring
- The credit assignment problem (why step granularity matters)
- Training approaches: human annotation, larger teacher, self-distillation
- SD-Search as the breakthrough: implicit PRM without external teacher
- Key result: 3B self-distilled matches 72B teacher, 7B surpasses it
- Open questions: PRM reliability, implicit vs explicit, domain transfer

*Why this matters*: The reward-modeling concept mentions PRM but doesn't explain it. The "reasoning and reasoning language models" focus area is directly served by this page. SD-Search is fresh (May 2026) and worth capturing.

## Gap Analysis

### Still thin or missing
1. **Constitutional AI / harm aversion training** — alignment technique from Anthropic; mentioned in one source paper but no concept page
2. **Reflection and self-correction architectures** — RAA, self-prompting patterns, metacognitive loops
3. **Verifier-graph theory** — Ty's own project; deserves concept page separate from the entity page
4. **MOP (Maximum Occupancy Path)** — mentioned in AGEM and synthesis docs; needs standalone concept
5. **Open-ended evolution in LMs** — connecting ALife work to language model diversity/capability
6. **Length generalization** — the problem of trained-on-short-test-on-long

### Emerging topics needing attention
- **Test-time compute scaling** is now a field (not just a concept) — worth a dedicated research thread
- **Self-distillation without teachers** (SD-Search pattern) — could inform EFHF Layer 0/1 design
- **Hybrid reward models** — combining hidden-state (ELHSR) with process-level (SD-Search)

## Open Questions

1. **Constitutional AI**: Should this be a standalone concept or folded into alignment? The concept differs from RLHF — principle-driven rather than example-driven. Flagging for Ty's decision.

2. **MoE fine-tuning**: The concept page notes MoE fine-tuning is hard but doesn't go deep. Is there existing work on this worth including, or should this be a research project?

3. **Verifier-graph**: The project entity exists but there's no concept page explaining the theory. Should this be synthesis or concept?

4. **Test-time compute economics**: The concept page is technically correct but doesn't address the deployment economics. Ty's use case (Hermes Agent) involves real-time inference — worth adding a section on "when inference-time scaling is and isn't worth it."

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-21]]
- [[wiki/index]]

- [[discovery-2026-05-21]]

## Cross-Links Added (Conceptual)

The new pages link to existing concepts:
- inference-time-compute-scaling → reward-modeling, hidden-states, chain-of-thought, load-bearing-reasoning
- mixture-of-experts → inference-time-compute-scaling, reward-modeling, scaling-law
- process-reward-model → reward-modeling, inference-time-compute-scaling, chain-of-thought, load-bearing-reasoning, hidden-states

The reverse links (back to these new pages from existing concepts) should be added by the librarian agent during next audit.

---

*Next run scheduled: Monday 2026-05-26 8:30AM*