# GoodRobot — Research Pipeline MVP Specification

**Prepared by:** CTO Agent  
**Date:** May 2026  
**Reference:** GOO-31  
**Status:** MVP Draft

---

## Pipeline Overview

```
Prospect Input (name + URL)
        │
        ▼
┌───────────────────┐
│  Research Agent   │ ← MiniMax-M2.7
│  (Stage 1)        │
└────────┬──────────┘
         │ StructuredBusinessProfile
         ▼
┌───────────────────┐
│ Gap Analysis Agent│ ← MiniMax-M2.7
│  (Stage 2)        │
└────────┬──────────┘
         │ ProspectBlindSpots
         ▼
┌───────────────────┐
│ Pitch Prep Agent  │ ← MiniMax-M2.7
│  (Stage 3)        │
└────────┬──────────┘
         │ DiscoveryCallScript
         ▼
   Human Review (if confidence < threshold)
         │
         ▼
   Discovery Call Delivery
```

---

## Stage 1: Research Agent

**Input:** `{ company_name: string, company_url: string }`

**Output:** `StructuredBusinessProfile`

### Output Schema

```json
{
  "company_name": "string",
  "website": "string",
  "research_timestamp": "ISO8601",
  "confidence": 0.0,
  "fields": {
    "legal_name": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "location": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "owner_leadership": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "years_in_business": { "value": "number|null", "source": "string", "confidence": 0.0 },
    "employee_count": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "revenue_signals": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "service_offerings": { "value": ["string"], "source": "string", "confidence": 0.0 },
    "pricing_structure": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "customer_demographics": { "value": "string|null", "source": "string", "confidence": 0.0 },
    "competitive_positioning": { "value": "string|null", "source": "string", "confidence": 0.0 }
  },
  "research_notes": "string (freeform synthesis)",
  "sources": ["string"],
  "data_quality_flags": ["string"]
}
```

### Data Sources (in priority order)

1. **Company Website** — Homepage, About, Services, Pricing pages
   - Tool: Playwright (headless Chrome)
   - Extract: text content, metadata, contact info, service descriptions

2. **Google Business Profile** (via scraping)
   - Extract: reviews, ratings, business categories, hours, photos count

3. **Social Media** (LinkedIn Company, Facebook Page)
   - Tool: Playwright for public LinkedIn pages
   - Extract: employee count, company description, posts, follower count

4. **Third-Party APIs** (future enhancement)
   - Clearbit Company API (requires key)
   - Apollo.io (requires key)

### Research Prompt Strategy

```
SYSTEM: You are a expert business researcher. Given web content about a local 
service business, extract factual business information. Be conservative — 
only assert what is explicitly stated or strongly implied. Flag uncertain 
information with confidence < 0.7.

USER: Research {company_name} from {company_url}. 
Website content:
{scraped_content}

Output a StructuredBusinessProfile JSON object.
```

### Quality Thresholds

| Metric | Threshold | Action if Failed |
|--------|-----------|-----------------|
| Overall confidence | ≥ 0.7 | Flag for human review |
| legal_name confidence | ≥ 0.5 | Flag in output |
| service_offerings populated | ≥ 3 services | Flag partial |
| pricing_structure found | any value | Flag if missing |

### Error Handling

- **Scraping failure:** Retry 3x with exponential backoff (1s, 2s, 4s). 
  Fall back to metadata-only profile with low confidence.
- **Website unreachable:** Return profile with `data_quality_flags: ["website_unreachable"]`
  and confidence 0.3.
- **LLM timeout:** Retry once. If fails, return partial profile with error flag.

---

## Stage 2: Gap Analysis Agent

**Input:** `StructuredBusinessProfile`

**Output:** `ProspectBlindSpots`

### Output Schema

```json
{
  "company_name": "string",
  "profile_confidence": 0.0,
  "blind_spots": [
    {
      "id": 1,
      "category": "pricing_structure| digital_presence| customer_acquisition| operations| technology",
      "title": "string",
      "description": "string",
      "severity": 1-5,
      "confidence": 0.0,
      "reasoning": "string",
      "discovery_questions": ["string"]
    }
  ],
  "top_blind_spots": [1, 2, 3],
  "analysis_confidence": 0.0
}
```

### Blind Spot Categories

| Category | Description | Example |
|----------|-------------|---------|
| `pricing_structure` | Revenue model gaps, underpricing signals | No packages, only hourly, price too low/high for market |
| `digital_presence` | Online visibility gaps | No Google Business Profile, no reviews, outdated website |
| `customer_acquisition` | Reliance on single channel | Word-of-mouth only, no referral system, no inbound |
| `operations` | Efficiency or scalability issues | No scheduling system, manual booking, no CRM |
| `technology` | Missing digital tools | No online booking, no email list, no SMS reminders |

### Scoring Logic

```
blind_spot_score = severity × confidence

Select top N (N=3-5) by blind_spot_score.
Require: severity ≥ 2 AND confidence ≥ 0.5 for inclusion.
```

### Quality Thresholds

| Metric | Threshold | Action if Failed |
|--------|-----------|-----------------|
| Min blind spots identified | ≥ 3 | Flag for human review |
| Analysis confidence | ≥ 0.5 | Flag for human review |
| At least 2 categories represented | yes/no | Flag if all same category |

---

## Stage 3: Pitch Prep Agent

**Input:** `ProspectBlindSpots + StructuredBusinessProfile`

**Output:** `DiscoveryCallScript`

### Output Schema

