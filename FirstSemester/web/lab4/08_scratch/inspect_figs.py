import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_all_figures_v2.py', 'r', encoding='utf-8') as f:
    text = f.read()

for name in ['fig15', 'fig16', 'fig17', 'fig18']:
    idx = text.find(f'html_{name} =')
    print(f'*** html_{name} ***')
    print(text[idx:idx+600])
    print('\n' + '='*40 + '\n')
