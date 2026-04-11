---
title: "Uncovering simultaneous breakthroughs with a robust measure of disruptiveness"
source: "https://www.science.org/doi/epdf/10.1126/sciadv.adx3420"
author:
published:
created: 2026-04-10
description:
tags:
  - "clippings"
---
Kim et al.,Sci. Adv.12, eadx3420 (2026)  
S c i e n c e A d v A n c e S | R e S e A R c h A R t i c l e  
1 of 13  
S C I E N T I F I C C O M M U N I T Y  
Uncovering simultaneous breakthroughs with a robust  
measure of disruptiveness  
Munjung Kim 1  
†, Sadamori Kojaku 2  
, Yong- Yeol Ahn 1  
\*†  
Progress in science and technology is punctuated by disruptive innovation and breakthroughs.To understand disruptive  
innovations and their drivers, the ability to operationalize and estimate “disruptiveness” is critical. Yet, this task remains  
difficult because scientific influence propagates through both direct and indirect citation paths, and discoveries are of-  
ten fragmented across multiple papers. Here, we introduce an embedding- based metric of disruptiveness.When applied  
to large- scale publication data, the measure not only reliably identifies canonical breakthroughs, such as Nobel Prize–  
winning papers, but also finds simultaneous disruptions that eluded standard approaches. By enabling more robust  
identification of disruptive innovations and simultaneous discoveries, our method facilitates more accurate attribution  
of transformative contributions while providing insights into the mechanisms driving scientific breakthroughs.  
INTRODUCTION  
Science is not a static body of knowledge but a dynamic system, con-  
tinuously reshaped as previously unknown discoveries challenge  
established paradigms. The efforts to identify regularities in this dy-  
namic reconfiguration led to theories of scientific progress, such as  
Kuhn’s theory of paradigm shifts (1), Schumpeter’s notion of cre-  
ative destruction (2 – 5), and evolutionary epistemology by Popper  
and Campbell (6,7). Now, the availability of massive bibliometric  
data and powerful computational tools enables scholars to examine  
such theories empirically and quantitatively (8,9). This effort requires  
operationalizing these dynamics along salient dimensions, such as  
novelty, surprise, and downstream impact (9 – 14). These often aim  
to assess the relationship between a focal artifact and its “past” or  
“future.” For instance, while novelty and expectedness (surprise)  
capture the relationship to the past—the extent to which a contribu-  
tion departs from prior patterns, downstream impact is about the  
future—how subsequent research builds on it.  
Integrating these temporal perspectives allows for assessing the  
transformative nature of works—how a contribution transforms in-  
herited knowledge to shape its subsequent utilization. This dynamic  
is often conceptualized as a contrast between consolidating (“develop-  
ing”) contributions that maintain an existing trajectory and destabi-  
lizing (“disruptive”) contributions that redirect it toward unforeseen lines  
of inquiry (15,16). This dichotomy has drawn sustained attention as  
it echoes long- standing accounts of scientific transformation (15 – 23).  
Empirically capturing this transformation is challenging. Citation  
links are sparse and semantically noisy (24 – 26), and influence fre-  
quently propagates through multistep pathways (27 – 31). Sociological  
processes—such as status effects and cumulative advantage—can  
further distort which work gets cited and by whom (32,33). More-  
over, the paper itself is an imperfect unit of analysis: A single publication  
may bundle several distinct ideas, although a single contribution may  
be distributed across multiple publications or found independently.  
Merton’s theory of multiple discoveries suggests that simultaneous,  
independent scientific advances are the norm rather than the ex-  
ception (34,35)—as exemplified by the independent formulations of  
calculus by Newton and Leibniz or the parallel development of the  
theory of evolution by Darwin and Wallace. The Nobel Prize com-  
monly honors several individuals for a single conceptual advance,  
whether collaborative or independent, yet still sparks controversy  
over neglected contributors (36). Given the rich- get- richer dynamics  
that can obscure lesser- known work, some transformative works can be  
overshadowed by better- cited counterparts. Together, these challenges  
raise an important question of how the transformative nature of scien-  
tific work can be reliably assessed despite such limitations.  
Here, we introduce an embedding- based measure that captures  
the extent to which a scientific work redirects the research trajectory.  
Our approach embeds each paper in a high- dimensional space re-  
flecting its direct and indirect connections to prior and subsequent  
work. Just like neural language models that represent tokens and  
sentences as vectors, we imagine each paper as a vector that captures  
its intellectual “position.” We then train two distinct vectors for each  
paper in the same embedding space: one representing its past, or “ante-  
cedents,” context—the configuration of prior work it draws upon—and  
another representing its future, or “descendants,” context—the body of  
work it gives rise to. When a contribution substantially reshapes the  
trajectory connecting past to future, or initiates a new stream of re-  
search, these two contexts diverge; the distance between them there-  
fore captures the extent to which subsequent work departs from the  
prior knowledge.  
To evaluate our measure, we examine several empirical dimen-  
sions. Specifically, we assess its ability to capture multigenerational  
structure, to identify landmark contributions that have exerted sub-  
stantial influence on the trajectories of their fields, and to correctly  
recognize contributions distributed across multiple papers. As a ref-  
erence point, we use the disruption index (“CD index”) (15,16), a  
widely used indicator that uses the topology of local citation network.  
The disruption index captures how subsequent work diverges from  
earlier foundations, focusing on whether later papers cite the prede-  
cessors of a focal contribution through direct citation links. Because  
it formalizes past- future linkage within a clearly defined local neigh-  
borhood of the citation network, it offers a useful comparison for  
approaches that characterize similar relationships at a broader scale.  
Following terminology used in the prior disruption index literature  
(16,17,37), we refer to the two ends of this past- future dimension as  
“disruptive” and “developing.”  
1 c enter for c omplex n etworks and Systems Research,l uddy School of i nformatics,  
c omputing, and e ngineering,i ndiana University, Bloomington,in 47405, USA.2 School  
of Systems Science and i ndustrial e ngineering, Binghamton University, State  
University of n ew York, Binghamton,n Y 13902, USA.  
\* c orresponding author.e mail: yyahn@ virginia.edu  
†Present address: School of d ata Science, University of v irginia,c harlottesville,v A  
22903, USA.  
c opyright © 2026 t he  
Authors, some rights  
reserved; exclusive  
licensee American  
Association for the  
Advancement of  
Science.n o claim to  
original U.S.  
Government Works.  
d istributed under a  
c reative c ommons  
Attribution  
n on c ommercial  
l icense 4.0 (cc BY- nc).

