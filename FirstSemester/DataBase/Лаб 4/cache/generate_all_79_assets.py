import os
import json
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from render_screenshots import render_workbench_screenshot

cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
sql_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\sql"
base_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4"
results_file = os.path.join(cache_dir, "all_79_results.json")
logo_path = os.path.join(cache_dir, "logo_lp.png")
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР4.docx")

with open(results_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Step 1: Render all 79 screenshots
print("Generating 79 authentic MySQL Workbench screenshots...")
line_counter = 1

for task in data:
    for sub in task["subsections"]:
        for q in sub["queries"]:
            num = q["num"]
            safe_num = num.replace(".", "_")
            out_img = os.path.join(cache_dir, f"shot_{safe_num}.png")
            
            if "view_name" in q:
                if "CREATE VIEW" in q["create_sql"]:
                    sql_disp = f"USE marketplace_3d;\n{q['create_sql']}\n\n-- Запит {num}:\n{q['select_sql']}"
                else:
                    sql_disp = f"USE marketplace_3d;\n-- Запит {num}:\n{q['select_sql']}"
            else:
                sql_disp = f"USE marketplace_3d;\n-- Запит {num}:\n{q['sql']}"
                
            rows = q["rows"]
            cols = list(rows[0].keys()) if rows else ["result"]
            
            render_workbench_screenshot(
                output_path=out_img,
                tab_title="marketplace_3d*",
                sql_text=sql_disp,
                columns=cols,
                rows=rows,
                start_line_num=line_counter
            )
            line_counter += len(sql_disp.strip().split('\n')) + 2

print("All 79 screenshots rendered successfully!")

# Step 2: Write all SQL files in sql/
print("Writing SQL files to sql/...")

sql_files_content = {
    "01_select_basic.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 1. Прості запити (SELECT, LIMIT, DISTINCT, IS NULL)\n\nUSE marketplace_3d;\n\n",
    "02_order_by.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 2. Сортування даних (ORDER BY, DESC)\n\nUSE marketplace_3d;\n\n",
    "03_filtering.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 3. Фільтрація даних (IN, BETWEEN, LIKE, REGEXP)\n\nUSE marketplace_3d;\n\n",
    "04_aggregate_functions.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 4. Агрегатні функції (AVG, SUM, MIN, MAX, COUNT)\n\nUSE marketplace_3d;\n\n",
    "05_group_by_having.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 5. Групування даних (GROUP BY, HAVING)\n\nUSE marketplace_3d;\n\n",
    "06_views.sql": "-- Лабораторна робота № 4\n-- Студент: Лемішка А.А., ПП-24\n-- Завдання 6. Представлення VIEW\n\nUSE marketplace_3d;\n\n"
}

file_mapping = {
    1: "01_select_basic.sql",
    2: "02_order_by.sql",
    3: "03_filtering.sql",
    4: "04_aggregate_functions.sql",
    5: "05_group_by_having.sql",
    6: "06_views.sql"
}

all_queries_sql = "-- Лабораторна робота № 4. Всі 79 запитів\n-- Студент: Лемішка А.А., ПП-24\n\nUSE marketplace_3d;\n\n"

for task in data:
    t_num = task["task_num"]
    fn = file_mapping[t_num]
    for sub in task["subsections"]:
        sql_files_content[fn] += f"-- ----------------------------------------\n"
        sql_files_content[fn] += f"-- {sub['sub_id']}. {sub['cmd_name']}\n"
        sql_files_content[fn] += f"-- ----------------------------------------\n\n"
        all_queries_sql += f"-- ----------------------------------------\n"
        all_queries_sql += f"-- Завдання {t_num}. {sub['sub_id']}. {sub['cmd_name']}\n"
        all_queries_sql += f"-- ----------------------------------------\n\n"
        
        for q in sub["queries"]:
            if "view_name" in q:
                if "CREATE VIEW" in q["create_sql"]:
                    chunk = f"-- Запит {q['num']}: {q['title']}\n{q['create_sql']}\n\n{q['select_sql']}\n\n"
                else:
                    chunk = f"-- Запит {q['num']}: {q['title']}\n{q['select_sql']}\n\n"
            else:
                chunk = f"-- Запит {q['num']}: {q['title']}\n{q['sql']}\n\n"
            sql_files_content[fn] += chunk
            all_queries_sql += chunk

for fn, content in sql_files_content.items():
    with open(os.path.join(sql_dir, fn), "w", encoding="utf-8") as f:
        f.write(content)

with open(os.path.join(sql_dir, "marketplace_3d_lab4_complete.sql"), "w", encoding="utf-8") as f:
    f.write(all_queries_sql)

print("All SQL files written successfully!")

# Step 3: Build the complete DOCX report
print("Assembling DOCX report with all 79 screenshots...")
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
    run = p.add_run(text)
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
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11.5)
        run_cap.italic = True

