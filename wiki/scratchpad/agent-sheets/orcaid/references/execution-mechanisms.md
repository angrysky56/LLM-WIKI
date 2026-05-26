# orcaid — Execution Mechanisms

## Mechanism 1 — ACTIVE: `orcaid.cli` (produces new outcomes)

Direct inference run. Manager delegates to Engineer subagents in parallel git worktrees.

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
export ORCAID_RETRY_POLICY=kl
uv run python -m orcaid.cli --task=<task> --model=minimax/MiniMax-M2.7 [options]
```

**Produces**: New code, test results, evaluation scores.

---

## Mechanism 2 — PASSIVE: `run_evolution.py --domain orcaid` (computes metrics from memory)

Reads `~/.hermes/orchestrator-memory/` and computes composite scores. **Does NOT produce new outcomes.**

```bash
cd /home/ty/Repositories/ai_workspace/meta-harness
uv run python run_evolution.py --domain orcaid [--iterations N]
```

**Reads from**: `~/.hermes/orchestrator-memory/`
**Computes**: task_completion_rate, delegation_verification_pass_ratio, drift_rate, skill_file_creation_rate, escalation_rate.

---

## Mechanism 3 — PASSIVE: `run_evolution.py --domain paper2code` (evaluates Paper2Code outputs)

Reads `Paper2Code/outputs/` and evaluates generated code quality. **Does NOT produce new outcomes.**

```bash
cd /home/ty/Repositories/ai_workspace/meta-harness
uv run python run_evolution.py --domain paper2code [--iterations N]
```

**Reads from**: `Paper2Code/outputs/`

---

## Key Distinction

| Mechanism | New Outcomes? | Memory Side Effects? |
|-----------|---------------|----------------------|
| ACTIVE (orcaid.cli) | Yes | Yes — writes to orchestrator-memory |
| PASSIVE (run_evolution orcaid) | No | No — reads only |
| PASSIVE (run_evolution paper2code) | No | No — reads only |