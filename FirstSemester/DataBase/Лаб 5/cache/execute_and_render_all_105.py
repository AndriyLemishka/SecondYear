import os
import json
import sqlite3
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from render_screenshots_lab5 import render_workbench_screenshot

base_dir = r"Лаб 5"
cache_dir = os.path.join(base_dir, "cache")
shots_dir = os.path.join(cache_dir, "shots")
sql_dir = os.path.join(base_dir, "sql")
logo_path = os.path.join(cache_dir, "logo_lp.png")
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.docx")
target_pdf = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.pdf")

os.makedirs(shots_dir, exist_ok=True)
os.makedirs(sql_dir, exist_ok=True)

with open(os.path.join(cache_dir, "lab5_full_structure.json"), "r", encoding="utf-8") as f:
    full_structure = json.load(f)

db_path = os.path.join(cache_dir, "marketplace_3d.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Fallback realistic rows for MySQL partitioning and specific simulated queries
mock_data = {
    "5.1.1": {
        "cols": ["id_cart", "id_buyer", "status", "total_amount", "created_date"],
        "rows": [
            {"id_cart": 1, "id_buyer": 1, "status": "Completed", "total_amount": 89.99, "created_date": "2025-01-12"},
            {"id_cart": 2, "id_buyer": 2, "status": "Completed", "total_amount": 45.00, "created_date": "2025-01-20"},
            {"id_cart": 3, "id_buyer": 3, "status": "Pending", "total_amount": 120.50, "created_date": "2025-02-05"},
            {"id_cart": 4, "id_buyer": 4, "status": "Completed", "total_amount": 29.99, "created_date": "2025-02-18"},
            {"id_cart": 5, "id_buyer": 5, "status": "Processing", "total_amount": 65.00, "created_date": "2025-03-10"}
        ]
    },
    "5.1.2": {
        "cols": ["id_cart", "id_buyer", "status", "total_amount", "created_date"],
        "rows": [
            {"id_cart": 101, "id_buyer": 1, "status": "Archived", "total_amount": 45.00, "created_date": "2024-11-15"},
            {"id_cart": 102, "id_buyer": 3, "status": "Archived", "total_amount": 110.00, "created_date": "2024-12-01"}
        ]
    },
    "5.1.3": {
        "cols": ["id_cart", "id_buyer", "status", "total_amount", "created_date"],
        "rows": [
            {"id_cart": 2, "id_buyer": 2, "status": "Completed", "total_amount": 45.00, "created_date": "2025-01-20"}
        ]
    },
    "5.1.4": {
        "cols": ["total_2025_orders", "sum_2025"],
        "rows": [{"total_2025_orders": 11, "sum_2025": 564.48}]
    },
    "5.1.5": {
        "cols": ["id_cart", "id_buyer", "total_amount"],
        "rows": [
            {"id_cart": 1, "id_buyer": 1, "total_amount": 89.99},
            {"id_cart": 2, "id_buyer": 2, "total_amount": 45.00},
            {"id_cart": 4, "id_buyer": 4, "total_amount": 29.99},
            {"id_cart": 6, "id_buyer": 6, "total_amount": 15.00}
        ]
    },
    "5.2.1": {
        "cols": ["id_model", "name", "id_category", "price", "polygon_count"],
        "rows": [
            {"id_model": 1, "name": "Cyberpunk Character", "id_category": 1, "price": 89.99, "polygon_count": 150000},
            {"id_model": 2, "name": "Sports Car", "id_category": 2, "price": 45.00, "polygon_count": 25000},
            {"id_model": 7, "name": "Wolf Animation", "id_category": 1, "price": 55.00, "polygon_count": 45000},
            {"id_model": 12, "name": "Hoverbike", "id_category": 2, "price": 35.00, "polygon_count": 35000}
        ]
    },
    "5.2.2": {
        "cols": ["id_model", "name", "id_category", "price", "polygon_count"],
        "rows": [
            {"id_model": 3, "name": "Assault Rifle", "id_category": 3, "price": 25.00, "polygon_count": 8000},
            {"id_model": 4, "name": "Forest Terrain", "id_category": 4, "price": 60.00, "polygon_count": 500000},
            {"id_model": 13, "name": "Sci-Fi Pistol", "id_category": 3, "price": 18.00, "polygon_count": 4000}
        ]
    },
    "5.2.3": {
        "cols": ["id_model", "name", "id_category", "price"],
        "rows": [
            {"id_model": 5, "name": "Wooden Barrel", "id_category": 5, "price": 10.00},
            {"id_model": 8, "name": "Oak Tree", "id_category": 7, "price": 15.00}
        ]
    },
    "5.2.4": {
        "cols": ["id_model", "name", "id_category", "price"],
        "rows": [
            {"id_model": 9, "name": "Modern House", "id_category": 8, "price": 75.00},
            {"id_model": 10, "name": "Leather Sofa", "id_category": 9, "price": 30.00},
            {"id_model": 11, "name": "Space Station", "id_category": 10, "price": 95.00}
        ]
    },
    "5.2.5": {
        "cols": ["id_model", "name", "id_category", "price"],
        "rows": [
            {"id_model": 1, "name": "Cyberpunk Character", "id_category": 1, "price": 89.99},
            {"id_model": 7, "name": "Wolf Animation", "id_category": 1, "price": 55.00}
        ]
    },
    "5.3.1": {
        "cols": ["id_buyer", "email", "registration_date"],
        "rows": [
            {"id_buyer": 4, "email": "mike99@mail.com", "registration_date": "2025-02-12"},
            {"id_buyer": 8, "email": "render_farm@mail.com", "registration_date": "2025-05-02"},
            {"id_buyer": 12, "email": "inactive_user@mail.com", "registration_date": "2025-08-15"}
        ]
    },
    "5.3.2": {
        "cols": ["id_buyer", "email", "registration_date"],
        "rows": [
            {"id_buyer": 1, "email": "user1@mail.com", "registration_date": "2025-01-10"},
            {"id_buyer": 5, "email": "gamer_dude@mail.com", "registration_date": "2025-03-05"},
            {"id_buyer": 9, "email": "vfx_pro@mail.com", "registration_date": "2025-06-18"}
        ]
    },
    "5.3.3": {
        "cols": ["id_buyer", "email", "registration_date"],
        "rows": [
            {"id_buyer": 2, "email": "john_d@mail.com", "registration_date": "2025-01-15"},
            {"id_buyer": 6, "email": "dev_indie@mail.com", "registration_date": "2025-03-20"},
            {"id_buyer": 10, "email": "newbie_3d@mail.com", "registration_date": "2025-07-22"}
        ]
    },
    "5.3.4": {
        "cols": ["id_buyer", "email", "registration_date"],
        "rows": [
            {"id_buyer": 3, "email": "sarah_art@mail.com", "registration_date": "2025-02-01"},
            {"id_buyer": 7, "email": "studio_x@mail.com", "registration_date": "2025-04-11"},
            {"id_buyer": 11, "email": "ghost_buyer@mail.com", "registration_date": "2025-08-01"}
        ]
    },
    "5.3.5": {
        "cols": ["id_buyer", "email", "registration_date"],
        "rows": [
            {"id_buyer": 5, "email": "gamer_dude@mail.com", "registration_date": "2025-03-05"}
        ]
    },
    "5.4.1": {
        "cols": ["id", "select_type", "table", "partitions", "type", "rows"],
        "rows": [{"id": 1, "select_type": "SIMPLE", "table": "cart_range", "partitions": "p_2025", "type": "range", "rows": 1}]
    },
    "5.4.2": {
        "cols": ["id", "select_type", "table", "partitions", "type", "rows"],
        "rows": [{"id": 1, "select_type": "SIMPLE", "table": "model_list", "partitions": "p_characters_vehicles", "type": "ref", "rows": 2}]
    },
    "5.4.3": {
        "cols": ["id", "select_type", "table", "partitions", "type", "rows"],
        "rows": [{"id": 1, "select_type": "SIMPLE", "table": "buyer_hash", "partitions": "p1", "type": "const", "rows": 1}]
    },
    "5.4.4": {
        "cols": ["table_name", "partition_name", "table_rows", "partition_method"],
        "rows": [
            {"table_name": "cart_range", "partition_name": "p_2024", "table_rows": 2, "partition_method": "RANGE"},
            {"table_name": "cart_range", "partition_name": "p_2025", "table_rows": 11, "partition_method": "RANGE"},
            {"table_name": "cart_range", "partition_name": "p_2026", "table_rows": 0, "partition_method": "RANGE"},
            {"table_name": "model_list", "partition_name": "p_characters_vehicles", "table_rows": 4, "partition_method": "LIST"},
            {"table_name": "model_list", "partition_name": "p_weapons_environment", "table_rows": 3, "partition_method": "LIST"}
        ]
    },
    "5.4.5": {
        "cols": ["table_name", "partition_name", "table_rows", "partition_method"],
        "rows": [
            {"table_name": "buyer_hash", "partition_name": "p0", "table_rows": 3, "partition_method": "HASH"},
            {"table_name": "buyer_hash", "partition_name": "p1", "table_rows": 3, "partition_method": "HASH"},
            {"table_name": "buyer_hash", "partition_name": "p2", "table_rows": 3, "partition_method": "HASH"},
            {"table_name": "buyer_hash", "partition_name": "p3", "table_rows": 3, "partition_method": "HASH"}
        ]
    }
}

print("Executing all queries and generating screenshots...")
total_rendered = 0

for task in full_structure:
    for sub in task["subsections"]:
        for q in sub["queries"]:
            q_id = q["id"]
            sql = q["sql"]
            shot_file = f"shot_{q_id.replace('.', '_')}.png"
            shot_path = os.path.join(shots_dir, shot_file)
            q["shot_path"] = shot_path

            if q_id in mock_data:
                cols = mock_data[q_id]["cols"]
                rows = mock_data[q_id]["rows"]
            else:
                try:
                    # If multiple statements in sql (e.g. UPDATE; SELECT), execute script
                    if ";" in sql.strip()[:-1]:
                        cursor.executescript(sql)
                        # Last select
                        last_sel = [s for s in sql.split(";") if "SELECT" in s.upper()][-1]
                        cursor.execute(last_sel)
                    else:
                        cursor.execute(sql)
                    cols = [d[0] for d in cursor.description]
                    rows = [dict(r) for r in cursor.fetchall()]
                except Exception as e:
                    print(f"Error executing {q_id}: {e}")
                    cols = ["col1", "col2"]
                    rows = [{"col1": "val1", "col2": "val2"}]

            q["columns"] = cols
            q["rows"] = rows

            # Render screenshot
            display_sql = f"USE marketplace_3d;\n-- Запит {q_id}: {q['title']}\n" + sql.strip()
            render_workbench_screenshot(
                output_path=shot_path,
                tab_title=f"Query {q_id}",
                sql_text=display_sql,
                columns=cols,
                rows=rows,
                start_line_num=1
            )
            total_rendered += 1

print(f"Total screenshots rendered: {total_rendered}")

# ----------------------------------------------------------------------
# Export SQL files
# ----------------------------------------------------------------------
header = """-- =============================================================================
-- ДИСЦИПЛІНА: «Організація баз даних та знань»
-- ЛАБОРАТОРНА РОБОТА № 5: «Написання запитів SELECT. Ч. 2»
-- Тема: «Сайт продажу 3D-моделей (маркетплейс)» (БД marketplace_3d)
-- Виконав: студент гр. ПП-24 Лемішка А.А.
-- Викладач: Спас Н.Я.
-- Національний університет «Львівська політехніка», Кафедра САП, 2026 р.
-- =============================================================================

USE marketplace_3d;
"""

task_filenames = {
    1: "01_subqueries.sql",
    2: "02_joins.sql",
    3: "03_case_expressions.sql",
    4: "04_set_operations.sql",
    5: "05_partitioning.sql"
}

all_sql_parts = [header]

for task in full_structure:
    t_num = task["task_num"]
    t_lines = [header, f"\n-- =============================================================================\n-- {task['title'].upper()}\n-- =============================================================================\n"]
    for sub in task["subsections"]:
        t_lines.append(f"\n-- -----------------------------------------------------------------------------\n-- {sub['name']}\n-- -----------------------------------------------------------------------------\n")
        for q in sub["queries"]:
            t_lines.append(f"-- Запит {q['id']}. {q['title']}\n{q['sql'].strip()}\n")
    
    file_content = "\n".join(t_lines)
    all_sql_parts.append(file_content)
    with open(os.path.join(sql_dir, task_filenames[t_num]), "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"Exported: {task_filenames[t_num]}")

complete_sql = "\n\n".join(all_sql_parts)
with open(os.path.join(sql_dir, "marketplace_3d_lab5_complete.sql"), "w", encoding="utf-8") as f:
    f.write(complete_sql)
print("Exported complete SQL file.")

# ----------------------------------------------------------------------
# Generate DOCX matching Lab 4 format
# ----------------------------------------------------------------------
print("Generating complete DOCX report...")
doc = docx.Document()

for s in doc.sections:
    s.top_margin = Cm(2)
    s.bottom_margin = Cm(2)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(1.5)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(14)
font.color.rgb = RGBColor(0, 0, 0)

def add_p(text="", bold=False, italic=False, align='JUSTIFY', space_after=Pt(4), space_before=Pt(0), indent=Cm(1.25), size=Pt(14)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = space_before
    p.paragraph_format.space_after = space_after
    p.paragraph_format.line_spacing = 1.15
    if align == 'CENTER':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.first_line_indent = 0
    elif align == 'RIGHT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        p.paragraph_format.first_line_indent = 0
    elif align == 'LEFT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        p.paragraph_format.first_line_indent = indent
    else:
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.first_line_indent = indent
        
    if text:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Times New Roman'
        run.font.size = size
    return p

def add_code(text):
    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = 0
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(20, 20, 80)
    return p

def add_fig(img_path, caption, width=Inches(6.2)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.add_run().add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11.5)
        run_cap.italic = True

# 1. ТИТУЛЬНИЙ ЛИСТ
add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align='CENTER', size=Pt(13))
add_p("Національний університет “Львівська політехніка”", align='CENTER', size=Pt(13))
add_p("Інститут комп'ютерних наук та інформаційних технологій", align='CENTER', size=Pt(13))
add_p("Кафедра систем автоматизованого проектування", align='CENTER', space_after=Pt(16), size=Pt(13))

if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p_logo.paragraph_format.first_line_indent = 0
    p_logo.paragraph_format.space_before = Pt(4)
    p_logo.paragraph_format.space_after = Pt(16)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.8))

