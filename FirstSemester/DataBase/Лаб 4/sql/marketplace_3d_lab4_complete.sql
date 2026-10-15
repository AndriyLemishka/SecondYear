-- Лабораторна робота № 4. Всі 79 запитів
-- Студент: Лемішка А.А., ПП-24

USE marketplace_3d;

-- ----------------------------------------
-- Завдання 1. 1.1. SELECT та FROM
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
-- Завдання 1. 1.2. Команда LIMIT
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
-- Завдання 1. 1.3. Команда DISTINCT
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
-- Завдання 1. 1.4. Команда IS NULL
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

-- ----------------------------------------
-- Завдання 2. 2.1. Команда ORDER BY
-- ----------------------------------------

-- Запит 2.1.1: Сортування моделей за зростанням ціни
SELECT id_model, name, price FROM model_3d ORDER BY price LIMIT 5;

-- Запит 2.1.2: Сортування продавців за рейтингом
SELECT * FROM seller ORDER BY rating LIMIT 5;

-- Запит 2.1.3: Сортування категорій за алфавітом
SELECT * FROM category ORDER BY name LIMIT 5;

-- ----------------------------------------
-- Завдання 2. 2.2. Команда DESC
-- ----------------------------------------

-- Запит 2.2.1: Сортування моделей від найдорожчої
SELECT id_model, name, price FROM model_3d ORDER BY price DESC LIMIT 5;

-- Запит 2.2.2: Сортування продавців від найвищого рейтингу
SELECT * FROM seller ORDER BY rating DESC LIMIT 5;

-- Запит 2.2.3: Сортування замовлень від найбільшої суми
SELECT * FROM cart ORDER BY total_amount DESC LIMIT 5;

-- ----------------------------------------
-- Завдання 3. 3.1. Команда IN
-- ----------------------------------------

-- Запит 3.1.1: Файли форматів FBX та OBJ
SELECT * FROM model_file WHERE format IN ('FBX', 'OBJ') LIMIT 5;

-- Запит 3.1.2: Замовлення зі статусами Completed та Active
SELECT * FROM cart WHERE status IN ('Completed', 'Active') LIMIT 5;

-- Запит 3.1.3: Моделі з категорій 1, 2, 3
SELECT id_model, name, id_category, price FROM model_3d WHERE id_category IN (1, 2, 3);

-- Запит 3.1.4: Файли інших форматів через NOT IN
SELECT * FROM model_file WHERE format NOT IN ('FBX', 'OBJ') LIMIT 5;

-- Запит 3.1.5: Відгуки з оцінками 4 та 5
SELECT * FROM review WHERE rating IN (4, 5) LIMIT 5;

-- ----------------------------------------
-- Завдання 3. 3.2. Команда BETWEEN
-- ----------------------------------------

-- Запит 3.2.1: Моделі з ціною від 10 до 30
SELECT id_model, name, price FROM model_3d WHERE price BETWEEN 10 AND 30;

-- Запит 3.2.2: Продавці з рейтингом від 4.5 до 5
SELECT * FROM seller WHERE rating BETWEEN 4.5 AND 5.0;

-- Запит 3.2.3: Файли розміром від 10 до 50 МБ
SELECT * FROM model_file WHERE size_mb BETWEEN 10 AND 50;

-- Запит 3.2.4: Замовлення на суму від 20 до 50
SELECT * FROM cart WHERE total_amount BETWEEN 20 AND 50;

-- Запит 3.2.5: Моделі з ціною не від 10 до 30
SELECT id_model, name, price FROM model_3d WHERE price NOT BETWEEN 10 AND 30;

-- ----------------------------------------
-- Завдання 3. 3.3. Команда LIKE
-- ----------------------------------------

-- Запит 3.3.1: Моделі на літеру C
SELECT id_model, name, price FROM model_3d WHERE name LIKE 'C%';

-- Запит 3.3.2: Моделі зі словом Car у назві
SELECT id_model, name, price FROM model_3d WHERE name LIKE '%Car%';

-- Запит 3.3.3: Пошта покупців на mail.com
SELECT * FROM buyer WHERE email LIKE '%@mail.com' LIMIT 5;

-- Запит 3.3.4: Пошта з одним символом після user_
SELECT * FROM buyer WHERE email LIKE 'user_@%';

-- Запит 3.3.5: Моделі без слова Car у назві
SELECT id_model, name, price FROM model_3d WHERE name NOT LIKE '%Car%' LIMIT 5;

-- ----------------------------------------
-- Завдання 3. 3.4. Команда REGEXP
-- ----------------------------------------

-- Запит 3.4.1: Моделі зі словом Car або Rifle
SELECT id_model, name, price FROM model_3d WHERE name REGEXP 'Car|Rifle';

-- Запит 3.4.2: Моделі що починаються на Space
SELECT id_model, name, price FROM model_3d WHERE name REGEXP '^Space';

-- Запит 3.4.3: Моделі що закінчуються на Station
SELECT id_model, name, price FROM model_3d WHERE name REGEXP 'Station$';

-- Запит 3.4.4: Моделі що містять цифру
SELECT id_model, name, price FROM model_3d WHERE name REGEXP '[0-9]';

-- Запит 3.4.5: Відгуки зі словами Amazing або Good
SELECT * FROM review WHERE comment_text REGEXP 'Amazing|Good';

-- ----------------------------------------
-- Завдання 4. 4.1. Функція AVG
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
-- Завдання 4. 4.2. Функція SUM
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
-- Завдання 4. 4.3. Функція MIN
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
-- Завдання 4. 4.4. Функція MAX
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
-- Завдання 4. 4.5. Функція COUNT
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

-- ----------------------------------------
-- Завдання 5. 5.1. Команда GROUP BY
-- ----------------------------------------

-- Запит 5.1.1: Кількість файлів для кожного формату
SELECT format, COUNT(*) FROM model_file GROUP BY format;

-- Запит 5.1.2: Кількість замовлень для кожного статусу
SELECT status, COUNT(*) FROM cart GROUP BY status;

-- Запит 5.1.3: Кількість моделей у кожній категорії
SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category;

-- ----------------------------------------
-- Завдання 5. 5.2. Команда HAVING
-- ----------------------------------------

-- Запит 5.2.1: Формати де більше 3 файлів
SELECT format, COUNT(*) FROM model_file GROUP BY format HAVING COUNT(*) > 3;

-- Запит 5.2.2: Статуси де 2 або більше замовлень
SELECT status, COUNT(*) FROM cart GROUP BY status HAVING COUNT(*) >= 2;

-- Запит 5.2.3: Категорії де 2 або більше моделей
SELECT id_category, COUNT(*) FROM model_3d GROUP BY id_category HAVING COUNT(*) >= 2;

-- ----------------------------------------
-- Завдання 6. 6.1. Команда VIEW
-- ----------------------------------------

-- Запит 6.1.1: Створення VIEW та вибірка моделей з ціною більше 15
DROP VIEW IF EXISTS v_models;
CREATE VIEW v_models AS
SELECT id_model, name, price
FROM model_3d;

SELECT * FROM v_models WHERE price > 15;

-- Запит 6.1.2: Вибірка з VIEW з сортуванням за ціною
SELECT * FROM v_models ORDER BY price DESC;

