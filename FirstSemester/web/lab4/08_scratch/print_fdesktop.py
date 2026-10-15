import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('fDesktop = figma.createFrame()')
end = text.find('fTablet = figma.createFrame()')

print(text[start:end])
