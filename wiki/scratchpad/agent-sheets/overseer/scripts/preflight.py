#!/usr/bin/env python3
"""
Wiki Overseer Pre-Flight Validation Script

Gathers ground truth from:
  - ~/.hermes/cron/jobs.json  (scheduler timestamps — authoritative)
  - wiki/scratchpad/agent-sheets/*/carryover.md  (agent state)
  - ~/.hermes/kanban.db  (open task summary)

Outputs structured JSON to stdout for the overseer LLM to consume.
This eliminates date hallucination by providing machine-verified data.

Usage:
    python3 preflight.py
    python3 preflight.py --output /tmp/wiki-overseer-preflight.json
"""

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Constants ────────────────────────────────────────────────────────────

WIKI_ROOT = Path("/home/ty/Documents/LLM-WIKI")
AGENT_SHEETS = WIKI_ROOT / "wiki" / "scratchpad" / "agent-sheets"
JOBS_JSON = Path.home() / ".hermes" / "cron" / "jobs.json"
KANBAN_DB = Path.home() / ".hermes" / "kanban.db"
REPORTS_DIR = WIKI_ROOT / "wiki" / "scratchpad" / "jobs" / "reports"

# Map cron job names → agent sheet directory names
JOB_NAME_TO_AGENT = {
    "Wiki Researcher": "researcher",
    "arxiv-top3": "arxiv",
    "world-news": "news",
    "llm-wiki-raw-ingest": "ingest",
    "Wiki Librarian": "librarian",
    "Wiki Librarians-Assistant": "librarians-assistant",
    "Wiki Insights Generator": "insights",
    "wiki-overseer": "overseer",
}

# Known agents (even if no cron job exists)
ALL_AGENTS = [
    "researcher", "arxiv", "news", "ingest",
    "librarian", "librarians-assistant", "insights",
    "overseer", "orcaid",
]


def get_system_date() -> str:
    """Return current system date as ISO string."""
    return datetime.now().strftime("%Y-%m-%d")


