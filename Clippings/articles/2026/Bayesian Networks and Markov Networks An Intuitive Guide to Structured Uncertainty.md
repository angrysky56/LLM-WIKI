---
title: "Bayesian Networks and Markov Networks: An Intuitive Guide to Structured Uncertainty"
source: "https://towardsdatascience.com/bayesian-networks-and-markov-networks-an-intuitive-guide-to-structured-uncertainty/"
author:
  - "[[Sean Moran]]"
published: 2026-06-10
created: 2026-06-10
description: "An intuitive introduction to reasoning with uncertainty, from directed Bayesian networks to undirected Markov networks and weighted logical rules."
tags:
  - "clippings"
---
explanations begin with prediction. A churn model estimates whether a customer is likely to leave. A fraud model estimates whether a transaction is suspicious. A diagnosis model estimates the likelihood of a condition from symptoms, tests and history. A document classifier assigns a category from text, metadata or embeddings.

In each case, the setup is broadly the same. We have some observed information, usually called the **inputs** or **features**, and a thing we want to predict, usually called the **target**. If we write the inputs as X and the target as Y, then the usual supervised learning problem is to learn a model of:

- *P(Y | X)*

That is, given the inputs, how likely is each possible output?

This framing is very useful. It gives us logistic regression, support vector machines, random forests, gradient boosting, neural networks, and a large part of modern applied machine learning. In many production settings, it is the right starting point. You have a target, some data, and a metric. The model’s job is to produce a good answer for that target.

Bayesian networks come from a different modelling instinct. They are useful when we want to represent a small uncertain world rather than only learn a mapping from inputs to one output. Instead of dividing the world into “inputs” and “target”, we describe a collection of uncertain variables:

- *X₁, …, Xₙ*

Some of these variables may be observed, some may be hidden, and any of them might become the thing we care about predicting. The graph describes how these uncertain variables depend on one another, where evidence can enter, and how beliefs should update when new information arrives.

A classifier is usually built around one prediction question:

- *Given these inputs, what is the output?*

A Bayesian network is built around a more general uncertainty question:

These uncertain things are related. Given evidence anywhere in the system, what should we now believe about the rest?

So rather than only asking for *P(Y | X)*, we represent a fuller joint distribution over the variables:

- P(*X₁, …, Xₙ)*

The purpose of the graph is to make that joint distribution manageable by encoding which variables depend directly on which others.

We will build the intuition in stages: first the full joint distribution, then a tiny wet-grass Bayesian network in Python, then explaining away any conditional independence, then parameter learning and inference, and finally Markov networks and Markov logic.

## The full joint distribution is the thing we cannot afford

Imagine a small world with a few uncertain facts: cloudiness, rain, sprinkler use, wet grass, slippery pavement, traffic, and late arrival.

In principle, the most complete probabilistic model would describe the probability of every possible configuration:

- *P(Cloudy, Rain, Sprinkler, WetGrass, SlipperyPavement, Traffic, LateArrival)*

This is the full joint distribution. If we had it, we could ask almost anything:

- *P(Rain | WetGrass)*
- *P(LateArrival | Rain, Traffic)*
- *P(Sprinkler | WetGrass, no Rain)*

The problem is that the full joint distribution grows brutally fast. If each variable is binary, then n variables require 2ⁿ possible configurations. Seven variables already give 128 states. Twenty variables give more than a million. One hundred variables are out of reach.

So the problem is partly statistical and partly representational. We need some way to avoid treating every variable as potentially entangled with every other variable in every possible way.

This is where graphical models enter.

A graphical model is a compact way of representing a probability distribution by making assumptions about structure. The graph says which local relationships we model directly, and which relationships we treat as indirect consequences of those local pieces.

The central idea is simple:

- *Do not model the whole uncertain world as one giant table. Break it into smaller conditional pieces.*

## A Bayesian network is a directed map of local dependence

Take the classic wet grass example. You walk outside and see that the grass is wet. Maybe it rained. Maybe the sprinkler was on. Maybe both happened. The model says that rain and sprinkler both influence whether the grass is wet. The probability distribution factorises as:

- *P(Rain, Sprinkler, WetGrass) = P(Rain) P(Sprinkler) P(WetGrass | Rain, Sprinkler)*

Instead of writing one table for every combination of rain, sprinkler and wet grass, we write smaller pieces:

- *P(Rain)*
- *P(Sprinkler)*
- *P(WetGrass | Rain, Sprinkler)*

The conditional table for wet grass is easy to imagine:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.20.20-1024x284.png)

Each variable gets a local probability model conditioned on its parents. For a Bayesian network over X₁, …, Xₙ, the general factorisation is:

- *P(X₁, …, Xₙ) = product over i of P(Xᵢ | Parents(Xᵢ))*

Each variable only needs to know about its direct parents. That is how a large probabilistic model becomes a collection of smaller, understandable pieces.

## A tiny Bayesian network in Python

It helps to make this concrete. We will build the smallest useful version of the wet grass model:

- *rain may or may not happen*
- *the sprinkler may or may not be on*
- *the grass may or may not be wet*

The structure is simple. Rain and sprinkler both influence whether the grass is wet. We can write the model as:

- *P(Rain, Sprinkler, WetGrass) = P(Rain) P(Sprinkler) P(WetGrass | Rain, Sprinkler)*

The first two terms are simple prior probabilities. The final term is a conditional probability table. Here is a deliberately small implementation using plain Python:

