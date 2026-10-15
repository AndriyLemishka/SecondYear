import re

with open('lab4/05_figma_exports/charge/code.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, l in enumerate(lines):
    m = re.match(r'\s*const\s+(f[A-Za-z0-9_]+)\s*=\s*figma\.createFrame\(\);', l)
    if m:
        var = m.group(1)
        name = ""
        # check next 3 lines for .name = "..."
        for j in range(i, min(i+5, len(lines))):
            m2 = re.search(r'\.name\s*=\s*"([^"]+)"', lines[j])
            if m2:
                name = m2.group(1)
                break
        print(f"Line {i+1}: {var} -> {name}")
