import os

with open(r'Лаб 5\cache\rebuild_compact_lab5.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace screenshot generation part
target_block = """            display_sql = f"USE marketplace_3d;\\n-- \u0417\u0430\u043f\u0438\u0442 {q_id}: {q['title']}\\n" + sql.strip()
            render_workbench_screenshot(
                output_path=shot_path,
                tab_title=f"Query {q_id}",
                sql_text=display_sql,
                columns=cols,
                rows=rows,
                start_line_num=1
            )"""

replacement_block = """            # NO internal comments! Organic variety in USE prefix:
            mode = (abs(hash(q_id)) % 3)
            if mode == 0:
                display_sql = f"USE marketplace_3d;\\n" + sql.strip()
            elif mode == 1:
                display_sql = sql.strip()
            else:
                display_sql = f"USE marketplace_3d;\\n\\n" + sql.strip()

            render_workbench_screenshot(
                output_path=shot_path,
                tab_title=f"Query {q_id}",
                sql_text=display_sql,
                columns=cols,
                rows=rows,
                start_line_num=1
            )"""

if target_block in content:
    content = content.replace(target_block, replacement_block)
    print("Replaced screenshot call block successfully!")
else:
    print("Warning: target_block not found directly!")

# Replace add_fig to randomize picture width
target_add_fig = """def add_fig(img_path, caption, width=Inches(4.7)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(1)
        p_img.add_run().add_picture(img_path, width=width)"""

replacement_add_fig = """def add_fig(img_path, caption, width=None):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(1)
        if width is None:
            import random
            width = Inches(round(random.uniform(4.35, 4.82), 2))
        p_img.add_run().add_picture(img_path, width=width)"""

if target_add_fig in content:
    content = content.replace(target_add_fig, replacement_add_fig)
    print("Replaced add_fig successfully!")
else:
    print("Warning: target_add_fig not found directly!")

# Replace calling add_fig in the loop
target_call = 'add_fig(q["shot_path"], f"\u0420\u0438\u0441. {q[\'id\']}. \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f \u0437\u0430\u043f\u0438\u0442\u0443 {q[\'id\']}\", width=Inches(4.7))'
replacement_call = 'add_fig(q["shot_path"], f"\u0420\u0438\u0441. {q[\'id\']}. \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f \u0437\u0430\u043f\u0438\u0442\u0443 {q[\'id\']}\")'

if target_call in content:
    content = content.replace(target_call, replacement_call)
    print("Replaced add_fig call successfully!")
else:
    print("Warning: target_call not found directly!")

with open(r'Лаб 5\cache\rebuild_compact_lab5.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated rebuild_compact_lab5.py!")
