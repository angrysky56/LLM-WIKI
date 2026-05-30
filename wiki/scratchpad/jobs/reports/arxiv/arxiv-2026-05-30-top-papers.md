# arxiv Report — 2026-05-30

## Papers Processed

### 1. LLMSurgeon: Diagnosing Data Mixture of Large Language Models (arxiv:2605.30348)
- **Why selected**: First formalization of data mixture auditing from model outputs alone. Novel contribution (inverse problem under label-shift). Directly addresses the transparency gap — knowing what LLMs were trained on is foundational for safety, accountability, and governance.
- **Status**: ingested → wiki/sources/papers/llmsurgeon-diagnosing-data-mixture-2026.md
- **Wiki connections**: llm-transparency, interpretability, ai-safety-auditing, model-evaluation, data-mixture

### 2. Locally Coherent, Globally Incoherent (arxiv:2605.30335)
- **Why selected**: Shows that multi-component LLM agents can produce globally incoherent probability distributions despite every component being locally calibrated — a fundamental architectural limitation. Connects to CCO, BES, and the broader agentic AI evaluation infrastructure theme.
- **Status**: ingested → wiki/sources/papers/locally-coherent-globally-incoherent-2026.md
- **Wiki connections**: multi-agent-systems, calibration, constraint-satisfaction, agentic-ai, belief-updates

### 3. Reasoning in Memory (RiM) (arxiv:2605.30343)
- **Why selected**: Decouples internal reasoning computation from external autoregressive generation — enabling single-forward-pass latent reasoning. Alternative to test-time scaling via token generation. Connects to Entropy-Cut MH (reasoning scaffolding) and test-time compute efficiency for agentic systems.
- **Status**: ingested → wiki/sources/papers/rim-reasoning-in-memory-2026.md
- **Wiki connections**: test-time-scaling, reasoning-scaffolding, llm-architecture, parallel-reasoning

## Wiki Updates
- New pages: 3 (llmsurgeon-diagnosing-data-mixture-2026.md, locally-coherent-globally-incoherent-2026.md, rim-reasoning-in-memory-2026.md)
- Tags added: paper, arxiv, data-mixture, multi-agent, probabilistic, coherence, test-time-compute, working-memory, latent-reasoning
- PDFs stored: /home/ty/Documents/paper-research/2605.30348v1.pdf, 2605.30335v1.pdf, 2605.30343v1.pdf

## Cross-Paper Theme: Transparency as Infrastructure for Agentic AI

All three papers address dimensions of transparency that become critical as AI systems become more capable and consequential:

| Paper | Transparency Dimension | Core Problem |
|-------|----------------------|--------------|
| LLMSurgeon | Data transparency | What did we train this model on? |
| Locally Coherent | Compositional transparency | How do components fail when composed? |
| RiM | Architectural transparency | How does the model actually compute? |

**Design principle**: As agentic AI systems become more capable, the bottleneck shifts from capability to trust — and trust requires transparency across multiple dimensions: data, composition, and computation.

## Notes
- arXiv API hit aggressive rate limiting — worked around via targeted ID queries
- All 3 PDFs downloaded via curl (200 status each)
- Text extracted via pdftotext (poppler-utils)
- arXiv rate limit events: 4 (handled via backoff and targeted queries)

## Related
- [[scratchpad/agent-sheets/arxiv/templates/report]]
- [[wiki/index]]
- [[scratchpad/jobs/index]]