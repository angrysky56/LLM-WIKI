---
summary: Compiling deterministic programs into transformer weights — the residual stream as a register file, attention as lookup, FFN as arithmetic, layers as machine steps; a substrate for executable symbolic reasoning inside frozen transformers
tags: [transformers, compilation, deterministic-computation, register-allocation, neuro-symbolic, computed-weights, vm, eml]
updated: 2026-06-03T14:08:54Z
---

---
created: 2026-05-25
updated: 2026-06-03
type: concept
summary: Compiling deterministic programs into transformer weights — the residual stream as a register file, attention as lookup, FFN as arithmetic, layers as machine steps; a substrate for executable symbolic reasoning inside frozen transformers
tags: [transformers, compilation, deterministic-computation, register-allocation, neuro-symbolic, computed-weights, vm, eml]
sources:
  - "[[sources/news/2026/transformer-vm-moran-2026]]"
  - "[[sources/news/2026/openai-o3-erdos-conjecture-breakthrough-2026]]"
status: active
confidence: 0.7
---

# Transformer VM (Moran 2026)

The Transformer VM is a 2026 research line, crystallized by Sean Moran's "I Built a Tiny Computer Inside a Transformer" (April 2026, [Towards Data Science](https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/)) and Percepta's "Constructing an LLM Computer" companion piece, demonstrating that transformer weights can be **analytically constructed** to execute a deterministic program — no training required. The approach treats the transformer as a programmable machine: given a computation graph and a schedule, you build the weights directly. This is fundamentally different from the standard ML paradigm where weights emerge from gradient descent.

## The Transformer as a Computer

The central reframing is a clean mapping from transformer components to classical computer architecture:

| Transformer Component | Computer Analogue |
|---|---|
| Residual stream | Working memory / registers |
| Hidden dimensions | Register slots (variables like x, y, z) |
| Attention heads | Lookup and routing (case-matching) |
| Feed-forward blocks | Local computation (arithmetic) |
| Residual addition | Write-back (commit state update) |
| Each layer | Two machine steps (attention half-layer + FFN half-layer) |

The residual stream evolves like a register file: `[x=B, y=·, z=·]` → `[x=B, y=5, z=·]` → `[x=B, y=5, z=6]`. Each layer performs one read, one compute, and one write — the standard fetch-decode-execute cycle, expressed in attention + FFN + residual arithmetic.

## The Compilation Process

Building a transformer that executes a specific program is a **compiler backend problem**, not a learning problem:

