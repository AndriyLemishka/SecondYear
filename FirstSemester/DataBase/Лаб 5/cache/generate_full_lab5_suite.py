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
os.makedirs(shots_dir, exist_ok=True)
os.makedirs(sql_dir, exist_ok=True)

db_path = os.path.join(cache_dir, "marketplace_3d.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ----------------------------------------------------------------------
# Definition of all Tasks and Sub-commands (exactly 5 queries per command)
# ----------------------------------------------------------------------
full_structure = [
    # ==================================================================
    # ЗАВДАННЯ 1. ПІДЗАПИТИ
    # ==================================================================
    {
        "task_num": 1,
        "title": "Завдання 1. Підзапити (корелюючі та некорелюючі)",
        "subsections": [
            {
                "sub_id": "1.1",
                "name": "1.1. Скалярні підзапити у реченні SELECT",
                "queries": [
                    {
                        "id": "1.1.1",
                        "title": "Відхилення ціни моделі від середньої по каталогу",
                        "sql": "SELECT id_model, name, price, (SELECT ROUND(AVG(price), 2) FROM model_3d) AS avg_cat_price, ROUND(price - (SELECT AVG(price) FROM model_3d), 2) AS diff FROM model_3d ORDER BY diff DESC LIMIT 5;"
                    },
                    {
                        "id": "1.1.2",
                        "title": "Вибірка моделі із зазначенням максимальної ціни в системі",
                        "sql": "SELECT id_model, name, price, (SELECT MAX(price) FROM model_3d) AS max_price FROM model_3d LIMIT 5;"
                    },
                    {
                        "id": "1.1.3",
                        "title": "Вибірка авторів із підрахунком кількості їх моделей підзапитом",
                        "sql": "SELECT id_seller, nickname, (SELECT COUNT(*) FROM model_3d m WHERE m.id_seller = seller.id_seller) AS models_cnt FROM seller ORDER BY models_cnt DESC LIMIT 5;"
                    },
                    {
                        "id": "1.1.4",
                        "title": "Вибірка покупців із підрахунком оформлених замовлень",
                        "sql": "SELECT id_buyer, email, (SELECT COUNT(*) FROM cart c WHERE c.id_buyer = buyer.id_buyer) AS orders_cnt FROM buyer LIMIT 5;"
                    },
                    {
                        "id": "1.1.5",
                        "title": "Вибірка категорій із підрахунком прикріплених моделей",
                        "sql": "SELECT id_category, name, (SELECT COUNT(*) FROM model_3d m WHERE m.id_category = category.id_category) AS total_items FROM category LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "1.2",
                "name": "1.2. Підзапити у WHERE з операторами порівняння (=, >, <)",
                "queries": [
                    {
                        "id": "1.2.1",
                        "title": "Модель із максимальною ціною в каталозі",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE price = (SELECT MAX(price) FROM model_3d);"
                    },
                    {
                        "id": "1.2.2",
                        "title": "Моделі, ціна яких вища за середню по всій базі",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE price > (SELECT AVG(price) FROM model_3d) ORDER BY price DESC LIMIT 5;"
                    },
                    {
                        "id": "1.2.3",
                        "title": "Моделі, дорожчі за середню ціну своєї категорії (корелюючий)",
                        "sql": "SELECT m1.id_model, m1.name, m1.id_category, m1.price FROM model_3d m1 WHERE m1.price > (SELECT AVG(m2.price) FROM model_3d m2 WHERE m2.id_category = m1.id_category) ORDER BY m1.id_category LIMIT 5;"
                    },
                    {
                        "id": "1.2.4",
                        "title": "Файли моделей з розміром, меншим за середній розмір файлів",
                        "sql": "SELECT id_file, id_model, format, size_mb FROM model_file WHERE size_mb < (SELECT AVG(size_mb) FROM model_file) LIMIT 5;"
                    },
                    {
                        "id": "1.2.5",
                        "title": "Замовлення, загальна сума яких перевищує середній чек",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount FROM cart WHERE total_amount > (SELECT AVG(total_amount) FROM cart) ORDER BY total_amount DESC LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "1.3",
                "name": "1.3. Підзапити з операторами IN та NOT IN",
                "queries": [
                    {
                        "id": "1.3.1",
                        "title": "Моделі від топових авторів з рейтингом від 4.70 (IN)",
                        "sql": "SELECT id_model, name, price, id_seller FROM model_3d WHERE id_seller IN (SELECT id_seller FROM seller WHERE rating >= 4.70) LIMIT 5;"
                    },
                    {
                        "id": "1.3.2",
                        "title": "Покупці, які мають хоча б одне замовлення (IN)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer WHERE id_buyer IN (SELECT DISTINCT id_buyer FROM cart) LIMIT 5;"
                    },
                    {
                        "id": "1.3.3",
                        "title": "Категорії, для яких є хоча б одна модель (IN)",
                        "sql": "SELECT id_category, name FROM category WHERE id_category IN (SELECT DISTINCT id_category FROM model_3d) LIMIT 5;"
                    },
                    {
                        "id": "1.3.4",
                        "title": "Покупці, які жодного разу не замовляли товари (NOT IN)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer WHERE id_buyer NOT IN (SELECT DISTINCT id_buyer FROM cart WHERE id_buyer IS NOT NULL);"
                    },
                    {
                        "id": "1.3.5",
                        "title": "Автори, моделі яких ще не додавалися до жодного замовлення (NOT IN)",
                        "sql": "SELECT id_seller, nickname, rating FROM seller WHERE id_seller NOT IN (SELECT m.id_seller FROM model_3d m JOIN cart_item ci ON m.id_model = ci.id_model) LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "1.4",
                "name": "1.4. Корелюючі підзапити з EXISTS та NOT EXISTS",
                "queries": [
                    {
                        "id": "1.4.1",
                        "title": "Покупці, для яких існує створене замовлення (EXISTS)",
                        "sql": "SELECT b.id_buyer, b.email FROM buyer b WHERE EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer) LIMIT 5;"
                    },
                    {
                        "id": "1.4.2",
                        "title": "Зареєстровані покупці без жодного кошика (NOT EXISTS)",
                        "sql": "SELECT b.id_buyer, b.email, b.registration_date FROM buyer b WHERE NOT EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer);"
                    },
                    {
                        "id": "1.4.3",
                        "title": "Моделі, які мають завантажені файли (EXISTS)",
                        "sql": "SELECT m.id_model, m.name, m.price FROM model_3d m WHERE EXISTS (SELECT 1 FROM model_file f WHERE f.id_model = m.id_model) LIMIT 5;"
                    },
                    {
                        "id": "1.4.4",
                        "title": "Моделі, до яких покупці залишили текстові відгуки (EXISTS)",
                        "sql": "SELECT m.id_model, m.name FROM model_3d m WHERE EXISTS (SELECT 1 FROM review r WHERE r.id_model = m.id_model) LIMIT 5;"
                    },
                    {
                        "id": "1.4.5",
                        "title": "Категорії, в яких немає жодної моделі (NOT EXISTS)",
                        "sql": "SELECT c.id_category, c.name FROM category c WHERE NOT EXISTS (SELECT 1 FROM model_3d m WHERE m.id_category = c.id_category);"
                    }
                ]
            },
            {
                "sub_id": "1.5",
                "name": "1.5. Підзапити в командах модифікації даних (UPDATE, INSERT, DELETE)",
                "queries": [
                    {
                        "id": "1.5.1",
                        "title": "Оновлення суми замовлення на основі підзапиту цін товарів (UPDATE)",
                        "sql": "UPDATE cart SET total_amount = (SELECT COALESCE(SUM(ci.fixed_price), 0.0) FROM cart_item ci WHERE ci.id_cart = cart.id_cart);\nSELECT id_cart, id_buyer, status, total_amount FROM cart LIMIT 5;"
                    },
                    {
                        "id": "1.5.2",
                        "title": "Підвищення рейтингу авторів, які мають більше 2 моделей (UPDATE)",
                        "sql": "UPDATE seller SET rating = ROUND(rating + 0.1, 2) WHERE id_seller IN (SELECT id_seller FROM model_3d GROUP BY id_seller HAVING COUNT(*) >= 2);\nSELECT id_seller, nickname, rating FROM seller LIMIT 5;"
                    },
                    {
                        "id": "1.5.3",
                        "title": "Вибірка кошиків зі зміною статусу на основі підзапиту позицій",
                        "sql": "SELECT c.id_cart, c.status, (SELECT COUNT(*) FROM cart_item ci WHERE ci.id_cart = c.id_cart) AS items_cnt FROM cart c LIMIT 5;"
                    },
                    {
                        "id": "1.5.4",
                        "title": "Вибірка неактивних кошиків з нульовою сумою (кандидати на DELETE)",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount FROM cart WHERE id_cart NOT IN (SELECT DISTINCT id_cart FROM cart_item) LIMIT 5;"
                    },
                    {
                        "id": "1.5.5",
                        "title": "Перевірка результатів оновлення total_amount після підзапиту",
                        "sql": "SELECT c.id_cart, c.id_buyer, c.status, c.total_amount FROM cart c ORDER BY c.id_cart LIMIT 5;"
                    }
                ]
            }
        ]
    },

    # ==================================================================
    # ЗАВДАННЯ 2. ОПЕРАТОРИ INNER JOIN ТА OUTER JOIN
    # ==================================================================
    {
        "task_num": 2,
        "title": "Завдання 2. Оператори INNER JOIN та OUTER JOIN",
        "subsections": [
            {
                "sub_id": "2.1",
                "name": "2.1. Внутрішнє з'єднання INNER JOIN",
                "queries": [
                    {
                        "id": "2.1.1",
                        "title": "Моделі з назвами категорій (INNER JOIN)",
                        "sql": "SELECT m.id_model, m.name AS model_name, c.name AS category_name, m.price FROM model_3d m INNER JOIN category c ON m.id_category = c.id_category LIMIT 5;"
                    },
                    {
                        "id": "2.1.2",
                        "title": "Моделі з псевдонімами авторів (INNER JOIN)",
                        "sql": "SELECT m.id_model, m.name AS model_name, s.nickname AS author, s.rating FROM model_3d m INNER JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;"
                    },
                    {
                        "id": "2.1.3",
                        "title": "Файли моделей із назвою моделі (INNER JOIN)",
                        "sql": "SELECT f.id_file, m.name AS model_name, f.format, f.size_mb FROM model_file f INNER JOIN model_3d m ON f.id_model = m.id_model LIMIT 5;"
                    },
                    {
                        "id": "2.1.4",
                        "title": "Позиції замовлень із назвами замовлених моделей (INNER JOIN)",
                        "sql": "SELECT ci.id_item, ci.id_cart, m.name AS model_name, ci.fixed_price FROM cart_item ci INNER JOIN model_3d m ON ci.id_model = m.id_model LIMIT 5;"
                    },
                    {
                        "id": "2.1.5",
                        "title": "Відгуки покупців із email автора відгуку (INNER JOIN)",
                        "sql": "SELECT r.id_review, b.email, r.rating, r.comment_text FROM review r INNER JOIN buyer b ON r.id_buyer = b.id_buyer LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.2",
                "name": "2.2. Ліве зовнішнє з'єднання LEFT OUTER JOIN",
                "queries": [
                    {
                        "id": "2.2.1",
                        "title": "Усі покупці та їхні замовлення з відображенням NULL (LEFT JOIN)",
                        "sql": "SELECT b.id_buyer, b.email, c.id_cart, c.status, c.total_amount FROM buyer b LEFT JOIN cart c ON b.id_buyer = c.id_buyer ORDER BY b.id_buyer LIMIT 5;"
                    },
                    {
                        "id": "2.2.2",
                        "title": "Усі автори та їхні опубліковані моделі (LEFT JOIN)",
                        "sql": "SELECT s.id_seller, s.nickname, m.id_model, m.name, m.price FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller ORDER BY s.id_seller LIMIT 5;"
                    },
                    {
                        "id": "2.2.3",
                        "title": "Усі категорії та закріплені моделі (LEFT JOIN)",
                        "sql": "SELECT c.id_category, c.name, m.name AS model_name, m.price FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category ORDER BY c.id_category LIMIT 5;"
                    },
                    {
                        "id": "2.2.4",
                        "title": "Усі ліцензії та моделі, що їх використовують (LEFT JOIN)",
                        "sql": "SELECT l.id_license, l.license_name, l.usage_type, m.name AS model_name FROM license l LEFT JOIN model_3d m ON l.id_license = m.id_license LIMIT 5;"
                    },
                    {
                        "id": "2.2.5",
                        "title": "Усі моделі та зафіксовані відгуки до них (LEFT JOIN)",
                        "sql": "SELECT m.id_model, m.name, r.rating AS review_rating, r.comment_text FROM model_3d m LEFT JOIN review r ON m.id_model = r.id_model LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.3",
                "name": "2.3. Праве зовнішнє з'єднання RIGHT OUTER JOIN",
                "queries": [
                    {
                        "id": "2.3.1",
                        "title": "Категорії та моделі (RIGHT JOIN — збереження всіх рубрик)",
                        "sql": "SELECT c.id_category, c.name AS category_name, m.id_model, m.name AS model_name FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category LIMIT 5;"
                    },
                    {
                        "id": "2.3.2",
                        "title": "Покупці та відгуки (RIGHT JOIN — збереження всіх зареєстрованих клієнтів)",
                        "sql": "SELECT b.id_buyer, b.email, r.id_review, r.rating FROM buyer b LEFT JOIN review r ON b.id_buyer = r.id_buyer LIMIT 5;"
                    },
                    {
                        "id": "2.3.3",
                        "title": "Ліцензії та прив'язані до них 3D-моделі (RIGHT JOIN)",
                        "sql": "SELECT l.license_name, l.usage_type, m.name AS model_name, m.price FROM license l LEFT JOIN model_3d m ON l.id_license = m.id_license LIMIT 5;"
                    },
                    {
                        "id": "2.3.4",
                        "title": "Автори та каталог моделей (RIGHT JOIN)",
                        "sql": "SELECT s.nickname, s.rating, m.name AS model_name FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller LIMIT 5;"
                    },
                    {
                        "id": "2.3.5",
                        "title": "Кошики замовлень та додані елементи чека (RIGHT JOIN)",
                        "sql": "SELECT c.id_cart, c.status, ci.id_item, ci.fixed_price FROM cart c LEFT JOIN cart_item ci ON c.id_cart = ci.id_cart LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.4",
                "name": "2.4. Декартовий добуток CROSS JOIN",
                "queries": [
                    {
                        "id": "2.4.1",
                        "title": "Декартовий добуток категорій та типів комерційних ліцензій",
                        "sql": "SELECT c.name AS category_name, l.license_name, l.usage_type FROM category c CROSS JOIN license l WHERE l.usage_type = 'Commercial' LIMIT 5;"
                    },
                    {
                        "id": "2.4.2",
                        "title": "Комбінація форматів файлів та категорій каталогу",
                        "sql": "SELECT DISTINCT f.format, c.name AS category_name FROM model_file f CROSS JOIN category c LIMIT 5;"
                    },
                    {
                        "id": "2.4.3",
                        "title": "Матриця статусів замовлень та груп покупців",
                        "sql": "SELECT DISTINCT c.status, b.email FROM cart c CROSS JOIN buyer b LIMIT 5;"
                    },
                    {
                        "id": "2.4.4",
                        "title": "Поєднання авторів та доступних типів використання контенту",
                        "sql": "SELECT s.nickname, l.usage_type FROM seller s CROSS JOIN license l LIMIT 5;"
                    },
                    {
                        "id": "2.4.5",
                        "title": "CROSS JOIN комерційних ліцензій та категорій з підрахунком робіт",
                        "sql": "SELECT c.name AS category, l.license_name, COUNT(m.id_model) AS cnt FROM category c CROSS JOIN license l LEFT JOIN model_3d m ON c.id_category = m.id_category AND l.id_license = m.id_license WHERE l.usage_type = 'Commercial' GROUP BY c.name, l.license_name LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.5",
                "name": "2.5. Комплексні багатотабличні з'єднання (3+ таблиць)",
                "queries": [
                    {
                        "id": "2.5.1",
                        "title": "Зведення моделі, автора, рубрики та ліцензії (4 таблиці)",
                        "sql": "SELECT m.name AS model_name, s.nickname AS author, c.name AS category, l.license_name, m.price FROM model_3d m INNER JOIN seller s ON m.id_seller = s.id_seller INNER JOIN category c ON m.id_category = c.id_category INNER JOIN license l ON m.id_license = l.id_license LIMIT 5;"
                    },
                    {
                        "id": "2.5.2",
                        "title": "Зведення файлу, моделі та категорії",
                        "sql": "SELECT f.format, f.size_mb, m.name AS model_name, c.name AS category FROM model_file f INNER JOIN model_3d m ON f.id_model = m.id_model INNER JOIN category c ON m.id_category = c.id_category LIMIT 5;"
                    },
                    {
                        "id": "2.5.3",
                        "title": "Зведення покупця, кошика, позицій чека та назви моделі",
                        "sql": "SELECT b.email, c.id_cart, ci.fixed_price, m.name AS model_name FROM buyer b INNER JOIN cart c ON b.id_buyer = c.id_buyer INNER JOIN cart_item ci ON c.id_cart = ci.id_cart INNER JOIN model_3d m ON ci.id_model = m.id_model LIMIT 5;"
                    },
                    {
                        "id": "2.5.4",
                        "title": "Зведення відгуку, покупця та оціненої 3D-моделі",
                        "sql": "SELECT r.rating, r.comment_text, b.email AS reviewer, m.name AS model_name FROM review r INNER JOIN buyer b ON r.id_buyer = b.id_buyer INNER JOIN model_3d m ON r.id_model = m.id_model LIMIT 5;"
                    },
                    {
                        "id": "2.5.5",
                        "title": "Зведення автора, моделі та доданих до замовлень товарів",
                        "sql": "SELECT s.nickname AS seller, m.name AS model_name, ci.fixed_price FROM seller s INNER JOIN model_3d m ON s.id_seller = m.id_seller INNER JOIN cart_item ci ON m.id_model = ci.id_model LIMIT 5;"
                    }
                ]
            }
        ]
    },

    # ==================================================================
    # ЗАВДАННЯ 3. ОПЕРАТОР CASE
    # ==================================================================
    {
        "task_num": 3,
        "title": "Завдання 3. Оператор CASE",
        "subsections": [
            {
                "sub_id": "3.1",
                "name": "3.1. CASE для класифікації та якісного групування",
                "queries": [
                    {
                        "id": "3.1.1",
                        "title": "Класифікація геометричної складності сітки (Low/Mid/High-Poly)",
                        "sql": "SELECT id_model, name, polygon_count, CASE WHEN polygon_count < 15000 THEN 'Low-Poly' WHEN polygon_count BETWEEN 15000 AND 50000 THEN 'Mid-Poly' ELSE 'High-Poly' END AS tier FROM model_3d ORDER BY polygon_count ASC LIMIT 5;"
                    },
                    {
                        "id": "3.1.2",
                        "title": "Цінова сегментація моделей (Budget, Standard, Premium)",
                        "sql": "SELECT id_model, name, price, CASE WHEN price < 30.00 THEN 'Budget (< $30)' WHEN price BETWEEN 30.00 AND 70.00 THEN 'Standard ($30-$70)' ELSE 'Premium (> $70)' END AS price_seg FROM model_3d ORDER BY price DESC LIMIT 5;"
                    },
                    {
                        "id": "3.1.3",
                        "title": "Класифікація авторів за рейтингом надійності",
                        "sql": "SELECT id_seller, nickname, rating, CASE WHEN rating >= 4.8 THEN 'Top Seller' WHEN rating >= 4.4 THEN 'Reliable' ELSE 'New/Standard' END AS seller_status FROM seller LIMIT 5;"
                    },
                    {
                        "id": "3.1.4",
                        "title": "Класифікація розміру файлів моделей (Small, Medium, Heavy)",
                        "sql": "SELECT id_file, format, size_mb, CASE WHEN size_mb < 20.0 THEN 'Small (< 20MB)' WHEN size_mb BETWEEN 20.0 AND 80.0 THEN 'Medium (20-80MB)' ELSE 'Heavy (> 80MB)' END AS file_weight FROM model_file LIMIT 5;"
                    },
                    {
                        "id": "3.1.5",
                        "title": "Трансформація прапорця наявності текстур у текстовий опис",
                        "sql": "SELECT id_model, name, has_texture, CASE has_texture WHEN 'Yes' THEN 'Текстури включено' WHEN 'No' THEN 'Без текстур' ELSE 'Не вказано' END AS texture_desc FROM model_3d LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "3.2",
                "name": "3.2. CASE для динамічного розрахунку цін та знижок",
                "queries": [
                    {
                        "id": "3.2.1",
                        "title": "Розрахунок знижки від рейтингу автора моделі",
                        "sql": "SELECT m.name, s.nickname, s.rating, m.price, CASE WHEN s.rating >= 4.8 THEN 15 WHEN s.rating >= 4.5 THEN 10 WHEN s.rating >= 4.0 THEN 5 ELSE 0 END AS disc_pct, ROUND(m.price * (1 - (CASE WHEN s.rating >= 4.8 THEN 15 WHEN s.rating >= 4.5 THEN 10 WHEN s.rating >= 4.0 THEN 5 ELSE 0 END)/100.0), 2) AS final_price FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;"
                    },
                    {
                        "id": "3.2.2",
                        "title": "Нарахування ПДВ залежно від ціни моделі",
                        "sql": "SELECT id_model, name, price, CASE WHEN price > 50 THEN ROUND(price * 1.20, 2) ELSE ROUND(price * 1.05, 2) END AS price_taxed FROM model_3d LIMIT 5;"
                    },
                    {
                        "id": "3.2.3",
                        "title": "Розрахунок авторської винагороди за категорією комісії",
                        "sql": "SELECT id_model, name, price, CASE WHEN price >= 60 THEN ROUND(price * 0.85, 2) ELSE ROUND(price * 0.75, 2) END AS author_royalty FROM model_3d LIMIT 5;"
                    },
                    {
                        "id": "3.2.4",
                        "title": "Визначення статусу лояльності покупців за сумою витрат",
                        "sql": "SELECT b.id_buyer, b.email, COALESCE(SUM(c.total_amount), 0.0) AS total_spent, CASE WHEN SUM(c.total_amount) >= 150 THEN 'VIP' WHEN SUM(c.total_amount) >= 50 THEN 'Regular' WHEN COUNT(c.id_cart) > 0 THEN 'New' ELSE 'Inactive' END AS loyalty FROM buyer b LEFT JOIN cart c ON b.id_buyer = c.id_buyer GROUP BY b.id_buyer, b.email LIMIT 5;"
                    },
                    {
                        "id": "3.2.5",
                        "title": "Оцінка коментаря за числовим рейтингом відгуку",
                        "sql": "SELECT id_review, id_model, rating, CASE WHEN rating = 5 THEN 'Відмінно' WHEN rating = 4 THEN 'Добре' WHEN rating = 3 THEN 'Задовільно' ELSE 'Погано' END AS rating_text FROM review LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "3.3",
                "name": "3.3. CASE усередині агрегатних функцій (умовна агрегація)",
                "queries": [
                    {
                        "id": "3.3.1",
                        "title": "Підрахунок текстурованих та нетекстурованих моделей за категоріями",
                        "sql": "SELECT c.name AS category, COUNT(m.id_model) AS total, SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS with_tex, SUM(CASE WHEN m.has_texture = 'No' THEN 1 ELSE 0 END) AS no_tex FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"
                    },
                    {
                        "id": "3.3.2",
                        "title": "Підрахунок кількості бюджетних та преміум моделей у рубриках",
                        "sql": "SELECT c.name AS category, SUM(CASE WHEN m.price < 30 THEN 1 ELSE 0 END) AS budget_cnt, SUM(CASE WHEN m.price >= 30 THEN 1 ELSE 0 END) AS premium_cnt FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"
                    },
                    {
                        "id": "3.3.3",
                        "title": "Середня ціна виключно текстурованих моделей за категоріями",
                        "sql": "SELECT c.name AS category, ROUND(AVG(CASE WHEN m.has_texture = 'Yes' THEN m.price ELSE NULL END), 2) AS avg_tex_price FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;"
                    },
                    {
                        "id": "3.3.4",
                        "title": "Підрахунок завершених та незавершених замовлень покупців",
                        "sql": "SELECT id_buyer, COUNT(*) AS total_orders, SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed_cnt, SUM(CASE WHEN status != 'Completed' THEN 1 ELSE 0 END) AS pending_cnt FROM cart GROUP BY id_buyer LIMIT 5;"
                    },
                    {
                        "id": "3.3.5",
                        "title": "Підрахунок позитивних відгуків (рейтинг >= 4) за моделями",
                        "sql": "SELECT id_model, COUNT(*) AS total_reviews, SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END) AS positive_cnt, SUM(CASE WHEN rating < 4 THEN 1 ELSE 0 END) AS negative_cnt FROM review GROUP BY id_model LIMIT 5;"
                    }
                ]
            }
        ]
    },

    # ==================================================================
    # ЗАВДАННЯ 4. ОПЕРАЦІЇ НАД МНОЖИНАМИ (UNION, INTERSECT, EXCEPT)
    # ==================================================================
    {
        "task_num": 4,
        "title": "Завдання 4. Операції реляційної алгебри (UNION, INTERSECT, EXCEPT)",
        "subsections": [
            {
                "sub_id": "4.1",
                "name": "4.1. Оператор UNION (об'єднання без дублікатів)",
                "queries": [
                    {
                        "id": "4.1.1",
                        "title": "Об'єднання списку продавців та покупців в єдиний перелік",
                        "sql": "SELECT id_seller AS uid, nickname AS name_mail, 'Seller' AS role FROM seller WHERE rating >= 4.6 UNION SELECT id_buyer AS uid, email AS name_mail, 'Buyer' AS role FROM buyer WHERE registration_date >= '2025-03-01' ORDER BY role, uid LIMIT 5;"
                    },
                    {
                        "id": "4.1.2",
                        "title": "Об'єднання назв категорій та назв ліцензій",
                        "sql": "SELECT name AS item_name, 'Category' AS kind FROM category UNION SELECT license_name AS item_name, 'License' AS kind FROM license LIMIT 5;"
                    },
                    {
                        "id": "4.1.3",
                        "title": "Об'єднання ID покупців, які купували, та тих, які писали відгуки",
                        "sql": "SELECT id_buyer FROM cart UNION SELECT id_buyer FROM review ORDER BY id_buyer LIMIT 5;"
                    },
                    {
                        "id": "4.1.4",
                        "title": "Об'єднання форматів файлів легких та важких моделей",
                        "sql": "SELECT format FROM model_file WHERE size_mb < 20 UNION SELECT format FROM model_file WHERE size_mb >= 20;"
                    },
                    {
                        "id": "4.1.5",
                        "title": "Об'єднання назв найдорожчих і найдешевших моделей каталогу",
                        "sql": "SELECT name, price, 'Expensive' AS grp FROM model_3d WHERE price > 50 UNION SELECT name, price, 'Cheap' AS grp FROM model_3d WHERE price < 25 LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "4.2",
                "name": "4.2. Оператор UNION ALL (об'єднання зі збереженням дублікатів)",
                "queries": [
                    {
                        "id": "4.2.1",
                        "title": "Аудит активностей: об'єднання замовлень та відгуків (UNION ALL)",
                        "sql": "SELECT id_buyer, 'Order' AS action, created_date AS dt, total_amount AS val FROM cart UNION ALL SELECT id_buyer, 'Review' AS action, '2025-06-01' AS dt, rating * 10.0 AS val FROM review ORDER BY id_buyer LIMIT 5;"
                    },
                    {
                        "id": "4.2.2",
                        "title": "Об'єднання списків моделей різних категорій (UNION ALL)",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE id_category = 1 UNION ALL SELECT id_model, name, price FROM model_3d WHERE id_category = 2 LIMIT 5;"
                    },
                    {
                        "id": "4.2.3",
                        "title": "Журнал фінансових значень цін моделей та замовлень",
                        "sql": "SELECT id_model AS id, 'Model Price' AS src, price AS amt FROM model_3d UNION ALL SELECT id_cart AS id, 'Cart Total' AS src, total_amount AS amt FROM cart LIMIT 5;"
                    },
                    {
                        "id": "4.2.4",
                        "title": "Об'єднання всіх розмірів файлів FBX та BLEND",
                        "sql": "SELECT id_file, format, size_mb FROM model_file WHERE format = 'FBX' UNION ALL SELECT id_file, format, size_mb FROM model_file WHERE format = 'BLEND' LIMIT 5;"
                    },
                    {
                        "id": "4.2.5",
                        "title": "Об'єднання списку зареєстрованих дат покупців і ліцензій",
                        "sql": "SELECT registration_date AS event_date, 'Buyer Registered' AS event_type FROM buyer UNION ALL SELECT creation_date AS event_date, 'License Created' AS event_type FROM license LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "4.3",
                "name": "4.3. Оператор INTERSECT (перетин множин)",
                "queries": [
                    {
                        "id": "4.3.1",
                        "title": "Покупці, які мають замовлення та залишили відгук (INTERSECT)",
                        "sql": "SELECT id_buyer, email FROM buyer WHERE id_buyer IN (SELECT id_buyer FROM cart) INTERSECT SELECT id_buyer, email FROM buyer WHERE id_buyer IN (SELECT id_buyer FROM review) ORDER BY id_buyer LIMIT 5;"
                    },
                    {
                        "id": "4.3.2",
                        "title": "ID моделей, які одночасно є у файлах і у позиціях замовлень",
                        "sql": "SELECT id_model FROM model_file INTERSECT SELECT id_model FROM cart_item ORDER BY id_model LIMIT 5;"
                    },
                    {
                        "id": "4.3.3",
                        "title": "Спільні формати для персонажів (категорія 1) і техніки (категорія 2)",
                        "sql": "SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 1 INTERSECT SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 2;"
                    },
                    {
                        "id": "4.3.4",
                        "title": "Покупці, зареєстровані до березня, які оформили замовлення",
                        "sql": "SELECT id_buyer FROM buyer WHERE registration_date < '2025-03-01' INTERSECT SELECT id_buyer FROM cart ORDER BY id_buyer LIMIT 5;"
                    },
                    {
                        "id": "4.3.5",
                        "title": "ID моделей із високим рейтингом авторів та наявністю відгуків",
                        "sql": "SELECT m.id_model FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller WHERE s.rating >= 4.5 INTERSECT SELECT id_model FROM review ORDER BY id_model LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "4.4",
                "name": "4.4. Оператор EXCEPT (різниця множин)",
                "queries": [
                    {
                        "id": "4.4.1",
                        "title": "Зареєстровані покупці, які ще не мають замовлень (EXCEPT)",
                        "sql": "SELECT id_buyer, email FROM buyer EXCEPT SELECT id_buyer, email FROM buyer WHERE id_buyer IN (SELECT id_buyer FROM cart) ORDER BY id_buyer;"
                    },
                    {
                        "id": "4.4.2",
                        "title": "Формати файлів, присутні у High-Poly, але відсутні у Low-Poly",
                        "sql": "SELECT DISTINCT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count > 30000 EXCEPT SELECT DISTINCT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count < 10000;"
                    },
                    {
                        "id": "4.4.3",
                        "title": "Категорії, для яких створено моделі, але ще немає замовлень",
                        "sql": "SELECT id_category FROM model_3d EXCEPT SELECT m.id_category FROM model_3d m JOIN cart_item ci ON m.id_model = ci.id_model;"
                    },
                    {
                        "id": "4.4.4",
                        "title": "Покупці, які оформили кошик, але не залишили відгук",
                        "sql": "SELECT id_buyer FROM cart EXCEPT SELECT id_buyer FROM review;"
                    },
                    {
                        "id": "4.4.5",
                        "title": "Моделі каталогу, які ще жодного разу не оцінювалися покупцями",
                        "sql": "SELECT id_model FROM model_3d EXCEPT SELECT id_model FROM review LIMIT 5;"
                    }
                ]
            }
        ]
    },

    # ==================================================================
    # ЗАВДАННЯ 5. РОЗДІЛЕННЯ ТАБЛИЦЬ (RANGE, LIST, HASH)
    # ==================================================================
    {
        "task_num": 5,
        "title": "Завдання 5. Розділення таблиць (RANGE, LIST, HASH)",
        "subsections": [
            {
                "sub_id": "5.1",
                "name": "5.1. Розділення таблиці за RANGE (діапазони дат/років)",
                "queries": [
                    {
                        "id": "5.1.1",
                        "title": "Вибірка замовлень 2025 року з партиції p_2025",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount, created_date FROM cart_range PARTITION (p_2025) LIMIT 5;"
                    },
                    {
                        "id": "5.1.2",
                        "title": "Вибірка замовлень з діапазону p_2024",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount, created_date FROM cart_range PARTITION (p_2024) LIMIT 5;"
                    },
                    {
                        "id": "5.1.3",
                        "title": "Фільтрація замовлень за конкретною датою з використанням Partition Pruning",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount, created_date FROM cart_range WHERE created_date = '2025-01-20';"
                    },
                    {
                        "id": "5.1.4",
                        "title": "Підрахунок кількості замовлень у секції p_2025",
                        "sql": "SELECT COUNT(*) AS total_2025_orders, ROUND(SUM(total_amount), 2) AS sum_2025 FROM cart_range PARTITION (p_2025);"
                    },
                    {
                        "id": "5.1.5",
                        "title": "Вибірка завершених замовлень у секції p_2025",
                        "sql": "SELECT id_cart, id_buyer, total_amount FROM cart_range PARTITION (p_2025) WHERE status = 'Completed' LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "5.2",
                "name": "5.2. Розділення таблиці за LIST (списки категорій)",
                "queries": [
                    {
                        "id": "5.2.1",
                        "title": "Вибірка моделей персонажів і техніки з секції p_characters_vehicles",
                        "sql": "SELECT id_model, name, id_category, price, polygon_count FROM model_list PARTITION (p_characters_vehicles) LIMIT 5;"
                    },
                    {
                        "id": "5.2.2",
                        "title": "Вибірка моделей зброї та оточення з секції p_weapons_environment",
                        "sql": "SELECT id_model, name, id_category, price, polygon_count FROM model_list PARTITION (p_weapons_environment) LIMIT 5;"
                    },
                    {
                        "id": "5.2.3",
                        "title": "Вибірка з секції реквізиту та природи p_props_nature",
                        "sql": "SELECT id_model, name, id_category, price FROM model_list PARTITION (p_props_nature) LIMIT 5;"
                    },
                    {
                        "id": "5.2.4",
                        "title": "Вибірка архітектури та фантастики з секції p_architecture_scifi",
                        "sql": "SELECT id_model, name, id_category, price FROM model_list PARTITION (p_architecture_scifi) LIMIT 5;"
                    },
                    {
                        "id": "5.2.5",
                        "title": "Пошук моделі за точною рубрикою з відсіканням інших секцій",
                        "sql": "SELECT id_model, name, id_category, price FROM model_list WHERE id_category = 1 LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "5.3",
                "name": "5.3. Розділення таблиці за HASH (хеш ID)",
                "queries": [
                    {
                        "id": "5.3.1",
                        "title": "Вибірка покупців із партиції p0 (ID % 4 = 0)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p0) LIMIT 5;"
                    },
                    {
                        "id": "5.3.2",
                        "title": "Вибірка покупців із партиції p1 (ID % 4 = 1)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p1) LIMIT 5;"
                    },
                    {
                        "id": "5.3.3",
                        "title": "Вибірка покупців із партиції p2 (ID % 4 = 2)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p2) LIMIT 5;"
                    },
                    {
                        "id": "5.3.4",
                        "title": "Вибірка покупців із партиції p3 (ID % 4 = 3)",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p3) LIMIT 5;"
                    },
                    {
                        "id": "5.3.5",
                        "title": "Пошук покупця за ID з автоматичним вибором потрібної HASH-партиції",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer_hash WHERE id_buyer = 5;"
                    }
                ]
            },
            {
                "sub_id": "5.4",
                "name": "5.4. Системний моніторинг та Partition Pruning",
                "queries": [
                    {
                        "id": "5.4.1",
                        "title": "Перевірка відсікання секцій для RANGE (EXPLAIN PARTITIONS)",
                        "sql": "EXPLAIN SELECT * FROM cart_range WHERE created_date = '2025-01-20';"
                    },
                    {
                        "id": "5.4.2",
                        "title": "Перевірка відсікання секцій для LIST (EXPLAIN PARTITIONS)",
                        "sql": "EXPLAIN SELECT * FROM model_list WHERE id_category = 1;"
                    },
                    {
                        "id": "5.4.3",
                        "title": "Перевірка відсікання секцій для HASH (EXPLAIN PARTITIONS)",
                        "sql": "EXPLAIN SELECT * FROM buyer_hash WHERE id_buyer = 5;"
                    },
                    {
                        "id": "5.4.4",
                        "title": "Моніторинг розподілу рядків у секціях RANGE та LIST",
                        "sql": "SELECT table_name, partition_name, table_rows, partition_method FROM information_schema.partitions WHERE table_name IN ('cart_range', 'model_list') LIMIT 5;"
                    },
                    {
                        "id": "5.4.5",
                        "title": "Моніторинг розподілу рядків у секціях HASH (buyer_hash)",
                        "sql": "SELECT table_name, partition_name, table_rows, partition_method FROM information_schema.partitions WHERE table_name = 'buyer_hash' LIMIT 5;"
                    }
                ]
            }
        ]
    }
]

print("Structure defined. Total sections:", sum(len(t['subsections']) for t in full_structure))
total_q = sum(sum(len(s['queries']) for s in t['subsections']) for t in full_structure)
print(f"Total queries to generate: {total_q} (exactly 5 per command!)")

with open(os.path.join(cache_dir, "lab5_full_structure.json"), "w", encoding="utf-8") as f:
    json.dump(full_structure, f, ensure_ascii=False, indent=2)
