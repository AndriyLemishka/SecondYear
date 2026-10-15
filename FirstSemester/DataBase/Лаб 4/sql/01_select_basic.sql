-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 1. Прості запити (SELECT, LIMIT, DISTINCT, IS NULL)

USE marketplace_3d;

-- ----------------------------------------
-- 1.1. SELECT та FROM
-- ----------------------------------------

-- Запит 1.1.1: Вибірка всіх полів з таблиці моделей
SELECT * FROM model_3d LIMIT 5;

-- Запит 1.1.2: Вибірка назви та ціни моделей
SELECT name, price FROM model_3d LIMIT 5;

-- Запит 1.1.3: Вибірка пошти покупців
SELECT id_buyer, email FROM buyer LIMIT 5;

-- Запит 1.1.4: Вибірка з псевдонімом стовпця
SELECT nickname AS author, rating FROM seller LIMIT 5;

-- Запит 1.1.5: Вибірка з простим множенням ціни
SELECT name, price, price * 2 AS double_price FROM model_3d LIMIT 5;

-- ----------------------------------------
-- 1.2. Команда LIMIT
-- ----------------------------------------

-- Запит 1.2.1: Вибірка перших 3 моделей
SELECT * FROM model_3d LIMIT 3;

-- Запит 1.2.2: Вибірка перших 5 покупців
SELECT * FROM buyer LIMIT 5;

-- Запит 1.2.3: Вибірка перших 2 продавців
SELECT * FROM seller LIMIT 2;

-- Запит 1.2.4: Вибірка 4 категорій
SELECT * FROM category LIMIT 4;

-- Запит 1.2.5: Вибірка 3 моделей починаючи з 2-го рядка
SELECT * FROM model_3d LIMIT 2, 3;

-- ----------------------------------------
-- 1.3. Команда DISTINCT
-- ----------------------------------------

-- Запит 1.3.1: Унікальні формати файлів
SELECT DISTINCT format FROM model_file;

-- Запит 1.3.2: Унікальні статуси замовлень
SELECT DISTINCT status FROM cart;

-- Запит 1.3.3: Унікальні типи ліцензій
SELECT DISTINCT usage_type FROM license;

-- Запит 1.3.4: Унікальні оцінки у відгуках
SELECT DISTINCT rating FROM review;

-- Запит 1.3.5: Унікальні значення наявності текстури
SELECT DISTINCT has_texture FROM model_3d;

-- ----------------------------------------
-- 1.4. Команда IS NULL
-- ----------------------------------------

-- Запит 1.4.1: Моделі без опису
SELECT * FROM model_3d WHERE description IS NULL;

-- Запит 1.4.2: Моделі з описом
SELECT * FROM model_3d WHERE description IS NOT NULL LIMIT 5;

-- Запит 1.4.3: Відгуки без тексту коментаря
SELECT * FROM review WHERE comment_text IS NULL;

-- Запит 1.4.4: Відгуки з текстом коментаря
SELECT * FROM review WHERE comment_text IS NOT NULL LIMIT 5;

-- Запит 1.4.5: Продавці з наявним рейтингом
SELECT * FROM seller WHERE rating IS NOT NULL LIMIT 5;

