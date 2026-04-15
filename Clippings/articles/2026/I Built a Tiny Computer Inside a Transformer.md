---
title: "I Built a Tiny Computer Inside a Transformer"
source: "https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/"
author:
  - "[[Sean Moran]]"
published: 2026-04-13
created: 2026-04-14
description: "By compiling a simple program directly into transformer weights."
tags:
  - "clippings"
---
transformers and hope useful pattern-recognition circuits emerge inside them. But what if we already knew the circuit? What if, instead of learning weights from data, we built them analytically so the model executed a computation graph directly?

That is the idea behind my Easter weekend project.

Instead of treating a transformer as a system that must discover an algorithm through optimisation, I treat it as a programmable machine. A schedule specifies which intermediate quantities should be computed at each step. Hidden dimensions are assigned to variables like registers in a tiny computer. Attention heads are wired to perform lookups and routing. Feed-forward units are wired to implement local gated computations. Residual updates write the next machine state back into the stream.

The result is a vanilla transformer executing a deterministic program.

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/04/1Mwb3Js9fEqGgyxFTcs-6AA-1-1024x579.webp)

Figure 1: A transformer executing a tiny program. The residual stream stores the current machine state (x,y,z). After embedding, the state contains the input x=B. The attention block performs the lookup step y=lookup\[x\]=5, and residual addition writes that result back into the state. The FFN then performs the local computation z=y+1=6. Finally, the output head reads the updated state and emits the result. Source: image by author.

In this view, the residual stream is working memory and each layer becomes a machine step. Some values are read, some are transformed, some are passed through, and some are overwritten when their slots can be safely reused. The transformer begins to resemble a small compiled computer built out of attention, linear projections, and gating blocks.

None of this requires training. If you already have a computation graph and a schedule for when each intermediate variable should exist, you can directly construct the model weights. As a result the transformer becomes an execution engine whose behaviour is determined by design rather than gradient descent.

> What makes this especially interesting is that it offers an alternative to external tool use. Instead of forcing the model to leave its own execution loop whenever exact computation is needed, we can imagine giving it an internal deterministic mode. In one regime, the model behaves like a flexible language system: generating, abstracting, and reasoning. In another, it behaves more like a compiled machine: updating state, following a fixed computation graph, and executing precise steps reliably. That is a very different picture from the standard “LLM plus tools” stack. It suggests that at least some forms of exact computation could live inside the model itself rather than outside it.

