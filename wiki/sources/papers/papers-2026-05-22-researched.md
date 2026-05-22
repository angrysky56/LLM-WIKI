# Papers Researched: 2026-05-22

## MOSS: Self-Evolution through Source-Level Rewriting

**Paper:** [arXiv:2605.22794v1](https://arxiv.org/abs/2605.22794)  
**Wiki:** [[moss-self-evolution-source-rewriting-2026]]

- **Topic:** Self-evolving autonomous agents that modify their own source code (harness-level), not just text-mutable artifacts (prompts, skills, memory)
- **Key result:** Single evolution cycle lifts four-task mean grader score from 0.25 → 0.61 on OpenClaw
- **Novelty:** Only system reaching the agent harness layer; all prior application-level self-evolving agents confined to text-mutable scope
- **Components:** Substrate (OpenClaw), moss evo CLI, external coding-agent CLI, host-daemon, ephemeral trial workers
- **Pipeline:** Directed evolution anchored to production-failure evidence; 7-stage pipeline (Locate → Plan → Plan-Review → Implement → Code-Review → Task-Evaluate → Verdict); user-consent-gated in-place container swap with health-probe rollback


## LCGuard: Latent Communication Guard for Safe KV Sharing

**Paper:** [arXiv:2605.22786v1](https://arxiv.org/abs/2605.22786)  
**Wiki:** [[lcguard-kv-communication-guard-2026]]

- **Topic:** Framework for safe KV-based latent communication in multi-agent LLM systems via adversarial-learned transformations
- **Key result:** 65-75% ASR reduction while maintaining competitive task performance (helpfulness 0.71 vs 0.78 baseline)
- **Novelty:** First framework to formalize reconstruction-based leakage from shared KV caches; treats KV as latent working memory, not inference artifact
- **Method:** Residual bottleneck transformation g_ij(K,V) trained adversarially; Full-System variant optimizes across all communication paths (vs Per-Agent local)
- **Models evaluated:** Qwen3-4B/8B/14B, Gemma-2-9B, LLaMA-3B/8B
- **Benchmarks:** PrivacyLens, AgentLeak, MAGPIE
