# AGEM Orchestration Strategies

## Strategy 1: Deep Analysis (single topic)

```
1. run_agem_cycle(prompt)           → build graph, get metrics
2. get_soc_metrics                  → check VNE/EE/CDP divergence
3. detect_gaps                      → find structural holes
4. generate_catalyst_questions      → get bridging questions
5. run_agem_cycle(catalyst_q)       → close gaps with targeted reasoning
6. Repeat 2-5 until H¹=0 and gaps=0
```

## Strategy 2: Multi-Perspective Analysis (contested topic)

```
1. run_agem_cycle(perspective_A)
2. run_agem_cycle(perspective_B)    → introduces competing concepts
3. get_cohomology                   → H¹ > 0 means genuine incompatibility detected
4. detect_gaps                      → find where perspectives diverge
5. generate_catalyst_questions      → bridge the gap
6. Use advanced-reasoning to reflect on whether the tension is resolvable
```

## Strategy 3: Verified Reasoning (high-stakes claims)

```
1. run_agem_cycle(topic)
2. For each key claim in the response:
   a. conscience-servitor:triage(claim)           → check ethical risk
   b. hipai-montague:add_belief(claim)            → add to world model
   c. hipai-montague:evaluate_hypothesis(claim)   → test against knowledge
   d. verifier-graph:propose_thought(claim)       → add to provenance chain
3. sheaf-consistency-enforcer:register_agent_state for each tool used
4. sheaf-consistency-enforcer:get_closure_status   → check cross-tool consistency
```

## Strategy 4: Value-Anchored Analysis (alignment-sensitive)

```
1. conscience-servitor:triage(topic)              → assess ethical risk
2. If high risk: conscience-servitor:evaluate(claims)
3. run_agem_cycle(topic)
4. hipai-montague:add_belief("ethical constraint: X")  → anchor values
5. run_agem_cycle(challenge_to_values)
6. hipai-montague:evaluate_hypothesis("constraint X is preserved")
7. sheaf-consistency-enforcer:get_closure_status  → detect value drift
```
