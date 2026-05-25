---
summary: Moran (2026) — analytically compiling programs into transformer weights; residual stream as registers, attention as lookup, FFN as arithmetic, layers as machine steps; connects to EML as minimal instruction set for compiled transformers
tags: [transformers, compilation, deterministic-computation, register-allocation, EML, neuro-symbolic, computed-weights]
updated: 2026-04-15T00:21:24Z
created: 2026-04-15T00:21:24Z
---

# Compiled Computation Inside Transformers

**Author:** Sean Moran
**Source:** [Towards Data Science](https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/)
**Published:** 2026-04-13
**Code:** [transformer-vm](https://github.com/sjmoran/transformer-vm)
**Related:** [Percepta — Constructing an LLM Computer](https://www.percepta.ai/blog/constructing-llm-computer)

## Core Idea

Instead of training a transformer to discover algorithms through optimization, treat it as a **programmable machine** and analytically construct weights that execute a deterministic program. No training required — if you have a computation graph and a schedule, you build the weights directly.

## The Transformer as a Computer

| Transformer Component | Computer Analogue |
|---|---|
| Residual stream | Working memory / registers |
| Hidden dimensions | Register slots (variables like x, y, z) |
| Attention heads | Lookup and routing (case-matching) |
| Feed-forward blocks | Local computation (arithmetic) |
| Residual addition | Write-back (commit state update) |
| Each layer | Two machine steps (attention half-layer + FFN half-layer) |

### Execution Loop

1. Read current state from residual stream
2. Compute an update (via attention lookup or FFN arithmetic)
3. Write update back via residual addition

The residual stream evolves like a register file: `[x=B, y=·, z=·]` → `[x=B, y=5, z=·]` → `[x=B, y=5, z=6]`.

## Compilation Process

This is literally a **compiler backend problem**:

1. **Computation graph** defines the program
2. **Schedule** decides which operations happen in which half-layer
3. **Slot assignment** maps variables to hidden-state dimensions (= register allocation)
4. **Liveness analysis** determines when slots can be reused (dead variable → free register)
5. **Weight construction** converts symbolic expressions to slot-indexed vectors placed into embedding/query/key/value/FFN/output weight matrices

A symbolic expression like `3·x - 2·y + z` with x→slot3, y→slot4, z→slot5 becomes a sparse vector `[0, 0, 0, 3, -2, 1, 0, ...]` — the compiler replaces variable names with slot addresses.

## Two Approaches

**Moran (this article):** Compiles the *target program itself* into weights. Dedicated compiled machine for a fixed computation graph. Simpler, more transparent.

**Percepta:** Compiles a *general interpreter* (WebAssembly VM) into weights, then supplies programs at inference time via prompt. More general, but heavier.

## Scaling: Convex Hull Attention

For long deterministic traces, attention lookup can be reinterpreted geometrically: query defines a direction, the selected key is the point furthest in that direction. For 2D attention heads, this is a convex-hull search — interior points can be discarded, reducing lookup from O(n) to O(k + log n). Degrades in higher dimensions as hull becomes dense.

## Connection to EML

This is where it gets interesting for the [[eml-operator]] and [[minimal-generative-architectures]]:

**EML as the instruction set for a compiled transformer.** If every elementary function reduces to `eml(x,y) = exp(x) - ln(y)`, then a compiled transformer executing EML programs needs only:
- **One attention pattern** (lookup: map inputs to eml arguments)
- **One FFN computation** (compute exp(a) - ln(b))
- **Residual write-back** (store result for next step)

Each layer is one EML step. The residual stream is a stack of EML intermediate values. A depth-7 EML tree for ln(x) requires 7 half-layers. A full scientific calculator compiled into a transformer would have depth equal to the deepest EML tree needed.

**The compiler backend is trivial for EML** because the grammar is `S → 1 | eml(S, S)` — every node is identical. Register allocation, scheduling, and slot assignment all simplify dramatically when there's only one operation type. Compare this to compiling arbitrary programs with heterogeneous operations.

**Percepta's interpreter approach + EML:** Instead of compiling a WebAssembly VM, compile an EML evaluator. The interpreter is simpler (one instruction), the programs are uniform binary trees, and the result can compute any elementary function. This is the minimal possible compiled transformer computer.

## Connection to OpenPraparat

The book/bookmarker mechanism in [[utimula-openpraparat-2025]] is structurally identical to this transformer-computer: a gene string (= program) is read sequentially by a bookmarker (= program counter), producing deterministic actions (EXPAND, CONNECT, DISCONNECT, TRANSITION = opcodes). The cell's neural network then handles the non-deterministic, environment-responsive part — exactly the dual-mode architecture this article proposes (deterministic compiled mode + flexible learned mode).

## Connections

- [[eml-operator]] — EML as the instruction set for the simplest possible compiled transformer
- [[minimal-generative-architectures]] — this is MGA applied to transformer internals
- [[sheffer-stroke]] — one operation type (EML/NAND) simplifies compilation to uniform circuits
- [[utimula-openpraparat-2025]] — book/bookmarker = compiled program; neural network = learned mode
- [[alphaevolve]] — could evolve optimal compilation schedules and slot assignments
- [[symbolic-regression]] — EML master trees as compilable programs for formula discovery inside transformers
- [[llm-kernel-optimization]] — compiled transformer computation as an alternative to external kernel calls
