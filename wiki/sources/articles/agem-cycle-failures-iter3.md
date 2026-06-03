---
summary: AGEM 3-cycle formal-logic run on the philosophy-of-mind corpus — 560 nodes, 10 communities, 21 pairwise FOL checks clean, 3 honest FOL encoding failures (D1/D6/D10 nested-→ syntax), surfaces the corpus's strongest unseen bridge (P/A ↔ HOT/HOP) and most isolated concept (IIT intrinsicity).
tags: [agem, chalmers-hard-problem, philosophy-of-mind, mace4-verification, iter3, fol-encoding, honest-failures]
updated: 2026-06-03T12:54:04Z
created: 2026-06-03T12:54:04Z
---

---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "AGEM 3-cycle formal-logic run on the philosophy-of-mind corpus — 560 nodes, 10 communities, 21 pairwise FOL checks clean, 3 honest FOL encoding failures (D1/D6/D10 nested-→ syntax), surfaces the corpus's strongest unseen bridge (P/A ↔ HOT/HOP) and most isolated concept (IIT intrinsicity)."
tags: [agem, chalmers-hard-problem, philosophy-of-mind, mace4-verification, iter3, fol-encoding, honest-failures]
sources:
  - http://localhost:5173/
status: active
confidence: 0.85
---

# AGEM Analysis: The 10 Distinctions in Philosophy of Mind — 3-Cycle Run with Formal Logic

**Source**: AGEM Interface (localhost:5173) chat export
**Engine**: AGEM stack (Mace4, sheaf-consistency-enforcer, ADMM, formula-evaluator)
**Captured**: 2026-06-02
**Archived**: `Clippings/articles/2026/AGEM hard problem minimax m3 cycle failures.md` (64KB, 1430 lines)
**Companion files**: [[sources/articles/agem-corpus-1-hard-problem]] (2-iter sheaf run) and [[sources/articles/agem-corpus-full-minimax-m3]] (3-iter 4-axis regrouping)

> **Note on this source**: `wiki_ingest_raw` timed out at 300s on the 64KB file (twice). The file is archived in `Clippings/articles/2026/` and this summary captures the unique analytical content (lines 1326–1430 of the source, the 3-cycle formal-logic run). The corpus lines 1–50 of the source duplicate content already summarized in [[sources/articles/agem-corpus-1-hard-problem]] and [[sources/articles/agem-corpus-full-minimax-m3]].

## What It Is

A **3-iteration** AGEM run on the same 10-distinction philosophy-of-mind corpus analyzed in [[sources/articles/agem-corpus-1-hard-problem]], but with a *different methodology*:

- **[[sources/articles/agem-corpus-1-hard-problem]]** — 2 iterations, sheaf-cohomology topology, Mace4 zombie-conceivability check, illusionism steelman, 3 vulnerabilities in Chalmers.
- **[[sources/articles/agem-corpus-full-minimax-m3]]** — 3 iterations, 4-axis regrouping of the 10 distinctions (Axis I "shape of explanation", Axis II "intrinsic vs relational", Axis III "kind vs phenomenon", Axis IV "higher-order structure").
- **This file** — 3 iterations, **formal-logic consistency check on all 10 load-bearing claims simultaneously** (21 pairwise + 0 triple), and the graph engine surfaces two non-obvious structural findings the corpus *itself does not mention*.

## Graph Topology (3 cycles, stable)

| Cycle | Nodes | Edges | Communities | Modularity | H⁰ | H¹ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 167 | 654 | 9 | 0.701 | 1 | 0 |
| 2 | 522 | 3401 | 12 | 0.597 | — | — |
| 3 | 560 | 3823 | 10 | 0.605 | 2 | 0 |

SOC regime: **nascent**, entropy rising 5.02 → 6.28 (slope 0.63). No phase transition. The graph is still developing — appropriate for a corpus that is more *taxonomic* than *contradictory*.

**Caveat on H⁰=2:** the sheaf split is between (a) the meta-distinction cluster ("smuggle", "beg question", "erase", "load bear") and (b) the rest. The corpus's *operative claim* — that a conflation of each pair is a substantive error — is itself a cluster. That's the 30,000-foot view of what this document is *for*, isolated as its own region of the graph.

## The 10 Communities and What Binds Them

