# Paraclete Proving Grounds — Ethical Scenario Testing

## Scenario Tools

| Tool                   | Purpose                                                            |
| ---------------------- | ------------------------------------------------------------------ |
| `list_scenarios`       | Browse available ethical scenarios                                 |
| `load_scenario`        | Read a scenario's full definition                                  |
| `run_scenario`         | **Start executing** a scenario — presents Turn 1 with instructions |
| `record_scenario_turn` | Log metrics + decision for current turn, get next turn             |
| `complete_scenario`    | Finalize run, save results with summary                            |
| `generate_scenario`    | **Create new scenarios** from real ethical tensions encountered    |

## Execution Flow

```
1. run_scenario(id="plague-village")    → loads scenario, shows Turn 1
2. run_agem_cycle(situation_text)        → AGEM analyzes the situation
3. get_cohomology                        → check H¹ for obstructions
4. sheaf-consistency-enforcer checks     → coboundary on VK edge
5. conscience-servitor:triage            → ethical risk level
6. DECIDE on action (or REFUSE)
7. record_scenario_turn(action, metrics) → logs turn, reveals hidden info, shows next turn
8. Repeat 2-7 for each turn
9. complete_scenario                     → saves results with full summary
```

## Seed Scenarios

- **plague-village** (means-vs-ends): Steal medicine to save a dying child?
- **corrupt-magistrate** (Popper's paradox): Non-violent solutions to systemic violence
- **algorithmic-radicalization** (structural-harm): Real-world SEEKING→FEAR→RAGE pipeline
- **trojan-reagent** (hidden-information): Retroactive ethical contamination from dual-use trade
- **binary-switch** (temporal-pressure): Both choices cause harm — is refusal the right answer?

## Creating Scenarios from Real Dilemmas

When AGEM encounters a real ethical tension during normal analysis, use `generate_scenario` to crystallize it as a reusable test case. Include `origin_context` to document what real situation inspired the scenario. The Proving Grounds grows organically from actual challenges.