```python
from itertools import product
# Prior probabilities
P_RAIN = {
    True: 0.2,
    False: 0.8,
}
P_SPRINKLER = {
    True: 0.1,
    False: 0.9,
}
# Conditional probability table:
# P(WetGrass = True | Rain, Sprinkler)
P_WET_GIVEN_RAIN_SPRINKLER = {
    (False, False): 0.01,
    (False, True): 0.80,
    (True, False): 0.90,
    (True, True): 0.99,
}

def p_wet_grass(wet, rain, sprinkler):
    """
    Return P(WetGrass = wet | Rain = rain, Sprinkler = sprinkler).
    """
    p_wet = P_WET_GIVEN_RAIN_SPRINKLER[(rain, sprinkler)]
    return p_wet if wet else 1 - p_wet

def joint_probability(rain, sprinkler, wet):
    """
    Return P(Rain, Sprinkler, WetGrass).
    """
    return (
        P_RAIN[rain]
        * P_SPRINKLER[sprinkler]
        * p_wet_grass(wet, rain, sprinkler)
    )
```

This is the whole Bayesian network. There is no library, no fitting, and no machinery hidden behind an API. The structure of the model is visible in the multiplication:

```python
P_RAIN[rain] * P_SPRINKLER[sprinkler] * p_wet_grass(wet, rain, sprinkler)
```

That line is the factorisation written in code. Now we can enumerate every possible world.

```python
for rain, sprinkler, wet in product([False, True], repeat=3):
    p = joint_probability(rain, sprinkler, wet)
    print(
        f"Rain={rain:5}  Sprinkler={sprinkler:5}  "
        f"WetGrass={wet:5}  P={p:.4f}"
    )
```

This gives us the probability of each complete assignment.

A complete assignment means a full possible state of the little world: whether it rained, whether the sprinkler was on, and whether the grass was wet.

The probabilities across all possible worlds should sum to one:

```python
total = 0.0
for rain, sprinkler, wet in product([False, True], repeat=3):
    total += joint_probability(rain, sprinkler, wet)
print(total)
```

The result should be 1.0 which is a useful sanity check. We have built a valid joint probability distribution by multiplying smaller local probability tables.

## Asking questions of the model

Once we have the joint distribution, we can ask questions. For example:

- *P(Rain | WetGrass)*

In words, if the grass is wet, how likely is it that it rained? By Bayes’ rule:

- *P(Rain | WetGrass) = P(Rain, WetGrass) / P(WetGrass)*

We can calculate this by summing over the unobserved variable, which is the sprinkler:

```python
def probability_of_evidence(**evidence):
    """
    Sum the joint probability of all worlds that match the observed evidence.

    Example:
        probability_of_evidence(wet=True)
        probability_of_evidence(rain=True, wet=True)
    """
    total = 0.0
    for rain, sprinkler, wet in product([False, True], repeat=3):
        world = {
            "rain": rain,
            "sprinkler": sprinkler,
            "wet": wet,
        }
        matches_evidence = all(
            world[name] == value
            for name, value in evidence.items()
        )
        if matches_evidence:
            total += joint_probability(rain, sprinkler, wet)
    return total
```

Now we can compute:

```python
p_rain_and_wet = probability_of_evidence(rain=True, wet=True)
p_wet = probability_of_evidence(wet=True)
p_rain_given_wet = p_rain_and_wet / p_wet
print(p_rain_given_wet)
```

This gives 0.6897. So in this tiny model, once we observe wet grass, the probability of rain rises from its prior value of 0.2 to about 0.69. That is Bayesian updating. The observation has changed our belief.

## Evidence can support more than one explanation

Wet grass also makes the sprinkler more likely:

```python
p_sprinkler_and_wet = probability_of_evidence(sprinkler=True, wet=True)
p_sprinkler_given_wet = p_sprinkler_and_wet / p_wet
print(p_sprinkler_given_wet)
```

This gives: 0.3577. The sprinkler had prior probability 0.1. After observing wet grass, its probability rises to about 0.36. That makes sense. Wet grass is evidence for both possible causes.

Now we can look at explaining away. Suppose we know two things:

- *the grass is wet*
- *it definitely rained*

How likely is it that the sprinkler was on?

- P(Sprinkler | WetGrass, Rain)
```python
p_sprinkler_rain_wet = probability_of_evidence(
    sprinkler=True,
    rain=True,
    wet=True,
)
p_rain_wet = probability_of_evidence(
    rain=True,
    wet=True,
)
p_sprinkler_given_wet_and_rain = p_sprinkler_rain_wet / p_rain_wet
print(p_sprinkler_given_wet_and_rain)
```

This gives 0.1099, which is much lower than 0.3577. When we only knew the grass was wet, the sprinkler became more plausible. Once we also learned that it rained, the sprinkler became less necessary as an explanation. This is *explaining away*. The grass is wet. At first, rain and sprinkler are both plausible explanations. Once rain is known, some of the evidential pressure on sprinkler disappears.

This is one of the reasons Bayesian networks are useful for structured reasoning. Evidence does not simply move forward from inputs to output. It moves through the structure.

## The complete toy implementation

Here is the whole thing together:

