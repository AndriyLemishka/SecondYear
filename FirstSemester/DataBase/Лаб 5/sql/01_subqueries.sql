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
-- ЗАВДАННЯ 1. ПІДЗАПИТИ (КОРЕЛЮЮЧІ ТА НЕКОРЕЛЮЮЧІ)
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 1.1. Скалярні підзапити у реченні SELECT
-- -----------------------------------------------------------------------------

-- Запит 1.1.1. Вибірка ціни та середньої ціни каталогу
SELECT name, price, (SELECT AVG(price) FROM model_3d) AS avg_price FROM model_3d LIMIT 5;

-- Запит 1.1.2. Вибірка ціни та максимальної ціни в базі
SELECT name, price, (SELECT MAX(price) FROM model_3d) AS max_price FROM model_3d LIMIT 5;

-- Запит 1.1.3. Підрахунок кількості моделей кожного автора
SELECT nickname, (SELECT COUNT(*) FROM model_3d m WHERE m.id_seller = s.id_seller) AS cnt FROM seller s LIMIT 5;

-- Запит 1.1.4. Підрахунок кількості замовлень покупця
SELECT email, (SELECT COUNT(*) FROM cart c WHERE c.id_buyer = b.id_buyer) AS orders FROM buyer b LIMIT 5;

-- Запит 1.1.5. Підрахунок кількості моделей у категорії
SELECT name, (SELECT COUNT(*) FROM model_3d m WHERE m.id_category = c.id_category) AS items FROM category c LIMIT 5;


-- -----------------------------------------------------------------------------
-- 1.2. Підзапити у WHERE з операторами порівняння (=, >, <)
-- -----------------------------------------------------------------------------

-- Запит 1.2.1. Модель із максимальною ціною
SELECT name, price FROM model_3d WHERE price = (SELECT MAX(price) FROM model_3d);

-- Запит 1.2.2. Моделі дорожчі за середню ціну каталогу
SELECT name, price FROM model_3d WHERE price > (SELECT AVG(price) FROM model_3d) LIMIT 5;

-- Запит 1.2.3. Моделі дорожчі за середню ціну своєї категорії
SELECT name, price FROM model_3d m WHERE price > (SELECT AVG(price) FROM model_3d WHERE id_category = m.id_category) LIMIT 5;

-- Запит 1.2.4. Файли розміром менше середнього
SELECT format, size_mb FROM model_file WHERE size_mb < (SELECT AVG(size_mb) FROM model_file) LIMIT 5;

-- Запит 1.2.5. Замовлення на суму більшу за середню
SELECT id_cart, total_amount FROM cart WHERE total_amount > (SELECT AVG(total_amount) FROM cart) LIMIT 5;


-- -----------------------------------------------------------------------------
-- 1.3. Підзапити з операторами IN та NOT IN
-- -----------------------------------------------------------------------------

-- Запит 1.3.1. Моделі авторів з рейтингом від 4.70 (IN)
SELECT name, price FROM model_3d WHERE id_seller IN (SELECT id_seller FROM seller WHERE rating >= 4.7);

-- Запит 1.3.2. Покупці, які мають замовлення (IN)
SELECT email FROM buyer WHERE id_buyer IN (SELECT id_buyer FROM cart) LIMIT 5;

-- Запит 1.3.3. Категорії, для яких створено моделі (IN)
SELECT name FROM category WHERE id_category IN (SELECT id_category FROM model_3d) LIMIT 5;

-- Запит 1.3.4. Покупці без жодного замовлення (NOT IN)
SELECT email FROM buyer WHERE id_buyer NOT IN (SELECT id_buyer FROM cart WHERE id_buyer IS NOT NULL);

-- Запит 1.3.5. Автори без створених моделей (NOT IN)
SELECT nickname FROM seller WHERE id_seller NOT IN (SELECT id_seller FROM model_3d);


-- -----------------------------------------------------------------------------
-- 1.4. Корелюючі підзапити з EXISTS та NOT EXISTS
-- -----------------------------------------------------------------------------

-- Запит 1.4.1. Покупці, що мають замовлення (EXISTS)
SELECT email FROM buyer b WHERE EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer) LIMIT 5;

-- Запит 1.4.2. Покупці без жодного замовлення (NOT EXISTS)
SELECT email FROM buyer b WHERE NOT EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer);

-- Запит 1.4.3. Моделі, які мають завантажені файли (EXISTS)
SELECT name FROM model_3d m WHERE EXISTS (SELECT 1 FROM model_file f WHERE f.id_model = m.id_model) LIMIT 5;

-- Запит 1.4.4. Моделі, для яких залишено відгуки (EXISTS)
SELECT name FROM model_3d m WHERE EXISTS (SELECT 1 FROM review r WHERE r.id_model = m.id_model) LIMIT 5;

-- Запит 1.4.5. Категорії без моделей (NOT EXISTS)
SELECT name FROM category c WHERE NOT EXISTS (SELECT 1 FROM model_3d m WHERE m.id_category = c.id_category);


-- -----------------------------------------------------------------------------
-- 1.5. Підзапити в командах модифікації даних (UPDATE, INSERT, DELETE)
-- -----------------------------------------------------------------------------

-- Запит 1.5.1. Оновлення вартості замовлень через підзапит (UPDATE)
UPDATE cart SET total_amount = (SELECT SUM(fixed_price) FROM cart_item WHERE id_cart = cart.id_cart);

-- Запит 1.5.2. Збільшення рейтингу авторів дорогих моделей (UPDATE)
UPDATE seller SET rating = rating + 0.1 WHERE id_seller IN (SELECT id_seller FROM model_3d WHERE price > 50);

-- Запит 1.5.3. Перевірка суми замовлень після оновлення
SELECT id_cart, total_amount FROM cart LIMIT 5;

-- Запит 1.5.4. Перевірка оновленого рейтингу авторів
SELECT nickname, rating FROM seller LIMIT 5;

-- Запит 1.5.5. Пошук порожніх кошиків перед видаленням
SELECT id_cart, status FROM cart WHERE id_cart NOT IN (SELECT id_cart FROM cart_item);
