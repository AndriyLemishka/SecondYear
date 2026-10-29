import os

sql_dir = r"Лаб 5\sql"
os.makedirs(sql_dir, exist_ok=True)

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

# 01_subqueries.sql
sql_01 = header + """
-- =============================================================================
-- ЗАВДАННЯ 1. РІЗНІ ТИПИ ПІДЗАПИТІВ (КОРЕЛЮЮЧІ ТА НЕКОРЕЛЮЮЧІ)
-- =============================================================================

-- Запит 1.1. Скалярний некорелюючий підзапит у списку вибірки SELECT
-- Призначення: обчислення різниці між ціною кожної 3D-моделі та середньою вартістю по всьому каталогу
SELECT id_model, name, price,
       ROUND((SELECT AVG(price) FROM model_3d), 2) AS avg_catalog_price,
       ROUND(price - (SELECT AVG(price) FROM model_3d), 2) AS price_diff
FROM model_3d
ORDER BY price_diff DESC
LIMIT 6;

-- Запит 1.2. Некорелюючий підзапит у реченні WHERE з оператором IN
-- Призначення: вибірка 3D-моделей, авторами яких є верифіковані продавці з найвищим рейтингом (>= 4.70)
SELECT id_model, name, price, id_seller
FROM model_3d
WHERE id_seller IN (
    SELECT id_seller
    FROM seller
    WHERE rating >= 4.70
)
ORDER BY price DESC;

-- Запит 1.3. Корелюючий підзапит у реченні WHERE з оператором порівняння >
-- Призначення: вибірка моделей, ціна яких перевищує середню вартість моделей саме їхньої тематичної категорії
SELECT m1.id_model, m1.name, m1.id_category, m1.price
FROM model_3d m1
WHERE m1.price > (
    SELECT AVG(m2.price)
    FROM model_3d m2
    WHERE m2.id_category = m1.id_category
)
ORDER BY m1.id_category, m1.price DESC;

-- Запит 1.4. Корелюючий підзапит у реченні WHERE з оператором перевірки існування NOT EXISTS
-- Призначення: виявлення зареєстрованих клієнтів (buyer), які досі не оформили жодного замовлення
SELECT b.id_buyer, b.email, b.registration_date
FROM buyer b
WHERE NOT EXISTS (
    SELECT 1
    FROM cart c
    WHERE c.id_buyer = b.id_buyer
);

-- Запит 1.5. Підзапит у команді оновлення даних UPDATE та перевірка вибіркою
-- Призначення: синхронізація поля total_amount у таблиці замовлень cart на основі суми вартості куплених товарів
UPDATE cart
SET total_amount = (
    SELECT COALESCE(SUM(ci.fixed_price), 0.0)
    FROM cart_item ci
    WHERE ci.id_cart = cart.id_cart
);

-- Контрольна вибірка результатів оновлення з підрахунком товарів підзапитом
SELECT c.id_cart, c.id_buyer, c.status, c.total_amount,
       (SELECT COUNT(*) FROM cart_item ci WHERE ci.id_cart = c.id_cart) AS items_count
FROM cart c
ORDER BY c.id_cart
LIMIT 6;
"""