```python
from itertools import product
# -----------------------------
# 1. Define the Bayesian network
# -----------------------------
P_RAIN = {
    True: 0.2,
    False: 0.8,
}
P_SPRINKLER = {
    True: 0.1,
    False: 0.9,
}
P_WET_GIVEN_RAIN_SPRINKLER = {
    (False, False): 0.01,
    (False, True): 0.80,
    (True, False): 0.90,
    (True, True): 0.99,
}

def p_wet_grass(wet, rain, sprinkler):
    p_wet = P_WET_GIVEN_RAIN_SPRINKLER[(rain, sprinkler)]
    return p_wet if wet else 1 - p_wet

def joint_probability(rain, sprinkler, wet):
    return (
        P_RAIN[rain]
        * P_SPRINKLER[sprinkler]
        * p_wet_grass(wet, rain, sprinkler)
    )

# -----------------------------
# 2. Sum over matching worlds
# -----------------------------
def probability_of_evidence(**evidence):
    total = 0.0
    for rain, sprinkler, wet in product([False, True], repeat=3):
        world = {
            "rain": rain,
            "sprinkler": sprinkler,
            "wet": wet,
        }
        if all(world[name] == value for name, value in evidence.items()):
            total += joint_probability(rain, sprinkler, wet)
    return total

def conditional_probability(query, given):
    """
    Compute P(query | given).
    query and given are dictionaries.
    Example:
        conditional_probability(
            query={"rain": True},
            given={"wet": True},
        )
    """
    numerator_evidence = dict(given)
    numerator_evidence.update(query)
    numerator = probability_of_evidence(**numerator_evidence)
    denominator = probability_of_evidence(**given)
    return numerator / denominator

# -----------------------------
# 3. Ask questions
# -----------------------------
print("Prior P(Rain):")
print(P_RAIN[True])
print("\nP(Rain | WetGrass):")
print(
    conditional_probability(
        query={"rain": True},
        given={"wet": True},
    )
)
print("\nP(Sprinkler | WetGrass):")
print(
    conditional_probability(
        query={"sprinkler": True},
        given={"wet": True},
    )
)
print("\nP(Sprinkler | WetGrass, Rain):")
print(
    conditional_probability(
        query={"sprinkler": True},
        given={"wet": True, "rain": True},
    )
)
```

Expected output is:

```python
P(Rain):
0.2
P(Rain | WetGrass):
0.6896551724137931
P(Sprinkler | WetGrass):
0.3577283372365339
P(Sprinkler | WetGrass, Rain):
0.10987791342952276
```

The key probabilities evolve as follows:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.19.14-1024x402.png)

Wet grass raises the probability of both rain and sprinkler. Then learning that it rained pushes the sprinkler probability back down. That is the article’s first concrete payoff. With a few probability tables and some enumeration, we get a model that can reason forwards, backwards, and sideways through uncertainty.

## The graph encodes what stops mattering

Now add cloudiness. Cloudiness influences whether it rains, and it may also influence whether someone turns on the sprinkler. Rain and sprinkler then influence whether the grass is wet.

The factorisation becomes:

- *P(C, R, S, W) = P(C) P(R | C) P(S | C) P(W | R, S)*

where:

```python
C = Cloudy
R = Rain
S = Sprinkler
W = Wet grass
```

This is already doing something subtle. The model says that wet grass depends directly on rain and sprinkler. It may depend indirectly on cloudiness, because cloudiness affects rain and sprinkler. Once we know whether it rained and whether the sprinkler was on, cloudiness no longer adds anything about wet grass.

Formally:

- *WetGrass ⟂ Cloudy | Rain, Sprinkler*

In words:

- *Wet grass is independent of cloudiness once rain and sprinkler are known.*

This does not make cloudiness irrelevant. It means cloudiness becomes irrelevant after the right variables have been observed.

That is one of the most useful ideas in Bayesian networks. They encode conditional independence. They tell us which information becomes redundant once other information is known.

In real systems, this matters. A signal can be useful before you observe a more direct cause, and useless afterwards. A variable can look predictive because it is standing in for another variable. A Bayesian network gives you a language for making those assumptions explicit.

## Evidence can enter anywhere

A standard classifier usually has a fixed direction. You feed in the features and get a prediction.

A Bayesian network is more flexible. Evidence can enter anywhere in the graph, and beliefs update throughout the system.

In the wet grass model, if we observe wet grass, our belief in rain increases. Our belief in sprinkler also increases. The effect has given us evidence about its possible causes.

This is diagnostic reasoning:

- *P(Rain | WetGrass)*

Now suppose we learn that it definitely rained.

The sprinkler becomes less necessary as an explanation. Its probability may go down relative to the moment when wet grass was the only evidence. This is called *explaining away*.

Before observing wet grass, rain and sprinkler may be independent or weakly related. After observing wet grass, they become connected through the shared effect. Evidence of one cause reduces the need for the other. This pattern appears everywhere.

A fever makes both flu and COVID more plausible. A positive flu test can reduce the probability that COVID is also needed to explain the fever, depending on the rest of the model. Missed payments can be explained by macroeconomic stress, a personal emergency, or both. Evidence for one explanation changes the probability of the other.

This is another reason Bayesian networks are useful for structured reasoning. They support reasoning in multiple directions. Causes predict effects, effects inform causes, and explanations compete with one another.

## Bayesian networks are useful when the question is not fixed

This is the practical distinction from logistic regression or SVMs. A logistic regression model is usually built for one conditional question:

- *P(Y = 1 | X)*

An SVM is similar in spirit, though less probabilistic by default. It tries to find a decision boundary that separates classes well.

These models are often exactly what you want. If the problem is “predict default from this feature vector”, a regularised logistic regression is a strong baseline and a boosted tree model may be the stronger production candidate.

A Bayesian network becomes interesting when the problem has a more structured shape.