Kim et al.,Sci. Adv.12, eadx3420 (2026)  
S c i e n c e A d v A n c e S | R e S e A R c h A R t i c l e  
2 of 13  
Using a dataset of more than 55 million scientific papers from  
the Web of Science (WoS) and the American Physical Society (APS),  
we show that our measure—“Embedding Disruptiveness Measure”  
(EDM)—provides a continuous, high- resolution view of how scientific  
contributions reconfigure the relationship between inherited knowl-  
edge and emerging directions. By drawing on multigenerational  
citation patterns, EDM yields stable, fine- grained signals that reflect  
shifts in a field’s trajectory—surfacing not only landmark contributions  
with enduring substantial influence but also simultaneous discoveries  
that remain underrecognized.  
RESULTS  
The key idea behind our approach is that we can imagine, for each  
paper, two distinct vectors: past and future. The past vector p i of paper  
i points to the antecedent papers—its references and their close rela-  
tives, whereas the future vector f i points to the future relatives of the  
focal paper. If the embedding model is trained such that the proximity  
between the vectors indicates higher connections between their papers,  
and if disruptive papers tend to eclipse the future knowledge from  
the past, making future knowledge less rely on the past, we expect that  
a paper’s past and future vectors diverge as the paper’s disruptive-  
ness increases. Thus, by quantifying the distance between these two  
vectors—representing the past and future context of each paper—we  
can estimate their disruptiveness. Because they are defined in the  
continuous embedding space from the entire citation network struc-  
ture, rather than the local neighborhood of the focal paper, we can  
also expect that this measure is more robust, incorporating higher- order  
relationships, reducing degeneracy, and remaining stable against indi-  
vidual citation link changes.  
To accomplish this, let us imagine an embedding framework  
where two representation vectors are learned from the past and future  
contexts, respectively, based on the citation relationship. One way to  
achieve this is to use an objective function that aligns the past vector  
of the focal paper with the future vectors of its antecedent papers,  
and the future vector of the focal paper with the past vectors of its  
descendant papers. Then, we can create training examples by generat-  
ing direction- aware random walks from the citation network (Fig. 1A).  
Mathematically, by using a commonly used softmax- based formulation,  
we can first assume that, if we obtain good representations for every  
paper, the conditional probability of seeing paper j after seeing  
paper i (within a short window) on a random walk trajectory that  
follows the citations to the past can be written as  
Pr � j ∣ i � \=  
exp  
�  
f j ⋅ p i  
�  
∑ k exp � f k ⋅ p i  
� (1)  
Fig. 1.Directional graph embedding captures disruptiveness.Our embedding approach leverages the entire network structure to estimate the disruptiveness of each  
paper.t his approach separately represents the citing and cited features of papers (see Materials and Methods for a detailed explanation of the algorithm). (A) First, we  
generate random walks (blue arrow) on the citation network. (B) Our model aims to learn two vectors (“future” and “past”) for each paper that can be used to accurately  
predict “what comes before” (future vector) and “what comes next” (past vector) in the random walk trajectories. (C) As a result, future vector f approaches descendant  
papers vectors whereas past vector p approaches the antecedent papers vectors. (D) For a developing paper, the distance between the vectors representing antecedent  
works and descendant works is close in the embedding space because of the large reliance of descendant works on antecedent works.t his makes the distance between  
future vector f and past vector p becomes closer. (E) For the disruptive paper, on the other hand, the distance between future vector and past vector becomes greater as  
the fewer connections between antecedent papers and descendant papers make their representation vector far away in the latent space.