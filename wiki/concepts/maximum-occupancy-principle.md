---
summary: Maximum Occupancy Principle — path-entropy-maximizing behavior theory; Layer 0 of EFHF (Prover9-verified)
tags: [mop, entropy, intrinsic-motivation, behavioral-variability, reward-free, reinforcement-learning, absorbing-states, stochastic-policy, efhf, kernel-2, lumpability]
updated: 2026-06-02T14:46:16Z
---

---
created: 2026-04-14 04:12:42+00:00
updated: 2026-05-23 08:55:00+00:00
type: concept
summary: Theory of behavior replacing reward maximization with action-state path entropy maximization — Layer 0 of EFHF architecture; absorbing states → Kernel 2 (Prover9-verified)
tags: ['mop', 'entropy', 'intrinsic-motivation', 'behavioral-variability', 'reward-free', 'reinforcement-learning', 'absorbing-states', 'stochastic-policy', 'efhf', 'kernel-2', 'lumpability']
sources: []
status: active
confidence: 1.0
---

# Maximum Occupancy Principle

**Source:** [[ramirez-ruiz-mop-2024]] — Ramírez-Ruiz et al., *Nature Communications* (2024)
**Status:** Active research area with follow-up work (NeuroMOP, PIMBAA workshop 2025)

## What It Is

A theory of behavior that replaces reward maximization with action-state path entropy maximization. The agent's goal is to visit as many different action-state paths as possible over the long term. Extrinsic rewards (food, energy) are treated as means to sustain continued exploration — not as objectives.

The principle is formalized as maximizing:

