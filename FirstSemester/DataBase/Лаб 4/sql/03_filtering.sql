-- Лабораторна робота № 4
-- Студент: Лемішка А.А., ПП-24
-- Завдання 3. Фільтрація даних (IN, BETWEEN, LIKE, REGEXP)

USE marketplace_3d;

-- ----------------------------------------
-- 3.1. Команда IN
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
-- 3.2. Команда BETWEEN
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
-- 3.3. Команда LIKE
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
-- 3.4. Команда REGEXP
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

