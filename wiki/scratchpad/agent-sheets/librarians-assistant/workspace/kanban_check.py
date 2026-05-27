import sqlite3, hashlib, uuid, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute("SELECT id, title, status, assignee FROM tasks WHERE status != 'done'", ())
rows = cur.fetchall()
print(f"Total non-done tasks: {len(rows)}")
for row in rows:
    print(f"  {row[0]} | {row[1][:60]} | {row[2]} | {row[3]}")

# Check specific task IDs from carryover
cur2 = DB.execute("SELECT id, title, status FROM tasks WHERE id IN (?, ?, ?, ?)",
    ('t_e366f0899e1f4b16', 't_c5205b4684fa4374', 't_eac64c085f424ab7', 't_f0fcb3dcd69d49b2'))
existing = {str(row[0]): row for row in cur2.fetchall()}
print(f"\nSpecific tasks from carryover: {len(existing)} found")
for tid in ['t_e366f0899e1f4b16', 't_c5205b4684fa4374', 't_eac64c085f424ab7', 't_f0fcb3dcd69d49b2']:
    if tid in existing:
        print(f"  {tid}: {existing[tid][2]} - {existing[tid][1][:50]}")
    else:
        print(f"  {tid}: NOT FOUND")
DB.close()