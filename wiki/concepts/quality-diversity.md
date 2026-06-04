---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Quality-Diversity (QD) — family of evolutionary algorithms that produce collections of diverse, high-quality solutions, not just one optimum."
tags: [evolutionary-algorithms, quality-diversity, map-elites, open-endedness]
sources: []
status: reference
confidence: 0.9
---

# Quality-Diversity (QD)

**Quality-Diversity (QD)** is a family of evolutionary algorithms (Pugh & Lehman 2016+) that produce *collections* of diverse, high-quality solutions — not a single optimum. Where standard evolutionary algorithms converge on one best solution, QD maintains a behavioral archive of solutions that each perform well in different niches.

Key algorithms in the QD family:
- **MAP-Elites** — bins solutions by behavioral descriptor, keeps best-in-cell
- **DNS (Dominated Novelty Search)** — for solution i, adjusted fitness is mean distance to k nearest better-performing solutions; used in AC/DC
- **CQD (CycleQD)** — task-vector crossover in QD setting; lineage for evolutionary model merging

## Connection to AC/DC

The [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] paper uses DNS as its selection mechanism. DNS is critical: ablating it drops Coverage by ~2.4% at N=3. AC/DC extends QD to the LM population setting — coevolving model populations with task populations.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — uses DNS from QD family
- [[concepts/open-endedness]] — QD is a core OE mechanism
- [[concepts/coevolution]] — AC/DC's model-task coevolution is a QD extension