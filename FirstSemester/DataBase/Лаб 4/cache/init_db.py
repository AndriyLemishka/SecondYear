import sqlite3
import re
import os

db_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\marketplace_3d.db"
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

def regexp(expr, item):
    if item is None:
        return False
    return bool(re.search(expr, str(item), re.IGNORECASE))

conn.create_function("REGEXP", 2, regexp)
cursor = conn.cursor()

ddl = """
CREATE TABLE seller (
    id_seller INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL UNIQUE,
    rating REAL NOT NULL CHECK (rating BETWEEN 1 AND 5)
);

CREATE TABLE buyer (
    id_buyer INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    registration_date TEXT NOT NULL
);

CREATE TABLE category (
    id_category INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE license (
    id_license INTEGER PRIMARY KEY AUTOINCREMENT,
    id_change INTEGER NOT NULL,
    license_name TEXT NOT NULL,
    usage_type TEXT NOT NULL,
    allow_modification TEXT NOT NULL,
    creation_date TEXT NOT NULL,
    creation_time TEXT NOT NULL
);

CREATE TABLE model_3d (
    id_model INTEGER PRIMARY KEY AUTOINCREMENT,
    id_seller INTEGER,
    id_category INTEGER,
    id_license INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK (price > 0),
    polygon_count INTEGER NOT NULL CHECK (polygon_count > 0),
    has_texture TEXT NOT NULL,
    FOREIGN KEY (id_seller) REFERENCES seller(id_seller),
    FOREIGN KEY (id_category) REFERENCES category(id_category),
    FOREIGN KEY (id_license) REFERENCES license(id_license)
);

CREATE TABLE model_file (
    id_file INTEGER PRIMARY KEY AUTOINCREMENT,
    id_model INTEGER,
    format TEXT NOT NULL,
    size_mb REAL NOT NULL CHECK (size_mb > 0),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

CREATE TABLE cart (
    id_cart INTEGER PRIMARY KEY AUTOINCREMENT,
    id_buyer INTEGER,
    status TEXT NOT NULL,
    total_amount REAL NOT NULL,
    created_date TEXT NOT NULL,
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);

CREATE TABLE cart_item (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cart INTEGER,
    id_model INTEGER,
    fixed_price REAL NOT NULL,
    FOREIGN KEY (id_cart) REFERENCES cart(id_cart),
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model)
);

CREATE TABLE review (
    id_review INTEGER PRIMARY KEY AUTOINCREMENT,
    id_model INTEGER,
    id_buyer INTEGER,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment_text TEXT,
    FOREIGN KEY (id_model) REFERENCES model_3d(id_model),
    FOREIGN KEY (id_buyer) REFERENCES buyer(id_buyer)
);
"""

cursor.executescript(ddl)

inserts = """
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
(2, 3, 1, 'Sci-Fi Pistol', 'Weapon prop', 8.00, 4000, 'Yes'),
(3, 5, 1, 'Draft Prototype Box', NULL, 3.50, 500, 'No'),
(4, 5, 3, 'Untextured Crate', NULL, 4.00, 800, 'No');

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
(1, 3, 4, 'Good rig.'),
(11, 2, 5, NULL),
(12, 5, 4, NULL);
"""

cursor.executescript(inserts)
conn.commit()
print("Database re-initialized with full test data!")
