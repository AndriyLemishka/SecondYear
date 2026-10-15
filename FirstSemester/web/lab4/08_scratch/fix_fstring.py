# -*- coding: utf-8 -*-
import os, sys

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
GEN_SCRIPT = os.path.join(BASE_DIR, "08_scratch", "generate_final_figma_plugin.py")

with open(GEN_SCRIPT, "r", encoding="utf-8") as f:
    text = f.read()

idx_desk = text.find('// FRAME 05: FULL DESKTOP')
idx_cat = text.find('const fCatalog = figma.createFrame();')

print("Found desk:", idx_desk, "cat:", idx_cat)
if idx_desk != -1 and idx_cat != -1:
    before = text[:idx_desk]
    middle = text[idx_desk:idx_cat]
    after = text[idx_cat:]
    
    # In middle, any single { not preceded or followed by { needs to be doubled
    m_temp = middle.replace("{{", "__OPEN__").replace("}}", "__CLOSE__")
    m_temp = m_temp.replace("{", "{{").replace("}", "}}")
    m_fixed = m_temp.replace("__OPEN__", "{{").replace("__CLOSE__", "}}")
    
    fixed_text = before + m_fixed + after
    with open(GEN_SCRIPT, "w", encoding="utf-8") as f:
        f.write(fixed_text)
    print("Fixed curly braces in generate_final_figma_plugin.py!")
else:
    print("Indices not found!")
