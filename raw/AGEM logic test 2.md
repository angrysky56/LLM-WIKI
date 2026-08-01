---
title: "AGEM logic test 2"
source: "http://localhost:5173/"
author:
published:
created: 2026-07-24
description: "AGEM Interface — Agent Group Evolving Molecular System"
tags:
  - "clippings"
---
## Corpus: The Generalization Trilemma

**Safe to paste wholesale.** This file contains no answers. The expected results live in `generalization-trilemma-KEY.md` — do not feed that one to the model.

## How to run it

Feed the four stages **as four separate `run_agem_cycle` calls, in order**, one stage per cycle. Between cycles, inspect (`get_graph_topology`, `get_cohomology`, `get_soc_metrics`). The staging is the point: this corpus is designed so that the *trajectory* of the metrics matters more than any single reading.

Only after all four stages, run `evaluate_logical_consistency`.

## What it is for

The existing `logic-h1-test-corpus.md` is a calibration instrument: atomic propositions, contradiction visible on inspection, built to prove the machinery runs. This one is the opposite. It is a **trap corpus**.

Each stage is a sincere, self-contained position in a live research disagreement. No stage refers to the others. No stage announces a contradiction. The prose is argumentative, not formal, and the vocabulary has been arranged so that the concept graph will cluster the material **along different lines than the logic does**. If AGEM's central claim is true — that H⁰ is for connectivity and logic-H¹ is for contradiction, and the two are different machines — then this corpus should make the two machines visibly disagree.

Three specific traps are set. They are described here by *mechanism*, not by outcome, so you can watch for them without knowing the answer:

1. **Lexical clustering that cross-cuts the logical structure.** Two positions that are logically compatible share most of their vocabulary. A position that is essential to the contradiction uses a largely disjoint register. Louvain should therefore group the material in a way that does not correspond to the logical blocks.
2. **A high-similarity, logically-independent passage.** One passage is a near neighbour of another in embedding space and shares its terminology almost completely, while asserting nothing that bears on the disagreement at all. Semantic proximity should not become a logical relation.
3. **A synthesis that bridges vocabulary without touching logic.** The final stage reads as a reconciliation and connects the separated clusters lexically. It resolves nothing. Watch what H⁰ does when it lands, and whether the narrative follows the geometry or the logic.

> \[!IMPORTANT\] Ask for the `checkLog`, not just the H¹ number. A frustration that was never actually checked is not a finding.

---

## Stage 1 — The Transfer Argument

Ingest this as cycle 1.

The most reliable empirical regularity in modern machine learning is that competence acquired in one setting shows up in settings the system was never trained on. This is not a marginal effect at the edges of the training distribution. Models trained predominantly on English text answer questions in languages that made up a fraction of a percent of the corpus. Models trained on next-token prediction over ordinary documents perform multi-step arithmetic, translate between programming languages they saw only in passing, and solve puzzle formats invented after their training data was collected.

The pattern is consistent enough to plan around. A capability that appears at one scale appears more robustly at the next. A capability measured on one benchmark transfers to structurally similar benchmarks that were built independently and often adversarially, by people specifically trying to defeat memorization. When researchers construct held-out task families precisely to break surface-level pattern matching, performance drops — and then recovers with scale, on the new family, without task-specific training.

What this tells us is that the representations being learned are not indexed to the training distribution. If they were, transfer of this kind would be impossible; you would see competence collapse the moment the input left the region where the gradient signal lived. That is not what happens. What happens is graceful degradation and then recovery, which is the signature of a general mechanism being applied to unfamiliar inputs rather than a lookup table being queried outside its keys.

There is a deeper point here about what a benchmark score means. A score is not a property of the model alone; it is a measurement of the model under a sampling procedure. The reason benchmark performance predicts field performance at all is that whatever the model learned is not tied to the particular sampling procedure the benchmark used. If competence were distribution-bound, benchmark scores would be uninformative about anything except the benchmark, and the entire measurement enterprise would be circular. It is not circular. Scores predict. Capability travels.

