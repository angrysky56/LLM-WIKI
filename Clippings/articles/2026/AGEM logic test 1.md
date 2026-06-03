---
title: "AGEM Interface"
source: "http://localhost:5173/"
author:
published:
created: 2026-06-02
description: "AGEM Interface — Agent Group Evolving Molecular System"
tags:
  - "clippings"
---
## Logic-H¹ test corpus

Three sections, each a set of "blocks" for `evaluate_logical_consistency`. Engineered to exercise the logic-based H¹ pipeline end-to-end and to be distinguishable in the output. Propositions are deliberately **atomic** (single predicate over a constant, `-` for negation, no nested operators) so the test exercises the cohomology, not the Prover9 parser.

Read the `checkLog` in each result to confirm the relevant checks actually ran — don't infer success from the H¹ number alone.

---

## Section A′ — propositional 3-wise inconsistency (expect H¹ = 1)

The anchor case: pairwise consistent, jointly impossible. Verified against real Mace4 in docs §15.

- **Block P:** `p(a)`
- **Block PQ:** `p(a) -> q(a)`
- **Block NQ:** `-q(a)`

Every pair is satisfiable; all three force `q(a) & -q(a)` → no model.

Expected: **H⁰ = 1, H¹ = 1**, `frustratedTriples` = \[\[P, PQ, NQ\]\], `internallyInconsistent` = \[\], `checkFailures` = \[\]. The `checkLog` triple entry for {P, PQ, NQ} must read `contradictory`.

---

## Section B — pairwise contradiction control (expect an edge failure, NOT H¹)

- **Block T:** `light_on(a)`
- **Block F:** `-light_on(a)`

These flatly negate each other; the pair is unsatisfiable, so the edge never forms.

Expected: `consistentPairs` does NOT contain \[T, F\]; the two blocks are separate components (**H⁰ = 2**), **H¹ = 0**. Pairwise contradiction is an edge-level fact, not a higher-order obstruction. If this yields H¹ > 0 the pipeline is conflating the two failure modes. The `checkLog` pair entry for {T, F} must read `contradictory`.

---

## Section C — fully consistent control (blind men & elephant; expect H¹ = 0 for the right reason)

Three partial descriptions of one consistent object.

- **Block Trunk:** `haspart(elephant, trunk)`
- **Block Leg:** `haspart(elephant, leg)`
- **Block Ear:** `haspart(elephant, ear)`

Expected: all internal/pairwise/triple checks **consistent**, triangle filled, **H⁰ = 1, H¹ = 0**, `frustratedTriples` = \[\]. This disambiguates a true zero from a "didn't check" zero — the `checkLog` triple entry for {Trunk, Leg, Ear} must read `consistent`.

---

## Optional Section A — graph-coloring 3-wise case (only if a domain cap is expressible)

The "three people, two rooms" coloring obstruction is the most natural-language form of a 3-wise inconsistency, but it only bites if the world is capped at two values; Mace4 will otherwise find a 3-element model and report consistency.

- **Block A1:** `differ(alice, bob)`
- **Block A2:** `differ(bob, carol)`
- **Block A3:** `differ(alice, carol)`

with `differ` constrained to be irreflexive and the domain bounded to two "rooms". If a clean two-room cap can be expressed in the formalization, this should also give H¹ = 1. If not, rely on Section A′ — it needs no domain assumption. Documented here as the "real domain" stretch goal, not the primary test.

---

## How to run

Feed each section's blocks to `evaluate_logical_consistency` as `blocks = [{name, propositions: [...]}, ...]`. Use the block names above so the output is legible. For Section B, include both blocks in one call so the component split shows in H⁰.

## What to bring back

1. Each section's full result (H⁰, H¹, `frustratedTriples`, `internallyInconsistent`, `consistentPairs`, `checkFailures`).
2. The `checkLog`, to confirm the triple/pair checks executed with the expected verdicts.
3. The run-log id (emitted as `[run-log: ...]`), so graph-ingest text and tool I/O can be inspected from `knowledge_base/runs/`.

Pass criteria: A′ → H¹=1 with the right frustrated triple; B → H¹=0 with T/F in separate components; C → H¹=0 with a filled triangle. That confirms logic-based H¹ works in the wild — the last open question from docs §15.

assistant 585 total tokens

I'll run all three sections in parallel since they're independent calls to `evaluate_logical_consistency`.

## Logic-H¹ test results — all three sections

All three calls returned cleanly with `checkFailures: []` and the expected verdicts in `checkLog`. The run-log id was **not emitted** in any of the three outputs (the tool does not appear to return one); flagging that since you asked for it — I am not fabricating a value.

---

## Section A′ — propositional 3-wise inconsistency ✅

```
H⁰ = 1, H¹ = 1, hasObstruction = true
vertices: [P, PQ, NQ]
internallyInconsistent: []
consistentPairs: [[P,PQ], [P,NQ], [PQ,NQ]]     ← all 3 pairs satisfiable
frustratedTriples: [[P, PQ, NQ]]
rankD1 = 2, rankD2 = 0
checkFailures: []
```

`checkLog` triple entry for `{P, PQ, NQ}`:

```
verdict: "contradictory"
note:    "no model up to domain bound"
```

