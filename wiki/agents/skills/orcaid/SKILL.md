---
type: skill-manual
name: orcaid
description: OrCAID multi-agent execution engine — correct entry (orcaid.cli), local path support, auto-build Docker, three task types (commit0/self_improve/paperbench)
triggers:
  - "run OrCAID"
  - "commit0"
  - "self_improve"
  - "paperbench"
  - "add OrCAID task"
tags: [orcaid, multi-agent, delegation]
updated: 2026-05-24
---

# OrCAID Skill Manual

> **Cron `297092f3b347` is PAUSED.** This skill is manual-only — run on-demand via CLI.

**Repo:** `/home/ty/Repositories/ai_workspace/OrCAID/`

## Correct Entry Point

**Always use `uv run python -m orcaid.cli`** — NOT `run_infer.py`, NOT bare `python`.

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID
uv run python -m orcaid.cli [flags...]
```

`.env` file at OrCAID root sets `LLM_MODEL` and `LLM_BASE_URL`.

## Three Task Types

### commit0 — Implement stubs, run pytest (primary task)

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID

uv run python -m orcaid.cli \
    --task=commit0 \
    --repo /home/ty/Repositories/ai_workspace/Paper2Code-Enhanced \
    --model minimax/MiniMax-M2.7 \
    --multi_agent=false \
    --max_iterations=5
```

### self_improve — OrCAID self-improvement (ast.parse only, weaker)

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID

uv run python -m orcaid.cli \
    --task=self_improve \
    --repo_path /home/ty/Repositories/ai_workspace/OrCAID \
    --task_description "Add memory-of-failures pattern to Manager._verify_and_return" \
    --model minimax/MiniMax-M2.7 \
    --multi_agent=false \
    --max_iterations=3
```

### paperbench — Reproduce ML papers (LLM judge evaluated)

```bash
uv run python -m orcaid.cli \
    --task=paperbench \
    --paper_id 2605.18703 \
    --model minimax/MiniMax-M2.7 \
    --multi_agent=false \
    --max_iterations=5
```

## Three-System Pipeline

```
arXiv cron (arxiv agent) → saves papers to arxiv-papers/
    ↓
Paper2Code-Enhanced (your CLI) → generates code repo
    ↓
OrCAID commit0 → validates + fixes generated repo
```

This pipeline runs on-demand, not on a cron schedule. Paper2Code generates; commit0 validates.

## Local Path Support

`--repo` accepts **absolute local paths** (starting with `/`). When given a local path:
- The local directory is **copied into the container** after it starts (not git clone)
- DockerDevWorkspace auto-builds an image from a **language-appropriate base image** (Python → `python:3.12-slim`, Node → `node:20-slim`, etc.)
- No pre-built benchmark Docker image needed
- No git authentication required

```bash
# Local path — container builds from python:3.12-slim automatically
uv run python -m orcaid.cli \
    --task=commit0 \
    --repo /home/ty/Repositories/ai_workspace/Paper2Code-Enhanced \
    --model minimax/MiniMax-M2.7