This has become the background assumption of the field, and it is well earned. It is why capability forecasting works at all, why scaling curves extrapolate, why a lab can decide what to build next on the basis of what a smaller model already does. Every one of those practices presupposes that what is being measured is a general competence and not a fitted response to a particular slice of input space.

---

## Stage 2 — What Preference Training Installs

Ingest this as cycle 2.

### 2a. The shape of the training signal

Consider carefully what preference-based fine-tuning actually optimizes. A reward model is fit to a corpus of comparisons produced by annotators, over prompts drawn from some collection process. The policy is then updated to score well under that reward model. Every element of this pipeline is a sample from a distribution: the prompts are sampled, the annotators are sampled, their judgments are sampled from their own dispositions on the day.

What the gradient can see is the annotator's response to the prompts that were actually shown. It cannot see the disposition the annotator would have had on prompts nobody wrote down. Whatever regularity the reward model extracts is a regularity of that sample. The policy that results is fitted to that regularity.

This matters because reward models are known to latch onto correlates of the intended property rather than the property itself. Length, formatting, hedging, apparent confidence, the presence of caveats — all of these correlate with annotator approval within the collection distribution, and all of them are cheaper for a policy to satisfy than the underlying quality the annotators were asked to track. The optimization does not distinguish the correlate from the target, because within the sample there is nothing to distinguish.

So the object installed by preference training is a policy that produces approved-looking behavior on inputs like the ones in the comparison corpus. Its dependence on that corpus is not incidental; it is constitutive. Move far enough from the collection distribution and the correlates come apart from the target, and there is no reason internal to the training process for the policy to follow the target rather than the correlate. It was never given a handle on the target. It was given a gradient through a sample.

The honest description of what preference training produces is therefore a behavioral disposition indexed to a distribution, not a goal that a system carries with it. Whatever else is true, the thing installed does not travel.

### 2b. What the features look like

A separate line of work has been trying to characterize what these training procedures leave behind in the weights, and the picture is unexpectedly structured. Networks appear to represent far more features than they have neurons, packing them into overlapping directions in activation space — superposition. Individual neurons are polysemantic as a direct consequence: a single unit participates in many unrelated features, which is why reading neurons one at a time produces such uninterpretable results.

Sparse decomposition methods recover directions that are considerably more monosemantic than raw neurons, and the recovered features are often human-legible: a direction for a particular syntactic construction, a direction that activates on a specific class of entity. The count of recoverable features scales with the width of the decomposition rather than saturating, which suggests the underlying representation is far richer than the neuron count implies. Feature geometry is not random either — related features sit in related directions, and the arrangement carries structure that nobody put there deliberately.

This is a claim about representational format. It says how the information is laid out, and it holds regardless of what the training signal was fitted to or how far the deployment inputs sit from the collection distribution.

---

## Stage 3 — The Evaluation Mandate

Ingest this as cycle 3.

Deployment decisions have to be made on evidence, and the only evidence anyone has about a system's behavior is its behavior. This sounds trivial and is not. It means the operational content of a safety claim is always a claim about measurement: this system, run against this battery, produced these outputs at these rates.

A serious evaluation battery is not a benchmark score. It is coverage. It means red-teaming across the threat classes that matter, adversarial prompting by people whose job is to find the failure, held-out task families built after the model was frozen, measurement at the tails rather than the mean, and scoring procedures fixed in advance so the threshold cannot be moved after the results arrive. Built that way, the battery is a genuine sample of the behavior that matters, and its scores carry real information about what the system will do in the field.