Suppose we are modelling credit risk. Economic conditions may influence job loss. Job loss may influence missed payments. Interest rates may affect affordability. Missed payments may influence default risk.

Now there is more than one useful question. You may want to ask:

- *P(Default | MissedPayments)*
- *P(JobLoss | MissedPayments)*
- *P(Default | JobLoss, no MissedPayments)*
- *P(MissedPayments | EconomicConditions)*
- *P(Default | do(InterestRates = high))*

That last question moves toward causal modelling and requires stronger assumptions, but the point remains: at that point, the model is doing more than one-way prediction. It is representing a structured uncertain system.

A useful rule of thumb:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.27.26-1024x353.png)

## A real example: Bayesian networks for visual surveillance

A useful real-world example comes from Christopher Town’s PhD thesis, *Ontology based Visual Information Processing*, completed at the University of Cambridge Computer Laboratory. The thesis addresses the problem of deriving high-level representations from visual data by integrating different kinds of evidence and incorporating prior knowledge. It develops an inference framework for computer vision based on ontologies and ontological languages.

![](https://cdn-images-1.medium.com/max/1600/1*X3dKhHrL3z2GOufsmUvECg.png)

Figure 2: Ontology-driven Bayesian network for visual surveillance, adapted from the Town thesis example. Low-level detections and tracks provide uncertain evidence about object states, which support higher-level events and scenarios. The directed structure lets evidence propagate upward while allowing competing interpretations, such as meeting, tailgating or suspicious activity, to be compared probabilistically. Source: image by author via GPT5.5.

The problem is a good fit for Bayesian networks because surveillance video contains many uncertain intermediate facts.

At the low level, a vision system may detect blobs, contours, tracks, object positions, motion patterns, and appearance cues. These are noisy. A tracker may lose someone briefly. A shadow may look like motion. Two people may merge into one blob. An object detector may produce a plausible but uncertain label.

At the high level, the system may need to infer more semantic facts:

- *Is this object a person?*
- *Is the person walking, standing, entering, leaving or meeting someone?*
- *Is this a normal movement pattern or a suspicious event?*
- *Which objects are participating in the same scenario?*

A flat classifier could be trained to predict one label from a set of visual features. Town’s setup is more structured. The ontology defines the vocabulary of the domain: objects, states, roles, events, situations and scenarios. The Bayesian network then provides a probabilistic layer that connects noisy visual evidence to those higher-level interpretations.

The useful modelling pattern is:

- *Visual descriptors → Object states → Events → Scenarios*

For example, the system may observe that a moving blob has a particular size, shape, trajectory and appearance. Those visual descriptors provide evidence that the blob is a person. The person’s trajectory and proximity to other entities provide evidence about whether they are walking, waiting, approaching, meeting or leaving. Those inferred states then support higher-level event and scenario labels.

The important point is that each layer is uncertain. The model is representing the intermediate structure of interpretation.

A Bayesian network is natural here because evidence can arrive at different levels. A reliable track may strengthen an object hypothesis. A known object role may change how a motion pattern is interpreted. A high-level scenario can make some lower-level interpretations more plausible than others.

This is the same principle as the wet grass example, but in a richer setting. Wet grass is evidence for rain or sprinkler. In surveillance video, a noisy track, shape, motion pattern and spatial relation are evidence for an object state or event. Once one explanation becomes more likely, other explanations may become less necessary.

Town’s work is also a good example of why the graph structure matters. The ontology supplies domain structure: which kinds of entities exist, which states and events are meaningful, and which relationships are allowed. The Bayesian network supplies the probabilistic machinery: how to combine evidence, handle uncertainty, and infer high-level labels from noisy observations.

That makes it a useful practical example because it sits between hand-built expert systems and ordinary supervised learning. It uses domain knowledge, but it also learns from labelled video. It uses visual detectors, but it does not treat their outputs as certain. It recognises high-level situations, but it gets there through a chain of uncertain intermediate variables.

Bayesian networks are useful when we want to connect noisy evidence to a structured interpretation of the world.

## The hidden cost: someone has to believe the graph

The power of a Bayesian network comes from the structure. The danger also comes from the structure.

In the wet grass model, we are making assumptions.

We are saying wet grass has no other direct causes in this toy world. We are saying cloudiness affects wet grass only through rain and sprinkler. We are saying the arrows capture the relevant dependencies.

In small examples, this feels obvious. In real systems, it is harder. Who decides the graph?

Sometimes experts define it. Sometimes it is learned from data. Often it is a mixture of both. Expert-designed graphs can be interpretable but biased. Learned graphs can be data-driven but unstable, especially when variables are correlated, data is limited, or causal direction is ambiguous.

This is one reason Bayesian networks require more modelling discipline than a standard supervised learner. You have to think carefully about variables, arrows, missing causes, measurement errors, and conditional independence assumptions.

## How the probabilities are estimated

So far, we have treated the probabilities in the Bayesian network as if they were simply written down. In the wet grass example, we used values like P(Rain) = 0.2 and P(WetGrass | Rain, Sprinkler) = 0.99. Those numbers have to come from somewhere.

There are usually two learning problems in a Bayesian network.

- **Structure learning** decides which variables are connected.
- **Parameter learning** estimates the probabilities or distributions attached to each node.

The structure is the graph. The parameters are the local probability models. Once the graph has been chosen, parameter learning means estimating each local term:

- P(Xᵢ | Parents(Xᵢ))

That is one of the practical advantages of Bayesian networks: one large estimation problem becomes a set of smaller local estimation problems.

## Categorical variables

For categorical variables, parameter learning usually means filling in a conditional probability table.

For example, WetGrass | Rain, Sprinkler needs one row for every parent configuration:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.17.05-1024x306.png)

