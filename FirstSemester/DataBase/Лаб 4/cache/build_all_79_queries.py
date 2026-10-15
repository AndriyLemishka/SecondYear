import os
import re
import json
import sqlite3
from render_screenshots import render_workbench_screenshot

db_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\marketplace_3d.db"
cache_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache"
sql_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\sql"

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row

def regexp(expr, item):
    if item is None:
        return False
    return bool(re.search(expr, str(item), re.IGNORECASE))

conn.create_function("REGEXP", 2, regexp)
cursor = conn.cursor()

# Full list of 79 queries structured by task and sub-command
all_tasks_def = [
    {
        "task_num": 1,
        "title": "Завдання 1. Написання запитів простої вибірки (SELECT, FROM, LIMIT, DISTINCT, IS NULL)",
        "subsections": [
            {
                "sub_id": "1.1",
                "cmd_name": "SELECT ... FROM",
                "desc": "Вибірка стовпців, усіх полів, псевдонімів AS, розрахункових формул та констант (5 комбінацій)",
                "queries": [
                    {
                        "num": "1.1.1",
                        "title": "Вибірка всіх стовпців таблиці моделей (SELECT *)",
                        "desc": "Повний перегляд атрибутів перших 5 записів каталогу 3D-моделей.",
                        "sql": "SELECT id_model, name, price, polygon_count, has_texture FROM model_3d LIMIT 5;"
                    },
                    {
                        "num": "1.1.2",
                        "title": "Вибірка обраних стовпців із таблиці покупців",
                        "desc": "Отримання списку покупців лише з полями id, email та дати реєстрації.",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer LIMIT 5;"
                    },
                    {
                        "num": "1.1.3",
                        "title": "Використання псевдонімів стовпців (AS)",
                        "desc": "Перейменування полів результату запиту продавців для зручності відображення у звіті.",
                        "sql": "SELECT nickname AS author_name, rating AS author_score FROM seller LIMIT 5;"
                    },
                    {
                        "num": "1.1.4",
                        "title": "Вибірка з обчислювальним стовпцем-формулою",
                        "desc": "Автоматичний розрахунок остаточної вартості моделі з урахуванням ПДВ 20%.",
                        "sql": "SELECT name, price, ROUND(price * 1.20, 2) AS price_with_vat FROM model_3d LIMIT 5;"
                    },
                    {
                        "num": "1.1.5",
                        "title": "Вибірка зі статичною константою у стовпці",
                        "desc": "Додавання фіксованої мітки типу контенту 'Digital 3D Asset' до кожного рядка вибірки.",
                        "sql": "SELECT name, 'Digital 3D Asset' AS product_type, price FROM model_3d LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "1.2",
                "cmd_name": "LIMIT",
                "desc": "Обмеження кількості рядків та вибірка зі зміщенням offset, count (5 комбінацій)",
                "queries": [
                    {
                        "num": "1.2.1",
                        "title": "Обмеження вибірки першими 3 записами (LIMIT 3)",
                        "desc": "Отримання перших трьох 3D-моделей каталогу.",
                        "sql": "SELECT id_model, name, price FROM model_3d LIMIT 3;"
                    },
                    {
                        "num": "1.2.2",
                        "title": "Обмеження вибірки категорій (LIMIT 5)",
                        "desc": "Виведення перших п'яти категорій каталогу.",
                        "sql": "SELECT id_category, name FROM category LIMIT 5;"
                    },
                    {
                        "num": "1.2.3",
                        "title": "Посторінкова навігація зі зміщенням (LIMIT 2, 3)",
                        "desc": "Пропуск перших двох записів моделей та вибірка наступних трьох.",
                        "sql": "SELECT id_model, name, price FROM model_3d LIMIT 2, 3;"
                    },
                    {
                        "num": "1.2.4",
                        "title": "Вибірка замовлень зі зміщенням (LIMIT 4, 3)",
                        "desc": "Отримання другої сторінки списку кошиків покупців.",
                        "sql": "SELECT id_cart, id_buyer, total_amount, status FROM cart LIMIT 4, 3;"
                    },
                    {
                        "num": "1.2.5",
                        "title": "Отримання однієї топ-позиції (LIMIT 1)",
                        "desc": "Швидке знаходження однієї найдорожчої моделі у каталозі.",
                        "sql": "SELECT id_model, name, price FROM model_3d ORDER BY price DESC LIMIT 1;"
                    }
                ]
            },
            {
                "sub_id": "1.3",
                "cmd_name": "DISTINCT",
                "desc": "Фільтрація дублікатів та вибірка унікальних значень (5 комбінацій)",
                "queries": [
                    {
                        "num": "1.3.1",
                        "title": "Унікальні формати файлів моделей",
                        "desc": "Отримання переліку неповторюваних розширень 3D-файлів на маркетплейсі.",
                        "sql": "SELECT DISTINCT format FROM model_file;"
                    },
                    {
                        "num": "1.3.2",
                        "title": "Унікальні статуси замовлень",
                        "desc": "Визначення всіх можливих унікальних статусів кошиків у системі.",
                        "sql": "SELECT DISTINCT status FROM cart;"
                    },
                    {
                        "num": "1.3.3",
                        "title": "Унікальні типи використання ліцензій",
                        "desc": "Перегляд категорій комерційного та некомерційного використання контенту.",
                        "sql": "SELECT DISTINCT usage_type FROM license;"
                    },
                    {
                        "num": "1.3.4",
                        "title": "Унікальні бали оцінок у відгуках",
                        "desc": "Вибірка переліку всіх оцінок (рейтингів), які покупці ставили товарам.",
                        "sql": "SELECT DISTINCT rating FROM review ORDER BY rating ASC;"
                    },
                    {
                        "num": "1.3.5",
                        "title": "Унікальні пари формату та розміру файлу",
                        "desc": "Вибірка неповторюваних комбінацій формату та розміру файлів моделей.",
                        "sql": "SELECT DISTINCT format, size_mb FROM model_file LIMIT 6;"
                    }
                ]
            },
            {
                "sub_id": "1.4",
                "cmd_name": "IS NULL / IS NOT NULL",
                "desc": "Перевірка полів на невизначені значення NULL та NOT NULL (5 комбінацій)",
                "queries": [
                    {
                        "num": "1.4.1",
                        "title": "Пошук 3D-моделей без опису (IS NULL)",
                        "desc": "Виявлення карток товарів, де опис не було заповнено автором.",
                        "sql": "SELECT id_model, name, description, price FROM model_3d WHERE description IS NULL;"
                    },
                    {
                        "num": "1.4.2",
                        "title": "Вибірка моделей із заповненим описом (IS NOT NULL)",
                        "desc": "Отримання моделей, які мають докладний опис функціоналу.",
                        "sql": "SELECT id_model, name, description, price FROM model_3d WHERE description IS NOT NULL LIMIT 5;"
                    },
                    {
                        "num": "1.4.3",
                        "title": "Пошук відгуків без тексту коментаря (IS NULL)",
                        "desc": "Виявлення оцінок, де користувач поставив бал без написання тексту.",
                        "sql": "SELECT id_review, id_model, id_buyer, rating, comment_text FROM review WHERE comment_text IS NULL;"
                    },
                    {
                        "num": "1.4.4",
                        "title": "Вибірка розгорнутих відгуків (IS NOT NULL)",
                        "desc": "Отримання відгуків покупців із текстовими коментарями.",
                        "sql": "SELECT id_review, id_model, id_buyer, rating, comment_text FROM review WHERE comment_text IS NOT NULL LIMIT 5;"
                    },
                    {
                        "num": "1.4.5",
                        "title": "Комбінована перевірка на IS NOT NULL та ціну",
                        "desc": "Вибірка моделей з описом та вартістю від 20 у.о.",
                        "sql": "SELECT id_model, name, price, description FROM model_3d WHERE description IS NOT NULL AND price >= 20.00 LIMIT 5;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 2,
        "title": "Завдання 2. Сортування даних у запитах (ORDER BY, DESC, ASC)",
        "subsections": [
            {
                "sub_id": "2.1",
                "cmd_name": "ORDER BY (ASC / за кількома стовпцями / за номером)",
                "desc": "Сортування за зростанням, декількома полями та номерами стовпців (3 комбінації)",
                "queries": [
                    {
                        "num": "2.1.1",
                        "title": "Сортування моделей за зростанням ціни (ORDER BY ASC)",
                        "desc": "Перегляд каталогу від найдешевших моделей до найдорожчих.",
                        "sql": "SELECT id_model, name, price FROM model_3d ORDER BY price ASC LIMIT 5;"
                    },
                    {
                        "num": "2.1.2",
                        "title": "Сортування файлів за форматом та розміром",
                        "desc": "Багаторівневе сортування за назвою формату та зростанням обсягу файлу.",
                        "sql": "SELECT id_file, id_model, format, size_mb FROM model_file ORDER BY format ASC, size_mb ASC LIMIT 6;"
                    },
                    {
                        "num": "2.1.3",
                        "title": "Сортування за порядковими номерами стовпців (ORDER BY 3, 2)",
                        "desc": "Сортування продавців за третім стовпцем (рейтинг) та другим (нікнейм).",
                        "sql": "SELECT id_seller, nickname, rating FROM seller ORDER BY 3 ASC, 2 ASC LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "2.2",
                "cmd_name": "ORDER BY ... DESC",
                "desc": "Сортування за спаданням одного стовпця, розрахункового виразу та комбіноване (3 комбінації)",
                "queries": [
                    {
                        "num": "2.2.1",
                        "title": "Сортування авторів за спаданням рейтингу (DESC)",
                        "desc": "Формування рейтингової таблиці найкращих продавців маркетплейсу.",
                        "sql": "SELECT id_seller, nickname, rating FROM seller ORDER BY rating DESC LIMIT 5;"
                    },
                    {
                        "num": "2.2.2",
                        "title": "Сортування за спаданням розрахункового виразу",
                        "desc": "Впорядкування моделей за спаданням ціни з урахуванням ПДВ 20%.",
                        "sql": "SELECT id_model, name, price, ROUND(price * 1.20, 2) AS price_vat FROM model_3d ORDER BY price * 1.20 DESC LIMIT 5;"
                    },
                    {
                        "num": "2.2.3",
                        "title": "Комбіноване сортування (текстура DESC, полігони ASC)",
                        "desc": "Пріоритет моделей з текстурами, а серед них — впорядкування за найменшою кількістю полігонів.",
                        "sql": "SELECT id_model, name, has_texture, polygon_count, price FROM model_3d ORDER BY has_texture DESC, polygon_count ASC LIMIT 6;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 3,
        "title": "Завдання 3. Фільтрація даних за умовами (IN, BETWEEN, LIKE, REGEXP)",
        "subsections": [
            {
                "sub_id": "3.1",
                "cmd_name": "Оператор IN / NOT IN",
                "desc": "Фільтрація за списками ідентифікаторів, форматів та статусів (5 комбінацій)",
                "queries": [
                    {
                        "num": "3.1.1",
                        "title": "Фільтрація моделей за списком категорій (IN)",
                        "desc": "Вибірка товарів категорій Characters (1), Vehicles (2) та Architecture (8).",
                        "sql": "SELECT id_model, name, id_category, price FROM model_3d WHERE id_category IN (1, 2, 8);"
                    },
                    {
                        "num": "3.1.2",
                        "title": "Фільтрація файлів за списком розширень (IN)",
                        "desc": "Вибірка файлів популярних 3D-форматів FBX та BLEND.",
                        "sql": "SELECT id_file, id_model, format, size_mb FROM model_file WHERE format IN ('FBX', 'BLEND') LIMIT 6;"
                    },
                    {
                        "num": "3.1.3",
                        "title": "Фільтрація кошиків за статусами (IN)",
                        "desc": "Вибірка замовлень зі статусами Completed або Active.",
                        "sql": "SELECT id_cart, id_buyer, status, total_amount FROM cart WHERE status IN ('Completed', 'Active') LIMIT 5;"
                    },
                    {
                        "num": "3.1.4",
                        "title": "Виключення ліцензій за списком (NOT IN)",
                        "desc": "Вибірка ліцензій, ідентифікатори яких не входять до списку (1, 3, 7).",
                        "sql": "SELECT id_license, license_name, usage_type FROM license WHERE id_license NOT IN (1, 3, 7) LIMIT 5;"
                    },
                    {
                        "num": "3.1.5",
                        "title": "Виключення низьких оцінок у відгуках (NOT IN)",
                        "desc": "Вибірка відгуків з високими балами (виключаючи оцінки 1, 2, 3).",
                        "sql": "SELECT id_review, id_model, rating, comment_text FROM review WHERE rating NOT IN (1, 2, 3) LIMIT 5;"
                    }
                ]
            },
            {
                "sub_id": "3.2",
                "cmd_name": "Оператор BETWEEN / NOT BETWEEN",
                "desc": "Фільтрація за числовими та часовими діапазонами (5 комбінацій)",
                "queries": [
                    {
                        "num": "3.2.1",
                        "title": "Фільтрація моделей за діапазоном цін (BETWEEN)",
                        "desc": "Пошук 3D-моделей середнього цінового сегменту від 10.00 до 30.00 у.о.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE price BETWEEN 10.00 AND 30.00;"
                    },
                    {
                        "num": "3.2.2",
                        "title": "Фільтрація розмірів файлів від 10 до 50 МБ (BETWEEN)",
                        "desc": "Вибірка файлів середнього обсягу для оптимізації завантаження.",
                        "sql": "SELECT id_file, id_model, format, size_mb FROM model_file WHERE size_mb BETWEEN 10.0 AND 50.0;"
                    },
                    {
                        "num": "3.2.3",
                        "title": "Фільтрація рейтингу авторів від 4.5 до 5.0 (BETWEEN)",
                        "desc": "Вибірка авторів з найвищими середніми оцінками.",
                        "sql": "SELECT id_seller, nickname, rating FROM seller WHERE rating BETWEEN 4.50 AND 5.00;"
                    },
                    {
                        "num": "3.2.4",
                        "title": "Фільтрація покупців за діапазоном дат реєстрації",
                        "desc": "Вибірка користувачів, зареєстрованих між лютим та травнем 2025 року.",
                        "sql": "SELECT id_buyer, email, registration_date FROM buyer WHERE registration_date BETWEEN '2025-02-01' AND '2025-05-31';"
                    },
                    {
                        "num": "3.2.5",
                        "title": "Фільтрація моделей поза діапазоном складності (NOT BETWEEN)",
                        "desc": "Пошук крайніх випадків полігональності (менше 10k або більше 100k).",
                        "sql": "SELECT id_model, name, polygon_count FROM model_3d WHERE polygon_count NOT BETWEEN 10000 AND 100000 LIMIT 6;"
                    }
                ]
            },
            {
                "sub_id": "3.3",
                "cmd_name": "Оператор LIKE / NOT LIKE",
                "desc": "Масковий пошук за шаблонами зі знаками % та _ (5 комбінацій)",
                "queries": [
                    {
                        "num": "3.3.1",
                        "title": "Пошук моделей за входженням підрядка (%Sci-Fi%)",
                        "desc": "Вибірка всіх 3D-моделей фантастичної тематики.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name LIKE '%Sci-Fi%';"
                    },
                    {
                        "num": "3.3.2",
                        "title": "Пошук моделей за початковою літерою (C%)",
                        "desc": "Знаходження товарів, назва яких починається з літери 'C'.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name LIKE 'C%';"
                    },
                    {
                        "num": "3.3.3",
                        "title": "Пошук арт-акаунтів за маскою email (%_art@%)",
                        "desc": "Фільтрація користувачів з арт-спеціалізацією поштової скриньки.",
                        "sql": "SELECT id_buyer, email FROM buyer WHERE email LIKE '%_art@%';"
                    },
                    {
                        "num": "3.3.4",
                        "title": "Фільтрація моделей, що не містять ключове слово (NOT LIKE)",
                        "desc": "Вибірка моделей, назва яких не містить слова 'Car'.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name NOT LIKE '%Car%' LIMIT 5;"
                    },
                    {
                        "num": "3.3.5",
                        "title": "Пошук за точним символом підстановки (user_@mail.com)",
                        "desc": "Вибірка користувачів, пошта яких має рівно один символ після 'user'.",
                        "sql": "SELECT id_buyer, email FROM buyer WHERE email LIKE 'user_@mail.com';"
                    }
                ]
            },
            {
                "sub_id": "3.4",
                "cmd_name": "Оператор REGEXP",
                "desc": "Складна фільтрація за регулярними виразами (5 комбінацій)",
                "queries": [
                    {
                        "num": "3.4.1",
                        "title": "Пошук за початком рядка з переліком слів ^(Cyberpunk|Sports|Space)",
                        "desc": "Вибірка моделей, що починаються з Cyberpunk, Sports або Space.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '^(Cyberpunk|Sports|Space).*';"
                    },
                    {
                        "num": "3.4.2",
                        "title": "Пошук за закінченням рядка (Character|Rifle|House|Station)$",
                        "desc": "Вибірка моделей з конкретним типом об'єкта в кінці назви.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '(Character|Rifle|House|Station)$';"
                    },
                    {
                        "num": "3.4.3",
                        "title": "Пошук назв із цифровими позначеннями [0-9]",
                        "desc": "Знаходження товарів, у назві яких присутні числові індекси.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '[0-9]';"
                    },
                    {
                        "num": "3.4.4",
                        "title": "Пошук за діапазоном літер на початку рядка ^[A-C]",
                        "desc": "Вибірка моделей, назви яких починаються з перших літер латиниці A, B, C.",
                        "sql": "SELECT id_model, name, price FROM model_3d WHERE name REGEXP '^[A-C]';"
                    },
                    {
                        "num": "3.4.5",
                        "title": "Пошук позитивних відгуків за ключовими словами",
                        "desc": "Вибірка коментарів, що містять слова Amazing, Great або Perfect.",
                        "sql": "SELECT id_review, id_model, rating, comment_text FROM review WHERE comment_text REGEXP '(Amazing|Great|Perfect)';"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 4,
        "title": "Завдання 4. Використання агрегатних функцій (AVG, SUM, MIN, MAX, COUNT)",
        "subsections": [
            {
                "sub_id": "4.1",
                "cmd_name": "Функція AVG()",
                "desc": "Обчислення середніх арифметичних значень (5 комбінацій)",
                "queries": [
                    {
                        "num": "4.1.1",
                        "title": "Середня вартість усіх моделей у каталозі",
                        "desc": "Розрахунок середнього чеку за позицію в маркетплейсі.",
                        "sql": "SELECT ROUND(AVG(price), 2) AS avg_model_price FROM model_3d;"
                    },
                    {
                        "num": "4.1.2",
                        "title": "Середня кількість полігонів 3D-моделей",
                        "desc": "Оцінка середньої геометричної складності об'єктів каталогу.",
                        "sql": "SELECT ROUND(AVG(polygon_count), 0) AS avg_polygons FROM model_3d;"
                    },
                    {
                        "num": "4.1.3",
                        "title": "Середній рейтинг продавців платформи",
                        "desc": "Оцінка загального рівня якості роботи авторів.",
                        "sql": "SELECT ROUND(AVG(rating), 2) AS avg_seller_rating FROM seller;"
                    },
                    {
                        "num": "4.1.4",
                        "title": "Середній розмір файлу формату FBX",
                        "desc": "Розрахунок середнього дискового обсягу для формату FBX.",
                        "sql": "SELECT ROUND(AVG(size_mb), 2) AS avg_fbx_size_mb FROM model_file WHERE format = 'FBX';"
                    },
                    {
                        "num": "4.1.5",
                        "title": "Середня сума оплаченого кошика покупця",
                        "desc": "Розрахунок середнього чеку успішної транзакції (status = Completed).",
                        "sql": "SELECT ROUND(AVG(total_amount), 2) AS avg_order_amount FROM cart WHERE status = 'Completed';"
                    }
                ]
            },
            {
                "sub_id": "4.2",
                "cmd_name": "Функція SUM()",
                "desc": "Обчислення сум замовлень, дискового простору та формул (5 комбінацій)",
                "queries": [
                    {
                        "num": "4.2.1",
                        "title": "Загальна сума виручки за сплаченими кошиками",
                        "desc": "Фінансовий підсумок обсягу продажів для статусів Completed.",
                        "sql": "SELECT SUM(total_amount) AS total_revenue FROM cart WHERE status = 'Completed';"
                    },
                    {
                        "num": "4.2.2",
                        "title": "Сумарний дисковий обсяг сховища файлів (МБ)",
                        "desc": "Розрахунок загального простору на сервері, зайнятого файлами моделей.",
                        "sql": "SELECT ROUND(SUM(size_mb), 2) AS total_storage_mb FROM model_file;"
                    },
                    {
                        "num": "4.2.3",
                        "title": "Сумарна кількість полігонів усіх моделей",
                        "desc": "Загальне навантаження геометрії всього каталогу.",
                        "sql": "SELECT SUM(polygon_count) AS total_polygons FROM model_3d;"
                    },
                    {
                        "num": "4.2.4",
                        "title": "Сумарна вартість робіт автора з id=1",
                        "desc": "Підсумок сумарної вартості каталогу конкретного 3D-художника.",
                        "sql": "SELECT SUM(price) AS seller1_total_price FROM model_3d WHERE id_seller = 1;"
                    },
                    {
                        "num": "4.2.5",
                        "title": "Сума комісії платформи (15%) за продажами",
                        "desc": "Розрахунок доходу платформи як суми виразу (total_amount * 0.15).",
                        "sql": "SELECT ROUND(SUM(total_amount * 0.15), 2) AS platform_commission FROM cart WHERE status = 'Completed';"
                    }
                ]
            },
            {
                "sub_id": "4.3",
                "cmd_name": "Функція MIN()",
                "desc": "Визначення мінімальних числових, розмірних та датових значень (5 комбінацій)",
                "queries": [
                    {
                        "num": "4.3.1",
                        "title": "Мінімальна ціна 3D-моделі у каталозі",
                        "desc": "Знаходження найдоступнішого товару на маркетплейсі.",
                        "sql": "SELECT MIN(price) AS min_model_price FROM model_3d;"
                    },
                    {
                        "num": "4.3.2",
                        "title": "Найменший розмір файлу серед моделей",
                        "desc": "Визначення мінімального обсягу завантажуваного 3D-файлу.",
                        "sql": "SELECT MIN(size_mb) AS min_file_size_mb FROM model_file;"
                    },
                    {
                        "num": "4.3.3",
                        "title": "Найперша дата реєстрації покупця",
                        "desc": "Визначення моменту появи найпершого користувача в базі даних.",
                        "sql": "SELECT MIN(registration_date) AS earliest_registration FROM buyer;"
                    },
                    {
                        "num": "4.3.4",
                        "title": "Мінімальний рейтинг серед авторів",
                        "desc": "Визначення найнижчої оцінки активного продавця.",
                        "sql": "SELECT MIN(rating) AS lowest_seller_rating FROM seller;"
                    },
                    {
                        "num": "4.3.5",
                        "title": "Мінімальна кількість полігонів серед текстурованих робіт",
                        "desc": "Пошук найбільш оптимізованої low-poly моделі з текстурами.",
                        "sql": "SELECT MIN(polygon_count) AS min_textured_polygons FROM model_3d WHERE has_texture = 'Yes';"
                    }
                ]
            },
            {
                "sub_id": "4.4",
                "cmd_name": "Функція MAX()",
                "desc": "Визначення максимальних числових, розмірних та датових значень (5 комбінацій)",
                "queries": [
                    {
                        "num": "4.4.1",
                        "title": "Максимальна ціна 3D-моделі у каталозі",
                        "desc": "Знаходження найдорожчого професійного пакету на платформі.",
                        "sql": "SELECT MAX(price) AS max_model_price FROM model_3d;"
                    },
                    {
                        "num": "4.4.2",
                        "title": "Максимальна кількість полігонів моделі",
                        "desc": "Визначення найбільш деталізованого high-poly об'єкта.",
                        "sql": "SELECT MAX(polygon_count) AS max_polygons FROM model_3d;"
                    },
                    {
                        "num": "4.4.3",
                        "title": "Найбільший розмір файлу в сховищі",
                        "desc": "Визначення найважчого архіву серед усіх моделей.",
                        "sql": "SELECT MAX(size_mb) AS max_file_size_mb FROM model_file;"
                    },
                    {
                        "num": "4.4.4",
                        "title": "Найбільша сума замовлення у кошику",
                        "desc": "Визначення найбільшого чеку за одну транзакцію.",
                        "sql": "SELECT MAX(total_amount) AS max_cart_amount FROM cart;"
                    },
                    {
                        "num": "4.4.5",
                        "title": "Найновіша дата оформлення замовлення",
                        "desc": "Визначення дати останньої купівельної активності на маркетплейсі.",
                        "sql": "SELECT MAX(created_date) AS latest_order_date FROM cart;"
                    }
                ]
            },
            {
                "sub_id": "4.5",
                "cmd_name": "Функція COUNT()",
                "desc": "Підрахунок кількості рядків, унікальних записів та комплексні звіти (5 комбінацій)",
                "queries": [
                    {
                        "num": "4.5.1",
                        "title": "Загальна кількість моделей у каталозі (COUNT *)",
                        "desc": "Підрахунок сумарного числа 3D-моделей у системі.",
                        "sql": "SELECT COUNT(*) AS total_models FROM model_3d;"
                    },
                    {
                        "num": "4.5.2",
                        "title": "Кількість моделей із заповненим описом",
                        "desc": "Підрахунок непорожніх описів через COUNT(description).",
                        "sql": "SELECT COUNT(description) AS models_with_description FROM model_3d;"
                    },
                    {
                        "num": "4.5.3",
                        "title": "Кількість унікальних категорій з товарами",
                        "desc": "Підрахунок унікальних категорій через COUNT(DISTINCT id_category).",
                        "sql": "SELECT COUNT(DISTINCT id_category) AS active_categories_count FROM model_3d;"
                    },
                    {
                        "num": "4.5.4",
                        "title": "Кількість успішно завершених замовлень",
                        "desc": "Підрахунок кількості кошиків у статусі Completed.",
                        "sql": "SELECT COUNT(*) AS completed_orders_count FROM cart WHERE status = 'Completed';"
                    },
                    {
                        "num": "4.5.5",
                        "title": "Комплексний статистичний звіт каталогу",
                        "desc": "Одночасний розрахунок COUNT, MIN, MAX та середнього значення вартості.",
                        "sql": "SELECT COUNT(*) AS total_models, MIN(price) AS min_p, MAX(price) AS max_p, ROUND(AVG(price), 2) AS avg_p FROM model_3d;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 5,
        "title": "Завдання 5. Групування вибраних даних та фільтрація груп (GROUP BY, HAVING)",
        "subsections": [
            {
                "sub_id": "5.1",
                "cmd_name": "Оператор GROUP BY",
                "desc": "Групування за однією та декількома категоріями з сортуванням (3 комбінації)",
                "queries": [
                    {
                        "num": "5.1.1",
                        "title": "Кількість моделей та середня ціна за категоріями",
                        "desc": "Аналіз розподілу 3D-моделей за товарними напрямками.",
                        "sql": "SELECT id_category, COUNT(*) AS models_count, ROUND(AVG(price), 2) AS avg_price FROM model_3d GROUP BY id_category ORDER BY models_count DESC;"
                    },
                    {
                        "num": "5.1.2",
                        "title": "Розподіл файлів за форматами (кількість і обсяг)",
                        "desc": "Групування файлів сховища за розширеннями (FBX, OBJ, BLEND).",
                        "sql": "SELECT format, COUNT(*) AS files_count, ROUND(SUM(size_mb), 2) AS total_mb FROM model_file GROUP BY format;"
                    },
                    {
                        "num": "5.1.3",
                        "title": "Групування кошиків за статусами з фільтрацією WHERE",
                        "desc": "Групування замовлень із сумою понад 10 у.о. за їхнім статусом.",
                        "sql": "SELECT status, COUNT(*) AS orders_count, ROUND(SUM(total_amount), 2) AS sum_amount FROM cart WHERE total_amount > 10.00 GROUP BY status;"
                    }
                ]
            },
            {
                "sub_id": "5.2",
                "cmd_name": "Оператор HAVING",
                "desc": "Фільтрація сформованих груп за агрегатними умовами (3 комбінації)",
                "queries": [
                    {
                        "num": "5.2.1",
                        "title": "Статуси замовлень з сумарним оборотом понад 50 (HAVING)",
                        "desc": "Виділення статусів замовлень із сумарним фінансовим обсягом > 50 у.о.",
                        "sql": "SELECT status, COUNT(*) AS orders_count, ROUND(SUM(total_amount), 2) AS total_volume FROM cart GROUP BY status HAVING total_volume > 50.00;"
                    },
                    {
                        "num": "5.2.2",
                        "title": "Автори з двома і більше моделями (HAVING COUNT >= 2)",
                        "desc": "Виявлення постійних продавців маркетплейсу та оцінка вартості їхнього портфоліо.",
                        "sql": "SELECT id_seller, COUNT(*) AS models_created, ROUND(SUM(price), 2) AS total_catalog_value FROM model_3d GROUP BY id_seller HAVING COUNT(*) >= 2;"
                    },
                    {
                        "num": "5.2.3",
                        "title": "Категорії з високою середньою вартістю моделі (HAVING AVG >= 20)",
                        "desc": "Знаходження категорій преміум-сегменту з середнім чеком від 20 у.о.",
                        "sql": "SELECT id_category, COUNT(*) AS count_models, ROUND(AVG(price), 2) AS avg_cat_price FROM model_3d GROUP BY id_category HAVING avg_cat_price >= 20.00;"
                    }
                ]
            }
        ]
    },
    {
        "task_num": 6,
        "title": "Завдання 6. Створення та використання представлень (CREATE VIEW, SELECT FROM VIEW)",
        "subsections": [
            {
                "sub_id": "6.1",
                "cmd_name": "Команда VIEW",
                "desc": "Створення 2 представлень для збереження вибірок та вибірка з них (2 запити)",
                "queries": [
                    {
                        "num": "6.1.1",
                        "title": "Створення v_premium_models (вітрина преміальних моделей без JOIN)",
                        "desc": "Формування віртуальної вітрини 3D-моделей з ціною від 20 у.о. без об'єднання таблиць.",
                        "view_name": "v_premium_models",
                        "create_sql": """DROP VIEW IF EXISTS v_premium_models;\nCREATE VIEW v_premium_models AS\nSELECT id_model, name, price, polygon_count, has_texture\nFROM model_3d\nWHERE price >= 20.00;""",
                        "select_sql": "SELECT * FROM v_premium_models ORDER BY price DESC;"
                    },
                    {
                        "num": "6.1.2",
                        "title": "Створення v_top_sellers (топ-продавці за рейтингом без JOIN)",
                        "desc": "Формування віртуальної таблиці найрейтинговіших продавців маркетплейсу.",
                        "view_name": "v_top_sellers",
                        "create_sql": """DROP VIEW IF EXISTS v_top_sellers;\nCREATE VIEW v_top_sellers AS\nSELECT id_seller, nickname, rating\nFROM seller\nWHERE rating >= 4.80;""",
                        "select_sql": "SELECT * FROM v_top_sellers ORDER BY rating DESC;"
                    }
                ]
            }
        ]
    }
]

# Execute all queries and collect results
print("Executing all 79 queries...")
all_executed_data = []
total_q_count = 0

for t in all_tasks_def:
    t_obj = {"task_num": t["task_num"], "title": t["title"], "subsections": []}
    for sub in t["subsections"]:
        s_obj = {"sub_id": sub["sub_id"], "cmd_name": sub["cmd_name"], "desc": sub["desc"], "queries": []}
        for q in sub["queries"]:
            total_q_count += 1
            if "view_name" in q:
                # View query
                cursor.executescript(q["create_sql"])
                cursor.execute(q["select_sql"])
                rows = [dict(r) for r in cursor.fetchall()]
                s_obj["queries"].append({
                    "num": q["num"],
                    "title": q["title"],
                    "desc": q["desc"],
                    "view_name": q["view_name"],
                    "create_sql": q["create_sql"],
                    "select_sql": q["select_sql"],
                    "rows": rows
                })
            else:
                cursor.execute(q["sql"])
                rows = [dict(r) for r in cursor.fetchall()]
                s_obj["queries"].append({
                    "num": q["num"],
                    "title": q["title"],
                    "desc": q["desc"],
                    "sql": q["sql"],
                    "rows": rows
                })
        t_obj["subsections"].append(s_obj)
    all_executed_data.append(t_obj)

print(f"Executed total {total_q_count} queries successfully!")

with open(os.path.join(cache_dir, "all_79_results.json"), "w", encoding="utf-8") as f:
    json.dump(all_executed_data, f, ensure_ascii=False, indent=2)

print("Saved all_79_results.json successfully!")