# 02_joins.sql
sql_02 = header + """
-- =============================================================================
-- ЗАВДАННЯ 2. ОПЕРАТОРИ INNER JOIN ТА OUTER JOIN ДЛЯ ЗВЕДЕНИХ ТАБЛИЦЬ
-- =============================================================================

-- Запит 2.1. Базове внутрішнє з'єднання двох таблиць (INNER JOIN)
-- Призначення: виведення каталогу 3D-моделей із зіставленням назви відповідної тематичної категорії
SELECT m.id_model, m.name AS model_name, c.name AS category_name, m.price, m.polygon_count
FROM model_3d m
INNER JOIN category c ON m.id_category = c.id_category
ORDER BY c.name, m.price DESC
LIMIT 6;

-- Запит 2.2. Комплексне багаторівневе внутрішнє з'єднання 4 таблиць (INNER JOIN)
-- Призначення: формування повної вітрини цифрового товару (модель + автор + категорія + умови ліцензування)
SELECT m.name AS model_name, s.nickname AS author, c.name AS category,
       l.license_name, l.usage_type, m.price
FROM model_3d m
INNER JOIN seller s ON m.id_seller = s.id_seller
INNER JOIN category c ON m.id_category = c.id_category
INNER JOIN license l ON m.id_license = l.id_license
ORDER BY m.price DESC
LIMIT 6;

-- Запит 2.3. Ліве зовнішнє з'єднання (LEFT OUTER JOIN) для виявлення зв'язків та відсутності замовлень
-- Призначення: аудит усіх зареєстрованих клієнтів та їхніх кошиків із наочним відображенням значень NULL
SELECT b.id_buyer, b.email, b.registration_date,
       c.id_cart, c.status AS cart_status, c.total_amount
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer
ORDER BY b.id_buyer, c.id_cart
LIMIT 7;

-- Запит 2.4. Праве зовнішнє з'єднання (RIGHT OUTER JOIN / LEFT JOIN довідника)
-- Призначення: перевірка наявності опублікованих моделей для кожної тематичної категорії платформи
SELECT c.id_category, c.name AS category_name,
       m.id_model, m.name AS model_name, m.price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
ORDER BY c.id_category, m.id_model
LIMIT 7;

-- Запит 2.5. Декартовий добуток (CROSS JOIN) комерційних ліцензій та категорій з агрегацією
-- Призначення: аналітична матриця попиту — зіставлення комерційних ліцензій та категорій із підрахунком наявних робіт
SELECT c.name AS category_name, l.license_name, l.usage_type,
       COUNT(m.id_model) AS models_count
FROM category c
CROSS JOIN license l
LEFT JOIN model_3d m ON m.id_category = c.id_category AND m.id_license = l.id_license
WHERE l.usage_type = 'Commercial'
GROUP BY c.name, l.license_name, l.usage_type
ORDER BY c.name, l.license_name
LIMIT 7;
"""

# 03_case_expressions.sql
sql_03 = header + """
-- =============================================================================
-- ЗАВДАННЯ 3. ЗАСТОСУВАННЯ ФУНКЦІЇ CASE (З АГРЕГАТНИМИ ТА БЕЗ НИХ)
-- =============================================================================

-- Запит 3.1. Пошуковий CASE для класифікації геометричної складності полігональної сітки
-- Призначення: поділ моделей на категорії оптимізації (Low-Poly, Mid-Poly, High-Poly)
SELECT id_model, name, polygon_count,
       CASE
           WHEN polygon_count < 15000 THEN 'Low-Poly'
           WHEN polygon_count BETWEEN 15000 AND 50000 THEN 'Mid-Poly'
           ELSE 'High-Poly'
       END AS complexity_tier
FROM model_3d
ORDER BY polygon_count ASC
LIMIT 7;

-- Запит 3.2. Умовний вираз CASE для комерційної та цінової сегментації цифрових активів
-- Призначення: категоризація товарів за доступністю (бюджетні, стандартні та преміум асети)
SELECT id_model, name, price,
       CASE
           WHEN price < 30.00 THEN 'Budget (< $30)'
           WHEN price BETWEEN 30.00 AND 70.00 THEN 'Standard ($30-$70)'
           ELSE 'Premium (> $70)'
       END AS price_category
FROM model_3d
ORDER BY price DESC
LIMIT 7;

-- Запит 3.3. CASE усередині агрегатних функцій (Pivot-агрегація за категоріями)
-- Призначення: умовне зведення кількості текстурованих і нетекстурованих моделей та середньої ціни
SELECT c.name AS category_name,
       COUNT(m.id_model) AS total_models,
       SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS textured_count,
       SUM(CASE WHEN m.has_texture = 'No' THEN 1 ELSE 0 END) AS untextured_count,
       ROUND(AVG(CASE WHEN m.has_texture = 'Yes' THEN m.price ELSE NULL END), 2) AS avg_textured_price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
GROUP BY c.id_category, c.name
ORDER BY total_models DESC
LIMIT 6;

-- Запит 3.4. Розрахунок прогресивної знижки та фінальної акційної вартості через CASE
-- Призначення: нарахування знижки (15%, 10%, 5%) на модель залежно від рейтингу надійності її творця
SELECT m.name AS model_name, s.nickname, s.rating, m.price AS original_price,
       CASE
           WHEN s.rating >= 4.8 THEN 15
           WHEN s.rating >= 4.5 THEN 10
           WHEN s.rating >= 4.0 THEN 5
           ELSE 0
       END AS discount_pct,
       ROUND(m.price * (1.0 - (CASE
           WHEN s.rating >= 4.8 THEN 15
           WHEN s.rating >= 4.5 THEN 10
           WHEN s.rating >= 4.0 THEN 5
           ELSE 0
       END) / 100.0), 2) AS discounted_price
FROM model_3d m
INNER JOIN seller s ON m.id_seller = s.id_seller
ORDER BY s.rating DESC, m.price DESC
LIMIT 6;

-- Запит 3.5. Сегментація лояльності клієнтів (покупців) на основі загальної суми замовлень
-- Призначення: надання статусу (VIP Buyer, Regular Buyer, New Buyer, Inactive)
SELECT b.id_buyer, b.email,
       COUNT(c.id_cart) AS total_orders,
       COALESCE(SUM(c.total_amount), 0.0) AS total_spent,
       CASE
           WHEN SUM(c.total_amount) >= 150.00 THEN 'VIP Buyer'
           WHEN SUM(c.total_amount) >= 50.00 THEN 'Regular Buyer'
           WHEN COUNT(c.id_cart) > 0 THEN 'New Buyer'
           ELSE 'Inactive'
       END AS customer_tier
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer
GROUP BY b.id_buyer, b.email
ORDER BY total_spent DESC
LIMIT 7;
"""

