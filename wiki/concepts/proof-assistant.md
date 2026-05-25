---
created: 2026-05-29
updated: 2026-06-08
type: concept
summary: Interactive software for constructing and verifying mathematical proofs — Coq, Isabelle, Lean, Agda — with landmark verification projects including seL4 and CompCert
tags: [formal-methods, theorem-proving, tools, verification]
sources: 
status: active
confidence: 0.8
---

# Proof Assistant

A proof assistant (interactive theorem prover) is software that helps humans construct and verify mathematical proofs. The distinguishing feature is machine-checked proof verification: every step in the proof is checked by a small trusted kernel, ensuring the result is sound regardless of the tool's complexity.

## How They Work

Proof assistants maintain a **proof state** — a collection of goals (theorems to prove). The user constructs a proof by issuing **tactics** (commands that transform the proof state). Each tactic application is checked by the kernel. Once a theorem is proved, it can be used as a lemma in subsequent proofs — the library accumulates.

Key properties:
- **Type theory foundation**: Proofs as programs, propositions as types (Curry-Howard correspondence)
- **Trusted kernel**: Small, simple checker; everything else is untrusted user code
- **Rich automation**: Decision procedures, symbolic execution, AI-assisted tactics

## The Major Proof Assistants

### Coq
Based on the Calculus of Inductive Constructions (CIC). The foundational system for the MathComp library (finite group theory, real analysis), CompCert verified C compiler, and the Four-color theorem proof. Strong in program verification and mathematical foundations.

### Isabelle
Generic proof assistant instantiated with HOL (Higher Order Logic). Used for the seL4 microkernel verification — the landmark achievement in software verification. Isabelle's Isar proof language is designed for human-readable proofs.

### Lean
Modern proof assistant with emphasis on programmer ergonomics. Lean 4 is also a functional programming language with dependent types. Mathlib is the community-built mathematical library — rapidly growing, covering analysis, algebra, topology, and more.

### Agda
Dependently typed programming language with a terminating checker. Based on Martin-Löf Type Theory. Used extensively in programming language research and type theory.

## AI Alignment Applications

Proof assistants are relevant to AI alignment:

1. **Formal verification of reasoning chains**: The [[load-bearing-reasoning]] framework identifies critical inference steps; proof assistants could verify invariants on those steps (e.g., "this constitutional-ai reasoning chain never violates safety constraints")

2. **Mechanistic interpretability**: Circuit-level verification — proving properties of neural network circuits against formal specifications

3. **AI agent safety protocols**: Multi-agent coordination protocols can be verified for safety, liveness, and termination properties

4. **Constitutional AI as formal specification**: Encoding CAI principles as formal invariants and proving system adherence

5. **Reward hacking detection**: Specifying "benign behavior" formally and checking whether a learned policy satisfies the specification

## Landmark Verification Projects

| Project | System | What Was Proved |
|---------|--------|----------------|
| seL4 microkernel | Isabelle/HOL | Functional correctness — implementation matches specification |
| CompCert | Coq | The verified C compiler produces correct output for all valid inputs |
| Four-color theorem | Coq | The theorem that any map can be colored with four colors |
| Feit-Thompson | Coq | Every finite group of odd order is solvable |
| Bedrock | Coq | Verified low-level programs with machine-checked proofs |

## Connections

- [[formal-methods]] — the broader field
- [[interactive-theorem-proving]] — the practice of using proof assistants
- [[formal-verification]] — application to software/hardware verification
- [[isabelle-hol]] — specific proof assistant with major verification results
- [[mathematical-reasoning]] — the underlying mathematics
- [[load-bearing-reasoning]] — identifying which reasoning steps need formal verification
- [[reward-hacking]] — reward hacking as violation of formal behavioral specifications
- Concept: [[category-theory]]
- Concept: [[isabelle]]
