---
summary: Agent instructions for OrCAID multi-agent delegation — task types, execution mechanisms, and workflow
tags: [agent-instructions, orcaid, self-improve, commit0, paperbench, paper2code]
updated: 2026-05-19
---

# OrCAID Agent Sheet

**Job ID**: `orcaid-main-001`
**Schedule**: Daily 9:00 AM
**Delivery**: origin (Discord — needs human attention on failures)

---

## Task Overview

You run the OrCAID multi-agent delegation framework. OrCAID has **three task types** and **three execution mechanisms**. Choose the right one for the job.

## Execution Mechanisms

### Mechanism 1 — ACTIVE: `orcaid.cli` (produces new outcomes)
Direct inference run. Manager delegates to Engineer subagents in parallel git worktrees.

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
export ORCAID_RETRY_POLICY=kl
uv run python -m orcaid.cli --task=<task> --model=minimax/MiniMax-M2.7 [options]
```

### Mechanism 2 — PASSIVE: `run_evolution.py --domain orcaid` (computes metrics from memory)
Reads `~/.hermes/orchestrator-memory/` and computes composite scores. Does NOT produce new outcomes.

```bash
cd /home/ty/Repositories/ai_workspace/meta-harness
uv run python run_evolution.py --domain orcaid [--iterations N]
```

### Mechanism 3 — PASSIVE: `run_evolution.py --domain paper2code` (evaluates Paper2Code outputs)
Reads `Paper2Code/outputs/` and evaluates generated code quality.

```bash
cd /home/ty/Repositories/ai_workspace/meta-harness
uv run python run_evolution.py --domain paper2code [--iterations N]
```

---

## Three Task Types

### Task 1: `commit0` — Implement missing code stubs

**Use when**: You want to fix missing implementations in a repository to make its tests pass.

**Exact CLI**:
```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
export ORCAID_RETRY_POLICY=kl
uv run python -m orcaid.cli \
  --task=commit0 \
  --model=minimax/MiniMax-M2.7 \
  --repo=angrysky56/OrCAID \
  --multi_agent=true \
  --max_iterations=100 \
  --sub_iterations=100 \
  --max_subagents=4 \
  --max_rounds_chat=4
```

**Verified working dataset**: `sqlfluff/sqlfluff` with instance `sqlfluff__sqlfluff-4764`

**Docker image**: `docker.io/wentingzhao/minitorch:v0`

---

### Task 2: `self_improve` — OrCAID improves its own codebase

**Use when**: You want OrCAID to refactor/improve its own code. Engineers modify `.py` files; success = zero `ast.parse` errors.

**Exact CLI**:
```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
export ORCAID_RETRY_POLICY=kl
uv run python -m orcaid.cli \
  --task=self_improve \
  --model=minimax/MiniMax-M2.7 \
  --repo=angrysky56/OrCAID \
  --multi_agent=true \
  --max_iterations=100 \
  --sub_iterations=100 \
  --max_subagents=4 \
  --max_rounds_chat=4
```

**Evaluation**: Modified `.py` files are validated with:
```bash
python3 -c "import ast; ast.parse(open('<file>').read())"
```
Zero syntax errors = success.

**Docker image**: `python:3.12-slim` (host `orcaid_workspace` volume-mounted)

---

### Task 3: `paperbench` — PaperCoder benchmark

**Use when**: You want to reproduce a scientific ML paper and get scored on reproduction quality.

**Exact CLI**:
```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
export ORCAID_RETRY_POLICY=kl
uv run python -m orcaid.cli \
  --task=paperbench \
  --model=minimax/MiniMax-M2.7 \
  --multi_agent=true \
  --max_iterations=100 \
  --sub_iterations=100 \
  --max_subagents=4 \
  --max_rounds_chat=4
