---
created: 2026-06-14
updated: 2026-06-25
type: concept
summary: "Cognitive system for temporary information storage and active manipulation during reasoning — in LLMs, manifests as attention-based context maintenance and activation patterns"
tags: [cognition, memory, working-memory, reasoning, attention, bounded-rationality]
sources: https://en.wikipedia.org/wiki/Working_memory (Baddeley's model)
status: active
confidence: 0.7
---

# Working Memory

## Definition

Working memory is the cognitive system responsible for temporarily storing and actively manipulating information during reasoning, problem-solving, and decision-making. It maintains information in an accessible but fragile state — available for immediate use, rapidly overwritten by new information, and limited in capacity.

The canonical model (Baddeley's multi-component working memory) includes:
- **Phonological loop**: stores and rehearses verbal information
- **Visuospatial sketchpad**: maintains visual and spatial information
- **Central executive**: attention control and coordination
- **Episodic buffer**: integrates information across domains into coherent episodes

## Why It Matters

Working memory is the bottleneck for reasoning. You cannot reason about information you cannot hold in mind simultaneously. This applies equally to humans and to language models — the fundamental constraint is combinatorial.

For humans: working memory limits how many variables you can track in a multi-step problem, how deep you can reason about abstract relationships, and how many alternatives you can consider in parallel.

For LLMs: the context window plays the role of working memory, but with different properties. Attention is not fixed-capacity like human attention — it's diffusely distributed across all context tokens. But degradation occurs: distant tokens receive less attention weight, and activating information at arbitrary positions requires explicit retrieval mechanisms (attention-based or otherwise).

## The Amnesiac Agent Problem

LLMs exhibit a distinctive working memory pathology: the amnesiac agent problem. Given a long conversation, the model progressively loses access to earlier context not because of a hard architectural limit, but because:

1. **Attention weight decay**: attention scores to early context diminish as more tokens are added (distant tokens receive diluted attention)
2. **Activation interference**: new information overwrites relevant activation patterns for old information
3. **Retrieval failure**: the model doesn't have an explicit "short-term memory buffer" — everything must be represented in the same activation space

This is why long conversation histories often require explicit summarization or retrieval mechanisms — the model cannot naturally consolidate early context the way humans do through sleep and memory consolidation.

## Working Memory and the MOP-EDM Framework

In the [[mop-edm-cognitive-architecture]], working memory is the **active maintenance substrate** for epistemic energy:

- **MOP's path entropy** is maintained by tracking which action-state paths are currently active in working memory — the agent samples different paths to maximize coverage
- **EDM's disruption signal** detects when working memory representations become inconsistent across time steps — the divergence between predicted and actual activation patterns signals a need to re-evaluate
- The **sheaf-consistency-enforcer** monitors working memory coherence across layers — if adjacent layers have inconsistent representations of the same information, the closure status degrades

Working memory in this framing is not just storage — it's the space where epistemic energy is actively consumed and monitored.

## Key Research Connections

- [[bounded-rationality]] — working memory capacity is the primary structural limit on bounded rationality; you cannot consider all alternatives if you cannot hold them all in mind
- [[agent-native-design]] — intrinsic motivation (MOP) must operate within working memory constraints; bounded rational agents cannot explore unboundedly
- [[world-model]] — working memory holds the current state of the world model during planning and simulation
- [[recursive-transformers]] — per-token recursion depth may be thought of as iterative refinement of working memory representation within a single forward pass; each recursion step is like a " rehearsal" of the token's representation
- [[critical-initialization-biological-neural-networks]] — biological working memory has initialization dynamics (prefrontal cortex maintenance) that relate to the edge-of-chaos initialization findings
- [[efhf]] — in the EFHF architecture, the episodic buffer corresponds to working memory; EFHF's "observation" step populates working memory, MOP's "update" step manages it

## Limitations

- **Human working memory is truly limited**: ~7±2 items (Miller's law). LLM "working memory" (context window) is architecturally unbounded but functionally degraded at distance.
- **No automatic consolidation**: humans consolidate working memory to long-term memory during sleep. LLMs have no equivalent automatic process — explicit retrieval or fine-tuning is required.
- **Attention is not the same as memory**: a token being in context doesn't mean it's "in working memory" in the cognitive sense. Attention can be diffusely distributed, meaning no single token receives focused processing.

## Open Questions

1. Can LLMs be trained to have a more human-like working memory with explicit consolidation mechanisms?
2. Is there a principled way to measure "effective working memory capacity" for a given LLM at a given context position?
3. How does working memory interact with in-context learning — does ICL essentially "upload" a task representation into working memory?


## Connections
- [[log]]
- [[sources/papers/critical-initialization-biological-neural-networks]]
- [[concepts/memory-mechanisms]]
- [[concepts/world-model]]
- [[concepts/agent-native-design]]
- [[concepts/bounded-rationality]]
- [[concepts/epistemic-energy]]
- [[concepts/working-memory]]
- [[index]]
- [[working-memory]]
- Concept: [[epistemic-energy]]
- Concept: [[memory-mechanisms]]
