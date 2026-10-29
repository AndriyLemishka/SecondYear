import os
import json
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

base_dir = r"Лаб 5"
cache_dir = os.path.join(base_dir, "cache")
logo_path = os.path.join(cache_dir, "logo_lp.png")
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР5.docx")

doc = docx.Document()

# Margins: 2 cm top/bottom, 2.5 cm left, 1.5 cm right
for s in doc.sections:
    s.top_margin = Cm(2)
    s.bottom_margin = Cm(2)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(1.5)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(14)
font.color.rgb = RGBColor(0, 0, 0)

def add_p(text="", bold=False, italic=False, align='JUSTIFY', space_after=Pt(4), space_before=Pt(0), indent=Cm(1.25), size=Pt(14)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = space_before
    p.paragraph_format.space_after = space_after
    p.paragraph_format.line_spacing = 1.15
    if align == 'CENTER':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.first_line_indent = 0
    elif align == 'RIGHT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        p.paragraph_format.first_line_indent = 0
    elif align == 'LEFT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        p.paragraph_format.first_line_indent = indent
    else:
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.first_line_indent = indent
        
    if text:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Times New Roman'
        run.font.size = size
    return p

def add_code(text):
    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = 0
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(20, 20, 80)
    return p

def add_fig(img_path, caption, width=Inches(6.2)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11.5)
        run_cap.italic = True

# ==========================================
# 1. ТИТУЛЬНИЙ ЛИСТ
# ==========================================
add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align='CENTER', size=Pt(13))
add_p("Національний університет “Львівська політехніка”", align='CENTER', size=Pt(13))
add_p("Інститут комп'ютерних наук та інформаційних технологій", align='CENTER', size=Pt(13))
add_p("Кафедра систем автоматизованого проектування", align='CENTER', space_after=Pt(16), size=Pt(13))

if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p_logo.paragraph_format.first_line_indent = 0
    p_logo.paragraph_format.space_before = Pt(4)
    p_logo.paragraph_format.space_after = Pt(16)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.8))

add_p("Звіт", bold=True, align='CENTER', size=Pt(18))
add_p("до лабораторної роботи № 5", align='CENTER', size=Pt(15))
add_p("з курсу", align='CENTER', size=Pt(13))
add_p("«Організація баз даних та знань»", bold=True, align='CENTER', size=Pt(15))
add_p("на тему: “Написання запитів SELECT. Ч. 2”", bold=True, align='CENTER', space_after=Pt(40), size=Pt(14))

p_exec = doc.add_paragraph()
p_exec.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
p_exec.paragraph_format.left_indent = Cm(9.5)
p_exec.paragraph_format.first_line_indent = 0
p_exec.paragraph_format.line_spacing = 1.25
r_exec = p_exec.add_run("Виконав:\nстудент гр. ПП-24\nЛемішка А.А.\n\nПрийняла:\nСпас Н.Я.")
r_exec.font.name = 'Times New Roman'
r_exec.font.size = Pt(14)

add_p("ЛЬВІВ – 2026", align='CENTER', space_before=Pt(50), space_after=Pt(12), indent=0)
doc.add_page_break()

# ==========================================
# 2. МЕТА ТА ХІД РОБОТИ
# ==========================================
add_p("Мета роботи: навчитися писати підзапити (корелюючі та некорелюючі), використовувати оператори об'єднання таблиць INNER JOIN та OUTER JOIN, умовний оператор CASE, операції над множинами UNION, INTERSECT, EXCEPT, а також виконувати горизонтальне секціонування таблиць (RANGE, LIST, HASH) у MySQL Workbench для бази даних marketplace_3d.", indent=Cm(1.25))

add_p("Хід роботи", bold=True, align='CENTER', space_before=Pt(8), space_after=Pt(12), indent=0)

