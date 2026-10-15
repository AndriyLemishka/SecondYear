import os

cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
file_path = os.path.join(cache_dir, "build_all_79_queries.py")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('"task_num": 6,')
end_idx = content.find("]\n\n# Execute", idx)

if idx != -1 and end_idx != -1:
    new_task6 = '''"task_num": 6,
        "title": "Завдання 6. Створення та використання представлень (CREATE VIEW, SELECT FROM VIEW)",
        "subsections": [
            {
                "sub_id": "6.1",
                "cmd_name": "Команда VIEW",
                "desc": "Створення 2 представлень для збереження вибірок та вибірка з них (2 запити)",
                "queries": [
                    {
                        "num": "6.1.1",
                        "title": "Створення v_premium_models (вітрина преміальних моделей без JOIN)",
                        "desc": "Формування віртуальної вітрини 3D-моделей з ціною від 20 у.о. без об'єднання таблиць.",
                        "view_name": "v_premium_models",
                        "create_sql": """DROP VIEW IF EXISTS v_premium_models;\\nCREATE VIEW v_premium_models AS\\nSELECT id_model, name, price, polygon_count, has_texture\\nFROM model_3d\\nWHERE price >= 20.00;""",
                        "select_sql": "SELECT * FROM v_premium_models ORDER BY price DESC;"
                    },
                    {
                        "num": "6.1.2",
                        "title": "Створення v_top_sellers (топ-продавці за рейтингом без JOIN)",
                        "desc": "Формування віртуальної таблиці найрейтинговіших продавців маркетплейсу.",
                        "view_name": "v_top_sellers",
                        "create_sql": """DROP VIEW IF EXISTS v_top_sellers;\\nCREATE VIEW v_top_sellers AS\\nSELECT id_seller, nickname, rating\\nFROM seller\\nWHERE rating >= 4.80;""",
                        "select_sql": "SELECT * FROM v_top_sellers ORDER BY rating DESC;"
                    }
                ]
            }
        ]
    }
'''
    updated = content[:idx] + new_task6 + content[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("build_all_79_queries.py updated successfully!")
else:
    print(f"Indices not found: {idx}, {end_idx}")