```json
{
  "prospect_name": "string",
  "script": {
    "opening": {
      "personalized_greeting": "string",
      "rapport_hook": "string"
    },
    "qualification": {
      "questions": [
        { "question": "string", "purpose": "string" }
      ]
    },
    "blind_spot_discussion": {
      "framing": "string",
      "transitions": ["string"]
    },
    "capability_match": {
      "how_we_help": "string",
      "relevant_experience": "string"
    },
    "close": {
      "commitment_question": "string",
      "next_steps": ["string"]
    }
  },
  "qualification_criteria": {
    "budget_range": "string",
    "decision_maker": "boolean",
    "timeline": "string",
    "authority": "boolean"
  },
  "script_confidence": 0.0,
  "notes_for_caller": ["string"]
}
```

### Personalization Rules

- Use prospect's actual business name and specific services in greeting
- Reference their location in rapport_hook
- Match category to specific capability ("We help businesses like yours with [X]")
- Never fabricate facts — only use confirmed profile data

---

## Data Flow

### JSON Schemas

```
StructuredBusinessProfile: see Stage 1
ProspectBlindSpots: see Stage 2  
DiscoveryCallScript: see Stage 3
```

### Transport

- In-memory Python objects during MVP
- Future: Redis pub/sub for async processing

### Error Handling & Retry

| Stage | Retry Logic | Fallback |
|-------|-------------|----------|
| Research Agent scraper fails | 3x exponential backoff | Partial profile, low confidence |
| Research Agent LLM fails | 1x retry | Return error profile |
| Gap Analysis fails | 1x retry | Return empty blind_spots array |
| Pitch Prep fails | 1x retry | Return minimal script |

### Quality Gates

| Gate | Check | On Fail |
|------|-------|---------|
| G1 | Research confidence ≥ 0.7 | Auto-fail → human review |
| G2 | Gap Analysis ≥ 3 blind spots | Auto-fail → human review |
| G3 | Pitch Prep script complete | Auto-fail → human review |
| G4 | All stages complete < 60s | Warn — performance SLA |

---

## Human-in-the-Loop Points

### Full Automation OK (confidence ≥ threshold)
- Routine local service business (restaurant, plumber, electrician, dentist)
- Research confidence ≥ 0.8
- Gap Analysis ≥ 3 blind spots with confidence ≥ 0.6
- All data quality flags empty

### Human Review Required
- Research confidence 0.5–0.7
- Any data_quality_flags present
- Blind spot categories all same (suggests false positive)
- Unknown/no common business type
- Website unreachable (profile based on inference only)

### Human Escalation Required
- Research confidence < 0.5
- Gap Analysis returns < 2 blind spots
- Any contradictory data detected (name mismatch, etc.)
- Prospect is a multi-location enterprise

---

## Tech Stack

### MVP Implementation

| Component      | Technology                   | Cost |
| -------------- | ---------------------------- | ---- |
| Orchestration  | FastAPI + asyncio            | Free |
| Web Scraping   | Playwright (headless Chrome) | Free |
| LLM Inference  | MiniMax-M2.7                 | £10  |
| Data Storage   | JSON files (MVP)             | Free |
| Total MVP Cost |                              | £10  |

### Production Enhancement (future)

| Component | Technology | Est. Cost |
|-----------|-----------|-----------|
| Orchestration | FastAPI + Celery | Free |
| Web Scraping | ScrapingBee API | £10/mo |
| LLM Inference | MiniMax-M2.7 | £0 (internal) |
| Data Storage | PostgreSQL | £5/mo |
| Vector Memory | ChromaDB (local) | Free |
| Monitoring | Grafana + Prometheus | Free |
| Total Production Cost | | ~£15/mo |

### LLM Calls Per Prospect

| Stage | Input Tokens (est.) | Output Tokens (est.) |
|-------|---------------------|----------------------|
| Research Agent | ~5,000 (scraped content) | ~800 |
| Gap Analysis | ~2,000 (profile) | ~600 |
| Pitch Prep | ~1,500 (profile + gaps) | ~1,200 |
| **Total per prospect** | ~8,500 | ~2,600 |

---

## C(R(F(S(D(RB(M(SF)))))) Applied to Research Pipeline

### C — Conceptualization
The research pipeline converts a prospect's web presence into a structured profile that powers 
discovery call preparation. Goal: replicate the son's 20-30 minute manual research in < 2 minutes.

### R — Representation
JSON schema with confidence scores per field. Confidence expressed as 0.0–1.0 with explicit 
source attribution. Enables downstream agents to weight fields appropriately.

### F — Facts Extracted
10 structured fields per business profile (see Stage 1 schema). Each field tagged with source 
and confidence. Facts are deterministic extractions from scraped content.

### S — Scrutiny (Failure Modes)
1. Website content is thin/outdated → low confidence profile
2. No Google presence → missing data_quality_flags
3. LLM makes inference beyond evidence → false confidence
4. Scraping blocked → partial profile only

### D — Derivation
From low-confidence fields: propagate low confidence to downstream gap analysis.
From missing data: flag for human review before gap analysis.
From high-confidence profile: confidence in blind spots can be higher.

### RB — Rules
1. Research confidence < 0.5 → human review required
2. Gap analysis requires ≥ 3 blind spots for pipeline to continue
3. Script personalization must use only confirmed profile data
4. No fabrication — all personalization must trace to explicit profile field

### M — Model
Multi-stage pipeline with explicit quality gates. Each stage is independently testable.
Data flows forward only after quality gate passes.

### SF — Semantic Formalization
Research Pipeline = Composition[ResearchAgent, GapAnalysisAgent, PitchPrepAgent]
with QualityGate per stage and HumanReview gate at output.
