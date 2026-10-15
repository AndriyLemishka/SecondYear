import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'.{0,30}(?:брон|заброн|слот).{0,30}', text, flags=re.IGNORECASE):
    print(m.group(0).strip())
