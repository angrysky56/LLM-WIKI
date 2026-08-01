---
title: "Position: LLMs can't jump"
source: "https://openreview.net/forum?id=klU4737opt"
author:
  - "[[Tom Zahavy]]"
published:
created: 2026-07-28
description: "How do we fundamentally discover new things? In a letter to Maurice Solovine, Albert Einstein conceptualized discovery as a cyclical process involving an intuitive 'jump' from sensory experience to axioms, followed by logical deduction. While Generative AI has mastered Induction (statistical pattern matching) and is rapidly conquering Deduction (formal proof), we argue it lacks the mechanism for Abduction—the generation of novel explanatory hypotheses. Using Einstein’s formulation of General Relativity as a computational case study, we demonstrate that the prevailing theory of \"creativity as data compression\" (induction) fails to account for discoveries where observational data is scarce. This position paper argues that while a modern Large Language Model could plausibly execute the deductive phase of proving theorems from established premises, it is structurally incapable of the abductive 'Jump' required to formulate those premises. We identify the translation of simulation into formal axioms as the critical bottleneck in artificial scientific invention, and propose that physically consistent, multimodal world models offer the necessary sensory grounding to bridge this divide."
tags:
  - "clippings"
---
### Tom Zahavy

ICML 2026 Position Paper Track regular Everyone [Revisions](https://openreview.net/revisions?id=klU4737opt) [BibTeX](#) [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**TL;DR:** Scientific invention requires manipulative abduction and physical simulation

**Abstract:**

How do we fundamentally discover new things? In a letter to Maurice Solovine, Albert Einstein conceptualized discovery as a cyclical process involving an intuitive 'jump' from sensory experience to axioms, followed by logical deduction. While Generative AI has mastered Induction (statistical pattern matching) and is rapidly conquering Deduction (formal proof), we argue it lacks the mechanism for Abduction—the generation of novel explanatory hypotheses. Using Einstein’s formulation of General Relativity as a computational case study, we demonstrate that the prevailing theory of "creativity as data compression" (induction) fails to account for discoveries where observational data is scarce. This position paper argues that while a modern Large Language Model could plausibly execute the deductive phase of proving theorems from established premises, it is structurally incapable of the abductive 'Jump' required to formulate those premises. We identify the translation of simulation into formal axioms as the critical bottleneck in artificial scientific invention, and propose that physically consistent, multimodal world models offer the necessary sensory grounding to bridge this divide.

**Lay Summary:**

I explore the fundamental nature of scientific invention, highlighting the critical gap between the ability of humans to create computational systems from physical intuition and current artificial intelligence capabilities. While modern Generative AI excels at pattern recognition (induction) and logical proofs (deduction), we argue it fundamentally lacks the capacity for "abduction"—the intuitive leap required to generate novel explanatory hypotheses. Using Einstein’s formulation of General Relativity as a case study, we demonstrate that LLMs are structurally incapable of creating new foundational axioms, particularly when observational data is scarce. Ultimately, we propose that integrating physically consistent, multimodal world models is the key to bridging this divide and unlocking true artificial scientific invention.

**Primary Area:** Research Priorities, Methodology, and Evaluation

**Keywords:** AI for science, abduction, simulation, physics

**Originally Submitted PDF:** [pdf](https://openreview.net/attachment?id=klU4737opt&name=originally_submitted_PDF "Download Originally Submitted PDF")

**Submission Number:** 235

#### Paper Decision

```
Decision
```

**Decision:** Accept (regular)

**Comment:**

This paper was a fun read given that the authors grounded their argument in a compelling example (the process through which Einstein developed the General Theory of Relativity). All reviewers enjoyed the framing and felt the argument was well thought out and illustrated through the example. Final ratings after rebuttal were uniformly positive: m94K (4: Borderline accept), vzJN (5: Accept, raised), and Ldv4 (5: Accept, raised).

Reviewer m94K wanted discussion of whether prompting or context engineering might unlock abductive capabilities. The authors clarified in rebuttal that while such techniques improve reasoning within existing symbolic space, they cannot provide the sensory grounding required for manipulative abduction—generating axioms without symbolic precedent.

Reviewer vzJN wanted an additional example that could be easier for the reader to digest and link to the authors' argument. In the rebuttal the authors offered to include Archimedes' principle, which satisfied the reviewer due to its simpler construction. This reviewer was also unsure about the claim that world models are sufficient for abductive leaps, but the authors also addressed this concern in their rebuttal satisfactorily—the world model creates a synthetic laboratory to test counterfactuals/reasoning that goes beyond the standard linguistic data. Reviewer Ldv4 was concerned that the conclusion was too strong (that LLMs can't do abductive reasoning because they lack world models). The authors handled this concern in the rebuttal by committing to revise language from "confirms" to "suggests," framing the paper as establishing a theoretical framework for future empirical testing rather than claiming absolute proof.

Reviewers independently converged on similar concerns: strength of claims, need for accessible examples. The authors addressed all substantively in rebuttal. Given the unanimous positive reviews, and my own assessment that the argument is interesting and persuasive, I recommend this paper for acceptance. I think as a position piece it is thought provoking. The authors have committed to adding the Archimedes example and expanding Section 4's discussion of how world models enable hypothesis formation; I expect these revisions to strengthen the final version.

**Reference Correctness Check:**

Automated checker did not flag any references in the submitted paper.

#### Official Review of Submission235 by Reviewer m94K

```
Official Review
```

**Position:** Yes

**Position In Title:** Yes

**Alternative Views Section:** No

**Paper Summary:**

This paper makes a position argument that current frontier LLMs lack a fundamental reasoning mechanism of abduction. It uses the process that Albert Einstein derives General Relativity as a contrasting example to show the gap existed in current LLMs for reasoning.

**Strengths And Weaknesses:**

Strengths:

- This paper gives a very clear and systematic explanation and classification of different reasoning abilities, and reveals abduction as a fundamentally lacking reasoning capability. It is very insightful and certainly benefits researchers in machine learning community to reconsider how to benchmark reasoning capabilities of LLMs in the future.
- Using history that Albert Einstein derives General Relativity is an impressive and persuasive examples supporting the importance of abduction.
- This paper's writing is generally good and well-organized.

Weaknesses:

- Discussions of alternative views or opposite opinions (e.g., frontier LLMs already have abduction capability but need some prompt/context engineering to stimulate it) are needed.
- A minor issue: please follow ICML submission template to have line numbers in the paper.

**Support:** 3: good

**Significance:** 3: good

**Discussion Potential:** 4: excellent

**Argument Clarity:** 4: excellent

**Questions:**

No additional questions.

**Ethics Flag:** No

**Rating:** 4: Borderline accept. Please use sparingly.

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Other details were not carefully checked.

**Compliance With LLM Reviewing Policy A Conservative:** Affirmed.

**Code Of Conduct Acknowledgment:** Affirmed.

**Final Justification:**

Rebuttal has addressed my concern so I will keep my rate.

#### Rebuttal by Authors

**Rebuttal:**

We would like to thank the reviewer for recommending to accept our paper, and for finding it insightful for the ML community.

1. Discussion of alternative views (e.g., prompting/context engineering). Thank you for this excellent suggestion. We agree that the paper would benefit from addressing advanced prompting techniques. In the revised "Alternative Views" section, we will add a paragraph discussing prompting techniques that could improve abductive reasoning. We will clarify that while these techniques drastically improve an LLM's reasoning and search capabilities by breaking down problems, they still operate entirely within the existing symbolic space. Prompt engineering can help an LLM find a clever combination of existing concepts, but it does not provide the sensory grounding required for manipulative abduction—the generation of entirely new axioms without symbolic precedent. Please also see our comment to R Ldv4 regarding existing work on abductive reasoning.
2. Missing line numbers. We apologize for this oversight and will ensure strict adherence to the ICML formatting guidelines, including line numbers, in the camera-ready version.

##### Replying to Rebuttal by Authors

#### Rebuttal Acknowledgement by Reviewer m94K

```
Rebuttal Acknowledgement
```

**Acknowledgement:** (a) Fully resolved - My concerns have been adequately addressed. If you select this option, please consider adjusting your score accordingly.

**Reasons:**

My concerns have been addressed so I will keep my rate.

#### Official Review of Submission235 by Reviewer vzJN

```
Official Review
```

**Position:** Yes

**Position In Title:** Yes

**Alternative Views Section:** Yes

**Paper Summary:**

The paper argues that modern LLMs are structurally incapable of performing an abductive 'jump' from sensory experience to axioms, which they argue is critical for revolutionary physics discovery. Even though LLMs excel in inductive and deductive tasks, this deficiency in performing an abductive jump is a critical limitation. They argue this in detail citing the discovery of General Relativity by Einstein, and the abductive jump process through which Einstein reached at the Equivalence principle, which a modern LLM would not be able to do. Finally, they posit that enabling this jump requires moving beyond better language processing, and suggests alternatives such as world models.

**Strengths And Weaknesses:**

Strengths:

1. The paper keeps the position discussion grounded in a concrete example of the discovery of General Relativity by Einstein. This works well for a clear position formulation and articulation.
2. Taking example from Einstein's insight "acceleration mimics gravity" to argue that this is the kind of jump that LLMs are currently incapable of doing is intuitive and well formulated.
3. The position is balanced in that it both attributes the strengths (induction, deduction) and limitations of LLMs. This puts the position in the right context within the broader discussion framework.

Weaknesses:

1. For the broader community discussion, an example which is, in some ways easier to understand than Einstein's general relativity might be better. Could the authors give an example outside of the complex GR scenario, or in a different domain.. to illustrate a discovery which would not have been possible by LLMs, but was otherwise achieved through a major abductive insight?
2. I understand the intuition that world models may learn richer latent structure about the environment than LLMs. However, it remains unclear why this would be sufficient for the kind of abductive conceptual leap discussed in the paper. Can the authors strengthen the argument by being more concrete as to how learning such latent representations might truly translate into new hypothesis formation, rather than improved prediction or planning alone.

For example, it would help if the authors could give some intuition for why a world model would be better positioned to discover the equivalence principle, whereas an LLM could not, in a deeper sense. Simply learning some latent structure does not necessarily mean the model can use it in a meaningful way like Einstein did.

**Support:** 3: good

**Significance:** 3: good

**Discussion Potential:** 3: good

**Argument Clarity:** 3: good

**Questions:**

See Weaknesses.

**Ethics Flag:** No

**Rating:** 5: Accept

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Other details were not carefully checked.

**Compliance With LLM Reviewing Policy A Conservative:** Affirmed.

**Code Of Conduct Acknowledgment:** Affirmed.

**Final Justification:**

I have changed my score in response to the rebuttal.

#### Rebuttal by Authors

**Rebuttal:**

We thank the reviewer for their constructive feedback and for identifying our position as "intuitive and well-formulated." We address the two primary weaknesses below:

1. Simpler example of abductive insight we agree that a more accessible example would benefit the broader community. In the revised manuscript, we will include Archimedes’ "eureka" moment as a foundational example of manipulative abduction. Archimedes needed to determine if a crown was pure gold without damaging it. The solution—water displacement—was not reached via statistical analysis (induction) or derived from existing physical axioms of the time (deduction). The abductive jump: sensing the buoyancy of his own body in a bath. This sensory "simulation" allowed him to abduct a new rule: that the volume of displaced water equals the volume of the submerged object.

The LLM gap: While an LLM can describe "Archimedes' principle" because it exists in its training corpora, it lacks the sensory grounding to originate such a principle from raw physical experience. It functions as a "Chinese room," manipulating symbols of buoyancy without the "feeling" of displacement that serves as the cognitive bridge to the axiom.

2. Why world models enable hypothesis formation (prediction vs. invention) We appreciate the push for deeper intuition on how latent representations translate into new hypotheses. We will expand section 4 to clarify this using counterfactual intervention.

Beyond passive prediction: current video generation models (e.g., veo) predict the "most likely" next frame based on correlation, which remains a form of induction. In contrast, action-controllable world models (e.g., genie) allow an agent to actively intervene in a simulation.

The "physical prior": a world model grounded in physical consistency provides a "synthetic laboratory." In Einstein’s case, the equivalence principle was linguistically unstated, making its symbolic probability in an LLM near zero. However, in a world model, an agent can "feel" the indistinguishability of acceleration and gravity through internal manipulation.

Invention as verification: We argue that world models increase the generation probability of novel axioms by providing a substrate for verification via simulation. An agent can conjecture a principle in language and immediately test its consistency against its internal physical priors. this bypasses the need for external experimental data—which, as in the case of general relativity, may not be available for years or decades after the theoretical "jump."

##### Replying to Rebuttal by Authors

#### Rebuttal Acknowledgement by Reviewer vzJN

```
Rebuttal Acknowledgement
```

**Acknowledgement:** (a) Fully resolved - My concerns have been adequately addressed. If you select this option, please consider adjusting your score accordingly.

**Reasons:**

Questions are resolved. I like the Archimedes example. I will change my score to reflect this.

#### Official Review of Submission235 by Reviewer Ldv4

```
Official Review
```

**Position:** Yes

**Position In Title:** No

**Alternative Views Section:** Yes

**Paper Summary:**

The authors propose that in the absence of a consistent world model that encodes physics, LLMs are incapable performing abductive reasoning: taking presently known rules, an observed phenomena (but usually not large numbers of observations) that may contradict the known rules, and proposing new rules which explain the observed phenomena in the simplest way possible. To illustrate this they take the example of Einstein's discovery of special and general relativity, where abductive reasoning, especially counterfactual thought experiments, was required to propose new axioms which could explain the advance of the perihelion.

They argue that present AI systems are only capable of deduction: combining axioms to deduce new true statements, and induction: learning from statistical regularity.

**Strengths And Weaknesses:**

**Strengths**

- I enjoyed the framing of this paper, using a known example of abductive reasoning to introduce the concepts required to understand the argument made reading this a pleasure.
- Given recent excitement about Google's Genie model and world models in general I feel that this position paper is timely and will generate interesting discussion.

**Weaknesses**

- I feel that the conclusion is too strong: The authors claim that "Our analysis confirms that the critical bottleneck is this intuitive Jump from sensory experience to formal axioms (E →A)." While they've made a well reasoned argument I don't believe this paper in anyway confirms that LLMs are incapable of abductive reasoning and further testing is required.
- The title, while funny, doesn't clearly state the position: it is unclear without further reading what "jump" refers to in this context.

**Support:** 2: fair

**Significance:** 2: fair

**Discussion Potential:** 3: good

**Argument Clarity:** 3: good

**Questions:**

1. Do you know of any attempts to make LLMs perform abductive reasoning as outlined in this paper?
2. Do you have any ideas on how to confirm or discomfirm the ability of LLMs to perform abductive reasoning experimentally?

**Ethics Flag:** No

**Rating:** 5: Accept

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Other details were not carefully checked.

**Compliance With LLM Reviewing Policy A Conservative:** Affirmed.

**Code Of Conduct Acknowledgment:** Affirmed.

**Final Justification:**

I think this paper, modulo the strong conclusion is likely to stimulate some interesting debate. The rebuttal indicates the authors are willing to moderate the conclusion which addresses my main concern with this paper.

#### Rebuttal by Authors

**Rebuttal:**

We would like to thank the reviewer for recommending to accept our paper. We are also happy to hear they enjoyed reading it.

1. Softening the Conclusion Thank you for this constructive feedback. We completely agree that the phrase "Our analysis confirms" is too strong for a position paper. We will revise the conclusion to state that our analysis "suggests" this bottleneck, explicitly clarifying that the paper establishes a theoretical framework intended to guide future empirical testing rather than claiming absolute proof.
2. Clarifying the Title We are glad you appreciated the humor! The phrase "LLMs Can't Jump" was chosen as a deliberate double entendre: it refers both to the model's inability to make a creative conceptual 'leap', and quite literally to its lack of a physical body (and thus, embodied sensory experience). While we acknowledge that the specific meaning only becomes fully clear upon reading the abstract, we hope the title's playfulness serves as an effective hook to invite the wider community into the discussion. Response to

Q1: Prior attempts at LLM abductive reasoning Standard abductive reasoning—inferring the most likely explanation for an observation—has been thoroughly studied in the context of LLMs, most notably in domains like medical diagnosis. However, as our paper highlights, manipulative abduction is fundamentally different; in Einstein’s case, he reasoned about physical sensations that did not previously exist in the world of language.

Additionally, we recently became aware of a concurrent paper on abductive reasoning ([https://arxiv.org/pdf/2509.23004](https://arxiv.org/pdf/2509.23004)). They develop a neuro-symbolic system (non-LLM) that is presented with empirical facts and must successfully abduce missing axioms to verify them. Because it is not an LLM, it neatly bypasses issues of data contamination, offering an interesting alternative approach to the problem.

Q2: Experimental confirmation While the implicit, 'sensual' knowledge Einstein utilized is inherently difficult to synthesize, one could approximate it experimentally by forcing an LLM to reason about novel, seemingly unrelated facts in an interactive environment.

##### Replying to Rebuttal by Authors

#### Rebuttal Acknowledgement by Reviewer Ldv4

```
Rebuttal Acknowledgement
```

**Acknowledgement:** (a) Fully resolved - My concerns have been adequately addressed. If you select this option, please consider adjusting your score accordingly.

**Reasons:**

Thank you for your thoughtful rebuttal.

My main concern was with the strength of the conclusion and as the revised manuscript addresses this I will raise my score.