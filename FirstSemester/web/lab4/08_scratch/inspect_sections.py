import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

sections = ['fDesktop', 'fTablet', 'fMobile', 'fCatalog', 'fDetails', 'fOverlays']
for s in sections:
    idx = text.find(f'{s} = figma.createFrame()')
    print(f'=== {s} ===')
    if idx != -1:
        # find where next section starts or 1500 chars
        snippet = text[idx:idx+1500]
        print(snippet[:600])
        print('...\n')