```

## Docker Image Requirement

**Docker must be running.** OrCAID uses `openhands.workspace.DockerDevWorkspace`:

- `openhands.workspace.DockerDevWorkspace` builds images **from base_image** (not from the target repo)
- `base_image` is set by `task_module.get_workspace_config()["base_image"]`
- For commit0 on Python repos: `python:3.12-slim`
- OpenHands' `build()` function builds from the base image
- Local repo is copied into the running container (not used as build context)

> Use `--docker_image=docker.io/wentingzhao/minitorch:v0` only when you specifically need the minitorch image.

## Key Parameters

| Flag | Task | Purpose |
|---|---|---|
| `--task` | all | `commit0`, `self_improve`, `paperbench` |
| `--repo` | commit0 | GitHub URL (`owner/repo`) or local absolute path |
| `--repo_path` | self_improve | Local absolute path to the repo |
| `--model` | all | LiteLLM model (`minimax/MiniMax-M2.7`) |
| `--multi_agent` | all | `true` (4 engineers) or `false` (single agent) |
| `--max_iterations` | all | Max Manager LLM turns |
| `--max_rounds_chat` | all | Subagent chat rounds (default: 2) |
| `--paper_id` | paperbench | arXiv paper ID |

## Key Paths

| Path | Role |
|---|---|
| `/home/ty/Repositories/ai_workspace/OrCAID/` | OrCAID repo root |
| `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/` | Target repo for commit0 |
| `~/.hermes/orchestrator-memory/verified/` | Verified SubAgentResult outcomes |
| `~/.hermes/orchestrator-memory/drift_logs/` | Drift/failure records |
| `~/.hermes/orchestrator-memory/escalations/` | Human review items |
| `~/.hermes/orcaid-bridge/` | Bridge storage |

## Key Files

| File | Role |
|---|---|
| `orcaid/cli.py` | Entry point — DockerDevWorkspace setup + workflow |
| `orcaid/core/utils.py` | `build_task_module()` (line 1309), `build_llm_kwargs()` |
| `orcaid/core/manager.py` | Manager + `_verify_and_return()` (lines 678, 710, 731) |
| `orcaid/core/subagent.py` | SubAgentRunner — git worktree per engineer |
| `orcaid/tasks/commit0.py` | commit0: pytest, stub implementations |
| `orcaid/tasks/self_improve.py` | self_improve: ast.parse syntax check |
| `orcaid/tasks/paperbench.py` | paperbench: LLM judge evaluation |
| `orcaid/tasks/paper2code.py` | PaperCoder task (stub, wired but not implemented) |
| `orcaid_verification_bridge.py` | Self-healing: verify_subagent_completion() |

## build_task_module Tasks (utils.py line 1309)

| Task | Kwarg mapping |
|---|---|
| `commit0` | `repo` → `repo_name`, also `base_branch`, `docker_image_prefix`, `docker_image`, `dataset_path` |
| `self_improve` | `repo_path`, `task_description` |
| `paperbench` | `paper_id`, `docker_image`, `paperbench_dir`, ... |
| `paper2code` | `repo_path`, `paper_url`, `output_dir` (wired but stub) |

## MiniMax Configuration

```env
# In OrCAID .env
LLM_MODEL=minimax/MiniMax-M2.7
LLM_BASE_URL=https://api.minimax.io/v1
LLM_API_KEY=<key>
```

**Must be `/v1`**, not `/anthropic/v1/messages`.

## Architecture

```
User → orcaid.cli → build_task_module() → TaskModule
    ↓
DockerDevWorkspace (base_image=python:3.12-slim, target=source-minimal)
    ↓ (OpenHands builds image + starts container)
container: copy local repo → run agent (Manager + Engineers)
    ↓
Manager: scan_and_analyze() → delegate_tasks() → run_subagents_parallel()
    ↓
collect_and_merge() → _verify_and_return()
    → bridge.verify_subagent_completion()
        → PASS: orchestrator-memory/verified/
        → FAIL: orchestrator-memory/drift_logs/ + correction_context
    ↓
final_review_all() → outputs/
```

Key line references:
- `orcaid/core/manager.py` lines 678, 710, 731: `_verify_and_return()`
- `orcaid/core/utils.py` line 1309: `build_task_module()`

## Common Issues

| Symptom | Cause | Fix |
|---|---|---|
| Exit 1, no output | Missing `.env` or Docker not running | Check LLM_BASE_URL, `docker ps` |
| "Unknown model provider" | Wrong LLM_BASE_URL | Must be `https://api.minimax.io/v1` |
| Local path not copied | Path must be absolute (start with `/`) | Use `/home/ty/...` not `~/...` |
| No container starts | Docker not running | `docker ps` to verify |
| `paper2code` task fails | `evaluate()` is still a stub | Implement evaluation or use commit0 on the generated repo instead |

## Add a New Task

1. `tasks/my_task.py`: `MyTaskConfig` dataclass + `MyTask(TaskModule)` implementing:
   - `get_docker_image()`, `get_work_dir()`, `get_workspace_config()`
   - `load_task_data()`, `setup_workspace()`, `evaluate()`
2. `tasks/__init__.py`: add `from .my_task import MyTaskConfig, MyTask`
3. `orcaid/core/utils.py` `build_task_module()`: add `elif task == "my_task": return MyTask(MyTaskConfig(**init))`