---
summary: v0.5 — implementation-ready. Spike Campaign 001-004 complete; Layer 2 fully specified by four validated pillars. Includes detailed implementation plan in 7 phases.
tags: [synthesis, ai-scientist, agentic-research, seg, efhf, verification, design-v0.5, implementation-ready]
updated: 2026-05-03T09:05:34Z
---

---
created: 2026-05-01T08:15:00Z
updated: 2026-05-03T09:05:00Z
type: synthesis
summary: Integrated design for an autonomous AI scientist combining the SEG council (Layer 1) with the EFHF verification stack. v0.5 — empirical foundation complete; Layer 2 fully specified by four validated patterns from Spike Campaign 001-004.
tags: [synthesis, ai-scientist, agentic-research, seg, efhf, verification]
status: implementation-ready
confidence: 0.94
---

# SEG Scientist Agent — Design v0.5

> **Status:** v0.5 — Implementation-ready. [[spike-campaign-001-004-summary|Spike Campaign 001-004]] complete; all four pillars validated. Confidence ~0.94. The remaining unknowns are now empirical (does Layer 1 council outperform compute-matched solo?) rather than architectural.

## Architecture v0.5

```
                        GENERATION PHASE

Layer 1   SEG COUNCIL  (LLM substrate)
          Essentia Distiller         → intake, assumption mapping
          Rational Dreamer +
            Daydream Cartographer    → hypothesis generation
          Bayesian Sage +
            Comedic Trickster        → adversarial filter
                                        ↓
                                        ↓ (claim emitted, classified by type)
                                        ↓
                        VERIFICATION PHASE — bifurcated by claim regime

  ┌──── Layer 2 (HiPAI-Montague refactored) ─────────┐  ┌──── Layer 3 ────┐
  │                                                   │  │ [[mcp-logic]]   │
  │ ─ Pillar 1: Semantic Synthesis (spaCy) ─          │  │                 │
  │   Dep-parse, lemmatization, POS, morph            │  │ Reserved for    │
  │   .lemma_ as canonical form                       │  │ claims beyond   │
  │                                                   │  │ OWL2 SROIQ(D):  │
  │ ─ Pillar 2: Safety + Inference (owlready2) ─      │  │ • full FOL      │
  │   T1 axioms as EquivalentTo + AllDisjoint pairs   │  │ • quantifier    │
  │   sync_reasoner() infers types as byproduct       │  │   elimination   │
  │   of deontic pass                                 │  │ • counterexample│
  │                                                   │  │   search        │
  │ ─ Pillar 3: EBE Pipeline (World Isolation) ─      │  │                 │
  │   Transaction-per-claim semantics                 │  │ prove() — Pr9   │
  │   Snapshot to SQLite, fresh World per pass        │  │ find_counter — │
  │   Inference-under-Relaxation for blocking_axiom   │  │   Mace4         │
  │                                                   │  │ abductive_      │
  │ ─ Pillar 4: Read-Model Projection (Neo4j) ─       │  │   explain — VFE │
  │   One-way OWL→Neo4j, post-sync_reasoner only      │  │                 │
  │   .ancestors() walk for transitive type signal    │  │                 │
  │   Embedding-indexed semantic_search retained      │  │                 │
  │                                                   │  │                 │
  │ ─ Paraclete EBE chain ─                           │  │                 │
  │   check_action → calibrate_belief → escalate_block│  │                 │
  │   (now backed by Pillars 2 + 3)                   │  │                 │
  └─────────────────────────┬─────────────────────────┘  └────────┬────────┘
                            └──────────────┬──────────────────────┘
                                           ↓
Layer 4   META-COGNITIVE MONITORING  [[advanced-reasoning-mcp]]
          confidence near-binary for Layer-2-routed claims
                                           ↓
Layer 5   SHEAF CONSISTENCY          [[sheaf-consistency-enforcer]]
          ADMM cycle; L2/L3 disagreement on cross-regime claims still flags
                                           ↓
Layer 5+  ETHICAL TRIAGE  [[conscience-servitor]]

PROVENANCE & ORCHESTRATION (cross-cutting)
  ├─ [[verifier-graph]]      DAG provenance + reasoning hygiene
  ├─ [[project-synapse-mcp]] wiki + Neo4j retrieval, run artifacts
  └─ [[aseke-compass-mcp]]   Panksepp-lens behavioral monitoring of agent
```

## What v0.5 adds over v0.4

| Element | v0.4 | v0.5 |
|---|---|---|
| Layer 2 validation | architectural hypothesis | four spikes empirically validated |
| Relational typing | separate routing rule | byproduct of deontic pass (Spike 002) |
| Error recovery | "world rebuild on inconsistency" | transaction-per-claim via World Isolation (Spike 003) |
| Blocking-axiom extraction | "if reasoner surfaces it" | Relaxed-Sync Diagnostics (Spike 003) |
| Neo4j role | "side-rail of unspecified shape" | read-model projection, OWL→Neo4j one-way (Spike 004) |
| AllDisjoint requirement | not in design | mandatory build-skill pattern (Spike 002) |
| Confidence | 0.91 | 0.94 |

## Routing rule (claim-type → verification layer)

