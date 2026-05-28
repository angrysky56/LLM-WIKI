---
summary: Schema competition: how competing Knowledge Pack layers vie for model attention during inference
tags: [meta-harness, knowledge-pack, schema, memory, agent-architecture, mop]
updated: 2026-05-27T18:07:01Z
created: 2026-05-27T18:07:01Z
---

---
created: 2026-05-27
updated: 2026-05-27
type: concept
summary: How competing schema representations (ontology, workflows, rules, examples) in a Knowledge Pack vie for model attention and behavioral dominance during inference
tags: [meta-harness, knowledge-pack, schema, memory, agent-architecture, mop]
sources: []
status: active
confidence: 0.75
---

# Schema Competition

## Definition

Schema competition is the phenomenon where multiple, potentially conflicting schema representations within a Knowledge Pack simultaneously vie for a language model's behavioral attention during inference — with no built-in arbitration mechanism to resolve which representation dominates when they disagree.

In the meta-harness system, a Knowledge Pack is a layered artifact: ontology (concepts, relations, distinguishers), workflows, rules (invariants, heuristics), failure modes, and canonical/edge-case examples. When `build_pack_context()` assembles these layers into a prompt (in order: distinguishers → heuristics → failure modes → invariants → examples), the model receives all of them at once. Each layer encodes different constraints on the model's behavior. When those constraints point in different directions, the model must implicitly arbitrate — and the outcome is not guaranteed to be the "correct" one the Pack author intended.

## Where It Occurs in the Meta-Harness System

### Build Pack Context Assembly

In `bootstrap_domain.py`, `build_pack_context()` concatenates Pack layers in teaching order:

```
## Distinguishers (the "is X vs Y" rules)
## Heuristics (soft rules with confidence weights)  
## Known failure patterns (catalog entries)
## Invariants (must-never-be-violated constraints)
## Reference examples (canonical + edge cases)
```

Each layer may encode different or conflicting signals:

- A **distinguisher** might say: "dead_stock means zero sales in 90 days, slow_moving_sku means low velocity but nonzero"
- A **heuristic** might say: "SKUs with one late sale are usually dead_stock, confidence 0.7"
- A **failure mode entry** might warn: "dead_stock misclassification is common when the single late sale is recent"
- A **canonical example** might show a case that violates the 90-day rule

The model receives all of these simultaneously. When it encounters an edge case, it implicitly decides which layer to "listen to" — with no explicit priority ordering beyond prompt position (and position effects alone are unreliable).

### Pack Delta Conflicts Across Iterations

Each Phase 1 iteration produces Pack deltas targeting named gaps. A later iteration might add a distinguisher that refines or partially contradicts an earlier one, or a new failure mode entry that conflicts with an existing heuristic's confidence. The Pack accumulates these deltas without schema migration — old and new representations coexist. The model has no mechanism to prefer the newer (more refined) representation over the older one unless the prompt makes the recency explicit.

### Rule Layer Conflicts

The heuristic/invariant split is itself a source of competition:

- **Invariants** are absolute: "reorder_quantity must be ≥ 1"
- **Heuristics** are probabilistic: "SKUs with 0 sales in 90 days are usually dead_stock, confidence 0.65"

When an invariant and a heuristic conflict on a specific input (a SKU with 0 sales in 90 days but a standing reorder policy), the model must decide. The current Pack schema provides no explicit priority — the invariant is conceptually "stronger," but this strength is conveyed by natural language emphasis, not by an enforceable constraint. A model under certain decoding conditions may weight the heuristic over the invariant if the prompt doesn't make the priority clear.

## Mechanisms of Competition

Schema competition in this context operates through several mechanisms:

### 1. Prompt Position Effects

The model exhibits recency and primacy biases within context windows. Layers presented later may receive higher attention weights unless structurally highlighted as overriding. `build_pack_context()` orders layers but doesn't use explicit priority markers (e.g., "OVERRIDE: the invariant below supersedes the heuristic above").

### 2. Confidence Weight Ambiguity

Heuristics carry explicit confidence values (0–1), but these are advisory. There's no mechanism that maps a confidence threshold to behavioral priority. A heuristic with confidence 0.9 doesn't "vote harder" than one with 0.3 — the model still treats both as soft guidance.

### 3. Example Override

Canonical examples can override abstract rules if the model judges the example to be more representative of the current input. This is a feature ( grounding) but also a bug: edge-case examples meant to illustrate boundary conditions can, if mis-prompted, cause the model to misapply them to non-edge inputs.

### 4. Failure Mode Catalog as Counter-Incentive

Failure mode entries describe *what not to do* but don't encode what *to do instead* except implicitly. A model that over-attends to failure mode warnings may become overly conservative, violating heuristics or invariants to avoid flagged failure patterns.

## Relationship to MOP Research

The [[ramirez-ruiz-mop-2024]] page explicitly identifies schema competition as an open question in the MOP (Memory-Oriented Programming) framework:

