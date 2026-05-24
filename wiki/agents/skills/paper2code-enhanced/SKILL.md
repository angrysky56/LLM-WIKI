---
name: paper2code-enhanced
description: Paper2Code-Enhanced — multi-agent paper-to-code pipeline (planning → analyzing → coding) using PaperCoder. Generates working implementations from ML papers. ~$0.50–0.70 per run, ~1 hour per run.
type: skill-manual
created: 2026-05-24
updated: 2026-05-24
tags: [paper-to-code, ml, reproduction, papercoder, autonomous-agents]
triggers:
  - "paper to code"
  - "generate from paper"
  - "reproduce paper"
  - "paper2code"
  - "TreeOfThoughts"
  - "Yao et al"
---

# Paper2Code-Enhanced Skill Manual

Paper2Code-Enhanced transforms ML papers into code repositories via PaperCoder — a three-stage multi-agent pipeline (planning, analysis, coding).

**Repo**: `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/`
**Entry**: `codes/pipeline.py` (Python API)

---

## When to Use

- Paper has an official implementation you want to reproduce or study
- You want a working scaffold from a paper without reading it line-by-line
- Paired with OrCAID commit0 for validation+fixup
- **Cost**: ~$0.50–0.70 per full run (MiniMax M2.7)
- **Runtime**: ~1 hour per full run

**Do NOT use for**:
- Simple papers with obvious implementations (overkill)
- Real-time needs (1 hour per run)
- Papers without clear algorithmic specs

---

## Python API (Recommended)

```python
import sys
sys.path.insert(0, '/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/codes')

from pipeline import run_pipeline, PipelineConfig

config = PipelineConfig(
    paper_name="TreeOfThoughts",
    pdf_json_path="/path/to/arxiv_2605.15612_cleaned.json",
    output_dir="/home/ty/Repositories/ai_workspace/paper2code-projects/TreeOfThoughts/",
    output_repo_dir="/home/ty/Repositories/ai_workspace/paper2code-projects/TreeOfThoughts_repo/",
)
result = run_pipeline(config)
print(result.status, result.output_repo_dir)
```

**Requires `PYTHONPATH`** — always prepend the codes directory:
```python
import sys
sys.path.insert(0, '/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/codes')
```

---

## Three Stages

| Stage | Script | What it does |
|---|---|---|
| Planning | `codes/1_planning.py` | Decomposes paper into modules, generates `planning_artifacts/` |
| Analyzing | `codes/2_analyzing.py` | Extracts algorithm details, produces `analyzing_artifacts/` |
| Coding | `codes/3_coding.py` | Generates the full repository in `<PaperName>_repo/` |

Each stage writes results to SQLite DB (`codes/db.py`) and artifacts to `output_dir/`.

---

## Input Preparation

### From arXiv JSON (cleaned format)

```bash
cd /home/ty/Repositories/ai_workspace/Paper2Code-Enhanced

uv run python codes/0_pdf_process.py \
    --input_json_path examples/Transformer.json \
    --output_json_path examples/Transformer_cleaned.json \
    --mode auto
```

### From PDF directly

```bash
uv run python codes/0_pdf_process.py \
    --input_json_path path/to/paper.pdf \
    --output_json_path output_cleaned.json \
    --mode auto
```

Modes: `auto` (default, VLM if key available, else local), `vlm` (Vision-Language Model), `local` (pypdf, offline), `olmocr` (olmOCR pipeline)

### From LaTeX source

```bash
cd scripts
uv run bash run_latex.sh
```

---

## Output Structure

```
outputs/
├── <PaperName>/           # Artifacts (planning, analyzing, coding artifacts)
│   ├── planning_artifacts/
│   ├── analyzing_artifacts/
│   ├── coding_artifacts/
│   └── accumulated_cost.json
└── <PaperName>_repo/      # Generated code repository (THE OUTPUT YOU WANT)
    ├── config.yaml
    ├── main.py
    ├── utils.py
    ├── tasks/
    └── tot/               # (for TreeOfThoughts paper)
```

---

## Configuration (.env)

Set in `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/.env`:

```env
LLM_API_KEY=your_key_here
LLM_BASE_URL=https://api.minimax.io/v1
LLM_MODEL=MiniMax-M2.7
```

**Base URL must be `https://api.minimax.io/v1`** (OpenAI-compatible endpoint). The `/anthropic/v1/messages` endpoint only serves Claude models and returns 404 for MiniMax.

MiniMax M2.7 recommended — supports thinking/reasoning blocks natively via Anthropic SDK.

---

## CLI (Broken — Use Python API)

The CLI scripts (`scripts/run.sh`, `codes/1_planning.py`, etc.) do `from db import ...` but don't set `PYTHONPATH`, causing import errors.

**Always use the Python API** for programmatic runs.

If calling stage scripts directly, prepend `PYTHONPATH`:
```bash
PYTHONPATH=/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/codes uv run python codes/1_planning.py ...
```

---

## Common Issues

### `db` module import error

CLI scripts do `from db import ...` but don't set `PYTHONPATH`. Use Python API instead.

### `run.sh` empty `--gpt_version`

If `LLM_MODEL` env var is empty, `GPT_VERSION=""` gets passed as `--gpt_version ""` which scripts interpret as a positional argument. Ensure `.env` has `LLM_MODEL=MiniMax-M2.7` set.

### Missing `_cleaned.json` suffix

Pipeline expects `<paper_name>_cleaned.json` (with the `_cleaned` suffix). Running `0_pdf_process.py` produces this.

---

## OrCAID Integration

Paper2Code-Enhanced generates a repository; OrCAID commit0 validates and fixes it:

1. **Paper2Code generates** → `<PaperName>_repo/` with implementation
2. **OrCAID commit0 validates** → runs pytest, parses JSON report, applies patches

```bash
cd /home/ty/Repositories/ai_workspace/OrCAID && \
uv run python -m orcaid.cli \
    --task=commit0 \
    --model=minimax/MiniMax-M2.7 \
    --multi_agent=false \
    --max_iterations=5 \
    --patch_target /home/ty/Repositories/ai_workspace/paper2code-projects/TreeOfThoughts_repo/
```

---

## Key Files

| File | Purpose |
|---|---|
| `codes/pipeline.py` | Python API entry (`run_pipeline`, `PipelineConfig`, `PipelineResult`) |
| `codes/1_planning.py` | Planning stage |
| `codes/2_analyzing.py` | Analyzing stage |
| `codes/3_coding.py` | Coding stage |
| `codes/0_pdf_process.py` | PDF/JSON ingestion + cleaning |
| `codes/eval.py` | Evaluation script |
| `codes/db.py` | SQLite persistence (sqlmodel) |
| `examples/Transformer_cleaned.json` | Example input |

---

## Constraints

- **Always use Python API** for programmatic runs (CLI broken due to db module path)
- **Prepend `PYTHONPATH`** when calling stage scripts directly
- `LLM_MODEL` must be set in `.env` before running
- ~1 hour per full run — don't use for trivial papers
- Cost ~$0.50–0.70 per run with MiniMax M2.7