# ==========================================
# 3. ЗАВДАННЯ 1: ПІДЗАПИТИ
# ==========================================
add_p("Завдання 1. Підзапити (корелюючі та некорелюючі)", bold=True, align='LEFT', indent=0, space_before=Pt(6))

# 1.1
add_p("Запит 1.1. Вибірка моделей з відхиленням ціни від середньої по каталогу (скалярний підзапит):", indent=0)
add_code("""SELECT id_model, name, price,
       ROUND((SELECT AVG(price) FROM model_3d), 2) AS avg_catalog_price,
       ROUND(price - (SELECT AVG(price) FROM model_3d), 2) AS price_diff
FROM model_3d
ORDER BY price_diff DESC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_1_1.png"), "Рис. 1.1. Результат виконання запиту 1.1")

# 1.2
add_p("Запит 1.2. Вибірка моделей авторів з рейтингом від 4.70 (підзапит з IN):", indent=0)
add_code("""SELECT id_model, name, price, id_seller
FROM model_3d
WHERE id_seller IN (
    SELECT id_seller
    FROM seller
    WHERE rating >= 4.70
)
ORDER BY price DESC;""")
add_fig(os.path.join(cache_dir, "shot_1_2.png"), "Рис. 1.2. Результат виконання запиту 1.2")

# 1.3
add_p("Запит 1.3. Моделі, які дорожчі за середню ціну своєї категорії (корелюючий підзапит):", indent=0)
add_code("""SELECT m1.id_model, m1.name, m1.id_category, m1.price
FROM model_3d m1
WHERE m1.price > (
    SELECT AVG(m2.price)
    FROM model_3d m2
    WHERE m2.id_category = m1.id_category
)
ORDER BY m1.id_category, m1.price DESC;""")
add_fig(os.path.join(cache_dir, "shot_1_3.png"), "Рис. 1.3. Результат виконання запиту 1.3")

# 1.4
add_p("Запит 1.4. Пошук зареєстрованих покупців без замовлень (корелюючий підзапит NOT EXISTS):", indent=0)
add_code("""SELECT b.id_buyer, b.email, b.registration_date
FROM buyer b
WHERE NOT EXISTS (
    SELECT 1
    FROM cart c
    WHERE c.id_buyer = b.id_buyer
);""")
add_fig(os.path.join(cache_dir, "shot_1_4.png"), "Рис. 1.4. Результат виконання запиту 1.4")

# 1.5
add_p("Запит 1.5. Оновлення total_amount кошика через підзапит суми та вибірка результату:", indent=0)
add_code("""UPDATE cart
SET total_amount = (SELECT COALESCE(SUM(ci.fixed_price), 0.0)
                    FROM cart_item ci WHERE ci.id_cart = cart.id_cart);

SELECT c.id_cart, c.id_buyer, c.status, c.total_amount,
       (SELECT COUNT(*) FROM cart_item ci WHERE ci.id_cart = c.id_cart) AS items_count
FROM cart c
ORDER BY c.id_cart
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_1_5.png"), "Рис. 1.5. Результат виконання запиту 1.5")

# ==========================================
# 4. ЗАВДАННЯ 2: INNER ТА OUTER JOIN
# ==========================================
add_p("Завдання 2. Оператори INNER JOIN та OUTER JOIN", bold=True, align='LEFT', indent=0, space_before=Pt(10))

# 2.1
add_p("Запит 2.1. Внутрішнє з'єднання моделей та їхніх категорій (INNER JOIN):", indent=0)
add_code("""SELECT m.id_model, m.name AS model_name, c.name AS category_name, m.price, m.polygon_count
FROM model_3d m
INNER JOIN category c ON m.id_category = c.id_category
ORDER BY c.name, m.price DESC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_2_1.png"), "Рис. 2.1. Результат виконання запиту 2.1")

# 2.2
add_p("Запит 2.2. З'єднання 4 таблиць: модель, продавець, категорія та ліцензія:", indent=0)
add_code("""SELECT m.name AS model_name, s.nickname AS author, c.name AS category,
       l.license_name, l.usage_type, m.price
FROM model_3d m
INNER JOIN seller s ON m.id_seller = s.id_seller
INNER JOIN category c ON m.id_category = c.id_category
INNER JOIN license l ON m.id_license = l.id_license
ORDER BY m.price DESC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_2_2.png"), "Рис. 2.2. Результат виконання запиту 2.2")

# 2.3
add_p("Запит 2.3. Ліве з'єднання покупців та їх кошиків із відображенням NULL (LEFT JOIN):", indent=0)
add_code("""SELECT b.id_buyer, b.email, b.registration_date,
       c.id_cart, c.status AS cart_status, c.total_amount
FROM buyer b
LEFT JOIN cart c ON b.id_buyer = c.id_buyer
ORDER BY b.id_buyer, c.id_cart
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_2_3.png"), "Рис. 2.3. Результат виконання запиту 2.3")

# 2.4
add_p("Запит 2.4. Праве з'єднання категорій та моделей (RIGHT JOIN):", indent=0)
add_code("""SELECT c.id_category, c.name AS category_name,
       m.id_model, m.name AS model_name, m.price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
ORDER BY c.id_category, m.id_model
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_2_4.png"), "Рис. 2.4. Результат виконання запиту 2.4")

# 2.5
add_p("Запит 2.5. Декартовий добуток комерційних ліцензій та рубрик (CROSS JOIN):", indent=0)
add_code("""SELECT c.name AS category_name, l.license_name, l.usage_type,
       COUNT(m.id_model) AS models_count
FROM category c
CROSS JOIN license l
LEFT JOIN model_3d m ON m.id_category = c.id_category AND m.id_license = l.id_license
WHERE l.usage_type = 'Commercial'
GROUP BY c.name, l.license_name, l.usage_type
ORDER BY c.name, l.license_name
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_2_5.png"), "Рис. 2.5. Результат виконання запиту 2.5")

# ==========================================
# 5. ЗАВДАННЯ 3: ОПЕРАТОР CASE
# ==========================================
add_p("Завдання 3. Оператор CASE (з агрегатними функціями та без них)", bold=True, align='LEFT', indent=0, space_before=Pt(10))

# 3.1
add_p("Запит 3.1. Класифікація складності сітки моделей (Low-Poly, Mid-Poly, High-Poly):", indent=0)
add_code("""SELECT id_model, name, polygon_count,
       CASE
           WHEN polygon_count < 15000 THEN 'Low-Poly'
           WHEN polygon_count BETWEEN 15000 AND 50000 THEN 'Mid-Poly'
           ELSE 'High-Poly'
       END AS complexity_tier
FROM model_3d
ORDER BY polygon_count ASC
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_3_1.png"), "Рис. 3.1. Результат виконання запиту 3.1")

# 3.2
add_p("Запит 3.2. Розподіл моделей за ціновими категоріями (Budget, Standard, Premium):", indent=0)
add_code("""SELECT id_model, name, price,
       CASE
           WHEN price < 30.00 THEN 'Budget (< $30)'
           WHEN price BETWEEN 30.00 AND 70.00 THEN 'Standard ($30-$70)'
           ELSE 'Premium (> $70)'
       END AS price_category
FROM model_3d
ORDER BY price DESC
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_3_2.png"), "Рис. 3.2. Результат виконання запиту 3.2")

# 3.3
add_p("Запит 3.3. Підрахунок моделей з текстурами та без них за рубриками (CASE в агрегації):", indent=0)
add_code("""SELECT c.name AS category_name,
       COUNT(m.id_model) AS total_models,
       SUM(CASE WHEN m.has_texture = 'Yes' THEN 1 ELSE 0 END) AS textured_count,
       SUM(CASE WHEN m.has_texture = 'No' THEN 1 ELSE 0 END) AS untextured_count,
       ROUND(AVG(CASE WHEN m.has_texture = 'Yes' THEN m.price ELSE NULL END), 2) AS avg_textured_price
FROM category c
LEFT JOIN model_3d m ON c.id_category = m.id_category
GROUP BY c.id_category, c.name
ORDER BY total_models DESC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_3_3.png"), "Рис. 3.3. Результат виконання запиту 3.3")

# 3.4
add_p("Запит 3.4. Розрахунок знижки та акційної ціни залежно від рейтингу автора:", indent=0)
add_code("""SELECT m.name AS model_name, s.nickname, s.rating, m.price AS original_price,
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
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_3_4.png"), "Рис. 3.4. Результат виконання запиту 3.4")

# 3.5
add_p("Запит 3.5. Визначення рівня лояльності покупця за загальною сумою покупок:", indent=0)
add_code("""SELECT b.id_buyer, b.email,
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
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_3_5.png"), "Рис. 3.5. Результат виконання запиту 3.5")

# ==========================================
# 6. ЗАВДАННЯ 4: ОПЕРАЦІЇ НАД МНОЖИНАМИ
# ==========================================
add_p("Завдання 4. Операції реляційної алгебри (UNION, INTERSECT, EXCEPT)", bold=True, align='LEFT', indent=0, space_before=Pt(10))

# 4.1
add_p("Запит 4.1. Об'єднання списку продавців та покупців без повторень (UNION):", indent=0)
add_code("""SELECT id_seller AS user_id, nickname AS identifier, 'Seller' AS role
FROM seller
WHERE rating >= 4.6
UNION
SELECT id_buyer AS user_id, email AS identifier, 'Buyer' AS role
FROM buyer
WHERE registration_date >= '2025-03-01'
ORDER BY role, user_id
LIMIT 8;""")
add_fig(os.path.join(cache_dir, "shot_4_1.png"), "Рис. 4.1. Результат виконання запиту 4.1")

# 4.2
add_p("Запит 4.2. Об'єднання замовлень та відгуків із збереженням усіх записів (UNION ALL):", indent=0)
add_code("""SELECT id_buyer, 'Cart Order' AS activity_type, created_date AS action_date, total_amount AS val
FROM cart
UNION ALL
SELECT r.id_buyer, 'Model Review' AS activity_type, '2025-06-01' AS action_date, r.rating * 10.0 AS val
FROM review r
ORDER BY id_buyer, action_date
LIMIT 8;""")
add_fig(os.path.join(cache_dir, "shot_4_2.png"), "Рис. 4.2. Результат виконання запиту 4.2")

# 4.3
add_p("Запит 4.3. Клієнти, які мають замовлення та одночасно залишили відгук (INTERSECT):", indent=0)
add_code("""SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM cart)
INTERSECT
SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM review)
ORDER BY id_buyer
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_4_3.png"), "Рис. 4.3. Результат виконання запиту 4.3")

# 4.4
add_p("Запит 4.4. Зареєстровані клієнти, які ще не зробили жодного замовлення (EXCEPT):", indent=0)
add_code("""SELECT id_buyer, email FROM buyer
EXCEPT
SELECT id_buyer, email FROM buyer
WHERE id_buyer IN (SELECT id_buyer FROM cart)
ORDER BY id_buyer;""")
add_fig(os.path.join(cache_dir, "shot_4_4.png"), "Рис. 4.4. Результат виконання запиту 4.4")

# 4.5
add_p("Запит 4.5. Формати файлів, що є тільки у High-Poly моделях (EXCEPT):", indent=0)
add_code("""SELECT DISTINCT f.format
FROM model_file f
JOIN model_3d m ON f.id_model = m.id_model
WHERE m.polygon_count > 30000
EXCEPT
SELECT DISTINCT f.format
FROM model_file f
JOIN model_3d m ON f.id_model = m.id_model
WHERE m.polygon_count < 10000;""")
add_fig(os.path.join(cache_dir, "shot_4_5.png"), "Рис. 4.5. Результат виконання запиту 4.5")

# ==========================================
# 7. ЗАВДАННЯ 5: СЕКЦІОНУВАННЯ
# ==========================================
add_p("Завдання 5. Розділення таблиць (RANGE, LIST, HASH)", bold=True, align='LEFT', indent=0, space_before=Pt(10))

# 5.1
add_p("Запит 5.1. Розділення замовлень cart_range за роками (RANGE) та вибірка з секції p_2025:", indent=0)
add_code("""SELECT id_cart, id_buyer, status, total_amount, created_date
FROM cart_range
PARTITION (p_2025)
ORDER BY created_date ASC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_5_1.png"), "Рис. 5.1. Вибірка з секції p_2025 (RANGE)")

# 5.2
add_p("Запит 5.2. Розділення моделей model_list за рубриками (LIST) та вибірка з секції рубрик 1 і 2:", indent=0)
add_code("""SELECT id_model, name, id_category, price, polygon_count
FROM model_list
PARTITION (p_characters_vehicles)
ORDER BY price DESC
LIMIT 6;""")
add_fig(os.path.join(cache_dir, "shot_5_2.png"), "Рис. 5.2. Вибірка з секції p_characters_vehicles (LIST)")

# 5.3
add_p("Запит 5.3. Розділення покупців buyer_hash за хешем ID на 4 секції (HASH):", indent=0)
add_code("""SELECT id_buyer, email, registration_date
FROM buyer_hash
PARTITION (p1)
ORDER BY id_buyer ASC;""")
add_fig(os.path.join(cache_dir, "shot_5_3.png"), "Рис. 5.3. Вибірка з секції p1 (HASH)")

# 5.4
add_p("Запит 5.4. Перевірка кількості рядків по секціях у information_schema.partitions:", indent=0)
add_code("""SELECT table_name, partition_name, table_rows, partition_method
FROM information_schema.partitions
WHERE table_name IN ('cart_range', 'model_list', 'buyer_hash')
LIMIT 7;""")
add_fig(os.path.join(cache_dir, "shot_5_4.png"), "Рис. 5.4. Результат запиту до information_schema.partitions")

# ==========================================
# 8. КОНТРОЛЬНІ ЗАПИТАННЯ (КОРОТКО, ЯК У ЛАБ 4)
# ==========================================
doc.add_page_break()
add_p("Контрольні запитання", bold=True, align='CENTER', size=Pt(15), space_after=Pt(10), indent=0)

qa_simple = [
    (
        "1. За допомогою яких операторів формують підзапити в SELECT?",
        "Підзапити формують за допомогою звичайних операторів порівняння (=, <>, <, >), операторів IN, NOT IN, ANY, ALL, а також EXISTS та NOT EXISTS. Підзапит записують у круглих дужках."
    ),
    (
        "2. Назвіть оператори для отримання набору значень.",
        "Для роботи зі списком значень використовують оператори IN (належить списку), NOT IN (не належить), ANY / SOME (підходить хоча б одне значення) та ALL (підходять усі значення зі списку)."
    ),
    (
        "3. Які функції підзапитів у командах UPDATE, INSERT, DELETE?",
        "• В INSERT: вставляти готові дані з іншої таблиці (INSERT INTO ... SELECT) або підставляти ID у VALUES через підзапит.\n"
        "• В UPDATE: рахувати нові значення полів у SET (наприклад, суму замовлення) або фільтрувати рядки для зміни у WHERE.\n"
        "• В DELETE: знаходити у WHERE непотрібні рядки за даними інших таблиць і видаляти їх."
    ),
    (
        "4. Для чого використовують оператор CASE?",
        "Для перевірки умов усередині запиту (аналог IF-THEN-ELSE). З ним можна розбивати дані на категорії (Low-Poly / High-Poly), рахувати персональні знижки та робити умовний підрахунок усередині SUM() чи COUNT()."
    ),
    (
        "5. Які оператори використовують для з’єднання таблиць?",
        "• INNER JOIN — повертає тільки ті рядки, які є в обох таблицях;\n"
        "• LEFT JOIN — бере всі рядки з лівої таблиці, а якщо в правій немає пари, ставить NULL;\n"
        "• RIGHT JOIN — бере всі рядки з правої таблиці;\n"
        "• CROSS JOIN — декартовий добуток (кожен рядок з кожним)."
    ),
    (
        "6. Які запити виконують за допомогою операторів UNION, INTERSET, EXEPT?",
        "• UNION — об'єднує результати двох запитів і прибирає однакові дублікати;\n"
        "• UNION ALL — об'єднує результати і залишає всі дублікати (працює швидше);\n"
        "• INTERSECT — залишає тільки ті рядки, які є і в першому, і в другому запиті (перетин);\n"
        "• EXCEPT — віднімає від першого запиту рядки другого запиту (різниця)."
    ),
    (
        "7. Запишіть запит на декартовий добуток відношень A та B.",
        "SELECT * FROM name_table_A CROSS JOIN name_table_B;\nабо просто: SELECT * FROM name_table_A, name_table_B;"
    ),
    (
        "8. Які типи розділення таблиці на частини пропонує MySQL?",
        "MySQL підтримує розбиття: RANGE (за числовими діапазонами), LIST (за списками значень), HASH (за залишком від ділення), KEY (внутрішній хеш MySQL) та COLUMNS (розбиття за датами чи рядками)."
    ),
    (
        "9. Охарактеризуйте тип розбиття таблиці RANGE.",
        "Таблиця розбивається на діапазони значень через VALUES LESS THAN (межа). Підходить для дат чи років: кожна секція зберігає дані за свій період, а застарілі роки легко видаляти окремою секцією."
    ),
    (
        "10. Охарактеризуйте тип розбиття таблиці LIST.",
        "Рядки потрапляють у секцію, якщо їхнє значення збігається з переліком через VALUES IN (...). Зручно розбивати дані за категоріями товарів, статусами або регіонами."
    ),
    (
        "11. Охарактеризуйте тип розбиття таблиці HASH.",
        "Рядки діляться рівномірно між заданою кількістю секцій (PARTITIONS N) за формулою MOD(id, N). Використовується, коли немає чіткого діапазону дат, але треба розвантажити диск і порівну поділити записи."
    )
]

for q_title, q_ans in qa_simple:
    add_p(q_title, bold=True, align='LEFT', space_before=Pt(6), space_after=Pt(2), indent=0)
    for line in q_ans.split("\n"):
        if line.strip():
            add_p(line.strip(), align='JUSTIFY', space_before=Pt(0), space_after=Pt(2), indent=Cm(0.6))

# ==========================================
# 9. ВИСНОВКИ (КОРОТКО, ЯК У ЛАБ 4)
# ==========================================
doc.add_page_break()
add_p("Висновки", bold=True, align='CENTER', size=Pt(15), space_after=Pt(10), indent=0)

add_p("Під час виконання лабораторної роботи № 5 було вивчено роботу зі складними запитами SELECT та секціонуванням у СУБД MySQL для бази даних marketplace_3d. На практиці написано та протестовано корелюючі й некорелюючі підзапити, оператори внутрішнього та зовнішнього з'єднання (INNER JOIN, LEFT/RIGHT/CROSS JOIN), умовний оператор CASE з агрегацією, операції над множинами (UNION, UNION ALL, INTERSECT, EXCEPT), а також виконано горизонтальне секціонування таблиць за RANGE, LIST та HASH. Усі запити перевірено у середовищі MySQL Workbench.", indent=Cm(1.25))

doc.save(target_docx)
print("Simplified docx generated successfully!")