A useful point of contrast is [Percepta’s recent work on executing programs inside transformers](https://www.percepta.ai/blog/constructing-llm-computer). Their construction compiles a general execution mechanism — effectively an interpreter — into the model weights, while supplying the specific program at inference time as part of the prompt. The setup here is narrower and more specialised. Rather than putting an interpreter in the weights, I am compiling the target program itself into the weights. In other words, their model behaves more like a general-purpose executor for supplied programs, whereas this one behaves more like a dedicated compiled machine for a fixed computation graph. That makes it less general, but also simpler and more transparent for understanding how deterministic computation can be embedded directly into standard transformer blocks.

In the rest of this post, I will make that concrete with a tiny example. We will start with a simple program, assign its variables to hidden-state slots, and then walk through how attention, feed-forward layers, and residual updates can be analytically wired so that a standard transformer carries it out step by step.

## A Tiny Program We Can Compile into a Transformer

Rather than stay at the level of metaphor, it helps to watch a very small program run. Here is the toy program I will use throughout the rest of the post:

```python
lookup = {
"A": 2,
"B": 5,
"C": 9,
}

x = input
y = lookup[x]
z = y + 1
output z
```

This program is deliberately tiny, but it contains the three ingredients we need:

1. *a lookup*
2. *a local computation*
3. *an output*

Suppose the input token is B. Then the program should evolve like this:

```python
x = B
y = lookup[B] = 5
z = 5 + 1 = 6
output 6
```

The key idea is that we can represent this evolving program state inside the Transformer’s *residual stream*. Instead of treating the hidden vector as an abstract learned representation, we assign parts of it explicit meaning:

```python
slot 3 = x
slot 4 = y
slot 5 = z
```

So the state evolves as:

```python
[x = B, y = ·, z = ·]
[x = B, y = 5, z = ·]
[x = B, y = 5, z = 6]
```

At that point, the output head reads z and emits 6. This is the central mental model for the rest of the article. The residual stream is the machine state of a tiny running program. Attention, feed-forward computation, and residual addition are the mechanisms by which that state is read, updated, and written back.

## One Machine Step: Attention, FFN, and Write-Back

Once variables have been assigned to slots, the first nontrivial step in the toy program is:

```python
y = lookup[x]
```

In this way, I repurpose the Transformer’s attention mechanism to perform the lookup operation. At a high level, attention already has the right shape for this job. It takes a current state, compares it against a set of stored patterns, selects the relevant one, and returns an associated value. In a language model, that mechanism is usually used for contextual retrieval. Here, I use it in a much more literal way: as a small deterministic lookup operator.

The attention head is wired so that:

- the **query** represents the current lookup request, derived from x
- the **keys** represent the possible cases, such as A, B, and C
- the **values** represent the corresponding outputs, such as 2, 5, and 9

So in this toy example, the head behaves like:

```python
if x == A, return 2
if x == B, return 5
if x == C, return 9
```

Once the correct value has been selected, it still has to become part of the machine state. That is where residual addition comes in. The attention block does not directly replace the whole residual stream. Instead, it produces an update that says, in effect, “write 5 into the slot for y,” and residual addition commits that update to state. After that step, the residual stream becomes:

```python
[x = B, y = 5, z = ·]
```

The next line of the program is different:

```python
z = y + 1
```

At this point, we do not need a lookup. We already have the value we need. What remains is to apply a small local transformation to it. That is exactly the role of the feed-forward block.

In a standard transformer, the FFN is often described as a position-wise nonlinear transformation. Here it is more helpful to think of it as a small local compute unit. It reads the current machine state, applies a fixed transformation, and produces an update that will be written back into the residual stream.

For the toy program, that means reading y = 5, computing z = 6, and emitting an update that targets the slot for z. After residual addition commits that update, the state becomes:

```python
[x = B, y = 5, z = 6]
```

So the division of labour is:

- **Attention** is best thought of as lookup and routing.
- **The FFN** is best thought of as local computation.
- **Residual addition** is the write-back mechanism that commits the update to state.

That gives a simple execution loop:

1. *read the current state*
2. *compute an update*
3. *write the update back*

This is the unit of computation inside the compiled transformer.

## From Program Variables to Compilation

Once the residual stream is interpreted as machine state, the construction starts to look much less like ordinary neural-network design and much more like compilation. The schedule tells us when each variable should exist. In the toy example, x exists first, then y is created from it, and then z is created from y. In a larger computation, different variables appear at different times, remain alive for a while, and then disappear once they are no longer needed.

That brings in the notion of **liveness**. A variable is alive at a given point in the schedule if some later step still needs it. Once no future step depends on it, that variable is dead, and its slot can be reclaimed.

This is very close to **register allocation** in a traditional compiler. A compiler takes program variables and decides where they should live in a limited pool of storage locations. This construction does the same thing, except the storage locations are hidden-state slots in the transformer. If a variable dies, its slot can later be reused for another one. That is how a fixed-width residual stream can support a longer chain of intermediate computations.

A standard transformer layer is then treated as two machine steps:

- an **attention half-layer**
- an **FFN half-layer**

Each one reads the current residual stream, computes an update, and writes that update back through residual addition. So instead of thinking of one layer as one opaque transformation, it is more useful to think of it as two explicit state transitions.

That is why the schedule operates at finer granularity than full layers. It cares which variables are alive after the attention part of a layer and after the FFN part of a layer. Birth, death, reuse, and write-back can all happen at that level.

Once those decisions have been made, the remaining task is to turn that compiled structure into actual transformer parameters. In other words: given a computation graph, a schedule, and a slot assignment, how do we construct the embedding, attention, FFN, and output weights that make the model execute the program?

## From Computation Graph to Weights

At this point, we’ve defined all the key conceptual pieces that allow us to turn a transformer into a general purpose computer:

- *a program defines the desired computation*
- *a schedule decides when each intermediate should be computed*
- *a slot assignment decides where each variable lives in the residual stream*
- *attention and FFN half-layers provide the state-transition machinery*

The remaining step is to turn that structure into transformer weights.

The starting point is the **computation graph**. Each intermediate quantity in the program is represented as a symbolic dimension together with the expression that defines how it should be computed from earlier quantities. The **schedule** then decides which computations happen in which attention half-layer and which happen in which FFN half-layer. It also specifies when each variable becomes live, when it stops being live, and when its slot can be reused. Once that schedule is fixed, each live variable is assigned to a hidden-state slot. Some slots are fixed from the beginning, some are allocated when new variables are born, and some are later reused after earlier variables die.

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/04/1F7y4TyYSJhfy-MovOl7h8Q-1024x550.webp)

Figure 2: Compiling a program into transformer weights. A symbolic computation graph, together with a schedule and slot assignment, is translated directly into embeddings, attention, feed-forward, write-back, and output weights. In this view, the model contains compiled program logic in its parameters. Source: image by author.

