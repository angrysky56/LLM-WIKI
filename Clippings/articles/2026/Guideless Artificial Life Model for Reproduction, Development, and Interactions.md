---
title: "Guideless Artificial Life Model for Reproduction, Development, and Interactions"
source: "https://direct.mit.edu/artl/article/31/1/31/127798/Guideless-Artificial-Life-Model-for-Reproduction"
author:
  - "[[Keishu Utimula]]"
published: 2025-02-25
created: 2026-04-14
description: "Abstract. Reproduction, development, and individual interactions are vital yet complex natural processes. Tierra (an ALife model proposed by Thomas Ray)"
tags:
  - "clippings"
---
[Skip Nav Destination](#)

Reproduction, development, and individual interactions are vital yet complex natural processes. Tierra (an ALife model proposed by Thomas Ray) and cellular automata, which can manage these aspects in a complex manner, are significantly limited in their ability to express morphology and behavior. In contrast, the virtual creatures proposed by Karl Sims have a considerably higher degree of freedom in terms of morphology and behavior. However, they also exhibit a limited capacity for processes like reproduction, development, and individual interactions. In addition, they employ genetic algorithms, which can result in a loss of biological diversity, as their implementation necessitates predefining a fitness function. Contrarily, the evolution of natural life is determined by mutation and natural selection, rather than by a human-defined fitness function. This study carefully extracts the characteristics of these models to propose a new Artificial Life model that can simulate reproduction, development, and individual interactions while exhibiting a high expressive power for morphology and behavior. The model is based on the concept of incorporating Tierra and cellular automata mechanisms into a cell that moves freely in 3-D space. In this model, no predefined fitness function or form that qualifies as a living creature exists. In other words, this approach can be rephrased as searching for persistent patterns, which is similar to the approach of Conway’s Game of Life. The primary objective of this study was to conduct a proof-of-concept demonstration to showcase the capabilities of this model. Guideless simulation by the proposed model using mutation and natural selection resulted in the formation of two types of creatures—dumbbell shaped and reticulated. These creatures exhibit intriguing features, exploiting the degrees of freedom inherent to the proposed model. Particularly noteworthy is their unique method of reproduction, which bears a striking resemblance to that of real organisms. These results reinforce the potential of this approach in modeling intricate processes observed in actual organisms and its ability to generate virtual creatures with intriguing ecologies.

Sims (1994b) introduced virtual creatures composed of multiple rigid bodies, controlled by their neurons. This was one of the first Artificial Life models that could be simulated on a computer. Through environmental interactions, this innovative model could acquire morphology and its control mechanism without the need for human design.

However, this model has two limitations in expressing biological diversity. The first is its limited expression of essential life processes like reproduction, development, and individual interactions. Consequently, these elements are frequently examined, but only individually (Godin-Dubois et al., 2019; Ito et al., 2013; Joachimczak et al., 2014, 2015; Joachimczak & Wróbel, 2012; Lehman & Stanley, 2011; Schramm et al., 2011; Sims, 1994a; Stanley, 2007). To the best of the author’s knowledge, no study on Sims’s model considers these elements in an integrated manner. Real-world organisms exhibit remarkable diversity in terms of reproduction, development, and individual interactions. Therefore studying these elements in virtual creatures, inspired by the work of Sims, will significantly expand the diversity in Artificial Life models. The second limitation is that this model uses genetic algorithms (GAs) for reproduction, which requires a predefined fitness function. This could result in a loss of biological diversity (Miconi, 2008; Ray, 2001). Furthermore, in the context of open-ended evolution (OEE), which investigates the endless creative productivity of evolution (Packard et al., 2019), the limitations of fitness functions become evident. For example, predefining fitness functions risks closing off potentially promising paths within the search space (Soros & Stanley, 2014). Moreover, there is an argument that artificial selection through fitness functions can only select based on predefined criteria and that anything emerging during the evolutionary process must arise from natural selection (Channon & Damper, 1998).

Frameworks that can simulate these elements—reproduction, development, and individual interactions—include Tierra (Ray, 1992); self-replicating patterns with cellular automata (von Neumann & Burks, 1966); and Avida, which was inspired by the former two models (Ofria & Wilke, 2004). In these models, the fitness of an organism is defined not by humans but by its interactions with other organisms. This enables the emergence of diverse survival strategies among organisms, thereby enhancing biodiversity.

However, the morphological and behavioral characteristics exhibited by these models were subject to significant limitations compared to Sims’s virtual creatures. Therefore enhancing the degree of freedom related to morphology and behavior within the Tierra and cellular automaton models would be a logical research direction. Several studies have attempted to achieve this, and all of them yielded extremely compelling results (e.g., Chan, 2019; Miconi, 2008). However, these attempts still have limitations, as discussed in the next section.

In this study, a new Artificial Life model that can simulate biological reproduction, development, and individual interactions while exhibiting a high expressive power for morphology and behavior is proposed. The proposed model is based on the concept of incorporating Tierra and cellular automata mechanisms into a cell that moves freely in 3-D space. Similar to Conway’s Game of Life (Gardner, 1970), the persistent patterns exhibited by these cells can be interpreted as virtual creatures. In other words, the proposed model does not employ any human-designed fitness functions, and the forms that qualify as creatures are not predefined. This framework allows for a variety of emergent structures that observers may consider as creatures. The primary objective of this study was to explain the details of this new model and to conduct a proof-of-concept demonstration showcasing its capabilities through several experimental results.

The mutation and natural selection processes of the simulations conducted using the proposed model led to the emergence of two distinct virtual creatures. These virtual creatures exhibited an intriguing ecology that utilized the degrees of freedom of the model. In particular, they independently acquired reproductive methods that resembled those of actual organisms, exhibiting not only simple binary fission but also phenomena that can be regarded as budding or spore formation. These results reinforce the potential of this approach in modeling intricate biological processes observed in actual organisms and its ability to generate virtual creatures with intriguing ecologies.

This section first describes the Artificial Life model proposed by Karl Sims, known as *virtual creatures*. Next, studies that have explored elements like reproduction, development, and individual interactions, which are challenging to represent comprehensively in Sims’s virtual creatures are examined. Following this, several models capable of handling these elements in a composite manner are introduced, noting their limited expressive power in terms of morphology and behavior compared to Sims’s virtual creatures and discussing a few approaches that were used to overcome these limitations. Finally, the concept of OEE, which is another important element of the proposed model, is discussed.

### 2.1 Sims’s Virtual Creatures

Karl Sims (1994b) proposed a system of virtual creatures that could be simulated on a computer. These creatures had bodies and neurons defined by directed graphs, and, through GAs, they evolved into creatures with various functions. Many studies have been derived from Sims’s virtual creatures. Sims demonstrated that it is possible to acquire lifelike forms and their control mechanisms through evolution. Many studies have been inspired by this concept, exploring various aspects and applications, for example, research exploring the relationship between evolutionary direction and morphological diversity (Lehman & Stanley, 2011), studies on the interaction between environment and evolution (e.g., Auerbach & Bongard, 2012), research proposing the fabrication of virtual creatures’ bodies from soft materials (Cheney et al., 2014), and applications to real-world robot design (Hornby et al., 2003; Lipson & Pollack, 2000). Sims’s ideas have been continuously expanded on and applied to various challenges.

However, these virtual creatures have limited expressive capacity regarding reproduction, development, and individual interactions. Therefore several studies have examined these elements, albeit as independent parameters.

### 2.2 Reproduction, Development, and Individual Interactions

#### 2.2.1 Focused Studies

The reproductive process is frequently simulated through GAs. In these algorithms, variations in the selection of parents and the mixing of their genes are manually set hyperparameters and not adjusted automatically by the model (Godin-Dubois et al., 2019; Lehman & Stanley, 2011; Sims, 1994a).

The mechanism of biological development was applied to a network structure for development by Stanley (2007). In several studies, the bodies of virtual creatures were constructed using particles and springs, connecting the particles to simulate the process of development (Joachimczak et al., 2014, 2015; Joachimczak & Wróbel, 2012; Schramm et al., 2011).

Individual interactions have occasionally been modeled as parameters for GAs (Sims, 1994a). Sims created interesting and diverse virtual creatures using the results of competition between individuals as criteria for the selection of the parents. Additionally, a study by Ito et al. (2013) examined changes in morphology and behavior in environments where predators and prey coevolve.

#### 2.2.2 Integrated Approaches

These earlier studies independently studied reproduction, development, and individual interactions. Contrarily, models such as Tierra (proposed by Ray, 1992) and self-replicating patterns of cellular automata (proposed by von Neumann & Burks, 1966), can address these aspects compositely.

Tierra simulates virtual creatures with genes expressed in byte code. This is executed by a virtual machine and evolves via mutation as it competes for CPU time and memory space (Ray, 1992). In this model, the reproductive process does not use a GA; therefore it does not require a predefined fitness function. Thus this model exhibits diverse reproductive methods. For example, a parasitic creature emerged in Tierra that was unable to reproduce on its own but could leverage the code of other creatures to reproduce. In response, other creatures emerged with acquired immunity to parasitic creatures, with some even using parasites to enhance their own propagation as a survival strategy.

A cellular automaton is a discrete computational model consisting of a regular grid of cells (von Neumann & Burks, 1966). Each cell changes its internal state according to a set of rules. In a series of studies on cellular automata beginning in the late 1940s, von Neumann demonstrated the existence of a self-reproduction pattern in a cellular automaton with 29 internal states (von Neumann & Burks, 1966). Several other researchers pursued this line of study, including Codd and Ashenhurst (1968), Banks (1971), and Devore and Hightower (1992). This self-reproduction was not instantaneous; rather, it involved a developmental process. The self-reproduction pattern loop proposed by Langton was robust and could achieve self-reproduction even when mutations were triggered by collisions with other loops (Langton, 1984; Sayama, 1999). Therefore this is an excellent method of expressing reproduction that incorporates interactions between individuals.

Although Tierra and cellular automata have a high expressive power for reproduction, development, and individual interactions, they are significantly restricted in their ability to simulate morphology and behavior. Therefore several attempts to increase the degrees of freedom of morphology and behavior for these models have been reported. For example, Lenia is a model that extends cellular automata to continuous space (Chan, 2019). Chan enumerated nine evolutionary abilities possessed by life and stated that Lenia can represent eight of these, excluding reproduction. The other abilities are quoted from the study as follows:

> Life can be defined as the capabilities of self-organizing (morphogenesis), self-regulating (homeostasis), self-directing (motility), self-replicating (reproduction), entropy reduction (metabolism), growth (development), response to stimuli (sensitivity), response to environment (adaptability) and evolving through mutation and selection (evolvability). Systems of artificial life are able to reproduce some of these capabilities with various levels of fidelity. Lenia, the subject of this paper, is able to achieve many of them, except self-replication that is yet to be discovered. (p. 252)

Reproduction within this model is challenging; nevertheless, recent studies on extended Lenia have reported that it is relatively easy to find self-reproduction patterns (Chan, 2020).

Evosphere is a model that connects the concept of damage to Sims’s virtual creatures (Miconi, 2008). This enables simulation through free natural selection without defining a fitness function. Although this model includes Tierra’s element of not defining fitness for Sims’s virtual creatures, it does not permit the emergence of parasitic organisms as seen in Tierra. Moreover, it omits certain developmental processes, such as body formation through repeated cell division starting from a single cell or growth from a young to an adult form. Therefore offspring in this model appear completely developed without undergoing these stages.

In addition, the division blocks model, an extension of Sims’s virtual creatures, offers a framework for simulating reproduction without the use of predefined fitness functions and the developmental processes of organisms (Spector et al., 2007). Although it does not provide for the emergence of parasitic entities, as Tierra does, this model aims to simulate various elements that support biological evolution. Investigating the conditions necessary for the emergence of different types of morphological or developmental complexities remains a key area for future research.

### 2.3 Open-Ended Evolution

Furthermore, I will discuss the concept of OEE, which is one of the central research areas in Artificial Life. In OEE, the focus is on investigating the endless creative productivity of nature (Packard et al., 2019). This creative productivity has been producing a staggering variety of organisms and is thought to be still at work today. Given these characteristics, it can be said that many studies in Artificial Life are related to OEE in some form. In the studies mentioned previously, for example, Tierra was designed with the realization of OEE as one of its goals (Ray, 1992), and the research on extended Lenia also aims to explore its connection with OEE (Chan, 2020). Additionally, the research on Evosphere, which derives from Sims’s virtual creatures, defines OEE as a state in which new fitness functions are continuously generated through coevolution, preventing the system from reaching an equilibrium, and focuses on investigating coevolution within Evosphere (Miconi, 2008). Similarly, the division blocks model extends Sims’s virtual creatures into a broader context of OEE and ecological dynamics by adopting natural selection without explicit fitness functions (Spector et al., 2007).

Bedau and Packard (1996) conducted a pioneering study to quantitatively evaluate evolutionary activity. Their proposed evolutionary activity statistics classified evolutionary dynamics into three classes. The Artificial Life model Geb, proposed by Channon (2001), was the first model to be classified in this evaluation as being capable of unbounded evolution (Bedau et al., 1998). It is important to note that Geb enabled continuous emergence by eliminating evolution through human-prepared fitness functions commonly used in GAs (Channon, 2001; Channon & Damper, 1998). In fact, predefining fitness functions runs the risk of closing off potentially promising paths within the search space (Soros & Stanley, 2014).

However, it remains unclear whether being unbounded in this assessment of evolutionary activity is equivalent to achieving an explosion of complexity, and the extent to which activity statistics capture the essence of open-ended phenomena is an unresolved issue (Soros & Stanley, 2014). An alternative approach to assessing the degree of OEE is the concept of a *complexity barrier* proposed by Dolson et al. (2023). Instead of asking what OEE is, they consider what the “barriers” are if a system is not open-ended and attempt to quantitatively evaluate them. The authors classify these barriers into five categories: change (population stops changing), novelty (novel organisms stop appearing), complexity (complexity stops increasing), ecology (ecosystem diversity stagnates), and individuality (shifts in individuality are impossible). Moreover, as a quantitative evaluation method for these barriers, they propose measuring the potential to overcome the first barrier, change, by examining “the number of genotypes in the population that appeared after being absent for at least 10 generations and then survived one round of selection. (p. 3)”

In recent years, the scope of research into OEE has significantly expanded, impacting various fields. For instance, Furlan et al. (2022) studied OEE in Artificial Life models that interact with humans, whereas Claire et al. (2023) investigated its implications for program generation. Furthermore, Balaz et al. (2021) examined the effects of OEE on the development of drug delivery systems. These studies highlight the versatility and potential of open-ended approaches across different technological and scientific domains. The evolution approach without predefined fitness functions, as employed in my model, aligns closely with the principles of OEE and serves as a promising framework for exploring continuous emergence.

Models like Tierra and cellular automata have mechanisms that read the genes with encoded information about the organism. The results depend on the surrounding environment, leading to reproduction and development. This system simulates the expressions of various reproductive and developmental processes, as well as those of individual interactions caused by interference from other creatures. The model proposed in this study is an attempt to incorporate this mechanism into a cell that moves freely in 3-D space. This design decision is aimed at equipping the cells with a level of morphological and behavioral freedom akin to that observed in Sims’s virtual creatures.

### 3.1 Overview

The proposed form of virtual creatures consists of spheres, which are called cells, and springs that connect them. These virtual creatures acquire their morphologies via repeated cell division, binding with the surrounding cells using springs, or unbinding. The procedure is encoded in the genes possessed by each cell and is read sequentially to represent the developmental process (see for more details). The cell can copy a portion, or all, of its own genes during division and pass them on to a new cell. These genes are constructed from 64 types of characters. During a mutation, these characters are replaced by other characters with a certain probability at regular intervals of time. This represents mutation within the proposed model. Thus, coupled with the selection that arises from survival competition, virtual creatures should undergo various forms of evolution.

In addition, each cell has a feedforward neural network (the parameters of which are determined by the genes) with only one hidden layer, enabling a response and action from an external input. This action is different from the gene-derived behavior described earlier.

Virtual creatures in this model are simulated on a 3-D field with elevations and depressions. A sun is located above the field and sways in one direction, serving as the only source of energy in the environment of the model. It emits a constant number of light particles per unit time in random directions. Consequently, the amount of sunlight received by each cell is inversely proportional to the square of the distance *h* from the sun. An example of this field is shown in Figure 1. Further details are given in.

Figure 1. 

Example of (left) field, (top right) top view, and (right bottom) side view. The sun is placed on top of the field and is swaying in one direction.

### 3.2 Gene

The genes of this virtual creature operate through a mechanism similar to the template-matching addressing used in Tierra, albeit simpler (Ray, 1992).

They are represented as strings. In this case, any two or more types of characters that describe the gene can be used, and this choice does not significantly influence the performance of the model. For example, the simplest form would be a binary sequence using only 0 and 1, which is frequently used in computer simulations; this represents an example of two different characters. In comparison, sequences observed in real organisms typically consist of four distinct types representing the four nucleotides: adenine (A), thymine (T), cytosine (C), and guanine (G); these represent examples of four different characters. In this work, 64 different characters are used to describe this gene for human readability. Fifty-two upper- and lowercase letters of the English alphabet, 10 Arabic numerals (0–9), and the symbols + and −are selected as the 64 different characters. Each cell has a string as a gene and another string that determines its readout position. Considering the difference in their roles, the gene and readout position strings are referred to as the *book* and the *bookmarker*, respectively. These correspond to DNA and promoters in real organisms, respectively. Examples of the book and the bookmarker are presented in Figure 2. In this example, book is “ABCDEFGHIJKLMN…” and bookmarker is “EF.” The text that is read from the book appears immediately after the bookmarker, which in this case is “G.” It should be noted that, in this simulation, the search for strings matching the bookmarker always starts from the beginning of the book. This rule is universally applicable and not restricted to this example alone.

Figure 2. 

Example for book and bookmarker.

The cell can perform four different actions depending on the character that is read out first, which are as follows:

1. EXPANSION (⁠ $\mathcal{E}$ ⁠): The generation of new cells around a source cell, corresponding to cell division. Here the generated cell is connected to the source cell by a spring.
2. CONNECTION (⁠ $\mathcal{C}$ ⁠): The action of connecting with the surrounding unconnected cells.
3. DISCONNECTION (⁠ $\mathcal{D}$ ⁠): An operation to disconnect a cell that has already been connected.
4. TRANSITION (⁠ $\mathcal{T}$ ⁠): The action of changing the bookmarker string.

In this simulation, 64 different characters were evenly assigned to these four actions, as listed in Figure 3.

Figure 3. 

Characters assigned to the four actions.

Thus EXPANSION is the action that would have been performed in the previous example, as indicated in Figure 4.

Figure 4. 

Examples for EXPANSION.

In terms of interpretation of actions, no difference exists between characters classified as the same action. Thus, in the example here, the behavior would be the same even if G were A or P. The action determines the interpretation of the string that follows.

#### 3.2.1 EXPANSION

If the action is EXPANSION, the 538 characters following bookmarker are interpreted as the information for the new cell.

Specifically, the information is as follows: (a) light absorption rate (color), (b) luminous intensity, (c) mass, (d) radius, (e) neural network weight, (f) start and end positions of the section to be copied and passed from the book, (g) bookmarker, and (h) amount of bookmarker shift. Details on how each piece of information is decoded are presented in Table 1.

Table 1. 

Relationship between a cellular phenotype and characters in the book.

| Phenotype | Length | \[Start, Stop, Step\] |
| --- | --- | --- |
| Color <sup>a</sup> | 2 | \[0, 1, 1/4095\] |
| Intensity <sup>a</sup> | 2 | \[0, 40.95, 1/100\] |
| Mass | 2 | \[ 0.0, 4.095, 1/1000\] <sup>b</sup> |
| Radius | 2 | \[0.0, 0.1638, 0.4/10000\] <sup>c</sup> |
| *w* <sub>1</sub> (29,4) <sup>d</sup> | 232(2×116) | \[−2.048, 2.047, 1/1000\] |
| *w* <sub>2</sub> (5,28) <sup>d</sup> | 280(2×140) | \[−2.048, 2.047, 1/1000\] |
| Book start | 3 | \[AA, - -\] |
| Book end | 3 | \[AA, - -\] |
| Bookmarker | 3 | \[AA, - -\] |
| Advance | 1 | \[A, -\] |

*Note.* Phenotype is literally a feature or trait expressed in a cell, and length is the number of characters used to represent it. Columns \[Start, stop, step\] indicate the range of possible values and increments that a character can take when it is decoded.

<sup>a</sup>

For each 1 component of r, g, b.

<sup>b</sup>

Note, however, that there is a minimum value, and if it is less than 0.5, the value is simply 0.5. Additionally, there is an upper limit of 4.03.

<sup>c</sup>

Note, however, that there is a minimum value, and if it is less than 0.1, the value is simply 0.1.

<sup>d</sup>

Matrix of neural network weights.

[View large](https://direct.mit.edu/view-large/5348944)

For example, consider the “red” element of “color,” one of the phenotypes. Two characters are assigned to this expression, resulting in 4,096 combinations, ranging from “AA” to “- -.” Assigning these combinations equally between 0 and 1, we obtain the relation { *AA*, *AB*, ⋯, - -} = {0/4,095, 1/4,095, ⋯, 4,095/4,095}. Moreover, the possible range of values representing red among the cell colors is 0–1, with an increment of 1/4,095. Similarly, for the traits of mass and radius, two characters are assigned to each. As shown in Table 1 or the previous example, the minimum value that can be represented by these two characters is 0, corresponding to “AA.” However, if the mass or radius is 0 or a very small value, the simulation would break down. Therefore, for these traits, a separate minimum value is set apart from the actual minimum that can be represented by the two characters. If the decoded value from the corresponding string is below this set minimum value, the minimum value itself is assigned. In this simulation, minimum values of 0.5 and 0.1 were set for mass and radius, respectively. Furthermore, each element in the neural network weight matrices *w* <sub>1</sub> and *w* <sub>2</sub> is assigned two characters, with the range and increment being \[−2.048, 2.047, 1/1,000\].

The cell generates new cells based on this information. The location of the new cell generation is around the original cell, albeit randomly chosen. Additionally, the generated cell is connected to the cell from which it originated. Any further strings following this are interpreted as the next bookmarker in this cell. Specifically, the following string is read by every other character and used as the new bookmarker. For example, the new bookmarker would be “df” if the length of the bookmarker were 2 and the string following the specifics of the action were “def…,” as presented in Figure 5. This is a simple encryption to prevent the instruction about the new bookmarker from becoming the next read position. In other words, the bookmarker can be interpreted as an instruction saying “go to the place in the book written as ‘bf.”’ However, as this description includes the “bf” itself, the reading position would be set to this location. To avoid this, the instruction “go to the place in the book written as ‘bef’ (ignoring the middle character)” must be included. In this simulation, the length of the bookmarker is fixed at 2. The length of the book is a variable, as will be demonstrated subsequently; nevertheless, it is set to a maximum of 65,536. This new bookmarker-selection mechanism is the same for other actions, such as CONNECTION, DISCONNECTION, and TRANSITION, which will be discussed comprehensively in the subsequent sections.

Figure 5. 

Examples for EXPANSION.

#### 3.2.2 CONNECTION

The cell will be in a waiting state for the connection if the action is CONNECTION. This is the state in which a cell will be connected only if it exists near another cell that is also waiting to be connected. The following string is interpreted as the next bookmarker, as indicated in Figure 6.

Figure 6. 

Examples for CONNECTION.

#### 3.2.3 DISCONNECTION

The cell will be in a state waiting for disconnection if the action is DISCONNECTION. This is the state in which a cell will be disconnected if a connected cell is also awaiting its disconnection. The following string is interpreted as the next bookmarker, as indicated in Figure 7.

Figure 7. 

Examples for DISCONNECTION.

#### 3.2.4 TRANSITION

If the action is TRANSITION, the bookmarker is simply updated (Figure 8).

Figure 8. 

Examples for TRANSITION.

#### 3.2.5 Shift for Bookmarker

A procedure that repeats the same action indefinitely can be easily realized using the implementation process described. An example of the book and bookmarker that repeatedly expand the same cell is shown in Figure 9.

Figure 9. 

Example of book and bookmarker with repeated EXPANSION of the same cell.

However, if the same operation is to be repeated a finite number of times, the same content should be described in the book for that number of times, which is inefficient. To eliminate this problem, a string called *advance* is introduced. The advance string shifts the readout position of the new bookmarker. For example, the new bookmarker would be “Fh” if advance were 2 in Figure 9. Advance is also updated at this point. Subsequently, the string that follows the string interpreted as the new bookmarker becomes the new advance. In this example, the new advance is “i” if the length of advance is 1. This string is interpreted as a 64-decimal integer at runtime. In this simulation, the length of advance is fixed to 1. Figure 10 is the correspondence table between advance strings and integers.

Figure 10. 

Correspondence table between advance strings and integers.

On the basis of the preceding discussion, a book that exhibits self-reproduction while forming a tetrahedral body, for instance, can be written as depicted in Figure 11. The first bookmarker and advance are “aa” and “A,” respectively. A flow for forming the tetrahedron is as follows: First, “aa” starting from the third character of the book matches the bookmarker; therefore this is the first readout position. The next character specifies the action, which in this case is “A”; thus EXPANSION is executed. The cyan-highlighted string, beginning with “A- -,” is interpreted as representing various properties, such as the size and color of the cell to be expanded. Specifically, the sequence begins with “A-,” which represents the red component of the cell’s color, interpreted as 63/4,095, as detailed in. The following characters, “- -” and “- -,” correspond to the green and blue components, respectively, both interpreted as 4,095/4,095. These values indicate the absorption rates for each color, and the actual RGB color values are derived by subtracting them from 1. Next, the three “BA” characters denote the luminous intensity for each RGB color. Interpreted as a two-digit base-64 number, “BA” translates to 64; therefore the intensity for R, G, and B is set at 64/100. (Refer to Table 1 for the 1/100 scaling factor.) Following this, “H1” corresponds to the cell’s mass. Interpreted as a two-digit base-64 number, “H1” equals 501, which, with a scaling factor of 1/1,000, yields a mass of 0.501. This value exceeds the set minimum mass threshold of 0.5; therefore it remains 0.501. The subsequent characters “- -” represent the cell’s radius, decoded as 4,095, which translates to 0.1638 using the steps 0.4/10,000, also shown in Table 1. As this exceeds the minimum radius threshold of 0.1, it is retained as 0.1638. Furthermore, the green-highlighted strings that follow are interpreted as real numbers in sets of two characters each, serving as the elements of the neural network weights, as detailed in Table 1. The following magenta-highlighted string specifies the book area to be passed to the cell that is to be expanded, as well as bookmarker and advance. Specifically, “0+0” is interpreted as “00,” and the following “1+1” is interpreted as “11.” The area of the book that starts with “00” and ends with “11” is the book area to be passed to the cell that is to be expanded. The “0+0” next to “1+1” is interpreted as “00,” which is the bookmarker to be passed to the cell to be expanded, and the “A” next to it is advance. The subsequent gray-highlighted strings are interpreted as the next bookmarker and advance for the originating cell of the expansion, specifically, “bb” and “A,” respectively. Because the next bookmarker is “bb,” the subsequent location to be read is the red-highlighted “bb” in this book. Therefore a tetrahedron will be formed by repeating this operation in each cell.

Figure 11. 

Book repeatedly self-reproducing while forming tetrahedral bodies.

### 3.3 Neural Networks

Each cell has a feedforward neural network with only one hidden layer. The output of this neural network is as follows: (a) output *S* <sub>out</sub> to connected cells, (b) output *L* <sub>out</sub> to connected cells, (c) output *E* <sub>out</sub> to connected cells, (d) determine whether to read the book (read if it exceeds 0), (e) determine the proportion of the contacted cell to be eaten (eat if it exceeds 0), (f) determine whether to incorporate the book of contacted cells (incorporate if it exceeds 0), and (g) determine whether to emit light (emit light if it exceeds 0.2).

Here *L* <sub>out</sub> is the output for changing the position relative to the connected cell. The natural length of the springs connecting each cell increases if the value is positive and the magnitude is greater than a threshold. Conversely, the natural length of the spring decreases if the value is negative and the magnitude is greater than that threshold. Specifically, if the current natural length is *l* (*t*) and the natural length at the next step is *l* (*t* + *Δt* ), it is updated as follows: where *L* <sub><em>c</em></sub> is a coefficient that modulates the extent to which *L* <sub>out</sub> is reflected in the natural length. In this simulation, this threshold and coefficient were set to 0.7 and 0.2, respectively. The natural length does not become less than 0, and, as indicated in, it has a maximum value. Therefore this mechanism functions as a muscle in this virtual creature. Additionally, this value is used as input to the neural network of the connected cell.

*E* <sub>out</sub> determines the amount of energy transferred to the connected cell. The cell transports its own energy to the connected cell at a rate corresponding to the magnitude of the value if this value is positive. This value is also used as input to the neural network of the connected cell.

In contrast, *S* <sub>out</sub> causes no action, and its value is simply used as input to the connected cell. This enables each cell to communicate with the connected cells. The input to this connected cell is multiplied by the variable *q* and not simply the value of the output *S*. The variable *q* is updated according to the value of the output *S*, which is expressed as

(1)

This system functions as variable weights in this neural network. In other words, *q* is the coupling strength of the neural network between connected cells, on which the feedback from Equation is applied. This is a simplified version of Hebb’s (1949) rule, in which the firing of a neuron improves the strength of the connections between neurons. Here *Δs* is a parameter that determines the simulation environment. This parameter is set to 0.1 for the simulations in this study. The inputs to this neural network are as follows: (a) output *S* <sub>out</sub> from the connected cell, (b) output *L* <sub>out</sub> from the connected cell, (c) output *E* <sub>out</sub> from the connected cell, (d) ratio of red in the light impinging on the cell, (e) ratio of green in the light impinging on the cell, (f) ratio of blue in the light impinging on the cell, and (g) information that other cells have been contacted. For the contact information of other cells, the input value is calculated by multiplying with 0.5 the number of cells in contact. Figure 12 is a schematic diagram of this neural network.

Figure 12. 

Schematic of a neural network in one cell. The circles on the left- and right-hand sides represent the input and output, respectively. cell <sub><em>X</em></sub> denotes the *X* th connected cell, and *E* and *L* denote the energy and natural length of the spring, respectively. *N* is the maximum number of cells that can be connected to the cell. LIGHT and TOUCH on the input side are the information on light and a cell in contact with the cell, respectively. On the output side, READ determines whether to read the book, EAT determines whether to eat the contacted cells, FUSION determines whether to take in the book of the contacted cells, and LIGHT determines whether to emit light.

The numbers of units in the input, hidden, and output layers are $3 \times N_{max} + 4$ ⁠, 4, and $3 \times N_{max} + 4$ ⁠, respectively, where $N_{max}$ represents the maximum number of cells that can be connected to a given cell. In this simulation, we set *N* <sub>max</sub> = 8. Thus the weight *w* <sub>1</sub> from the input layer to the hidden layer forms a matrix of (28 + 1) × 4, and the weight *w* <sub>2</sub> from the hidden layer to the output layer forms a matrix of (4 + 1) × 28. The “+1” within the parentheses represents the inclusion of a bias term in the neural network weights. Each element of these matrices is determined by the book and is constant. Additionally, the activation function is $tan h$ ⁠.

In this neural network configuration, each layer’s number of units is fixed, so even if there is no cell currently connected at the *X* th position, the units corresponding to cell <sub><em>X</em></sub> *S*, cell <sub><em>X</em></sub> *L*, and cell <sub><em>X</em></sub> *E* in the input and output layers are always present. In cases in which no cell is connected at the *X* th position, the input values for cell <sub><em>X</em></sub> *S*, cell <sub><em>X</em></sub> *L*, and cell <sub><em>X</em></sub> *E* are set to zero, and the corresponding output layer units are unused. When a new cell becomes connected at the *X* th position, the first calculation cycle inputs zero for these parameters, and subsequent cycles will then reflect the inputs from the newly connected cells in the neural network calculations.

### 3.4 Energy

Cells have a quantity called energy, the value of which decreases at a fixed rate for each simulation step. The cell will die and disappear if the value falls below a certain amount, which mimics the metabolism of an organism.

The virtual creatures cannot increase their energy by themselves, as light from the sun placed above the field is the only energy source in this world. A cell can absorb light at a rate corresponding to its color and retain it as energy.

There are three situations in which the energy of a cell increases: (a) when absorbing light, (b) when eating other cells, and (c) when receiving energy from a connected cell. Conversely, there are five situations in which the cell energy is reduced: (a) when time has passed, (b) when eaten by other cells, (c) when transferring energy to the connected cell, (d) when generating a new cell, and (e) when emitting light. Details on these items are given in the following sections.

#### 3.4.1 Energy Change due to Light Absorption

The amount of light absorbed by a cell is expressed as the product of the light intensity and its light absorption coefficient, which consists of three components: red, green, and blue. As per the implementation, the cell color is determined as color = 1 – light absorption rate. If the light intensities for each component are *I* <sub><em>r</em></sub>, *I* <sub><em>g</em></sub>, and *I* <sub><em>b</em></sub> and the respective absorptivities of the cell are *a* <sub><em>r</em></sub>, *a* <sub><em>g</em></sub>, and *a* <sub><em>b</em></sub>, then the amount of light *ΔL* absorbed by the cell can be expressed as

(2)

Here the parameters of the amount of each color to be converted into energy must be determined. The conversion efficiencies of the three components into energy are expressed as *c* <sub><em>r</em></sub>, *c* <sub><em>g</em></sub>, and *c* <sub><em>b</em></sub>. Subsequently, the amount of energy *ΔE* <sub><em>L</em></sub> obtained from the light absorbed by the cell is calculated using

(3)

The parameters in this simulation were set to *c* <sub><em>r</em></sub> = 0.8, *c* <sub><em>g</em></sub> = 0.2, and *c* <sub><em>b</em></sub> = 0.8.

#### 3.4.2 Energy Change When Eating Cells

Cells can eat other cells that are in contact. The equation for the energy *ΔE* <sub><em>P</em></sub> obtained by eating a cell is expressed as

(4)

where *d* is the value of the unit labeled as “EAT” in the output layer of the neural network. In addition, *N* <sub><em>c</em></sub> is the number of connections of cells attempting predation, and $N_{c}^{′}$ is the number of connections of cells about to be predated. In other words, cells can only eat other cells with fewer connections than themselves.

#### 3.4.3 Energy Transport Between Connected Cells

As mentioned in, cells can transfer their own energy to the connected cells, and the magnitude of this energy transfer is determined by the output of the neural network. Specifically, when *v* <sub><em>x</em></sub> is the output value of the unit labeled cell <sub><em>x</em></sub> *E* in the output layer, the amount of energy *ΔE* <sub><em>T</em></sub> that the cell transfers to its *x* th connected cell can be expressed as

(5)

where *E* represents the energy of the cell that is attempting to transfer its energy.

#### 3.4.4 Energy Consumption Over Time

As mentioned earlier, the cell’s energy decreases with each simulation step. The cell energy *E* after *Δt* (one step) is updated, which is expressed as

(6)

where *N* <sub><em>c</em></sub> is the number of cells currently connected to the cell. *U* represents the energy decay parameter, which is defined as $U = C A^{N_{c} - N_{max}}$ ⁠. *C* and *A* are parameters for optimizing the energy consumption, where *C* is a real number greater than 0 and *A* is a real number greater than 1. In this simulation, 1.0 is used for *C*, and *A* is adjusted in real time such that the number of cells in the field is 4,000. This is because the indefinite proliferation of cells will result in insufficient computing memory and, consequently, a significant increase in computational costs. The optimal *A* to maintain the number of cells at 4,000 depends on the survival strategy of the virtual creature; however, there is a positive correlation between the number of cells and the parameter *A*. Specifically, a smaller value of *A* decreases the number of cells in the field because the energy consumption of the cell increases. Conversely, increasing the value of *A* reduces the energy consumption of the cell and increases the number of cells in the field.

The variations in *U* for several values of *A* are depicted in Figure 13. As observed in this graph, more energy is consumed when more cells are connected.

Figure 13. 

Values of *U* for several values of *A*. *C* is set to 1.0.

In this simulation, there is no energy expenditure due to exercise. Here “exercise” means changing the natural length between connected cells. Moreover, energy consumption is not considered for exchanging information between the cells using neural networks. However, in practice, it is more realistic to consider this type of energy consumption. The energy consumption according to the number of connected cells defined in Equation is introduced to consider the energy consumption associated with both changing the natural length of connected cells and exchanging information between cells via neural networks.

#### 3.4.5 Energy Change When a New Cell Is Generated

Energy is required for one cell to generate a new cell. There are two perspectives on this “required energy.” One perspective is that energy is consumed by the cell generation, and the other is that energy is passed on to the newly generated cell. We can reasonably assume that the required energy is the sum of these two perspectives. However, the energy consumed by cell generation is not considered in this simulation. Thus the only energy that the cell loses in generating a new cell is that which it imparts to the new cell at the time of generation. Here the magnitude of energy transferred to a new cell is based on that which the generated cell could acquire after a sufficient duration.

When a cell obtains energy from only one light source, the obtained energy converges to $E_{\infty}$ in a certain duration; $E_{\infty}$ can be estimated as follows:

(7)

where *ΔE* <sub><em>L</em></sub> represents the energy that the cells obtain from absorbed light, as described in, and varies for each cell. Moreover, *P* is the amount of light received per unit time per unit area, and *ΔS* is the cell area that receives light. For simplicity, I assumed that the distance between the light source and the cell remained constant. However, the distance could change with the scenario. For example, if we consider the sun as the light source in this simulation, the sun sways along the *x* axis. Therefore, for a fixed cell, the distance between it and the light source will vary periodically. Contrarily, if the cell moves with the sun, the distance will remain constant. Moreover, the distance may vary with the origin of the cell, and there might be cases in which the sun is not the light source. Therefore it is practically impossible to derive a general formula considering changes in the distance. Thus, in this study, I derived a formula assuming that the distance between a light source and a cell remains constant. This formula can be effectively used when a representative value is provided for the distance between the light source and the cell. Details of this derivation are provided in the.

Equation is valid for any light source. However, the energy $E_{\infty}^{\text{sun}}$ that can be attained by the newly generated cell can be predicted by considering the sun as the only light source. Here the distance when the cell is directly under the sun is considered the representative distance and, accordingly, used in the formula. In this simulation, this distance is set to 30. This energy, which is multiplied by a factor, is defined as the amount of energy transferred to the cell during its generation. This factor is set to 0.5 in the simulation. This implies that cells that obtain more energy in the future will incur higher generation costs. For example, white and black cells have smaller and higher generation costs, respectively, as indicated in Equation.

#### 3.4.6 Energy Change When a Cell Emits Light

As mentioned in, cells can emit light corresponding to the output of the neural network. Specifically, if the output value of the unit labeled “LIGHT ” in the output layer is greater than a certain threshold value, the cell emits photons in an amount proportional to its surface area. In this simulation, this threshold is set to 0.2. The emission intensity (*I* <sub><em>r</em></sub>, *I* <sub><em>g</em></sub>, *I* <sub><em>b</em></sub>) of the emitted photons is determined by the genes of the cell. In this case, the energy quantity *ΔE* <sub><em>E</em></sub> that the cell loses per photon can be expressed as

(8)

### 3.5 Environment

#### 3.5.1 Field

Simulations were performed on a 3-D field of 32 × 32 blocks with elevations and depressions. The maximum radius of the cell is set to 0.1638 when the length of one side of this block is 1. An example of a field is illustrated in Figure 1. A sun is located above the field and sways in one direction, emitting a constant number of light particles per unit time in random directions. In this simulation, this number is set to 16, and the sun’s altitude is set to 30 units above the average height of the field. The light emitted by the sun serves as the only source of energy in the model’s environment.

#### 3.5.2 Mutation

There are two types of mutations: (a) mutations that can occur for all cells at certain intervals of simulation steps and (b) mutations that occur only in the region of the new cell’s book containing the new cell’s information during cell division. These mutation probabilities are represented by α and β, respectively. The mutation occurring for all cells at certain intervals of simulation steps may affect either book or bookmarker. To elaborate, when a mutation occurs with a probability of α, there is an equal chance that it will affect either the book or the bookmarker. In the case of the book, one character from a randomly chosen spot in the cell’s book changes to any of the 64 types of characters. In the case of the bookmarker, two consecutive characters randomly chosen from the cell’s book become a new bookmarker. For the latter mutation, which occurs with a probability of β during cell division, one character in the book of the new cell changes randomly.

Four fields were independently calculated with different mutation probabilities in this simulation, and the virtual creatures were mixed on each field after a specific time, as shown in the conceptual diagram of Figure 14. The length of the specific time (time development) is set to 10 <sup>6</sup> steps.

Figure 14. 

Conceptual diagram of mutation. The probability of mutation occurring for all cells at certain intervals of the simulation steps is α, and the probability of mutation occurring only for the new cell book at cell division is β. Four fields were prepared and assigned different mutation probabilities to each field. After simulating a specific amount of time in each field, the virtual creatures grown in each field are distributed to the four fields, and simulation is rerun.

#### 3.5.3 Parameters for Connections

Cells can connect to surrounding cells, but connecting to cells that are significantly apart is unnatural. Therefore only cells within 1.95 times their radius *r* were allowed to be connected. In addition, the natural length of the connections between cells is varied according to the output of the neural network, but this is also unnatural if it is considerably stretched. Therefore this limit is set to 1.10 times a cell’s own radius *r*. Finally, the connections are broken if the distance between the connected cells is stretched for some reason (such as being pulled by other creatures) and exceeds 2.00 times the natural length.

#### 3.5.4 Processes Occurring Within One Step

The flow of processes conducted in one step of the simulation can be written as follows:

1. Each cell’s neural network is computed in the forward direction, and the output results are obtained.
2. The output results are input into the neural networks of the cells that are connected (*S*, *L*, *E*).
3. The update of *q*, defined by Equation, is performed according to the value of *S*.
4. The natural length of the springs connecting the cells is updated according to the value of *L*.
5. Energy transfer to the connected cells is conducted based on the value of *E*.
6. If the output unit labeled “READ” is positive, an operation based on the book is executed.
7. If the output unit labeled “LIGHT” exceeds a threshold, light is emitted.
8. Collision detection with the floor and walls is calculated.
9. Collision detection between cells and light is calculated, and this information is input into the cell’s neural network.
10. For cells in contact, predation and the fusion of the book are executed based on the neural network output.
11. Cells that are in proximity and awaiting a connection are connected.
12. The force from the spring, corresponding to the distance between the connected cells, is calculated.
13. Air resistance and gravity are calculated.
14. Energy is consumed over time.
15. The positions and velocities of cells are updated.

However, for reading the book, an interval is set. In this simulation, it is set to 200 steps. This means that the gene-derived operation is executed at most once every 200 steps. During the 200 steps when the book is not read, only actions derived from the neural network and physical calculations like gravity, air resistance, and spring force are performed.

As discussed in, the simulation involves numerous parameters that need to be predefined by the designer. For this study, I did not perform an exhaustive exploration of the parameter space; therefore the results and discussions presented here reflect only one of the many possible combinations of these parameters. The specific values used are as stated in. We will revisit these parameters and their implications for the study in.

Here we conducted simulations using a virtual creature that exhibited self-reproduction while forming a tetrahedron (Figure 11) as the initial creature. In other words, we observed the evolution of this tetrahedral virtual creature through repeated mutations and natural selection.

The results and discussion of the two observed virtual creatures and an examination of their ecology are presented here.

### 4.1 Dumbbell-Shaped Virtual Creatures

In the simulations performed, single cells were generated in several cases that proliferated by simple division in the early stages. One example of this is illustrated in Figure 15. Dumbbell-shaped virtual creatures can be observed after the simulation is continued for some time from this point, as depicted in Figure 16. The actual appearance of the virtual creatures is illustrated on the left, and a schematic of the self-reproduction is shown on the right. This reproductive process is similar to the binary fission observed in actual organisms, such as sea anemones (Hand & Uhlinger, 1992). This dumbbell-shaped morphology is first observed at approximately 15 × 10 <sup>6</sup> steps after the start of the simulation (top row in Figure 16). At the 193 × 10 <sup>6</sup> step, which is more than 10 times longer, the morphology did not change significantly; it merely changed in terms of color and size (bottom row in Figure 16). As mentioned in, the energy-conversion efficiency is set high for red and blue light; therefore this color change is considered an adaptation that reduces the absorption rate of green, which has a low energy-conversion efficiency.

Figure 15. 

Example of a single cell proliferating by simple division.

Figure 16. 

Dumbbell-shaped virtual creatures evolved from a single cell. The actual appearance of a virtual creature is shown on the left, and a schematic of self-reproduction is shown on the right.

Focusing on the morphogenetic process of this dumbbell-shaped virtual creature, the white cells were born between the second and third steps and disappeared between the fourth and fifth steps. This disappearance was caused by the green cells that were connected to white cells eating the white cells. I considered that this seemingly inexplicable process, in which the green cells ate the cells they generated, prevented the green cells from being eaten by other virtual creatures. As discussed in, cells with a high number of connections can eat cells with a low number of connections. Thus, without this white cell, the green cell at the edge would be vulnerable to predation by other virtual creatures because it has only one connection. This white cell increased the number of connections of the green cell and worked as a protector to physically prevent other virtual creatures from approaching it. In fact, the protector shifted toward a larger and whiter appearance, as illustrated in Figure 16. This is a reasonable change when attempting the protector expansion to repel predators at the lowest possible generation cost.

To confirm this role, a virtual creature is generated by partially editing the book of this dumbbell-shaped virtual creature to remove the process that generated the white cells. Specifically, “SgSEmEefaAe3” in the book is edited to “SgSEmEdfdAe3.” The differences in this morphogenetic process are depicted in Figure 17. This virtual creature without protector generation has a superior proliferation rate compared to the original dumbbell-type virtual creature because of its short self-reproduction cycle.

Figure 17. 

Comparison of morphogenetic process of (left) a dumbbell-type virtual creature and (right) a virtual creature whose book is edited to eliminate the process of protector generation.

These two types of virtual creatures were placed in the same field, and changes to their respective populations were observed, as shown in Figure 18. Notably, the simulation is run with a fixed *A*, referring to the simulation results of the dumbbell-shaped virtual organism before editing. The role of parameter *A* is discussed in. With time, the populations of virtual creatures without protectors will decline and eventually become extinct.

Figure 18. 

Population changes of a dumbbell-shaped virtual creature with protector (red) and a virtual creature, omitting the process of protector development (blue). (top) The change in respective populations with time. (bottom) Distribution in the field for three time periods.

This result strongly suggests that the white cells function as protectors. I considered that the morphology is acquired from the single-celled state shown in Figure 15, reflecting individual interactions.

### 4.2 Reticulated Virtual Creatures

The dumbbell-shaped virtual creatures discussed in contained two or three cells per individual. In this section, reticulated virtual creatures with a larger number of cells constituting one individual are discussed. Notably, this reticulated virtual creature is observed in simulations performed independently of the simulation presented in. The only difference between the two simulations is the seed value of the random number, which affected the formation of the terrain, mutations, and locations where the cells and photons were generated.

#### 4.2.1 Number of Connections and Energy Transport

As noted in, virtual creatures with a higher number of connections consume more energy. To increase the number of cells that constitute one individual, the virtual creature must acquire a mechanism for efficiently distributing energy throughout its body. The reticulated virtual creature illustrated here had acquired such a mechanism. The change in the number of connections and energy transport over the entire field versus simulation time is depicted in Figure 19.

Figure 19. 

Variation in the number of connections and energy transport times across the field versus simulation time. The solid line is the average of 5 × 10 <sup>5</sup> steps, and the shaded area indicates the widths of minimum and maximum values. (I), (II), (III), (IV), and (V) are labels of times with characteristic energy transport and number of bonds.

The energy transport between connected cells is approximately 0 until the simulation time (I) neared, and the number of connections fluctuated widely between 0 and 2,000. This fluctuation occurred because virtual creatures with several connections were born but could not survive in a stable manner because the energy is not distributed properly.

An example of a virtual creature from Figure 19 (I) is depicted in Figure 20. Only the bonding is visualized on the right-hand side of the figure, and it has a more complex morphology than the dumbbell type. It appears as if pink legs are growing against a yellow body, and these legs are in violent motion.

Figure 20. 

Example of a virtual creature from Figure 19 (I). (left) A cell and its bonding. (right) Only the bonding.

The number of energy transport events increased in proportion to the number of connections at Figure 19 (II). This occurred because the virtual creatures obtained the ability to distribute energy more efficiently. In fact, the number of connections was also stable from that point forward.

The virtual creatures seen on the field at times (II), (III), (IV), and (V) from Figure 19 are illustrated in Figure 21(a), (b), (c), and (d), respectively. The network increased with the simulation time. Accordingly, the color of the cells is closer to white, which incurred a small generation cost, as noted earlier. This is considered a survival strategy in which the energy that a single cell could acquire from light is reduced, thus creating a wide network and energy sharing across it.

Figure 21. 

Virtual creatures seen on the field: (a) Time II from Figure 19, (b) Time III, (c) Time IV, and (d) Time V. The network grows larger and whiter in color with simulation time.

Next, we consider the fact that the number of energy transfer events requires 2 × 10 <sup>7</sup> timesteps to start increasing and thereafter rapidly increases within a short duration. As mentioned in, the energy transfer is controlled by *w* <sub>1</sub> with (28 + 1) × 4 elements and *w* <sub>2</sub> with (4 + 1) × 28 elements. Therefore for the number of energy transport events to increase, these 256 elements must be properly optimized by mutations in the book. Therefore the simulation requires a certain number of timesteps to reach the appropriate book. Conversely, once a virtual creature capable of efficiently distributing energy is born, its population increases rapidly, as it is more successful in reproducing than are virtual creatures that cannot distribute energy. The theory of punctuated equilibrium in evolutionary biology includes two periods: one with few changes and another with rapid changes in the characteristics of organisms during evolution (Eldredge, 1972). The pattern of changes in the number of energy transfers observed in the simulation corresponds to this theory.

#### 4.2.2 How to Spread Offsprings Over a Wide Area

This reticulated virtual creature has a maximum of three connections extending from a single cell. Furthermore, it is simultaneously expanding and disconnecting the fourth cell. Figure 22 is a schematic of this scenario.

Figure 22. 

Schematic of cell disconnection: Step 1, original cell; Step 2, the fourth cell is expanded; Step 3, the connection distance between expanded and source cells is reduced; and Step 4, the bond is broken when reduction reaches the distance limit between cells, and the fourth cell is separated.

The cells expanded in Step 2 are connected to the cells from which they were generated. The natural length reduction of this spring is derived from the output signal of the neural network, as described in. Here the natural length can be reduced to zero, but the cells cannot completely overlap each other because of their sizes. Therefore contact between cells causes the spring to be stretched as the natural length of the spring is reduced. This connection will eventually break, because the bond is designed to break when the distance between cells is twice the natural length, as mentioned in. Figure 23 is a more detailed diagram of this mechanism in which the spring shreds. Moreover, disconnected cells are separated by repulsion. This mechanism is an essential function of this virtual creature to push the offspring farther away. This reproduction has similarities to the budding observed in real organisms, such as hydras (Bode, 2009; Martin et al., 1997), or to the spore reproduction observed in mosses (Luizi-Ponzo & da Costa Silva-e Costa, 2019).

Figure 23. 

Behavior of the spring connecting cells when it breaks. Natural length is represented as *l* and distance between cells as *d*. Until *l* = 2 *r*, natural length *l* and distance *d* coincide. However, if *l* is further reduced, the spring is stretched, as cells cannot approach any closer. Once *l* is reduced to less than *r*, the spring breaks, because 2 *l* < *d* = 2 *r*.

Notably, this disconnection is not one of the four direct actions driven by the book (DISCONNECTION); rather, it is induced by the change in natural length controlled by the neural network. Although the neural network’s parameters were determined by the book at the stage of EXPANSION, it then operates independently of the book-driven actions, according to the surrounding environment. Hence this neural network–triggered disconnection can be flexibly executed in response to the surrounding circumstances. In this case, the disconnection is performed under the condition that there were four connections. The reticulate virtual creature could have acquired the survival strategy whereby reaching three bonds is sufficient for growth and thus it is better to move to the procreation phase.

#### 4.2.3 Energy Transport and Parameters Δs

As mentioned earlier, the energy distribution is significant in a virtual creature composed of numerous cells. The amount of energy to distribute is determined by the neural network presented in. Next, I discuss the influence of changes in the parameter *Δs*, which determines the behavior of the neural network, on the virtual creatures. The simulations were run with *A* = 2.0, as discussed in.

This reticulated virtual creature evolved and grew in an environment where *Δs* = 0.1. First, the amount of available energy transport capacity in this setting is checked.

This experiment is performed according to the following procedure. First, one cell is sampled from Figure 21(d) and fixed in the center of the flat field. Second, energy is continuously provided only to that cell so that it continues to hold a certain amount of energy. This energy is set as approximately 10 times the energy required to produce the same cell. Third, cutting off light from the sun is simulated, and only energy from this fixed cell is supplied to the other cells. Even if this fixed cell generates other cells, the generated cell dies if the fixed cell cannot successfully transport energy. The number of cells in the field equilibrated after the simulation is run for some time. The reticulated virtual creatures at this instance are illustrated in Figure 24.

Figure 24. 

One cell from Figure 21(d) is sampled and fixed in the center of the flat field, and simulation is run with constant energy applied only to that fixed cell. The magnitude of this energy is set to twice the energy required to produce the same cell. (left) Only cell bonding. (right) The energy of each cell. *Δs* is set to 0.1.

The reticulated virtual creature could form a large body composed of several cells, even though only a fixed central cell is supplied with energy. This result indicates that energy transport is conducted efficiently.

Next, the simulation results when the parameter is changed to *Δs* = 0.0 are described in Figure 25. Compared with Figure 24, the network spread is smaller, and *Δs* = 0.0 caused problems in the information transfer between cells, indicating that the energy transport did not work efficiently.

Figure 25. 

One cell from Figure 21(d) is sampled and fixed in the center of the field, and simulation is run with constant energy applied only to that fixed cell. The magnitude of this energy is set to twice the energy required to produce the same cell. (left) Only cell bonding. (right) The energy of each cell. *Δs* is set to 0.0.

Finally, *Δs* is set to −0.1 for the reticulated virtual creature from Figure 24, and the results are illustrated in Figure 26.

Figure 26. 

*Δs* = −0.1 for a reticulated virtual creature from Figure 24.

In this case, the reticulated virtual creatures were scattered because the change in *Δs* = −0.1 malfunctioned the diffusion process discussed in.

These results indicate that Hebb’s rule, which is incorporated in a simplified manner, has a significant impact on energy transport and the diffusion of offspring. Specifically, energy transport exhibited a problem, and the size of the reticulated virtual creature is reduced if *Δs* is set to 0.0 and grown without updating the coupling strength. In addition, providing inverse feedback on the coupling strength by setting *Δs* to −0.1 caused a collapse that may have been due to a malfunction of the offspring diffusion process. This result demonstrates the importance of cell-to-cell communication in reproduction and development.

### 4.3 Changes in the Book due to Evolution

Here I briefly consider the changes in the book. The book of the dumbbell-shaped virtual creature has increased in length from 2,207 to 64,575 compared to the initial book shown in Figure 11. Figure 27 shows the book of this dumbbell-shaped virtual creature with two different color-coding schemes. First, in the left-hand-side image, the active regions (used regions) of the book are shown in yellow, while the inactive regions (unused regions) are shown in black. Here “active regions” refers to the regions involved in the cycle shown in Figure 16. In other words, even if the “inactive regions” other than these were removed, the dumbbell-shaped virtual creature would exhibit exactly the same life cycle as before, at least in appearance. Looking at this, it is clear that most of the regions are inactive. Only approximately 1.68% of the total is active.

Figure 27. 

A book of a dumbbell-shaped virtual creature is displayed with two distinct color-coding schemes. On the left, active regions (used regions) of the book are shown in yellow, while inactive regions (unused regions) are shown in black. On the right, regions that are considered to be derived from the initial book are shown in blue, while the rest are shown in black.

Next, in the right-hand-side image, the regions that are considered to be derived from the initial book shown in Figure 11 are shown in blue, while the rest are shown in black. Here, if a continuous sequence of five characters (a fragment) included in the book of the dumbbell-shaped virtual creature is also included in the initial book, then that region is assumed to be derived from the initial book. Examining this, most of the regions are blue, and under this assumption, approximately 97.5% can be considered to be derived from the initial book. However, when comparing the two color-coding schemes, it is clear that the “active regions” shown in yellow in the left-hand-side image and the “regions not derived from the initial book” shown in black in the right-hand-side image roughly overlap. This means that although most of the book of the dumbbell-shaped virtual creature is derived from the initial book, when limited to the regions that are actually active, most are not derived from the initial book. Only approximately 1.75% of the active regions can be considered to be derived from the initial book. This is thought to be due to the higher setting of the mutation β that occurs only for the new cell book at cell division, as shown in.

In the preceding consideration, if a continuous sequence of five characters (a fragment) included in the book is also included in the initial book, that region is considered to be derived from the initial book, but this choice of five characters is arbitrary. Instead of verifying the validity of this fragment length, we investigate how the results change when the length of the fragment is varied. Figure 28 illustrates the changes in the proportion of regions regarded as derived from the initial book in the entire book of the dumbbell-shaped virtual creature and the proportion of regions regarded as derived from the initial book in the active regions of the dumbbell-shaped virtual creature’s book when the length of the fragment is varied from 1 to 10. From this perspective, it is clear that both proportions tend to decrease as the length of the fragment increases, but the results of the aforementioned discussion do not change.

Figure 28. 

Proportion of the initial book in the entire sequence and proportion of the initial book in active regions vary when the length of the fragment considered to be derived from the initial book is changed from 1 to 10 in the book of the dumbbell-shaped virtual creature. Both proportions decrease as the length of the fragment increases, but the proportion of the initial book in the entire sequence remains over 95%, even at a fragment length of 10, indicating that most of this book is derived from the initial book. However, the proportion of the initial book in active regions is 33.5% when the length of the fragment is 1, 6.53% when it is 2, and 1.75% thereafter, indicating that regions that can be regarded as derived from the initial book are very few when only active regions are considered.

Next, the results for the reticulated virtual creature are depicted in Figures 29 and 30. This virtual creature also exhibits exactly the same characteristics as those observed in the dumbbell-shaped virtual creature. In other words, it is clear that although most of the reticulated virtual creature’s book is derived from the initial book, most of the active regions are not derived from the initial book.

Figure 29. 

A book of a reticulated virtual creature is shown with two types of color coding. On the left, active regions (used regions) of the book are shown in yellow, while inactive regions (unused regions) are shown in black. On the right, regions that are considered to be derived from the initial book are shown in blue, while the rest are shown in black.

Figure 30. 

The proportion of the initial book in the entire sequence and the proportion of the initial book in active regions vary when the length of the fragment considered to be derived from the initial book is changed from 1 to 10 in the book of the reticulated virtual creature. Both proportions decrease as the length of the fragment increases, but the proportion of the initial book in the entire sequence is over 80% even when the length of the fragment is 10, indicating that most of this book is derived from the initial book. In contrast, the proportion of the initial book in active regions is 35.6% when the length of the fragment is 1 and 7.13% when it is 2; it decreases to 0% when it is 5 or more. The regions that can be regarded as derived from the initial book are very few when only the active regions are considered.

### 4.4 Computing Resources and Time

This section describes the computational resources used in the simulations and the time they took to complete. I utilized an Intel(R) Xeon(R) W-1270P CPU with 16 cores for the simulations, with each core operating at a base frequency of 3.80 GHz and capable of turbo boosting up to 5.10 GHz. As mentioned in, each simulation involved the independent calculation of four fields, with virtual creatures from each field mixed after every 10 <sup>6</sup> steps. Each field was run on a single core, meaning that four cores were dedicated to each simulation. For the two types of virtual creatures presented thus far to have emerged, simulations on the order of 10 <sup>8</sup> steps were conducted. Given that each simulation step takes approximately 0.03 s on the aforementioned machine, the simulations required 2–3 months to complete.

This duration is not negligible and posed a challenge for advancing research. To expedite the simulations, several methods could be considered. One is optimizing parameters like the number of cells simulated and the mutation rate. Another possibility is increasing the number of fields calculated independently from four.

Future research will need to explore these and other potential optimizations to enhance the practicality of this model, making it more widely usable within the research community.

### 4.5 Model Design and Future Revisions

Numerous variables in the proposed model need to be decided before running simulations. These include the possible range of cell radii and mass, the number of units in the hidden layer of the neural network, mechanisms and thresholds related to natural length and energy transport between cells, various parameters related to connections discussed in, and variations of actions that cells can perform. In addition, there are environmental variables, such as mutation parameters, terrain, and the distance of the sun.

The simulations represent merely one example of the possible combinations of these variables. Future research should evaluate the impact of changes in these parameters. For this purpose, methods like the quantitative evaluation of evolutionary activity introduced by Bedau and Packard could be utilized (Bedau & Packard, 1996; Bedau et al., 1998). Another approach could be to evaluate Dolson et al.’s (2023) “complexity barrier,” particularly their proposed method for evaluating change potential by examining the number of genotypes that appear after being absent for a certain number of generations, and then survived selection can be almost directly adapted to the model proposed in this study.

Such evaluations will not only enable discussion of the qualities of the proposed model in terms of OEE but also serve as a catalyst for deepening the understanding of OEE through the many parameters of this model.

This study proposed a new model of Artificial Life that could handle reproduction, development, and individual interactions in a composite manner. Through the discussion of two virtual creatures discovered via mutation and natural selection, a proof-of-concept demonstration showcasing the model’s capabilities was conducted.

The reticulated virtual creature had an interesting reproduction process in which it detached parts of its own body and separated far from them. The virtual creature also grew a body composed of several cells by efficiently sharing energy, which is a more advanced developmental process than that observed in earlier tetrahedral virtual creatures. Regarding individual interactions, the dumbbell-shaped virtual creature acquired a form of protection by expanding a protective organ during division, making itself less susceptible to predation by other virtual creatures.

The two virtual creatures that emerged in this study were not thoroughly analyzed. For example, the specifics of the genetic book alterations that occurred during the evolutionary process, including the methodology for such analysis, are still under exploration. Future research should discuss the genetic factors, particularly focusing on the changes in the book’s descriptions when the method of energy distribution among cells shifted in the reticulated creatures. Also anticipated are detailed studies on the neural network signals of the virtual creatures during their activity.

However, several properties were not observed in this simulation. For example, all the virtual creatures observed in this study exhibited self-reproduction through asexual reproduction. Additionally, we did not observe the evolution of vertical growth or active movement. We assumed that one of the causes for this was simply the short simulation time, but the possibility that the model was not designed to easily produce such virtual creatures cannot be eliminated. Another challenge was that the field used in this simulation was not sufficiently large compared to the size of the cell. Therefore, as the simulation proceeded, the variety of virtual creatures in the same field remained almost exclusively the same.

Furthermore, owing to the high computational cost, only a handful of simulations could be conducted. Consequently, a thorough investigation into the extent of variation within the proposed framework or the factors determining the direction of evolution was not possible. The plausible factors that could steer evolution in a certain direction include the shape of the terrain and the maximum cell radius setting; nevertheless, their actual impact has not yet been investigated. The direction of evolution may also be influenced by changes in the length of the book. Further research is required to address these issues.

The source code for the Artificial Life model discussed in this study is publicly accessible on [GitHub](https://github.com/A5size/OpenPraparat) ([https://github.com/A5size/OpenPraparat](https://github.com/A5size/OpenPraparat)) and is licensed under the terms of the MIT License.

I thank Hirokazu Nitta for his feedback, which significantly helped enhance the manuscript, especially the Conclusion section. The advice and comments provided by Soichi Ezoe were also helpful in improving the Model and Methodology section. Moreover, I am deeply grateful to Kazumasa Itahashi. Kentaro Yonemura also read the article carefully and provided invaluable comments, especially about the wording of the text. In addition, Keisuke Tokiwa provided useful suggestions regarding the reproduction of the actual organisms cited in the article. I would like to express my sincere appreciation to everyone who provided comments, resolved bugs, and developed tools via GitHub, Niconico, and blogs. Their efforts will undoubtedly contribute to my future research. Finally, I thank Editage ([http://www.editage.com](http://www.editage.com/)) for English language editing.

1 

Owing to a minor error in the analysis program, the actual value is approximately 9.976 times.

Auerbach

,

J. E.

, &

Bongard

,

J. C.

(

2012

).. In

Proceedings of the 14th annual conference on Genetic and evolutionary computation

(pp.

521

–

528

).

Association for Computing Machinery

.

[https://doi.org/10.1145/2330163.2330238](https://doi.org/10.1145/2330163.2330238)

Balaz

,

I.

,

Petrić

,

T.

, &

Stillman

,

N.

(

2021

).. In

ALIFE 2021: The 2021 Conference on Artificial Life

(p.

98

).

MIT Press

.

[https://doi.org/10.1162/isal\_a\_00435](https://doi.org/10.1162/isal_a_00435)

Banks

,

E. R.

(

1971

)..

Massachusetts Institute of Technology

.

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Information%20processing%20and%20transmission%20in%20cellular%20automata%20%5BUnpublished%20doctoral%20dissertation%5D&author=E.%20R.%20Banks&publication_year=1971&book=)

Bedau

,

M. A.

, &

Packard

,

N. H.

(

1996

).

Measurement of evolutionary activity, teleology, and life

. [https://api.semanticscholar.org/CorpusID:16270216](https://api.semanticscholar.org/CorpusID:16270216) ().