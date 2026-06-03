# arxiv-agent — 2026-06-03 Episodic Vault

## Run Context
- Date: 2026-06-03 14:25 UTC (cron 0 8 * * *)
- Inbox: empty, no claims needed
- arXiv: 2026-06-02 batch is the new listings (today's submission 20:00 UTC batch not yet posted)
- API issues: 429s, 503s on initial attempts; 60-180s backoff worked
- Categories fetched: cs.AI, cs.CL, cs.LG (18 unique papers from 2026-06-02)

## Phase 2 — Selection
Top 3 by significance + active-thread overlap:

| Rank | arXiv ID | Title | Author | Fit |
|------|----------|-------|--------|-----|
| 1 | 2606.03979 | Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories | Behrouz, Hashemi, Mirrokni | Novel LLM memory paradigm, new direction (self-modification), strong lab (Google) |
| 2 | 2606.03980 | Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill | Chen, Jiang, Cheng | Strong fit with 7+ paper skill thread (SkillOpt, SkillLens, SkillHarm, ReuseRL) — agent skill as RM primitive |
| 3 | 2606.03969 | Quantifying Faithful Faithful Confidence Expression in Large Reasoning Models | Gani, Meskin, Liu, Cohan | Calibration in LRMs, connects to evaluation infrastructure / trustworthiness thread |

### Also-considered
- 2606.03990 (Neuron Populations Divergent Selectivity with Scale) — interpretability but mechanical, less novel
- 2606.03962 (Reward Uncertainty Diverse RL) — diversity, less novel vs prior work
- 2606.03965 (Agentic CoT Steering) — incremental over efficient-reasoning literature
- 2606.03988 (Imaginative Perception Tokens) — narrower
- 2606.03985 (Humanoid-GPT) — robotics, off-thread
- 2606.03892 (Synthesize and Reward) — multi-step tool use, runner-up
- 2606.03954 (VLESA) — embodied safety, runner-up

## Phase 3 — PDFs
- Download all 3 via curl in parallel
- Save to /home/ty/Documents/paper-research/{id}.pdf

## Phase 4 — Subagents
- Three delegate_task calls, one per paper
- Each writes to wiki/sources/papers/{slug}.md and appends to papers-YYYY-MM-DD-researched.md

## Phase 5 — Report
- Final report at wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-06-03-top-papers.md
- Theme: ?? — to be determined after research

## MOP Compression
- Compress this vault to carryover.md at end (~512 tokens)
- Identify cross-paper theme for the cycle