There is an important distinction worth calling out here between **global placement** and **local weight construction**. Turning a symbolic expression into a slot-indexed vector is the local step: once I know where x, y, and z live, turning 3·x — 2·y + z into a sparse vector is almost mechanical. The harder problem comes earlier. Before I can write any weights, I first have to decide where each operation runs in the finite transformer, which slot each intermediate occupies, and when a slot can be safely reused.

That is why this starts to look like a compiler backend problem. The system has to satisfy several constraints at once: lookups must happen in attention phases, local nonlinear computations must happen in FFN phases, every consumer must run after its producer, and the total number of layers and residual-stream slots should stay as small as possible. [As outlined by Percepta](https://www.percepta.ai/blog/constructing-llm-computer), in more general constructions, this can be formulated as a scheduling and register-allocation problem and solved with a mixed-integer program. Once that global placement problem is solved, the remaining weight construction becomes much simpler.

Only then do we actually build the weights. The core mechanism is to convert symbolic expressions over program variables into vectors over slots. Suppose a symbolic expression is

```python
3·x - 2·y + z
```

and suppose that x, y, and z have been assigned to slots 3, 4, and 5 respectively. Then the expression becomes a vector that is zero everywhere except at those three positions, where its entries are 3, -2, and 1. In effect, the compiler has replaced variable names with slot addresses. The symbolic expression has become a concrete linear readout over the current machine state.

A simple way to picture it is:

```python
slot 0  slot 1  slot 2  slot 3  slot 4  slot 5  ...
  0       0       0       3      -2       1
```

So the relationship is straightforward: the symbolic expression says what combination of variables is needed, and the slot vector is the transformer-level implementation of that same expression in hidden-state coordinates.

The remaining question is where that vector should go inside the transformer. That depends on the role the expression plays in the computation graph:

- If the expression defines how the state should be initialised from an input token, it goes into an **embedding row**.
- If it is used to decide which case should match during a lookup, it goes into a **query row** or a **key row**.
- If it specifies the result that should be returned once a case is matched, it goes into a **value row**.
- If it defines a local deterministic transformation over the current state, it goes into an **FFN weight row**.
- If it defines what should be emitted from the final machine state, it goes into an **output-head row**.

So the compiler is really doing two things at once. First, it translates symbolic program logic into slot-indexed vectors. Then it places those vectors into the transformer block that implements the required operation.

That is the key bridge from programs to transformers. A symbolic expression over named variables becomes a concrete tensor over hidden-state dimensions, and its role in the computation graph determines whether it is used for state initialisation, matching, retrieval, local computation, or output. Once that translation is in place, we can go block by block and wire the transformer to execute the program.

Seen this way, the construction is doing something quite unusual. By repurposing the transformer’s core blocks in the way that we have, we are turning a probabilistic pattern-recognition system into a deterministic machine. In a trained model, internal circuitry is usually something we infer after the fact: we observe behaviour, inspect activations, and try to guess which circuit emerged. Here, the circuit is known in advance. The weights are built to realise it deliberately. That makes the model much easier to reason about, because the computational role of each block is explicit from the start.

## Scaling Program Execution to Long Deterministic Traces

The remaining question is what happens when this idea is pushed further, in particular, how lookup-heavy execution can be made efficient enough to support much longer deterministic traces.

In the constructions above, attention is often operating in a near-hard lookup regime. Conceptually, a head forms a query q, compares it against candidate keys k₁, k₂, …, kₙ, computes the scores q · kⱼand returns the value attached to the highest-scoring key. In a standard implementation, that means scanning across all candidate keys. As the trace grows, this becomes increasingly expensive.

The useful observation is that this lookup can be reinterpreted geometrically. The query q defines a direction, each key is a point, and the selected key is the one whose dot product with q is largest — in other words, the point furthest in that direction. If the keys live in two dimensions, that is exactly a convex-hull search problem.

This is where the computational advantage appears. A linear attention lookup checks every candidate key. In the convex-hull view, interior points can be discarded because they can never be the maximiser in any query direction. That means we can maintain a convex-hull data structure over the stored 2D keys and answer each lookup by searching that structure, rather than scanning the full set of past keys.

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/04/1W1IEmuoYGVLnOgpzjCKVHA-1024x892.webp)

Figure 3: k -sparse softmax retrieves the top-k candidates from nested convex hulls and applies softmax only over those points, reducing lookup to O(k + log n). The same geometric construction can also be extended to 3D heads via 3D convex hulls. Source: image by author and inspired by a similar diagram in the he Percepta article: Can LLMs Be Computers?

