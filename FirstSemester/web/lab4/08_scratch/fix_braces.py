# -*- coding: utf-8 -*-
import os, sys

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
GEN_SCRIPT = os.path.join(BASE_DIR, "08_scratch", "generate_final_figma_plugin.py")
UPDATE_SCRIPT = os.path.join(BASE_DIR, "08_scratch", "update_figma_plugin_code.py")

with open(UPDATE_SCRIPT, "r", encoding="utf-8") as f:
    text = f.read()

# In update_figma_plugin_code.py, replace the insertion line to escape braces:
old_line = "new_code = code[:pos_desk] + new_desktop_tablet_mobile + \"\\n  \" + code[pos_cat:]"
new_line = "new_code = code[:pos_desk] + new_desktop_tablet_mobile.replace('{', '{{').replace('}', '}}') + \"\\n  \" + code[pos_cat:]"

if old_line in text:
    text = text.replace(old_line, new_line)
    with open(UPDATE_SCRIPT, "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated update_figma_plugin_code.py with brace escaping.")
else:
    print("Could not find line, checking...")

