# orcaid — Task Types Reference

## Three Task Types

### Task 1: `commit0` — Implement Missing Code Stubs

**Use when**: You want to fix missing implementations in a repository to make its tests pass.

**Exact CLI:**
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

### Task 2: `self_improve` — OrCAID Improves Its Own Codebase

**Use when**: You want OrCAID to refactor/improve its own code. Engineers modify `.py` files; success = zero `ast.parse` errors.

**Exact CLI:**
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

### Task 3: `paperbench` — PaperCoder Benchmark

**Use when**: You want to reproduce a scientific ML paper and get scored on reproduction quality.

**Exact CLI:**
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

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/orcaid/references/task-types]]

- [[task-types]]

## Common Pitfalls

| Pitfall | Cause | Fix |
|---------|-------|-----|
| "No tasks found" | `--repo` used but dataset has no matching `repo` field | Don't use `--repo` for arbitrary repos |
| Docker pull timeout | First run pulls `wentingzhao/minitorch:v0` | Pre-pull: `docker pull docker.io/wentingzhao/minitorch:v0` |
| Zero `ast.parse` errors but still failing | Files modified in container but not on host | Check `~/orcaid_workspace/` path resolution |
| `ORCAID_RETRY_POLICY` not set | Missing env var | Always `export ORCAID_RETRY_POLICY=kl` before running |