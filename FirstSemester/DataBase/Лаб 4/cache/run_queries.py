import sqlite3
import re
import json

db_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\marketplace_3d.db"
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

def regexp(expr, item):
    if item is None:
        return False
    return bool(re.search(expr, str(item), re.IGNORECASE))

conn.create_function("REGEXP", 2, regexp)
cursor = conn.cursor()

tasks = [
    {
        "task_num": 1,
        "title": "Завдання 1. Написання запитів простої вибірки (SELECT, FROM, LIMIT, DISTINCT, IS NULL)",
        "queries": [
            {
                "num": "1.1",
                "desc": "Вибірка всіх полів та записів з таблиці каталогу 3D-моделей (базовий SELECT *).",
                "sql": "SELECT id_model, name, price, polygon_count, has_texture FROM model_3d LIMIT 6;"
            },
            {
                "num": "1.2",
                "desc": "Вибірка унікальних форматів файлів моделей у маркетплейсі з використанням DISTINCT.",
                "sql": "SELECT DISTINCT format FROM model_file;"
            },
            {
                "num": "1.3",
                "desc": "Отримання списку перших трьох зареєстрованих покупців з обмеженням кількості через LIMIT.",
                "sql": "SELECT id_buyer, email, registration_date FROM buyer LIMIT 3;"
            },
            {
                "num": "1.4",
                "desc": "Пошук 3D-моделей, у яких відсутній детальний опис (перевірка на IS NULL).",
                "sql": "SELECT id_model, name, description, price FROM model_3d WHERE description IS NULL;"
            },
            {
                "num": "1.5",
                "desc": "Вибірка унікальних пар 'статус кошика — сума' з пропуском перших двох рядків (LIMIT 2, 4).",
                "sql": "SELECT DISTINCT status, total_amount FROM cart LIMIT 2, 4;"
            }
        ]
    },
    {
        "task_num": 2,
        "title": "Завдання 2. Сортування даних у запитах (ORDER BY, DESC, сортування за декількома стовпцями)",
        "queries": [
            {
                "num": "2.1",
                "desc": "Сортування списку авторів (продавців) за рейтингом від найвищого до найнижчого (ORDER BY DESC).",
                "sql": "SELECT id_seller, nickname, rating FROM seller ORDER BY rating DESC LIMIT 5;"
            },
            {
                "num": "2.2",
                "desc": "Сортування моделей за ціною у зростаючому порядку з обчисленням ціни з ПДВ 20% через псевдонім (AS).",
                "sql": "SELECT id_model, name, price, ROUND(price * 1.20, 2) AS price_with_vat FROM model_3d ORDER BY price ASC LIMIT 5;"
            },
            {
                "num": "2.3",
                "desc": "Сортування за двома стовпцями: за наявністю текстури (за спаданням) та кількістю полігонів (за зростанням).",
                "sql": "SELECT id_model, name, has_texture, polygon_count, price FROM model_3d ORDER BY has_texture DESC, polygon_count ASC LIMIT 6;"
            }
        ]
    },
    {
        "task_num": 3,
        "title": "Завдання 3. Фільтрація даних за умовами (IN, BETWEEN, LIKE, REGEXP)",
        "queries": [
            {
                "num": "3.1",
                "desc": "Фільтрація моделей за списком ідентифікаторів категорій за допомогою оператора IN.",
                "sql": "SELECT id_model, name, id_category, price FROM model_3d WHERE id_category IN (1, 2, 8);"
            },
            {
                "num": "3.2",
                "desc": "Фільтрація файлів 3D-моделей за розміром у діапазоні від 10 до 50 МБ за допомогою BETWEEN.",
                "sql": "SELECT id_file, id_model, format, size_mb FROM model_file WHERE size_mb BETWEEN 10.0 AND 50.0;"
            },
            {
                "num": "3.3",
                "desc": "Пошук моделей за шаблоном назви з входженням підрядка 'Sci-Fi' оператором LIKE.",
                "sql": "SELECT id_model, name, price, polygon_count FROM model_3d WHERE name LIKE '%Sci-Fi%';"
            },
            {
                "num": "3.4",
                "desc": "Фільтрація користувачів за маскою електронної пошти за допомогою оператора LIKE (підрядки '_art@' або 'user_%').",
                "sql": "SELECT id_buyer, email, registration_date FROM buyer WHERE email LIKE '%_art@%' OR email LIKE 'user_%';"
            },
            {
                "num": "3.5",
                "desc": "Складна фільтрація назв моделей за регулярним виразом REGEXP (початок з Cyberpunk, Sports або Space).",
                "sql": "SELECT id_model, name, price, polygon_count FROM model_3d WHERE name REGEXP '^(Cyberpunk|Sports|Space).*';"
            }
        ]
    },
    {
        "task_num": 4,
        "title": "Завдання 4. Використання агрегатних функцій (COUNT, AVG, MIN, MAX, SUM)",
        "queries": [
            {
                "num": "4.1",
                "desc": "Підрахунок загальної кількості моделей та кількості унікальних категорій у каталозі.",
                "sql": "SELECT COUNT(*) AS total_models, COUNT(DISTINCT id_category) AS unique_categories_count FROM model_3d;"
            },
            {
                "num": "4.2",
                "desc": "Обчислення середньої вартості 3D-моделі та середньої кількості полігонів (функція AVG).",
                "sql": "SELECT ROUND(AVG(price), 2) AS avg_model_price, ROUND(AVG(polygon_count), 0) AS avg_polygon_count FROM model_3d;"
            },
            {
                "num": "4.3",
                "desc": "Визначення мінімальної та максимальної вартості 3D-моделей у маркетплейсі (функції MIN, MAX).",
                "sql": "SELECT MIN(price) AS min_model_price, MAX(price) AS max_model_price FROM model_3d;"
            },
            {
                "num": "4.4",
                "desc": "Обчислення загальної суми виручки за всіма успішно оплаченими замовленнями (функція SUM).",
                "sql": "SELECT SUM(total_amount) AS total_revenue FROM cart WHERE status = 'Completed';"
            },
            {
                "num": "4.5",
                "desc": "Зведена статистика щодо розмірів файлів моделей у системі (COUNT, MIN, MAX, AVG, SUM).",
                "sql": "SELECT COUNT(id_file) AS total_files, MIN(size_mb) AS min_file_size, MAX(size_mb) AS max_file_size, ROUND(AVG(size_mb), 2) AS avg_file_size, ROUND(SUM(size_mb), 2) AS total_storage_mb FROM model_file;"
            }
        ]
    },
    {
        "task_num": 5,
        "title": "Завдання 5. Групування даних та фільтрація груп (GROUP BY, HAVING)",
        "queries": [
            {
                "num": "5.1",
                "desc": "Аналіз кількості 3D-моделей та їх середньої вартості у розрізі кожної категорії товару.",
                "sql": "SELECT id_category, COUNT(*) AS models_count, ROUND(AVG(price), 2) AS avg_price FROM model_3d GROUP BY id_category ORDER BY models_count DESC;"
            },
            {
                "num": "5.2",
                "desc": "Групування замовлень за статусами з фільтрацією груп за сумарним грошовим оборотом понад 50 (HAVING).",
                "sql": "SELECT status, COUNT(*) AS orders_count, ROUND(SUM(total_amount), 2) AS total_volume FROM cart GROUP BY status HAVING total_volume > 50.00;"
            },
            {
                "num": "5.3",
                "desc": "Визначення авторів (продавців), які мають 2 і більше робіт, з підрахунком сумарної вартості їхніх моделей.",
                "sql": "SELECT id_seller, COUNT(*) AS models_created, ROUND(SUM(price), 2) AS total_catalog_value FROM model_3d GROUP BY id_seller HAVING COUNT(*) >= 2;"
            }
        ]
    },
    {
        "task_num": 6,
        "title": "Завдання 6. Створення та використання представлень (CREATE VIEW, SELECT FROM VIEW)",
        "views": [
            {
                "num": "6.1",
                "view_name": "view_popular_models",
                "desc": "Представлення 'view_popular_models': вітрина 3D-моделей із назвою категорії та нікнеймом автора.",
                "create_sql": """CREATE VIEW IF NOT EXISTS view_popular_models AS
SELECT 
    m.id_model,
    m.name AS model_name,
    c.name AS category_name,
    s.nickname AS author_nickname,
    m.price,
    m.polygon_count,
    m.has_texture
FROM model_3d m
JOIN category c ON m.id_category = c.id_category
JOIN seller s ON m.id_seller = s.id_seller;""",
                "select_sql": "SELECT * FROM view_popular_models WHERE price >= 20.00 ORDER BY price DESC;"
            },
            {
                "num": "6.2",
                "view_name": "view_buyer_order_summary",
                "desc": "Представлення 'view_buyer_order_summary': зведена аналітика покупок клієнтів із витраченою сумою.",
                "create_sql": """CREATE VIEW IF NOT EXISTS view_buyer_order_summary AS
SELECT 
    b.id_buyer,
    b.email,
    COUNT(c.id_cart) AS total_orders,
    COALESCE(SUM(c.total_amount), 0) AS total_spent
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer AND c.status = 'Completed'
GROUP BY b.id_buyer, b.email;""",
                "select_sql": "SELECT * FROM view_buyer_order_summary WHERE total_orders > 0 ORDER BY total_spent DESC;"
            }
        ]
    }
]

# Run and collect results
all_results = []
for t in tasks:
    task_res = {"task_num": t["task_num"], "title": t["title"], "items": []}
    if "queries" in t:
        for q in t["queries"]:
            cursor.execute(q["sql"])
            rows = [dict(row) for row in cursor.fetchall()]
            task_res["items"].append({
                "num": q["num"],
                "desc": q["desc"],
                "sql": q["sql"],
                "rows": rows
            })
    elif "views" in t:
        for v in t["views"]:
            cursor.execute(v["create_sql"])
            cursor.execute(v["select_sql"])
            rows = [dict(row) for row in cursor.fetchall()]
            task_res["items"].append({
                "num": v["num"],
                "view_name": v["view_name"],
                "desc": v["desc"],
                "create_sql": v["create_sql"],
                "select_sql": v["select_sql"],
                "rows": rows
            })
    all_results.append(task_res)

with open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\query_results.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print("All queries executed successfully and saved to query_results.json!")
