import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_reference_matching_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'def add_[a-zA-Z0-9_]+\s*\(', text):
    print(m.group(0))

for m in re.finditer(r'(?:Рисунок|fig\d+)[^\n]+', text):
    line = m.group(0).strip()
    if 'Рисунок' in line:
        print(line)
