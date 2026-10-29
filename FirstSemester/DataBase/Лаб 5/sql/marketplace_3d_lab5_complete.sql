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
-- ЗАВДАННЯ 5. РОЗДІЛЕННЯ ТАБЛИЦЬ (RANGE, LIST, HASH)
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 5.1. Розділення таблиці за RANGE (діапазони дат/років)
-- -----------------------------------------------------------------------------

-- Запит 5.1.1. Вибірка замовлень 2025 року з партиції p_2025
SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2025) LIMIT 5;

-- Запит 5.1.2. Вибірка замовлень з діапазону p_2024
SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2024);

-- Запит 5.1.3. Пошук замовлення за датою (Partition Pruning)
SELECT id_cart, status, total_amount FROM cart_range WHERE created_date = '2025-01-20';

-- Запит 5.1.4. Підрахунок кількості замовлень у секції p_2025
SELECT COUNT(*) AS total_orders FROM cart_range PARTITION (p_2025);

-- Запит 5.1.5. Вибірка завершених замовлень у секції p_2025
SELECT id_cart, total_amount FROM cart_range PARTITION (p_2025) WHERE status = 'Completed' LIMIT 5;


-- -----------------------------------------------------------------------------
-- 5.2. Розділення таблиці за LIST (списки категорій)
-- -----------------------------------------------------------------------------

-- Запит 5.2.1. Вибірка персонажів і техніки з p_characters_vehicles
SELECT id_model, name, id_category, price FROM model_list PARTITION (p_characters_vehicles) LIMIT 5;

-- Запит 5.2.2. Вибірка зброї та оточення з p_weapons_environment
SELECT id_model, name, id_category, price FROM model_list PARTITION (p_weapons_environment) LIMIT 5;

-- Запит 5.2.3. Вибірка реквізиту та природи з p_props_nature
SELECT id_model, name, id_category FROM model_list PARTITION (p_props_nature);

-- Запит 5.2.4. Вибірка архітектури з p_architecture_scifi
SELECT id_model, name, price FROM model_list PARTITION (p_architecture_scifi);

-- Запит 5.2.5. Пошук моделі за точною рубрикою з відсіканням секцій
SELECT id_model, name, id_category FROM model_list WHERE id_category = 1;


-- -----------------------------------------------------------------------------
-- 5.3. Розділення таблиці за HASH (хеш ID)
-- -----------------------------------------------------------------------------

-- Запит 5.3.1. Вибірка покупців із партиції p0 (ID % 4 = 0)
SELECT id_buyer, email FROM buyer_hash PARTITION (p0);

-- Запит 5.3.2. Вибірка покупців із партиції p1 (ID % 4 = 1)
SELECT id_buyer, email FROM buyer_hash PARTITION (p1);

-- Запит 5.3.3. Вибірка покупців із партиції p2 (ID % 4 = 2)
SELECT id_buyer, email FROM buyer_hash PARTITION (p2);

-- Запит 5.3.4. Вибірка покупців із партиції p3 (ID % 4 = 3)
SELECT id_buyer, email FROM buyer_hash PARTITION (p3);

-- Запит 5.3.5. Пошук покупця за ID у потрібній HASH-партиції
SELECT id_buyer, email FROM buyer_hash WHERE id_buyer = 5;


-- -----------------------------------------------------------------------------
-- 5.4. Системний моніторинг та Partition Pruning
-- -----------------------------------------------------------------------------

-- Запит 5.4.1. Перевірка відсікання секцій для RANGE (EXPLAIN)
EXPLAIN SELECT * FROM cart_range WHERE created_date = '2025-01-20';

-- Запит 5.4.2. Перевірка відсікання секцій для LIST (EXPLAIN)
EXPLAIN SELECT * FROM model_list WHERE id_category = 1;

-- Запит 5.4.3. Перевірка відсікання секцій для HASH (EXPLAIN)
EXPLAIN SELECT * FROM buyer_hash WHERE id_buyer = 5;

-- Запит 5.4.4. Моніторинг рядків у секціях RANGE
SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'cart_range';

-- Запит 5.4.5. Моніторинг рядків у секціях HASH
SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'buyer_hash';
