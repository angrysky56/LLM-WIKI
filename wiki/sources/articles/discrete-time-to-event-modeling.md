---
summary: Introduction to discrete-time survival analysis: discretization, censoring mechanisms, and life table foundations
tags: [time-to-event, survival-analysis, censoring, life-table, discrete-time, predictive-modeling]
updated: 2026-05-07T16:27:31Z
created: 2026-05-07T16:27:31Z
---

# Discrete Time-To-Event Modeling – Predicting When Something Will Happen

**Source:** [Towards Data Science](https://towardsdatascience.com/discrete-time-to-event-modeling-predicting-when-something-will-happen/) (2026-05-05)
**Author:** [not specified]
**Status:** Part 1 of multi-part series

## Summary

Introduction to discrete time-to-event modeling (survival analysis) — the branch of predictive modeling focused on predicting *when* something will happen, as opposed to the more common *what* or *how much*.

## Key Concepts

### 1. Discretizing Time
- **Continuous treatment** appropriate when: event is inherently continuous, timing measured precisely, time granularity is small relative to horizon
- **Discrete treatment** appropriate when: event is inherently discrete (e.g., missed payment on a due date), precise timing cannot be captured, data aggregated at intervals for practical reasons
- Ties (multiple events at same time) are a problem for continuous models but naturally handled in discrete

### 2. Censoring
- **Right censoring** (most common): event hasn't happened yet, or data collection stopped
- Models ignoring censoring will *underpredict* events — bias toward fewer events
- Standard assumption: censoring is **non-informative** (unrelated to underlying event risk after accounting for features)
- If censoring IS related to risk, must model the censoring mechanism explicitly (competing risk)

### 3. The Life Table
- Cuts time into discrete chunks to handle censoring
- **Observational columns:** units at risk, events, censored
- **Calculation columns:** adjusted at-risk, conditional probability (hazard), survival probability, unconditional probability
- Survival probability = product of conditional survival probabilities across intervals
- Life tables themselves are underfit for prediction but their data structure is foundational for all discrete-time methods

## Relevance

Time-to-event modeling is directly adjacent to time series forecasting but addresses a complementary question. While TimesFM predicts *future values*, survival analysis predicts *event timing*. The two frameworks could be hybridized.
