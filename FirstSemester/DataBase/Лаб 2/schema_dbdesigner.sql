-- ========================================================
-- Національний університет "Львівська політехніка"
-- Кафедра систем автоматизованого проектування (САП)
-- Дисципліна: "Організація баз даних та знань"
-- Лабораторна робота № 2: "Логічне та фізичне моделювання бази даних"
-- 
-- Студент: Лемішка А., група ПП-24
-- Викладач: Спас Н.Я.
--
-- Фізична модель БД (MySQL DDL для DbDesigner):
-- Предметна область: "Сайт продажу 3D-моделей (маркетплейс)"
-- ========================================================

-- 1. Таблиця "seller" (Продавець)
CREATE TABLE seller (
    id_seller INT PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    rating DECIMAL(3, 2) NOT NULL
);

-- 2. Таблиця "buyer" (Покупець)
CREATE TABLE buyer (
    id_buyer INT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

-- 3. Таблиця "category" (Категорія)
CREATE TABLE category (
    id_category INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- 4. Таблиця "license" (Ліцензія)
CREATE TABLE license (
    id_license INT PRIMARY KEY,
    id_change INT NOT NULL,
    license_name VARCHAR(50) NOT NULL,
    usage_type VARCHAR(50) NOT NULL,
    allow_modification VARCHAR(10) NOT NULL,
    creation_date DATE NOT NULL,
    creation_time TIME NOT NULL
);

-- 5. Таблиця "model_3d" (3D-Модель)
CREATE TABLE model_3d (
    id_model INT PRIMARY KEY,
    id_seller INT NOT NULL,
    id_category INT NOT NULL,
    id_license INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(1000),
    price DECIMAL(10, 2) NOT NULL,
    polygon_count INT NOT NULL,
    has_texture VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_seller) REFERENCES seller(id_seller),
    FOREIGN KEY (id_category) REFERENCES category(id_category),
    FOREIGN KEY (id_license) REFERENCES license(id_license)
);

-- 6. Таблиця "model_file" (Файл 3D-моделі)
CREATE TABLE model_file (
    id_file INT PRIMARY KEY,
    id_model INT NOT NULL,
    format VARCHAR(20) NOT NULL,
    size_mb DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

-- 7. Таблиця "cart" (Кошик замовлення)
CREATE TABLE cart (
    id_cart INT PRIMARY KEY,
    id_buyer INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    created_date DATE NOT NULL,
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);

-- 8. Таблиця "cart_item" (Елемент кошика)
CREATE TABLE cart_item (
    id_item INT PRIMARY KEY,
    id_cart INT NOT NULL,
    id_model INT NOT NULL,
    fixed_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cart) REFERENCES cart(id_cart),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

-- 9. Таблиця "review" (Відгук покупця)
CREATE TABLE review (
    id_review INT PRIMARY KEY,
    id_model INT NOT NULL,
    id_buyer INT NOT NULL,
    rating INT NOT NULL,
    comment_text VARCHAR(1000),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model),
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);
