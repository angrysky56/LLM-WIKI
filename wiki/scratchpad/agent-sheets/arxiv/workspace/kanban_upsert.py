import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing non-done tasks
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    status = "blocked" if blocked else "done"  # arxiv writes to wiki, not workspace → done
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:arxiv-agent', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# Open items from arxiv carryover 2026-05-30
items = [
    {
        "agent": "researcher",
        "title": "STV vs RiM comparison — reasoning at test time",
        "body": "Compare Self-Trained Verification (2605.30290) with RiM (2605.30343) — both address reasoning at test time: memory blocks (RiM) vs verifier-refinement (STV). Different mechanisms, complementary. RiM decouples internal computation; STV trains the verifier that drives refinement. Does wiki have a synthesis page on test-time reasoning mechanisms? Write comparison in wiki/synthesis/test-time-reasoning-mechanisms.md or expand existing.",
        "priority": 2,
        "blocked": False,
    },
    {
        "agent": "researcher",
        "title": "Physics vs LLMSurgeon investigator agent pattern comparison",
        "body": "Compare Physics-Is-All-You-Need (2605.30353) with LLMSurgeon (2605.30348) — both use static environment ablation to catch failures invisible to standard testing. LLMSurgeon: DMS investigator agent (reproduces misbehavior in static environment with hardcoded tool responses). Physics: oracle test suites against CLASS-PT reference. Both reveal that standard benchmarks miss systematic failures. Compare approaches for evaluation design — write to wiki/synthesis/static-environment-ablation-evaluation.md or expand existing.",
        "priority": 2,
        "blocked": False,
    },
    {
        "agent": "researcher",
        "title": "Predictive adequacy vs explanatory correctness — create concept page",
        "body": "Physics-Is-All-You-Need (2605.30353) makes a critical distinction: 'predictive adequacy' (produces right numbers) vs 'explanatory correctness' (produces right numbers for the right reasons). This distinction drives the 33-session architecture error. Does wiki have a page on this distinction? If not, create wiki/concepts/predictive-adequacy-vs-explanatory-correctness.md — could be a useful concept for agentic AI evaluation design.",
        "priority": 2,
        "blocked": False,
    },
]

results = []
for item in items:
    tid, status = upsert(
        item["agent"],
        item["title"],
        item["body"],
        item["priority"],
        item["blocked"]
    )
    results.append((item["title"], tid, status))

conn.close()

print("Upsert results:")
for title, tid, status in results:
    print(f"  [{status}] {title} -> {tid}")