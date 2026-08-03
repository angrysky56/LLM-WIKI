---
title: "Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web"
source: "https://www.latent.space/p/ontologies-agentic-systems?fbclid=IwY2xjawTdBgJwZG9mBWV4dG4DYWVtAjEwAGJyaWQRMVZzc3ptN0dhTkVoRzhtRHhzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEe7J-spctsDEBv0egIIU2d44wjgEcoQ-25Z1FWtlFKcsAuSAs4kDdRAPMnHMg_aem_3bYynfSQ463V6zerykCJag"
author:
  - "[[Richard MacManus]]"
published: 2026-07-30
created: 2026-08-02
description: "AI engineers are rediscovering ontologies as a way to keep probabilistic agents inside deterministic boundaries."
tags:
  - "clippings"
---
![](https://substackcdn.com/image/fetch/$s_!180z!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33011df5-c14f-4770-9b91-efa55618b6eb_1672x941.png)

One of the most watched videos from the recent AI Engineer World’s Fair is [a 20-minute talk by](https://youtu.be/Sir59K8ZDPU?si=tKiHra9RZEM2Nwk5) **[Frank Coyle](https://youtu.be/Sir59K8ZDPU?si=tKiHra9RZEM2Nwk5)**, a professor of computer science who currently teaches generative AI and LLMs at UC Berkeley. Drawing on his decades of experience, **Coyle re-introduced the concept and practice of ontologies to today’s AI engineers**.

Coyle argued that while LLMs are very effective at providing probabilistic reasoning, for agentic systems to be truly effective they need “logical guardrails” — by which he means ontologies.

![](https://substackcdn.com/image/fetch/$s_!0pxB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2b52d0c-da81-4ff7-9509-6f9eea43e31f_1280x720.webp)

UC Berkeley professor Frank Coyle speaking at AIEWF 2026.

In computer science, an ontology is “a description of data structure – of classes, properties, and relationships in a domain of knowledge” (as nicely [defined by Oxford Semantic Technologies](https://www.oxfordsemantic.tech/faqs/what-is-an-ontology)). **Coyle himself defined an ontology as simply “data as graphs.”** He added that ontologies as a concept go right back to Aristotle, and have been used throughout the history of Artificial Intelligence.

The company Neo4j, known for its graph database systems, is also using ontologies in its agentic products.

In [a keynote session at AIEWF](https://www.youtube.com/watch?v=VGN22pPpb-8), Neo4j CEO **Emil Eifrem** talked about **three different types of ontologies to enable a “smarter shared substrate” to run agents at scale**. The first is a business-facing ontology, describing the key concepts in an organization; next is a technical ontology, which Eifrem described as “all the metadata of all the data sources and data assets in your enterprise ecosystem”; and finally execution traces, which are “the runtime signals out of your agent.”

![](https://substackcdn.com/image/fetch/$s_!W90X!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66e7b03f-0ca0-4d76-9750-a148d511f069_1200x729.jpeg)

Neo4j’s ontology-based semantic layer

## What’s Old is New Again: the Semantic Web

Frank Coyle thinks **web ontologies** are especially useful in building agentic systems. He mentioned Schema.org, FOAF, Dublin Core and other ontologies familiar to web developers — or at least, those of a certain vintage. He also mentioned “augmenting technologies” like RDFS (Resource Description Framework Schema) and OWL (Web Ontology Language).

One benefit of using these established ontologies is that they’re already in the training data of LLMs, so developers can just prompt for them — much better than reinventing ontologies from first principles.

![](https://substackcdn.com/image/fetch/$s_!0JLS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe90e1f72-5917-41ac-a244-3cc6ab341617_1386x784.png)

“This stuff has been out there underlying a lot of what we already do,” Coyle said. **“So take advantage of these things that already exist.”**

As an example, he showed a Claude agent loop which used an ontology to help validate the LLM’s reasoning after the tool had run.

![](https://substackcdn.com/image/fetch/$s_!uCW8!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf5d5854-297f-4166-829e-39a8f38840d6_1322x798.png)

Coyle calls the convergence of probabilistic agents with ontologies “neurosymbolic AI.”

“Sounds pretty fancy,” he said, “but it’s really **neural networks tied into symbolic AI** — rule-based systems come under that category, as do the knowledge graphs that we’re assembling.”

He reiterated that neurosymbolic AI represents “a way to keep the LLM on its guardrails.”

## The Pros and Cons of Ontologies

Someone who has been steeped in ontologies for many years and is now combining that with AI engineering is **Kingsley Idehen**, who runs a company called [OpenLink Software](https://www.openlinksw.com/). He’s been building an “agent engineering stack” that uses Semantic Web technologies — [including](https://www.linkedin.com/pulse/agent-engineering-stack-nobody-shows-you-kingsley-uyi-idehen-d7vyc/) an “agent with RDF memory.”

![](https://substackcdn.com/image/fetch/$s_!p0DB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b0141ea-b004-47af-bd7f-58a0c6f5aca8_2448x1257.jpeg)

Kingsley Idehen’s agent-rdf-memory system.

I asked Idehen to explain to me the benefits of ontologies.

“The beauty of LLMs is that they are powerful processors of language,” he replied. “ **The beauty of an ontology is that it defines the types of entities and relationships through which language acquires computable context.** Together, they bring the expressive power of language to computing’s UI/UX stack.”

That makes a lot of sense, but if you’ve been a web developer for a while you’ll know the challenges of ontologies: maintenance and keeping them up-to-date. It’s why the 1990s and 2000s vision for a “Semantic Web” — which was based on ontologies — never took off.

[

![X avatar for @lux](https://substackcdn.com/image/fetch/$s_!xBtH!,w_40,h_40,c_fill,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1773545940730974208%2FYUCcCApI.jpg)

lux@lux

you have to be over 40 to even discuss ontologies

6:29 PM · Jul 25, 2026 · 357 Views

---

1 Reply · 9 Likes

](https://x.com/lux/status/2081175084145021293)

Current AI developer Prasenjit Sarkar offered a potential solution for the maintenance problem on X, [arguing that](https://x.com/stretchcloud/status/2081974683038290021) “ **when an agent maintains the ontology as part of its own operation**, updating definitions when it encounters edge cases, the maintenance problem changes character.” It’s still a hard problem though, he added.

Despite these issues, the structured nature of ontologies does appear to be a good match with the occasionally wayward tendencies of probabilistic LLMs. **You get the power of LLMs, but ontologies will keep them in check.**

Plus, as Neo4j’s Eifrem explained, ontologies allow us to move from “a world of thick agents with manually wired data sources” to a new world of “thin agents on a smarter shared ontology-based semantic layer.”

![](https://substackcdn.com/image/fetch/$s_!W6uB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26f28150-6fb0-4022-810e-6c873d6a43b0_1188x698.png)

Neo4j’s “thin agents” concept, which relies on ontologies.

## Loops and Guardrails

Back to Coyle’s presentation. He also had a great point about loop engineering, which he noted “has been around forever” in computer science. The problem, of course, is that **loops can break or otherwise “go off the rails.”**

Again, this is where an ontology system can act as a guardrail to a probabilistic LLM. One of Coyle’s slides referred to it as **“a bounded set of rules around an unbounded loop.”**

Near the end of his presentation, Coyle demonstrated how to use OWL as a check on agents. One slide showed that while language can be slippery, “an OWL axiom is a rule a machine enforces.”

![](https://substackcdn.com/image/fetch/$s_!9NAt!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c238482-5674-429c-92e4-6f183e44fdd8_1336x800.png)

He also showed how “you can have a reasoner built on ontology, to check \[and\] keep the LLM on track — have guardrails to keep it honest.”

![](https://substackcdn.com/image/fetch/$s_!VtYO!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80cabaf6-b95c-45ce-88c9-fbeaa263a65e_1320x764.png)

## Semantic Vibes

Perhaps ontologies are starting to resonate with AI engineers because **a central concern at this time is quality control for loop engineering**. We saw [this debate play out at AIEWF](https://www.latent.space/p/aiewf-daily-dispatch-locomotives), with many conference speakers not willing to go all-in on fully automated “ [software factories](https://www.latent.space/p/software-factories) ” just yet. One of the [key learnings from the event](https://www.latent.space/p/aiewf26trends) was that there need to be guardrails and humans in the loop.

Also it’s fascinating to see traditional web technologies make a resurgence in the field of AI engineering, especially after the 2025 trend of “vibe coding” made it seem like anyone could create software. Of course, since then the penny has dropped: we need to maintain that software and make sure it doesn’t break! **So in 2026, we’re seeing a return to software engineering discipline — including now a revival of web ontologies** as a way to keep probabilistic LLMs honest.

![](https://www.youtube.com/watch?v=Sir59K8ZDPU)