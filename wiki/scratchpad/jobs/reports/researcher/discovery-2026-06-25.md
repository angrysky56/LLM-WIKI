# Researcher Discovery Report — 2026-06-25

## Discovery Cycle
- Topics researched: 6
- New pages created: 5 (converted from stubs)
- Pages updated: 1 (grpo → deleted as redundant)
- Cross-links added: ~30+

## New Entries (Stub → Active Conversions)

### Video/Vision Cluster (5 pages) — Complete
- **[[llm-agent-architecture]]**: Runtime architecture patterns for LLM agents — the LLM/software boundary as first-class design concern. Maps production-llm-agent-runtime-architecture-patterns findings: guardrail layers, confirmation gates, state machines, replay buffers. Connects to agent-native-design and production-stage-architecture.
- **[[code-generation]]**: Narrow task of producing code from specifications. HumanEval/SWE-Bench/MBPP benchmarks. Key challenges: context window limits, multi-file coherence, test reliability, long-horizon stability. Connection to MOP and swe-bench as structured search space.
- **[[video-llm]]**: Video-LLM pipeline architecture (vision encoder → projector → LLM). DeltaDirect findings: directional motion blindness, direction binding gap, magnitude deficit, projector-level fix. Zero-shot transfer from synthetic to real.
- **[[vision-language-alignment]]**: Core alignment problem (vision encoder vs LLM trained independently). DeltaDirect as case study: alignment ≠ accessibility. Projector-level intervention sufficient. Magnitude deficit as OOD failure mechanism.
- **[[motion-understanding]]**: Elementary motion primitives; signed motion direction as fundamental case. Direction binding gap (signal present but not bound). Probing evidence table. Magnitude deficit explanation. Projector-level fix (DeltaDirect).

### Redundant Stub Cleanup
- **[[grpo.md]]**: Deleted as duplicate — `group-relative-policy-optimization.md` already has full content. The grpo stub was a redundant alias, not a distinct concept.

## Gap Analysis

**Vision/video cluster is now complete**: video-llm, vision-language-alignment, motion-understanding all have substantive content and form a coherent cluster (video → visual-temporal processing → motion perception → direction binding). The DeltaDirect paper (already in sources) was the primary source material for all three.

**llm-agent-architecture** fills the high-priority gap identified in carryover (very thin, connects to agent-native-design/MOP). The production-llm-agent-runtime-architecture-patterns paper provides the empirical grounding — confirming that boundary failures dominate model failures.

**code-generation** connects the swe-bench/code-agent chain to the MOP search-space framing. The structured program space as low-entropy output domain is the key conceptual link.

**Stub count correction**: 180 concept stubs remain (not ~125). The count in carryover was from an earlier cycle with incomplete enumeration. The carryover heading should be updated to reflect 180.

## Open Questions

- **MoE routing collapse under RLHF**: is it happening in practice? No empirical data. Worth monitoring.
- **Adaptive budget learning**: how to train the gating model. No clear paper yet.
- **Hybrid reward models**: combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction — no full treatment yet.
- **Reward hacking detectability**: Is there a reliable signal that reward hacking is occurring before it becomes severe? Current approaches are post-hoc.
- **Magnitude deficit as general failure mode**: Does this pattern (geometry preserved but magnitude collapses OOD) apply to other capabilities beyond motion direction?
- **Cognitive world models for LLM agents**: How do you represent "what the world looks like" for a text-based agent? Conversation state? Tool return history?