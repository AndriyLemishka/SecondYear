import docx
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = docx.Document()
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(14)

def add_paragraph(text, bold=False, align='LEFT', space_after=Pt(0), first_line_indent=Cm(1.25)):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = space_after
    if align == 'CENTER':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.first_line_indent = 0
    elif align == 'RIGHT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        p.paragraph_format.first_line_indent = 0
    elif align == 'JUSTIFY':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.first_line_indent = first_line_indent
    else:
        p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        p.paragraph_format.first_line_indent = first_line_indent
        
    run = p.add_run(text)
    run.bold = bold
    return p

# --- TITLE PAGE ---
add_paragraph("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align='CENTER')
add_paragraph("Національний університет “Львівська політехніка”", align='CENTER')
add_paragraph("Інститут комп'ютерних наук та інформаційних технологій", align='CENTER')
add_paragraph("Кафедра систем автоматизованого проектування", align='CENTER', space_after=Pt(40))

add_paragraph("Звіт", bold=True, align='CENTER')
add_paragraph("до лабораторної роботи № 3", align='CENTER')
add_paragraph("з курсу", align='CENTER')
add_paragraph("«Організація баз даних та знань»", align='CENTER')
add_paragraph("на тему: “Написання SQL-сценаріїв для створення БД”", align='CENTER', space_after=Pt(40))

p_exec = doc.add_paragraph()
p_exec.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
p_exec.paragraph_format.left_indent = Cm(9)
p_exec.paragraph_format.first_line_indent = 0
p_exec.add_run("Виконав:\nстудент гр. ПП-24\nЛемішка А.А.\nПрийняла:\nСпас Н.Я.")

add_paragraph("ЛЬВІВ – 2026", align='CENTER', space_after=Pt(12), first_line_indent=0)
doc.add_page_break()

# --- META ---
p_meta = doc.add_paragraph()
p_meta.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
p_meta.paragraph_format.first_line_indent = Cm(1.25)
p_meta.add_run("Мета: ").bold = True
p_meta.add_run("навчитися створювати базу даних у MySQL Workbench: писати SQL-сценарії створення БД і таблиць, задавати первинні та зовнішні ключі, додаткові обмеження цілісності (CHECK, UNIQUE), наповнювати таблиці тестовими даними та генерувати EER-модель БД.")

# --- TASK 1 ---
add_paragraph("Завдання 1. Створення БД для предметної області «Сайт продажу 3D-моделей (маркетплейс)»", bold=True, align='LEFT')
add_paragraph("Базу даних створено для предметної області «Сайт продажу 3D-моделей (маркетплейс)». БД має назву marketplace_3d і кодування utf8mb4, щоб коректно зберігати текст різними мовами (в тому числі українською). На початку сценарію стоїть DROP DATABASE IF EXISTS: так сценарій можна запускати повторно й щоразу отримувати «чисту» БД (властивість ідемпотентності). Команда USE робить БД активною для подальших операторів.", align='JUSTIFY')
add_paragraph("1.1. Сценарій створення БД marketplace_3d", bold=True, align='LEFT')

sql_db = """DROP DATABASE IF EXISTS marketplace_3d;
CREATE DATABASE IF NOT EXISTS marketplace_3d
CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE marketplace_3d;
SHOW DATABASES LIKE 'marketplace_3d';"""

def add_code(text):
    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    p.paragraph_format.left_indent = Cm(0)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(10)
    return p

add_code(sql_db)

add_paragraph("[Тут розмістити Рис. 1. Сценарій створення БД marketplace_3d та результат його виконання (вкладка Output)]", align='CENTER', first_line_indent=0)
add_paragraph("Результат: БД marketplace_3d створено, вона з’явилась у списку SCHEMAS у навігаторі Workbench.", align='JUSTIFY')

# --- TASK 2 ---
add_paragraph("Завдання 2. Створення таблиць БД та визначення ключових полів", bold=True, align='LEFT')
add_paragraph("Таблиці створено відповідно до фізичної моделі, побудованої в DbDesigner у лабораторній роботі № 2. Первинний ключ кожної таблиці — цілочисельне поле з атрибутом AUTO_INCREMENT. Зв’язки між таблицями задано обмеженнями FOREIGN KEY ... REFERENCES. Таблиці створюються в такому порядку: від батьківських до дочірніх, щоб таблиця, на яку посилається зовнішній ключ, на момент створення вже існувала.", align='JUSTIFY')
add_paragraph("Окремим блоком через ALTER TABLE ADD CONSTRAINT додано додаткові обмеження цілісності: CHECK для перевірки, що price > 0, polygon_count > 0, size_mb > 0, а rating знаходиться в межах від 1 до 5; також додано UNIQUE для унікальності email та nickname.", align='JUSTIFY')

add_paragraph("2.1. Сценарій створення таблиць та ключів", bold=True, align='LEFT')

sql_tables = """CREATE TABLE seller (
    id_seller INT AUTO_INCREMENT,
    nickname VARCHAR(50) NOT NULL,
    rating DECIMAL(3,2) NOT NULL,
    PRIMARY KEY (id_seller)
);

CREATE TABLE buyer (
    id_buyer INT AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    PRIMARY KEY (id_buyer)
);

CREATE TABLE category (
    id_category INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_category)
);

CREATE TABLE license (
    id_license INT AUTO_INCREMENT,
    id_change INT NOT NULL,
    license_name VARCHAR(100) NOT NULL,
    usage_type VARCHAR(50) NOT NULL,
    allow_modification VARCHAR(10) NOT NULL,
    creation_date DATE NOT NULL,
    creation_time TIME NOT NULL,
    PRIMARY KEY (id_license)
);

CREATE TABLE model_3d (
    id_model INT AUTO_INCREMENT,
    id_seller INT,
    id_category INT,
    id_license INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    polygon_count INT NOT NULL,
    has_texture VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_model),
    FOREIGN KEY (id_seller) REFERENCES seller(id_seller),
    FOREIGN KEY (id_category) REFERENCES category(id_category),
    FOREIGN KEY (id_license) REFERENCES license(id_license)
);

CREATE TABLE model_file (
    id_file INT AUTO_INCREMENT,
    id_model INT,
    format VARCHAR(20) NOT NULL,
    size_mb DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (id_file),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

CREATE TABLE cart (
    id_cart INT AUTO_INCREMENT,
    id_buyer INT,
    status VARCHAR(30) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    created_date DATE NOT NULL,
    PRIMARY KEY (id_cart),
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);

CREATE TABLE cart_item (
    id_item INT AUTO_INCREMENT,
    id_cart INT,
    id_model INT,
    fixed_price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_item),
    FOREIGN KEY (id_cart) REFERENCES cart(id_cart),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

CREATE TABLE review (
    id_review INT AUTO_INCREMENT,
    id_model INT,
    id_buyer INT,
    rating INT NOT NULL,
    comment_text TEXT,
    PRIMARY KEY (id_review),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model),
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);

-- Додавання обмежень
ALTER TABLE seller 
    ADD CONSTRAINT uq_seller_nickname UNIQUE (nickname),
    ADD CONSTRAINT chk_seller_rating CHECK (rating BETWEEN 1 AND 5);

ALTER TABLE buyer 
    ADD CONSTRAINT uq_buyer_email UNIQUE (email);

ALTER TABLE category 
    ADD CONSTRAINT uq_category_name UNIQUE (name);

ALTER TABLE model_3d 
    ADD CONSTRAINT chk_model_price CHECK (price > 0),
    ADD CONSTRAINT chk_model_polygons CHECK (polygon_count > 0);

ALTER TABLE model_file 
    ADD CONSTRAINT chk_file_size CHECK (size_mb > 0);

ALTER TABLE review 
    ADD CONSTRAINT chk_review_rating CHECK (rating BETWEEN 1 AND 5);

SHOW TABLES;
DESCRIBE model_3d;"""

add_code(sql_tables)

add_paragraph("[Тут розмістити Рис. 2. Сценарій створення таблиць і результат виконання (SHOW TABLES, DESCRIBE model_3d)]", align='CENTER', first_line_indent=0)
add_paragraph("Результат: створено 9 таблиць. У DESCRIBE model_3d видно первинний ключ id_model (PRI) та поля зовнішніх ключів (MUL — для них автоматично створено індекси).", align='JUSTIFY')

# --- TASK 3 ---
add_paragraph("Завдання 3. Наповнення таблиць БД даними", bold=True, align='LEFT')
add_paragraph("Таблиці наповнено багаторядковими операторами INSERT INTO ... VALUES. Спочатку заповнюються довідкові таблиці (seller, buyer, category, license), потім підпорядковані таблиці, які посилаються на них (model_3d, cart), і далі — залежні від них (model_file, cart_item, review). Інакше спрацює обмеження зовнішнього ключа. У кожній таблиці міститься від 10 до 13 записів.", align='JUSTIFY')
add_paragraph("Частину даних навмисно підібрано під запити наступних лабораторних робіт: існують моделі без жодного відгуку, а також покупці зі створеними, але пустими або активними кошиками, щоб можна було перевіряти оператори LEFT JOIN, умови IS NULL та NOT EXISTS.", align='JUSTIFY')
add_paragraph("3.1. Сценарій наповнення таблиць даними", bold=True, align='LEFT')

sql_insert = """-- Наповнення довідкових таблиць
INSERT INTO seller (nickname, rating) VALUES
('3D_Master', 4.8), ('PixelPro', 4.5), ('PolyGenius', 4.9), ('Artisan3D', 4.2), ('MeshCreator', 5.0),
('VoxelKing', 4.1), ('TextureGod', 4.7), ('VertexHero', 4.6), ('RenderBoss', 4.3), ('ModelGuru', 4.4);

INSERT INTO buyer (email, registration_date) VALUES
('user1@mail.com', '2025-01-10'), ('john_d@mail.com', '2025-01-15'), ('sarah_art@mail.com', '2025-02-01'),
('mike99@mail.com', '2025-02-12'), ('gamer_dude@mail.com', '2025-03-05'), ('dev_indie@mail.com', '2025-03-20'),
('studio_x@mail.com', '2025-04-11'), ('render_farm@mail.com', '2025-05-02'), ('vfx_pro@mail.com', '2025-06-18'),
('newbie_3d@mail.com', '2025-07-22'), ('ghost_buyer@mail.com', '2025-08-01'), ('inactive_user@mail.com', '2025-08-15');

INSERT INTO category (name) VALUES
('Characters'), ('Vehicles'), ('Weapons'), ('Environments'), ('Props'),
('Animals'), ('Plants'), ('Architecture'), ('Furniture'), ('Sci-Fi');

INSERT INTO license (id_change, license_name, usage_type, allow_modification, creation_date, creation_time) VALUES
(1, 'Standard License', 'Personal', 'No', '2025-01-01', '10:00:00'),
(2, 'Extended License', 'Commercial', 'Yes', '2025-01-01', '10:05:00'),
(3, 'Free Use', 'Educational', 'Yes', '2025-01-02', '11:30:00'),
(4, 'Editorial', 'Editorial', 'No', '2025-01-03', '09:15:00'),
(5, 'Exclusive Rights', 'Commercial', 'Yes', '2025-01-05', '14:20:00'),
(6, 'Standard Commercial', 'Commercial', 'No', '2025-01-06', '16:45:00'),
(7, 'CC BY 4.0', 'Any', 'Yes', '2025-01-10', '08:00:00'),
(8, 'CC BY-NC 4.0', 'Non-Commercial', 'Yes', '2025-01-12', '12:00:00'),
(9, 'Game Dev License', 'Commercial', 'Yes', '2025-01-15', '15:30:00'),
(10, 'Print Only', 'Personal', 'No', '2025-01-20', '18:10:00');

-- Наповнення підпорядкованих таблиць
INSERT INTO model_3d (id_seller, id_category, id_license, name, description, price, polygon_count, has_texture) VALUES
(1, 1, 2, 'Cyberpunk Character', 'High poly rigged character', 25.00, 150000, 'Yes'),
(2, 2, 2, 'Sports Car', 'Low poly sports car', 15.00, 25000, 'Yes'),
(3, 3, 1, 'Assault Rifle', 'Detailed weapon with textures', 10.00, 8000, 'Yes'),
(4, 4, 3, 'Forest Terrain', 'Large environment map', 0.01, 500000, 'No'),
(5, 5, 2, 'Wooden Barrel', 'Game prop', 5.00, 1200, 'Yes'),
(6, 6, 2, 'Wolf Animation', 'Rigged wolf', 30.00, 45000, 'Yes'),
(7, 7, 7, 'Oak Tree', 'Tree model', 12.00, 15000, 'Yes'),
(8, 8, 2, 'Modern House', 'Archviz model', 40.00, 120000, 'Yes'),
(9, 9, 1, 'Leather Sofa', 'PBR textures', 18.00, 8500, 'Yes'),
(10, 10, 5, 'Space Station', 'Modular sci-fi station', 55.00, 320000, 'Yes'),
(1, 2, 2, 'Hoverbike', 'Sci-fi vehicle', 22.00, 35000, 'Yes'),
(2, 3, 1, 'Sci-Fi Pistol', 'Weapon prop', 8.00, 4000, 'Yes');

INSERT INTO model_file (id_model, format, size_mb) VALUES
(1, 'FBX', 45.5), (1, 'BLEND', 50.2), (2, 'OBJ', 12.0), (3, 'FBX', 8.5),
(4, 'BLEND', 120.0), (5, 'OBJ', 2.1), (6, 'FBX', 35.0), (7, 'FBX', 18.4),
(8, 'BLEND', 85.0), (9, 'OBJ', 15.6), (10, 'FBX', 210.0), (11, 'BLEND', 42.0),
(12, 'OBJ', 5.5);

INSERT INTO cart (id_buyer, status, total_amount, created_date) VALUES
(1, 'Completed', 25.00, '2025-02-10'),
(2, 'Completed', 15.00, '2025-02-20'),
(3, 'Pending', 10.00, '2025-03-01'),
(4, 'Completed', 40.00, '2025-03-15'),
(5, 'Completed', 18.00, '2025-04-05'),
(6, 'Pending', 55.00, '2025-04-22'),
(7, 'Completed', 30.00, '2025-05-10'),
(8, 'Pending', 12.00, '2025-06-01'),
(9, 'Completed', 5.00, '2025-06-15'),
(10, 'Pending', 0.01, '2025-07-10'),
(1, 'Active', 22.00, '2025-08-01');

INSERT INTO cart_item (id_cart, id_model, fixed_price) VALUES
(1, 1, 25.00), (2, 2, 15.00), (3, 3, 10.00), (4, 8, 40.00),
(5, 9, 18.00), (6, 10, 55.00), (7, 6, 30.00), (8, 7, 12.00),
(9, 5, 5.00), (10, 4, 0.01), (11, 11, 22.00);

INSERT INTO review (id_model, id_buyer, rating, comment_text) VALUES
(1, 1, 5, 'Amazing quality!'),
(2, 2, 4, 'Good, but needs better textures.'),
(3, 4, 5, 'Perfect for my game.'),
(8, 5, 5, 'Very detailed archviz model.'),
(9, 7, 4, 'Looks great in my render.'),
(10, 6, 5, 'Outstanding work!'),
(6, 8, 4, 'Nice animation loop.'),
(5, 9, 5, 'Simple but effective.'),
(7, 10, 3, 'A bit low-res for my taste.'),
(1, 3, 4, 'Good rig.');

-- Перевірка кількості записів
SELECT 'seller' AS Table_Name, COUNT(*) AS Rows_Count FROM seller
UNION ALL SELECT 'buyer', COUNT(*) FROM buyer
UNION ALL SELECT 'category', COUNT(*) FROM category
UNION ALL SELECT 'license', COUNT(*) FROM license
UNION ALL SELECT 'model_3d', COUNT(*) FROM model_3d
UNION ALL SELECT 'model_file', COUNT(*) FROM model_file
UNION ALL SELECT 'cart', COUNT(*) FROM cart
UNION ALL SELECT 'cart_item', COUNT(*) FROM cart_item
UNION ALL SELECT 'review', COUNT(*) FROM review;"""

add_code(sql_insert)

add_paragraph("[Тут розмістити Рис. 3. Сценарій наповнення даними та результат перевірки кількості записів]", align='CENTER', first_line_indent=0)

# Додати Таблицю 1
add_paragraph("Таблиця 1. Кількість записів у таблицях БД marketplace_3d", align='RIGHT', first_line_indent=0)

table_data = [
    ["Таблиця", "Зміст", "Записів"],
    ["seller", "Продавці (автори) 3D-моделей", "10"],
    ["buyer", "Покупці (користувачі маркетплейсу)", "12"],
    ["category", "Категорії 3D-моделей", "10"],
    ["license", "Ліцензії на використання", "10"],
    ["model_3d", "Дані про 3D-моделі", "12"],
    ["model_file", "Файли моделей (формати, розміри)", "13"],
    ["cart", "Кошики та замовлення", "11"],
    ["cart_item", "Елементи кошика (одиниці замовлення)", "11"],
    ["review", "Відгуки та оцінки моделей", "10"]
]

table1 = doc.add_table(rows=len(table_data), cols=3)
table1.style = 'Table Grid'
table1.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, row in enumerate(table_data):
    for j, cell_text in enumerate(row):
        cell = table1.cell(i, j)
        cell.text = cell_text
        for p in cell.paragraphs:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(12)
            if i == 0:
                p.runs[0].bold = True

add_paragraph("")

# --- TASK 4 ---
add_paragraph("Завдання 4. Генерація EER-моделі БД та порівняння з моделлю DbDesigner", bold=True, align='LEFT')
add_paragraph("EER-модель згенеровано засобами MySQL Workbench зі створеної БД (зворотне проєктування):", align='JUSTIFY')
add_paragraph("1) меню Database → Reverse Engineer… (Ctrl+R);", align='JUSTIFY')
add_paragraph("2) обрати з’єднання Local instance та ввести пароль користувача root, Next;", align='JUSTIFY')
add_paragraph("3) у списку схем позначити marketplace_3d, Next → Execute;", align='JUSTIFY')
add_paragraph("4) залишити позначку «Place imported objects on a diagram», Execute → Next → Finish.", align='JUSTIFY')
add_paragraph("Workbench відкриває EER-діаграму, побудовану за структурою створених таблиць.", align='JUSTIFY')

add_paragraph("[Тут розмістити Рис. 4. EER-модель БД marketplace_3d, згенерована в MySQL Workbench]", align='CENTER', first_line_indent=0)

add_paragraph("Порівняння з моделлю з ЛР2 (DbDesigner) наведено в табл. 2. В обох моделях однакові 9 таблиць, склад атрибутів і типи даних, а також 9 зв’язків «один-до-багатьох».", align='JUSTIFY')

add_paragraph("Таблиця 2. Зв’язки між таблицями в EER-моделі та моделі DbDesigner", align='RIGHT', first_line_indent=0)

table2_data = [
    ["Зв’язок (батьківська → дочірня)", "Зовнішній ключ", "Тип", "Збіг з ЛР2"],
    ["seller → model_3d", "id_seller", "1:N", "так"],
    ["category → model_3d", "id_category", "1:N", "так"],
    ["license → model_3d", "id_license", "1:N", "так"],
    ["model_3d → model_file", "id_model", "1:N", "так"],
    ["buyer → cart", "id_buyer", "1:N", "так"],
    ["cart → cart_item", "id_cart", "1:N", "так"],
    ["model_3d → cart_item", "id_model", "1:N", "так"],
    ["model_3d → review", "id_model", "1:N", "так"],
    ["buyer → review", "id_buyer", "1:N", "так"]
]

table2 = doc.add_table(rows=len(table2_data), cols=4)
table2.style = 'Table Grid'
table2.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, row in enumerate(table2_data):
    for j, cell_text in enumerate(row):
        cell = table2.cell(i, j)
        cell.text = cell_text
        for p in cell.paragraphs:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(12)
            if i == 0:
                p.runs[0].bold = True

add_paragraph("")

# --- CONCLUSIONS ---
add_paragraph("Висновки", bold=True, align='CENTER')
add_paragraph("У лабораторній роботі засобами SQL у MySQL Workbench створено базу даних marketplace_3d для предметної області «Сайт продажу 3D-моделей (маркетплейс)». Сценарій створення БД можна запускати повторно: DROP DATABASE IF EXISTS та CREATE DATABASE IF NOT EXISTS щоразу дають однаковий результат, забезпечуючи ідемпотентність.", align='JUSTIFY')
add_paragraph("Створено 9 таблиць із первинними ключами AUTO_INCREMENT і 9 зовнішніми ключами. За допомогою ALTER TABLE додано додаткові обмеження CHECK та UNIQUE, тож СКБД сама не дає внести некоректні дані (від’ємну ціну чи розмір файлу, рейтинг поза межами від 1 до 5, або неунікальні email та nickname).", align='JUSTIFY')
add_paragraph("Таблиці наповнено тестовими даними: від 10 до 13 записів у кожній. EER-модель, згенерована Workbench, повністю збігається з фізичною моделлю, побудованою в DbDesigner у ЛР2. Отже, SQL-сценарії реалізують спроєктовану структуру БД без жодних відхилень.", align='JUSTIFY')

doc.save("Лемішка А_ПП-24_ЛР3.docx")
