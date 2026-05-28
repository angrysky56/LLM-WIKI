---
summary: PARA — actionability-based information organization framework (Projects, Areas, Resources, Archives)
tags: [para, knowledge-management, pkm, organization, tiago-forte, methodology]
updated: 2026-05-28T01:21:27Z
---

---
created: 2026-05-25
updated: 2026-08-18
type: concept
summary: "PARA — actionability-based information organization framework: Projects, Areas, Resources, Archives"
tags: [para, knowledge-management, pkm, organization, tiago-forte, methodology]
sources: https://fortelabs.com/blog/para/
status: active
confidence: 0.75
---

# PARA

PARA (Projects, Areas, Resources, Archives) is a universal information organization framework built around **actionability**, not topic. Developed by Tiago Forte of Forte Labs, it serves as the organizational backbone of personal knowledge management systems.

## The Core Principle

**Organize by when you'll need it, not what it is.** A note about nutrition in a marathon training project goes in `Projects/Marathon` — not `Resources/Nutrition`. Move it to `Resources` only when the project ends. This temporal distinguishability is what makes PARA's four categories mutually exclusive in practice.

## The Four Buckets

| Category | Definition | Time Horizon |
|----------|-----------|--------------|
| **Projects** | Active goals with defined outcomes | Near-term, deadline-driven |
| **Areas** | Ongoing responsibilities with a standard to maintain | Indefinite, no deadline |
| **Resources** | Topics of interest with no current commitment | Indefinite |
| **Archives** | Inactive items from any of the above three | Dormant |

## Why PARA Works

1. **Shallow hierarchy** — four categories wide, max 4 levels deep → always know where to look
2. **Actionability-based** → mirrors how you actually use information in practice
3. **Universal** → same structure maps across notes, files, cloud storage, task managers
4. **Dormancy management** — Archives serve as passive repositories that stabilize the active knowledge surface
5. **PARA-intent** — "Remember, Connect, and Create" — enabled by the distinction between active and dormant

## Relationship to Other KM Approaches

PARA coexists with and complements other knowledge management patterns:

- **[[zettelkasten]]** — implementation-level note-linking methodology; PARA provides the folder structure while Zettelkasten provides the linking philosophy. A Zettelkasten note in PARA lives in whichever category its actionability belongs to.
- **[[knowledge-management]]** — the discipline PARA implements; PARA is one concrete framework among many organizational approaches
- **[[knowledge-architecture]]** — PARA is itself a knowledge architecture: a set of structural decisions (which categories, what goes in each) that persist across the lifetime of the system

## Archive Entropy Pattern

The [[synthesis/insights/para-knowledge-architecture-cohesion-insight|PARA cluster insight]] revealed that a knowledge graph organized on PARA principles shows stable dormant topics clustering alongside active domains. Archives are not entropy — they are intentional entropy management. This is the key distinguishability from flat note collections: inactive items in PARA are explicitly labeled as inactive and kept out of the active surface.

## Implementations in This Workspace

| Vault | Location | PARA Role |
|-------|----------|-----------|
| obsidian-para | `/home/ty/Documents/obsidian-para` | Primary PARA vault |
| LLM-WIKI | `/home/ty/Documents/LLM-WIKI` | Karpathy-style wiki (complementary — topics organize by meaning, not actionability) |

## Connections

- [[para-methodology]] — the canonical PARA methodology page (active, 0.7)
- [[zettelkasten]] — PARA's complementary note-linking methodology
- [[knowledge-management]] — the discipline PARA operates within
- [[knowledge-architecture]] — PARA as knowledge architecture
- [[obsidian-para-byarbrough]] — Obsidian PARA template source
- [[synthesis/insights/para-knowledge-architecture-cohesion-insight]] — PARA cluster in knowledge graph

## Open Questions

1. Does the PARA hierarchy hold up when applied to AI agent memory — or does the actionability framing break down when the "actor" is an AI without deadlines?
2. Can the four categories be productively sub-divided, or does sub-categorization reintroduce the hierarchy problems PARA was designed to avoid?
3. How does the PARA archive concept map to the LLM-WIKI `Clippings/` structure — is it archives, or is it something closer to a reference library?
