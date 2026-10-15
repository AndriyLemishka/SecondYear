import re

with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_reference_matching_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'add_figure\s*\(\s*doc\s*,\s*["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', text):
    fname = m.group(1)
    caption = m.group(2)
    print(f'{fname}  ===>  {caption}')
