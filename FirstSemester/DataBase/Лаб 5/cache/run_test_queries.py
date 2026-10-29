import sqlite3
import json
import os

db_path = r"Лаб 5\cache\marketplace_3d.db"
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

queries = {
    # Завдання 1
    "1.1": """
SELECT id_model, name, price,
       ROUND((SELECT AVG(price) FROM model_3d), 2) AS avg_catalog_price,
       ROUND(price - (SELECT AVG(price) FROM model_3d), 2) AS price_diff
FROM model_3d
ORDER BY price_diff DESC
LIMIT 6;
    """,
    "1.2": """
SELECT id_model, name, price, id_seller
FROM model_3d
WHERE id_seller IN (
    SELECT id_seller
    FROM seller
    WHERE rating >= 4.70
)
ORDER BY price DESC;
    """,
    "1.3": """
SELECT m1.id_model, m1.name, m1.id_category, m1.price
FROM model_3d m1
WHERE m1.price > (
    SELECT AVG(m2.price)
    FROM model_3d m2
    WHERE m2.id_category = m1.id_category
)
ORDER BY m1.id_category, m1.price DESC;
    """,
    "1.4": """
SELECT b.id_buyer, b.email, b.registration_date
FROM buyer b
WHERE NOT EXISTS (
    SELECT 1
    FROM cart c
    WHERE c.id_buyer = b.id_buyer
);
    """,
    "1.5": """
SELECT c.id_cart, c.id_buyer, c.status, c.total_amount,
       (SELECT COUNT(*) FROM cart_item ci WHERE ci.id_cart = c.id_cart) AS items_count
FROM cart c
ORDER BY c.id_cart
LIMIT 6;
    """,

    # Завдання 2
    "2.1": """
SELECT m.id_model, m.name AS model_name, c.name AS category_name, m.price, m.polygon_count
FROM model_3d m
INNER JOIN category c ON m.id_category = c.id_category
ORDER BY c.name, m.price DESC
LIMIT 6;
    """,
    "2.2": """
SELECT m.name AS model_name,
       s.nickname AS author,
       c.name AS category,
       l.license_name,
       l.usage_type,
       m.price
FROM model_3d m
INNER JOIN seller s ON m.id_seller = s.id_seller
INNER JOIN category c ON m.id_category = c.id_category
INNER JOIN license l ON m.id_license = l.id_license
ORDER BY m.price DESC
LIMIT 6;
    """,
    "2.3": """
SELECT b.id_buyer, b.email, b.registration_date,
       c.id_cart, c.status AS cart_status, c.total_amount
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer
ORDER BY b.id_buyer, c.id_cart
LIMIT 7;
    """,
    "2.4": """
SELECT c.id_category, c.name AS category_name,
       m.id_model, m.name AS model_name, m.price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
ORDER BY c.id_category, m.id_model
LIMIT 7;
    """,
    "2.5": """
SELECT c.name AS category_name,
       l.license_name,
       l.usage_type,
       COUNT(m.id_model) AS models_count
FROM category c
CROSS JOIN license l
LEFT JOIN model_3d m ON m.id_category = c.id_category AND m.id_license = l.id_license
WHERE l.usage_type = 'Commercial'
GROUP BY c.name, l.license_name, l.usage_type
ORDER BY c.name, l.license_name
LIMIT 7;
    """,

    # Завдання 3
    "3.1": """
SELECT id_model, name, polygon_count,
       CASE
           WHEN polygon_count < 15000 THEN 'Low-Poly'
           WHEN polygon_count BETWEEN 15000 AND 50000 THEN 'Mid-Poly'
           ELSE 'High-Poly'
       END AS complexity_tier
FROM model_3d
ORDER BY polygon_count ASC
LIMIT 7;
    """,
    "3.2": """
SELECT id_model, name, price,
       CASE
           WHEN price < 30.00 THEN 'Budget (< $30)'
           WHEN price BETWEEN 30.00 AND 70.00 THEN 'Standard ($30-$70)'
           ELSE 'Premium (> $70)'
       END AS price_category
FROM model_3d
ORDER BY price DESC
LIMIT 7;
    """,
    "3.3": """
SELECT c.name AS category_name,
       COUNT(m.id_model) AS total_models,
       SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS textured_count,
       SUM(CASE WHEN m.has_texture = 'No' THEN 1 ELSE 0 END) AS untextured_count,
       ROUND(AVG(CASE WHEN m.has_texture = 'Yes' THEN m.price ELSE NULL END), 2) AS avg_textured_price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
GROUP BY c.id_category, c.name
ORDER BY total_models DESC
LIMIT 6;
    """,
    "3.4": """
SELECT m.name AS model_name, s.nickname, s.rating, m.price AS original_price,
       CASE
           WHEN s.rating >= 4.8 THEN 15
           WHEN s.rating >= 4.5 THEN 10
           WHEN s.rating >= 4.0 THEN 5
           ELSE 0
       END AS discount_pct,
       ROUND(m.price * (1.0 - (CASE
           WHEN s.rating >= 4.8 THEN 15
           WHEN s.rating >= 4.5 THEN 10
           WHEN s.rating >= 4.0 THEN 5
           ELSE 0
       END) / 100.0), 2) AS discounted_price
FROM model_3d m
INNER JOIN seller s ON m.id_seller = s.id_seller
ORDER BY s.rating DESC, m.price DESC
LIMIT 6;
    """,
    "3.5": """
SELECT b.id_buyer, b.email,
       COUNT(c.id_cart) AS total_orders,
       COALESCE(SUM(c.total_amount), 0.0) AS total_spent,
       CASE
           WHEN SUM(c.total_amount) >= 150.00 THEN 'VIP Buyer'
           WHEN SUM(c.total_amount) >= 50.00 THEN 'Regular Buyer'
           WHEN COUNT(c.id_cart) > 0 THEN 'New Buyer'
           ELSE 'Inactive'
       END AS customer_tier
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer
GROUP BY b.id_buyer, b.email
ORDER BY total_spent DESC
LIMIT 7;
    """,

    # Завдання 4
    "4.1": """
SELECT id_seller AS user_id, nickname AS identifier, 'Seller' AS role
FROM seller
WHERE rating >= 4.6
UNION
SELECT id_buyer AS user_id, email AS identifier, 'Buyer' AS role
FROM buyer
WHERE registration_date >= '2025-03-01'
ORDER BY role, user_id
LIMIT 8;
    """,
    "4.2": """
SELECT id_buyer, 'Cart Order' AS activity_type, created_date AS action_date, total_amount AS val
FROM cart
UNION ALL
SELECT r.id_buyer, 'Model Review' AS activity_type, '2025-06-01' AS action_date, r.rating * 10.0 AS val
FROM review r
ORDER BY id_buyer, action_date
LIMIT 8;
    """,
    "4.3": """
SELECT id_buyer FROM cart
INTERSECT
SELECT id_buyer FROM review
ORDER BY id_buyer;
    """,
    "4.4": """
SELECT id_buyer FROM cart
EXCEPT
SELECT id_buyer FROM review
ORDER BY id_buyer;
    """,
    "4.5": """
SELECT DISTINCT format FROM model_file
WHERE id_model IN (SELECT id_model FROM model_3d WHERE price > 50)
EXCEPT
SELECT DISTINCT format FROM model_file
WHERE id_model IN (SELECT id_model FROM model_3d WHERE price <= 50);
    """
}

results = {}
for q_id, sql in queries.items():
    try:
        cursor.execute(sql)
        cols = [d[0] for d in cursor.description]
        rows = [dict(r) for r in cursor.fetchall()]
        results[q_id] = {
            "sql": sql.strip(),
            "columns": cols,
            "rows": rows
        }
        print(f"Query {q_id}: {len(rows)} rows, cols: {cols}")
    except Exception as e:
        print(f"Error in {q_id}: {e}")

out_json = r"Лаб 5\cache\query_results.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved query results to JSON")
