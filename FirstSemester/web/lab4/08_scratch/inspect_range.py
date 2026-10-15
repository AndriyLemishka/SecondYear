import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('lab4/05_figma_exports/charge/code.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = int(sys.argv[1]) if len(sys.argv) > 1 else 636
end = int(sys.argv[2]) if len(sys.argv) > 2 else 740

for i in range(start - 1, min(end, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
