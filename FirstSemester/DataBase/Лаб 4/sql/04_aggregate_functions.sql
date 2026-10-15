-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 4. Агрегатні функції (AVG, SUM, MIN, MAX, COUNT)

USE marketplace_3d;

-- ----------------------------------------
-- 4.1. Функція AVG
-- ----------------------------------------

-- Запит 4.1.1: Середня ціна всіх моделей
SELECT AVG(price) FROM model_3d;

-- Запит 4.1.2: Середній рейтинг продавців
SELECT AVG(rating) FROM seller;

-- Запит 4.1.3: Середній розмір файлів
SELECT AVG(size_mb) FROM model_file;

-- Запит 4.1.4: Середня сума замовлення
SELECT AVG(total_amount) FROM cart;

-- Запит 4.1.5: Середня оцінка у відгуках
SELECT AVG(rating) FROM review;

-- ----------------------------------------
-- 4.2. Функція SUM
-- ----------------------------------------

-- Запит 4.2.1: Сума цін усіх моделей
SELECT SUM(price) FROM model_3d;

-- Запит 4.2.2: Загальна сума замовлень
SELECT SUM(total_amount) FROM cart;

-- Запит 4.2.3: Загальний розмір усіх файлів
SELECT SUM(size_mb) FROM model_file;

-- Запит 4.2.4: Загальна кількість полігонів
SELECT SUM(polygon_count) FROM model_3d;

-- Запит 4.2.5: Сума виконаних замовлень
SELECT SUM(total_amount) FROM cart WHERE status = 'Completed';

-- ----------------------------------------
-- 4.3. Функція MIN
-- ----------------------------------------

-- Запит 4.3.1: Мінімальна ціна моделі
SELECT MIN(price) FROM model_3d;

-- Запит 4.3.2: Мінімальний рейтинг продавця
SELECT MIN(rating) FROM seller;

-- Запит 4.3.3: Мінімальний розмір файлу
SELECT MIN(size_mb) FROM model_file;

-- Запит 4.3.4: Мінімальна сума замовлення
SELECT MIN(total_amount) FROM cart;

-- Запит 4.3.5: Мінімальна кількість полігонів
SELECT MIN(polygon_count) FROM model_3d;

-- ----------------------------------------
-- 4.4. Функція MAX
-- ----------------------------------------

-- Запит 4.4.1: Максимальна ціна моделі
SELECT MAX(price) FROM model_3d;

-- Запит 4.4.2: Максимальний рейтинг продавця
SELECT MAX(rating) FROM seller;

-- Запит 4.4.3: Максимальний розмір файлу
SELECT MAX(size_mb) FROM model_file;

-- Запит 4.4.4: Максимальна сума замовлення
SELECT MAX(total_amount) FROM cart;

-- Запит 4.4.5: Максимальна кількість полігонів
SELECT MAX(polygon_count) FROM model_3d;

-- ----------------------------------------
-- 4.5. Функція COUNT
-- ----------------------------------------

-- Запит 4.5.1: Загальна кількість моделей
SELECT COUNT(*) FROM model_3d;

-- Запит 4.5.2: Кількість покупців
SELECT COUNT(*) FROM buyer;

-- Запит 4.5.3: Кількість продавців
SELECT COUNT(*) FROM seller;

-- Запит 4.5.4: Кількість відгуків з коментарем
SELECT COUNT(comment_text) FROM review;

-- Запит 4.5.5: Кількість унікальних форматів
SELECT COUNT(DISTINCT format) FROM model_file;

