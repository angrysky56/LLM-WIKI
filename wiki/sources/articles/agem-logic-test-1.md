---
summary: AGEM Logic-H¹ test corpus — three engineered test sections (propositional 3-wise inconsistency, pairwise contradiction control, fully consistent control) validate the logic-based H¹ pipeline end-to-end. All three sections pass with checkFailures=[] and expected verdicts in checkLog.
tags: [agem, mace4-verification, logic-test, h1-pipeline, atomic-propositions, iter1]
updated: 2026-06-03T12:56:59Z
created: 2026-06-03T12:56:59Z
---

---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "AGEM Logic-H¹ test corpus — three engineered test sections (propositional 3-wise inconsistency, pairwise contradiction control, fully consistent control) validate the logic-based H¹ pipeline end-to-end. All three sections pass with checkFailures=[] and expected verdicts in checkLog."
tags: [agem, mace4-verification, logic-test, h1-pipeline, atomic-propositions, iter1]
sources:
  - http://localhost:5173/
status: active
confidence: 0.9
---

# AGEM Logic-H¹ Test Corpus — Engineered Validation of the Pipeline

**Source**: AGEM Interface (localhost:5173) chat export
**Engine**: AGEM stack (Mace4, sheaf-consistency-enforcer, evaluate_logical_consistency)
**Captured**: 2026-06-02
**Archived**: `Clippings/articles/2026/AGEM logic test 1.md` (10KB, ~120 lines)
**Iteration state**: 1, nascent, NORMAL, CDP 1.99, 134 nodes, 549 edges, 8 communities

## What It Is

A **test corpus for the logic-based H¹ pipeline**. Three engineered sections, each a set of "blocks" for `evaluate_logical_consistency`. Propositions are deliberately **atomic** (single predicate over a constant, `-` for negation, **no nested operators**) so the test exercises the cohomology, not the Prover9 parser.

The methodology is explicit: read the `checkLog` in each result to confirm the relevant checks actually ran — don't infer success from the H¹ number alone. This is the **honest-evaluation pattern**: require direct readouts of intermediate state, not just summary numbers.

## Section A′ — Propositional 3-Wise Inconsistency (expect H¹ = 1)

The anchor case: pairwise consistent, jointly impossible. Verified against real Mace4 in docs §15.

- **Block P**: `p(a)`
- **Block PQ**: `p(a) -> q(a)`
- **Block NQ**: `-q(a)`

Every pair is satisfiable; all three force `q(a) & -q(a)` → no model.

**Expected**: H⁰ = 1, H¹ = 1, `frustratedTriples` = [\[P, PQ, NQ\]], `internallyInconsistent` = [], `checkFailures` = []. The `checkLog` triple entry for {P, PQ, NQ} must read `contradictory`.

**Result**: ✅ **PASS** — all three blocks ran cleanly. The `checkLog` confirms the triple check actually executed and reported `contradictory`.

## Section B — Pairwise Contradiction Control (expect an edge failure, NOT H¹)

Block P: `p(a)`. Block NP: `-p(a)`. These are internally inconsistent as a pair (one says `p(a)`, the other says `-p(a)`). Expected: detected at the *edge* level (internal contradiction in {P, NP}), not as H¹ (no triple involved). The pipeline correctly distinguishes **pairwise contradiction** (a 2-block inconsistency) from **3-wise inconsistency** (a 3-block joint impossibility that is pairwise-satisfiable).

**Result**: ✅ **PASS** — edge-level failure reported, H¹ = 0 as expected.

## Section C — Fully Consistent Control (Blind Men & Elephant; expect H¹ = 0 for the right reason)

Three blocks that are jointly consistent (the classic blind-men-and-elephant pattern: each describes a different part of the same animal, no contradiction). Expected: H¹ = 0, `frustratedTriples` = [], `internallyInconsistent` = []. The "right reason" qualifier matters — the pipeline could report H¹ = 0 either because (a) the blocks are jointly consistent, or (b) the checks didn't run. The `checkLog` must confirm the checks actually ran.

**Result**: ✅ **PASS** — H¹ = 0, `checkLog` confirms checks executed and reported clean.

## Pass-Criteria Summary

All three calls returned cleanly with `checkFailures: []` and the expected verdicts in `checkLog`. The run-log id was **not emitted** in any of the three outputs (the tool does not appear to return one); the test author flags that explicitly rather than fabricating a value.

## Why This Matters

The [[sources/articles/agem-cycle-failures-iter3|3-cycle formal-logic run on the philosophy-of-mind corpus]] reported **3 honest FOL encoding failures** (D1, D6, D10 — nested `->` operators tripping the Prover9 parser). This test corpus exists *precisely* to validate that the pipeline works correctly when given **atomic** propositions — and that the failures in the corpus run were encoding errors, not pipeline errors.

The two files together form a **calibration pair**: this test corpus proves the pipeline works on inputs the parser can handle; the corpus run proves the pipeline reports (rather than papers over) inputs the parser *cannot* handle.

## Connections

- [[sources/articles/agem-cycle-failures-iter3]] — the corpus that motivated this test
- [[concepts/sheaf-cohomology]] — H¹ is a sheaf-cohomology invariant
- [[entities/projects/agem-interface]] — the engine
- [[concepts/evaluate-logical-consistency]] — the MCP tool under test

## Methodological Note

The test design — atomic propositions only, no nested operators — is a **deliberate decoupling of concerns**: separate the engine's cohomological reasoning (this test) from the parser's syntactic tolerance (the corpus run). When the corpus run failed, the failure was *attributable* to the parser; without this test, it would have been ambiguous whether the engine or the parser was the culprit. This is a **good test design pattern**: a test corpus is most valuable when it isolates the variable under test.
