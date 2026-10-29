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
-- ЗАВДАННЯ 4. ОПЕРАЦІЇ РЕЛЯЦІЙНОЇ АЛГЕБРИ (UNION, INTERSECT, EXCEPT)
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 4.1. Оператор UNION (об'єднання без дублікатів)
-- -----------------------------------------------------------------------------

-- Запит 4.1.1. Об'єднання продавців та покупців
SELECT nickname AS user FROM seller UNION SELECT email AS user FROM buyer LIMIT 5;

-- Запит 4.1.2. Об'єднання назв категорій та ліцензій
SELECT name FROM category UNION SELECT license_name FROM license LIMIT 5;

-- Запит 4.1.3. Об'єднання покупців, які замовляли і які писали відгуки
SELECT id_buyer FROM cart UNION SELECT id_buyer FROM review LIMIT 5;

-- Запит 4.1.4. Об'єднання форматів файлів за розміром
SELECT format FROM model_file WHERE size_mb < 20 UNION SELECT format FROM model_file WHERE size_mb >= 20;

-- Запит 4.1.5. Об'єднання найдорожчих і найдешевших моделей
SELECT name FROM model_3d WHERE price > 50 UNION SELECT name FROM model_3d WHERE price < 25 LIMIT 5;


-- -----------------------------------------------------------------------------
-- 4.2. Оператор UNION ALL (об'єднання з дублікатами)
-- -----------------------------------------------------------------------------

-- Запит 4.2.1. Об'єднання замовлень та відгуків (UNION ALL)
SELECT id_buyer, 'Замовлення' AS act FROM cart UNION ALL SELECT id_buyer, 'Відгук' AS act FROM review LIMIT 5;

-- Запит 4.2.2. Об'єднання списків моделей категорій 1 та 2
SELECT name, price FROM model_3d WHERE id_category = 1 UNION ALL SELECT name, price FROM model_3d WHERE id_category = 2 LIMIT 5;

-- Запит 4.2.3. Об'єднання сум цін моделей та сум замовлень
SELECT price AS val FROM model_3d UNION ALL SELECT total_amount AS val FROM cart LIMIT 5;

-- Запит 4.2.4. Об'єднання всіх форматів файлів FBX та BLEND
SELECT format FROM model_file WHERE format = 'FBX' UNION ALL SELECT format FROM model_file WHERE format = 'BLEND' LIMIT 5;

-- Запит 4.2.5. Об'єднання дат реєстрацій покупців і дат замовлень
SELECT registration_date AS dt FROM buyer UNION ALL SELECT created_date AS dt FROM cart LIMIT 5;


-- -----------------------------------------------------------------------------
-- 4.3. Оператор INTERSECT (перетин множин)
-- -----------------------------------------------------------------------------

-- Запит 4.3.1. Покупці, які замовляли та залишили відгук (INTERSECT)
SELECT id_buyer FROM cart INTERSECT SELECT id_buyer FROM review LIMIT 5;

-- Запит 4.3.2. Моделі, які мають файли і є у замовленнях
SELECT id_model FROM model_file INTERSECT SELECT id_model FROM cart_item LIMIT 5;

-- Запит 4.3.3. Спільні формати для рубрик 1 і 2
SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 1 INTERSECT SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.id_category = 2;

-- Запит 4.3.4. Покупці, зареєстровані до березня, які замовляли
SELECT id_buyer FROM buyer WHERE registration_date < '2025-03-01' INTERSECT SELECT id_buyer FROM cart LIMIT 5;

-- Запит 4.3.5. Автори з високим рейтингом, моделі яких є в базі
SELECT id_seller FROM seller WHERE rating >= 4.5 INTERSECT SELECT id_seller FROM model_3d LIMIT 5;


-- -----------------------------------------------------------------------------
-- 4.4. Оператор EXCEPT (різниця множин)
-- -----------------------------------------------------------------------------

-- Запит 4.4.1. Зареєстровані покупці без замовлень (EXCEPT)
SELECT id_buyer FROM buyer EXCEPT SELECT id_buyer FROM cart;

-- Запит 4.4.2. Формати файлів тільки для High-Poly моделей
SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count > 30000 EXCEPT SELECT f.format FROM model_file f JOIN model_3d m ON f.id_model = m.id_model WHERE m.polygon_count < 10000;

-- Запит 4.4.3. Категорії, для яких створено моделі, але немає покупок
SELECT id_category FROM model_3d EXCEPT SELECT m.id_category FROM model_3d m JOIN cart_item ci ON m.id_model = ci.id_model;

-- Запит 4.4.4. Покупці з замовленнями, які не залишили відгук
SELECT id_buyer FROM cart EXCEPT SELECT id_buyer FROM review;

-- Запит 4.4.5. Моделі каталогу без жодного відгуку
SELECT id_model FROM model_3d EXCEPT SELECT id_model FROM review LIMIT 5;