# 04_set_operations.sql
sql_04 = header + """
-- =============================================================================
-- ЗАВДАННЯ 4. ТЕОРЕТИКО-МНОЖИННІ ОПЕРАЦІЇ (UNION, INTERSECT, EXCEPT)
-- =============================================================================

-- Запит 4.1. Об'єднання множин без повторень (UNION)
-- Призначення: консолідований перелік ключових учасників платформи (продавців і покупців)
SELECT id_seller AS user_id, nickname AS identifier, 'Seller' AS role
FROM seller
WHERE rating >= 4.6
UNION
SELECT id_buyer AS user_id, email AS identifier, 'Buyer' AS role
FROM buyer
WHERE registration_date >= '2025-03-01'
ORDER BY role, user_id
LIMIT 8;

-- Запит 4.2. Об'єднання множин зі збереженням дублікатів (UNION ALL)
-- Призначення: хронологічний аудит-лог усіх користувацьких активностей (замовлення та рецензії)
SELECT id_buyer, 'Cart Order' AS activity_type, created_date AS action_date, total_amount AS val
FROM cart
UNION ALL
SELECT r.id_buyer, 'Model Review' AS activity_type, '2025-06-01' AS action_date, r.rating * 10.0 AS val
FROM review r
ORDER BY id_buyer, action_date
LIMIT 8;

-- Запит 4.3. Перетин множин (INTERSECT)
-- Призначення: вибірка клієнтів, які одночасно оформили замовлення та залишили рецензію на придбані моделі
SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM cart)
INTERSECT
SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM review)
ORDER BY id_buyer
LIMIT 6;

-- Запит 4.4. Різниця множин (EXCEPT)
-- Призначення: визначення зареєстрованих клієнтів, які ще не створили жодного замовлення (для таргетингу)
SELECT id_buyer, email FROM buyer
EXCEPT
SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM cart)
ORDER BY id_buyer;

-- Запит 4.5. Різниця множин (EXCEPT) для порівняльного аналізу форматів файлів
-- Призначення: визначення форматів файлів, що застосовуються виключно у High-Poly моделях
SELECT DISTINCT f.format
FROM model_file f
JOIN model_3d m ON f.id_model = m.id_model
WHERE m.polygon_count > 30000
EXCEPT
SELECT DISTINCT f.format
FROM model_file f
JOIN model_3d m ON f.id_model = m.id_model
WHERE m.polygon_count < 10000;
"""

