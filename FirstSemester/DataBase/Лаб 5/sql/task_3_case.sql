-- Завдання 3. Створення запитів з використанням функції CASE (з агрегатними функціями та без них)
USE marketplace_3d;

-- Запит 3.1: Простий оператор CASE без агрегації (перетворення ознаки наявності текстур)
SELECT name, has_texture,
    CASE has_texture 
        WHEN 'Yes' THEN 'Текстурована' 
        ELSE 'Базова' 
    END AS texture_status 
FROM model_3d 
LIMIT 5;

-- Запит 3.2: Пошуковий оператор CASE (класифікація моделей за кількістю полігонів Low/Mid/High-Poly)
SELECT name, polygon_count,
    CASE 
        WHEN polygon_count < 20000 
            THEN 'Low-Poly'
        WHEN polygon_count <= 80000 
            THEN 'Mid-Poly'
        ELSE 'High-Poly'
    END AS poly_grade 
FROM model_3d 
LIMIT 5;

-- Запит 3.3: Використання CASE в агрегатній функції SUM (підрахунок кількості замовлень за статусами)
SELECT id_buyer,
    SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS done_cnt,
    SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) AS active_cnt
FROM cart 
GROUP BY id_buyer 
LIMIT 5;

-- Запит 3.4: Умовне обчислення цін зі знижкою 15% для преміум-моделей
SELECT name, price,
    CASE 
        WHEN price > 60 
            THEN ROUND(price * 0.85, 2)
        ELSE price 
    END AS sale_price 
FROM model_3d 
LIMIT 5;

-- Запит 3.5: Класифікація покупців за статусом лояльності та датою реєстрації
SELECT email,
    CASE 
        WHEN registration_date < '2024-01-01' 
            THEN 'VIP Клієнт'
        ELSE 'Новий'
    END AS client_status 
FROM buyer 
LIMIT 5;