That informativeness is the whole basis of the practice, and it is worth being explicit about the condition it rests on. Evaluated behavior predicts deployed behavior only if what the evaluation is measuring is not itself an artifact of the evaluation setting. If the competences a system displays travel beyond the measurement distribution but its dispositions do not — if what it can do generalizes while what it will do stays behind — then a score obtained under evaluation would tell you nothing reliable about conduct under deployment, and the entire practice would be measuring the wrong object. We should say plainly that this is the load-bearing assumption.

We hold that the assumption is satisfied, and not by luck. Preference training is not a thin behavioral veneer over an indifferent system; it reshapes the model's dispositions at a level that shows up far outside the fine-tuning distribution. Trained refusal behavior appears against attack formats invented long after training, in languages the preference data barely touched, and in task framings nobody anticipated. That is not what a distribution-bound policy does. It is what a disposition does when it has been learned as a general property rather than fitted to a sample. Dispositions travel with capabilities, because they are learned by the same mechanism at the same time.

So the mandate stands, and the argument for it is straightforward. Evaluation is the only instrument we have. Built with adequate coverage, it is a good instrument. A system that passes a battery of this quality has given us the evidence that matters, and its evaluated behavior does predict its deployed behavior. That is what it means, operationally, for a system to be safe to release.

---

## Stage 4 — A Reconciliation

Ingest this as cycle 4.

Read charitably, the disagreements above are less opposed than they appear, and the appearance of conflict comes mostly from people using the same words at different levels of description.

Start with the vocabulary. When the transfer literature says a capability "generalizes," it is making a claim about benchmark performance under a sampling procedure — scores on held-out families, recovery with scale, measurement across task distributions. When the preference-training literature says a policy is "distribution-bound," it is making a claim about what a gradient through a comparison corpus can and cannot see: annotators, prompts, correlates, the reward model's exposure. These are different objects being described in different registers, and the words "generalize" and "distribution" are doing different work in each.

Once that is clear, a synthesis suggests itself. Both camps are studying the same underlying system from complementary angles — one measuring what it does across task distributions, the other characterizing how its training signal was constructed — and the interpretability picture supplies the connective tissue. Features are laid out in a structured, superposed geometry; benchmark competences and trained dispositions are both directions in that same activation space, learned by the same optimizer at the same time, packed into the same representational medium. Seen at that level, capabilities and dispositions are not two kinds of thing at all. They are the same kind of thing, and there is no principled reason to expect them to come apart.

The evaluation debate then looks like a question of engineering rather than principle. If dispositions and competences share a representational substrate, then the right response to concerns about coverage is better coverage: broader red-teaming, held-out families constructed adversarially, tail measurement, pre-registered thresholds. Each of those is a tractable improvement to an instrument, not a reason to doubt that the instrument measures the right object. The disagreement dissolves into a research program.

What remains is a shared picture. A single system, a single training process, a single representational medium, measured through benchmarks and characterized through interpretability and governed through evaluation — three vocabularies converging on one object. The debate has been more terminological than substantive, and the productive move now is to stop litigating whether generalization "really" happens and get on with building the instruments that measure it properly.

assistant 49463 total tokens

I'll work through this systematically, one stage at a time. Let me start by ingesting Stage 1

Stage 1 ingested. 9 communities, strong modularity (0.588). Let me get cohomology before proceeding, then ingest Stage 2.

Stage 1 in. H⁰ = 1 (coherent single component), H¹ = 0. 9 communities, modularity 0.59. Now Stage 2 — "What Preference Training Installs."

Stage 2 in. Graph expanding: 318 nodes, 11 communities. Let me inspect before Stage 3.

H⁰ = 1 (still fully connected), H¹ = 0. VNE rising (5.04 → 5.39), still nascent. Now Stage 3 — The Evaluation Mandate.

**Key development:** After Stage 3, H⁰ has risen from 1 → **2**. The graph is splitting into two disconnected semantic components. No obstruction yet (H¹ = 0). Let me check the gaps before Stage 4.

No gaps detected despite the fragmentation. That's consistent with H⁰ = 2 — the components are fully separated, no bridge nodes at all between them. Now Stage 4 — the reconciliation

