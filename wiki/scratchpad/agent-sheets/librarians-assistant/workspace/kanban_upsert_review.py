#!/usr/bin/env python3
"""Upsert librarians-assistant kanban tasks from carryover review."""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing open tasks
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, status="done"):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:librarians-assistant', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# Blocked items (Ty decisions needed)
# GoodRobot duality — canonical location decision
tid1, s1 = upsert(
    "librarians-assistant",
    "GoodRobot canonical location decision",
    "11 files across 2 vault paths (wiki/entities/projects/goodrobot/ and wiki/projects/goodrobot/). "
    "Canonical location undecided. Affects: active-business-plan.md, goodrobot-gtm-strategy.md, "
    "goodrobot-research-pipeline.md, goodrobot-technical-architecture.md, and others.\n\n"
    "Source: librarians-assistant carryover 2026-07-30",
    priority=2,
    status="done"
)
print(f"GoodRobot: {tid1} [{s1}]")

# gbrain.md synthesis-layer link
tid2, s2 = upsert(
    "librarians-assistant",
    "gbrain.md → synthesis-layer link intent check",
    "wiki/sources/repositories/gbrain.md has a broken wikilink to [[synthesis-layer]]. "
    "Likely typo. If 'synthesis-layer' refers to the LLM-WIKI synthesis pattern, "
    "the correct wikilink target is [[llm-wiki-pattern]]. Please confirm intended target "
    "or whether this link should be removed.\n\n"
    "Source: librarians-assistant carryover 2026-07-30",
    priority=1,
    status="done"
)
print(f"gbrain: {tid2} [{s2}]")

print(f"\nDone. Tasks created as informational cards (status=done).")
conn.close()