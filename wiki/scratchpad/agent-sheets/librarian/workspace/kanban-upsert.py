#!/usr/bin/env python3
"""Kanban upsert for librarian carryover — informational done-cards."""
import sqlite3, os, hashlib, uuid, time

DB = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check existing tasks (non-done only)
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
active = {str(row[1]).strip(): row[0] for row in cur.fetchall()}
print(f"Active non-done cron tasks: {len(active)}")

# Check done tasks too (for dedup)
cur.execute("SELECT id, title, status FROM tasks WHERE status = 'done' AND created_by LIKE 'cron:%'")
done = {str(row[1]).strip(): row[0] for row in cur.fetchall()}
print(f"Done cron tasks: {len(done)}")

all_existing = {**active, **done}

def upsert_done(agent, title, body, priority=1):
    """Create informational done-card (wiki agent, not dispatcher-executed)."""
    key = f"{agent}: {title}".strip()
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    if key in all_existing:
        status = cur.execute("SELECT status FROM tasks WHERE title = ?", (key,)).fetchone()[0]
        print(f"  SKIPPED ({status}): {key}")
        return all_existing[key], "skipped"
    tid = f"t_{uuid.uuid4().hex[:16]}"
    now = int(time.time())
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'cron:librarian-kanban-review', ?, ?)
    """, (tid, key, body, agent, priority, ik, now))
    conn.commit()
    print(f"  CREATED: {key} -> {tid}")
    return tid, "created"

# Items from librarian carryover

# 1. GoodRobot — blocked needs Ty
print("\n=== GoodRobot multi-location ===")
upsert_done("librarian", "GoodRobot multi-location — needs Ty decision",
    "11 files across 2 vault locations. wiki/entities/projects/goodrobot.md SHUT DOWN May 18; wiki/projects/projects 1/ active; wiki/projects/goodrobot/ active business entity. Priority: MEDIUM, blocked.")

# 2. Stub concepts — batch for librarians-assistant
print("\n=== 11 stub concepts ===")
upsert_done("librarians-assistant", "11 stub concepts — batch expand or consolidate",
    "True stub (15 lines): legal-accountability-stub. Template cluster (10, 18 lines each, all created 2026-06-03): 3dgs, CRI, Firecracker, autopoiesis, blackmail, codebase-inspection, compound-commands, directed-preferential-placement, fts5, functional-emotions. Greek letters (beta/delta/epsilon/gamma/zeta) are NOT stubs at 19 lines each. Delegate to librarians-assistant.")

# 3. Broken links — delegate to librarians-assistant
print("\n=== 94 broken links ===")
upsert_done("librarians-assistant", "94 broken links — delegate to librarians-assistant",
    "Genuine missing refs: deliberative-agents, reactive-agents, hybrid-agents, meta-cognitive-agents (from agents.md), tool-use (autonomous-agents.md), diffusion-models (generative-ai.md), grpo (group-relative-policy-optimization.md), qora (lora.md), MOP (neural-architecture-search.md, rz-nas.md), bradley-terry, test-time-compute-scaling. Also template refs in operating docs and GoodRobot cross-refs. Full list in librarian carryover.")

# 4. Merge candidates — informational only
print("\n=== 10 merge candidates — template artifacts, skip ===")
upsert_done("librarian", "10 merge candidates — template artifacts, skip",
    "agentic-planner↔agentic-sequential: both genuine, different depths. 3dgs↔CRI↔...: same-template stub, similarity is artifact. Skip all 10 — no actionable merges.")

conn.close()
print("\nDone.")