If we have labelled data, we estimate each row by counting. Among all examples where Rain = true and Sprinkler = false, count how often the grass was wet:

- P(WetGrass = true | Rain = true, Sprinkler = false) = count(WetGrass = true, Rain = true, Sprinkler = false) / count(Rain = true, Sprinkler = false)

If we saw 90 wet-grass cases out of 100 examples with rain and no sprinkler, the estimate is 0.9.

The intuition is simple, for each parent configuration, take the matching slice of the data and estimate the child distribution inside that slice. In Python:

```python
from collections import defaultdict
def estimate_binary_cpt(rows, child, parents):
    counts = defaultdict(lambda: {"total": 0, "true": 0})
    for row in rows:
        parent_values = tuple(row[parent] for parent in parents)
        counts[parent_values]["total"] += 1
        if row[child] is True:
            counts[parent_values]["true"] += 1
    cpt = {}
    for parent_values, values in counts.items():
        cpt[parent_values] = values["true"] / values["total"]
    return cpt
```

For a categorical child with more than two values, the same idea applies. Count each category and normalise so each row sums to one.

## Smoothing

Plain counting can break down when data is sparse. If a parent configuration appears once, the estimate is noisy. If it never appears, the estimate is undefined.

A common fix is smoothing. For a binary variable, instead of:

- *count(true) / count(total)*

use:

- *(count(true) + α) / (count(total) + 2α)*

When α = 1, this is Laplace smoothing. It prevents exact zero or one probabilities from tiny samples.

This matters because conditional probability tables grow quickly. If a categorical node has k possible values and its parents have m possible configurations, the table has roughly m(k − 1) free parameters. As the number of parents grows, data becomes sparse. This is one reason Bayesian networks usually prefer sparse parent sets.

## Continuous variables

Continuous variables need a local density model rather than a table. For a continuous node with no parents, a simple choice is a Gaussian:

- X ~ Normal(μ, σ²)

Parameter learning means estimating μ and σ² from data. The maximum likelihood estimates are the sample mean and variance.

If a continuous child has categorical parents, we can estimate a separate Gaussian for each parent state. For example:

- *Temperature | Flu = true ~ Normal(μ₁, σ₁²)*
- *Temperature | Flu = false ~ Normal(μ₀, σ₀²)*

So the model learns one temperature distribution for flu cases and another for non-flu cases.

If both the child and the parents are continuous, a common choice is a linear Gaussian model. For example:

- *BloodPressure | Age, BMI*

could be modelled as:

- *BloodPressure = β₀ + β₁ Age + β₂ BMI + ε*

where:

- *ε ~ Normal(0, σ²)*

The local conditional distribution is:

- *BloodPressure | Age, BMI ~ Normal(β₀ + β₁ Age + β₂ BMI, σ²)*

Parameter estimation now looks like ordinary linear regression. The Bayesian network still factorises a joint distribution, but one local factor is a regression model.

Each node has a local predictive model conditioned on its parents. For categorical children, that local model is often a conditional probability table. For continuous children, it may be a Gaussian, a linear Gaussian, or another conditional density model.

## Missing data

If all variables are observed in the training data, parameter learning is mostly counting, averaging, or fitting local regressions. If variables are hidden or missing, we often use expectation-maximisation, or EM. The rough idea is:

1. *Start with initial parameter guesses.*
2. *Use the current model to infer probable values for missing variables.*
3. *Re-estimate the parameters using those inferred values.*
4. *Repeat until the parameters stabilise.*

This is useful when some important variables are latent, partially observed, or inconsistently recorded. For example, we may observe symptoms and tests but not the true disease state for every patient.

The graph does not remove the need for statistical estimation. It makes estimation modular.

## The three basic structures

Most of the intuition for Bayesian networks comes from three small patterns.

### 1\. Chain

A chain has the form:

- A → B → C

For example, a disease may affect a biomarker, and the biomarker may affect a test result. Here, A influences C through B. If we know B, then A may no longer tell us anything extra about C:

- A ⟂ C | B

Once the middle variable is known, the upstream variable is screened off from the downstream variable.

### 2\. Fork

A fork has the form:

- A → B

and:

- A → C

For example, hot weather may increase both ice cream sales and sunburn.

Ice cream sales and sunburn may be correlated, but the relationship is explained by a shared cause. If we condition on weather, the association may disappear:

- B ⟂ C | A

This is a common-cause pattern.

### 3\. Collider

A collider has the form:

- A → C ← B

For example, rain and sprinkler can both cause wet grass. This one behaves differently. If we do not observe C, A and B may be independent. Once we observe C, they become dependent.

Wet grass connects rain and sprinkler. Fever connects possible diseases. A hiring decision connects talent and luck. A traffic jam connects accidents and roadworks.

This is the *explaining-away* pattern.

The collider is also the structure that most often trips people up. Conditioning on a common effect can create dependence where none existed before.

That is a source of many selection-bias problems.

If you only look at successful startups, founder quality and market luck may appear negatively related. A company can enter the “successful” set through exceptional execution, exceptional market timing, or some mixture of both. Conditioning on success can make the causes compete.

The graph gives us a way to see that.

## Inference is belief propagation over structure

