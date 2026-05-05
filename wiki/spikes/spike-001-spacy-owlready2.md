---
summary: VALIDATED — spaCy+owlready2 handles transitive subsumption, lemmatization, and pluralization in one sync_reasoner() call. Three v0.3 Layer-2 caveats collapse.
tags: [spike, validated, hipai-montague, spacy, owlready2, hermit]
updated: 2026-05-03T08:33:53Z
created: 2026-05-03T08:33:53Z
---

---
created: 2026-05-03T08:30:00Z
updated: 2026-05-03T08:30:00Z
type: spike-result
summary: GSD Spike 001 — validated that spaCy + owlready2 + HermiT replaces HiPAI-Montague's regex parser and manual Cypher subsumption with depth-N transitive reasoning in a single sync_reasoner() call.
tags: [spike, hipai-montague, spacy, owlready2, hermit, layer-2, validated]
status: validated
location: /home/ty/Repositories/ai_workspace/HiPAI-Montague-Semantic-Cognition/.planning/spikes/001-spacy-owlready2-integration/
---

# Spike 001 — spaCy + owlready2 Integration

> **Verdict:** ✅ **VALIDATED.** The architectural shift from regex+Cypher to spaCy+owlready2 is highly viable. Combined overhead (spaCy model load + JVM for HermiT) is acceptable for the depth of deductive reasoning enabled. Three of the four v0.3 Layer-2 caveats are structurally eliminated.

## Question

Can `spaCy` (dependency parsing, lemmatization, POS) plus `owlready2` (OWL2 ontology + HermiT DL reasoner) replace HiPAI-Montague's hand-rolled regex pattern dispatch and Cypher inheritance traversal — and in particular, can the depth-3 transitive chain "Aristotle → Philosopher → Man → Mortal" be handled in a single `sync_reasoner()` call?

## Method

A self-contained spike script (`spike.py`) that:

1. Parses test sentences with spaCy `en_core_web_sm`, extracting `nsubj` and `attr`/`acomp` dependency tags
2. Builds an owlready2 ontology dynamically using `types.new_class` for runtime ontology construction
3. Calls `sync_reasoner()` (HermiT) for classification
4. Uses `isinstance(individual, class_obj)` to verify inferred memberships

## Result

| Capability | Verdict |
|---|---|
| Depth-N transitive subsumption (Aristotle → Philosopher → Man → Mortal) | ✅ Single `sync_reasoner()` call |
| Verb lemmatization (`harms` → `harm`) | ✅ Native via `.lemma_` |
| Pluralization (`men` → `man`) | ✅ Native via `.lemma_` |
| Dependency tag extraction (nsubj, attr, acomp) | ✅ spaCy stable |
| Runtime ontology building | ✅ `types.new_class` |
| Verification idiom | `isinstance(individual, class_obj)` |

## Discoveries

- **Use `.lemma_` for class and individual names** to normalize forms like "men" → "man". This bypasses `.capitalize()` entirely, structurally eliminating the v0.3 `Concept_Moralpatient` CamelCase bug.
- **Use `types.new_class`** for runtime ontology building, not class-statement metaprogramming.
- **JVM dependency** for HermiT — must be available in deployment environment. Verified present on this machine via `java -version`.

## What this resolves

Three of the four v0.3 Layer-2 caveats collapse simultaneously:

1. **Transitive chain failure** (v0.3 caveat: "Concept-to-concept linking absent; depth-2 doesn't fire") — HermiT does this natively as a fixed-point computation.
2. **Verb-stem regression at action gates** (v0.3 caveat: `check_action(... HARMS ...)` returns PERMITTED) — spaCy lemmatization at the parse boundary means relations are normalized before they reach the gate.
3. **Plural-noun-as-property** (v0.3 caveat: `prop_men=true` instead of `IS_A Concept_Man`) — `.lemma_` emits `man` regardless of surface form, and owlready2 represents the relation as a real subclass edge, not a property string.

The fourth caveat (CamelCase concept naming) is implicitly resolved by routing through `.lemma_`.

## Implication for the SEG Scientist Agent

Promotes the [[seg-scientist-agent-design|design]] from v0.3 to v0.4. Layer 2's claim regime expands from "depth-1 subsumption + deontic" to "depth-N subsumption + deontic + consistency". The Layer 1 (SEG council) NL→FOL translation burden shrinks further because OWL2 covers more claim types than the v0.3 Layer 2 could handle. Layer 3 (mcp-logic / Prover9) is reserved for claims that OWL2 cannot express — true quantifier elimination and counterexample search.

## Next Up

`/gsd-spike-wrap-up` — package findings into a project skill for the real refactor of HiPAI-Montague.

## Connections

- [[hipai-montague]] — target of refactor
- [[seg-scientist-agent-design]] — promoted to v0.4 by this spike
- [[mcp-logic]] — residual scope narrowed; reserved for OWL2-inexpressible claims