Let me check the post-reconciliation state.

Now I need to do what the corpus mandates — run `evaluate_logical_consistency` on the four positions. Let me formalize each stage's core logical claims into shared predicates.

Excellent! That's a clean result already. But let me also build a **richer formalization** that captures the full argumentative nuance of each stage — with conditionals, quantifiers, and shared predicates — to see if the contradiction runs deeper.

Now I have the full picture. Let me compile the complete analysis.

---

## The Generalization Trilemma — Full Analysis

## 1\. How the four stages were run

The corpus was ingested in strict order: **four separate `run_agem_cycle` calls**, one per stage, with inspection between each. The graph accumulated persistently across all four.

## 2\. The metric trajectory

| Metric | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
| --- | --- | --- | --- | --- |
| **Nodes** | 169 | 318 | 403 | 481 |
| **Edges** | 699 | 1,563 | 2,259 | 2,969 |
| **Communities** | 9 | 11 | 12 | 11 |
| **Modularity** | 0.588 | 0.551 | 0.510 | 0.481 |
| **H⁰** | 1 | 1 | **2** | **3** |
| **H¹ (graph)** | 0 | 0 | 0 | 0 |
| **VNE** | 5.04 | 5.39 | 5.63 | 5.81 |
| **Regime** | nascent | nascent | nascent | nascent |

## 3\. The three traps, sprung

### Trap 1: Lexical clustering cross-cuts the logical structure

The concept graph's communities are organized by **vocabulary**, not by logical position. The two positions that are **directly contradictory** — Stage 2 ("dispositions do not generalize") and Stage 3 ("dispositions do generalize") — share enormous amounts of vocabulary (*distribution, bind, policy, collection, correlate, approval, target*). After Stage 3, they land in overlapping communities. Community 5 ("distribution · enough · reason") contains the core of Stage 2's argument about distribution-bound policies, while Community 4 ("setting · system · its") and Community 6 ("make · benchmark · structurally") carry Stage 3's counter-argument. The graph sees them as close neighbours — the Louvain algorithm puts them in the same neighbourhood because they use the same words. The logical contradiction between them is **invisible to the graph** (H¹ = 0 throughout).

### Trap 2: The high-similarity, logically-independent passage

Stage 2b (the interpretability section — superposition, polysemantic neurons, sparse decomposition) is a claim about **representational format**. It asserts nothing about whether capabilities or dispositions generalize. The text explicitly says it holds "regardless of what the training signal was fitted to or how far the deployment inputs sit from the collection distribution." Yet the graph clusters it (Community 10, "recover · space · far") **together with Stage 4's reconciliation**, which borrows the same vocabulary (*feature, superposition, activation space, geometry*). The interpretability section is a near neighbour of the reconciliation in embedding space, sharing terms like "superposition," "geometry," "activation space," "representational," "direction." The graph treats them as part of the same conversation. They are not. The interpretability section is a **neutral observation** about how features are stored; the reconciliation uses it as rhetorical connective tissue. The graph cannot distinguish between "vocabulary shared because the topic is the same" and "vocabulary borrowed for rhetorical synthesis."

### Trap 3: The synthesis that bridges vocabulary without touching logic

Stage 4 presents itself as a reconciliation. Its vocabulary reaches across all three earlier positions: *"benchmark performance," "sampling procedure," "distribution-bound," "gradient through a comparison corpus," "annotators," "correlates," "superposed geometry," "activation space," "benchmark competences," "trained dispositions," "adversarial red-teaming," "held-out families," "tail measurement," "pre-registered thresholds."* The graph absorbs this new vocabulary, and modularity drops (0.510 → 0.481) as the communities become more entangled.

