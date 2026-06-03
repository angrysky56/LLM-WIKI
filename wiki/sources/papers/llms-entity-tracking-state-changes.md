---
summary: LMs don't track entity states incrementally — they aggregate all relevant information in parallel at the final token once the query is evident. REMOVE uses a fragile global suppression tag, revealing failure modes that mechanistic analysis predicts.
tags: [entity-tracking, mechanistic-interpretability, language-models, ICML-2026]
updated: 2026-06-03T14:53:26Z
---

---
created: 2026-05-29
updated: 2026-06-03T14:48:00Z
type: source
paper_id: 2605.30233
summary: LMs don't track entity states incrementally — they aggregate all relevant information in parallel at the final token once the query is evident. REMOVE uses a fragile global suppression tag, revealing failure modes that mechanistic analysis predicts.
tags: ['entity-tracking', 'mechanistic-interpretability', 'language-models', 'ICML-2026']
authors: 
venue: ICML main conference 2026
sources: https://arxiv.org/abs/2605.30233
status: active
confidence: 0.85
---

# Do Language Models Track Entities Across State Changes?

Tang, Zhao, Franco, Wijaya, Mueller, Schuster, Kim — ICML 2026

## Paper

[arXiv:2605.30233](https://arxiv.org/abs/2605.30233) | [PDF](https://arxiv.org/pdf/2605.30233v1)

## Abstract

Entity tracking (ET) — the ability to maintain a coherent representation of how entity states change over the course of a context — is a fundamental reasoning skill. Prior work has studied how transformer language models perform entity binding *without* state changes. This paper investigates ET in more realistic scenarios featuring **multiple natural-language state-changing operations**.

**Core finding:** LMs do not incrementally track world states across tokens or query-relevant states across layers. Instead, they **aggregate all relevant information in parallel at the last token**, but only once the query becomes evident. The authors characterize this as solving a fundamentally sequential task using a non-sequential strategy.

The paper further dissects three operations — `PUT`, `REMOVE`, `MOVE` — and finds that:

- **`PUT`** writes entity state
- **`REMOVE`** deletes entity state via a **fragile global suppression tag**
- **`MOVE`** relocates entities between containers

The global removal mechanism predicts specific behavioral failure modes, which the authors confirm experimentally. They then provide a mechanistic fix by nullifying the tag, partially recovering performance.

**Broader contribution:** A demonstrated synergy between behavioral and mechanistic analysis — behavioral results generate hypotheses for mechanistic investigation, and mechanistic insights expose blind spots in behavioral benchmarks.

## Key Concepts

- **Entity Tracking (ET):** Maintaining accurate state representations of entities as they undergo changes through a context
- **Entity Binding:** Associating an entity with its properties/states without explicit state change
- **Global Suppression Tag:** A single attention mechanism that globally suppresses removed entities rather than incrementally updating state representations
- **Non-incremental ET:** Aggregating all relevant information in parallel at inference time rather than updating state incrementally as the context unfolds

## Background and Motivation

Prior work on entity tracking in LMs has focused on relatively simple binding problems — e.g., "the apple is red, the bowl is blue; where is the red object?" — problems that don't involve state changes. Real-world reasoning, however, requires tracking entities through sequences of put, remove, and move operations expressed in natural language.

The authors identify a gap: there is limited understanding of how non-toy LMs handle ET problems of realistic difficulty in natural language. This paper begins to fill that gap.

## Methodology

The authors perform experiments with transformer-based LMs on ET tasks involving multiple sequential state-changing operations. They combine:

1. **Behavioral evaluation** — probing where and when LMs correctly answer ET queries
2. **Mechanistic analysis** — identifying the internal mechanisms (attention patterns, specific components) responsible for ET behavior

This two-pronged approach allows them to not only document behavior but explain *why* the model behaves that way, and to predict failure modes before confirming them empirically.

## Key Findings

### Finding 1: Non-incremental State Aggregation

LMs do not track entity states incrementally across tokens or query-relevant states across layers. Instead:

- Information relevant to an ET query is aggregated **in parallel** at the position of the final token
- This aggregation only occurs once the query becomes evident (i.e., when the model knows what question to answer)
- The model effectively solves a sequential task (multiple state changes in order) with a fundamentally non-sequential strategy

### Finding 2: Operation-Specific Mechanisms

The three state-changing operations are implemented differently:

| Operation | Mechanism | Notes |
|-----------|-----------|-------|
| `PUT` | Writes entity state directly | Standard write operation |
| `REMOVE` | **Global suppression tag** | Single marker that globally suppresses the entity; fragile — predicts failure modes |
| `MOVE` | Relocates entity between containers | Move semantics between container entities |

### Finding 3: REMOVE is Fragile

The `REMOVE` operation's reliance on a global suppression tag makes it brittle:

- The tag is a single attention mechanism rather than an incremental update
- Predicted failure modes (confirmed behaviorally):
  - The model may fail to suppress the entity in certain contexts
  - Cross-contamination between similar entity representations
  - Degraded performance when multiple remove operations accumulate
- **Mechanistic fix demonstrated:** Nullifying the global suppression tag partially restores performance

### Finding 4: Behavioral–Mechanistic Synergy

The paper illustrates a productive feedback loop:

1. **Behavioral → Mechanistic:** Observed failure modes prompt investigation of internal mechanisms
2. **Mechanistic → Behavioral:** Understanding the mechanism reveals *why* failures occur and predicts failure modes that behavioral tests then confirm
3. This interaction produces stronger evaluations than either approach in isolation

## Significance

The finding that LMs use a **non-incremental parallel aggregation strategy** for inherently sequential entity-tracking tasks has implications for:

- **Model design:** Architectures that support true incremental state tracking may be needed for robust multi-step reasoning
- **Evaluation:** Benchmarks that only test final-state accuracy may miss intermediate reasoning failures
- **Interpretability:** The fragile global suppression tag for REMOVE is a specific, actionable target for mechanistic debugging and repair

## Related Work

The paper is situated at the intersection of:

- Entity tracking and coreference resolution in LMs
- Mechanistic interpretability of transformer attention mechanisms
- Behavioral evaluation of LMs on reasoning tasks

It builds on prior work in [[entity-tracking-externalization]], [[mechanistic-interpretability]], and [[attention-mechanism]] in transformers.

## Connections

- [[entity-tracking-externalization]] — entity-tracking as a cognitive externalization pattern (related entity project)
- [[mechanistic-interpretability]] — the broader field of mechanistic analysis
- [[attention-mechanism]] — the architectural component central to the suppression-tag finding
- [[transformer-architecture]] — model family investigated
- [[ICML-2026]] — venue (if a tag page exists; otherwise drop)

## References

- arXiv:2605.30233 [cs.CL]
- ICML 2026 main conference