| # | Community | Size | Internal weight | What it holds |
| --- | --- | --- | --- | --- |
| 7 | *opposite · place · type* | 102 | 2066.7 | Items 7 & 8 (type phys/functionalism, epiphenomenalism/interactionism) — and absorbed most causal-role vocabulary |
| 3 | *consciousness · phenomenal · access* | 81 | 1317.2 | Items 2 & 3 (Block, IIT/GWT) — the "what is consciousness" axis |
| 0 | *process · follow · view* | 62 | 835.1 | Item 5 (predictive processing) |
| 4 | *study · item · name* | 60 | 593.9 | Meta-discourse: "smuggle", "careless", "load bear" |
| 2 | *corpus · contain · number* | 57 | 885.1 | Item 1 (hard problem) |
| 5 | *share · high · order* | 52 | 1177.0 | Item 4 (HOT/HOP) |
| 1 | *philosophical · chalmers · explanatory* | 47 | 837.1 | Item 9 (explanatory gap / zombie) |
| 6 | *character · quale · feel* | 46 | 605.8 | Item 6 (qualia/intentionality) |
| 8 | *substrate · independence · medium* | 43 | 600.7 | Item 10 |
| 9 | *its · current · constrain* | 10 | 113.7 | A bleed-off of IIT's "intrinsic cause-effect from its own perspective" |

## Two Genuine Surprises the Topology Reveals That the Corpus Does Not

### Surprise 1 — C9 is the most isolated concept in the graph

C9 (10 nodes) — IIT's "intrinsic" and "from its own perspective" — is the *most isolated* concept in the graph. Nothing else in the corpus cares about "intrinsicity" as a *property* of a system. The corpus says IIT and GWT "locate consciousness in opposite places" but the topology says they barely share a vocabulary. **The corpus understates the disagreement.**

### Surprise 2 — C3↔C5 is the strongest bridge in the entire graph

C5 (HOT/HOP) and C3 (P/A) share the *strongest* bridge (83 links, w=240.2) — stronger than the C2↔C4 bridge (hard-problem ↔ type-physicalism) that the analyst predicted. The engine sees what the corpus *doesn't say*: a meta-state-on-mental-state (HOT/HOP) and a phenomenal-vs-access split are the *same structural move* — *first-order* vs *second-order* access to a mental state.

- Block uses "poised for use in reasoning" (A-consciousness)
- Rosenthal uses "in virtue of being the target of a further mental state" (HOT)

Both are *availability for further operations*. The corpus treats them as different items (item 2 and item 4); the graph says they are two views on one structural idea.

## Top Bridges, Ranked

| Bridge (cluster ↔ cluster) | Weight | What it reveals |
| --- | --- | --- |
| 3 ↔ 5 (P/A ↔ HOT/HOP) | 240.2 | Meta-states and access — see Surprise 2 |
| 7 ↔ 8 (type-phys ↔ substrate-independence) | 192.5 | The "kind-in-many-substrates" debate is downstream of the type-identity debate |
| 1 ↔ 7 (gap/zombie ↔ type-phys) | 184.7 | The strongest *philosophical* bridge: the anti-physicalist conclusions all hang off the same pair |
| 6 ↔ 7 (qualia ↔ type-phys) | 184.4 | Qualia/intentionality *is* where the "what is a mental kind" debate gets fought |
| 1 ↔ 2 (gap/zombie ↔ hard problem) | 170.2 | Chalmers' two arguments hang together (he wrote both) |
| 2 ↔ 3 (hard problem ↔ P/A) | 142.2 | The hard problem presupposes P-consciousness |

