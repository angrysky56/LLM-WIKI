import sqlite3, hashlib, uuid, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'", ())

existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}
print("Non-done tasks:", len(existing))

# Check the MOP task
mop_key = "researcher: MOP vs fine-tuning boundary"
print(f"MOP task status: {existing.get(mop_key, 'NOT FOUND')}")

# Check hybrid-agents task
hybrid_key = "researcher: hybrid-agents stub upgrade"
print(f"hybrid-agents task status: {existing.get(hybrid_key, 'NOT FOUND')}")

# Check if any researcher open tasks exist
researcher_open = DB.execute(
    "SELECT id, title, status FROM tasks WHERE assignee = 'researcher' AND status != 'done'",
    ()
).fetchall()
print(f"\nResearcher open tasks: {len(researcher_open)}")
for t in researcher_open:
    print(f"  {t}")