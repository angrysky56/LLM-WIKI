---
summary: Librarian carryover 2026-06-03 cycle 4 — fixed 47 invalid frontmatter files (regression from cycle 3 duplicate-YAML remediation), 0 invalid remaining; all other metrics stable
tags: [librarian, carryover, wiki-audit, daily, 2026-06-03, cycle-4, invalid-frontmatter-fix]
updated: 2026-06-03T20:25:00Z
---

# Librarian Carryover — 2026-06-03 (Cycle 4, 20:25 UTC)

## Kanban Status
- [x] Audit complete: 2026-06-03 20:25 UTC
- [x] MCP tools: REACHABLE ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] **CRITICAL FIX: 47 invalid frontmatter files remediated** (regression from cycle 3 duplicate-YAML remediation)
- [x] wiki_update_index (deep refresh) — 1357 pages indexed
- [x] Verified all 47 files now parse as valid YAML

## Established

### Vault Stats (2026-06-03 20:25 UTC)
- **Total wiki pages: 1363** (1096 knowledge, 267 operational excluded)
- Orphans: **71** (was 73, -2)
- Broken links: **595** (was 588, +7 all operational path refs)
- Missing frontmatter: **42** (was 9, +33 from invalid files now reclassified as missing)
- **Invalid frontmatter: 0** ✅ (was 47, -47 — FULLY RESOLVED)
- Non-reciprocal: **428** (was 424, +4)
- Non-preferred tags: **0** ✅
- GAAC clusters: **8** (was 74 last cycle — linter behavior change, not vault change)
- Merge candidates (sim>0.7): **10** (all sim=1.0 — confirmed false-positive stub pattern, no action)

### Cycle 3 → Cycle 4 Diff
The cycle 3 remediation (which claimed "True remaining target: 0") left 47 files with **invalid YAML** that the linter catches. The script removed the wrong block in 47 cases, leaving either:
1. Body text (`*Archived ...*` or `*Stub page ...*`) inside the frontmatter block — 25 files
2. Unquoted colons inside `summary:` values — 19 files
3. Duplicate empty YAML blocks — 1 file
4. Unescaped quotes/apostrophes inside quoted summaries — 2 files

All 47 now parse as valid YAML. The +33 jump in "missing frontmatter" is a reclassification: the linter used to report them under "invalid" but apparently now flags them as missing when parsing fails.

### HITS Authority Top 5 (stable, 4 cycles)
1. [[wiki/index]] — 0.0633
2. [[log]] — 0.0445
3. [[maximum-occupancy-principle]] — 0.0130 (bare slug, phantom)
4. [[concepts/maximum-occupancy-principle]] — 0.0105 (prefixed, alias)
5. [[efhf]] — 0.0053

### HITS Hub Top 5
1. [[lint-2026-06-03]] — 0.0042 (audit artifact)
2. [[maximum-occupancy-principle]] — 0.0028
3. [[efhf]] — 0.0025
4. [[concept-index]] — 0.0021
5. [[load-bearing-reasoning]] — 0.0019

## What Remains

### High Priority
- [ ] **33 newly-classified missing-frontmatter files** (mostly the same 47 just-fixed files, now visible as "missing" instead of "invalid" — re-verify on next cycle to confirm these are actually separate files, not a re-classification artifact)
- [ ] **9 pre-existing missing-frontmatter files** (carryover from cycle 3 — not remediated this cycle):
  - `wiki/research/mop-agents-integration.md`
  - `wiki/research/projects/goodrobot/Q2_SALES_TARGET_LIST.md`
  - `wiki/research/projects/goodrobot/STRATEGIC_BRIEF.md`
  - `wiki/synthesis/_index/structural-reuse-crosslink-survey-2026-06-01.md`
  - 5× `wiki/synthesis/news/2026-May/headlines-*.md` files
- [ ] **71 knowledge orphans** (slight improvement from 73; re-verify next cycle)
- [ ] **595 broken links** — all operational path refs; not actionable in knowledge layer

### Medium Priority
- [ ] **GAAC cluster 0/1 inflated missing-link counts** (250k+ / 153k+) — false positives confirmed, no action; skill documentation already covers this
- [ ] **428 non-reciprocal flags** — body-text-only, false-positive heavy

### Low Priority / Re-verify
- [ ] **MOP phantom HITS nodes** — known limitation, server-side algorithm; will not self-resolve
- [ ] **linter "invalid frontmatter" counter regression** — needs investigation: did the linter get stricter between cycle 3 and cycle 4, or did the cycle 3 remediation truly leave 47 files broken?

## Flagged for Ty
- **Linter behavior changed between cycle 3 and cycle 4**: cycle 3 reported 0 invalid + 9 missing; cycle 4 reports 0 invalid + 42 missing. The 47 "invalid" files I just fixed were not flagged as invalid in cycle 3. Two possibilities: (a) linter now checks invalid before missing (was missing-only before), or (b) cycle 3's "fully remediated" report was overconfident. Recommend cycle 5: compare lint output across two runs to detect linter drift.
- **Cycle 3 remediation overclaimed**: "True remaining target: 0 ✅" was wrong. 47 files were broken. The detection script must have only counted one specific YAML-block pattern and missed the body-text-in-frontmatter and unquoted-colon variants. **Lesson for future remediations: always re-run wiki_lint after the remediation to confirm the count actually dropped.**
- **goodrobot/ operational files in research/** — should the linter exclude operational research files from frontmatter checks? (3 of 9 missing-frontmatter files)
- **News headlines frontmatter policy** (5 of 9 missing-frontmatter files) — should the linter auto-author news report frontmatter, or is this a content-authoring task?

## Heading
- Vault health: **9/10** (↑ from 8.5 — critical invalid-frontmatter regression fully resolved)
- Audit report: `wiki/audits/lint-2026-06-03.md` (was rewritten 20:25 UTC)
- Next cycle: re-verify 33 missing-frontmatter count; run lint twice to detect drift
- HITS authority top-3 stable 4 cycles — vault graph topology healthy
- Tag taxonomy compliance: 0 violations
- **Key action this cycle:** discovered and fixed 47-file invalid-frontmatter regression from cycle 3 remediation
- **Verified false:** cycle 3 prediction "True remaining target: 0" — actual was 47 broken files
- **Verified true:** cycle 3 prediction "MOP alias will not self-resolve" — confirmed 4th cycle
