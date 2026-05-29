---
created: 2026-06-17
updated: 2026-07-15
type: concept
summary: CoLLM-NAS — dual-LLM Navigator/Generator architecture for neural architecture search; separates strategic exploration from tactical generation
tags: [neural-architecture-search, dual-llm, ml-evolution, architecture-discovery, guided-evolution]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.75
---

# CoLLM-NAS (Collaborative LLM NAS)

**Also known as:** CoLLM-NAS, Collaborative LLM Neural Architecture Search

## What It Is

CoLLM-NAS is a Neural Architecture Search method that uses a dual-LLM architecture to separate strategic exploration from tactical generation. Unlike conventional NAS methods that sample random mutations or use gradient-based architecture optimization, CoLLM-NAS leverages the semantic understanding of a Navigator LLM to guide architecture search toward promising regions of the design space, with a Generator LLM then translating those strategic intentions into concrete, valid architecture configurations.

## The Dual-LLM Mechanism

### Navigator LLM
The Navigator LLM receives:
- The target task description
- The current architecture state (layer configurations, connectivity, parameter counts)
- Historical search experience (fitness trajectories of prior candidates)

It outputs strategic suggestions: "increase MoE expert count in layers 4-6 to improve specialization" or "replace LayerNorm with RMSNorm to reduce compute."

The Navigator operates in **design space language** — it thinks about architectures in terms of component roles, not raw parameter values.

### Generator LLM
The Generator LLM takes the Navigator's strategic proposals and translates them into:
- Specific architectural configurations (layer connections, dimension choices)
- Constraint-satisfying specifications (valid ranges for each hyperparameter)
- Parsable architecture representations (for evaluation)

The Generator ensures that all proposed architectures are grammatically valid and can be instantiated in the search framework. This prevents the semantic bloat problem in pure random search, where architecture mutations frequently produce syntactically invalid or incompatible layer combinations.

## How It Works

1. **Initialize**: Setup architecture search space and seed candidates
2. **Strategic Proposal**: Navigator LLM proposes architecture modifications based on fitness history
3. **Tactical Generation**: Generator LLM translates proposals into valid architecture configurations
4. **Evaluation**: Candidate architecture is trained/evaluated (or scored via proxy)
5. **Feedback**: Fitness feedback updates Navigator's understanding of good design regions
6. **Iterate**: Continue until convergence or compute budget exhausted

## Why Dual Over Single-LLM?

Single-LLM NAS approaches have two failure modes:
1. **Strategic confusion**: The LLM is asked to produce final architecture specs directly, but can't balance global design goals with local constraints
2. **Generative hallucination**: The LLM proposes architectures that are syntactically valid but architecturally invalid (e.g., connecting layers that produce incompatible tensor shapes)

CoLLM-NAS isolates these concerns:
- Navigator handles **what to change** (strategic, goal-directed)
- Generator handles **how to express it** (tactical, constraint-satisfying)

This mirrors the principle behind [[MCTS]] where separate selection and simulation phases prevent single-phase confusion.

## Connection to Guided ML Evolution

CoLLM-NAS is a core instance of the Guided ML Evolution paradigm from the [[ml-evolution-benchmarking-protocol]]. The Navigator LLM acts as the "semantic compass" — constraining the architecture search space to regions that are:
- Syntactically valid (Generator ensures this)
- Architecturally meaningful (Navigator ensures this)
- High-potential (fitness feedback ensures this)

The dual-LLM design also parallels [[agent-architectures]] where deliberative and reactive layers are separated.

## Connections
- [[wiki/index]]
- [[concepts/llama-nas]]
- [[concepts/rz-nas]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-03]]
- [[concepts/neural-architecture-search]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[concepts/collm-nas]]
- [[log]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[collm-nas]]

- [[neural-architecture-search]] — CoLLM-NAS is a specific NAS method within the broader architecture search field
- [[ml-evolution-benchmarking-protocol]] — source reference for CoLLM-NAS
- [[ml-evolution]] — CoLLM-NAS exemplifies LLM-guided evolution (Navigator as mutator, Generator as evaluator interface)
- [[rz-nas]] — complementary NAS method; RZ-NAS uses zero-cost proxies, CoLLM-NAS uses LLM guidance
- [[llama-nas]] — another architecture search method (one-shot sub-network search)
- [[evolutionary-strategies]] — CoLLM-NAS replaces standard ES mutation with LLM-driven strategic mutations
- [[essa]] — both CoLLM-NAS and ESSA use LLMs as intelligent search operators in evolutionary frameworks
- [[agent-architectures]] — dual-LLM separation mirrors deliberative/reactive layer split

## Open Questions

1. Does separating Navigator and Generator roles require specialized fine-tuning, or can any capable LLM fulfill either role with prompting?
2. CoLLM-NAS's effectiveness scales with Navigator LLM capability — does it beat random search on frontier models but not on smaller models?
3. Can the Navigator's strategic proposals be distilled into a small model for faster iteration?
4. Does the dual-LLM overhead in evaluation time negate the efficiency gains from smarter search?
