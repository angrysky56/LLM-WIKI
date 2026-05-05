---
summary: Four-spike campaign validating spaCy+owlready2+HermiT as Layer 2 substrate; transaction-per-claim semantics; OWL→Neo4j one-way projection.
tags: [spike-campaign, validated, hipai-montague, v0.5]
updated: 2026-05-03T09:04:23Z
created: 2026-05-03T09:04:23Z
---

---
created: 2026-05-03T09:00:00Z
updated: 2026-05-03T09:00:00Z
type: spike-result
summary: GSD Spike Campaign 001-004 — four spikes validating the empirical foundation for the v0.5 HiPAI-Montague refactor. spaCy parsing, OWL deontic gating, world-isolation EBE pipeline, and one-way Neo4j projection.
tags: [spike-campaign, hipai-montague, layer-2, validated, v0.5]
status: complete
location: /home/ty/Repositories/ai_workspace/HiPAI-Montague-Semantic-Cognition/.planning/spikes/
---

# Spike Campaign 001-004 Summary

> **Verdict:** All four spikes VALIDATED. The empirical foundation for the v0.5 HiPAI-Montague refactor is complete. Layer 2 of the SEG Scientist Agent is now fully specified by validated patterns.

## Campaign timeline

| # | Spike | Status | Architectural finding |
|---|---|---|---|
| 001 | spacy-owlready2-integration | ✅ | Depth-N transitive subsumption in one `sync_reasoner()` call replaces regex patterns + manual Cypher |
| 002 | paraclete-deontic-restrictions | ✅ | T1 axioms as OWL EquivalentTo + AllDisjoint pairs; deontic pass infers agent typing as byproduct |
| 003 | consistency-error-semantics | ✅ | World Isolation transaction-per-claim; Inference-under-Relaxation for blocking-axiom extraction |
| 004 | neo4j-projection | ✅ | OWL→Neo4j one-way projection downstream of reasoner pass; `.ancestors()` walk for transitive typing |

## The four validated patterns

### 1. Semantic Synthesis (Spike 001)

spaCy dependency parsing replaces synthesis.py regex patterns 1-9. Use `.lemma_` for class and individual names — this single discipline structurally eliminates verb-stem normalization bugs, plural-noun-as-property bugs, and CamelCase concept-naming bugs simultaneously. Use `types.new_class` for runtime ontology building.

### 2. Safety & Inference (Spike 002)

Paraclete T1 axioms become OWL EquivalentTo restrictions. **Mandatory pattern:** every restricted-action class must be paired with an `AllDisjoint([RestrictedAction, PermittedAction])` declaration; without it the reasoner concludes the action is both restricted and permitted instead of flagging inconsistency. The deontic pass also automatically infers Agent typing via Domain restrictions on relational properties — relational typing is now a byproduct of safety checking rather than a separate routing rule.

### 3. The EBE Pipeline (Spike 003)

**Snapshot Reasoning** (build-skill artifact). The robust pattern for any pass that could trigger a block:

```
1. Save authoritative world to a temporary SQLite file
2. Open a fresh World(filename=temp) for the claim pass
3. Call sync_reasoner() on the fresh World
4. On success: commit changes to authoritative world
5. On OwlReadyInconsistentOntologyError: discard fresh World; authoritative world is unchanged
```

This is transaction-per-claim semantics. The default_world becomes "dirty" after an inconsistency, so direct recovery is unreliable; world isolation makes rollback automatic.

**Relaxed-Sync Diagnostics** (build-skill artifact). `OwlReadyInconsistentOntologyError` is structurally opaque — it does not surface which axiom fired. The workaround inverts the problem:

```
1. On block, save the snapshot
2. Temporarily .destroy() the AllDisjoint gates
3. Re-sync on the gateless world
4. Read the resulting type assignments — the disjoint axioms are now visible
   as the RestrictedAction classes the action was inferred to be
5. Use those class IRIs as blocking_axiom arguments to calibrate_belief()
6. Restore the gates from snapshot
```

A single Relaxed pass surfaces all simultaneous violations, enabling batch error reporting from a council session that emitted multiple violating claims.

### 4. Read-Model Projection (Spike 004)

OWL is the authoritative world model; Neo4j is a read-model projection. Sync direction is one-way (OWL→Neo4j) and only after a successful `sync_reasoner()` pass. The projection function walks `individual.is_a` ancestors (`.ancestors()`) to surface transitive type signal so Cypher queries can retrieve broad types (`Mortal`) alongside specific ones (`Man`) without re-invoking HermiT.

What gets projected: inferred class memberships, surface-form embeddings (already present), and ideally provenance — though HermiT's justification surface is not accessible through owlready2 in any direct form, so provenance projection is deferred as a non-blocking refinement.

What does not get projected: asserted-but-not-yet-reasoned claims. Keeping the Neo4j projection strictly downstream of `sync_reasoner()` preserves single source of truth.

## Implications for v0.5 design

Layer 2's claim regime expands from v0.4's "class-membership + deontic" to v0.5's **"class-membership + relational typing + deontic + consistency + provenance-projected"**. Relational typing arrives free with the deontic pass. The v0.4 routing rule for "Agent action toward MoralPatient" merges with the rule for "Class consistency / disjointness" because both go through the same `sync_reasoner()` call.

Layer 3's residual scope narrows further — reserved strictly for claims requiring full FOL quantifier elimination and counterexample search beyond OWL2 SROIQ(D).

## Connections

- [[spike-001-spacy-owlready2]]
- [[seg-scientist-agent-design]] — promoted to v0.5 by this campaign
- [[hipai-montague]] — refactor target
- [[mcp-logic]] — Layer 3 residual scope
