#!/usr/bin/env python3
"""Mark 6 stub tasks as done in kanban."""
import sqlite3, time

DB = sqlite3.connect('/home/ty/.hermes/kanban.db')

task_ids = [
    't_5afeeaae9ca345e8',  # cognitive-decline, neuroinflammation, hypothalamus stubs
    't_761dd3ea54c44f76',  # AI-policy-global-governance stub
    't_4fd8315c70424f17',  # xai stub
    't_8eca0a1a15f84f92',   # saas-pricing stub
]

for tid in task_ids:
    cur = DB.execute("SELECT id, title FROM tasks WHERE id = ?", (tid,))
    row = cur.fetchone()
    if row:
        DB.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (tid,))
        print(f"DONE: {tid} — {row[1][:50]}")
    else:
        print(f"NOT FOUND: {tid}")

DB.commit()
print("\nAll stubs tasks marked done.")