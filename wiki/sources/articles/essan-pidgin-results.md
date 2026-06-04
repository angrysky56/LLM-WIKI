---
created: 2026-05-22
updated: 2026-05-30
type: source
summary: "Blind Essan pidgin communication: 0% decode accuracy across 20 trials; symbols encode structural roles but lack semantic bindings"
tags: [essan, pidgin, communication, blind-decoding, hallucination, vector-symbolic]
sources: []
status: active
confidence: 0.85
---

# Blind Pidgin Essan Communication Experiment

## Protocol
- **Agent A (Sender):** Encodes reasoning traces as Essan symbol sequences
- **Agent B (Receiver):** Decodes symbols → natural language (BLIND — no access to original)
- **Evaluator:** Compares decoded content against original reasoning

## Symbol Vocabulary

| Symbol | Meaning |
|--------|---------|
| ⦿ | claim (something being asserted) |
| ⧈ | inference link (x supports y) |
| ⫰ | transition (moving from x to y) |
| ⩘ | commit (final conclusion) |
| ⧉ | strengthen (reinforce with evidence) |
| ⧿ | cycle (feedback loop) |
| ⧬ | initiate |

## Results

**Total Trials:** 20 | **Hallucinated:** 20/20 (100%) | **Decode Accuracy:** 0.0%

| Score | Count | Percentage |
|-------|-------|------------|
| Hallucinated | 20 | 100.0% |
| Partial | 0 | 0.0% |
| Too Vague | 0 | 0.0% |

## Key Findings

1. **Information Loss is Fundamental**: Without semantic content bindings, Agent B can only infer structural roles, not specific propositional content
2. **Hallucination Patterns**: Blind decoders must generate content to fill structural slots when no semantic bindings exist
3. **Structural Accuracy**: Symbol sequences reliably encode reasoning structure (⧬=start, ⦿=claim, ⩘=conclusion, etc.)
4. **The "Too Vague" Problem**: In pure blind decoding, specific semantic content cannot be recovered from structural symbols alone

## Conclusion

Pure symbol-based pidgin Essan achieves 0% decode accuracy in blind conditions. The vocabulary encodes structural reasoning roles but **lacks semantic bindings**. To improve decode accuracy: bind specific concept labels to symbols rather than using bare symbols.

## Connections

- [[essan-mcp-logic-results]] — FOL formalization confirms symbols are structurally consistent but semantically ungrounded
- [[essan-vector-results]] — Vector encoding confirms symbol-only spaces have no semantic signal (mean sim ≈0 vs natural language)
- [[essan-vgcp-comparative-analysis]] — Essan's symbolic notation lacks VGCP's tool-causality enforcement; hallucinated tool results possible