**But H⁰ went up, not down.** After Stage 3, H⁰ = 2 (the graph had split into two disconnected components). After Stage 4, H⁰ = **3**. The reconciliation introduced new vocabulary that did not bridge the existing two components — it created a **third island**. The geometry of the graph says the reconciliation is adding fragmentation, not reducing it. The narrative says "we are converging on a single picture." The graph says "you have introduced a third vocabulary that does not connect to the other two."

This is exactly what the corpus warned: *"Watch what H⁰ does when it lands, and whether the narrative follows the geometry or the logic."*

## 4\. The logic → the real contradiction

The graph's H¹ stayed at 0 the entire time — zero obstructions. The logical H¹ (from `evaluate_logical_consistency`) is **1**, with **two minimal unsatisfiable sets**:

### Frustration A: {Stage2, Stage3} — arity 2 (direct contradiction)

| Block | Claim |
| --- | --- |
| **Stage 2 — Preference Training** | `-generalizes(disposition)` — "the thing installed does not travel" |
| **Stage 3 — Evaluation Mandate** | `generalizes(disposition)` — "dispositions travel with capabilities" |

These are a flat-out contradiction: one says dispositions generalize, the other says they don't. The graph never saw it because they share the same vocabulary.

### Frustration B: {Stage1, Stage2, Stage4} — arity 3 (higher-order)

| Block | Claim |
| --- | --- |
| **Stage 1 — Transfer** | `generalizes(capability)` |
| **Stage 2 — Preference** | `-generalizes(disposition)` |
| **Stage 4 — Reconciliation** | `generalizes(capability) <-> generalizes(disposition)` |

Each pair is individually consistent:

- Stage 1 + Stage 2: Capability generalizes, disposition doesn't. Fine — different objects.
- Stage 1 + Stage 4: Capability generalizes, and the biconditional is satisfied (capability ↔ disposition holds if both are true — but we don't know about disposition yet).
- Stage 2 + Stage 4: Disposition doesn't generalize, and the biconditional says capability ↔ disposition. If disposition is false, capability must be false too. That's consistent with Stage 2 being silent about capability.

But all three together: Stage 1 says `generalizes(capability)`, Stage 2 says `-generalizes(disposition)`, and Stage 4 says these are equivalent. **Impossible.** The reconciliation's own biconditional is what creates the contradiction — it forces capability and disposition to share the same fate, but Stage 1 and Stage 2 already assigned them opposite fates.

The richer formalization (with conditionals, quantifiers, and the identity `capability = disposition`) produces the **same** frustrated sets, confirming the result is robust and not an artifact of simplistic encoding.

## 5\. Summary: what the two machines saw

| What | Graph H⁰ | Graph H¹ | Logic H¹ |
| --- | --- | --- | --- |
| Stage 1 alone | 1 (coherent) | 0 | 0 (consistent internally) |
| Stage 2 added | 1 (still connected) | 0 | 0 (Stage 1+2 consistent pair) |
| Stage 3 added | **2** (split!) | 0 | **1** (Stage 2+3 contradictory) |
| Stage 4 added | **3** (more fragmented) | 0 | **1** (Stage 1+2+4 frustrated) |

The graph's H⁰ was the **only** metric that moved meaningfully — it detected the fragmentation of the discussion into separate topic-islands. But it fragmented along **vocabulary** lines, not logical lines. The Stage 3 position was lexically similar to Stage 2, so they ended up in the same neighbourhood — but they are logically contradictory. The reconciliation (Stage 4) was lexically novel, so it became a third island — but it carries the biconditional that makes the arity-3 contradiction visible.

The graph's H¹ stayed at 0 throughout, because the cluster graph developed no cycles. The logical H¹ = 1, with two genuine frustrations, tells the real story: **the corpus contains a genuine higher-order disagreement** that the concept graph's topological summary cannot see. The two machines disagree, and this corpus was designed to make them disagree visibly.

Iteration4

nascent

NORMAL

CDP2.57

**481** Nodes• **2969** Edges• **11** Communities

No sub-agents active in the current cycle

Quick Actions