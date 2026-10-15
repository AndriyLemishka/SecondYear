-- Завдання 1. Створення БД
DROP DATABASE IF EXISTS marketplace_3d;
CREATE DATABASE IF NOT EXISTS marketplace_3d
CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE marketplace_3d;
SHOW DATABASES LIKE 'marketplace_3d';

-- Завдання 2. Створення таблиць БД
CREATE TABLE seller (
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
DESCRIBE model_3d;

-- Завдання 3. Наповнення таблиць БД даними
-- Наповнення довідкових таблиць
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
UNION ALL SELECT 'review', COUNT(*) FROM review;