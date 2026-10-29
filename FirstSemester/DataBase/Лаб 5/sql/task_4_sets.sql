-- Завдання 4. Реалізація теоретико-множинних операцій реляційної алгебри (UNION, INTERSECT, EXCEPT)
USE marketplace_3d;

-- Запит 4.1: Об'єднання унікальних значень UNION (контакти користувачів системи)
SELECT nickname AS user_contact FROM seller
UNION
SELECT email AS user_contact FROM buyer
LIMIT 5;

-- Запит 4.2: Об'єднання всіх записів UNION ALL зі збереженням дублікатів
SELECT nickname AS user_contact FROM seller
UNION ALL
SELECT email AS user_contact FROM buyer
LIMIT 5;

-- Запит 4.3: Перетин множин INTERSECT (покупці, які одночасно залишали відгуки на маркетплейсі)
SELECT id_buyer AS common_id FROM cart
INTERSECT
SELECT id_buyer FROM review;

-- Запит 4.4: Різниця множин EXCEPT (покупці, які зареєстровані, але ще не здійснювали замовлень)
SELECT id_buyer AS registered_only FROM buyer
EXCEPT
SELECT id_buyer FROM cart;

-- Запит 4.5: Комбінована операція UNION з фільтрацією та сортуванням результатів
SELECT name, price FROM model_3d WHERE price > 60
UNION
SELECT name, price FROM model_3d WHERE id_category = 1
ORDER BY price DESC
LIMIT 5;

