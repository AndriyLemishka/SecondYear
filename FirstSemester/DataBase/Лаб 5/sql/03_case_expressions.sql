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
-- ЗАВДАННЯ 3. ОПЕРАТОР CASE
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 3.1. CASE для класифікації та групування
-- -----------------------------------------------------------------------------

-- Запит 3.1.1. Класифікація полігонів (Low/High)
SELECT name, polygon_count, CASE WHEN polygon_count < 20000 THEN 'Low' ELSE 'High' END AS poly_tier FROM model_3d LIMIT 5;

-- Запит 3.1.2. Цінова сегментація моделей
SELECT name, price, CASE WHEN price < 30 THEN 'Дешева' WHEN price < 60 THEN 'Середня' ELSE 'Дорога' END AS pr_cat FROM model_3d LIMIT 5;

-- Запит 3.1.3. Класифікація авторів за рейтингом
SELECT nickname, rating, CASE WHEN rating >= 4.5 THEN 'Top' ELSE 'Normal' END AS s_tier FROM seller LIMIT 5;

-- Запит 3.1.4. Класифікація ваги файлів (Small/Large)
SELECT format, size_mb, CASE WHEN size_mb < 30 THEN 'Small' ELSE 'Large' END AS sz_grp FROM model_file LIMIT 5;

-- Запит 3.1.5. Текстовий опис наявності текстур
SELECT name, has_texture, CASE has_texture WHEN 'Yes' THEN 'Є текстури' ELSE 'Немає' END AS tex_status FROM model_3d LIMIT 5;


-- -----------------------------------------------------------------------------
-- 3.2. CASE для динамічного розрахунку цін та знижок
-- -----------------------------------------------------------------------------

-- Запит 3.2.1. Розрахунок знижки 10% на дорогі моделі
SELECT name, price, CASE WHEN price > 50 THEN price * 0.9 ELSE price END AS sale_price FROM model_3d LIMIT 5;

-- Запит 3.2.2. Нарахування ПДВ залежно від вартості
SELECT name, price, CASE WHEN price > 40 THEN price * 1.2 ELSE price * 1.05 END AS with_vat FROM model_3d LIMIT 5;

-- Запит 3.2.3. Знижка від рейтингу автора моделі
SELECT m.name, s.rating, CASE WHEN s.rating >= 4.8 THEN 15 ELSE 5 END AS disc_pct FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller LIMIT 5;

-- Запит 3.2.4. Визначення статусу лояльності покупця
SELECT email, CASE WHEN id_buyer <= 5 THEN 'VIP' ELSE 'Standard' END AS b_status FROM buyer LIMIT 5;

-- Запит 3.2.5. Оцінка коментаря за числовим рейтингом
SELECT rating, comment_text, CASE WHEN rating >= 4 THEN 'Добре' ELSE 'Погано' END AS grade FROM review LIMIT 5;


-- -----------------------------------------------------------------------------
-- 3.3. CASE усередині агрегатних функцій
-- -----------------------------------------------------------------------------

-- Запит 3.3.1. Підрахунок текстурованих моделей у категоріях
SELECT c.name, SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS tex_cnt FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;

-- Запит 3.3.2. Підрахунок дорогих моделей (> 40) у категоріях
SELECT c.name, COUNT(CASE WHEN m.price > 40 THEN 1 END) AS exp_cnt FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;

-- Запит 3.3.3. Середня ціна дешевих моделей (< 50) за рубриками
SELECT c.name, AVG(CASE WHEN m.price < 50 THEN m.price END) AS avg_cheap FROM category c LEFT JOIN model_3d m ON c.id_category = m.id_category GROUP BY c.name LIMIT 5;

-- Запит 3.3.4. Підрахунок завершених замовлень покупців
SELECT id_buyer, SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS ok_orders FROM cart GROUP BY id_buyer LIMIT 5;

-- Запит 3.3.5. Підрахунок відгуків з оцінкою 5 зірок
SELECT id_model, SUM(CASE WHEN rating = 5 THEN 1 ELSE 0 END) AS stars_5 FROM review GROUP BY id_model LIMIT 5;
