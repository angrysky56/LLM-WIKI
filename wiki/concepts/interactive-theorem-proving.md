---
created: 2026-05-28
updated: 2026-06-08
type: concept
summary: Human-guided machine-checked mathematical proof construction — the practice of using proof assistants (Coq, Isabelle, Lean) to verify complex proofs
tags: [formal-methods, mathematics, theorem-proving, proof-assistant, logic]
sources: 
status: active
confidence: 0.8
---

# Interactive Theorem Proving

Interactive theorem proving (ITP) is the practice of constructing machine-checked mathematical proofs with a human prover guiding the process. Unlike automated theorem proving (which is fully automatic), ITP involves a dialogue: the human proposes a proof step, the system checks it, and the process continues until the proof is complete.

## Core Concept

A proof assistant maintains a **proof state** — a set of goals to prove. Each step (applying a lemma, introducing a variable, rewriting) transforms the proof state until all goals are discharged. Every step is checked for logical validity by the kernel, making the result trustworthy regardless of the tool's complexity.

Key distinction:
- **Trustworthy core**: The type checker / proof kernel is small and verified
- **Rich library**: Large mathematical libraries (analysis, algebra, etc.) built on top
- **Human guidance**: Complex proofs require human insight; automation helps but doesn't replace judgment

## The Major Systems

### Coq
Based on the Calculus of Inductive Constructions (CIC) — a dependently typed lambda calculus. Coq's stdlib is extensive; the CompCert verified C compiler and the Four-color theorem proof are landmark achievements. The Univalent Foundations (HoTT) project is built in Coq.

### Isabelle
Generic proof assistant with a distinctive "wrapper" architecture — the generic framework (Isar proof language, simplifier) is instantiated with specific logic (FOL, ZFC, HOL). The seL4 microkernel verification is Isabelle/HOL.

### Lean
More recent, with an emphasis on programmer ergonomics and a powerful macro/automation system. Lean 4 is a full programming language (functional, dependent types) with a built-in tactic system. Mathlib is a massive community-driven mathematical library.

### Agda
Dependently typed programming language that doubles as a proof assistant. Based on Martin-Löf type theory. Used heavily in programming language theory research.

## The Role in AI Alignment

ITP tools are increasingly relevant to AI safety research:

1. **Verifying reasoning chains**: The [[load-bearing-reasoning]] framework identifies critical inference steps; proof assistants could formally verify invariants on those steps (e.g., "this constitutional-ai reasoning chain never produces harmful output")

2. **Mechanistic interpretability**: Circuit-level verification — specifying what a circuit should compute and proving what it actually computes, finding the gap

3. **Constitutional AI as formal specification**: CAI's principles are a kind of specification; ITP could encode and verify that a system's behavior adheres to those principles

4. **Multi-agent protocols**: Formal verification of agent coordination protocols for safety properties (no harmful actions, information barriers, termination guarantees)

## Key Concepts

**Tactic**: A proof step — a command that manipulates the proof state. Tactics can be composed into complex proof scripts. E.g., `intro`, `apply`, `rewrite`, `induction`, `cases`.

**Lemma/Theorem**: A proved statement. Once proved, a lemma can be used in subsequent proofs. The library of proved lemmas grows over time.

**Inductive type**: A type defined by its constructors — e.g., natural numbers are `0` and `S(n)`. Induction principles are derived automatically. The foundation of formalized mathematics.

**Dependent type**: A type that depends on a value — e.g., `Vector A n` (vectors of length n). Enables encoding specifications in types (e.g., "sorted list").

## Notable Achievements

- **Four-color theorem** (Coq, 2005): First machine-checked proof of a century-old problem
- **seL4 microkernel** (Isabelle/HOL, 2009): Functional correctness proof — implementation matches specification
- **CompCert** (Coq, 2007): Verified C compiler — no miscompilation bugs
- **Odd Order Theorem** (Coq, 2012): Feit-Thompson theorem — major group theory result
- **Liquid fluid dynamics** (Lean, 2023+): Formalizing fluid dynamics

## Limitations

- **Steep learning curve**: ITP requires learning both the formalism and the specific tool
- **Proof engineering**: Large proofs require managing complexity — structuring, abstraction, libraries
- **Automation gap**: Full proofs require human insight; automation exists but is limited
- **Scalability**: Full verification of complex systems (OS kernels, compilers) requires person-years

## Connections
- [[entities/tools/isabelle-hol]]
- [[concepts/formal-methods]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/formal-verification]]
- [[concepts/mathematical-reasoning]]
- [[wiki/index]]
- [[concepts/category-theory]]
- [[concepts/proof-assistant]]
- [[log]]
- [[concepts/interactive-theorem-proving]]
- [[concepts/isabelle-hol]]
- [[interactive-theorem-proving]]

- [[formal-methods]] — the broader field
- [[formal-verification]] — applying ITP to verify software/hardware systems
- [[proof-assistant]] — the tools themselves (Coq, Isabelle, Lean, Agda)
- [[mathematical-reasoning]] — the broader practice of rigorous deduction
- [[category-theory]] — provides high-level organizing principles for formal mathematics; composition as morphism
- [[load-bearing-reasoning]] — causal mediation for identifying which reasoning steps need formal verification
- Concept: [[isabelle-hol]]
