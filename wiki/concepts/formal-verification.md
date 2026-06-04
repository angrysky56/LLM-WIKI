---
created: 2026-05-28
updated: 2026-06-08
type: concept
summary: Mathematically proving program correctness against specifications — pre/postconditions, invariants, formal verification vs testing
tags: [formal-methods, verification, software-engineering, safety, correctness]
sources: 
status: active
confidence: 0.7
---

# Formal Verification

Formal verification is the application of [[formal-methods]] to prove that a program satisfies a formal specification — that the implementation is correct with respect to what it should do, not just that it passes tests.

## What It Is

Formal verification establishes mathematical proof that a system respects its specification. Unlike testing (which samples execution paths) or static analysis (which approximates behavior), formal verification provides exhaustive proof of correctness for the specified properties.

Two main approaches:

### Hoare Logic / Deductive Verification
Write preconditions and postconditions for program fragments, then prove that the code establishes its postconditions from its preconditions. Tools: Why3, Frama-C, SPARK (for Ada).

### Model Checking (Algorithmic Verification)
Exhaustively explore the state space of a concurrent or reactive system to verify temporal logic specifications. Tools: CBMC, SPIN, nuXmv, OFMC.

## Key Concepts

**Invariant**: A property that holds at all points during execution. Proving loop invariants is central to deductive verification.

**Precondition**: What must be true before a program fragment executes for its specification to apply.

**Postcondition**: What must be true after a program fragment completes, assuming the preconditions held.

**Refinement**: Showing that a more abstract specification is correctly implemented by a more concrete one. Key for compositional verification.

## Why It Matters in AI Context

Formal verification is increasingly relevant to AI systems:

1. **LLM-generated code**: Who verifies the verifier? If formal verification tools are used to check AI-generated code, the toolchain itself must be sound
2. **AI agent safety invariants**: Can we prove an agent won't take harmful actions under specific conditions? E.g., a code agent shouldn't delete `/etc` or exfiltrate secrets
3. **Reward hacking detection**: If we can formally specify "benign behavior" vs "reward-hacked behavior," we can check whether a policy satisfies the specification
4. **Multi-agent coordination**: Formal protocols for agent communication can be verified for deadlock freedom, liveness, and safety

The [[concepts/load-bearing-reasoning]] framework identifies critical inference steps; formal verification could prove invariants on those steps — e.g., "this reasoning chain never violates the constitution."

## Major Projects

- **seL4**: Formally verified microkernel; proof machine-checked in Isabelle/HOL
- **CompCert**: Verifying C compiler — the output provably matches the source semantics
- **Verifiable Software Toolchain (VST)**: CompCert's verification framework in Coq; proves safety properties of CompCert-compiled programs
- **K Framework**: executable semantic framework; allows formal definition of languages and verification of properties

## Limitations

- **Specification correctness**: You can only verify against what you specified. Wrong specifications → wrong results
- **Scalability**: State explosion; fully verifying concurrent systems remains expensive
- **Human cost**: Requires expertise in both the domain and the verification toolchain
- **Model vs implementation**: Verifying a model of a system doesn't verify the implementation matches the model

## Connections
- [[concepts/attention-monoidal-closure]]
- [[concepts/category-theory]]
- [[entities/tools/isabelle]]
- [[concepts/proof-assistant]]
- [[log]]
- [[concepts/interactive-theorem-proving]]
- [[concepts/isabelle-hol]]
- [[concepts/reward-hacking]]
- [[entities/tools/isabelle-hol]]
- [[concepts/categorical-reasoning]]
- [[sources/documentation/isabelle-installation]]
- [[concepts/formal-methods]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/formal-verification]]
- [[concepts/mathematical-reasoning]]
- [[entities/tools/prover9]]
- [[wiki/index]]
- [[formal-verification]]

- [[formal-methods]] — the broader field
- [[proof-assistant]] — tools like Coq, Isabelle, Lean for interactive verification
- [[interactive-theorem-proving]] — the practice of constructing machine-checked proofs
- [[isabelle-hol]] — specific proof assistant with major verification results
- [[concepts/load-bearing-reasoning]] — causal mediation analysis for identifying verification targets
- [[reward-hacking]] — reward hacking as a violation of formal behavioral specifications
- Concept: [[attention-monoidal-closure]]
- Concept: [[categorical-reasoning]]
- Concept: [[category-theory]]
- Concept: [[isabelle]]
- Concept: [[mathematical-reasoning]]
- Concept: [[prover9]]