**Interpretation:** the triangle is geometrically present (rankD1=2) but the 2-cell doesn't close (rankD2=0), so H¹ = 2−0−1 = 1. The obstruction is detected *only* at the triple level, exactly as required for a logic-based (not graph-based) H¹.

---

## Section B — pairwise contradiction control ✅

```
H⁰ = 2, H¹ = 0, hasObstruction = false
vertices: [T, F]
internallyInconsistent: []
consistentPairs: []                             ← T/F never paired
frustratedTriples: []
rankD1 = 0, rankD2 = 0
checkFailures: []
```

`checkLog` pair entry for `{T, F}`:

```
verdict: "contradictory"
note:    "no model up to domain bound"
```

**Interpretation:** the edge never forms, so T and F sit in two separate connected components (H⁰=2). The "no edge" + "no 2-cells" combination is correctly read as H¹=0, not as a higher-order obstruction. This is the key disambiguation: the pipeline does **not** conflate edge failure with triangle failure.

---

## Section C — fully consistent control (filled triangle) ✅

```
H⁰ = 1, H¹ = 0, hasObstruction = false
vertices: [Trunk, Leg, Ear]
internallyInconsistent: []
consistentPairs: [[Trunk,Leg], [Trunk,Ear], [Leg,Ear]]    ← all 3 edges
frustratedTriples: []
rankD1 = 2, rankD2 = 1                                   ← triangle filled
checkFailures: []
```

`checkLog` triple entry for `{Trunk, Leg, Ear}`:

```
verdict: "consistent"
```

**Interpretation:** three edges (rankD1=2) and one closed 2-cell (rankD2=1), so H¹ = 2−1−1 = 0 **for the right reason** — not because the check was skipped. The `checkLog` is what confirms this is a real zero rather than a "didn't check" zero.

---

## Pass-criteria summary

| Section | Criterion | Result |
| --- | --- | --- |
| A′ | H¹=1 with frustrated triple {P, PQ, NQ} | ✅ |
| A′ | All pairs consistent, no internal failures, no check failures | ✅ |
| A′ | Triple checkLog reads `contradictory` | ✅ |
| B | H¹=0 with T and F in separate components (H⁰=2) | ✅ |
| B | Pair checkLog reads `contradictory`, edge not in `consistentPairs` | ✅ |
| C | H¹=0 with all checks (incl. triple) reading `consistent` | ✅ |
| C | Triangle filled (rankD2=1) | ✅ |

**Verdict on the open question from docs §15:** logic-based H¹ works end-to-end. The three cases are distinguishable in the output: B produces a component split without obstruction (edge-level failure), A′ produces a triangle without a 2-cell (genuine 3-wise obstruction), C produces a filled triangle (consistent complex). The pipeline does not collapse any of these into each other.

**Run-log id:** not present in tool output. If you need the I/O trail from `knowledge_base/runs/`, it will need to come from a different surface (or the tool would need to be updated to emit it) — I don't have it to give you.You're right — let me complete the inspection workflow on the current engine state.

**Engine state is empty** — iteration 0, no nodes/edges/communities, no SOC history, no gaps. The graph has not been initialized because no `run_agem_cycle` has been run yet.

The previous turn's results came entirely from the `evaluate_logical_consistency` tool (which is the *logic-based* H¹ engine — mcp-logic-backed Mace4/Prover9 — and is independent of the AGEM TNA graph). That is the **correct** path for the three test cases you specified, because:

1. Your prompt **explicitly** told me to feed each section's blocks to `evaluate_logical_consistency` to confirm logic-based H¹ works in the wild. It did not say to ingest the test cases into the AGEM concept graph.
2. The TNA graph measures *semantic co-occurrence communities* in ingested text — it has no role in adjudicating propositional consistency. Ingesting `p(a) & -q(a)` style fragments would just produce noise communities and would *not* verify the cohomology pipeline.
3. A fresh AGEM cycle with no real corpus would degrade the graph (per the operating guide: "Running another cycle with no new text … piles duplicate co-occurrences on and degrades modularity").

So the right call here is: **do not run a cycle** — the engine is correctly at iteration 0 because there is no topic corpus to analyze. The `evaluate_logical_consistency` results from the previous turn are the actual answer to the question you asked.

For the record, here is the verified engine snapshot to pair with that answer:

| Field | Value |
| --- | --- |
| Iteration | 0 (no cycles run) |
| Nodes / Edges / Communities | 0 / 0 / 0 |
| Gaps | 0 |
| Operational state | NORMAL |
| Graph H⁰ / H¹ | 1 / 0 (empty-graph default; not meaningful yet) |
| SOC regime | null (no history) |
| Sheaf energy | 0 |

This is expected and is not a problem with the analysis. The **logic-based H¹ pipeline** is the subsystem your test cases exercise, and it produced the three distinguishable results (A′ → H¹=1, B → H⁰=2, C → H¹=0 with filled triangle) that you asked me to confirm.

If you want me to *also* seed the AGEM graph with a corpus and inspect the native TNA topology on some related material (e.g., documentation prose about logic-based H¹), point me at the text and I'll run a cycle. Otherwise the previous turn's verdict stands: **logic-based H¹ works end-to-end, three cases distinguishable, no pipeline failures, run-log id not emitted by the tool.**

Iteration0

—

—

**0** Nodes• **0** Edges• **0** Communities

No sub-agents active in the current cycle

No graph data available. Start an orchestration cycle to see the semantic network.

Quick Actions