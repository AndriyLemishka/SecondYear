import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1065, min(1085, len(lines))):
    print(f'{i+1}: {lines[i]}', end='')
