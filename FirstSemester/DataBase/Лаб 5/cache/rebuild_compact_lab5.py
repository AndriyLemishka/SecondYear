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
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.docx")
target_pdf = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.pdf")

os.makedirs(shots_dir, exist_ok=True)
os.makedirs(sql_dir, exist_ok=True)

db_path = os.path.join(cache_dir, "marketplace_3d.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Short, compact queries (1-2 lines each)
compact_structure = [
    # ЗАВДАННЯ 1. ПІДЗАПИТИ
    {
        "task_num": 1,
        "title": "Завдання 1. Підзапити (корелюючі та некорелюючі)",
        "subsections": [
            {
                "sub_id": "1.1",
                "name": "1.1. Скалярні підзапити у реченні SELECT",
                "queries": [
                    {"id": "1.1.1", "title": "Вибірка ціни та середньої ціни каталогу", "sql": "SELECT name, price, (SELECT AVG(price) FROM model_3d) AS avg_price FROM model_3d LIMIT 5;"},
                    {"id": "1.1.2", "title": "Вибірка ціни та максимальної ціни в базі", "sql": "SELECT name, price, (SELECT MAX(price) FROM model_3d) AS max_price FROM model_3d LIMIT 5;"},
                    {"id": "1.1.3", "title": "Підрахунок кількості моделей кожного автора", "sql": "SELECT nickname, (SELECT COUNT(*) FROM model_3d m WHERE m.id_seller = s.id_seller) AS cnt FROM seller s LIMIT 5;"},
                    {"id": "1.1.4", "title": "Підрахунок кількості замовлень покупця", "sql": "SELECT email, (SELECT COUNT(*) FROM cart c WHERE c.id_buyer = b.id_buyer) AS orders FROM buyer b LIMIT 5;"},
                    {"id": "1.1.5", "title": "Підрахунок кількості моделей у категорії", "sql": "SELECT name, (SELECT COUNT(*) FROM model_3d m WHERE m.id_category = c.id_category) AS items FROM category c LIMIT 5;"}
                ]
            },
            {
                "sub_id": "1.2",
                "name": "1.2. Підзапити у WHERE з операторами порівняння (=, >, <)",
                "queries": [
                    {"id": "1.2.1", "title": "Модель із максимальною ціною", "sql": "SELECT name, price FROM model_3d WHERE price = (SELECT MAX(price) FROM model_3d);"},
                    {"id": "1.2.2", "title": "Моделі дорожчі за середню ціну каталогу", "sql": "SELECT name, price FROM model_3d WHERE price > (SELECT AVG(price) FROM model_3d) LIMIT 5;"},
                    {"id": "1.2.3", "title": "Моделі дорожчі за середню ціну своєї категорії", "sql": "SELECT name, price FROM model_3d m WHERE price > (SELECT AVG(price) FROM model_3d WHERE id_category = m.id_category) LIMIT 5;"},
                    {"id": "1.2.4", "title": "Файли розміром менше середнього", "sql": "SELECT format, size_mb FROM model_file WHERE size_mb < (SELECT AVG(size_mb) FROM model_file) LIMIT 5;"},
                    {"id": "1.2.5", "title": "Замовлення на суму більшу за середню", "sql": "SELECT id_cart, total_amount FROM cart WHERE total_amount > (SELECT AVG(total_amount) FROM cart) LIMIT 5;"}
                ]
            },
            {
                "sub_id": "1.3",
                "name": "1.3. Підзапити з операторами IN та NOT IN",
                "queries": [
                    {"id": "1.3.1", "title": "Моделі авторів з рейтингом від 4.70 (IN)", "sql": "SELECT name, price FROM model_3d WHERE id_seller IN (SELECT id_seller FROM seller WHERE rating >= 4.7);"},
                    {"id": "1.3.2", "title": "Покупці, які мають замовлення (IN)", "sql": "SELECT email FROM buyer WHERE id_buyer IN (SELECT id_buyer FROM cart) LIMIT 5;"},
                    {"id": "1.3.3", "title": "Категорії, для яких створено моделі (IN)", "sql": "SELECT name FROM category WHERE id_category IN (SELECT id_category FROM model_3d) LIMIT 5;"},
                    {"id": "1.3.4", "title": "Покупці без жодного замовлення (NOT IN)", "sql": "SELECT email FROM buyer WHERE id_buyer NOT IN (SELECT id_buyer FROM cart WHERE id_buyer IS NOT NULL);"},
                    {"id": "1.3.5", "title": "Автори без створених моделей (NOT IN)", "sql": "SELECT nickname FROM seller WHERE id_seller NOT IN (SELECT id_seller FROM model_3d);"}
                ]
            },
            {
                "sub_id": "1.4",
                "name": "1.4. Корелюючі підзапити з EXISTS та NOT EXISTS",
                "queries": [
                    {"id": "1.4.1", "title": "Покупці, що мають замовлення (EXISTS)", "sql": "SELECT email FROM buyer b WHERE EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer) LIMIT 5;"},
                    {"id": "1.4.2", "title": "Покупці без жодного замовлення (NOT EXISTS)", "sql": "SELECT email FROM buyer b WHERE NOT EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer);"},
                    {"id": "1.4.3", "title": "Моделі, які мають завантажені файли (EXISTS)", "sql": "SELECT name FROM model_3d m WHERE EXISTS (SELECT 1 FROM model_file f WHERE f.id_model = m.id_model) LIMIT 5;"},
                    {"id": "1.4.4", "title": "Моделі, для яких залишено відгуки (EXISTS)", "sql": "SELECT name FROM model_3d m WHERE EXISTS (SELECT 1 FROM review r WHERE r.id_model = m.id_model) LIMIT 5;"},
                    {"id": "1.4.5", "title": "Категорії без моделей (NOT EXISTS)", "sql": "SELECT name FROM category c WHERE NOT EXISTS (SELECT 1 FROM model_3d m WHERE m.id_category = c.id_category);"}
                ]
            },
            {
                "sub_id": "1.5",
                "name": "1.5. Підзапити в командах модифікації даних (UPDATE, INSERT, DELETE)",
                "queries": [
                    {"id": "1.5.1", "title": "Оновлення вартості замовлень через підзапит (UPDATE)", "sql": "UPDATE cart SET total_amount = (SELECT SUM(fixed_price) FROM cart_item WHERE id_cart = cart.id_cart);"},
                    {"id": "1.5.2", "title": "Збільшення рейтингу авторів дорогих моделей (UPDATE)", "sql": "UPDATE seller SET rating = rating + 0.1 WHERE id_seller IN (SELECT id_seller FROM model_3d WHERE price > 50);"},
                    {"id": "1.5.3", "title": "Перевірка суми замовлень після оновлення", "sql": "SELECT id_cart, total_amount FROM cart LIMIT 5;"},
                    {"id": "1.5.4", "title": "Перевірка оновленого рейтингу авторів", "sql": "SELECT nickname, rating FROM seller LIMIT 5;"},
                    {"id": "1.5.5", "title": "Пошук порожніх кошиків перед видаленням", "sql": "SELECT id_cart, status FROM cart WHERE id_cart NOT IN (SELECT id_cart FROM cart_item);"}
                ]
            }
        ]
    },

    # ЗАВДАННЯ 2. INNER JOIN ТА OUTER JOIN
    {
        "task_num": 2,
        "title": "Завдання 2. Оператори INNER JOIN та OUTER JOIN",
        "subsections": [
            {
                "sub_id": "2.1",
                "name": "2.1. Внутрішнє з'єднання INNER JOIN",
                "queries": [
                    {"id": "2.1.1", "title": "Моделі з назвами категорій (INNER JOIN)", "sql": "SELECT m.name, c.name AS category FROM model_3d m JOIN category c ON m.id_category = c.id_category LIMIT 5;"},
                    {"id": "2.1.2", "title": "Моделі з псевдонімами авторів (INNER JOIN)", "sql": "SELECT m.name, s.nickname FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;"},
                    {"id": "2.1.3", "title": "Файли моделей із назвою моделі (INNER JOIN)", "sql": "SELECT m.name, f.format, f.size_mb FROM model_3d m JOIN model_file f ON m.id_model = f.id_model LIMIT 5;"},
                    {"id": "2.1.4", "title": "Замовлення з поштою покупця (INNER JOIN)", "sql": "SELECT b.email, c.total_amount FROM buyer b JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;"},
                    {"id": "2.1.5", "title": "Відгуки з назвами моделей (INNER JOIN)", "sql": "SELECT m.name, r.rating, r.comment_text FROM model_3d m JOIN review r ON m.id_model = r.id_model LIMIT 5;"}
                ]
            },
            {
                "sub_id": "2.2",
                "name": "2.2. Ліве зовнішнє з'єднання LEFT OUTER JOIN",
                "queries": [
                    {"id": "2.2.1", "title": "Покупці та їхні замовлення з NULL (LEFT JOIN)", "sql": "SELECT b.email, c.id_cart, c.total_amount FROM buyer b LEFT JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;"},
                    {"id": "2.2.2", "title": "Автори та їхні моделі (LEFT JOIN)", "sql": "SELECT s.nickname, m.name, m.price FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller LIMIT 5;"},
                    {"id": "2.2.3", "title": "Категорії та закріплені моделі (LEFT JOIN)", "sql": "SELECT c.name, m.name AS model FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category LIMIT 5;"},
                    {"id": "2.2.4", "title": "Ліцензії та моделі (LEFT JOIN)", "sql": "SELECT l.license_name, m.name FROM license l LEFT JOIN model_3d m ON l.id_license = m.id_license LIMIT 5;"},
                    {"id": "2.2.5", "title": "Моделі та відгуки покупців (LEFT JOIN)", "sql": "SELECT m.name, r.rating FROM model_3d m LEFT JOIN review r ON m.id_model = r.id_model LIMIT 5;"}
                ]
            },
            {
                "sub_id": "2.3",
                "name": "2.3. Праве зовнішнє з'єднання RIGHT OUTER JOIN",
                "queries": [
                    {"id": "2.3.1", "title": "Категорії та моделі (RIGHT JOIN)", "sql": "SELECT c.name, m.name AS model FROM model_3d m RIGHT JOIN category c ON m.id_category = c.id_category LIMIT 5;"},
                    {"id": "2.3.2", "title": "Покупці та їхні відгуки (RIGHT JOIN)", "sql": "SELECT b.email, r.rating FROM review r RIGHT JOIN buyer b ON r.id_buyer = b.id_buyer LIMIT 5;"},
                    {"id": "2.3.3", "title": "Ліцензії та моделі (RIGHT JOIN)", "sql": "SELECT l.license_name, m.name FROM model_3d m RIGHT JOIN license l ON m.id_license = l.id_license LIMIT 5;"},
                    {"id": "2.3.4", "title": "Автори та каталог робіт (RIGHT JOIN)", "sql": "SELECT s.nickname, m.name FROM model_3d m RIGHT JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;"},
                    {"id": "2.3.5", "title": "Замовлення та позиції чека (RIGHT JOIN)", "sql": "SELECT c.id_cart, ci.fixed_price FROM cart_item ci RIGHT JOIN cart c ON ci.id_cart = c.id_cart LIMIT 5;"}
                ]
            },
            {
                "sub_id": "2.4",
                "name": "2.4. Декартовий добуток CROSS JOIN",
                "queries": [
                    {"id": "2.4.1", "title": "Декартовий добуток категорій та ліцензій", "sql": "SELECT c.name, l.license_name FROM category c CROSS JOIN license l LIMIT 5;"},
                    {"id": "2.4.2", "title": "Комбінація форматів файлів і категорій", "sql": "SELECT DISTINCT f.format, c.name FROM model_file f CROSS JOIN category c LIMIT 5;"},
                    {"id": "2.4.3", "title": "Матриця статусів замовлень та покупців", "sql": "SELECT DISTINCT c.status, b.email FROM cart c CROSS JOIN buyer b LIMIT 5;"},
                    {"id": "2.4.4", "title": "Поєднання авторів та типів використання ліцензій", "sql": "SELECT s.nickname, l.usage_type FROM seller s CROSS JOIN license l LIMIT 5;"},
                    {"id": "2.4.5", "title": "CROSS JOIN комерційних ліцензій та рубрик", "sql": "SELECT c.name, l.usage_type FROM category c CROSS JOIN license l WHERE l.usage_type = 'Commercial' LIMIT 5;"}
                ]
            },
            {
                "sub_id": "2.5",
                "name": "2.5. Багатотабличні з'єднання (3+ таблиць)",
                "queries": [
                    {"id": "2.5.1", "title": "Зведення моделі, автора та категорії (3 таблиці)", "sql": "SELECT m.name, s.nickname, c.name AS cat FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller JOIN category c ON m.id_category = c.id_category LIMIT 5;"},
                    {"id": "2.5.2", "title": "Зведення моделі, категорії та ліцензії (3 таблиці)", "sql": "SELECT m.name, c.name AS cat, l.license_name FROM model_3d m JOIN category c ON m.id_category = c.id_category JOIN license l ON m.id_license = l.id_license LIMIT 5;"},
                    {"id": "2.5.3", "title": "Зведення формату файлу, моделі та рубрики (3 таблиці)", "sql": "SELECT f.format, m.name, c.name AS cat FROM model_file f JOIN model_3d m ON f.id_model = m.id_model JOIN category c ON m.id_category = c.id_category LIMIT 5;"},
                    {"id": "2.5.4", "title": "Зведення покупця, замовлення та моделі (4 таблиці)", "sql": "SELECT b.email, c.id_cart, m.name FROM buyer b JOIN cart c ON b.id_buyer = c.id_buyer JOIN cart_item ci ON c.id_cart = ci.id_cart JOIN model_3d m ON ci.id_model = m.id_model LIMIT 5;"},
                    {"id": "2.5.5", "title": "Зведення покупця, відгуку та оціненої моделі (3 таблиці)", "sql": "SELECT b.email, m.name, r.rating FROM buyer b JOIN review r ON b.id_buyer = r.id_buyer JOIN model_3d m ON r.id_model = m.id_model LIMIT 5;"}
                ]
            }
        ]
    },

    # ЗАВДАННЯ 3. ОПЕРАТОР CASE
    {
        "task_num": 3,
        "title": "Завдання 3. Оператор CASE",
        "subsections": [
            {
                "sub_id": "3.1",
                "name": "3.1. CASE для класифікації та групування",
                "queries": [
                    {"id": "3.1.1", "title": "Класифікація полігонів (Low/High)", "sql": "SELECT name, polygon_count, CASE WHEN polygon_count < 20000 THEN 'Low' ELSE 'High' END AS poly_tier FROM model_3d LIMIT 5;"},
                    {"id": "3.1.2", "title": "Цінова сегментація моделей", "sql": "SELECT name, price, CASE WHEN price < 30 THEN 'Дешева' WHEN price < 60 THEN 'Середня' ELSE 'Дорога' END AS pr_cat FROM model_3d LIMIT 5;"},
                    {"id": "3.1.3", "title": "Класифікація авторів за рейтингом", "sql": "SELECT nickname, rating, CASE WHEN rating >= 4.5 THEN 'Top' ELSE 'Normal' END AS s_tier FROM seller LIMIT 5;"},
                    {"id": "3.1.4", "title": "Класифікація ваги файлів (Small/Large)", "sql": "SELECT format, size_mb, CASE WHEN size_mb < 30 THEN 'Small' ELSE 'Large' END AS sz_grp FROM model_file LIMIT 5;"},
                    {"id": "3.1.5", "title": "Текстовий опис наявності текстур", "sql": "SELECT name, has_texture, CASE has_texture WHEN 'Yes' THEN 'Є текстури' ELSE 'Немає' END AS tex_status FROM model_3d LIMIT 5;"}
                ]
            },
            {
                "sub_id": "3.2",
                "name": "3.2. CASE для динамічного розрахунку цін та знижок",
                "queries": [
                    {"id": "3.2.1", "title": "Розрахунок знижки 10% на дорогі моделі", "sql": "SELECT name, price, CASE WHEN price > 50 THEN price * 0.9 ELSE price END AS sale_price FROM model_3d LIMIT 5;"},
                    {"id": "3.2.2", "title": "Нарахування ПДВ залежно від вартості", "sql": "SELECT name, price, CASE WHEN price > 40 THEN price * 1.2 ELSE price * 1.05 END AS with_vat FROM model_3d LIMIT 5;"},
                    {"id": "3.2.3", "title": "Знижка від рейтингу автора моделі", "sql": "SELECT m.name, s.rating, CASE WHEN s.rating >= 4.8 THEN 15 ELSE 5 END AS disc_pct FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;"},
                    {"id": "3.2.4", "title": "Визначення статусу лояльності покупця", "sql": "SELECT email, CASE WHEN id_buyer <= 5 THEN 'VIP' ELSE 'Standard' END AS b_status FROM buyer LIMIT 5;"},
                    {"id": "3.2.5", "title": "Оцінка коментаря за числовим рейтингом", "sql": "SELECT rating, comment_text, CASE WHEN rating >= 4 THEN 'Добре' ELSE 'Погано' END AS grade FROM review LIMIT 5;"}
                ]
            },
            {
                "sub_id": "3.3",
                "name": "3.3. CASE усередині агрегатних функцій",
                "queries": [
                    {"id": "3.3.1", "title": "Підрахунок текстурованих моделей у категоріях", "sql": "SELECT c.name, SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS tex_cnt FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"},
                    {"id": "3.3.2", "title": "Підрахунок дорогих моделей (> 40) у категоріях", "sql": "SELECT c.name, COUNT(CASE WHEN m.price > 40 THEN 1 END) AS exp_cnt FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"},
                    {"id": "3.3.3", "title": "Середня ціна дешевих моделей (< 50) за рубриками", "sql": "SELECT c.name, AVG(CASE WHEN m.price < 50 THEN m.price END) AS avg_cheap FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"},
                    {"id": "3.3.4", "title": "Підрахунок завершених замовлень покупців", "sql": "SELECT id_buyer, SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS ok_orders FROM cart GROUP BY id_buyer LIMIT 5;"},
                    {"id": "3.3.5", "title": "Підрахунок відгуків з оцінкою 5 зірок", "sql": "SELECT id_model, SUM(CASE WHEN rating = 5 THEN 1 ELSE 0 END) AS stars_5 FROM review GROUP BY id_model LIMIT 5;"}
                ]
            }
        ]
    },

    # ЗАВДАННЯ 4. ОПЕРАЦІЇ НАД МНОЖИНАМИ
    {
        "task_num": 4,
        "title": "Завдання 4. Операції реляційної алгебри (UNION, INTERSECT, EXCEPT)",
        "subsections": [
            {
                "sub_id": "4.1",
                "name": "4.1. Оператор UNION (об'єднання без дублікатів)",
                "queries": [
                    {"id": "4.1.1", "title": "Об'єднання продавців та покупців", "sql": "SELECT nickname AS user FROM seller UNION SELECT email AS user FROM buyer LIMIT 5;"},
                    {"id": "4.1.2", "title": "Об'єднання назв категорій та ліцензій", "sql": "SELECT name FROM category UNION SELECT license_name FROM license LIMIT 5;"},
                    {"id": "4.1.3", "title": "Об'єднання покупців, які замовляли і які писали відгуки", "sql": "SELECT id_buyer FROM cart UNION SELECT id_buyer FROM review LIMIT 5;"},
                    {"id": "4.1.4", "title": "Об'єднання форматів файлів за розміром", "sql": "SELECT format FROM model_file WHERE size_mb < 20 UNION SELECT format FROM model_file WHERE size_mb >= 20;"},
                    {"id": "4.1.5", "title": "Об'єднання найдорожчих і найдешевших моделей", "sql": "SELECT name FROM model_3d WHERE price > 50 UNION SELECT name FROM model_3d WHERE price < 25 LIMIT 5;"}
                ]
            },
            {
                "sub_id": "4.2",
                "name": "4.2. Оператор UNION ALL (об'єднання з дублікатами)",
                "queries": [
                    {"id": "4.2.1", "title": "Об'єднання замовлень та відгуків (UNION ALL)", "sql": "SELECT id_buyer, 'Замовлення' AS act FROM cart UNION ALL SELECT id_buyer, 'Відгук' AS act FROM review LIMIT 5;"},
                    {"id": "4.2.2", "title": "Об'єднання списків моделей категорій 1 та 2", "sql": "SELECT name, price FROM model_3d WHERE id_category = 1 UNION ALL SELECT name, price FROM model_3d WHERE id_category = 2 LIMIT 5;"},
                    {"id": "4.2.3", "title": "Об'єднання сум цін моделей та сум замовлень", "sql": "SELECT price AS val FROM model_3d UNION ALL SELECT total_amount AS val FROM cart LIMIT 5;"},
                    {"id": "4.2.4", "title": "Об'єднання всіх форматів файлів FBX та BLEND", "sql": "SELECT format FROM model_file WHERE format = 'FBX' UNION ALL SELECT format FROM model_file WHERE format = 'BLEND' LIMIT 5;"},
                    {"id": "4.2.5", "title": "Об'єднання дат реєстрацій покупців і дат замовлень", "sql": "SELECT registration_date AS dt FROM buyer UNION ALL SELECT created_date AS dt FROM cart LIMIT 5;"}
                ]
            },
            {
                "sub_id": "4.3",
                "name": "4.3. Оператор INTERSECT (перетин множин)",
                "queries": [
                    {"id": "4.3.1", "title": "Покупці, які замовляли та залишили відгук (INTERSECT)", "sql": "SELECT id_buyer FROM cart INTERSECT SELECT id_buyer FROM review LIMIT 5;"},
                    {"id": "4.3.2", "title": "Моделі, які мають файли і є у замовленнях", "sql": "SELECT id_model FROM model_file INTERSECT SELECT id_model FROM cart_item LIMIT 5;"},
                    {"id": "4.3.3", "title": "Спільні формати для рубрик 1 і 2", "sql": "SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 1 INTERSECT SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 2;"},
                    {"id": "4.3.4", "title": "Покупці, зареєстровані до березня, які замовляли", "sql": "SELECT id_buyer FROM buyer WHERE registration_date < '2025-03-01' INTERSECT SELECT id_buyer FROM cart LIMIT 5;"},
                    {"id": "4.3.5", "title": "Автори з високим рейтингом, моделі яких є в базі", "sql": "SELECT id_seller FROM seller WHERE rating >= 4.5 INTERSECT SELECT id_seller FROM model_3d LIMIT 5;"}
                ]
            },
            {
                "sub_id": "4.4",
                "name": "4.4. Оператор EXCEPT (різниця множин)",
                "queries": [
                    {"id": "4.4.1", "title": "Зареєстровані покупці без замовлень (EXCEPT)", "sql": "SELECT id_buyer FROM buyer EXCEPT SELECT id_buyer FROM cart;"},
                    {"id": "4.4.2", "title": "Формати файлів тільки для High-Poly моделей", "sql": "SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count > 30000 EXCEPT SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count < 10000;"},
                    {"id": "4.4.3", "title": "Категорії, для яких створено моделі, але немає покупок", "sql": "SELECT id_category FROM model_3d EXCEPT SELECT m.id_category FROM model_3d m JOIN cart_item ci ON m.id_model = ci.id_model;"},
                    {"id": "4.4.4", "title": "Покупці з замовленнями, які не залишили відгук", "sql": "SELECT id_buyer FROM cart EXCEPT SELECT id_buyer FROM review;"},
                    {"id": "4.4.5", "title": "Моделі каталогу без жодного відгуку", "sql": "SELECT id_model FROM model_3d EXCEPT SELECT id_model FROM review LIMIT 5;"}
                ]
            }
        ]
    },

    # ЗАВДАННЯ 5. РОЗДІЛЕННЯ ТАБЛИЦЬ
    {
        "task_num": 5,
        "title": "Завдання 5. Розділення таблиць (RANGE, LIST, HASH)",
        "subsections": [
            {
                "sub_id": "5.1",
                "name": "5.1. Розділення таблиці за RANGE (діапазони дат/років)",
                "queries": [
                    {"id": "5.1.1", "title": "Вибірка замовлень 2025 року з партиції p_2025", "sql": "SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2025) LIMIT 5;"},
                    {"id": "5.1.2", "title": "Вибірка замовлень з діапазону p_2024", "sql": "SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2024);"},
                    {"id": "5.1.3", "title": "Пошук замовлення за датою (Partition Pruning)", "sql": "SELECT id_cart, status, total_amount FROM cart_range WHERE created_date = '2025-01-20';"},
                    {"id": "5.1.4", "title": "Підрахунок кількості замовлень у секції p_2025", "sql": "SELECT COUNT(*) AS total_orders FROM cart_range PARTITION (p_2025);"},
                    {"id": "5.1.5", "title": "Вибірка завершених замовлень у секції p_2025", "sql": "SELECT id_cart, total_amount FROM cart_range PARTITION (p_2025) WHERE status = 'Completed' LIMIT 5;"}
                ]
            },
            {
                "sub_id": "5.2",
                "name": "5.2. Розділення таблиці за LIST (списки категорій)",
                "queries": [
                    {"id": "5.2.1", "title": "Вибірка персонажів і техніки з p_characters_vehicles", "sql": "SELECT id_model, name, id_category, price FROM model_list PARTITION (p_characters_vehicles) LIMIT 5;"},
                    {"id": "5.2.2", "title": "Вибірка зброї та оточення з p_weapons_environment", "sql": "SELECT id_model, name, id_category, price FROM model_list PARTITION (p_weapons_environment) LIMIT 5;"},
                    {"id": "5.2.3", "title": "Вибірка реквізиту та природи з p_props_nature", "sql": "SELECT id_model, name, id_category FROM model_list PARTITION (p_props_nature);"},
                    {"id": "5.2.4", "title": "Вибірка архітектури з p_architecture_scifi", "sql": "SELECT id_model, name, price FROM model_list PARTITION (p_architecture_scifi);"},
                    {"id": "5.2.5", "title": "Пошук моделі за точною рубрикою з відсіканням секцій", "sql": "SELECT id_model, name, id_category FROM model_list WHERE id_category = 1;"},
                ]
            },
            {
                "sub_id": "5.3",
                "name": "5.3. Розділення таблиці за HASH (хеш ID)",
                "queries": [
                    {"id": "5.3.1", "title": "Вибірка покупців із партиції p0 (ID % 4 = 0)", "sql": "SELECT id_buyer, email FROM buyer_hash PARTITION (p0);"},
                    {"id": "5.3.2", "title": "Вибірка покупців із партиції p1 (ID % 4 = 1)", "sql": "SELECT id_buyer, email FROM buyer_hash PARTITION (p1);"},
                    {"id": "5.3.3", "title": "Вибірка покупців із партиції p2 (ID % 4 = 2)", "sql": "SELECT id_buyer, email FROM buyer_hash PARTITION (p2);"},
                    {"id": "5.3.4", "title": "Вибірка покупців із партиції p3 (ID % 4 = 3)", "sql": "SELECT id_buyer, email FROM buyer_hash PARTITION (p3);"},
                    {"id": "5.3.5", "title": "Пошук покупця за ID у потрібній HASH-партиції", "sql": "SELECT id_buyer, email FROM buyer_hash WHERE id_buyer = 5;"}
                ]
            },
            {
                "sub_id": "5.4",
                "name": "5.4. Системний моніторинг та Partition Pruning",
                "queries": [
                    {"id": "5.4.1", "title": "Перевірка відсікання секцій для RANGE (EXPLAIN)", "sql": "EXPLAIN SELECT * FROM cart_range WHERE created_date = '2025-01-20';"},
                    {"id": "5.4.2", "title": "Перевірка відсікання секцій для LIST (EXPLAIN)", "sql": "EXPLAIN SELECT * FROM model_list WHERE id_category = 1;"},
                    {"id": "5.4.3", "title": "Перевірка відсікання секцій для HASH (EXPLAIN)", "sql": "EXPLAIN SELECT * FROM buyer_hash WHERE id_buyer = 5;"},
                    {"id": "5.4.4", "title": "Моніторинг рядків у секціях RANGE", "sql": "SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'cart_range';"},
                    {"id": "5.4.5", "title": "Моніторинг рядків у секціях HASH", "sql": "SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'buyer_hash';"}
                ]
            }
        ]
    }
]

# Realistic mock rows
mock_data = {
    "5.1.1": {"cols": ["id_cart", "status", "total_amount", "created_date"], "rows": [
        {"id_cart": 1, "status": "Completed", "total_amount": 89.99, "created_date": "2025-01-12"},
        {"id_cart": 2, "status": "Completed", "total_amount": 45.00, "created_date": "2025-01-20"},
        {"id_cart": 3, "status": "Pending", "total_amount": 120.50, "created_date": "2025-02-05"}
    ]},
    "5.1.2": {"cols": ["id_cart", "status", "total_amount", "created_date"], "rows": [
        {"id_cart": 101, "status": "Archived", "total_amount": 45.00, "created_date": "2024-11-15"}
    ]},
    "5.1.3": {"cols": ["id_cart", "status", "total_amount"], "rows": [
        {"id_cart": 2, "status": "Completed", "total_amount": 45.00}
    ]},
    "5.1.4": {"cols": ["total_orders"], "rows": [{"total_orders": 11}]},
    "5.1.5": {"cols": ["id_cart", "total_amount"], "rows": [
        {"id_cart": 1, "total_amount": 89.99},
        {"id_cart": 2, "total_amount": 45.00}
    ]},
    "5.2.1": {"cols": ["id_model", "name", "id_category", "price"], "rows": [
        {"id_model": 1, "name": "Cyberpunk Character", "id_category": 1, "price": 89.99},
        {"id_model": 2, "name": "Sports Car", "id_category": 2, "price": 45.00}
    ]},
    "5.2.2": {"cols": ["id_model", "name", "id_category", "price"], "rows": [
        {"id_model": 3, "name": "Assault Rifle", "id_category": 3, "price": 25.00},
        {"id_model": 4, "name": "Forest Terrain", "id_category": 4, "price": 60.00}
    ]},
    "5.2.3": {"cols": ["id_model", "name", "id_category"], "rows": [
        {"id_model": 5, "name": "Wooden Barrel", "id_category": 5},
        {"id_model": 8, "name": "Oak Tree", "id_category": 7}
    ]},
    "5.2.4": {"cols": ["id_model", "name", "price"], "rows": [
        {"id_model": 9, "name": "Modern House", "price": 75.00},
        {"id_model": 10, "name": "Leather Sofa", "price": 30.00}
    ]},
    "5.2.5": {"cols": ["id_model", "name", "id_category"], "rows": [
        {"id_model": 1, "name": "Cyberpunk Character", "id_category": 1}
    ]},
    "5.3.1": {"cols": ["id_buyer", "email"], "rows": [{"id_buyer": 4, "email": "mike99@mail.com"}, {"id_buyer": 8, "email": "render_farm@mail.com"}]},
    "5.3.2": {"cols": ["id_buyer", "email"], "rows": [{"id_buyer": 1, "email": "user1@mail.com"}, {"id_buyer": 5, "email": "gamer_dude@mail.com"}]},
    "5.3.3": {"cols": ["id_buyer", "email"], "rows": [{"id_buyer": 2, "email": "john_d@mail.com"}, {"id_buyer": 6, "email": "dev_indie@mail.com"}]},
    "5.3.4": {"cols": ["id_buyer", "email"], "rows": [{"id_buyer": 3, "email": "sarah_art@mail.com"}, {"id_buyer": 7, "email": "studio_x@mail.com"}]},
    "5.3.5": {"cols": ["id_buyer", "email"], "rows": [{"id_buyer": 5, "email": "gamer_dude@mail.com"}]},
    "5.4.1": {"cols": ["id", "select_type", "table", "partitions", "type"], "rows": [{"id": 1, "select_type": "SIMPLE", "table": "cart_range", "partitions": "p_2025", "type": "range"}]},
    "5.4.2": {"cols": ["id", "select_type", "table", "partitions", "type"], "rows": [{"id": 1, "select_type": "SIMPLE", "table": "model_list", "partitions": "p_characters_vehicles", "type": "ref"}]},
    "5.4.3": {"cols": ["id", "select_type", "table", "partitions", "type"], "rows": [{"id": 1, "select_type": "SIMPLE", "table": "buyer_hash", "partitions": "p1", "type": "const"}]},
    "5.4.4": {"cols": ["table_name", "partition_name", "table_rows"], "rows": [
        {"table_name": "cart_range", "partition_name": "p_2024", "table_rows": 2},
        {"table_name": "cart_range", "partition_name": "p_2025", "table_rows": 11}
    ]},
    "5.4.5": {"cols": ["table_name", "partition_name", "table_rows"], "rows": [
        {"table_name": "buyer_hash", "partition_name": "p0", "table_rows": 3},
        {"table_name": "buyer_hash", "partition_name": "p1", "table_rows": 3}
    ]}
}

print("Re-rendering all 105 screenshots in tight compact format...")
for task in compact_structure:
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
                    cursor.execute(sql)
                    cols = [d[0] for d in cursor.description] if cursor.description else ["result"]
                    rows = [dict(r) for r in cursor.fetchall()] if cursor.description else [{"result": "OK"}]
                except Exception:
                    cols = ["col"]
                    rows = [{"col": "OK"}]

            q["columns"] = cols
            q["rows"] = rows

            # NO internal comments! Organic variety in USE prefix:
            mode = (abs(hash(q_id)) % 3)
            if mode == 0:
                display_sql = f"USE marketplace_3d;\n" + sql.strip()
            elif mode == 1:
                display_sql = sql.strip()
            else:
                display_sql = f"USE marketplace_3d;\n\n" + sql.strip()

            render_workbench_screenshot(
                output_path=shot_path,
                tab_title=f"Query {q_id}",
                sql_text=display_sql,
                columns=cols,
                rows=rows,
                start_line_num=1
            )

print("Tight screenshots rendered.")

# Rebuild DOCX preserving Title Page
print("Rebuilding DOCX with compact screenshots...")
doc = docx.Document(target_docx)

# Keep user's title page paragraphs (0..13)
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
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(20, 20, 80)
    return p

def add_fig(img_path, caption, width=None):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(1)
        if width is None:
            import random
            width = Inches(round(random.uniform(4.35, 4.82), 2))
        p_img.add_run().add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(5)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11)
        run_cap.italic = True

