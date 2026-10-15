-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 6. Представлення VIEW

USE marketplace_3d;

-- ----------------------------------------
-- 6.1. Команда VIEW
-- ----------------------------------------

-- Запит 6.1.1: Створення VIEW та вибірка моделей з ціною більше 15
DROP VIEW IF EXISTS v_models;
CREATE VIEW v_models AS
SELECT id_model, name, price
FROM model_3d;

SELECT * FROM v_models WHERE price > 15;

-- Запит 6.1.2: Вибірка з VIEW з сортуванням за ціною
SELECT * FROM v_models ORDER BY price DESC;

