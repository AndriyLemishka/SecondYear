-- =============================================================================
-- ДИСЦИПЛІНА: «Організація баз даних та знань»
-- ЛАБОРАТОРНА РОБОТА № 5: «Написання запитів SELECT. Ч. 2»
-- Тема: «Сайт продажу 3D-моделей (маркетплейс)» (БД marketplace_3d)
-- Виконав: студент гр. ПП-24 Лемішка А.А.
-- Викладач: Спас Н.Я.
-- Національний університет «Львівська політехніка», Кафедра САП, 2026 р.
-- =============================================================================

USE marketplace_3d;


-- =============================================================================
-- ЗАВДАННЯ 2. ОПЕРАТОРИ INNER JOIN ТА OUTER JOIN
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 2.1. Внутрішнє з'єднання INNER JOIN
-- -----------------------------------------------------------------------------

-- Запит 2.1.1. Моделі з назвами категорій (INNER JOIN)
SELECT m.name, c.name AS category FROM model_3d m JOIN category c ON m.id_category = c.id_category LIMIT 5;

-- Запит 2.1.2. Моделі з псевдонімами авторів (INNER JOIN)
SELECT m.name, s.nickname FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;

-- Запит 2.1.3. Файли моделей із назвою моделі (INNER JOIN)
SELECT m.name, f.format, f.size_mb FROM model_3d m JOIN model_file f ON m.id_model = f.id_model LIMIT 5;

-- Запит 2.1.4. Замовлення з поштою покупця (INNER JOIN)
SELECT b.email, c.total_amount FROM buyer b JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;

-- Запит 2.1.5. Відгуки з назвами моделей (INNER JOIN)
SELECT m.name, r.rating, r.comment_text FROM model_3d m JOIN review r ON m.id_model = r.id_model LIMIT 5;


-- -----------------------------------------------------------------------------
-- 2.2. Ліве зовнішнє з'єднання LEFT OUTER JOIN
-- -----------------------------------------------------------------------------

-- Запит 2.2.1. Покупці та їхні замовлення з NULL (LEFT JOIN)
SELECT b.email, c.id_cart, c.total_amount FROM buyer b LEFT JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;

-- Запит 2.2.2. Автори та їхні моделі (LEFT JOIN)
SELECT s.nickname, m.name, m.price FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller LIMIT 5;

-- Запит 2.2.3. Категорії та закріплені моделі (LEFT JOIN)
SELECT c.name, m.name AS model FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category LIMIT 5;

-- Запит 2.2.4. Ліцензії та моделі (LEFT JOIN)
SELECT l.license_name, m.name FROM license l LEFT JOIN model_3d m ON l.id_license = m.id_license LIMIT 5;

-- Запит 2.2.5. Моделі та відгуки покупців (LEFT JOIN)
SELECT m.name, r.rating FROM model_3d m LEFT JOIN review r ON m.id_model = r.id_model LIMIT 5;


-- -----------------------------------------------------------------------------
-- 2.3. Праве зовнішнє з'єднання RIGHT OUTER JOIN
-- -----------------------------------------------------------------------------

-- Запит 2.3.1. Категорії та моделі (RIGHT JOIN)
SELECT c.name, m.name AS model FROM model_3d m RIGHT JOIN category c ON m.id_category = c.id_category LIMIT 5;

-- Запит 2.3.2. Покупці та їхні відгуки (RIGHT JOIN)
SELECT b.email, r.rating FROM review r RIGHT JOIN buyer b ON r.id_buyer = b.id_buyer LIMIT 5;

-- Запит 2.3.3. Ліцензії та моделі (RIGHT JOIN)
SELECT l.license_name, m.name FROM model_3d m RIGHT JOIN license l ON m.id_license = l.id_license LIMIT 5;

-- Запит 2.3.4. Автори та каталог робіт (RIGHT JOIN)
SELECT s.nickname, m.name FROM model_3d m RIGHT JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;

-- Запит 2.3.5. Замовлення та позиції чека (RIGHT JOIN)
SELECT c.id_cart, ci.fixed_price FROM cart_item ci RIGHT JOIN cart c ON ci.id_cart = c.id_cart LIMIT 5;


-- -----------------------------------------------------------------------------
-- 2.4. Декартовий добуток CROSS JOIN
-- -----------------------------------------------------------------------------

-- Запит 2.4.1. Декартовий добуток категорій та ліцензій
SELECT c.name, l.license_name FROM category c CROSS JOIN license l LIMIT 5;

-- Запит 2.4.2. Комбінація форматів файлів і категорій
SELECT DISTINCT f.format, c.name FROM model_file f CROSS JOIN category c LIMIT 5;

-- Запит 2.4.3. Матриця статусів замовлень та покупців
SELECT DISTINCT c.status, b.email FROM cart c CROSS JOIN buyer b LIMIT 5;

-- Запит 2.4.4. Поєднання авторів та типів використання ліцензій
SELECT s.nickname, l.usage_type FROM seller s CROSS JOIN license l LIMIT 5;

-- Запит 2.4.5. CROSS JOIN комерційних ліцензій та рубрик
SELECT c.name, l.usage_type FROM category c CROSS JOIN license l WHERE l.usage_type = 'Commercial' LIMIT 5;


-- -----------------------------------------------------------------------------
-- 2.5. Багатотабличні з'єднання (3+ таблиць)
-- -----------------------------------------------------------------------------

-- Запит 2.5.1. Зведення моделі, автора та категорії (3 таблиці)
SELECT m.name, s.nickname, c.name AS cat FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller JOIN category c ON m.id_category = c.id_category LIMIT 5;

-- Запит 2.5.2. Зведення моделі, категорії та ліцензії (3 таблиці)
SELECT m.name, c.name AS cat, l.license_name FROM model_3d m JOIN category c ON m.id_category = c.id_category JOIN license l ON m.id_license = l.id_license LIMIT 5;

-- Запит 2.5.3. Зведення формату файлу, моделі та рубрики (3 таблиці)
SELECT f.format, m.name, c.name AS cat FROM model_file f JOIN model_3d m ON f.id_model = m.id_model JOIN category c ON m.id_category = c.id_category LIMIT 5;

-- Запит 2.5.4. Зведення покупця, замовлення та моделі (4 таблиці)
SELECT b.email, c.id_cart, m.name FROM buyer b JOIN cart c ON b.id_buyer = c.id_buyer JOIN cart_item ci ON c.id_cart = ci.id_cart JOIN model_3d m ON ci.id_model = m.id_model LIMIT 5;

-- Запит 2.5.5. Зведення покупця, відгуку та оціненої моделі (3 таблиці)
SELECT b.email, m.name, r.rating FROM buyer b JOIN review r ON b.id_buyer = r.id_buyer JOIN model_3d m ON r.id_model = m.id_model LIMIT 5;
