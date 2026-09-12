-- =======================================================
-- База даних: Маркетплейс 3D-моделей
-- Лабораторна робота № 1. Завдання 2
-- Скрипт створення таблиць (SQL DDL) українською мовою
-- =======================================================

-- 1. Таблиця "Продавець"
CREATE TABLE Продавець (
    ID_Продавця INT PRIMARY KEY,
    Нікнейм VARCHAR(50) NOT NULL,
    Рейтинг DECIMAL(3, 2) NOT NULL
);

-- 2. Таблиця "Покупець"
CREATE TABLE Покупець (
    ID_Покупця INT PRIMARY KEY,
    Email VARCHAR(100) NOT NULL,
    Дата_реєстрації DATE NOT NULL
);

-- 3. Таблиця "Категорія"
CREATE TABLE Категорія (
    ID_Категорії INT PRIMARY KEY,
    Назва VARCHAR(50) NOT NULL
);

-- 4. Таблиця "3D_Модель"
CREATE TABLE 3D_Модель (
    ID_Моделі INT PRIMARY KEY,
    ID_Продавця INT NOT NULL,
    ID_Категорії INT NOT NULL,
    Назва VARCHAR(100) NOT NULL,
    Опис VARCHAR(1000),
    Ціна DECIMAL(10, 2) NOT NULL,
    Кількість_полігонів INT NOT NULL,
    Наявність_текстури VARCHAR(10) NOT NULL,
    FOREIGN KEY (ID_Продавця) REFERENCES Продавець(ID_Продавця),
    FOREIGN KEY (ID_Категорії) REFERENCES Категорія(ID_Категорії)
);

-- 5. Таблиця "Файл_Моделі"
CREATE TABLE Файл_Моделі (
    ID_Файлу INT PRIMARY KEY,
    ID_Моделі INT NOT NULL,
    Формат VARCHAR(20) NOT NULL,
    Розмір_МБ DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ID_Моделі) REFERENCES 3D_Модель(ID_Моделі)
);

-- 6. Таблиця "Кошик"
CREATE TABLE Кошик (
    ID_Кошика INT PRIMARY KEY,
    ID_Покупця INT NOT NULL,
    Статус VARCHAR(50) NOT NULL,
    Дата_створення DATE NOT NULL,
    FOREIGN KEY (ID_Покупця) REFERENCES Покупець(ID_Покупця)
);

-- 7. Таблиця "Елемент_Кошика"
CREATE TABLE Елемент_Кошика (
    ID_Елемента INT PRIMARY KEY,
    ID_Кошика INT NOT NULL,
    ID_Моделі INT NOT NULL,
    Фіксована_ціна DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ID_Кошика) REFERENCES Кошик(ID_Кошика),
    FOREIGN KEY (ID_Моделі) REFERENCES 3D_Модель(ID_Моделі)
);

-- 8. Таблиця "Транзакція"
CREATE TABLE Транзакція (
    ID_Транзакції INT PRIMARY KEY,
    ID_Кошика INT NOT NULL,
    ID_Покупця INT NOT NULL,
    Сума DECIMAL(10, 2) NOT NULL,
    Дата DATE NOT NULL,
    FOREIGN KEY (ID_Кошика) REFERENCES Кошик(ID_Кошика),
    FOREIGN KEY (ID_Покупця) REFERENCES Покупець(ID_Покупця)
);

-- 9. Таблиця "Відгук"
CREATE TABLE Відгук (
    ID_Відгуку INT PRIMARY KEY,
    ID_Моделі INT NOT NULL,
    ID_Покупця INT NOT NULL,
    Оцінка INT NOT NULL,
    Текст VARCHAR(1000),
    FOREIGN KEY (ID_Моделі) REFERENCES 3D_Модель(ID_Моделі),
    FOREIGN KEY (ID_Покупця) REFERENCES Покупець(ID_Покупця)
);