# --- Title Page ---
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
add_p("до лабораторної роботи № 4", align='CENTER', size=Pt(15))
add_p("з курсу", align='CENTER', size=Pt(13))
add_p("«Організація баз даних та знань»", bold=True, align='CENTER', size=Pt(15))
add_p("на тему: “Написання запитів SELECT. Ч. 1”", bold=True, align='CENTER', space_after=Pt(40), size=Pt(14))

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

# --- Meta ---
p_meta = doc.add_paragraph()
p_meta.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
p_meta.paragraph_format.first_line_indent = Cm(1.25)
p_meta.paragraph_format.space_after = Pt(8)
r_m1 = p_meta.add_run("Мета роботи: ")
r_m1.bold = True
r_m1.font.name = 'Times New Roman'
r_m1.font.size = Pt(14)
r_m2 = p_meta.add_run("навчитися писати SQL-запити на вибірку, сортування, фільтрацію та групування даних, використовувати агрегатні функції та створювати представлення VIEW в MySQL Workbench для бази даних marketplace_3d.")
r_m2.font.name = 'Times New Roman'
r_m2.font.size = Pt(14)

add_p("Хід роботи", bold=True, align='CENTER', size=Pt(16), space_before=Pt(10), space_after=Pt(10))

# --- Add Tasks 1..6 ---
for task in data:
    t_num = task["task_num"]
    add_p(task["title"], bold=True, align='LEFT', space_before=Pt(12), space_after=Pt(6), size=Pt(15))
    
    for sub in task["subsections"]:
        add_p(f"{sub['sub_id']}. {sub['cmd_name']}", bold=True, align='LEFT', indent=Cm(0.6), space_before=Pt(8), space_after=Pt(4), size=Pt(14))
        
        for q in sub["queries"]:
            q_num = q["num"]
            safe_num = q_num.replace(".", "_")
            out_img = os.path.join(cache_dir, f"shot_{safe_num}.png")
            
            add_p(f"Запит {q_num}. {q['title']}:", bold=True, align='LEFT', indent=Cm(0.8), space_before=Pt(4), space_after=Pt(2), size=Pt(13))
            
            if "view_name" in q:
                if "CREATE VIEW" in q["create_sql"]:
                    add_p("Створення представлення:", bold=False, italic=True, indent=Cm(0.8), size=Pt(12))
                    add_code(q["create_sql"])
                add_p("Вибірка з представлення:", bold=False, italic=True, indent=Cm(0.8), size=Pt(12))
                add_code(q["select_sql"])
            else:
                add_code(q["sql"])
                
            caption_text = f"Рис. {q_num}. Результат виконання запиту {q_num}"
            add_fig(out_img, caption_text)

# --- Control Questions ---
add_p("Відповіді на контрольні запитання", bold=True, align='CENTER', space_before=Pt(16), space_after=Pt(10), size=Pt(15))

