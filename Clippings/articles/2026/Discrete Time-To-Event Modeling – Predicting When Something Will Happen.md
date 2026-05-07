---
title: "Discrete Time-To-Event Modeling – Predicting When Something Will Happen"
source: "https://towardsdatascience.com/discrete-time-to-event-modeling-predicting-when-something-will-happen/"
author:
  - "[[Jarom Hulet]]"
published: 2026-05-05
created: 2026-05-07
description: "Part 1: The basics — discretization of time, censoring and the life table"
tags:
  - "clippings"
---
## Introduction

data science problems predict the *what* — for example, *what* will a house sell for? Or *what* will a customer purchase? Or *what* is the probability that a patient has a disease?

Many real-world decisions, however, depend just as much on *when* something will happen. How long until a customer churns? When will a loan default? How much time remains before a component fails?

Predicting when something will happen is a predictive modeling use case that doesn’t get much attention in introductory materials. Predicting the “when” is often referred to as **time-to-event modeling** or **survival analysis**.

While event modeling shares techniques and intuitions with more traditional predictive modeling, it also introduces nuances that must be accommodated to create effective predictions.

This is the start of a multi-part series that will cover the basics of time-to-event modeling. This first part will discuss basic concepts while future articles will cover time-to-event model development techniques.

Here are the three topics I’ll cover in this article:

- Putting events into discrete time
- Censoring in event data
- The life table

## Discretizing Time

While time is continuous by nature, depending on the time-to-event modeling use case, it can be appropriate to treat time as continuous or discrete. In this article we’ll be focusing on discrete, but I do want to spend a little time discussing the decision of discrete vs. continuous time treatment.

### Guidelines for when to treat time as continuous

Time is often best treated as continuous when:

- The event can occur at any point in time and is inherently continuous (we’ll contrast this with the less intuitive, inherently discrete events in the next section). Equipment failure is a common example.
- The timing of the event can be measured precisely. It is difficult to measure the exact moment an unemployed person gets a job, but modern vehicle sensors can capture the exact timing of a car accident.
- The granularity of the time measurement is very small relative to the overall time horizon. For example, measuring events down to the second when the natural timeline of the event spans weeks or months.

Note that, measuring time in small increments alone does not automatically imply a continuous-time setting. Consider human response time to changing images. Response time can be measured in centiseconds (1/100 of a second), but since typical response times are on the order of 2–3 centiseconds, this unit represents a large portion of the underlying timeline. Despite the small unit of measurement, this example probably wouldn’t do well as a continuous-time model.

### Guidelines for when to treat time as discrete

- The event itself is inherently discrete. For example, a customer can only miss a payment on a due date; they cannot miss it at an arbitrary point in time.
- Precise event timing cannot be reliably captured. We can’t know exactly when a pipe burst or when a person contracted a disease.
- Data are aggregated at discrete intervals for practical reasons. In many applications, treating time as continuous adds little value. In home insurance, for example, it rarely matters what second a pipe burst or a fire started; the relevant unit is typically just the day of the event or the day the claim was filed.

When the modeling context requires discrete time, an explicit decision must be made about how to discretize. This requires a good understanding of the problem domain. In life insurance, time is often measured in years; in business reporting, months or quarters may be more appropriate.

A note on ties — One additional difference I wanted to call out between discrete and continuous time are ‘ties’ — i.e., an event happening at the exact same time for multiple observations. Many continuous time-to-event modeling techniques assume that ties are not possible and do not exist in the dataset. Discrete time-to-event approaches do not have this assumption and depending on the use case, ties can be frequent (think of insurance claims in a month).

## Censoring

Data censoring is much more common in time-to-event data than in more traditional machine learning applications. Data censoring occurs when the value of an observation is only partially known — we might know it lies above (right censoring) or below (left censoring) a certain point, but we don’t know the actual value.

Think of yourself as an example, how many years are you going to live? You know you will at least live to your current age (because you already have), but you don’t know how much further you’ll make it. You are a right censored data point! Your great-great grandmother is not censored because she has already passed, you can find out how long she lived. Okay, enough of this example, I don’t like contemplating my own mortality.

While right and left censoring can occur in time-to-event applications, I’ll focus my discussion on right censoring because it is the most common type you’ll come across. Right censoring will usually come from two phenomena in the data: **(1)** **the event hasn’t happened** or hasn’t had full opportunity to happen for some observations and **(2)** **data stopped being collected** for some observations at some point in time. We’ll spend a little time discussing each.

### The event hasn’t happened

Our slightly too-real life span example falls into the category of censoring due to an event not happening. Death and taxes are inevitable — or so they say. But not all events that you might need to model are guaranteed to eventually happen. Think of modeling when someone gets the flu, gets fired from their job or when an insurance claim on a house is filed. These are things that could or could not happen, but they are also subject to censoring.

Let’s explore the home insurance example a little more. We want to predict the timing of claims for a set of home insurance policies. We have a dataset with 1-year contracts that goes back to contracts that started 5 years ago and includes data up to last month. Stop and think about where the censoring comes in here. All contracts that originated less than a year ago are right censored — we don’t know how many claims they will have because they are still open.

