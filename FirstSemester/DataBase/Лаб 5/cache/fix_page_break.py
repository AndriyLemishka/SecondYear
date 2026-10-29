with open(r'Лаб 5\cache\rebuild_compact_lab5.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Check if this line is doc.add_page_break() right before Visnovky
    if 'doc.add_page_break()' in line and i + 1 < len(lines) and 'Висновки' in lines[i+1]:
        print(f"Skipping page break at line {i+1}")
        continue
    if 'add_p("Висновки"' in line:
        new_lines.append('add_p("Висновки", bold=True, align=\'CENTER\', size=Pt(14), space_before=Pt(14), space_after=Pt(6), indent=0)\n')
        continue
    new_lines.append(line)

with open(r'Лаб 5\cache\rebuild_compact_lab5.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully updated rebuild_compact_lab5.py without page break before conclusions!")
