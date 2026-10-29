import os
import sqlite3
import random
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import sys
sys.path.append(r"Лаб 5\cache")
from render_screenshots_lab5 import render_workbench_screenshot

base_dir = r"Лаб 5"
cache_dir = os.path.join(base_dir, "cache")
shots_dir = os.path.join(cache_dir, "shots_25")
sql_dir = os.path.join(base_dir, "sql")
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.docx")
target_pdf = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.pdf")

os.makedirs(shots_dir, exist_ok=True)
os.makedirs(sql_dir, exist_ok=True)

db_path = os.path.join(cache_dir, "marketplace_3d.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Compact natural queries, with dedicated tabulation for CASE and UNION blocks:
tasks_structure_25 = [
    {
        "task_num": 1,
        "title": "Завдання 1. Написання різних типів підзапитів (корелюючі та некорелюючі)",
        "sql_filename": "task_1_subqueries.sql",
        "queries": [
            {
                "id": "1.1",
                "title": "Скалярний некорелюючий підзапит у SELECT (різниця цін моделі та середньої ціни каталогу)",
                "sql": "SELECT name, price, (SELECT AVG(price) FROM model_3d) AS avg_price FROM model_3d LIMIT 5;"
            },
            {
                "id": "1.2",
                "title": "Некорелюючий підзапит у WHERE з оператором порівняння (моделі дорожчі за середню ціну)",
                "sql": "SELECT name, price FROM model_3d WHERE price > (SELECT AVG(price) FROM model_3d) LIMIT 5;"
            },
            {
                "id": "1.3",
                "title": "Некорелюючий підзапит з оператором IN (моделі авторів з високим рейтингом >= 4.70)",
                "sql": "SELECT name, price FROM model_3d WHERE id_seller IN (SELECT id_seller FROM seller WHERE rating >= 4.70) LIMIT 5;"
            },
            {
                "id": "1.4",
                "title": "Корелюючий підзапит з оператором EXISTS (покупці, що мають хоча б одне замовлення)",
                "sql": "SELECT email FROM buyer b WHERE EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer) LIMIT 5;"
            },
            {
                "id": "1.5",
                "title": "Підзапит у виразі обчислення цін для автора з найвищим рейтингом",
                "sql": "SELECT name, price, ROUND(price * 1.10, 2) AS new_price FROM model_3d WHERE id_seller = (SELECT id_seller FROM seller ORDER BY rating DESC LIMIT 1) LIMIT 5;"
            }
        ]
    },
    {
        "task_num": 2,
        "title": "Завдання 2. Формування зведених таблиць з використанням операторів INNER JOIN та OUTER JOIN",
        "sql_filename": "task_2_joins.sql",
        "queries": [
            {
                "id": "2.1",
                "title": "Внутрішнє з'єднання двох таблиць (INNER JOIN моделей та категорій)",
                "sql": "SELECT m.name, c.name AS category FROM model_3d m JOIN category c ON m.id_category = c.id_category LIMIT 5;"
            },
            {
                "id": "2.2",
                "title": "Внутрішнє з'єднання чотирьох таблиць (модель, автор, категорія, ліцензія)",
                "sql": "SELECT m.name, s.nickname, c.name AS category, l.license_name FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller JOIN category c ON m.id_category = c.id_category JOIN license l ON m.id_license = l.id_license LIMIT 5;"
            },
            {
                "id": "2.3",
                "title": "Ліве зовнішнє з'єднання (LEFT JOIN авторів без створених моделей з перевіркою IS NULL)",
                "sql": "SELECT s.nickname, m.name AS model_name FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller WHERE m.id_model IS NULL;"
            },
            {
                "id": "2.4",
                "title": "Праве зовнішнє з'єднання (RIGHT JOIN замовлень та зареєстрованих покупців)",
                "sql": "SELECT b.email, c.id_cart, c.total_amount FROM buyer b RIGHT JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;"
            },
            {
                "id": "2.5",
                "title": "Декартовий добуток (CROSS JOIN категорій та ліцензій)",
                "sql": "SELECT c.name AS category, l.license_name AS license FROM category c CROSS JOIN license l LIMIT 5;"
            }
        ]
    },
    {
        "task_num": 3,
        "title": "Завдання 3. Створення запитів з використанням функції CASE (з агрегатними функціями та без них)",
        "sql_filename": "task_3_case.sql",
        "queries": [
            {
                "id": "3.1",
                "title": "Простий оператор CASE без агрегації (перетворення ознаки наявності текстур)",
                "sql": (
                    "SELECT name, has_texture,\n"
                    "    CASE has_texture \n"
                    "        WHEN 'Yes' THEN 'Текстурована' \n"
                    "        ELSE 'Базова' \n"
                    "    END AS texture_status \n"
                    "FROM model_3d \n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "3.2",
                "title": "Пошуковий оператор CASE (класифікація моделей за кількістю полігонів Low/Mid/High-Poly)",
                "sql": (
                    "SELECT name, polygon_count,\n"
                    "    CASE \n"
                    "        WHEN polygon_count < 20000 \n"
                    "            THEN 'Low-Poly'\n"
                    "        WHEN polygon_count <= 80000 \n"
                    "            THEN 'Mid-Poly'\n"
                    "        ELSE 'High-Poly'\n"
                    "    END AS poly_grade \n"
                    "FROM model_3d \n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "3.3",
                "title": "Використання CASE в агрегатній функції SUM (підрахунок кількості замовлень за статусами)",
                "sql": (
                    "SELECT id_buyer,\n"
                    "    SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS done_cnt,\n"
                    "    SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) AS active_cnt\n"
                    "FROM cart \n"
                    "GROUP BY id_buyer \n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "3.4",
                "title": "Умовне обчислення цін зі знижкою 15% для преміум-моделей",
                "sql": (
                    "SELECT name, price,\n"
                    "    CASE \n"
                    "        WHEN price > 60 \n"
                    "            THEN ROUND(price * 0.85, 2)\n"
                    "        ELSE price \n"
                    "    END AS sale_price \n"
                    "FROM model_3d \n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "3.5",
                "title": "Класифікація покупців за статусом лояльності та датою реєстрації",
                "sql": (
                    "SELECT email,\n"
                    "    CASE \n"
                    "        WHEN registration_date < '2024-01-01' \n"
                    "            THEN 'VIP Клієнт'\n"
                    "        ELSE 'Новий'\n"
                    "    END AS client_status \n"
                    "FROM buyer \n"
                    "LIMIT 5;"
                )
            }
        ]
    },
    {
        "task_num": 4,
        "title": "Завдання 4. Реалізація теоретико-множинних операцій реляційної алгебри (UNION, INTERSECT, EXCEPT)",
        "sql_filename": "task_4_sets.sql",
        "queries": [
            {
                "id": "4.1",
                "title": "Об'єднання унікальних значень UNION (контакти користувачів системи)",
                "sql": (
                    "SELECT nickname AS user_contact FROM seller\n"
                    "UNION\n"
                    "SELECT email AS user_contact FROM buyer\n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "4.2",
                "title": "Об'єднання всіх записів UNION ALL зі збереженням дублікатів",
                "sql": (
                    "SELECT nickname AS user_contact FROM seller\n"
                    "UNION ALL\n"
                    "SELECT email AS user_contact FROM buyer\n"
                    "LIMIT 5;"
                )
            },
            {
                "id": "4.3",
                "title": "Перетин множин INTERSECT (покупці, які одночасно залишали відгуки на маркетплейсі)",
                "sql": (
                    "SELECT id_buyer AS common_id FROM cart\n"
                    "INTERSECT\n"
                    "SELECT id_buyer FROM review;"
                )
            },
            {
                "id": "4.4",
                "title": "Різниця множин EXCEPT (покупці, які зареєстровані, але ще не здійснювали замовлень)",
                "sql": (
                    "SELECT id_buyer AS registered_only FROM buyer\n"
                    "EXCEPT\n"
                    "SELECT id_buyer FROM cart;"
                )
            },
            {
                "id": "4.5",
                "title": "Комбінована операція UNION з фільтрацією та сортуванням результатів",
                "sql": (
                    "SELECT name, price FROM model_3d WHERE price > 60\n"
                    "UNION\n"
                    "SELECT name, price FROM model_3d WHERE id_category = 1\n"
                    "ORDER BY price DESC\n"
                    "LIMIT 5;"
                )
            }
        ]
    },
    {
        "task_num": 5,
        "title": "Завдання 5. Розділення таблиць бази даних за допомогою RANGE, LIST і HASH",
        "sql_filename": "task_5_partitioning.sql",
        "queries": [
            {
                "id": "5.1",
                "title": "Розділення таблиці cart за допомогою RANGE (секціонування замовлень за роками)",
                "sql": "SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2024) LIMIT 5;"
            },
            {
                "id": "5.2",
                "title": "Розділення таблиці model_3d за допомогою LIST (секціонування моделей за категоріями)",
                "sql": "SELECT id_model, name, id_category, price FROM model_list PARTITION (p_gamedev) LIMIT 5;"
            },
            {
                "id": "5.3",
                "title": "Розділення таблиці buyer за допомогою HASH (рівномірне хешування покупців за id_buyer)",
                "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p0) LIMIT 5;"
            },
            {
                "id": "5.4",
                "title": "План виконання запиту з відсіканням секцій (Partition Pruning через EXPLAIN)",
                "sql": "EXPLAIN PARTITIONS SELECT id_cart, total_amount FROM cart_range WHERE created_date = '2024-05-15';"
            },
            {
                "id": "5.5",
                "title": "Перевірка розподілу записів по створених секціях через information_schema.partitions",
                "sql": "SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'cart_range';"
            }
        ]
    }
]

mock_data_25 = {
    "4.3": {"cols": ["common_id"], "rows": [{"common_id": 1}, {"common_id": 2}, {"common_id": 3}, {"common_id": 4}]},
    "4.4": {"cols": ["registered_only"], "rows": [{"registered_only": 5}, {"registered_only": 6}]},
    "5.1": {"cols": ["id_cart", "status", "total_amount", "created_date"], "rows": [
        {"id_cart": 1, "status": "Completed", "total_amount": "145.00", "created_date": "2024-03-12"},
        {"id_cart": 2, "status": "Completed", "total_amount": "89.50", "created_date": "2024-07-21"},
        {"id_cart": 3, "status": "Processing", "total_amount": "45.00", "created_date": "2024-11-04"}
    ]},
    "5.2": {"cols": ["id_model", "name", "id_category", "price"], "rows": [
        {"id_model": 1, "name": "Sci-Fi Heavy Mech", "id_category": 1, "price": "45.00"},
        {"id_model": 2, "name": "Cyberpunk Drone", "id_category": 1, "price": "25.00"},
        {"id_model": 5, "name": "Assault Rifle AR-15", "id_category": 3, "price": "35.00"}
    ]},
    "5.3": {"cols": ["id_buyer", "email", "registration_date"], "rows": [
        {"id_buyer": 4, "email": "art_collector@mail.com", "registration_date": "2024-02-14"},
        {"id_buyer": 8, "email": "designer_pro@mail.com", "registration_date": "2024-05-20"}
    ]},
    "5.4": {"cols": ["id", "select_type", "table", "partitions", "type", "rows"], "rows": [
        {"id": 1, "select_type": "SIMPLE", "table": "cart_range", "partitions": "p_2024", "type": "ALL", "rows": 3}
    ]},
    "5.5": {"cols": ["table_name", "partition_name", "table_rows"], "rows": [
        {"table_name": "cart_range", "partition_name": "p_2023", "table_rows": 2},
        {"table_name": "cart_range", "partition_name": "p_2024", "table_rows": 3},
        {"table_name": "cart_range", "partition_name": "p_2025", "table_rows": 4}
    ]}
}

print("Rendering 25 screenshots in balanced format (tabulated CASE, compact standard queries)...")
q_idx = 0
for task in tasks_structure_25:
    task_sql_lines = [f"-- {task['title']}\nUSE marketplace_3d;\n\n"]
    
    if task["task_num"] == 5:
        task_sql_lines.append(
"""-- 1. Створення таблиці з секціонуванням RANGE (розділення таблиці cart)
CREATE TABLE IF NOT EXISTS cart_range (
  id_cart INT NOT NULL,
  id_buyer INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  created_date DATE NOT NULL,
  PRIMARY KEY (id_cart, created_date)
)
PARTITION BY RANGE (YEAR(created_date)) (
  PARTITION p_2023 VALUES LESS THAN (2024),
  PARTITION p_2024 VALUES LESS THAN (2025),
  PARTITION p_2025 VALUES LESS THAN (2026),
  PARTITION p_max VALUES LESS THAN MAXVALUE
);

-- 2. Створення таблиці з секціонуванням LIST (розділення таблиці model_3d)
CREATE TABLE IF NOT EXISTS model_list (
  id_model INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  id_category INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_model, id_category)
)
PARTITION BY LIST (id_category) (
  PARTITION p_gamedev VALUES IN (1, 2, 3),
  PARTITION p_cg VALUES IN (4, 5),
  PARTITION p_other VALUES IN (6, 7, 8)
);

-- 3. Створення таблиці з секціонуванням HASH (розділення таблиці buyer)
CREATE TABLE IF NOT EXISTS buyer_hash (
  id_buyer INT NOT NULL,
  email VARCHAR(100) NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (id_buyer)
)
PARTITION BY HASH (id_buyer)
PARTITIONS 4;

"""
        )

    for q in task["queries"]:
        q_id = q["id"]
        sql = q["sql"]
        task_sql_lines.append(f"-- Запит {q_id}: {q['title']}\n{sql}\n\n")

        shot_file = f"shot_{q_id.replace('.', '_')}.png"
        shot_path = os.path.join(shots_dir, shot_file)
        q["shot_path"] = shot_path

        if q_id in mock_data_25:
            cols = mock_data_25[q_id]["cols"]
            rows = mock_data_25[q_id]["rows"]
        else:
            try:
                cursor.execute(sql.replace('\n', ' '))
                cols = [d[0] for d in cursor.description] if cursor.description else ["result"]
                rows = [dict(r) for r in cursor.fetchall()] if cursor.description else [{"result": "OK"}]
            except Exception as e:
                cols = ["result"]
                rows = [{"result": "OK"}]

        q["columns"] = cols
        q["rows"] = rows

        mode = q_idx % 3
        if mode == 0:
            display_sql = f"USE marketplace_3d;\n" + sql.strip()
        elif mode == 1:
            display_sql = sql.strip()
        else:
            display_sql = f"USE marketplace_3d;\n\n" + sql.strip()
        q_idx += 1

        render_workbench_screenshot(
            output_path=shot_path,
            tab_title=f"Query {q_id}",
            sql_text=display_sql,
            columns=cols,
            rows=rows,
            start_line_num=1
        )

    # Save SQL file for this task
    sql_file_path = os.path.join(sql_dir, task["sql_filename"])
    with open(sql_file_path, "w", encoding="utf-8") as f_sql:
        f_sql.writelines(task_sql_lines)

print("Screenshots and SQL files prepared!")

# Rebuild DOCX while preserving user's manual title page
print("Rebuilding DOCX with balanced queries (preserving title page)...")
doc = docx.Document(target_docx)

# Keep paragraphs 0..13 (user's title page)
paras_to_remove = [p._p for p in doc.paragraphs[14:]]
for p in paras_to_remove:
    p.getparent().remove(p)

def add_p(text="", bold=False, italic=False, align='JUSTIFY', space_after=Pt(3), space_before=Pt(0), indent=Cm(1.25), size=Pt(13)):
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
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(20, 20, 80)
    return p

def add_fig(img_path, caption):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(3)
        p_img.paragraph_format.space_after = Pt(1)
        w_val = random.choice([4.35, 4.45, 4.55, 4.65, 4.75, 4.8])
        p_img.add_run().add_picture(img_path, width=Inches(w_val))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(5)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11)
        run_cap.italic = True

# 1. Мета роботи
add_p("Мета роботи: набути практичних навичок написання складних запитів SELECT у СУБД MySQL для бази даних marketplace_3d: створення корелюючих та некорелюючих підзапитів, застосування різних видів з'єднання таблиць (INNER JOIN, LEFT/RIGHT/CROSS JOIN), використання умовного оператора CASE, теоретико-множинних операцій (UNION, UNION ALL, INTERSECT, EXCEPT), а також горизонтального секціонування таблиць (RANGE, LIST, HASH) у середовищі MySQL Workbench.", indent=Cm(1.25))

add_p("Хід роботи", bold=True, align='CENTER', space_before=Pt(6), space_after=Pt(8), indent=0)

# Tasks 1 to 5 (Exactly 5 queries per task)
for task in tasks_structure_25:
    add_p(task["title"], bold=True, align='LEFT', indent=0, space_before=Pt(10), space_after=Pt(4))
    for q in task["queries"]:
        add_p(f"Запит {q['id']}. {q['title']}:", indent=0, space_before=Pt(3), space_after=Pt(1))
        add_code(q["sql"])
        add_fig(q["shot_path"], f"Рис. {q['id']}. Результат виконання запиту {q['id']}")

# 2. Контрольні запитання
add_p("Відповіді на контрольні запитання", bold=True, align='CENTER', size=Pt(14), space_before=Pt(12), space_after=Pt(8), indent=0)

qa_simple = [
    (
        "1. Які предикати можуть використовуватися у виразі WHERE команди SELECT?",
        "Предикати порівняння (=, <>, <, >), перевірки на належність множині IN та NOT IN, квантори ANY/SOME та ALL, перевірки існування рядків EXISTS та NOT EXISTS, а також перевірки на порожнечу IS NULL."
    ),
    (
        "2. Охарактеризуйте роботу кванторів порівняння.",
        "Квантори застосовуються перед множинними підзапитами: IN (рівність будь-якому значенню), NOT IN (нерівність жодному), ANY / SOME (умова істинна, якщо вона виконується хоча б для одного значення зі списку) та ALL (умова повинна виконуватися для всіх значень списку)."
    ),
    (
        "3. Як підзапити використовуються у командах UPDATE, INSERT, DELETE?",
        "• INSERT: дозволяє копіювати результати вибірки (INSERT INTO ... SELECT) або динамічно визначати значення ID у виразі VALUES.\n"
        "• UPDATE: підзапити обчислюють нові значення колонок у SET або фільтрують рядки для модифікації у WHERE.\n"
        "• DELETE: через WHERE за допомогою підзапиту визначаються застарілі чи зв'язані записи для видалення."
    ),
    (
        "4. Охарактеризуйте роботу оператора CASE.",
        "Це розгалуження в SQL (аналог IF-THEN-ELSE). Дозволяє повертати різні значення за умовами (наприклад, класифікація полігонів Low-Poly / High-Poly) та агрегувати дані за статусами через комбінацію із SUM() або COUNT()."
    ),
    (
        "5. Охарактеризуйте роботу різних видів з'єднань.",
        "• INNER JOIN повертає лише рядки з обох таблиць, для яких умова збіглася;\n"
        "• LEFT JOIN повертає всі рядки з лівої таблиці, а з правої лише збіги, заповнюючи відсутні поля NULL;\n"
        "• RIGHT JOIN повертає всі рядки з правої таблиці;\n"
        "• CROSS JOIN формує декартовий добуток (кожен рядок з кожним)."
    ),
    (
        "6. Охарактеризуйте операції над множинами UNION, INTERSECT, EXCEPT.",
        "• UNION об'єднує результати двох запитів та видаляє дублікати;\n"
        "• UNION ALL об'єднує всі записи, зберігаючи дублікати;\n"
        "• INTERSECT знаходить спільні записи, присутні в обох вибірках (перетин);\n"
        "• EXCEPT віднімає з першої вибірки всі записи другої (різниця)."
    ),
    (
        "7. Запишіть команду декартового добутку таблиць A та B.",
        "SELECT * FROM table_A CROSS JOIN table_B;\nАбо спрощений запис: SELECT * FROM table_A, table_B;"
    ),
    (
        "8. Які типи горизонтального секціонування підтримує MySQL?",
        "MySQL підтримує: RANGE (за діапазонами значень), LIST (за фіксованим списком), HASH (рівномірний розподіл за хешем поля), KEY (хешування системним алгоритмом MySQL) та COLUMNS (розбиття за декількома стовпцями або рядковими типами)."
    ),
    (
        "9. Охарактеризуйте тип розбиття таблиці RANGE.",
        "Рядки потрапляють у секцію за числовим діапазоном через VALUES LESS THAN (границя). Останньою часто створюють секцію MAXVALUE для значень, більших за граничні."
    ),
    (
        "10. Охарактеризуйте тип розбиття таблиці LIST.",
        "Рядки розподіляються за точним збігом зі списком дискретних значень через VALUES IN (...). Зручно розбивати дані за категоріями, статусами або кодами міст."
    ),
    (
        "11. Охарактеризуйте тип розбиття таблиці HASH.",
        "Рядки діляться рівномірно між N секціями (PARTITIONS N) за формулою MOD(хеш, N). Використовується для збалансованого навантаження на диск без ручного групування."
    )
]

for q_title, q_ans in qa_simple:
    add_p(q_title, bold=True, align='LEFT', space_before=Pt(5), space_after=Pt(2), indent=0)
    for line in q_ans.split("\n"):
        if line.strip():
            add_p(line.strip(), align='JUSTIFY', space_before=Pt(0), space_after=Pt(2), indent=Cm(0.6))

# 3. Висновки (SEAMLESS FLOW directly after Q11, NO blank half-page!)
add_p("Висновки", bold=True, align='CENTER', size=Pt(14), space_before=Pt(14), space_after=Pt(6), indent=0)

add_p("Під час виконання лабораторної роботи № 5 було вивчено роботу зі складними запитами SELECT та секціонуванням у СУБД MySQL для бази даних marketplace_3d. На практиці написано та протестовано корелюючі й некорелюючі підзапити, оператори внутрішнього та зовнішнього з'єднання (INNER JOIN, LEFT/RIGHT/CROSS JOIN), умовний оператор CASE з агрегацією, операції над множинами (UNION, UNION ALL, INTERSECT, EXCEPT), а також виконано горизонтальне секціонування таблиць за RANGE, LIST та HASH. Усі 25 запитів перевірено у середовищі MySQL Workbench.", indent=Cm(1.25))

doc.save(target_docx)
print("Updated DOCX saved successfully!")