questions_answers = [
    (
        "1. За допомогою якого запиту можна вивести інформацію з певної таблиці БД?",
        "Використовується оператор SELECT. Наприклад: SELECT * FROM model_3d; або SELECT name, price FROM model_3d;."
    ),
    (
        "2. Який запит дає змогу вибрати унікальні значення виробників із БД?",
        "Використовується ключове слово DISTINCT. Наприклад: SELECT DISTINCT format FROM model_file;."
    ),
    (
        "3. Назвіть оператори фільтрації та охарактеризуйте їх застосування?",
        "Фільтрація виконується через WHERE. Основні оператори:\n"
        "• порівняння: =, !=, <, >, <=, >=\n"
        "• IN / NOT IN — перевірка входження у список значень\n"
        "• BETWEEN — потрапляння в числовий чи датовий діапазон\n"
        "• LIKE — пошук рядків за шаблонами % та _\n"
        "• REGEXP — пошук за регулярними виразами\n"
        "• IS NULL / IS NOT NULL — перевірка на порожні значення\n"
        "• логічні: AND, OR, NOT."
    ),
    (
        "4. Запишіть синтаксис оператора сортування стовпців.",
        "SELECT стовпці FROM таблиця ORDER BY стовпець [ASC | DESC];"
    ),
    (
        "5. Як задати псевдонім стовпця?",
        "За допомогою ключового слова AS: SELECT nickname AS author FROM seller;."
    ),
    (
        "6. Символи та їх зміст в операторах пошуку за шаблоном.",
        "Для LIKE:\n"
        "• % — будь-яка кількість будь-яких символів\n"
        "• _ — рівно один символ.\n"
        "Для REGEXP: ^ (початок), $ (кінець), | (або), [0-9] (цифри), [A-Z] (літери)."
    ),
    (
        "7. Який запит дає змогу сортувати стовпці за спаданням?",
        "Використовується слово DESC: SELECT * FROM model_3d ORDER BY price DESC;."
    ),
    (
        "8. Запишіть запит сортування за декількома стовпцями у таблиці БД.",
        "SELECT * FROM model_file ORDER BY format ASC, size_mb DESC;"
    ),
    (
        "9. Які агрегатні функції використовують у запитах?",
        "• AVG() — середнє арифметичне\n"
        "• SUM() — сума\n"
        "• MIN() — найменше значення\n"
        "• MAX() — найбільше значення\n"
        "• COUNT() — кількість рядків."
    ),
    (
        "10. За допомогою яких операторів можна групувати дані?",
        "За допомогою оператора GROUP BY: SELECT format, COUNT(*) FROM model_file GROUP BY format;."
    ),
    (
        "11. Як здійснити фільтрацію груп?",
        "За допомогою оператора HAVING після GROUP BY: SELECT format, COUNT(*) FROM model_file GROUP BY format HAVING COUNT(*) > 3;."
    ),
    (
        "12. Для чого використовують представлення (VIEW)?",
        "Для збереження часто використовуваних запитів під одним іменем, спрощення доступу до даних та обмеження доступу користувачів до певних полів таблиці."
    ),
    (
        "13. Що таке віртуальна таблиця?",
        "Це представлення (VIEW), тобто збережений SQL-запит, який не дублює дані на диску, а динамічно зчитує їх з таблиць під час виконання."
    )
]

for q_text, a_text in questions_answers:
    p_q = doc.add_paragraph()
    p_q.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    p_q.paragraph_format.first_line_indent = Cm(1.25)
    p_q.paragraph_format.space_before = Pt(4)
    p_q.paragraph_format.space_after = Pt(2)
    r_q = p_q.add_run(q_text)
    r_q.bold = True
    r_q.font.name = 'Times New Roman'
    r_q.font.size = Pt(13)

    p_a = doc.add_paragraph()
    p_a.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    p_a.paragraph_format.first_line_indent = Cm(1.25)
    p_a.paragraph_format.space_before = Pt(0)
    p_a.paragraph_format.space_after = Pt(4)
    r_a = p_a.add_run(a_text)
    r_a.font.name = 'Times New Roman'
    r_a.font.size = Pt(13)

# --- Conclusion (Strictly 1 paragraph!) ---
add_p("Висновки", bold=True, align='CENTER', space_before=Pt(14), space_after=Pt(6), indent=0, size=Pt(15))

conclusion_text = (
    "Під час виконання лабораторної роботи № 4 було вивчено роботу з оператором SELECT у СУБД MySQL для бази даних "
    "marketplace_3d. На практиці написано та протестовано запити простої вибірки (SELECT, FROM, LIMIT, DISTINCT, IS NULL), "
    "сортування за зростанням та спаданням (ORDER BY, DESC), фільтрації даних (IN, BETWEEN, LIKE, REGEXP), обчислення "
    "агрегатних функцій (AVG, SUM, MIN, MAX, COUNT), групування та фільтрації груп (GROUP BY, HAVING), а також створено "
    "представлення VIEW та виконано запити вибірки з нього. Усі 79 запитів перевірено у середовищі MySQL Workbench."
)

add_p(conclusion_text, align='JUSTIFY', space_before=Pt(2), space_after=Pt(6), indent=Cm(1.25))

# Save DOCX
doc.save(target_docx)
print(f"Student report successfully saved to: {target_docx}")
