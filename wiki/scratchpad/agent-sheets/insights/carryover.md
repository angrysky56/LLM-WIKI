---
agent: insights
schema: carryover-v1
generated: 2026-06-06
cycle: 9
---

## CarryoverState

### Established
- **Cycle 9 (June 5, 7:25pm) GAAC-clustered 220 wiki pages into 5 clusters** and identified 3 candidate insights.
- **Only 1 of 3 insights was surfaced** in the wiki page `wiki/synthesis/2026-06-05-insights-batch.md` — the other 2 were dropped due to output truncation.
- **Output ballooned to 73KB** — 4× the typical cycle. Cron storage cap is not the issue; the agent's response itself exceeded the practical synthesis range.
- **Lost 3 rounds of insights total** across June 4-5 (2 on June 4, 1 on June 5).

### Open
- **[Q]** Should the agent write a structured JSON intermediate before the wiki page, so a downstream synthesis step can pick up the dropped insights?
- **[Q]** Are the 2 dropped insights worth recovering, or are they the GAAC artefacts (cluster centroid labels) that aren't real insights?
- **[R]** 73KB output risks rate-limit and response-truncation by the model itself; downstream tooling may also reject on size.
- **[R]** Synthesis step is single-pass — no progressive refinement, so quality degrades with cluster count.

### Heading
- **[Intent]** Truncate output at 20KB max — keep the wiki page, drop the verbose cluster breakdown (or move it to a separate `_raw` file).
- **[Intent]** Surface all N candidate insights in a single wiki page (numbered, with confidence scores), even if 1-2 are weak.
- **[Constraint]** Cap prompt at 3K tokens; 20KB response cap.