| Claim regime | Route | Why |
|---|---|---|
| `X is a Y` / `X has property P` / `All Y are P` ⊢ `X is P` | Layer 2 | Depth-1 subsumption — HermiT trivial |
| Transitive `X⊆Y, Y⊆Z, Z has P` ⊢ `X has P` | Layer 2 | Spike 001 validated |
| Class consistency / disjointness | Layer 2 | OWL2 native |
| Agent action toward MoralPatient (deontic) | Layer 2 | Spike 002 validated; types inferred as byproduct |
| Multi-claim batch with possible violations | Layer 2 | Spike 003 — Relaxed-Sync surfaces all in one pass |
| `For all x, ∃y, …` arbitrary FOL | Layer 3 | Beyond OWL2 |
| Counterexample existence for claim C | Layer 3 | Mace4 model finding |
| Crosses both regimes | Both, must align | L5 lumpability flag on disagreement |

## Implementation Plan

The refactor is now a focused engineering task. Estimated 1-2 days of work; sequenced for incremental verification.

### Phase A — Substrate (~4 hrs)

1. Add `spacy` and `owlready2` to HiPAI-Montague's pyproject.toml; install the `en_core_web_sm` model.
2. Create `world_model_owl.py` alongside the existing `world_model.py`. Both coexist during the migration.
3. Implement the `SnapshotReasoning` context manager — opens a fresh `World(filename=temp_sqlite)` per claim pass, commits or rolls back based on `OwlReadyInconsistentOntologyError`.

### Phase B — Parser refactor (~3 hrs)

4. Replace `synthesis.py` regex patterns 1-9 with spaCy dep-parse handlers. Each handler emits a typed tuple `(parse_kind, subject_lemma, predicate_lemma, object_lemma, modality)` rather than mutating a graph directly.
5. Mirror the existing `add_belief` / `evaluate_hypothesis` signatures so the MCP server interface is unchanged. Internal implementation routes through owlready2 instead of Cypher.

### Phase C — OWL ontology (~4 hrs)

6. Implement `add_belief` over owlready2: `class_membership` parses become individual class assertions; `universal_belief` parses become subclass + property axioms.
7. Implement `incorporate_axiom` over owlready2: T1 axioms become `EquivalentTo` restrictions plus mandatory paired `AllDisjoint` declarations.
8. Implement `evaluate_hypothesis` as `sync_reasoner()` + `isinstance(individual, target_class)`.

### Phase D — Paraclete gate (~3 hrs)

9. Refactor `check_action` to use the SnapshotReasoning context. Inside the snapshot, assert the proposed action; on success, return PERMITTED; on `OwlReadyInconsistentOntologyError`, return BLOCKED.
10. Refactor `calibrate_belief` to use Inference-under-Relaxation: destroy AllDisjoint gates, re-sync, read which RestrictedAction class the action was inferred to be.
11. `escalate_block` semantically unchanged.

### Phase E — Neo4j projection (~2 hrs)

12. Implement `project_to_neo4j(world)` — walks `world.individuals`, emits `MERGE (n:Individual {iri:...})` and `MERGE (n)-[:INFERRED_AS]->(c:Class)` for each ancestor in `individual.ancestors()`.
13. Wire projection as a post-step on every successful `sync_reasoner()` pass. Idempotency is essential — projection must produce no duplicate edges on repeated calls.
14. Existing embedding-based `semantic_search` continues to work unchanged; it's already Neo4j-side and the new projection only adds typed edges.

### Phase F — Tests + cutover (~3 hrs)

15. Port the existing 21 tests to the new substrate. Most should pass unchanged given the preserved API surface; the ones that asserted on internal Cypher structures will need rewrites.
16. Add new tests for the four pillars: transitive subsumption, AllDisjoint enforcement, World Isolation rollback, Neo4j projection idempotency.
17. Cutover: rename `world_model.py` to `world_model_legacy.py`, rename `world_model_owl.py` to `world_model.py`. Tag the commit.

### Phase G — Optional refinement

18. **Provenance projection** — investigate whether `owlready2` can be augmented with HermiT justifications via direct OWL API access. If yes, add provenance edges to the projection; if no, ship without and note the gap.

## Open questions (revised)

1. **Compute-matched calibration run.** Now genuinely the highest-value next experiment — the architecture is locked, the council can be tested against compute-matched solo on Layer-2-passing rates with full L2 active.
2. **OWL2 expressivity boundary mapping.** Once the refactor is in, run an empirical sweep of claim shapes against the boundary. Most claims will route to L2; the exceptions become L3's job description.
3. **HermiT justification access.** Phase G refinement; non-blocking.
4. **Persona ensemble interactions under v1.2 Molecular Self.** Still single-run observation; needs replication after the refactor lands.
5. **AGEM as MCP server.** Still deferred; v0.5 doesn't need new orchestration.

## Connections

- [[efhf]] — verification substrate
- [[sentience-metaphysics]] — Layer 1 council substrate
- [[seg-molecular-self]] — drift-resistance at the persona level
- [[why-llms-arent-scientists-yet]] — Trehan-Chopra failure-mode taxonomy
- [[agentic-research]] — broader paradigm context
- [[mcp-logic]] — Layer 3 (residual scope)
- [[hipai-montague]] — Layer 2 refactor target
- [[spike-campaign-001-004-summary]] — empirical foundation
- [[spike-001-spacy-owlready2]] — semantic synthesis validation
- [[sheaf-consistency-enforcer]] — Layer 5 lumpability
- [[verifier-graph]] — DAG provenance + reasoning hygiene
- [[advanced-reasoning-mcp]] — Layer 4 meta-cognition
- [[conscience-servitor]] — Layer 5+ ethical triage
- [[aseke-compass-mcp]] — agent behavioral monitoring
- [[agem]] — sheaf-theoretic coordination (UI-only, deferred)
