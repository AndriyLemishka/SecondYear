# -*- coding: utf-8 -*-
import re

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_reference_matching_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

out_lines = []
figures_added = re.findall(r'add_figure\("([^"]+)",\s*"([^"]+)"', text)
out_lines.append(f"Total figures added in report: {len(figures_added)}")
for i, (fn, cap) in enumerate(figures_added):
    out_lines.append(f"Fig {i+1:02d}: File='{fn}' | Caption='{cap}'")

expected_nums = set(range(1, 23))
actual_nums = []
for fn, cap in figures_added:
    m = re.search(r'Рисунок\s+(\d+)', cap)
    if m:
        actual_nums.append(int(m.group(1)))
out_lines.append(f"\nFigure numbers in captions: {actual_nums}")
missing = expected_nums - set(actual_nums)
out_lines.append(f"Missing figure numbers: {missing if missing else 'None! All 1-22 present.'}")

# Find any figure references in text like "рисунок X" or "рисунках X і Y"
refs = re.findall(r'(рисун(?:ок|ку|ках|ки|ком)\s+\d+(?:\s*(?:і|,|та)\s*\d+)?)', text, re.IGNORECASE)
out_lines.append("\nTextual references to figures:")
for r in sorted(set(refs)):
    out_lines.append(f"  {r}")

tables_added = re.findall(r'(Таблиця\s+\d+[^"]*)', text)
out_lines.append(f"\nTables found: {len(tables_added)}")
for t in tables_added:
    out_lines.append(f"  {t}")

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\audit_output.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print("Audit finished successfully.")
