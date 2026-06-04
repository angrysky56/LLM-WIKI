---
summary: Vromen (arXiv 2410.13065) — LLMs are models of Derrida's écriture (writing), not of mind — embeddings as Saussurean signs, writing as the AI's world, next-token sampling as post-structuralist unfixed meaning. Critical reading — it is a rigorous account of operational closure (Luhmann in Derridean dress), correct about pretraining, but the closure is an artifact of choosing Saussure over Peirce; read against Peirce's index it becomes an argument for an external indexical/execution layer. Part 3 conflates semantic indeterminacy with decode-time stochasticity.
tags: [source, semiotics, derrida, saussure, peirce, llm-theory, ecriture, operational-closure, indexicality, scientist-agent]
updated: 2026-06-04T06:21:46Z
created: 2026-06-04T06:21:46Z
---

# Language Models as Semiotic Machines (Vromen)

**Type:** Source — article summary
**Author:** Elad Vromen
**Source:** arXiv 2410.13065v1 · raw clipping at `raw/Language Models as Semiotic Machines.md`
**Relates to:** [[internalizable-index-and-the-harness]] · [[semiotic-founders-council-2026-06-03]] · [[seg-scientist-agent-design]] · [[agentic-research]]

## Thesis

LLMs should be understood not as imitations of human cognition but as *models of language itself* — specifically as models of Derrida's *l'écriture* (writing). The "AI" framing invites the wrong comparison; the right object of modeling is the written sign-system.

## The three moves

1. **Embeddings as Saussurean signs.** word2vec/embedding spaces realize Saussure's relational, *non-referential* meaning — a sign's value is its position among other signs, not a denotation of the world. Vromen adopts non-referential and non-mentalistic as explicit theory-selection constraints.
2. **The object modeled is writing.** Via Derrida's reading of Saussure, the logocentric hierarchy (world → thought → language → writing, with writing as a derivative "sign of a sign") is inverted: writing is primary, and the model's "thought" is a projection *of writing*. For the AI, **writing functions as the world** — a closed textual system with no external engagement (he explicitly brackets RLHF).
3. **Next-token generation as post-structuralist unfixed meaning.** Drawing on Derrida's *Signature Event Context*: meaning is a distribution over signifying forms across contexts; iterability and the structural orphaning of writing from sender/receiver/context yield "no center or absolute anchoring." Sampling/temperature is read as the operationalization of this openness.

## Why it matters here (critical reading)

The paper is a rigorous articulation of **operational closure** — Luhmann's position in Derridean dress. It is *correct* about pretraining: a base model genuinely is pure écriture, self-consistency with the corpus, with no world to be consistent with. That is exactly why it inadvertently proves the [[seg-scientist-agent-design]] premise — inside écriture the self/world distinction has no second term, so the model cannot tell self- from world-consistency.

The crack is the scope line: he brackets RLHF and world-engagement as out of scope, and closes by setting "knowledge" and "truth" aside. That bracketed remainder is the whole point for an autonomous reasoner.

**The Peirce move (our extension):** the closure is partly an artifact of choosing Saussure (dyadic, deliberately non-referential) over Peirce (triadic, with the *index* / secondness). A dyadic semiotics has no slot where the world could enter; a Peircean one does — the index, the sign that is also a brute coupling. Read against Peirce, Vromen's paper flips into the strongest available argument *for* an external indexical layer (execution / verification): if the base model is closed écriture, the only thing that can give it a world is an act whose result it did not author.

## Critique on its own terms

Part 1 (Saussure/word2vec) is sturdy; **Part 3 (SEC/temperature) over-reaches.** Derridean iterability is *semantic* openness (new senders/contexts → new meaning); temperature is *operational* stochasticity at decode time. They are not the same — a model at temperature 0 is deterministic yet its meanings are no less "unfixed" in Derrida's sense. Sampling is wobble/recombination within a fixed landscape, not evidence of post-structuralist meaning. See [[internalizable-index-and-the-harness]].