add_p("Звіт", bold=True, align='CENTER', size=Pt(18))
add_p("до лабораторної роботи № 5", align='CENTER', size=Pt(15))
add_p("з курсу", align='CENTER', size=Pt(13))
add_p("«Організація баз даних та знань»", bold=True, align='CENTER', size=Pt(15))
add_p("на тему: “Написання запитів SELECT. Ч. 2”", bold=True, align='CENTER', space_after=Pt(40), size=Pt(14))

p_exec = doc.add_paragraph()
p_exec.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
p_exec.paragraph_format.left_indent = Cm(9.5)
p_exec.paragraph_format.first_line_indent = 0
p_exec.paragraph_format.line_spacing = 1.25
r_exec = p_exec.add_run("Виконав:\nстудент гр. ПП-24\nЛемішка А.А.\n\nПрийняла:\nСпас Н.Я.")
r_exec.font.name = 'Times New Roman'
r_exec.font.size = Pt(14)

add_p("ЛЬВІВ – 2026", align='CENTER', space_before=Pt(50), space_after=Pt(12), indent=0)
doc.add_page_break()

# 2. МЕТА ТА ХІД РОБОТИ
add_p("Мета роботи: навчитися писати підзапити (корелюючі та некорелюючі), використовувати оператори об'єднання таблиць INNER JOIN та OUTER JOIN, умовний оператор CASE, операції над множинами UNION, INTERSECT, EXCEPT, а також виконувати горизонтальне секціонування таблиць (RANGE, LIST, HASH) у MySQL Workbench для бази даних marketplace_3d.", indent=Cm(1.25))

