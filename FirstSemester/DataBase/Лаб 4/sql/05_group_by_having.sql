-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 5. Групування даних (GROUP BY, HAVING)

USE marketplace_3d;

-- ----------------------------------------
-- 5.1. Команда GROUP BY
-- ----------------------------------------

-- Запит 5.1.1: Кількість файлів для кожного формату
SELECT format, COUNT(*) FROM model_file GROUP BY format;

-- Запит 5.1.2: Кількість замовлень для кожного статусу
SELECT status, COUNT(*) FROM cart GROUP BY status;

-- Запит 5.1.3: Кількість моделей у кожній категорії
SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category;

-- ----------------------------------------
-- 5.2. Команда HAVING
-- ----------------------------------------

-- Запит 5.2.1: Формати де більше 3 файлів
SELECT format, COUNT(*) FROM model_file GROUP BY format HAVING COUNT(*) > 3;

-- Запит 5.2.2: Статуси де 2 або більше замовлень
SELECT status, COUNT(*) FROM cart GROUP BY status HAVING COUNT(*) >= 2;

-- Запит 5.2.3: Категорії де 2 або більше моделей
SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category HAVING COUNT(*) >= 2;