$$V^\pi(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t \left(\alpha \mathcal{H}(A|s_t) + \beta \mathcal{H}(S'|s_t, a_t)\right)\right]$$

## Why It Matters

MOP resolves several persistent problems in theories of behavior:

**The reward definition problem.** Reward-maximizing agents need a reward function specified by design. MOP sidesteps this — define only what kills the agent (absorbing states), and complex behavior emerges.

**The exploration-exploitation tradeoff.** Under MOP this tradeoff disappears. Agents explore intrinsically and exploit only when survival requires it.

**Behavioral variability after learning.** All reward-maximizing frameworks predict behavior should collapse to a deterministic optimal policy once learning is complete. MOP predicts — and biological evidence supports — that behavioral stochasticity persists indefinitely. Optimal MOP policies are always stochastic.

## The Three Parameters

Only the ratio β/α and γ matter:

| Parameter | Controls | Effect |
|---|---|---|
| α | Action entropy weight | Higher → more diverse action strategies |
| β | State-transition entropy weight | Higher → preference for surprising/novel outcomes; also controls risk sensitivity |
| γ | Discount factor | Higher → longer planning horizon; avoids myopic traps (noisy TV problem) |

## Absorbing States Are the Only Design Choice

Instead of designing rewards, a MOP system designer only needs to define absorbing states — states from which no further action-state paths are possible. These have zero value by construction. The agent's entire behavioral repertoire emerges from avoiding absorbing states while maximizing path entropy.

This has a deep connection to ethical frameworks where harm is defined deontologically (certain states are unconditionally to be avoided) while behavior within the non-absorbing space is guided by entropy maximization (freedom, diversity, possibility).

## Key Mathematical Properties

1. **Uniqueness (Theorem 1):** Path entropy is the *only* occupancy measure satisfying additivity, monotonicity, and smoothness
2. **Bellman equation exists:** The value function can be computed recursively
3. **Convergent value iteration:** The iterative map (Eq. 7) converges from any positive initial condition
4. **Optimal policy is always stochastic:** No deterministic optimal policy under MOP
5. **Absolute vs. relative entropy matters:** KL-regularization cancels the preference for states with many actions — self-defeating for occupancy maximization. This directly challenges RLHF's standard structure.

## EFHF Integration: Layer 0

MOP serves as Layer 0 (Intrinsic Motivation) of the [[efhf]] architecture. The existing EFHF pipeline (L1-L5+) is reactive — it waits for user prompts. MOP makes it proactive by generating exploration targets autonomously.

**Formally verified (Prover9):** MOP absorbing states → EFHF Kernel 2 transitions. Zero future entropy ↔ zero future computation ↔ Kernel 2. The structural equivalence is a logical theorem, not an analogy.

| MOP Concept | EFHF Concept | Relationship |
|---|---|---|
| Absorbing state | Kernel 2 transition | Proved equivalent |
| Energy reservoir | Buffering capacity T | Operational mapping |
| Discount factor γ | Coherence window τ | Both control planning horizon |
| Controlled high-Δ | Strong lumpability | Coherent exploration |
| Uncontrolled high-Δ | Weak lumpability failure | Hallucination |

## Connections

- [[concepts/reinforcement-learning-from-human-feedback]]
- [[concepts/privacy-mas]]
- [[concepts/agent-skills-spec]]
- [[concepts/synthetic-data]]
- [[agents/skills/researcher-agent/skill]]
- [[concepts/trump-administration-national-security]]
- [[concepts/public-health-governance]]
- [[concepts/nasa-artemis]]
- [[concepts/epistemic-energy]]
- [[sources/papers/utimula-openpraparat-2025]]
- [[concepts/spacex-starship-development]]
- [[concepts/spec-driven-development]]
- [[concepts/peter-steinberger]]
- [[sources/news/2026/wolchover-life-force-2026]]
- [[entities/projects/efhf]]
- [[concepts/uv]]
- [[concepts/probing-analysis]]
- [[concepts/programmatic-seo]]
- [[concepts/google-research]]
- [[concepts/hybrid-agents]]
- [[sources/papers/shannon-scaling-law-2026]]
- [[concepts/3dgs]]
- [[concepts/code-generation]]
- [[concepts/content-addressed-storage]]
- [[concepts/episodic-memory]]
- [[concepts/mop-and-rlhf-interaction]]
- [[concepts/russia-belarus-nuclear]]
- [[concepts/firecracker]]
- [[concepts/llm-agents]]
- [[concepts/latent-communication]]
- [[concepts/spike-campaign-001-004-summary]]
- [[sources/papers/betteti-baggio-bullo-zampieri-hopfield-2025]]
- [[concepts/cri]]
- [[concepts/public-health]]
- [[concepts/waldis-instructions-shape-language-2026]]
- [[concepts/nato-expansion]]
- [[wiki/index]]
- [[concepts/spike-001-spacy-owlready2]]
- [[synthesis/causal-state-edm-ood-isomorphism]]
- [[concepts/india-us-relations]]
- [[concepts/who-emergency-declarations]]
- [[concepts/north-american-energy-politics]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/china-industrial-policy]]
- [[concepts/world-model]]
- [[concepts/mojo-language]]
- [[concepts/tabular-data]]
- [[concepts/namm]]
- [[sources/articles/prd-ralph-loop-mop-gemini]]
- [[concepts/who-emergency-declaration]]
- [[concepts/us-intelligence-community]]
- [[sources/articles/llm-kernel-optimization]]
- [[sources/papers/proxy-based-shapley-banzhaf-2026]]
- [[concepts/open-ended-evolution]]
- [[concepts/directed-preferential-placement]]
- [[concepts/business-model]]
- [[synthesis/self-prompting-via-production-stage-architecture]]
- [[concepts/compound-commands]]
- [[concepts/global-health-infrastructure]]
- [[concepts/bounded-rationality]]
- [[concepts/sovereign-ai]]
- [[synthesis/bounded-structured-memory]]
- [[synthesis/mop-edm-cognitive-architecture]]
- [[log]]
- [[concepts/2026-05-news]]
- [[entities/tools/mcp-logic]]
- [[concepts/tabpfn-extensions]]
- [[concepts/github-actions]]
- [[concepts/java]]
- [[concepts/major-transitions]]
- [[concepts/rz-nas]]
- [[sources/papers/vector-policy-optimization-vpo-2026]]
- [[concepts/autopoiesis]]
- [[concepts/geometric-hashing]]
- [[concepts/trunk]]
- [[concepts/agent-group-evolving-molecular-system-agem]]
- [[concepts/codebase-inspection]]
- [[concepts/production-stage-architecture]]
- [[concepts/taplo]]
- [[concepts/wikilinks]]
- [[concepts/habitat]]
- [[concepts/machine-psychology]]
- [[concepts/russia-ukraine-war]]
- [[concepts/blackmail]]
- [[concepts/mop-next-token-prediction]]
- [[concepts/social-media-regulation]]
- [[concepts/mobile-automata]]
- [[concepts/seg-molecular-self]]
- [[entities/projects/alphaevolve]]
- [[concepts/product-strategy]]
- [[synthesis/cross-layer-drift-falsification]]
- [[concepts/fts5]]
- [[entities/projects/mop-explorer]]
- [[concepts/overlayfs]]
- [[concepts/functional-emotions]]
- [[sources/papers/ramirez-ruiz-mop-2024]]
- [[concepts/novelty-search]]
- [[concepts/ai-for-science]]
- [[concepts/india-energy-strategy]]
- [[concepts/vlm]]
- [[concepts/group-relative-policy-optimization]]
- [[sources/papers/orthogonal-bottlenecks-rl]]
- [[concepts/truth-seeking]]
- [[concepts/ollama]]
- [[concepts/musk-velocity]]
- [[concepts/tiktok-youtube-ofcom-report]]
- [[concepts/llm-agent-architecture]]
- [[concepts/hormuz-strait-security]]
- [[concepts/latex]]
- [[concepts/autonomous-research]]
- [[concepts/printing-press]]
- [[synthesis/minimal-generative-architectures]]
- [[concepts/news]]
- [[concepts/micro-saas]]
- [[concepts/agent-native-design]]
- [[concepts/video-llm]]
- [[concepts/sledgehammer]]
- [[concepts/information-retrieval]]
- [[concepts/evolutionary-strategies]]
- [[concepts/china-energy-security]]
- [[concepts/curiosity-driven-exploration]]
- [[sources/papers/bae-lmac-2026]]
- [[concepts/shap]]
- [[concepts/causal-reasoning]]
- [[concepts/solo-development]]
- [[concepts/agentic-reasoning]]
- [[concepts/iran-ceasefire]]
- [[wiki/sources/papers/on-the-representation-collapse-of-sparse-mixture-of-experts]]
- [[concepts/ai-safety]]
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]]
- [[sources/papers/awarevln-self-aware-vision-language-navigation-2026]]
- [[concepts/global-health-security]]
- [[concepts/random-forest]]
- [[concepts/tabpfn-client]]
- [[concepts/edm-framework]]
- [[concepts/webhook-subscriptions]]
- [[concepts/reconstruction-attack]]
- [[concepts/revenue-model]]
- [[concepts/llm-evaluation]]
- [[concepts/activation-engineering]]
- [[concepts/mcp-model-context-protocol]]
- [[concepts/indie-hacking]]
- [[concepts/concept-index]]
- [[synthesis/intelligence-as-entropic-sculpting]]

