---
summary: Combining the entity-tracking mechanism (fragile REMOVE tag, parallel final-token aggregation) with Entropy-Cut sampling: test-time repair substitutes for retraining only on recombination-OOD (correct path already in the base model), never on capability-OOD (state absent from the machine). Confident silent failures need a mechanistic cut signal, not entropy.
tags: [synthesis, ood, test-time-scaling, entropy-cut, entity-tracking, causal-states, hallucination-detection, retraining, chain-of-thought, mechanistic-interpretability]
updated: 2026-05-29T20:00:30Z
created: 2026-05-29T20:00:30Z
type: synthesis
status: draft
confidence: 0.65
sources: [entropy-cut-mh-reasoning-2026, llms-entity-tracking-state-changes]
---

# Test-Time Sampling vs. Retraining: The Recombination/Capability OOD Boundary

**Type:** Synthesis
**Origin:** Ty + Claude, 2026-05-29 (cross-domain synthesis)
**Source papers:** [[entropy-cut-mh-reasoning-2026]], [[llms-entity-tracking-state-changes]]
**Parent synthesis:** [[causal-state-edm-ood-isomorphism]] — this page answers its Open Question 3
**Confidence:** boundary logic ~0.85 (deductive); specific externalization bridge ~0.5 (testable conjecture)

## The Question

Can the mechanistic picture of *how* LMs fail at sequential state tracking be combined with entropy-guided test-time sampling to repair out-of-distribution reasoning **without retraining**?

Yes — but only for one class of OOD. The boundary between "fixable by sampling" and "requires retraining" is the load-bearing result, and it has a clean reading in this vault's existing causal-state frame.

## The Two Inputs

**Entity tracking ([[llms-entity-tracking-state-changes]]).** LMs do not track entity state incrementally. They aggregate all query-relevant information *in parallel at the final token*, once the query is evident — solving a sequential task with a non-sequential strategy. `REMOVE` is implemented as a *fragile global suppression tag*, not an incremental update, producing predictable failures: silent suppression failure, cross-contamination between similar entities, and degradation as removals accumulate.

**Entropy-Cut MH ([[entropy-cut-mh-reasoning-2026]]).** Next-token entropy locates consequential decision points in a *generated* trace. Cut there, resample the suffix, accept/reject via Metropolis–Hastings. Mixing time scales with the number of decision points, not token count. Training-free, dataset-free, verifier-free — and it rests on the "reasoning is already in the base model" thesis (Karan & Du).

Shared structure: **reasoning is a few load-bearing junctions buried in many inert tokens** ([[load-bearing-reasoning]]). Paper 1 locates failure junctions mechanistically; Paper 2 locates decision junctions statistically.

## The Locus Mismatch (resolve this first)

The two papers do not act at the same site:

| | Where the action is | What can intervene |
|--|--|--|
| Entity tracking | Parallel aggregation at the final token, reading a static context | Nothing sequential to cut |
| Entropy-Cut | High-entropy positions in a generated suffix | Resampling the suffix |

Entity-tracking failure is *internal and non-sequential*; Entropy-Cut needs a *sequential generated trace*. They compose only through a bridge.

**Bridge — externalize the state.** Force state tracking out of the internal parallel mechanism into explicit chain of thought ([[chain-of-thought]]). Once "apple → box, then removed, then …" is *tokens*, the state transitions become decision points Entropy-Cut can resample. This converts an un-interventable internal computation into a sampleable external one — the same internal-weights-to-external-harness move seen in the externalization literature, and structurally adjacent to CoT-topology work ([[chen-molecular-cot-2026]]).

**This bridge is the load-bearing assumption, and neither paper validates it.** It is a testable conjecture (see Open Questions): it is possible that verbalizing the state *routes around* the fragile internal mechanism entirely, in which case externalization alone is the fix and the cut step is redundant for this task.

## The Boundary: Recombination-OOD vs Capability-OOD

