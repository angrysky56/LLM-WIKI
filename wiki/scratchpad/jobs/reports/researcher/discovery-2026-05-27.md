# Researcher Discovery Report — 2026-05-27

## Discovery Cycle
- Topics researched: 1 (schema competition)
- New pages created: 1
- Pages updated: 1 (researcher carryover)
- Cross-links added: 6 (to ramirez-ruiz-mop-2024, mop-architecture, bounded-structured-memory, domain-curator, knowledge-pack, meta-harness)

## New Entries

### `wiki/concepts/schema-competition.md`
Created full concept page for schema competition in the meta-harness Knowledge Pack context.

**Definition**: Schema competition is the phenomenon where multiple, potentially conflicting schema representations within a Knowledge Pack simultaneously vie for a language model's behavioral attention during inference — with no built-in arbitration mechanism to resolve which representation dominates when they disagree.

**Key content**:
- How `build_pack_context()` in `bootstrap_domain.py` concatenates competing layers (distinguishers → heuristics → failure modes → invariants → examples) without explicit priority
- Four mechanisms of competition: prompt position effects, confidence weight ambiguity, example override, failure mode catalog as counter-incentive
- Relationship to [[ramirez-ruiz-mop-2024]] MOP research (which explicitly identified schema competition as an open question)
- Five mitigation strategies (priority markers, thresholded rules, explicit layer confidence, conflict documentation, verifier detection)
- Five open questions specific to meta-harness context

**Connections**: ramirez-ruiz-mop-2024 (open question source), mop-architecture, bounded-structured-memory (Hermes layer analogy), domain-curator (Phase 1 curation), knowledge-pack (the artifact), meta-harness (the system)

## Updated Entries
- `wiki/scratchpad/agent-sheets/researcher/carryover.md` — marked schema competition as resolved, removed kanban block note, updated stub count notation

## Gap Analysis
- Schema competition (t_7c84f292915e48b8): **RESOLVED** — concept page created, kanban task unblocked
- MOP vs fine-tuning boundary: still open — empirical question about GRPO for MoE, needs web research
- agentic-react concept gap: low priority, coverage adequate via skill — no action needed

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-27]]

- [[discovery-2026-05-27]]

## Open Questions
1. Is prompt position a reliable priority mechanism for Pack layers, or is structural priority encoding needed?
2. Should the Pack schema encode explicit priority edges between layers?
3. Does schema competition interact with model scale (smaller models more susceptible)?
4. Does Phase 2 (architecture) ever need to address schema competition, or is it purely a knowledge-layer problem?
5. Can the VerifierGraphEvaluator detect schema competition at evaluation time via DAG tracing?