-- Завдання 2. Формування зведених таблиць з використанням операторів INNER JOIN та OUTER JOIN
USE marketplace_3d;

-- Запит 2.1: Внутрішнє з'єднання двох таблиць (INNER JOIN моделей та категорій)
SELECT m.name, c.name AS category FROM model_3d m JOIN category c ON m.id_category = c.id_category LIMIT 5;

-- Запит 2.2: Внутрішнє з'єднання чотирьох таблиць (модель, автор, категорія, ліцензія)
SELECT m.name, s.nickname, c.name AS category, l.license_name FROM model_3d m JOIN seller s ON m.id_seller = s.id_seller JOIN category c ON m.id_category = c.id_category JOIN license l ON m.id_license = l.id_license LIMIT 5;

-- Запит 2.3: Ліве зовнішнє з'єднання (LEFT JOIN авторів без створених моделей з перевіркою IS NULL)
SELECT s.nickname, m.name AS model_name FROM seller s LEFT JOIN model_3d m ON s.id_seller = m.id_seller WHERE m.id_model IS NULL;

-- Запит 2.4: Праве зовнішнє з'єднання (RIGHT JOIN замовлень та зареєстрованих покупців)
SELECT b.email, c.id_cart, c.total_amount FROM buyer b RIGHT JOIN cart c ON b.id_buyer = c.id_buyer LIMIT 5;

-- Запит 2.5: Декартовий добуток (CROSS JOIN категорій та ліцензій)
SELECT c.name AS category, l.license_name AS license FROM category c CROSS JOIN license l LIMIT 5;