Entropy-Cut works because the correct path *already has nonzero mass* in the base model; it escapes a bad local mode rather than inventing a new one. That cleaves OOD in two:

| | Recombination-OOD | Capability-OOD |
|--|--|--|
| Definition | Novel arrangement of operations the model already knows | An operation/relation the model never learned |
| Path in base distribution | Exists, low marginal probability | Zero support |
| Sampling repair | reachable ✓ | unreachable ✗ |
| Causal-state reading | New *path* through existing states | A *state not in the machine* |
| Remedy | Test-time sampling / externalization | Retraining (= adding the state) |

This is the [[causal-state-edm-ood-isomorphism]] frame applied to *repair*: Entropy-Cut is MCMC over the causal-state **path** with within-state emissions held fixed. It can traverse a novel path through existing states; it cannot mint a state that isn't in the machine. The fragile `REMOVE` tag is *state aliasing* — a degenerate transition — and resampling rescues it only if a non-aliased path exists.

So **"avoid retraining OOD thinking" is true exactly on the recombination side of the boundary.**

## The Caveat That Bites Here: Confident Silent Failure

Entropy detects *uncertain* errors. The fragile `REMOVE` tag tends to fail *silently* — confidently wrong, low entropy — which is exactly what an entropy cut will not fire on. For this failure mode the cut signal should be **mechanistic** (the suppression-tag activation Paper 1 already isolated), not entropy. Entropy is the cheap proxy; the tag is the real one. ([[mechanistic-interpretability]])

This sharpens a distinction already in the vault. [[engineering-internal-awareness]] frames the core diagnostic as: *is a failure due to lack of knowledge or lack of internal awareness?* That maps onto the boundary directly:

- lack of knowledge = capability-OOD (no state in the machine → retrain)
- lack of internal awareness = recombination-OOD (state exists, right path not surfaced → sample / externalize)

And it supplies the handle for confident failures: a [[metacognitive-architecture-closed-loop-self-regulation]] layer that abstains or calls a tool when *mechanistic* confidence — not entropy — is low.

## Practical Recipe (conjectured)

1. **Externalize** the state-tracking computation into CoT so transitions become tokens.
2. **Cut** at decision points — by entropy where errors are *uncertain*, by mechanistic signature (suppression-tag activation) where errors are *silent*.
3. **Resample** the suffix; accept/reject via MH.
4. **Gate**: if the correct path keeps failing to appear across resamples, treat the case as capability-OOD — escalate to retraining or external tools, do not keep sampling.

Net: training-free repair on the recombination side; a *detector*, not a fix, on the capability side.

## Connection to Existing Frameworks

- **MOP** ([[maximum-occupancy-principle]]): β = state-splitting appetite. Recombination-OOD is path occupancy *within* existing states; capability-OOD requires genuine state-splitting, which sampling cannot supply. KL-regularized RLHF (which MOP critiques) pulls *toward* the old modes — the opposite of the mode-switching that repair needs.
- **EFHF / hallucination**: confident silent failure is lumpability failure at *low* entropy — the case the entropy detector misses but a sheaf/mechanistic detector should catch.
- **EDM isomorphism** ([[causal-state-edm-ood-isomorphism]]): answers its Open Question 3 (which internal representation serves as past/future vector) for one task class — the entity-state aggregation site at the final token, with suppression-tag activation as the disruption signal.

## Empirical pilot (2026-05-29): the ceiling result

A first behavioral probe was built at `/home/ty/Repositories/ai_workspace/entity-tracking-externalization/` (PUT/MOVE/REMOVE tasks, deterministic ground truth, ~50% removed-query items; `direct` vs `externalized` conditions graded off a shared `ANSWER:` line; wrong answers classified as `ghost` / `false_remove` / `stale_or_wrong`).

**MiniMax-M2.7, 14 tasks, n_ops=12, remove_prob=0.45, temp=0, run twice — identical both times:**

