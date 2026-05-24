---
summary: Research summaries for 2026-05-24 batch: ConvexTok (optimal tokenization), AwareVLN (sparse self-aware VLN), AlphaProof Nexus (formal proof with basic agent matching full RL agent)
tags: [arxiv, daily-report]
updated: 2026-05-24T08:30:00Z
created: 2026-05-24T08:30:00Z
---

# Papers Researched — 2026-05-24

### 2605.22821 — tokenisation-convex-relaxations
Tokenisation via Convex Relaxations (ConvexTok) replaces greedy BPE with an LP-based global optimizer. Formulates tokeniser construction as an integer program then relaxes to LP — surprisingly near-integral at practical vocabulary sizes. Key finding: all existing tokenisers are within 1% of optimal compression per the LP lower bound; Bias rounding scheme consistently outperforms BPE on intrinsic metrics.

### 2605.22816 — awarevln-self-aware-vision-language-navigation
AwareVLN adds sparse self-aware reasoning to VLM-based vision-language navigation. Triggers structured analysis only at key navigation decision nodes, giving the agent explicit state understanding without 3D sensors or SLAM. The model autonomously decides when to reason — only when strategically beneficial. Significantly outperforms prior VLN state-of-the-art in Habitat simulator.

### 2605.22763 — alphaproof-nexus-formal-proof-search
AlphaProof Nexus uses LLM + Lean compiler for formal proof search on open research problems. The full agent solved 9 open Erdős problems (two open 56 years), 44 OEIS conjectures, and is actively aiding research in multiple math domains. Striking finding: a basic LLM+Ralph loop agent solved all 9 same Erdős problems as the RL-equipped full agent — shift toward simple agentic loops as LLMs improve. $100-500/problem cost. Lean compiler acts as a hard verifier node preventing logical hallucination.

---