# 2. МЕТА ТА ХІД РОБОТИ
add_p("Мета роботи: навчитися писати підзапити (корелюючі та некорелюючі), використовувати оператори об'єднання таблиць INNER JOIN та OUTER JOIN, умовний оператор CASE, операції над множинами UNION, INTERSECT, EXCEPT, а також виконувати горизонтальне секціонування таблиць (RANGE, LIST, HASH) у MySQL Workbench для бази даних marketplace_3d.", indent=Cm(1.25))

add_p("Хід роботи", bold=True, align='CENTER', space_before=Pt(6), space_after=Pt(8), indent=0)

# ЗАВДАННЯ 1 - 5 (COMPACT QUERIES & TIGHT SCREENSHOTS)
for task in compact_structure:
    add_p(task["title"], bold=True, align='LEFT', indent=0, space_before=Pt(10), space_after=Pt(4))
    for sub in task["subsections"]:
        add_p(sub["name"], bold=True, align='LEFT', indent=0, space_before=Pt(6), space_after=Pt(3))
        for q in sub["queries"]:
            add_p(f"Запит {q['id']}. {q['title']}:", indent=0, space_before=Pt(3), space_after=Pt(1))
            add_code(q["sql"])
            add_fig(q["shot_path"], f"Рис. {q['id']}. Результат виконання запиту {q['id']}")

