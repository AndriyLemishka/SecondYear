-- Завдання 1. Написання різних типів підзапитів (корелюючі та некорелюючі)
USE marketplace_3d;

-- Запит 1.1: Скалярний некорелюючий підзапит у SELECT (різниця цін моделі та середньої ціни каталогу)
SELECT name, price, (SELECT AVG(price) FROM model_3d) AS avg_price FROM model_3d LIMIT 5;

-- Запит 1.2: Некорелюючий підзапит у WHERE з оператором порівняння (моделі дорожчі за середню ціну)
SELECT name, price FROM model_3d WHERE price > (SELECT AVG(price) FROM model_3d) LIMIT 5;

-- Запит 1.3: Некорелюючий підзапит з оператором IN (моделі авторів з високим рейтингом >= 4.70)
SELECT name, price FROM model_3d WHERE id_seller IN (SELECT id_seller FROM seller WHERE rating >= 4.70) LIMIT 5;

-- Запит 1.4: Корелюючий підзапит з оператором EXISTS (покупці, що мають хоча б одне замовлення)
SELECT email FROM buyer b WHERE EXISTS (SELECT 1 FROM cart c WHERE c.id_buyer = b.id_buyer) LIMIT 5;

-- Запит 1.5: Підзапит у виразі обчислення цін для автора з найвищим рейтингом
SELECT name, price, ROUND(price * 1.10, 2) AS new_price FROM model_3d WHERE id_seller = (SELECT id_seller FROM seller ORDER BY rating DESC LIMIT 1) LIMIT 5;

