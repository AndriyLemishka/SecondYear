import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

sub = text[:text.find('const SVG_ASSETS')]
keys = re.findall(r'(\w+):\s*"data:image', sub)
print('Keys in ASSETS_B64:', keys)