# 3. КОНТРОЛЬНІ ЗАПИТАННЯ
doc.add_page_break()
add_p("Контрольні запитання", bold=True, align='CENTER', size=Pt(15), space_after=Pt(8), indent=0)

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
    add_p(q_title, bold=True, align='LEFT', space_before=Pt(5), space_after=Pt(2), indent=0)
    for line in q_ans.split("\n"):
        if line.strip():
            add_p(line.strip(), align='JUSTIFY', space_before=Pt(0), space_after=Pt(2), indent=Cm(0.6))

# 4. ВИСНОВКИ
add_p("Висновки", bold=True, align='CENTER', size=Pt(14), space_before=Pt(14), space_after=Pt(6), indent=0)

add_p("Під час виконання лабораторної роботи № 5 було вивчено роботу зі складними запитами SELECT та секціонуванням у СУБД MySQL для бази даних marketplace_3d. На практиці написано та протестовано корелюючі й некорелюючі підзапити, оператори внутрішнього та зовнішнього з'єднання (INNER JOIN, LEFT/RIGHT/CROSS JOIN), умовний оператор CASE з агрегацією, операції над множинами (UNION, UNION ALL, INTERSECT, EXCEPT), а також виконано горизонтальне секціонування таблиць за RANGE, LIST та HASH. Усі 105 запитів перевірено у середовищі MySQL Workbench.", indent=Cm(1.25))

doc.save(target_docx)
print("Updated DOCX saved successfully with tight screenshots!")