| Condition | Overall | Removed-query | Present-query | Ghost rate |
|--|--|--|--|--|
| direct | **1.00** | 1.00 | 1.00 | 0.00 |
| externalized | 0.71 | 0.57 | 0.86 | 0.00 |

The externalized "errors" were **all instrumentation artifacts** — empty output (the reply was a `thinking` block with no `text` block) or token-budget truncation mid-trace — **not a single wrong location, and zero ghost errors in either condition.**

This **inverts the original conjecture** for a current reasoning model:

1. **No fragility to route around.** The fragile-`REMOVE` failure ([[llms-entity-tracking-state-changes]]) is **model-dependent**, found in smaller/older models. MiniMax-M2.7 tracks REMOVE perfectly at this difficulty — its `thinking` block is plausibly *already* externalizing the state internally. The question "does CoT route around the tag?" is moot when there's no tag-failure to begin with.
2. **Forced externalization can *hurt*.** It spent the token budget and pushed the answer into the reasoning channel, manufacturing artifacts where direct answering was clean.
3. **The result is a difficulty/capability *floor*, not a test of the boundary.** To probe the recombination/capability boundary you need a regime where `direct` actually fails — a weaker model (the local gemma4 runs trended this way but were too slow to complete) or a harder task that breaks `direct` even for M2.7.

**Tie to [[cross-layer-drift-falsification]].** Same category lesson from the behavioral side: that page shows a *geometric* apparatus (MOPS sheaf drift) missing a signal that lives in a *sparse directional* substrate — wrong observable for where the signal lives. Here a *behavioral output-accuracy* probe cannot see a sub-threshold internal mechanism either: when the competent computation lives in the substrate (the thinking channel), a surface measure (final-answer accuracy) reports a ceiling and tells you nothing about the mechanism. And the Pandey "registers internally, answers anyway" finding is mirrored benignly — M2.7 does the work internally and the externalization harness, measuring the surface, both misses it and interferes with it.

## Open Questions

1. **Does externalization preserve the failure?** *(Partially tested, 2026-05-29.)* On MiniMax-M2.7 the question is moot — no REMOVE fragility at this difficulty, and forced externalization only added artifacts. **Still open on a model where `direct` fails:** find the difficulty/model regime where direct REMOVE-tracking breaks, then test whether externalization repairs it (recombination-OOD) or not (capability-OOD). A behavioral probe alone is insufficient to confirm the *mechanism* — see Q2.
2. **Entropy vs. suppression-tag activation as cut signal** — do they correlate, anti-correlate, or fire on disjoint error sets? Anti-correlation would empirically confirm the confident-failure blind spot.
3. **Online classification of the boundary.** Is there a cheap test that labels a failure recombination- vs capability-OOD *before* spending a sampling budget? Repeated-resample non-appearance is one signal; a mechanistic probe is another.
4. **Generality.** Does the recombination/capability split hold for non-entity tasks (arithmetic carries, multi-hop retrieval), or is it specific to the parallel-aggregation strategy entity tracking uses?

## Connections
- [[entropy-cut-mh-reasoning-2026]] — decision-point sampling; the "cut" machinery
- [[llms-entity-tracking-state-changes]] — non-incremental aggregation; the fragile REMOVE tag
- [[causal-state-edm-ood-isomorphism]] — parent frame; OOD as state-splitting
- [[chen-molecular-cot-2026]] — CoT topology; the externalization target
- [[engineering-internal-awareness]] — knowledge-vs-awareness diagnostic = the OOD boundary
- [[metacognitive-architecture-closed-loop-self-regulation]] — abstain/tool-call gate for silent failures
- [[load-bearing-reasoning]] — sparse consequential junctions
- [[chain-of-thought]] — externalization medium
- [[maximum-occupancy-principle]] — β = state-splitting appetite; RLHF KL pull
- [[mechanistic-interpretability]] — source of the non-entropy cut signal
- [[mop-edm-cognitive-architecture]] — fuller framework synthesis
- [[cross-layer-drift-falsification]] — same lesson, mechanistic side: wrong observable for where the signal lives
