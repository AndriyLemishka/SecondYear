-- Завдання 5. Розділення таблиць бази даних за допомогою RANGE, LIST і HASH
USE marketplace_3d;

-- 1. Створення таблиці з секціонуванням RANGE (розділення таблиці cart)
CREATE TABLE IF NOT EXISTS cart_range (
  id_cart INT NOT NULL,
  id_buyer INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  created_date DATE NOT NULL,
  PRIMARY KEY (id_cart, created_date)
)
PARTITION BY RANGE (YEAR(created_date)) (
  PARTITION p_2023 VALUES LESS THAN (2024),
  PARTITION p_2024 VALUES LESS THAN (2025),
  PARTITION p_2025 VALUES LESS THAN (2026),
  PARTITION p_max VALUES LESS THAN MAXVALUE
);

-- 2. Створення таблиці з секціонуванням LIST (розділення таблиці model_3d)
CREATE TABLE IF NOT EXISTS model_list (
  id_model INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  id_category INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_model, id_category)
)
PARTITION BY LIST (id_category) (
  PARTITION p_gamedev VALUES IN (1, 2, 3),
  PARTITION p_cg VALUES IN (4, 5),
  PARTITION p_other VALUES IN (6, 7, 8)
);

-- 3. Створення таблиці з секціонуванням HASH (розділення таблиці buyer)
CREATE TABLE IF NOT EXISTS buyer_hash (
  id_buyer INT NOT NULL,
  email VARCHAR(100) NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (id_buyer)
)
PARTITION BY HASH (id_buyer)
PARTITIONS 4;

-- Запит 5.1: Розділення таблиці cart за допомогою RANGE (секціонування замовлень за роками)
SELECT id_cart, status, total_amount, created_date FROM cart_range PARTITION (p_2024) LIMIT 5;

-- Запит 5.2: Розділення таблиці model_3d за допомогою LIST (секціонування моделей за категоріями)
SELECT id_model, name, id_category, price FROM model_list PARTITION (p_gamedev) LIMIT 5;

-- Запит 5.3: Розділення таблиці buyer за допомогою HASH (рівномірне хешування покупців за id_buyer)
SELECT id_buyer, email, registration_date FROM buyer_hash PARTITION (p0) LIMIT 5;

-- Запит 5.4: План виконання запиту з відсіканням секцій (Partition Pruning через EXPLAIN)
EXPLAIN PARTITIONS SELECT id_cart, total_amount FROM cart_range WHERE created_date = '2024-05-15';

-- Запит 5.5: Перевірка розподілу записів по створених секціях через information_schema.partitions
SELECT table_name, partition_name, table_rows FROM information_schema.partitions WHERE table_name = 'cart_range';

