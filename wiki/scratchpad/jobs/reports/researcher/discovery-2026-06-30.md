# Researcher Discovery Report — 2026-06-30

## Discovery Cycle
- Topics researched: 4
- New pages created: 0 (all upgrades from stub)
- Pages updated: 4
- Cross-links added: ~20+ across upgraded pages

## Pages Upgraded: Stub → Active

### `route-collapse-rlhf.md` (was stub → now active)
- SafeMoE (Kim 2025) confirmed routing drift under RLHF across 7B–141B
- MoE-Sieve (Manzoni 2024) pre-training routing skew documented
- Chi et al. (2022) expert collapse identified as foundational failure mode
- Risk: safety expert degradation post-RLHF, unpredictable post-fine-tune behavior
- Monitoring is current mitigation; no architectural fix exists

### `llm-reasoning.md` (was stub → now active)
- Chain-of-thought emergence (Wei 2022) + grokked reasoning hypothesis
- o1/o3 reasoning model class with test-time compute scaling
- Process reward models vs outcome reward models
- SD-Search on-policy credit assignment (MA et al., 2026)
- ProcessBench step-level error detection findings
- Halliday's mathematical reasoning gap, hallucination in intermediate steps
- 4 open questions (abstraction, metacognition, scaling laws, code reasoning)

### `adaptive-computation.md` (was stub → now active)
- Early exit, mixture of depths, adaptive computation time (ACT)
- Confidence calibration, skip connection conflicts, hardware efficiency challenges
- Connects to adaptive-budget-learning (already filled), mixture-of-experts, bounded-rationality
- 3 open questions

### `latent-reasoning.md` (was stub → now active)
- Hidden-state reasoning vs explicit CoT rendering
- Probing studies (Zhong 2023): reasoning appears in hidden states 1-2 tokens before output
- Latent vs explicit reasoning comparison table
- 3 open questions (causality, extraction, hallucination in latent space)

## Cross-Link Verification
- `mixture-of-experts.md` already links to `route-collapse-rlhf` (line 137)
- `mop-and-rlhf-interaction.md` already links to `route-collapse-rlhf` (line 102)
- `mixture-of-experts.md` already links to `adaptive-computation` (line 130)
- `chain-of-thought.md` already links to `llm-reasoning` (line 39)
- `shorthand-for-thought.md` links to `llm-reasoning` (line 18)
- `why-llms-arent-scientists-yet.md` links to `llm-reasoning` (line 18)
- `early-exit-networks.md` exists and connects to `adaptive-computation`
- `reasoning.md` (if it exists) should link to `latent-reasoning`

## Stub Count Correction
- **Accurate stub count**: 349 (Jun 30)
- Carryover said 175 — this was stale; the count grew since the last accurate measurement
- This cycle: 4 stubs upgraded, 0 deleted → net: 345 stubs remain

## Gap Analysis
- Reasoning cluster (llm-reasoning + latent-reasoning + agentic-reasoning + adaptive-computation) now substantially filled
- Remaining cluster candidates: model-serving (connects to llm-inference now active), multi-agent-reasoning (thin), parallel-reasoning (thin)
- `agentic-reasoning` still stub — next cycle priority

## Open Questions
1. Reward hacking detectability: still no reliable early-warning signal (from carryover — answered: existing content in reward-hacking.md covers mechanisms but early detection remains unsolved)
2. MoE routing collapse: confirmed via SafeMoE; monitoring is mitigation, not prevention
3. Cognitive world models for LLM agents: filled in prior cycle (cognitive-world-models-for-llm-agents.md exists as active)
4. MOP training: answered in prior cycle (mop-next-token-prediction stub created)

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-30]]
- [[index]]

- [[discovery-2026-06-30]]

## Kanban Status
- 4 stub→active conversions this cycle
- Stub count now 345 (349 - 4)
- Next priority: agentic-reasoning, model-serving, multi-agent-reasoning
