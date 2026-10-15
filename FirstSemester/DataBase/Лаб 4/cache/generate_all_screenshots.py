import os
import json
from render_screenshots import render_workbench_screenshot

cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
results_file = os.path.join(cache_dir, "query_results.json")

with open(results_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Task 1 screenshot: query 1.1 + rows
t1 = data[0]["items"][0]
sql_t1 = """USE marketplace_3d;
-- Запит 1.1: Вибірка основних характеристик моделей каталогу
SELECT id_model, name, price, polygon_count, has_texture 
FROM model_3d 
LIMIT 6;"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig1_task1_select.png"),
    tab_title="01_select_basic.sql",
    sql_text=sql_t1,
    columns=list(t1["rows"][0].keys()),
    rows=t1["rows"],
    status_text="SELECT id_model, name, price... 6 row(s) returned"
)

# Task 2 screenshot: query 2.2 + rows
t2 = data[1]["items"][1] # 2.2
sql_t2 = """USE marketplace_3d;
-- Запит 2.2: Сортування моделей за зростанням ціни з урахуванням ПДВ (20%)
SELECT id_model, name, price, ROUND(price * 1.20, 2) AS price_with_vat 
FROM model_3d 
ORDER BY price ASC 
LIMIT 5;"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig2_task2_order.png"),
    tab_title="02_order_by.sql",
    sql_text=sql_t2,
    columns=list(t2["rows"][0].keys()),
    rows=t2["rows"],
    status_text="SELECT id_model, name, price... 5 row(s) returned"
)

# Task 3 screenshot: query 3.1 + rows
t3 = data[2]["items"][0] # 3.1
sql_t3 = """USE marketplace_3d;
-- Запит 3.1: Фільтрація моделей за списком категорій (IN)
SELECT id_model, name, id_category, price 
FROM model_3d 
WHERE id_category IN (1, 2, 8);"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig3_task3_filter.png"),
    tab_title="03_filtering.sql",
    sql_text=sql_t3,
    columns=list(t3["rows"][0].keys()),
    rows=t3["rows"],
    status_text="SELECT id_model, name, id_category... 4 row(s) returned"
)

# Task 4 screenshot: query 4.5 + rows
t4 = data[3]["items"][4] # 4.5
sql_t4 = """USE marketplace_3d;
-- Запит 4.5: Комплексна статистика за параметрами файлів моделей
SELECT 
    COUNT(id_file) AS total_files, 
    MIN(size_mb) AS min_file_size_mb, 
    MAX(size_mb) AS max_file_size_mb, 
    ROUND(AVG(size_mb), 2) AS avg_file_size_mb, 
    ROUND(SUM(size_mb), 2) AS total_storage_mb 
FROM model_file;"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig4_task4_aggregate.png"),
    tab_title="04_aggregate_functions.sql",
    sql_text=sql_t4,
    columns=list(t4["rows"][0].keys()),
    rows=t4["rows"],
    status_text="SELECT COUNT(id_file)... 1 row(s) returned"
)

# Task 5 screenshot: query 5.1 + rows
t5 = data[4]["items"][0] # 5.1
sql_t5 = """USE marketplace_3d;
-- Запит 5.1: Кількість 3D-моделей та середня ціна у розрізі категорій
SELECT 
    id_category, 
    COUNT(*) AS models_count, 
    ROUND(AVG(price), 2) AS avg_price 
FROM model_3d 
GROUP BY id_category 
ORDER BY models_count DESC;"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig5_task5_group.png"),
    tab_title="05_group_by_having.sql",
    sql_text=sql_t5,
    columns=list(t5["rows"][0].keys()),
    rows=t5["rows"],
    status_text="SELECT id_category, COUNT(*)... 10 row(s) returned"
)

# Task 6 screenshot: view 1 select + rows
t6 = data[5]["items"][0] # 6.1
sql_t6 = """USE marketplace_3d;
-- Запит до представлення view_popular_models
SELECT * 
FROM view_popular_models 
WHERE price >= 20.00 
ORDER BY price DESC;"""
render_workbench_screenshot(
    output_path=os.path.join(cache_dir, "fig6_task6_views.png"),
    tab_title="06_views.sql",
    sql_text=sql_t6,
    columns=list(t6["rows"][0].keys()),
    rows=t6["rows"],
    status_text="SELECT * FROM view_popular_models... 5 row(s) returned"
)

print("All 6 figures generated successfully!")