The same geometric reformulation exists in higher dimensions as well. In two dimensions, the set of potentially winning keys lies on a simple polygonal boundary, and supporting-point queries can be answered efficiently on that boundary. In higher dimensions, however, the hull becomes a much more complicated polytope with many faces and many more extreme points. In the worst case, a large fraction of the stored keys can lie on the hull itself, so the “small boundary” advantage disappears. Once that happens, searching the hull is no longer much cheaper than scanning the original key set, and the geometric speedup effectively degrades back toward linear scan. That is why this idea is interesting for very small head dimensions, especially 2D, but not a practical route to sublinear attention for standard transformers with large heads: as the head dimension grows, the hull stops being a compact summary of the candidate set, and the computational advantage largely evaporates.

## Making This All Deterministic in Practice

Of course, there is a gap between a clean toy construction that we have built in this artcile and a practical system. For compiled computation inside transformers to work reliably in the real world, several things have to line up: the intended state transition must be scored above all alternatives at each step, slot reuse has to be carefully managed, and the scheduling problem must fit within a finite width and depth budget. Determinism here is not something transformers provide for free; it has to be engineered into the construction through exact weight design, careful placement of operations, and a fixed decoding rule.

[Percepta’s work](https://www.percepta.ai/blog/constructing-llm-computer) is notable because it addresses these practical constraints end to end. They define transformer-native primitives, compile them into a gate graph, use mixed-integer optimisation to schedule operations and reuse residual-stream slots, and then analytically construct the weights. Crucially, they also introduce a decoding methodology tailored to execution traces, so the model behaves less like an ordinary probabilistic next-token predictor and more like a controlled executor whose intended next step wins reliably under greedy decoding. Combined with exact lookup constructions and an interpreter embedded in the weights, that turns the idea from an interesting theoretical possibility into something much closer to a working execution system.

## A New AI Design Pattern: Integrating Learned Representations with Deterministic Algorithms

Compiling programs into transformer weights points to a compelling future for AI systems: architectures that can combine probabilistic inference with deterministic computation inside the same model, rather than constantly handing exact work off to external tools. Probabilistic components are well suited to abstraction, pattern recognition, and reasoning under uncertainty. Deterministic components are well suited to precise state updates, exact execution, and long reliable chains of computation. Real systems need both.

The deeper promise is that deterministic execution need not remain outside the model. If transformer-native operations such as attention and feed-forward blocks can be organised into a programmable execution substrate, then parts of an interpreter or a specialised program can be compiled directly into the weights. The model is no longer just calling tools more cleverly; it is beginning to internalise some of the computation itself.

That points to a more unified kind of machine: one that can reason flexibly when uncertainty is unavoidable, and switch into exact execution when precision matters. For high-stakes domains where both reliability and performance matter — finance, healthcare, insurance, and supply chains among them — that feels like an important emerging AI design pattern.

And the good news is, you can already try this out in your own AI systems: [Percepta](https://www.percepta.ai/blog/constructing-llm-computer) have developed a system that analytically compiles a WebAssembly virtual machine into transformer weights so that compiled programs can be executed step by step inside the model itself. I’ve tried to convey the main ideas of Percepta’s approach through a tiny compiled example in this article. The key takeaway from Percepta’s work is that deterministic computation does not always have to sit outside the model as a separate tool call. In some cases, it can be compiled into the model’s own circuitry.

*Disclaimer: The views and opinions expressed in this article are my own and do not represent those of my employer or any affiliated organizations. The content is based on personal experience and reflection, and should not be taken as professional or academic advice.*

*Inspired by the Percepta articles:* [Can LLMs Be Computers?](https://www.percepta.ai/blog/can-llms-be-computers) and [Constructing an LLM-Computer](https://www.percepta.ai/blog/constructing-llm-computer)

## Further Reading

- [**transformer-vm**](https://github.com/sjmoran/transformer-vm/tree/main) **—** Containsthe compiler-like machinery described in this article: computation graphs, schedules, slot assignment, and analytical construction of transformer weights.
- **Percepta (2026) blog posts:** [**Percepta (2026) — Can LLMs Be Computers?Percepta (2026) — Constructing an LLM Computer**](https://www.percepta.ai/blog/can-llms-be-computers) explore how transformers can be turned into a kind of internal “LLM computer” that executes long deterministic computations rather than only pattern-matching next tokens. It shows how exact procedural behavior can be embedded inside the model, allowing reliable multi-step execution without constant external tool use. It also examines how 2D attention gives rise to geometric lookup mechanisms, including structures that support operations like convex-hull queries.