# 05_partitioning.sql
sql_05 = header + """
-- =============================================================================
-- ЗАВДАННЯ 5. РОЗДІЛЕННЯ ТАБЛИЦЬ (PARTITIONING): RANGE, LIST, HASH
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 5.1. Розділення таблиці cart за діапазоном значень (RANGE)
-- Критерій секціонування: календарний рік створення замовлення YEAR(created_date)
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS cart_range;
CREATE TABLE cart_range (
    id_cart INT NOT NULL,
    id_buyer INT NOT NULL,
    status VARCHAR(30) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    created_date DATE NOT NULL,
    PRIMARY KEY (id_cart, created_date)
)
PARTITION BY RANGE (YEAR(created_date)) (
    PARTITION p_2024 VALUES LESS THAN (2025),
    PARTITION p_2025 VALUES LESS THAN (2026),
    PARTITION p_2026 VALUES LESS THAN (2027),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- Запит вибірки з конкретної партиції p_2025 (Partition Pruning)
SELECT id_cart, id_buyer, status, total_amount, created_date
FROM cart_range
PARTITION (p_2025)
ORDER BY created_date ASC
LIMIT 6;

-- -----------------------------------------------------------------------------
-- 5.2. Розділення таблиці model_3d за списком дискретних значень (LIST)
-- Критерій секціонування: ідентифікатор категорії моделі id_category
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS model_list;
CREATE TABLE model_list (
    id_model INT NOT NULL,
    id_seller INT NOT NULL,
    id_category INT NOT NULL,
    id_license INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    polygon_count INT NOT NULL,
    has_texture VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_model, id_category)
)
PARTITION BY LIST (id_category) (
    PARTITION p_characters_vehicles VALUES IN (1, 2),
    PARTITION p_weapons_environment VALUES IN (3, 4),
    PARTITION p_props_nature VALUES IN (5, 6, 7),
    PARTITION p_architecture_scifi VALUES IN (8, 9, 10)
);

-- Запит вибірки моделей лише з секції p_characters_vehicles
SELECT id_model, name, id_category, price, polygon_count
FROM model_list
PARTITION (p_characters_vehicles)
ORDER BY price DESC
LIMIT 6;

-- -----------------------------------------------------------------------------
-- 5.3. Розділення таблиці buyer за алгоритмом хешування (HASH)
-- Критерій секціонування: первинний ключ користувача id_buyer, 4 партиції
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS buyer_hash;
CREATE TABLE buyer_hash (
    id_buyer INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    PRIMARY KEY (id_buyer)
)
PARTITION BY HASH (id_buyer)
PARTITIONS 4;

-- Запит вибірки клієнтів із секції p1 (HASH % 4 = 1)
SELECT id_buyer, email, registration_date
FROM buyer_hash
PARTITION (p1)
ORDER BY id_buyer ASC;

-- -----------------------------------------------------------------------------
-- 5.4. Моніторинг системних метаданих секціонування у information_schema
-- -----------------------------------------------------------------------------
SELECT table_name, partition_name, table_rows, partition_method
FROM information_schema.partitions
WHERE table_name IN ('cart_range', 'model_list', 'buyer_hash')
LIMIT 7;
"""

# Complete all-in-one file
sql_complete = header + "\n" + sql_01 + "\n" + sql_02 + "\n" + sql_03 + "\n" + sql_04 + "\n" + sql_05

files = {
    "01_subqueries.sql": sql_01,
    "02_joins.sql": sql_02,
    "03_case_expressions.sql": sql_03,
    "04_set_operations.sql": sql_04,
    "05_partitioning.sql": sql_05,
    "marketplace_3d_lab5_complete.sql": sql_complete
}

for fname, content in files.items():
    p = os.path.join(sql_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {p} ({len(content)} bytes)")

print("All SQL scripts created successfully!")