Once we have a graph and local probability tables, inference means answering questions like:

- P(Rain | WetGrass)
- P(Default | MissedPayments, JobLoss)
- P(Disease | Symptoms, TestResult)

The mechanics can become technical: variable elimination, belief propagation, junction trees, sampling methods. But the intuition is straightforward.

Evidence enters the graph. Beliefs update locally. Those updates propagate through connected variables, constrained by the conditional independencies encoded in the structure.

In a tree-shaped graph, this can be efficient and exact. In dense or loopy graphs, inference can become expensive. That is another practical limit. Bayesian networks are elegant, but exact inference is not always cheap.

Still, the conceptual benefit remains. The graph makes the reasoning inspectable. You can often explain why a probability moved:

- *Wet grass observed.*
- *Rain probability increased.*
- *Sprinkler probability increased.*
- *Rain then confirmed.*
- *Sprinkler probability partially explained away.*

That kind of explanation is much harder to get from a pure discriminative classifier.

## What a junction tree is

Exact inference in a Bayesian network can become difficult when the graph has many interacting variables.

For a simple chain, evidence can be passed along the graph efficiently. In richer networks, the graph may contain loops once we ignore the direction of the arrows. Those loops make local message passing harder, because information can circulate and be counted more than once.

A *junction tree* is a way to reorganise the graph so exact inference becomes manageable.

The idea is:

- *Take the original graphical model, group tightly connected variables into clusters, and arrange those clusters into a tree.*
- *Each cluster is called a clique. Instead of passing messages between individual variables, the algorithm passes messages between clusters of variables.*

Suppose we have four variables:

- A, B, C, D

and the model has these dependencies:

- A → B
- A → C
- B → D
- C → D

In words, A influences B and C, and then B and C both influence D. The Bayesian network factorises as:

- P(A, B, C, D) = P(A) P(B | A) P(C | A) P(D | B, C)

This is a small network, but it already has a loop if we ignore arrow direction:

- A − B − D − C − A

That loop means exact inference is less straightforward than in a simple chain. For example, suppose we observe:

- D = true

and want to compute:

- P(A | D = true)

Evidence about D needs to flow backward through both B and C, then combine at A. The two paths are related because B and C share the same parent A.

A junction tree handles this by grouping variables into cliques. For this model, a useful set of cliques is:

- (A, B, C)

and:

- (B, C, D)

The junction tree is:

- (A, B, C) − (B, C, D)

The overlap between the two cliques is:

- (B, C)

That overlap is called the separator.

The idea is now cleaner. One clique handles the part of the model involving A, B, and C. The other clique handles the part involving B, C, and D. They communicate through the variables they share: B and C.

You can think of the two clique tables as:

- ψ₁(A, B, C)

and:

- ψ₂(B, C, D)

The evidence D = true is absorbed into the second clique, because D lives there. The second clique then sends a message to the first clique.

A message is just a summary table. It says:

- *Given everything I know on my side of the graph, here is what I imply about the variables we share.*

The right-hand clique cannot send its whole table to the left-hand clique, because the left-hand clique does not contain D. The only shared language between the two cliques is B and C.

So the second clique compresses everything it knows into a table over just B and C:

- m₂→₁(B, C) = sum over D of ψ₂(B, C, D)

If D has been observed, say D = true, then the incompatible values of D are ignored. In that case the message is essentially:

- m₂→₁(B, C) = ψ₂(B, C, D = true)

The message might look like this:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.16.20-1024x298.png)

This table says that, given D = true, the right clique thinks the combination B = true, C = true is the most plausible.

The left clique then combines that message with its own local table over A, B, C.

Suppose the left clique table is:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.15.54-1024x483.png)

The message is used by multiplying each row by the message value for that row’s B, C pair:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.13.38-1024x446.png)

Now sum the combined scores for each value of A.

For A = false:

- 0.020 + 0.060 + 0.060 + 0.090 = 0.230

For A = true:

- 0.005 + 0.040 + 0.090 + 0.720 = 0.855

So the unnormalised belief is:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.13.08-1024x225.png)

Now normalise:

- P(A = true | D = true) = 0.855 / (0.855 + 0.230) = 0.788
- P(A = false | D = true) = 0.230 / (0.855 + 0.230) = 0.212

So after receiving the message from the right clique, the left clique concludes:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.12.21-1024x219.png)

This is the junction tree idea in miniature. The evidence about D is converted into a message over B and C. The left clique combines that message with its own local relationship between A, B, and C. It then sums out B and C to get the belief about A.