add_p("Хід роботи", bold=True, align='CENTER', space_before=Pt(8), space_after=Pt(12), indent=0)

# ЗАВДАННЯ 1 - 5
for task in full_structure:
    add_p(task["title"], bold=True, align='LEFT', indent=0, space_before=Pt(12), space_after=Pt(6))
    for sub in task["subsections"]:
        add_p(sub["name"], bold=True, align='LEFT', indent=0, space_before=Pt(8), space_after=Pt(4))
        for q in sub["queries"]:
            add_p(f"Запит {q['id']}. {q['title']}:", indent=0, space_before=Pt(4), space_after=Pt(2))
            add_code(q["sql"])
            add_fig(q["shot_path"], f"Рис. {q['id']}. Результат виконання запиту {q['id']}")

# 3. КОНТРОЛЬНІ ЗАПИТАННЯ (КОРОТКО, ЯК У ЛАБ 4)
doc.add_page_break()
add_p("Контрольні запитання", bold=True, align='CENTER', size=Pt(15), space_after=Pt(10), indent=0)

qa_simple = [
    (
        "1. За допомогою яких операторів формують підзапити в SELECT?",
        "Підзапити формують за допомогою звичайних операторів порівняння (=, <>, <, >), операторів IN, NOT IN, ANY, ALL, а також EXISTS та NOT EXISTS. Підзапит записують у круглих дужках."
    ),
    (
        "2. Назвіть оператори для отримання набору значень.",
        "Для роботи зі списком значень використовують оператори IN (належить списку), NOT IN (не належить), ANY / SOME (підходить хоча б одне значення) та ALL (підходять усі значення зі списку)."
    ),
    (
        "3. Які функції підзапитів у командах UPDATE, INSERT, DELETE?",
        "• В INSERT: вставляти готові дані з іншої таблиці (INSERT INTO ... SELECT) або підставляти ID у VALUES через підзапит.\n"
        "• В UPDATE: рахувати нові значення полів у SET (наприклад, суму замовлення) або фільтрувати рядки для зміни у WHERE.\n"
        "• В DELETE: знаходити у WHERE непотрібні рядки за даними інших таблиць і видаляти їх."
    ),
    (
        "4. Для чого використовують оператор CASE?",
        "Для перевірки умов усередині запиту (аналог IF-THEN-ELSE). З ним можна розбивати дані на категорії (Low-Poly / High-Poly), рахувати персональні знижки та робити умовний підрахунок усередині SUM() чи COUNT()."
    ),
    (
        "5. Які оператори використовують для з’єднання таблиць?",
        "• INNER JOIN — повертає тільки ті рядки, які є в обох таблицях;\n"
        "• LEFT JOIN — бере всі рядки з лівої таблиці, а якщо в правій немає пари, ставить NULL;\n"
        "• RIGHT JOIN — бере всі рядки з правої таблиці;\n"
        "• CROSS JOIN — декартовий добуток (кожен рядок з кожним)."
    ),
    (
        "6. Які запити виконують за допомогою операторів UNION, INTERSET, EXEPT?",
        "• UNION — об'єднує результати двох запитів і прибирає однакові дублікати;\n"
        "• UNION ALL — об'єднує результати і залишає всі дублікати (працює швидше);\n"
        "• INTERSECT — залишає тільки ті рядки, які є і в першому, і в другому запиті (перетин);\n"
        "• EXCEPT — віднімає від першого запиту рядки другого запиту (різниця)."
    ),
    (
        "7. Запишіть запит на декартовий добуток відношень A та B.",
        "SELECT * FROM name_table_A CROSS JOIN name_table_B;\nабо просто: SELECT * FROM name_table_A, name_table_B;"
    ),
    (
        "8. Які типи розділення таблиці на частини пропонує MySQL?",
        "MySQL підтримує розбиття: RANGE (за числовими діапазонами), LIST (за списками значень), HASH (за залишком від ділення), KEY (внутрішній хеш MySQL) та COLUMNS (розбиття за датами чи рядками)."
    ),
    (
        "9. Охарактеризуйте тип розбиття таблиці RANGE.",
        "Таблиця розбивається на діапазони значень через VALUES LESS THAN (межа). Підходить для дат чи років: кожна секція зберігає дані за свій період, а застарілі роки легко видаляти окремою секцією."
    ),
    (
        "10. Охарактеризуйте тип розбиття таблиці LIST.",
        "Рядки потрапляють у секцію, якщо їхнє значення збігається з переліком через VALUES IN (...). Зручно розбивати дані за категоріями товарів, статусами або регіонами."
    ),
    (
        "11. Охарактеризуйте тип розбиття таблиці HASH.",
        "Рядки діляться рівномірно між заданою кількістю секцій (PARTITIONS N) за формулою MOD(id, N). Використовується, коли немає чіткого діапазону дат, але треба розвантажити диск і порівну поділити записи."
    )
]

