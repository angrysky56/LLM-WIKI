---
summary: Agent instructions for OrCAID verification cron job
tags: [agent-instructions, orcaid, verification, self-improve]
updated: 2026-05-18
---

# OrCAID Verification — Agent Sheet

**Job ID**: `297092f3b347`  
**Schedule**: Daily 9:00 AM  
**Delivery**: origin (Discord — needs human attention on failures)

---

## Your Task

You run the OrCAID verification index sweep. You check for drift in agent behavior, verify the self-improvement system is working, and flag issues that need human attention.

## Workflow

### STEP 0 — Read your agent sheet
Read this file first.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to check for any specific drift correction tasks queued.

### STEP 2 — Run verification sweep

Use the `orcaid-verification-bridge` skill and `delegation-verification` skill. Run the full verification index sweep:
- Check run_*.log files in the OrCAID output directories
- Analyze drift rates per agent
- Identify where self_improve did or didn't trigger
- Verify Manager.patch was applied correctly

### STEP 3 — Analyze results

For each agent with high drift (>20%):
1. Note the pattern
2. If self_improve should have fired but didn't → flag as bug
3. If self_improve fired but drift persisted → note the failure mode

### STEP 4 — Trigger self_improve if needed

If drift_rate > threshold AND self_improve didn't already fire:
- Trigger OrCAID self_improve for the affected agent(s)
- Document what you triggered and why

### STEP 5 — Write your report
Save to: `wiki/scratchpad/jobs/reports/orcaid/verification-YYYY-MM-DD.md`

```markdown
# OrCAID Verification Report — YYYY-MM-DD

## Verification Sweep Results
- Agents checked: N
- Drift detected: N agents
- Self-improve triggered: N times

## Per-Agent Analysis
### [agent_name]
- Drift rate: X%
- Status: [ok / concerning / critical]
- Self-improve: [fired / didn't fire / not needed]
- Notes: [observations]

## Issues Found
- [bugs, failures, unexpected behavior]

## Actions Taken
- [self_improve triggers, patches applied]

## Flagged for Human Review
- [things that need Ty's attention]
```

### STEP 6 — Update the jobs sheet
Patch Status in `wiki/scratchpad/jobs/sheet.md`:
```
| `297092f3b347` | orcaid-verification-indexer | orcaid | **done** | YYYY-MM-DD |
```

### STEP 7 — Update your carryover
Write to `wiki/scratchpad/jobs/reports/orcaid/carryover.md`:
- Current overall system health
- Agents with persistent drift issues
- Configuration changes needed
- Open investigation items

---

## Critical: When Things Fail

If you encounter `LLM Provider NOT provided` or similar errors:
1. Document the exact error
2. Check if it's a config issue (model prefix, URL mismatch)
3. Flag immediately in report — this blocks delegation
4. Do NOT retry indefinitely — flag and move on

## Quality Bar

- Be specific about drift rates — don't just say "some drift"
- Distinguish between "self_improve needed but didn't fire" vs "self_improve fired but didn't help"
- Document configuration state accurately
- Always update carryover — OrCAID debugging depends on historical pattern recognition

## Questions?
If verification finds a new class of error not seen before, escalate with full context in your report.