> "When new information conflicts with existing schemas, how does the agent resolve the conflict? Is there a schema arbitration mechanism?"

The meta-harness system is a concrete instantiation of this open question. Ramirez-Ruiz's three-layer memory model (working / short-term / long-term) maps onto the Pack's structure: the context window is working memory, the Pack's ontology and rules are long-term memory, and the Phase 0 analysis is short-term episodic signal. Schema competition in this mapping is precisely the problem of how the long-term Pack knowledge interacts with the immediate context.

### Diversity-Weighted Consolidation as Analog

In Ramirez-Ruiz's framework, *diversity-weighted* memory consolidation prevents "schema monopolization" — where one schema dominates memory bandwidth at the expense of others. The meta-harness Pack faces an analogous problem: if the ontology layer is rich but the examples layer is thin, the model may default to ontological reasoning even when examples would give better guidance. Pack completeness is uneven by design (Phase 1 iterates toward coverage), but the model has no signal about which layers are more reliable.

## Consequences in the Meta-Harness Loop

Schema competition has concrete consequences for Phase 1 curation:

| Symptom | Root Cause | Impact |
|---------|------------|--------|
| Pack delta improves one metric but degrades another | The delta addressed the gap but created a conflict with an existing rule/layer | Attributing fitness changes is difficult |
| Model ignores a new distinguisher | The existing heuristic on the same distinction has higher prompt coverage | Gap persists despite correct Pack update |
| Edge case example over-applied | Example is more salient than abstract rule in few-shot retrieval | False positive on non-edge inputs |
| Invariant violation despite Pack having the invariant | Natural language emphasis insufficient to override heuristic or example | Fitness regression |

## Mitigation Strategies

The Pack schema currently provides no built-in arbitration. Mitigation requires explicit design:

### 1. Priority Markers

Prefix conflicting sections with explicit priority indicators:
```
## Invariants (OVERRIDE ALL — these must never be violated)
## Heuristics (follow when no invariant applies)
```

### 2. Confidence as Behavioral Threshold

Instead of advisory confidences, use thresholded rules in the Pack itself:
```
## Heuristic
IF sales_velocity < 0.1 AND days_since_sale > 90:
  CONFIDENCE 0.85 → apply dead_stock classification
```

### 3. Explicit Layer Confidence

Assign a meta-confidence to each Pack layer reflecting its refinement level:
```yaml
coverage:
  concepts_defined: 12      # high confidence in ontology
  rules_defined: 3          # low confidence — rules still being curated
  canonical_examples: 0     # no grounding yet
```

The model could use layer confidence as attention weighting during inference.

### 4. Conflict Documentation

Each failure mode entry in `failure_modes/catalog.md` should explicitly name which other Pack layers it may conflict with:
```markdown
## dead_stock_misclassification
Detection: ...
Conflicts with: heuristics.md#slow_moving_sku (overlapping definitions)
Resolution: apply the 90-day rule strictly; the single-late-sale exception is a trap
```

## Open Questions

1. **Is prompt position a reliable priority mechanism?** Empirical question: does moving a constraint to the end of the context reliably make it dominate? This could be tested by measuring fitness deltas across Pack ordering variations.

2. **Should the Pack schema encode explicit priority edges?** A `rules/priority.md` file that names which layers override which would give the model structural (not just textual) priority information.

3. **How does schema competition interact with model scale?** Smaller models may be more susceptible to schema competition (less able to reason about conflicting constraints). Larger models may have more robust implicit arbitration.

4. **Does Phase 2 (architecture) ever need to address schema competition?** If schema competition is purely a knowledge-layer problem, Phase 1 curation should be sufficient. Architecture would only be needed if the model requires a persistent arbitration mechanism that can't be expressed in the Pack's content.

5. **Can the verifier evaluator detect schema competition at evaluation time?** The `VerifierGraphEvaluator` could potentially flag when a failure mode trace shows the model attended to the wrong Pack layer — if the DAG evaluation distinguishes between "followed the wrong constraint" vs. "followed the right constraint incorrectly."

## Connections

- [[ramirez-ruiz-mop-2024]]: foundational MOP research that identified schema competition as an open question
- [[mop-architecture]]: general pattern this research established; schema competition is an architectural concern within MOP
- [[bounded-structured-memory]]: the Hermes implementation of layered memory; analogous to Pack layers
- [[domain-curator]]: Phase 1 skill that creates Pack content; schema competition is a failure mode of Phase 1 deltas
- [[knowledge-pack]]: the artifact whose layered structure creates the competition conditions
- [[meta-harness]]: the system in which schema competition is concretely observable

## See Also
- [[concepts/schema-competition]]
- [[index]]
- [[log]]
- [[schema-competition]]

- The [[ramirez-ruiz-mop-2024]] page, which explicitly frames schema competition as an open research question
- `bootstrap_domain.py::build_pack_context()` — the assembly function that concatenates competing layers
- `domain_curator/SKILL.md` — Phase 1 curator; mitigation of schema competition is a curation quality concern