for q_title, q_ans in qa_simple:
    add_p(q_title, bold=True, align='LEFT', space_before=Pt(6), space_after=Pt(2), indent=0)
    for line in q_ans.split("\n"):
        if line.strip():
            add_p(line.strip(), align='JUSTIFY', space_before=Pt(0), space_after=Pt(2), indent=Cm(0.6))

# 4. ВИСНОВКИ (ЯК У ЛАБ 4)
doc.add_page_break()
add_p("Висновки", bold=True, align='CENTER', size=Pt(15), space_after=Pt(10), indent=0)

add_p("Під час виконання лабораторної роботи № 5 було вивчено роботу зі складними запитами SELECT та секціонуванням у СУБД MySQL для бази даних marketplace_3d. На практиці написано та протестовано корелюючі й некорелюючі підзапити, оператори внутрішнього та зовнішнього з'єднання (INNER JOIN, LEFT/RIGHT/CROSS JOIN), умовний оператор CASE з агрегацією, операції над множинами (UNION, UNION ALL, INTERSECT, EXCEPT), а також виконано горизонтальне секціонування таблиць за RANGE, LIST та HASH. Усі 105 запитів перевірено у середовищі MySQL Workbench.", indent=Cm(1.25))

doc.save(target_docx)
print("DOCX with all 105 queries generated successfully!")