### Data stopped being collected

Sometimes our data are censored because we fail to collect event data for various reasons. Imagine we are doing a study on how long it takes a job seeker to get an offer. We start out with 500 participants in our study, but after a little while, 50 of them stop answering our calls and emails. We know what their offer status was the last time we contacted them, but we don’t know what it is now or in the future (assuming they continue to ghost us).

To further illustrate, let’s go back to our home insurance example. We will probably have some customers that will cancel their contracts with us during the contract period. For these customers, we know the number and timing of claims (if any) up to cancellation, but after they cancel, we don’t know if they had a claimable event(s).

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/04/image-30-1024x420.png)

Illustration of censoring in time-to-event data – image by author

### What happens if you don’t do anything about data censoring?

Models that are created without addressing censoring will present bias in their predictions. Because we are observing events, more censoring reduces the number of observed events. When our model sees fewer events, it predicts them less frequently. Time-to-event models built without accommodations for censoring will generate predictions that are biased below actual observed events.

Additional Note: Most time-to-event methods assume censoring is non-informative. Meaning the reason an observation is censored is unrelated to its underlying event risk after accounting for observed features. If censoring is related to event risk, standard time-to-event methods can become biased. In some applications, it may be more appropriate to model the censoring mechanism explicitly. For example, by treating it as a competing risk.

The good news is that there is a simple data transformation that corrects for time-based right censoring. The life table provides a clear and intuitive way to see how this correction works.

## The Life Table

Life tables are very simple, but illustrative tools for modeling time-to-event data. While the actual prediction methodology is generally inflexible and underfit, understanding the data structuring in life tables sets a good foundation for more advanced time-to-event modeling approaches.

Before getting into the nitty-gritty of life tables, I want to give a conceptual overview of what they do. In short, life tables cut time into multiple discrete chunks to manage the censoring challenge.

Think about a single home insurance policy. We can definitely know the number of claims by simply observing the contract until it expires. But to do that, we have to wait until the contract ends, which delays our ability to learn from recent data. The life table allows us to start learning from the data much more quickly by cutting time into discrete chunks. We can learn from each discrete chunk of time as soon as it ends. Instead of waiting on a home insurance policy expiration date, we can start learning after the first month (if we discretize time by month).

Each row of a life table corresponds to a discrete unit of time. The columns of the life table broadly fit into two categories: (1) observational data and (2) calculations from the observational data. The **observational columns** include the number of units ‘at risk’ (units that could have an event happen to them), number of units that did have the event occur and the number of units that were censored. The **calculation columns** include number of units adjusted for censoring, the conditional probability of the event, the unconditional probability of the event and the survival probability.

Verbally describing the life table isn’t easy. Let’s go through an example to develop our intuition.

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/image-334.png)

Example of life table – image by author Note, I added the additional (1-conditional prob) column for illustration

![](https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/image-335-1024x138.png)

Table with the excel formulas to illustrate calculations – image by author

I want to re-emphasize the importance of understanding the calculations in the life table. While life tables themselves are rarely used for predictive modeling, the details of the calculations are absolutely fundamental knowledge when using more advanced techniques.

If you are able to read through the formulas and get it, great! If not, I left additional comments on each calculation below.

Let’s go through the columns one at a time.

**Discrete Time** — The sequential discretized units of time. These could be days, weeks, months etc.

**Units at Risk** — This column is the number of units at risk at the beginning of each time period. In other words, they are the number of units that did not have the event before the time period under consideration.

The first value of 1,283 is an input, the other values can be calculated by subtracting the censored units and number of events from the prior time period’s units at risk.

**Censored** — These are the number of units that were censored in the current time period. Note that these calculations assume that they were censored at the beginning of the time period. Meaning that the censored units were not ‘at risk’ during time period. Simple modifications to the calculations can change the assumption about the timing of the censoring. Risk exposure for the full time period and half of the time period are common modifications.

**Conditional Probability** —In discrete-time survival analysis, this is often referred to as the hazard. It is the probability of the event occurring in the current interval given survival up to that interval.

**1-Conditional Probability** — Simple calculation to get the conditional survival probability.

**Survival Probability** — The products of all of the conditional survival probabilities up to the current point. You can think of survival as a series of coin flips with varying probabilities of getting heads for each flip. The survival probability captures that probability that you will not flip a heads *n* times in a row.

**Unconditional Probability** – This calculation captures the probability of an event in a specific time period not conditioned on survival up to that point. It deconditions by multiplying the probability of the event in time period n by the product of all of the survival probabilities in the time periods for 1 to n-1.

## Wrapping It Up

Time-to-event modeling gives us the tools to predict when something will happen. This differs from the more common machine learning approaches that predict *what* or *how much*.

In this article, we discussed three main points. (1) Discretizing time, (2) understanding censoring in time-to-event data, and (3) using the life table as a demonstration of how censoring can be addressed through data structuring.

In the next article, we’ll build on these concepts and show how they translate into practical predictive modeling techniques.