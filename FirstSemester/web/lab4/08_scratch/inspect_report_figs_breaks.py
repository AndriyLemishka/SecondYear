import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_reference_matching_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('fig13_desktop_top.png')
print(text[start-100:start+1200])