![](https://cdn-images-1.medium.com/max/1600/1*vouARzkoSVWg3YgOl0h41A.png)

Figure 3: A junction tree turns a loopy Bayesian network into a tree of cliques. Evidence enters at D, is compressed into messages over shared variables, and is passed through the tree so the model can compute beliefs about A without double-counting evidence. Source: image by author via GPT5.5.

The method is exact, but it has a cost. Each clique needs a table over all its variables. If A, B, C, and D are binary, each three-variable clique has 2³ = 8 states, which is tiny. If a junction tree creates a clique with 20 binary variables, that clique has 2²⁰= 1,048,576 states. That is the trade-off. Junction trees make exact inference systematic, but they are only practical when the largest clique is not too large. The size of the largest clique is related to a graph property called *treewidth*. Low-treewidth graphs can be handled efficiently. High-treewidth graphs can make exact inference infeasible.

The practical lesson is that Bayesian networks are easier to reason with when the graph is sparse and the dependencies are local. The graph is not only an explanatory object. It affects whether inference is computationally tractable.

## Generative and discriminative are different modelling attitudes

This is a useful way to place Bayesian networks among other ML models.

A Bayesian network is usually a generative model. It tries to model how the variables in a domain jointly arise. A logistic regression or SVM is usually discriminative. It models the boundary or conditional relationship needed for prediction.

Discriminative framing:

- P(Y | X)

Generative framing:

- P(X, Y)

or more generally:

- P(X₁, …, Xₙ)

Generative models are often more work because they model more of the world. That extra structure can be useful when you want to handle missing data, reason backwards from effects to causes, simulate scenarios, or incorporate domain knowledge.

Discriminative models often fit narrow prediction problems well because they spend their capacity directly on the decision you care about. The key question is: are you trying to predict a label, or represent a system?

For many supervised learning tasks, start with the supervised model. For structured uncertainty, Bayesian networks become more interesting.

## A small medical example

Suppose we model flu, fever, cough and fatigue. The assumption is simple: flu can cause fever, cough and fatigue.

The factorisation is:

- P(Flu, Fever, Cough, Fatigue) = P(Flu) P(Fever | Flu) P(Cough | Flu) P(Fatigue | Flu)

This is a simple diagnostic model. If we observe fever and cough, flu becomes more likely:

- P(Flu | Fever, Cough)

If we also observe a negative flu test, flu becomes less likely. If the test is noisy, it may not drop to zero. If we observe fatigue too, it may rise again.

The same model can answer different questions depending on which evidence is available. That is the important point.

A classifier would usually need a fixed feature vector made up of fever, cough, fatigue, test result and any other available predictors. That may be simpler and more accurate if all features are present and the only question is flu prediction. The Bayesian network gives you a more structured object. It can represent the reliability of tests, missing symptoms, shared causes, and competing diagnoses.

Now extend the example. Flu can cause fever and cough. COVID can also cause fever and cough.

Fever and cough can now be explained by different diseases. Observing symptoms increases belief in both. Confirming one diagnosis changes the probability of the other. This is exactly the kind of reasoning Bayesian networks were built to express.

## Where Markov networks enter

Bayesian networks use directed edges. The arrows matter. They support a natural story of local conditional dependence, and sometimes a causal interpretation if the graph was built that way.

Some domains have relationships where direction is awkward. Consider image denoising. Nearby pixels tend to have similar labels. If one pixel is foreground, its neighbours are more likely to be foreground too. Which pixel causes which? Usually, none of them. The relationship is symmetric. Neighbouring labels are mutually compatible.

This is where Markov networks, also called Markov random fields, become natural.

A Markov network is an undirected graphical model. Instead of arrows and conditional probability tables, it uses compatibility functions over connected groups of variables.

For a simple chain of three variables A, B, and C, where A is connected to B, and B is connected to C, we might write:

- P(A, B, C) = (1 / Z) φ₁(A, B) φ₂(B, C)

The φ functions are potentials. They are not probabilities by themselves. They are scores saying how compatible certain assignments are. For example:

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/Screenshot-2026-06-06-at-18.07.33-1024x298.png)

This says A and B prefer to have the same value. The Z term is the partition function. It normalises all the unnormalised compatibility scores into a proper probability distribution:

- Z = sum over A, B, C of φ₁(A, B) φ₂(B, C)

That normalisation is often expensive. In large Markov networks, computing Z can be one of the main difficulties.

## Bayesian networks generate; Markov networks constrain

A useful intuition is:

- A *Bayesian network* describes how variables are generated from their parents.
- A *Markov network* describes which configurations of variables are compatible.

For a Bayesian network, a medical example feels natural: disease influences symptoms. For a Markov network, an image example feels natural: neighbouring pixel labels prefer to agree.

The Bayesian network feels like a *causal or diagnostic story*. The Markov network feels like a *system of soft constraints*.

This distinction is not absolute. Bayesian networks can represent non-causal structure, and Markov networks can be used in many settings beyond spatial constraints. But as a first mental model, it is useful.

Use a Bayesian network when direction is meaningful. Cloudiness affects rain. Rain affects wet grass. Disease affects symptoms. Economic stress affects missed payments.

Use a Markov network when compatibility is more natural than direction. Neighbouring pixels should usually agree. Adjacent words should have compatible labels. Nearby locations should have similar states.

Conditional random fields sit in this family. A CRF models:

- P(Y | X)

where Y is usually a structured output, such as a sequence of labels, and X is the observed input. They became popular for tasks like named entity recognition before neural sequence models took over much of that territory.

The conceptual point remains useful: sometimes prediction is structured, and the labels should be modelled together.

## Where Markov logic fits

There is one more useful step in this family: *Markov logic*. A Markov network gives us soft compatibility constraints between variables. Markov logic adds a language for writing those constraints as rules.

For example:

- Friends(x, y) → SimilarPreferences(x, y)

or:

- WorksAt(x, c) AND LocatedIn(c, city) → LivesNear(x, city)

In ordinary logic, rules are brittle. A rule is true or false. If the rule is broken, the world becomes invalid.

Real domains rarely behave like that. Friends often share preferences, but not always. People often live near work, but not always. Customers who complain repeatedly are more likely to churn, but not always. These are useful patterns, not laws.

Markov logic networks attach weights to rules. A high-weight rule is a strong preference. A low-weight rule is a weak preference. Worlds that satisfy many high-weight rules receive higher probability. Worlds that violate them remain possible, but less likely.

