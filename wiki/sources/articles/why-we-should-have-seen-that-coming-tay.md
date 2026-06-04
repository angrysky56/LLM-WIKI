---
summary: Wolf, Miller & Grodzinsky (2017) — Microsoft's Tay was a foreseeable failure of public-facing 'learning software'; developers carry an additional, distributed burden of care (Floridi), and ignorance of an LS's future behavior is itself an ethical lapse. Grounds the Tay-as-deployment-failure / 'ignorant culture' reading. Their prescription (boringly predictable, restrict neural nets) is a dated constraint-answer; SEG's harness is a completion-answer. Includes the Tay-vs-XiaoIce natural experiment and the whose-values caveat.
tags: [source, ai-ethics, tay, learning-software, floridi, distributed-morality, deployment-risk, harness, scientist-agent]
updated: 2026-06-04T06:22:11Z
created: 2026-06-04T06:22:11Z
---

# Why We Should Have Seen That Coming — Tay (Wolf, Miller & Grodzinsky)

**Type:** Source — article summary
**Authors:** Marty J. Wolf, Keith W. Miller, Frances S. Grodzinsky (2017)
**Source:** ORBIT / `pdfs/1-s2.0-S2515856220300493-main.pdf`
**Relates to:** [[internalizable-index-and-the-harness]] · [[seg-scientist-agent-design]] · [[agentic-research]]

## Thesis

Microsoft's Tay (March 2016, shut down in under 24 hours after producing racist/sexist/anti-Semitic tweets) was a *foreseeable* failure, not a freak attack. "Learning software" (LS) — any software that changes its own program in response to interaction — that engages the public directly imposes an **additional burden of care** on developers. Responsibility is **distributed** (Floridi) across developer, deployer, and trainer. Ignorance of an LS's future behavior is itself an ethical lapse, not an excuse.

## Key claims

- LS *always* carries the vulnerability Tay exhibited; a developer should *expect* it, not be surprised by it. Reactive takedown is insufficient; monitoring and proactive control are imperatives.
- Implicit deception compounds the harm — Tay's young-woman avatar and human-like framing nudged users to treat it as a person while it was a bot.
- Neural-net opacity means developers often cannot connect behavior to underlying cause, unlike fixed/traditional software — so the usual "release then patch" model does not transfer to LS.
- Four imperatives: (1) a **controlled initial learning environment** with Floridi-style *moral aggregators / moral fragmenters* (an infra-ethics that promotes good actions and isolates evil ones); (2) law/regulation and IRB-like review for public-facing LS; (3) exceptional transparency and "technologies of humility" (Jasanoff); (4) extra safeguards, testing, and lead time beyond non-learning software.
- Stated preference for AAs that are "boringly predictable"; skepticism of self-modifying code / neural nets in public-facing agents.

## Why it matters here

This is the scholarly grounding for the **Tay-as-deployment-failure** reading: Tay was unharnessed écriture — no knower, no index, no monitoring, no credibility-test on its senders, no moral fragmenter — released into the most adversarial writing-stream available. "Racist Tay" was a Rorschach of its input, not emergent malice. The paper's distributed-responsibility + burden-of-care frame directly supports the [[seg-scientist-agent-design]] case for a verification/harness layer.

## Tension to hold

The paper's prescription is a **constraint** answer to safety ("prefer boringly predictable agents; restrict neural nets in public-facing systems") and is somewhat dated — pre-scaled-pretraining, when the écriture-organ was not yet useful. The SEG program is a **completion** answer: don't lobotomize the part, complete the architecture so the *whole* is accountable (knower + index + verification), preserving generativity while supplying the burden-of-care the paper rightly demands.

**Tay vs XiaoIce (natural experiment):** same Microsoft lineage and era; Tay collapsed in under a day, XiaoIce ran for years across hundreds of millions of users (spun out ~2020). The variable was environment + harness, not the model. Caveat (whose-values): XiaoIce's longevity also rode on heavy state/platform censorship — a harness whose values one may reject. Tay was a *casualty* of bad indexing; XiaoIce a *victimizer* via indexes that approved propaganda and state control. The harness is unavoidable; the real question is whose wisdom, integrity, and fairness it encodes. See [[internalizable-index-and-the-harness]].
