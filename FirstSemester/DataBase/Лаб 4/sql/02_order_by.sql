-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 2. Сортування даних (ORDER BY, DESC)

USE marketplace_3d;

-- ----------------------------------------
-- 2.1. Команда ORDER BY
-- ----------------------------------------

-- Запит 2.1.1: Сортування моделей за зростанням ціни
SELECT id_model, name, price FROM model_3d ORDER BY price LIMIT 5;

-- Запит 2.1.2: Сортування продавців за рейтингом
SELECT * FROM seller ORDER BY rating LIMIT 5;

-- Запит 2.1.3: Сортування категорій за алфавітом
SELECT * FROM category ORDER BY name LIMIT 5;

-- ----------------------------------------
-- 2.2. Команда DESC
-- ----------------------------------------

-- Запит 2.2.1: Сортування моделей від найдорожчої
SELECT id_model, name, price FROM model_3d ORDER BY price DESC LIMIT 5;

-- Запит 2.2.2: Сортування продавців від найвищого рейтингу
SELECT * FROM seller ORDER BY rating DESC LIMIT 5;

-- Запит 2.2.3: Сортування замовлень від найбільшої суми
SELECT * FROM cart ORDER BY total_amount DESC LIMIT 5;