1. **Computation graph** defines the program (e.g., a scientific calculator's operations)
2. **Schedule** decides which operations happen in which half-layer (latency vs. parallelism)
3. **Slot assignment** maps variables to hidden-state dimensions — this is *register allocation*
4. **Liveness analysis** determines when slots can be reused (dead variable → free register)
5. **Weight construction** converts symbolic expressions to slot-indexed vectors placed into embedding, query, key, value, FFN, and output weight matrices

A symbolic expression like `3·x - 2·y + z` with x→slot3, y→slot4, z→slot5 becomes a sparse vector `[0, 0, 0, 3, -2, 1, 0, ...]`. The compiler replaces variable names with slot addresses. The result is a weight matrix that, when applied to a residual stream with x, y, z in the right slots, produces the right intermediate value — exactly, with no noise.

This is the key insight: **for deterministic computation, you don't need to learn**. You can construct.

## Two Approaches: Compiled Machine vs. Compiled Interpreter

The 2026 work splits into two regimes:

**Moran (compiled machine):** The transformer is the program. The weights execute a specific computation graph. Simpler, more transparent, faster, but the transformer can only run that one program.

**Percepta (compiled interpreter):** The transformer is a general-purpose computer. The weights implement a WebAssembly (or similar) interpreter, and the program is supplied at inference time via prompt. More general — the same transformer can run any WASM program — but heavier, and the program must be expressed in a format the interpreter understands.

The trade-off is the standard compiled-vs-interpreted trade-off, now applied to neural-network computation. Compiled machines are faster and more transparent; interpreters are more flexible. The two are not mutually exclusive — you could compile a small interpreter for a domain-specific language (e.g., EML) and get a middle ground.

## Convex Hull Attention — A Geometric Optimization

For long deterministic traces, attention lookup can be reinterpreted geometrically: a query defines a direction, and the selected key is the point furthest in that direction. For 2D attention heads, this is a convex-hull search — interior points can be discarded, reducing lookup from O(n) to O(k + log n). This is a real algorithmic improvement, not just a re-description.

The optimization degrades in higher dimensions as the convex hull becomes dense, but for low-dimensional attention (e.g., 2D or 4D heads used for routing), it's a meaningful win. The 2026 work suggests using low-dimensional heads for lookup-heavy operations and reserving high-dimensional heads for representational richness.

## Connection to EML — The Minimal Compiled Transformer

The most interesting extension of the Transformer VM idea connects to the [[eml-operator]] (Odrzywołek 2026). EML is the single binary operator `eml(x,y) = exp(x) - ln(y)` that, together with the constant 1, generates all standard elementary functions — the continuous-domain analogue of NAND. Its grammar is `S → 1 | eml(S, S)`, where every node of the expression tree is identical.

If every elementary function reduces to `eml(x,y)`, then a compiled transformer executing EML programs needs only:

- **One attention pattern** (lookup: map inputs to eml arguments)
- **One FFN computation** (compute `exp(a) - ln(b)`)
- **Residual write-back** (store result for next step)

Each layer is one EML step. The residual stream is a stack of EML intermediate values. A depth-7 EML tree for `ln(x)` requires 7 half-layers. A full scientific calculator compiled into a transformer has depth equal to the deepest EML tree needed.

The compiler backend is **trivial for EML** because the grammar is uniform — every node is identical. Register allocation, scheduling, and slot assignment all simplify dramatically when there's only one operation type. This is the minimal possible compiled transformer computer: one operation, one attention pattern, one FFN computation.

The Percepta + EML synthesis: instead of compiling a WebAssembly VM, compile an EML evaluator. The interpreter is simpler (one instruction), the programs are uniform binary trees, and the result can compute any elementary function. This is the **most compact possible executable transformer** — a frozen weight matrix that evaluates any EML expression supplied at inference.

## Connection to OpenPraparat

The dual-mode structure (compiled + learned) parallels the [[utimula-openpraparat-2025]] cell architecture:

- **Compiled mode** (transformer VM): deterministic, interpretable, fast, brittle outside its compiled program
- **Learned mode** (LLM in standard training): flexible, statistical, opaque, robust to novel inputs
- **OpenPraparat's gene + bookmarker**: a gene string (= program) is read sequentially by a bookmarker (= program counter), producing deterministic actions (EXPAND, CONNECT, DISCONNECT, TRANSITION = opcodes). The cell's neural network handles the non-deterministic, environment-responsive part.

The Transformer VM and OpenPraparat are structurally identical architectures: a deterministic, programmable inner loop + a flexible, learned outer loop. The transformer-VM literature makes the compiled side explicit and gives it a compiler-style implementation.

## Why This Matters for AI Architecture

The Transformer VM line matters because it shows that **frozen transformers can execute exact programs**. This has several implications:

1. **Interpretability**: When a transformer's weights are analytically constructed (not trained), every weight has a known meaning. This is a path to interpretable AI that doesn't require post-hoc analysis of trained networks.
2. **Verification**: A compiled transformer's behavior is provably equivalent to a known program. This addresses the verification problem for safety-critical applications.
3. **Hybrid systems**: Standard LLM + compiled transformer. The LLM handles the flexible, general reasoning; the compiled transformer handles the deterministic, exact computation (arithmetic, lookup, code execution). This is structurally similar to the [[bounded-structured-memory]] pattern: the LLM is the slow, flexible layer; the compiled transformer is the fast, exact layer.
4. **Mathematical reasoning**: The compiled-transformer regime is exactly what's needed for verifiable math. The [[mathematical-reasoning-ai]] trajectory — competition math → formal proof → autonomous conjecture falsification — depends on the model being able to *verify* its own reasoning step-by-step. A compiled EML evaluator is the substrate where this verification is exact.

## Open Questions

1. **Scalability**: How large can compiled transformers be before construction becomes infeasible? Moran's examples are small; how does the approach scale to 7B+ parameter models with hundreds of layers?
2. **Approximate compilation**: Can the technique be extended to compiled transformers that *approximate* a function (like a neural network) but with formal guarantees on the approximation error?
3. **The compiled-LLM boundary**: When should a task be handled by the compiled (exact) part vs. the LLM (statistical) part of a hybrid system? The boundary is the open architectural question.
4. **EML performance**: Is an EML-compiled transformer fast enough for production use? Each EML step requires `exp` and `ln` evaluations, which are expensive compared to standard FFN matrix multiplies. The EML tree depth for common functions may be too deep for real-time inference.
5. **Learning vs. compiling hybrid**: Can a transformer be *partially* compiled (some layers analytically constructed) and *partially* trained (others learned)? This would combine the best of both regimes — exact computation where possible, statistical flexibility where necessary.

## Connections
- [[eml-operator]]: the minimal instruction set for compiled transformers
- [[odrzywolek-eml-2026]]: the EML discovery paper
- [[minimal-generative-architectures]]: synthesis page on minimal primitives
- [[utimula-openpraparat-2025]]: dual-mode compiled + learned architecture
- [[mathematical-reasoning-ai]]: the application regime for compiled transformers
- [[agents]]: agents that may use compiled transformers for exact computation
- [[neuro-symbolic]]: the broader field of neural + symbolic systems
- [[mixture-of-recursions]]: another adaptive-computation approach (linked)
- [[synthesis/minimal-generative-architectures]]: synthesis page on the MGA pattern
- [[sources/news/2026/transformer-vm-moran-2026]]: the Moran 2026 source
- [[sources/news/2026/openai-o3-erdos-conjecture-breakthrough-2026]]: the 2026 Erdős result
- [[sources/articles/llm-kernel-optimization]]: related LLM optimization work
- [[open-ended-evolution]]: the evolutionary-design perspective
- [[symbolic-regression]]: another symbolic-learning regime
- [[concepts/transformer-vm-moran-2026]]
- [[concepts/eml-operator]]
- [[concepts/mathematical-reasoning-ai]]
- [[concepts/odrzywolek-eml-2026]]
- [[concepts/utimula-openpraparat-2025]]
- [[concepts/minimal-generative-architectures]]
- [[concepts/agents]]
- [[concepts/neuro-symbolic]]
- [[concepts/symbolic-regression]]
- [[concepts/open-ended-evolution]]
- [[concepts/llm-kernel-optimization]]
- [[wiki/index]]

## Source Anchors
- [[sources/news/2026/transformer-vm-moran-2026]] — Moran's Towards Data Science article
- [[sources/papers/odrzywolek-eml-2026]] — the EML discovery paper
- [[sources/news/2026/openai-o3-erdos-conjecture-breakthrough-2026]] — the 2026 mathematical-reasoning breakthrough
- [[sources/papers/utimula-openpraparat-2025]] — the OpenPraparat dual-mode architecture

## See Also
- [[concepts/eml-operator]]
- [[concepts/mathematical-reasoning-ai]]
- [[concepts/odrzywolek-eml-2026]]
- [[concepts/utimula-openpraparat-2025]]
- [[concepts/minimal-generative-architectures]]
- [[concepts/agents]]
- [[concepts/neuro-symbolic]]
- [[concepts/symbolic-regression]]
- [[concepts/open-ended-evolution]]
- [[concepts/llm-kernel-optimization]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/mop-edm-cognitive-architecture]]
- [[transformer-vm-moran-2026]]
- [[transformers]]
- [[machine-learning]]
- [[log]]
- [[wiki/index]]
