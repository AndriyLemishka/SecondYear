import sys
import re

with open(r'Лаб 5\cache\rebuild_compact_lab5.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all queries
# Format: {"id": "1.1.1", "title": "...", "sql": "..."}
queries = re.findall(r'\{\s*"id":\s*"([^"]+)",\s*"title":\s*"([^"]+)",\s*"sql":\s*"([^"]+)"', text)

print(f"Total queries found: {len(queries)}")

# Group by task
by_task = {}
for q_id, title, sql in queries:
    task_num = q_id.split('.')[0]
    sub_num = q_id.split('.')[1]
    by_task.setdefault(task_num, []).append((q_id, title, sql))

for t, qlist in sorted(by_task.items()):
    print(f"\nTask {t} has {len(qlist)} queries. First 5:")
    for q in qlist[:5]:
        print(f"  {q[0]}: {q[1]} -> {q[2][:60]}")
