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
