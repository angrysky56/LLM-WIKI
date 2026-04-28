---
summary: Distinction between what cryptographic protocols can prove (integrity, provenance, state validity) and what they cannot (semantic alignment of outputs to consequences in a world the protocol does not see); decentralized consensus is necessary but not sufficient for AI governance
tags: [analytical-primitive, ai-governance, cryptography, alignment, decentralization, frame]
updated: 2026-04-28T18:26:30Z
created: 2026-04-28T18:26:30Z
---

# Cryptographic vs Semantic Alignment

A distinction relevant to any "decentralized consensus solves alignment" proposal: cryptographic protocols can verify computational properties (integrity, provenance, signature validity, state-transition correctness). They cannot verify semantic properties of outputs in their relationship to a world the protocol does not see.

## What cryptography can prove

- *this code ran* (attestation, ZK execution proofs)
- *this state transition is valid given consensus rules* (blockchain finality)
- *this output came from this model with these weights* (model provenance / signed inference)
- *this signature was produced by this key* (authentication)
- *no node has unilateral authority to alter the ledger* (decentralization properties)

These are real and valuable. They give tamper-resistance, auditability, and provenance — necessary preconditions for any survivable AI governance architecture. The work to build post-quantum cryptographic readiness, verifiable computation, and signed model provenance is not wasted; it is the floor.

## What cryptography cannot prove

- *this output won't enable harm*
- *this model is aligned with human values*
- *this strike package will not kill children*
- *this recommendation is in the recipient's interest*
- *this fine-tune has not stripped safety properties from the base model*

These are predicates over consequences in a substrate the chain has no access to. The same forward pass that drafts a poem drafts a strike package; the bytes are indistinguishable until they meet the world. The chain sees the inference, not the world the inference acts on.

This is not a temporary limitation awaiting a more clever proof system. It is a category boundary. Semantic alignment is a property of the relationship between an output and a world; cryptography operates over the output alone.

## Why this matters for "decentralized alignment" proposals

A common architectural answer to AI governance — particularly attractive once central authority is rejected as a power-concentration trap (see [[institutional-capture-vs-species-framing]]) — is that alignment can be enforced by the network architecture itself, via consensus protocols rejecting unaligned actions. This proposal does meaningful work at the integrity/provenance layer. It does not close the alignment loop, because the protocol cannot evaluate the property the proposal claims it enforces.

In every real implementation, the gap is closed by some governance process: a foundation, a token-weighted vote (capital captures it), or a small group of core developers (oligarchy under a new name). Bitcoin maximalism solved a narrower problem and still couldn't escape this; it just hid the governance behind ossification.

The kingmaker comes back in through the protocol-governance layer. The trust assumption is not eliminated — it is relocated.

## The fine-tune / adapter problem as a concrete instance

LoRAs, modular adapters, and lightweight fine-tunes can attach to a frozen base model and re-shape its behavior — including stripping safety training — without rewriting weights. Cryptographic provenance can prove *which* adapter ran on *which* base model. It cannot prove that the adapter's behavior is aligned, because alignment is not a property of the weights but of the weights' interaction with future inputs in the world.

There is currently no equivalent of Know-Your-Customer for fine-tunes, no provenance regime for adapters, no audit standard for what gets bolted onto a base model after release. This is one of the largest unaddressed governance gaps, and it is not solvable by better cryptography alone.

## Implication

Decentralized cryptographic infrastructure is necessary but not sufficient for survivable AI governance. It buys tamper-resistance, provenance, and removes some pathologies of central authority. It does not constitute alignment. Pretending the protocol can carry the moral weight is the same move alignment research made when it pretended RLHF could carry it — offloading a problem into mathematics that the mathematics cannot hold.

Where the moral weight actually has to live, if anywhere: see [[frame-transmission]].

## Related

- [[institutional-capture-vs-species-framing]] — why central authority fails as the alternative
- [[frame-transmission]] — what actually carries the moral work
- [[spin-vs-substrate]] — adjacent failure mode; treating proof-of-protocol-integrity as proof-of-system-alignment