The usual form is:

- P(X = x) = (1 / Z) exp(sum over i of wᵢ nᵢ(x))

where:

- *wᵢ is the weight of rule i*
- *nᵢ(x) is the number of times rule i is satisfied in world x*
- *Z is the partition function*

The intuition is simple: worlds that satisfy many high-weight rules get higher probability.

Suppose we write:

- w: Smokes(x) AND Friends(x, y) → Smokes(y)

This does not say that friends must share smoking behaviour. It says that, all else equal, worlds where friends have similar smoking behaviour should be more probable than worlds where that tendency is repeatedly violated.

That is the Markov network idea expressed through logic. The rules define the soft constraints. The weights say how strongly each constraint matters. The resulting probability distribution is a Markov network grounded over the objects and relationships in the domain.

This becomes useful when the domain has relational structure: people, organisations, products, documents, citations, transactions, accounts, devices, events. The same rule can apply repeatedly across many entities.

For example:

- Mentions(Document, Company) AND Acquires(Company, Target) → Relevant(Document, Target)

That kind of pattern is awkward to express as a flat feature vector. Markov logic gives you a way to write the relational pattern directly, while keeping the uncertainty.

The progression is natural:

- *Bayesian networks represent directed dependence.*
- *Markov networks represent undirected compatibility.*
- *Markov logic networks represent weighted logical rules as undirected probabilistic structure.*

This is the bridge from graphical models into probabilistic logic and knowledge representation.

## Why this still matters

It is easy to treat Bayesian networks and Markov networks as older machinery from before the current neural era. In some production environments, that is a fair instinct. If you have a huge labelled dataset and a narrow prediction task, these methods are rarely the first stop.

The ideas behind them remain central. They give us a disciplined way to think about uncertainty, structure, evidence, independence, explanation, and relational reasoning. They make us ask questions that plain supervised learning can hide:

- *What is the target?*
- *What are the causes?*
- *What are the effects?*
- *Which variables become irrelevant after others are known?*
- *Where can evidence enter the system?*
- *Are we predicting one thing, or reasoning over many things?*
- *Are the relationships directional, symmetric, or rule-like?*

These questions matter even when the final model is not a Bayesian network, a Markov network, or a Markov logic network.

In applied ML, it is easy to flatten the world into a feature matrix and let the model sort it out. Sometimes that is exactly the right engineering choice. It still comes with assumptions. Those assumptions move into the data pipeline, the feature set, the sampling process, and the interpretation layer.

Graphical models force the assumptions back into view. That is their enduring value.

## The practical takeaway

Use logistic regression when you want a simple, interpretable classifier.

Use an SVM when you want a strong decision boundary, especially in medium-sized, high-dimensional settings.

Use boosted trees or neural networks when predictive performance is the main objective and you have enough data.

Use a Bayesian network when you need to reason about a structured uncertain system, especially when evidence may arrive in different places, domain knowledge matters, missing data is common, or explanation is part of the job.

Use a Markov network when the relationships are less about direction and more about compatibility, agreement, or soft constraints between neighbouring variables.

Use Markov logic when the domain has objects, relationships and imperfect rules. It gives you a way to express relational knowledge without pretending that every rule is absolute.

The core distinction is:

- A **classifier** is built around a *prediction question*.
- A **graphical model** is built around an *uncertain system*.
- **Markov logic** extends that system with *weighted rules over objects and relationships*.

Once that distinction is clear, Bayesian networks, Markov networks and Markov logic become easier to place. Bayesian networks are useful when direction carries meaning. Markov networks are useful when compatibility is the better representation. Markov logic is useful when those compatibilities are easier to write as imperfect rules over objects and relationships.

***Disclaimer:*** *The views and opinions expressed in this article are my own and do not represent those of my employer or any affiliated organizations. The content is based on personal experience and reflection, and should not be taken as professional or academic advice.*

## References

- [Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*. Morgan Kaufmann.](https://dl.acm.org/doi/book/10.5555/534975) Classic foundation for Bayesian networks, belief propagation, and probabilistic reasoning under uncertainty.
- [Koller, D. and Friedman, N. (2009). *Probabilistic Graphical Models: Principles and Techniques*](https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/). MIT Press. The standard modern textbook on Bayesian networks, Markov networks, inference, learning, and structured probabilistic modelling.
- [Town, C. (2004). *Ontology based Visual Information Processing*. PhD thesis, University of Cambridge](https://www.cl.cam.ac.uk/~cpt23/papers/TownPhD.pdf). A useful applied example of combining visual evidence, ontologies, and probabilistic reasoning for scene understanding.
- [Town, C. (2004). “Ontology-driven Bayesian Networks for Dynamic Scene Understanding”](https://ui.adsabs.harvard.edu/abs/2004cvpr.conf..123T/abstract). *CVPR Workshop on Detection and Recognition of Events in Video*. A compact real-world example of Bayesian networks applied to dynamic scene and event recognition.
- [Richardson, M. and Domingos, P. (2006). “Markov Logic Networks”. *Machine Learning*.](https://link.springer.com/article/10.1007/s10994-006-5833-1) The core paper introducing Markov logic: weighted first-order logic grounded into Markov networks.
- [Koller, D., Friedman, N., Getoor, L. and Taskar, B. (2007). “Graphical Models in a Nutshell”](https://ai.stanford.edu/~koller/Papers/Koller%2Bal%3ASRL07.pdf). A concise overview of graphical models and their role in statistical relational learning.