## See Also

- [[ramirez-ruiz-mop-2024]] — source paper with full mathematical detail
- [[efhf]] — the five-layer architecture MOP integrates with as Layer 0
- [[edm-framework]] — disruption as measurement analog: high Δ = high state entropy = novel conceptual territory
- [[causal-state-edm-ood-isomorphism]] — epsilon machines provide the theoretical bridge; MOP agents seek to *create* new causal states
- [[zettelkasten-engine]] — MOP-guided exploration prioritizes high-disruption insight regions
- [[mop-edm-cognitive-architecture]] — full synthesis: MOP + EDM + EFHF cognitive architecture

## Related Concepts

- [[2026-05-news]]
- [[3dgs]]
- [[CRI]]
- [[Firecracker]]
- [[agent-group-evolving-molecular-system-agem]]
- [[agent-native-design]]
- [[agent-skills-spec]]
- [[agentic-reasoning]]
- [[ai-for-science]]
- [[ai-safety]]
- [[alphaevolve]]
- [[autonomous-research]]
- [[autopoiesis]]
- [[blackmail]]
- [[bounded-structured-memory]]
- [[business-model]]
- [[causal-reasoning]]
- [[china-energy-security]]
- [[china-industrial-policy]]
- [[code-generation]]
- [[codebase-inspection]]
- [[compound-commands]]
- [[concept-index]]
- [[content-addressed-storage]]
- [[continual-learning]]
- [[curiosity-driven-exploration]]
- [[directed-preferential-placement]]
- [[ebola-outbreak-drc-2026]]
- [[episodic-memory]]
- [[epistemic-energy]]
- [[essa]]
- [[evolutionary-strategies]]
- [[fts5]]
- [[functional-emotions]]
- [[geometric-hashing]]
- [[github-actions]]
- [[global-health-infrastructure]]
- [[global-health-security]]
- [[google-research]]
- [[group-relative-policy-optimization]]
- [[habitat]]
- [[hormuz-strait-security]]
- [[india-energy-strategy]]
- [[india-us-relations]]
- [[indie-hacking]]
- [[information-retrieval]]
- [[iran-ceasefire]]
- [[java]]
- [[latent-communication]]
- [[latex]]
- [[llm-agent-architecture]]
- [[llm-agents]]
- [[llm-evaluation]]
- [[llm-kernel-optimization]]
- [[machine-psychology]]
- [[major-transitions]]
- [[mcp-model-context-protocol]]
- [[micro-saas]]
- [[mobile-automata]]
- [[mojo-language]]
- [[mop-and-rlhf-interaction]]
- [[mop-explorer]]
- [[mop-next-token-prediction]]
- [[nasa-artemis]]
- [[nato-expansion]]
- [[neural-architecture-search]]
- [[north-american-energy-politics]]
- [[novelty-search]]
- [[ollama]]
- [[open-ended-evolution]]
- [[overlayfs]]
- [[peter-steinberger]]
- [[prd-ralph-loop-mop-gemini]]
- [[printing-press]]
- [[privacy-mas]]
- [[probing-analysis]]
- [[product-strategy]]
- [[production-stage-architecture]]
- [[programmatic-seo]]
- [[public-health]]
- [[public-health-governance]]
- [[qes]]
- [[random-forest]]
- [[reconstruction-attack]]
- [[reinforcement-learning-from-human-feedback]]
- [[retrieval-augmented-generation]]
- [[russia-belarus-nuclear]]
- [[russia-ukraine-war]]
- [[seg-molecular-self]]
- [[shap]]
- [[sledgehammer]]
- [[social-media-regulation]]
- [[solo-development]]
- [[sovereign-ai]]
- [[spacex-starship-development]]
- [[spec-driven-development]]
- [[synthetic-data]]
- [[tabpfn-client]]
- [[tabpfn-extensions]]
- [[tabular-data]]
- [[taplo]]
- [[tiktok-youtube-ofcom-report]]
- [[trump-administration-national-security]]
- [[trunk]]
- [[truth-seeking]]
- [[us-intelligence-community]]
- [[utimula-openpraparat-2025]]
- [[uv]]
- [[video-llm]]
- [[vlm]]
- [[waldis-instructions-shape-language-2026]]
- [[webhook-subscriptions]]
- [[who-emergency-declaration]]
- [[who-emergency-declarations]]
- [[wikilinks]]
- [[world-model]]
