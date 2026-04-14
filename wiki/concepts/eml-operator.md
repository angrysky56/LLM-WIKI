---
summary: Single binary operator eml(x,y)=exp(x)−ln(y) that generates all elementary functions from constant 1 — the continuous NAND gate, with applications to symbolic regression, neuro-symbolic AI, automated reasoning, and single-instruction hardware
tags: [mathematics, operator-theory, sheffer-stroke, neuro-symbolic, symbolic-regression, analog-computing, computational-minimalism]
updated: 2026-04-14T08:15:44Z
created: 2026-04-14T08:15:44Z
---

# EML Operator

The EML (Exp-Minus-Log) operator is a binary function:

$$\operatorname{eml}(x,y) = \exp(x) - \ln(y)$$

that, together with the constant $1$, generates all standard elementary functions — the continuous-domain analogue of the [[sheffer-stroke]] (NAND gate) for Boolean logic. Discovered by Andrzej Odrzywołek via systematic exhaustive search and reported in [[odrzywolek-eml-2026]].

## Formal Properties

**Grammar:** $S \to 1 \mid \operatorname{eml}(S,S)$ — every elementary expression is a binary tree of identical nodes.

**Non-commutativity** is essential — the first argument feeds $\exp$, the second feeds $\ln$, and the subtraction is asymmetric. This provides both expression-tree growth and inversion capabilities.

**Completeness** over the 36-primitive scientific calculator basis (constants, unary functions, binary operations) is constructively verified.

**Complex internals:** Real-valued results require complex intermediate computations — $\pi$ and trigonometric functions emerge via Euler's formula through $\ln(-1)$.

## Structural Significance

EML reveals that elementary functions belong to a simpler structural class than previously recognized. The entire zoo of school-taught operations ($\sin, \cos, \sqrt{}, \ln, +, \times, \ldots$) collapses into a single recursive primitive. This is not merely a theoretical curiosity — it has direct architectural consequences.

The uniform binary tree structure means:
- Every formula is a circuit of identical gates (like NAND in digital logic)
- The search space for [[symbolic-regression]] becomes complete and regular
- Expression complexity is measured by a single metric: tree depth

## Use Cases

### 1. Exact Symbolic Regression for Time-Series

Traditional time-series models produce black-box predictions. EML turns formula discovery into a trainable circuit: standard gradient descent (Adam) optimizes tree weights, which then "snap" to exact closed-form equations. This yields transparent, computationally cheap algebraic models instead of opaque neural approximations. Applicable to financial indicators, physics discovery, and any domain where the underlying law is elementary.

### 2. Neuro-Symbolic Bridge

Continuous math and symbolic logic have required different computational paradigms. EML reduces continuous functions to a purely symbolic tree of identical nodes — the grammar $S \to 1 \mid \operatorname{eml}(S,S)$ is a context-free language isomorphic to Catalan structures and full binary trees. This makes EML an ideal primitive for systems that need to manipulate, generate, or verify mathematical formulas using discrete logic structures.

### 3. Native Continuous Math in Automated Reasoning

For reasoning servers like [[mcp-logic]], handling continuous math typically requires offloading to external interpreters. An EML compiler within a logic server would let it natively parse, reduce, and verify mathematical identities using a single set of rules — trigonometric functions and logarithms become the exact same class of object. This vastly reduces symbolic solver complexity without requiring monolithic orchestration.

### 4. Rulial Space Exploration

The existence of EML parallels Rule 110 and NAND for continuous domains. If all standard mathematics emerges from repeated $\exp(x) - \ln(y)$, researchers can map how complex mathematical behaviors generate from minimal starting conditions. The open question of whether an even simpler operator exists (ternary variant without distinguished constant, or a constant-free binary Sheffer) connects to foundational questions about computational irreducibility.

### 5. Single-Instruction Hardware (OISC for Continuous Math)

EML suggests FPGA or silicon designs using only one gate type (an EML evaluator). A compiler would break any physics engine, differential equation solver, or generative algorithm into pure EML machine code. The uniform binary tree topology maps naturally to massively parallel hardware — every node is identical, enabling extreme regularity in chip layout and routing.

## Connections

- [[odrzywolek-eml-2026]] — source paper
- [[symbolic-regression]] — gradient-based formula discovery
- [[sheffer-stroke]] — Boolean logic analogue
- [[mcp-logic]] — automated reasoning integration point
- [[alphaevolve]] — evolutionary code discovery (related paradigm: searching for optimal mathematical representations)
- [[efhf]] — neuro-symbolic architecture that could use EML as its continuous math primitive
