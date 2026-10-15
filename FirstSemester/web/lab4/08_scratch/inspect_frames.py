import re, sys

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'([a-zA-Z0-9_]+)\.name\s*=\s*["\']([^"\']+)["\']', text):
    var_name = m.group(1)
    frame_name = m.group(2)
    print(f'{var_name}: {frame_name}')