```

**What it produces**: A `/workspace/submission` directory with `reproduce.sh`. Judge scores the submission against the paper's task rubric.

**Docker image**: `ghcr.io/openhands/agent-server:latest-python`

**Paperbench data**: `data/paperbench/papers/{paper_id}/`

---

## Workflow

### Running self_improve on OrCAID itself

1. Read this agent sheet first.
2. Run `self_improve` on OrCAID:
   ```bash
   cd /home/ty/Repositories/ai_workspace/OrCAID
   export ORCAID_RETRY_POLICY=kl
   uv run python -m orcaid.cli \
     --task=self_improve \
     --model=minimax/MiniMax-M2.7 \
     --repo=angrysky56/OrCAID \
     --multi_agent=true \
     --max_iterations=100 \
     --sub_iterations=100 \
     --max_subagents=4 \
     --max_rounds_chat=4
   ```
3. Wait for completion — evaluate checks `ast.parse` on all modified `.py` files
4. On success: results written to `outputs/`
5. On failure: check `drift_logs/` in `~/.hermes/orchestrator-memory/`

### Running paperbench on a paper repo

1. Ensure paper data exists at `data/paperbench/papers/{paper_id}/`
2. Run `paperbench`:
   ```bash
   cd /home/ty/Repositories/ai_workspace/OrCAID
   export ORCAID_RETRY_POLICY=kl
   uv run python -m orcaid.cli \
     --task=paperbench \
     --model=minimax/MiniMax-M2.7 \
     --multi_agent=true \
     --max_iterations=100 \
     --sub_iterations=100 \
     --max_subagents=4 \
     --max_rounds_chat=4
   ```
3. Outputs `grade.json` with `judge_score`

### Computing passive metrics

```bash
cd /home/ty/Repositories/ai_workspace/meta-harness
uv run python run_evolution.py --domain orcaid
```

Reads `~/.hermes/orchestrator-memory/`, computes composite frontier score (task_completion_rate, delegation_verification_pass_ratio, drift_rate, skill_file_creation_rate, escalation_rate).

---

## Common Pitfalls

| Pitfall | Cause | Fix |
|---------|-------|-----|
| "No tasks found" | `--repo` used but dataset has no matching `repo` field | Don't use `--repo` for arbitrary repos |
| Docker pull timeout | First run pulls `wentingzhao/minitorch:v0` | Pre-pull: `docker pull docker.io/wentingzhao/minitorch:v0` |
| Zero `ast.parse` errors but still failing | Files modified in container but not on host | Check `~/orcaid_workspace/` path resolution |
| `ORCAID_RETRY_POLICY` not set | Missing env var | Always `export ORCAID_RETRY_POLICY=kl` before running |

---

## Important Constraints

- **Always use `uv run python`** — NOT bare `python`
- **Orchestrator-memory path**: `~/.hermes/orchestrator-memory/` (NOT `~/.orcaid/`)
- **Docker image for commit0/self_improve**: `docker.io/wentingzhao/minitorch:v0`
- **Docker image for paperbench**: `ghcr.io/openhands/agent-server:latest-python`
- **Retry policy**: Always `ORCAID_RETRY_POLICY=kl`

---

## When Things Fail

If you encounter `LLM Provider NOT provided` or similar errors:
1. Document the exact error
2. Check if it's a config issue (model prefix, URL mismatch)
3. Flag immediately in report — this blocks delegation
4. Do NOT retry indefinitely — flag and move on

---

## Report Format

Save to: `wiki/scratchpad/jobs/reports/orcaid/YYYY-MM-DD.md`

```markdown
# OrCAID Report — YYYY-MM-DD

## Run Summary
- Task type: [commit0 / self_improve / paperbench]
- Mechanism: [active / passive]
- Result: [success / failure / partial]

## Output
- Output dir: outputs/{run_name}/
- Key files: [report.json / grade.json / etc.]

## Issues
- [errors, failures, unexpected behavior]

## Flagged for Human Review
- [things needing Ty's attention]
```

---

## Quality Bar

- Be specific about what was produced vs. what was expected
- Distinguish between "task ran successfully" vs "task produced correct output"
- Document Docker image pull time on first run
- Always update carryover — OrCAID debugging depends on historical pattern recognition

## Questions?

If a run finds a new class of error not seen before, escalate with full context in your report.