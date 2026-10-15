# -*- coding: utf-8 -*-
import os, re

p = r'd:\Studing\SecondYear\FirstSemester\web\lab4\06_prototypes\index.html'
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
print(f"Total image references: {len(imgs)}")
for im in set(imgs):
    # check if path exists relative to prototype dir
    p_rel = os.path.normpath(os.path.join(os.path.dirname(p), im))
    exists = os.path.exists(p_rel)
    print(f"  {im} -> exists: {exists}")
