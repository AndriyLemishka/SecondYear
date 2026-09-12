-- =======================================================
-- Database: 3D Model Marketplace (Маркетплейс 3D-моделей)
-- Laboratory Work #1. Task 2
-- Standard ANSI SQL DDL (English identifiers for ERDplus Import)
-- =======================================================

-- 1. Table "Seller" (Продавець)
CREATE TABLE Seller (
    Seller_ID INT PRIMARY KEY,
    Nickname VARCHAR(50) NOT NULL,
    Rating DECIMAL(3, 2) NOT NULL
);

-- 2. Table "Buyer" (Покупець)
CREATE TABLE Buyer (
    Buyer_ID INT PRIMARY KEY,
    Email VARCHAR(100) NOT NULL,
    Registration_Date DATE NOT NULL
);

-- 3. Table "Category" (Категорія)
CREATE TABLE Category (
    Category_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

-- 4. Table "Model_3D" (3D_Модель)
CREATE TABLE Model_3D (
    Model_ID INT PRIMARY KEY,
    Seller_ID INT NOT NULL,
    Category_ID INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(1000),
    Price DECIMAL(10, 2) NOT NULL,
    Polygon_Count INT NOT NULL,
    Has_Texture VARCHAR(10) NOT NULL,
    FOREIGN KEY (Seller_ID) REFERENCES Seller(Seller_ID),
    FOREIGN KEY (Category_ID) REFERENCES Category(Category_ID)
);

-- 5. Table "Model_File" (Файл_Моделі)
CREATE TABLE Model_File (
    File_ID INT PRIMARY KEY,
    Model_ID INT NOT NULL,
    Format VARCHAR(20) NOT NULL,
    Size_MB DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Model_ID) REFERENCES Model_3D(Model_ID)
);

-- 6. Table "Cart" (Кошик)
CREATE TABLE Cart (
    Cart_ID INT PRIMARY KEY,
    Buyer_ID INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    Created_Date DATE NOT NULL,
    FOREIGN KEY (Buyer_ID) REFERENCES Buyer(Buyer_ID)
);

-- 7. Table "Cart_Item" (Елемент_Кошика)
CREATE TABLE Cart_Item (
    Item_ID INT PRIMARY KEY,
    Cart_ID INT NOT NULL,
    Model_ID INT NOT NULL,
    Fixed_Price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Cart_ID) REFERENCES Cart(Cart_ID),
    FOREIGN KEY (Model_ID) REFERENCES Model_3D(Model_ID)
);

-- 8. Table "Transaction" (Транзакція)
CREATE TABLE Transaction (
    Transaction_ID INT PRIMARY KEY,
    Cart_ID INT NOT NULL,
    Buyer_ID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Transaction_Date DATE NOT NULL,
    FOREIGN KEY (Cart_ID) REFERENCES Cart(Cart_ID),
    FOREIGN KEY (Buyer_ID) REFERENCES Buyer(Buyer_ID)
);

-- 9. Table "Review" (Відгук)
CREATE TABLE Review (
    Review_ID INT PRIMARY KEY,
    Model_ID INT NOT NULL,
    Buyer_ID INT NOT NULL,
    Rating INT NOT NULL,
    Comment_Text VARCHAR(1000),
    FOREIGN KEY (Model_ID) REFERENCES Model_3D(Model_ID),
    FOREIGN KEY (Buyer_ID) REFERENCES Buyer(Buyer_ID)
);