def get_system_datetime() -> str:
    """Return current system datetime as ISO string."""
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown text.

    Returns dict with parsed key-value pairs. Handles missing or
    malformed frontmatter gracefully.
    """
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            fm[key] = value
    return fm


def validate_date(date_str: str, system_date: str) -> str | None:
    """Validate a date string is not in the future.

    Returns the date string if valid, None if hallucinated (future date).
    """
    if not date_str:
        return None
    # Extract just the date part (handle ISO datetime formats)
    date_part = date_str[:10]
    try:
        parsed = datetime.strptime(date_part, "%Y-%m-%d")
        system = datetime.strptime(system_date, "%Y-%m-%d")
        if parsed > system:
            return None  # Future date = hallucinated
        return date_part
    except ValueError:
        return None


def extract_open_items(text: str) -> list[str]:
    """Extract open items from carryover markdown.

    Looks for unchecked items in 'What Remains', 'Open', 'Open Questions',
    'Still Open', 'Next' sections.
    """
    items = []
    # Find sections that typically contain open items
    section_patterns = [
        r"##\s+(?:What Remains|Open|Open Questions|Still Open|Next)\b",
        r"##\s+(?:What|Items)\s+(?:Remains|Open|Remaining)\b",
    ]

    in_open_section = False
    for line in text.split("\n"):
        # Check if we're entering an open-items section
        for pat in section_patterns:
            if re.match(pat, line, re.IGNORECASE):
                in_open_section = True
                break

        # Check if we're leaving (new ## section)
        if in_open_section and re.match(r"^##\s+", line) and not any(
            re.match(p, line, re.IGNORECASE) for p in section_patterns
        ):
            in_open_section = False

        # Extract unchecked items
        if in_open_section:
            match = re.match(r"^\s*-\s+\[\s\]\s+(.*)", line)
            if match:
                items.append(match.group(1).strip())

    return items


def read_carryover(agent: str) -> dict:
    """Read and parse an agent's carryover file.

    Returns structured data with validated dates and extracted open items.
    """
    carryover_path = AGENT_SHEETS / agent / "carryover.md"
    result = {
        "exists": False,
        "path": str(carryover_path),
        "frontmatter_updated": None,
        "validated_updated": None,
        "has_frontmatter": False,
        "summary": None,
        "open_items": [],
        "open_items_count": 0,
        "raw_first_lines": "",
    }

    if not carryover_path.exists():
        return result

    result["exists"] = True
    try:
        text = carryover_path.read_text(encoding="utf-8")
    except Exception as e:
        result["error"] = str(e)
        return result

    # Save first 5 non-empty lines for context
    non_empty = [ln.strip() for ln in text.split("\n") if ln.strip()][:5]
    result["raw_first_lines"] = "\n".join(non_empty)

    # Parse frontmatter
    fm = parse_frontmatter(text)
    result["has_frontmatter"] = bool(fm)

    system_date = get_system_date()

    if "updated" in fm:
        result["frontmatter_updated"] = fm["updated"]
        result["validated_updated"] = validate_date(fm["updated"], system_date)

    if "summary" in fm:
        result["summary"] = fm["summary"]

    # Extract open items
    result["open_items"] = extract_open_items(text)
    result["open_items_count"] = len(result["open_items"])

    return result


def read_cron_jobs() -> dict:
    """Read jobs.json and extract per-agent cron state.

    Uses scheduler timestamps as ground truth (not LLM-parseable dates).
    """
    agents_cron = {}

    if not JOBS_JSON.exists():
        return agents_cron

    try:
        with open(JOBS_JSON) as f:
            data = json.load(f)
    except Exception as e:
        return {"_error": str(e)}

    for job in data.get("jobs", []):
        job_name = job.get("name", "")
        agent_name = JOB_NAME_TO_AGENT.get(job_name)
        if not agent_name:
            continue

        agents_cron[agent_name] = {
            "job_id": job.get("id"),
            "job_name": job_name,
            "schedule": job.get("schedule_display", ""),
            "enabled": job.get("enabled", False),
            "state": job.get("state", "unknown"),
            "last_run_at": job.get("last_run_at"),
            "last_status": job.get("last_status"),
            "last_error": job.get("last_error"),
            "next_run_at": job.get("next_run_at"),
            "runs_completed": job.get("repeat", {}).get("completed", 0),
            "deliver": job.get("deliver", ""),
            "skills": job.get("skills", []),
            "model": job.get("model"),
        }

    return agents_cron


def read_kanban_summary() -> dict:
    """Read kanban.db and produce a summary of open tasks."""
    result = {
        "total_open": 0,
        "by_assignee": {},
        "by_status": {},
        "blocked_items": [],
        "recent_items": [],
    }

    if not KANBAN_DB.exists():
        result["error"] = "kanban.db not found"
        return result

    try:
        db = sqlite3.connect(str(KANBAN_DB))
        db.row_factory = sqlite3.Row

        # Open tasks
        rows = db.execute(
            "SELECT id, title, assignee, status, priority, created_at "
            "FROM tasks WHERE status != 'done' ORDER BY priority DESC, created_at DESC"
        ).fetchall()

        result["total_open"] = len(rows)

        for row in rows:
            assignee = row["assignee"] or "unassigned"
            status = row["status"] or "unknown"
            result["by_assignee"][assignee] = result["by_assignee"].get(assignee, 0) + 1
            result["by_status"][status] = result["by_status"].get(status, 0) + 1

            if status == "blocked":
                result["blocked_items"].append({
                    "id": row["id"],
                    "title": row["title"],
                    "assignee": assignee,
                })

        # 5 most recent
        for row in rows[:5]:
            result["recent_items"].append({
                "id": row["id"],
                "title": row["title"],
                "assignee": row["assignee"] or "unassigned",
                "status": row["status"],
                "priority": row["priority"],
            })

        db.close()
    except Exception as e:
        result["error"] = str(e)

    return result


def count_reports(agent: str) -> int:
    """Count report files for an agent."""
    report_dir = REPORTS_DIR / agent
    if not report_dir.exists():
        return 0
    return len(list(report_dir.glob("*.md")))


def main():
    """Run pre-flight validation and output structured JSON."""
    system_date = get_system_date()
    system_datetime = get_system_datetime()

    # Gather data from all sources
    cron_data = read_cron_jobs()
    kanban = read_kanban_summary()

    agents = {}
    for agent_name in ALL_AGENTS:
        carryover = read_carryover(agent_name)
        cron = cron_data.get(agent_name, {})

        # Determine effective last-run date: prefer cron ground truth
        cron_last_run = cron.get("last_run_at")
        effective_last_run = None
        last_run_source = None

        if cron_last_run:
            # Validate cron timestamp too (should always be valid, but be safe)
            validated = validate_date(cron_last_run[:10] if cron_last_run else "", system_date)
            if validated:
                effective_last_run = validated
                last_run_source = "cron_scheduler"

        if not effective_last_run and carryover.get("validated_updated"):
            effective_last_run = carryover["validated_updated"]
            last_run_source = "carryover_frontmatter"

        # Compute staleness
        days_since_run = None
        if effective_last_run:
            try:
                last = datetime.strptime(effective_last_run, "%Y-%m-%d")
                now = datetime.strptime(system_date, "%Y-%m-%d")
                days_since_run = (now - last).days
            except ValueError:
                pass

        # Determine status
        status = "unknown"
        if cron.get("state") == "scheduled" and cron.get("enabled"):
            if cron.get("last_status") == "ok":
                status = "active" if (days_since_run is not None and days_since_run <= 2) else "stale"
            elif cron.get("last_status") == "error":
                status = "error"
            else:
                status = "active"
        elif not cron.get("enabled", True):
            status = "disabled"
        elif agent_name == "orcaid":
            status = "paused"

        # Check for hallucinated dates in carryover
        date_hallucinated = False
        if carryover.get("frontmatter_updated") and not carryover.get("validated_updated"):
            date_hallucinated = True

        agents[agent_name] = {
            "effective_last_run": effective_last_run,
            "last_run_source": last_run_source,
            "days_since_run": days_since_run,
            "status": status,
            "cron": {
                "enabled": cron.get("enabled"),
                "state": cron.get("state"),
                "last_status": cron.get("last_status"),
                "last_error": cron.get("last_error"),
                "schedule": cron.get("schedule"),
                "runs_completed": cron.get("runs_completed"),
                "job_id": cron.get("job_id"),
            },
            "carryover": {
                "exists": carryover["exists"],
                "has_frontmatter": carryover["has_frontmatter"],
                "date_hallucinated": date_hallucinated,
                "raw_frontmatter_updated": carryover.get("frontmatter_updated"),
                "validated_updated": carryover.get("validated_updated"),
                "summary": carryover.get("summary"),
                "open_items": carryover["open_items"],
                "open_items_count": carryover["open_items_count"],
            },
            "report_count": count_reports(agent_name),
        }

    # Build final output
    output = {
        "system_date": system_date,
        "system_datetime": system_datetime,
        "generated_by": "preflight.py",
        "agents": agents,
        "kanban": kanban,
        "warnings": [],
    }

    # Add warnings
    for name, agent in agents.items():
        if agent["carryover"].get("date_hallucinated"):
            output["warnings"].append(
                f"{name}: carryover frontmatter 'updated' is hallucinated "
                f"({agent['carryover']['raw_frontmatter_updated']}), "
                f"using cron scheduler date instead"
            )
        if agent["status"] == "stale" and agent["days_since_run"] is not None:
            output["warnings"].append(
                f"{name}: {agent['days_since_run']} days since last run"
            )
        if agent["status"] == "error":
            output["warnings"].append(
                f"{name}: last cron run errored: {agent['cron'].get('last_error')}"
            )

    # Output
    output_path = None
    if len(sys.argv) > 2 and sys.argv[1] == "--output":
        output_path = sys.argv[2]

    json_str = json.dumps(output, indent=2, default=str)

    if output_path:
        Path(output_path).write_text(json_str)
        print(f"Written to {output_path}", file=sys.stderr)

    print(json_str)


if __name__ == "__main__":
    main()
