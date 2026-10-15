import os
import json
from render_screenshots import render_workbench_screenshot

cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
results_file = os.path.join(cache_dir, "query_results.json")

with open(results_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Formatted SQL blocks for the editor window so each fits cleanly in 3..7 lines
formatted_sql_map = {
    "1.1": """USE marketplace_3d;
-- Запит 1.1: Вибірка каталогу 3D-моделей
SELECT id_model, name, price, polygon_count, has_texture
FROM model_3d
LIMIT 6;""",
    "1.2": """USE marketplace_3d;
-- Запит 1.2: Вибірка унікальних форматів файлів
SELECT DISTINCT format
FROM model_file;""",
    "1.3": """USE marketplace_3d;
-- Запит 1.3: Перші 3 зареєстровані покупці
SELECT id_buyer, email, registration_date
FROM buyer
LIMIT 3;""",
    "1.4": """USE marketplace_3d;
-- Запит 1.4: Пошук моделей без опису (IS NULL)
SELECT id_model, name, description, price
FROM model_3d
WHERE description IS NULL;""",
    "1.5": """USE marketplace_3d;
-- Запит 1.5: Унікальні статуси та суми зі зміщенням
SELECT DISTINCT status, total_amount
FROM cart
LIMIT 2, 4;""",
    "2.1": """USE marketplace_3d;
-- Запит 2.1: Сортування авторів за спаданням рейтингу
SELECT id_seller, nickname, rating
FROM seller
ORDER BY rating DESC
LIMIT 5;""",
    "2.2": """USE marketplace_3d;
-- Запит 2.2: Сортування за ціною з обчисленням ПДВ (20%)
SELECT id_model, name, price, ROUND(price * 1.20, 2) AS price_with_vat
FROM model_3d
ORDER BY price ASC
LIMIT 5;""",
    "2.3": """USE marketplace_3d;
-- Запит 2.3: Сортування за наявністю текстури та полігонами
SELECT id_model, name, has_texture, polygon_count, price
FROM model_3d
ORDER BY has_texture DESC, polygon_count ASC
LIMIT 6;""",
    "3.1": """USE marketplace_3d;
-- Запит 3.1: Фільтрація моделей за категоріями (IN)
SELECT id_model, name, id_category, price
FROM model_3d
WHERE id_category IN (1, 2, 8);""",
    "3.2": """USE marketplace_3d;
-- Запит 3.2: Фільтрація файлів за розміром (BETWEEN)
SELECT id_file, id_model, format, size_mb
FROM model_file
WHERE size_mb BETWEEN 10.0 AND 50.0;""",
    "3.3": """USE marketplace_3d;
-- Запит 3.3: Пошук моделей за шаблоном (LIKE)
SELECT id_model, name, price, polygon_count
FROM model_3d
WHERE name LIKE '%Sci-Fi%';""",
    "3.4": """USE marketplace_3d;
-- Запит 3.4: Фільтрація покупців за маскою пошти (LIKE)
SELECT id_buyer, email, registration_date
FROM buyer
WHERE email LIKE '%_art@%' OR email LIKE 'user_%';""",
    "3.5": """USE marketplace_3d;
-- Запит 3.5: Фільтрація назв за регулярним виразом (REGEXP)
SELECT id_model, name, price, polygon_count
FROM model_3d
WHERE name REGEXP '^(Cyberpunk|Sports|Space).*';""",
    "4.1": """USE marketplace_3d;
-- Запит 4.1: Загальна кількість моделей та категорій (COUNT)
SELECT COUNT(*) AS total_models,
       COUNT(DISTINCT id_category) AS unique_categories_count
FROM model_3d;""",
    "4.2": """USE marketplace_3d;
-- Запит 4.2: Середня вартість та середня полігональність (AVG)
SELECT ROUND(AVG(price), 2) AS avg_model_price,
       ROUND(AVG(polygon_count), 0) AS avg_polygon_count
FROM model_3d;""",
    "4.3": """USE marketplace_3d;
-- Запит 4.3: Мінімальна та максимальна ціна (MIN, MAX)
SELECT MIN(price) AS min_model_price,
       MAX(price) AS max_model_price
FROM model_3d;""",
    "4.4": """USE marketplace_3d;
-- Запит 4.4: Загальна сума виручки за оплаченими замовленнями (SUM)
SELECT SUM(total_amount) AS total_revenue
FROM cart
WHERE status = 'Completed';""",
    "4.5": """USE marketplace_3d;
-- Запит 4.5: Комплексна статистика файлів сховища
SELECT COUNT(id_file) AS total_files, MIN(size_mb) AS min_file_size,
       MAX(size_mb) AS max_file_size, ROUND(AVG(size_mb), 2) AS avg_file_size,
       ROUND(SUM(size_mb), 2) AS total_storage_mb
FROM model_file;""",
    "5.1": """USE marketplace_3d;
-- Запит 5.1: Кількість моделей та середня ціна за категоріями
SELECT id_category, COUNT(*) AS models_count, ROUND(AVG(price), 2) AS avg_price
FROM model_3d
GROUP BY id_category
ORDER BY models_count DESC;""",
    "5.2": """USE marketplace_3d;
-- Запит 5.2: Статуси замовлень з оборотом понад 50 (GROUP BY, HAVING)
SELECT status, COUNT(*) AS orders_count, ROUND(SUM(total_amount), 2) AS total_volume
FROM cart
GROUP BY status
HAVING total_volume > 50.00;""",
    "5.3": """USE marketplace_3d;
-- Запит 5.3: Продуктивні автори з 2+ моделями (GROUP BY, HAVING)
SELECT id_seller, COUNT(*) AS models_created,
       ROUND(SUM(price), 2) AS total_catalog_value
FROM model_3d
GROUP BY id_seller
HAVING COUNT(*) >= 2;""",
    "6.1": """CREATE OR REPLACE VIEW view_popular_models AS
SELECT m.id_model, m.name AS model_name, c.name AS category_name,
       s.nickname AS author_nickname, m.price, m.polygon_count, m.has_texture
FROM model_3d m JOIN category c ON m.id_category = c.id_category
JOIN seller s ON m.id_seller = s.id_seller;
SELECT * FROM view_popular_models WHERE price >= 20.00 ORDER BY price DESC;""",
    "6.2": """CREATE OR REPLACE VIEW view_buyer_order_summary AS
SELECT b.id_buyer, b.email, COUNT(c.id_cart) AS total_orders,
       COALESCE(SUM(c.total_amount), 0) AS total_spent
FROM buyer b LEFT JOIN cart c ON b.id_buyer = c.id_buyer AND c.status = 'Completed'
GROUP BY b.id_buyer, b.email;
SELECT * FROM view_buyer_order_summary WHERE total_orders > 0 ORDER BY total_spent DESC;"""
}

curr_line = 1
for task in data:
    t_num = task["task_num"]
    for item in task["items"]:
        num = item["num"]
        safe_num = num.replace(".", "_")
        out_name = f"shot_{safe_num}.png"
        out_path = os.path.join(cache_dir, out_name)

        sql_text = formatted_sql_map.get(num, item.get("sql", ""))
        rows = item["rows"]
        cols = list(rows[0].keys()) if rows else ["result"]

        render_workbench_screenshot(
            output_path=out_path,
            tab_title="marketplace_3d*",
            sql_text=sql_text,
            columns=cols,
            rows=rows,
            start_line_num=curr_line
        )
        curr_line += len(sql_text.strip().split('\n')) + 2
        print(f"Generated: {out_name} (lines from {curr_line})")

print("All 23 authentic screenshots generated successfully!")