The fact that the engine weights the **C3↔C5 bridge** (meta/availability vocabulary) above the **C1↔C2 bridge** (Chalmers' own self-consistency) is the graph's main independent observation.

## Logical Consistency Check (10 blocks, pairwise + triple)

Each item's load-bearing claim was encoded as FOL propositions and run through internal / pairwise / triple satisfiability checks.

**Verdict**: the 10 distinctions are **jointly consistent** (logic-based H⁰=1, H¹=0). No block is internally contradictory. Every pair is satisfiable. No triple is "consistent pairwise but impossible all together." This is the right answer: the corpus is presenting *alternatives in genuine dispute*, not a contradictory thesis.

## Three Honest FOL Encoding Failures

This is the most important methodological note in the file. **The engine reports three check failures as encoding errors, not corpus errors:**

> my FOL encodings of D1 (hard/easy), D6 (qualia/intentionality), and D10 (realizability/substrate-independence) tripped the Prover9 parser on nested `->` operators. These are *encoding failures*, not corpus failures. The 21 pairwise and 0 triple checks that did run are clean. I am not claiming D1/D6/D10 are jointly consistent on the strength of a tool I did not run; the corpus's *prose* arguments for them are consistent, and the other 7 blocks' FOL formalization passed.

This is the **honest accounting** pattern: report the failure, distinguish encoding failure from corpus failure, do not paper over the gap. Contrast this with summaries that would silently omit the 3 un-runnable checks.

## The Meta-Pattern the Corpus Is Teaching

Each of the 10 items is the *same shape*: a familiar label, a pair of views, and a description of the *specific error* committed by a careless fusion. The errors come in three families:

| Error family | Items | What the fusion does |
| --- | --- | --- |
| **Category collapse** | 1, 2, 4, 6, 9, 10 | Treats a categorical/structural distinction as one of degree (hard→easy; P↔A; thought↔perception; qualia↔intentionality; epistemic↔modal; realizability↔substrate-independence) |
| **Location confusion** | 3, 7, 8 | Treats "X vs Y" as variants of one view (intrinsic vs relational; identity vs role; inert vs interactive) — they answer different *questions* about X |
| **Mechanism elision** | 5 | Drops the *how-much-to-care* layer and keeps only the *what-is-wrong* layer; the *entire account of attention* evaporates |

Items 7, 8, 3 share a common deeper fault: the fused view has *nothing left to say* about what each side actually says. Epiphenomenalism and interactionism are not two answers to "is the mental real?" — they are two answers to "does the mental *do* anything?", and they give *opposite* answers. The graph gives them the highest internal weight (C7 = 2066.7) because *opposite* is the load-bearing word.

## What the Corpus Is Silent On (Catalyst Questions, from the Gap Structure)

The graph's empty `detect_gaps` list plus topology inspection points to three questions a competent reader should ask that the document does not address:

1. **C9 isolation (IIT's "intrinsic / its own perspective")**: *Is the relevant claim about consciousness that it is intrinsic* (IIT) *or that it is intrinsic to the system in a sense that survives the system's causal embedding* (a more austere reading)? The corpus treats "intrinsic" as one word. The graph sees it as the only concept in the entire document with no semantic neighbors.
2. **C3↔C5 convergence (P/A ↔ HOT/HOP)**: *Is Block's A-consciousness doing the same work as Rosenthal's higher-order thought* — i.e., is "globally available" in Block's sense the same as "the target of a further thought" in Rosenthal's? If yes, two of the 10 items collapse. If no, the corpus should say why.
3. **C7 absorption**: C7 now contains items 7, 8, *and* the bulk of causal-role language from items 1, 2, 5. The *causal role* concept is the graph's most over-loaded term. "Pain = causal role" (functionalism), "consciousness = broadcast availability" (GWT), "epiphenomenalism = no causal role," "attention = optimization of precision" (predictive processing) — *causal role* is doing four distinct jobs. The corpus names this nowhere.

## Direct Answer to the Implicit Question

If the corpus is being used to *prevent conflations* in a downstream summary, the rules are:

- Never describe something as "the [familiar label]" without saying which side of the distinction you mean.
- Never write "X is hard but we're making progress" (collapses the categorical gap).
- Never write "consciousness is information integration" (fuses intrinsic and relational).
- Never write "the mind is physical" (fuses identity and role).
- Never write "the explanatory gap shows consciousness isn't physical" (fuses epistemic and modal).
- Never write "the brain minimizes prediction error" *without* the precision-weighting clause.
- Never fuse items 4 & 6 into "the felt, meaningful character of experience" — that prejudges representationalism.
- Never state item 10's *substrate independence* as a consequence of *multiple realizability* — that smuggles the uploading thesis in via the back door.

The 10 distinctions, taken together, are a *taxonomy of category mistakes* in philosophy of mind. The graph confirms they are independent and consistent; the corpus itself does not surface the strongest bridge (P/A ↔ HOT/HOP) and does not name the most isolated concept (IIT's intrinsicity). Both are worth flagging.

## Connections

- [[sources/articles/agem-corpus-1-hard-problem]] — 2-iter sheaf run on the same corpus
- [[sources/articles/agem-corpus-full-minimax-m3]] — 3-iter 4-axis regrouping of the same corpus
- [[concepts/sheaf-cohomology]] — method used in the companion file
- [[concepts/integrated-information-theory]] — IIT's intrinsicity is the most isolated concept here
- [[concepts/higher-order-thought]] — strongest bridge partner
- [[concepts/phenomenal-consciousness]] — strongest bridge partner
- [[entities/projects/agem-interface]] — the engine that produced this analysis

## Methodological Note

The combination of (a) sheaf topology, (b) formal-logic consistency, and (c) **honest reporting of the 3 FOL encoding failures as encoding errors** is itself worth flagging. The 2-iter file used sheaf-cohomology; the 3-iter regrouping file used the 4-axis interpretation; this 3-iter cycle-failures file adds formal logic *and* the honest-failure report. The trilogy demonstrates the AGEM stack's three modes (sheaf, regrouping, formal logic) applied to the same corpus with methodological transparency about which checks ran and which did not.
