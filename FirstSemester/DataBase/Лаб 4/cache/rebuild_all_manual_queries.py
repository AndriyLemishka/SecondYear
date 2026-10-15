import os
import sqlite3
import json
import re

cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
db_path = os.path.join(cache_dir, "marketplace_3d.db")

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

def regexp(pattern, value):
    if value is None:
        return False
    return bool(re.search(pattern, str(value), re.IGNORECASE))

conn.create_function("REGEXP", 2, regexp)
cursor = conn.cursor()

all_tasks_def = [
    {
        "task_num": 1,
        "title": "Завдання 1. Прості запити",
        "subsections": [
            {
                "sub_id": "1.1",
                "cmd_name": "SELECT та FROM",
                "queries": [
                    {
                        "num": "1.1.1",
                        "title": "Вибірка всіх полів з таблиці моделей",
                        "sql": "SELECT * FROM model_3d LIMIT 5;"
                    },
                    {
                        "num": "1.1.2",
                        "title": "Вибірка назви та ціни моделей",
                        "sql": "SELECT name, price FROM model_3d LIMIT 5;"
                    },
                    {
                        "num": "1.1.3",
                        "title": "Вибірка пошти покупців",
                        "sql": "SELECT id_buyer, email FROM buyer LIMIT 5;"
                    },
                    {
                        "num": "1.1.4",
                        "title": "Вибірка з псевдонімом стовпця",
                        "sql": "SELECT nickname AS author, rating FROM seller LIMIT 5;"
                    },
                    {
                        "num": "1.1.5",
                        "title": "Вибірка з простим множенням ціни",
                        "sql": "SELECT name, price, price * 2 AS double_price FROM model_3d LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "1.2",
                "cmd_name": "Команда LIMIT",
                "queries": [
                    {
                        "num": "1.2.1",
                        "title": "Вибірка перших 3 моделей",
                        "sql": "SELECT * FROM model_3d LIMIT 3;"
                    },
                    {
                        "num": "1.2.2",
                        "title": "Вибірка перших 5 покупців",
                        "sql": "SELECT * FROM buyer LIMIT 5;"
                    },
                    {
                        "num": "1.2.3",
                        "title": "Вибірка перших 2 продавців",
                        "sql": "SELECT * FROM seller LIMIT 2;"
                    },
                    {
                        "num": "1.2.4",
                        "title": "Вибірка 4 категорій",
                        "sql": "SELECT * FROM category LIMIT 4;"
                    },
                    {
                        "num": "1.2.5",
                        "title": "Вибірка 3 моделей починаючи з 2-го рядка",
                        "sql": "SELECT * FROM model_3d LIMIT 2, 3;"
                    }
                ]
            },
            {
                "sub_id": "1.3",
                "cmd_name": "Команда DISTINCT",
                "queries": [
                    {
                        "num": "1.3.1",
                        "title": "Унікальні формати файлів",
                        "sql": "SELECT DISTINCT format FROM model_file;"
                    },
                    {
                        "num": "1.3.2",
                        "title": "Унікальні статуси замовлень",
                        "sql": "SELECT DISTINCT status FROM cart;"
                    },
                    {
                        "num": "1.3.3",
                        "title": "Унікальні типи ліцензій",
                        "sql": "SELECT DISTINCT usage_type FROM license;"
                    },
                    {
                        "num": "1.3.4",
                        "title": "Унікальні оцінки у відгуках",
                        "sql": "SELECT DISTINCT rating FROM review;"
                    },
                    {
                        "num": "1.3.5",
                        "title": "Унікальні значення наявності текстури",
                        "sql": "SELECT DISTINCT has_texture FROM model_3d;"
                    }
                ]
            },
            {
                "sub_id": "1.4",
                "cmd_name": "Команда IS NULL",
                "queries": [
                    {
                        "num": "1.4.1",
                        "title": "Моделі без опису",
                        "sql": "SELECT * FROM model_3d WHERE description IS NULL;"
                    },
                    {
                        "num": "1.4.2",
                        "title": "Моделі з описом",
                        "sql": "SELECT * FROM model_3d WHERE description IS NOT NULL LIMIT 5;"
                    },
                    {
                        "num": "1.4.3",
                        "title": "Відгуки без тексту коментаря",
                        "sql": "SELECT * FROM review WHERE comment_text IS NULL;"
                    },
                    {
                        "num": "1.4.4",
                        "title": "Відгуки з текстом коментаря",
                        "sql": "SELECT * FROM review WHERE comment_text IS NOT NULL LIMIT 5;"
                    },
                    {
                        "num": "1.4.5",
                        "title": "Продавці з наявним рейтингом",
                        "sql": "SELECT * FROM seller WHERE rating IS NOT NULL LIMIT 5;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 2,
        "title": "Завдання 2. Сортування даних",
        "subsections": [
            {
                "sub_id": "2.1",
                "cmd_name": "Команда ORDER BY",
                "queries": [
                    {
                        "num": "2.1.1",
                        "title": "Сортування моделей за зростанням ціни",
                        "sql": "SELECT id_model, name, price FROM model_3d ORDER BY price LIMIT 5;"
                    },
                    {
                        "num": "2.1.2",
                        "title": "Сортування продавців за рейтингом",
                        "sql": "SELECT * FROM seller ORDER BY rating LIMIT 5;"
                    },
                    {
                        "num": "2.1.3",
                        "title": "Сортування категорій за алфавітом",
                        "sql": "SELECT * FROM category ORDER BY name LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.2",
                "cmd_name": "Команда DESC",
                "queries": [
                    {
                        "num": "2.2.1",
                        "title": "Сортування моделей від найдорожчої",
                        "sql": "SELECT id_model, name, price FROM model_3d ORDER BY price DESC LIMIT 5;"
                    },
                    {
                        "num": "2.2.2",
                        "title": "Сортування продавців від найвищого рейтингу",
                        "sql": "SELECT * FROM seller ORDER BY rating DESC LIMIT 5;"
                    },
                    {
                        "num": "2.2.3",
                        "title": "Сортування замовлень від найбільшої суми",
                        "sql": "SELECT * FROM cart ORDER BY total_amount DESC LIMIT 5;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 3,
        "title": "Завдання 3. Фільтрація даних",
        "subsections": [
            {
                "sub_id": "3.1",
                "cmd_name": "Команда IN",
                "queries": [
                    {
                        "num": "3.1.1",
                        "title": "Файли форматів FBX та OBJ",
                        "sql": "SELECT * FROM model_file WHERE format IN ('FBX', 'OBJ') LIMIT 5;"
                    },
                    {
                        "num": "3.1.2",
                        "title": "Замовлення зі статусами Completed та Active",
                        "sql": "SELECT * FROM cart WHERE status IN ('Completed', 'Active') LIMIT 5;"
                    },
                    {
                        "num": "3.1.3",
                        "title": "Моделі з категорій 1, 2, 3",
                        "sql": "SELECT id_model, name, id_category, price FROM model_3d WHERE id_category IN (1, 2, 3);"
                    },
                    {
                        "num": "3.1.4",
                        "title": "Файли інших форматів через NOT IN",
                        "sql": "SELECT * FROM model_file WHERE format NOT IN ('FBX', 'OBJ') LIMIT 5;"
                    },
                    {
                        "num": "3.1.5",
                        "title": "Відгуки з оцінками 4 та 5",
                        "sql": "SELECT * FROM review WHERE rating IN (4, 5) LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "3.2",
                "cmd_name": "Команда BETWEEN",
                "queries": [
                    {
                        "num": "3.2.1",
                        "title": "Моделі з ціною від 10 до 30",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE price BETWEEN 10 AND 30;"
                    },
                    {
                        "num": "3.2.2",
                        "title": "Продавці з рейтингом від 4.5 до 5",
                        "sql": "SELECT * FROM seller WHERE rating BETWEEN 4.5 AND 5.0;"
                    },
                    {
                        "num": "3.2.3",
                        "title": "Файли розміром від 10 до 50 МБ",
                        "sql": "SELECT * FROM model_file WHERE size_mb BETWEEN 10 AND 50;"
                    },
                    {
                        "num": "3.2.4",
                        "title": "Замовлення на суму від 20 до 50",
                        "sql": "SELECT * FROM cart WHERE total_amount BETWEEN 20 AND 50;"
                    },
                    {
                        "num": "3.2.5",
                        "title": "Моделі з ціною не від 10 до 30",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE price NOT BETWEEN 10 AND 30;"
                    }
                ]
            },
            {
                "sub_id": "3.3",
                "cmd_name": "Команда LIKE",
                "queries": [
                    {
                        "num": "3.3.1",
                        "title": "Моделі на літеру C",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name LIKE 'C%';"
                    },
                    {
                        "num": "3.3.2",
                        "title": "Моделі зі словом Car у назві",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name LIKE '%Car%';"
                    },
                    {
                        "num": "3.3.3",
                        "title": "Пошта покупців на mail.com",
                        "sql": "SELECT * FROM buyer WHERE email LIKE '%@mail.com' LIMIT 5;"
                    },
                    {
                        "num": "3.3.4",
                        "title": "Пошта з одним символом після user_",
                        "sql": "SELECT * FROM buyer WHERE email LIKE 'user_@%';"
                    },
                    {
                        "num": "3.3.5",
                        "title": "Моделі без слова Car у назві",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name NOT LIKE '%Car%' LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "3.4",
                "cmd_name": "Команда REGEXP",
                "queries": [
                    {
                        "num": "3.4.1",
                        "title": "Моделі зі словом Car або Rifle",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP 'Car|Rifle';"
                    },
                    {
                        "num": "3.4.2",
                        "title": "Моделі що починаються на Space",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '^Space';"
                    },
                    {
                        "num": "3.4.3",
                        "title": "Моделі що закінчуються на Station",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP 'Station$';"
                    },
                    {
                        "num": "3.4.4",
                        "title": "Моделі що містять цифру",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '[0-9]';"
                    },
                    {
                        "num": "3.4.5",
                        "title": "Відгуки зі словами Amazing або Good",
                        "sql": "SELECT * FROM review WHERE comment_text REGEXP 'Amazing|Good';"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 4,
        "title": "Завдання 4. Агрегатні функції",
        "subsections": [
            {
                "sub_id": "4.1",
                "cmd_name": "Функція AVG",
                "queries": [
                    {
                        "num": "4.1.1",
                        "title": "Середня ціна всіх моделей",
                        "sql": "SELECT AVG(price) FROM model_3d;"
                    },
                    {
                        "num": "4.1.2",
                        "title": "Середній рейтинг продавців",
                        "sql": "SELECT AVG(rating) FROM seller;"
                    },
                    {
                        "num": "4.1.3",
                        "title": "Середній розмір файлів",
                        "sql": "SELECT AVG(size_mb) FROM model_file;"
                    },
                    {
                        "num": "4.1.4",
                        "title": "Середня сума замовлення",
                        "sql": "SELECT AVG(total_amount) FROM cart;"
                    },
                    {
                        "num": "4.1.5",
                        "title": "Середня оцінка у відгуках",
                        "sql": "SELECT AVG(rating) FROM review;"
                    }
                ]
            },
            {
                "sub_id": "4.2",
                "cmd_name": "Функція SUM",
                "queries": [
                    {
                        "num": "4.2.1",
                        "title": "Сума цін усіх моделей",
                        "sql": "SELECT SUM(price) FROM model_3d;"
                    },
                    {
                        "num": "4.2.2",
                        "title": "Загальна сума замовлень",
                        "sql": "SELECT SUM(total_amount) FROM cart;"
                    },
                    {
                        "num": "4.2.3",
                        "title": "Загальний розмір усіх файлів",
                        "sql": "SELECT SUM(size_mb) FROM model_file;"
                    },
                    {
                        "num": "4.2.4",
                        "title": "Загальна кількість полігонів",
                        "sql": "SELECT SUM(polygon_count) FROM model_3d;"
                    },
                    {
                        "num": "4.2.5",
                        "title": "Сума виконаних замовлень",
                        "sql": "SELECT SUM(total_amount) FROM cart WHERE status = 'Completed';"
                    }
                ]
            },
            {
                "sub_id": "4.3",
                "cmd_name": "Функція MIN",
                "queries": [
                    {
                        "num": "4.3.1",
                        "title": "Мінімальна ціна моделі",
                        "sql": "SELECT MIN(price) FROM model_3d;"
                    },
                    {
                        "num": "4.3.2",
                        "title": "Мінімальний рейтинг продавця",
                        "sql": "SELECT MIN(rating) FROM seller;"
                    },
                    {
                        "num": "4.3.3",
                        "title": "Мінімальний розмір файлу",
                        "sql": "SELECT MIN(size_mb) FROM model_file;"
                    },
                    {
                        "num": "4.3.4",
                        "title": "Мінімальна сума замовлення",
                        "sql": "SELECT MIN(total_amount) FROM cart;"
                    },
                    {
                        "num": "4.3.5",
                        "title": "Мінімальна кількість полігонів",
                        "sql": "SELECT MIN(polygon_count) FROM model_3d;"
                    }
                ]
            },
            {
                "sub_id": "4.4",
                "cmd_name": "Функція MAX",
                "queries": [
                    {
                        "num": "4.4.1",
                        "title": "Максимальна ціна моделі",
                        "sql": "SELECT MAX(price) FROM model_3d;"
                    },
                    {
                        "num": "4.4.2",
                        "title": "Максимальний рейтинг продавця",
                        "sql": "SELECT MAX(rating) FROM seller;"
                    },
                    {
                        "num": "4.4.3",
                        "title": "Максимальний розмір файлу",
                        "sql": "SELECT MAX(size_mb) FROM model_file;"
                    },
                    {
                        "num": "4.4.4",
                        "title": "Максимальна сума замовлення",
                        "sql": "SELECT MAX(total_amount) FROM cart;"
                    },
                    {
                        "num": "4.4.5",
                        "title": "Максимальна кількість полігонів",
                        "sql": "SELECT MAX(polygon_count) FROM model_3d;"
                    }
                ]
            },
            {
                "sub_id": "4.5",
                "cmd_name": "Функція COUNT",
                "queries": [
                    {
                        "num": "4.5.1",
                        "title": "Загальна кількість моделей",
                        "sql": "SELECT COUNT(*) FROM model_3d;"
                    },
                    {
                        "num": "4.5.2",
                        "title": "Кількість покупців",
                        "sql": "SELECT COUNT(*) FROM buyer;"
                    },
                    {
                        "num": "4.5.3",
                        "title": "Кількість продавців",
                        "sql": "SELECT COUNT(*) FROM seller;"
                    },
                    {
                        "num": "4.5.4",
                        "title": "Кількість відгуків з коментарем",
                        "sql": "SELECT COUNT(comment_text) FROM review;"
                    },
                    {
                        "num": "4.5.5",
                        "title": "Кількість унікальних форматів",
                        "sql": "SELECT COUNT(DISTINCT format) FROM model_file;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 5,
        "title": "Завдання 5. Групування даних",
        "subsections": [
            {
                "sub_id": "5.1",
                "cmd_name": "Команда GROUP BY",
                "queries": [
                    {
                        "num": "5.1.1",
                        "title": "Кількість файлів для кожного формату",
                        "sql": "SELECT format, COUNT(*) FROM model_file GROUP BY format;"
                    },
                    {
                        "num": "5.1.2",
                        "title": "Кількість замовлень для кожного статусу",
                        "sql": "SELECT status, COUNT(*) FROM cart GROUP BY status;"
                    },
                    {
                        "num": "5.1.3",
                        "title": "Кількість моделей у кожній категорії",
                        "sql": "SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category;"
                    }
                ]
            },
            {
                "sub_id": "5.2",
                "cmd_name": "Команда HAVING",
                "queries": [
                    {
                        "num": "5.2.1",
                        "title": "Формати де більше 3 файлів",
                        "sql": "SELECT format, COUNT(*) FROM model_file GROUP BY format HAVING COUNT(*) > 3;"
                    },
                    {
                        "num": "5.2.2",
                        "title": "Статуси де 2 або більше замовлень",
                        "sql": "SELECT status, COUNT(*) FROM cart GROUP BY status HAVING COUNT(*) >= 2;"
                    },
                    {
                        "num": "5.2.3",
                        "title": "Категорії де 2 або більше моделей",
                        "sql": "SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category HAVING COUNT(*) >= 2;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 6,
        "title": "Завдання 6. Представлення VIEW",
        "subsections": [
            {
                "sub_id": "6.1",
                "cmd_name": "Команда VIEW",
                "queries": [
                    {
                        "num": "6.1.1",
                        "title": "Створення VIEW та вибірка моделей з ціною більше 15",
                        "view_name": "v_models",
                        "create_sql": """DROP VIEW IF EXISTS v_models;
CREATE VIEW v_models AS
SELECT id_model, name, price
FROM model_3d;""",
                        "select_sql": "SELECT * FROM v_models WHERE price > 15;"
                    },
                    {
                        "num": "6.1.2",
                        "title": "Вибірка з VIEW з сортуванням за ціною",
                        "view_name": "v_models",
                        "create_sql": """-- Вибірка зі створеного представлення v_models:""",
                        "select_sql": "SELECT * FROM v_models ORDER BY price DESC;"
                    }
                ]
            }
        ]
    }
]

print("Executing all 79 simplified student-style queries...")
all_executed_data = []
total_q_count = 0

for t in all_tasks_def:
    t_obj = {"task_num": t["task_num"], "title": t["title"], "subsections": []}
    for sub in t["subsections"]:
        s_obj = {"sub_id": sub["sub_id"], "cmd_name": sub["cmd_name"], "queries": []}
        for q in sub["queries"]:
            total_q_count += 1
            if "view_name" in q:
                if "CREATE VIEW" in q["create_sql"]:
                    cursor.executescript(q["create_sql"])
                cursor.execute(q["select_sql"])
                rows = [dict(r) for r in cursor.fetchall()]
                s_obj["queries"].append({
                    "num": q["num"],
                    "title": q["title"],
                    "view_name": q["view_name"],
                    "create_sql": q["create_sql"],
                    "select_sql": q["select_sql"],
                    "rows": rows
                })
            else:
                cursor.execute(q["sql"])
                rows = [dict(r) for r in cursor.fetchall()]
                s_obj["queries"].append({
                    "num": q["num"],
                    "title": q["title"],
                    "sql": q["sql"],
                    "rows": rows
                })
        t_obj["subsections"].append(s_obj)
    all_executed_data.append(t_obj)

print(f"Executed total {total_q_count} queries successfully!")

out_file = os.path.join(cache_dir, "all_79_results.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_executed_data, f, ensure_ascii=False, indent=2)

print("Saved clean student all_79_results.json successfully!")
