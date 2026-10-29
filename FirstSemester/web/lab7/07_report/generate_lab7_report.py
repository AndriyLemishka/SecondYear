# -*- coding: utf-8 -*-
"""
Майстер-генератор академічного звіту до Лабораторної роботи №7
з навчальної дисципліни «Технології веброзробки та дизайну»
Тема: «Проєктування та реалізація повноцінного лендингу»
Тема вебпроєкту: «Лендинг мережі швидкісних зарядних хабів для електромобілів «ChargeUA» (інформаційний помічник та агрегатор станцій)»

Студент: Лемішка Андрій Андрійович, група ПП-24
Викладач: к.т.н., доцент Юрчак Ірина Юріївна
Кафедра САПР, Національний університет «Львівська політехніка»
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab7"
REPORT_DIR = os.path.join(BASE_DIR, "07_report")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")
DOCX_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л7_ChargeUA.docx")
PDF_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л7_ChargeUA.pdf")

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def create_report():
    print("Ініціалізація документа Word...")
    doc = Document()

    # Встановлення полів документа (2 см з усіх боків за ДСТУ)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.79)

    def set_font(run, name="Times New Roman", size_pt=12, bold=False, italic=False, color_rgb=(0,0,0)):
        run.font.name = name
        run.font.size = Pt(size_pt)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = RGBColor(*color_rgb)

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, line_spacing=1.15):
        p = doc.add_paragraph()
        p.alignment = align
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.line_spacing = line_spacing
        if text:
            r = p.add_run(text)
            set_font(r, name="Times New Roman", size_pt=12)
        return p

    def add_heading1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(16)
        pf.space_after = Pt(6)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=14, bold=True, color_rgb=(0, 51, 102))
        return p

    def add_heading2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(12)
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=13, bold=True, color_rgb=(30, 41, 59))
        return p

    def add_heading3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(10)
        pf.space_after = Pt(3)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=12, bold=True, color_rgb=(51, 65, 85))
        return p

    def add_screenshot_figure(filename, caption, width_in=6.0):
        full_path = os.path.join(SCREENSHOTS_DIR, filename)
        if os.path.exists(full_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            p_img.paragraph_format.keep_with_next = True
            r_img = p_img.add_run()
            r_img.add_picture(full_path, width=Inches(width_in))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption)
            set_font(r_cap, name="Times New Roman", size_pt=10.5, italic=True, bold=True, color_rgb=(70, 70, 70))
        else:
            print(f"Попередження: файл {filename} не знайдено!")

    # =========================================================================
    # ТИТУЛЬНИЙ ЛИСТ (АКАДЕМІЧНИЙ СТАНДАРТ КАФЕДРИ САПР)
    # =========================================================================
    print("Формування титульної сторінки...")
    p = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], size_pt=11, bold=True)

    p = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], size_pt=11, bold=True)

    p = add_p("Кафедра систем автоматизованого проєктування", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=8, line_spacing=1.0)
    set_font(p.runs[0], size_pt=11)

    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(8)
        r_logo = p_logo.add_run()
        r_logo.add_picture(coat_path, width=Inches(2.0))

    p = add_p("ЗВІТ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=2, line_spacing=1.0)
    set_font(p.runs[0], size_pt=16, bold=True)

    p = add_p("до лабораторної роботи №7", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0)
    set_font(p.runs[0], size_pt=13, bold=True)

    p = add_p("з навчальної дисципліни «Технології веброзробки та дизайну»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12, italic=True)

    p = add_p("Тема: «Проєктування та реалізація повноцінного лендингу»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=6, line_spacing=1.1)
    set_font(p.runs[0], size_pt=13, bold=True)

    p_spec = add_p("Специфікація проєкту: вебагрегатор та інформаційний помічник швидкісних зарядних станцій електромобілів «ChargeUA» (каталог хабів, моніторинг живих статусів у блекаути, без транзакцій та бронювань)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=24, line_spacing=1.0)
    set_font(p_spec.runs[0], size_pt=10.5, italic=True)

    # Таблиця авторів
    tbl_auth = doc.add_table(rows=1, cols=2)
    tbl_auth.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_left, c_right = tbl_auth.rows[0].cells
    c_left.width = Inches(3.2)
    c_right.width = Inches(3.3)

    p_r = c_right.paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_r.paragraph_format.line_spacing = 1.15
    r = p_r.add_run("Виконав:\n")
    set_font(r, size_pt=11)
    r = p_r.add_run("студент групи ПП-24\n")
    set_font(r, size_pt=11)
    r = p_r.add_run("Лемішка Андрій Андрійович\n\n")
    set_font(r, size_pt=11, bold=True)
    r = p_r.add_run("Прийняла:\n")
    set_font(r, size_pt=11)
    r = p_r.add_run("к.т.н., доцент кафедри САПР\n")
    set_font(r, size_pt=11)
    r = p_r.add_run("Юрчак Ірина Юріївна\n\n")
    set_font(r, size_pt=11, bold=True)
    r = p_r.add_run("Оцінка: _____________\n")
    set_font(r, size_pt=11)
    r = p_r.add_run("Підпис: _____________")
    set_font(r, size_pt=11)

    p_city = add_p("Львів — 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=36, space_after=0)
    set_font(p_city.runs[0], size_pt=11)

    doc.add_page_break()

    # =========================================================================
    # РОЗДІЛ 1. МЕТА РОБОТИ ТА ОПИС ПРОЄКТУ
    # =========================================================================
    add_heading1("1. Мета роботи та опис проєкту")
    
    p = add_p(space_before=4, space_after=6)
    p.add_run("Мета роботи: ").bold = True
    p.add_run("Оволодіти практичними навичками проєктування та автоматизованого збирання робочого, цілісного та адаптивного "
              "Landing Page на основі компонентної бази попередніх лабораторних робіт (ЛР №2–6). Навчитися застосовувати методологію "
              "ітераційного промптингу (Iterative Prompting), точкового рефакторингу виділених елементів (Pick Element), "
              "безпечного та адаптивного ембедингу мультимедійних активів (YouTube, Google Maps) та динамічних інформерів згідно "
              "з міжнародними стандартами доступності WCAG та рекомендаціями W3C.")

    p = add_p(space_before=4, space_after=4)
    p.add_run("Опис вебпроєкту «ChargeUA»:").bold = True
    
    p = add_p(space_before=2, space_after=3)
    p.add_run("• Тематика проєкту: ").bold = True
    p.add_run("Національний вебагрегатор та відкритий інформаційний помічник зарядної інфраструктури для електромобілів в Україні «ChargeUA».")

    p = add_p(space_before=2, space_after=3)
    p.add_run("• Цільова аудиторія (ЦА): ").bold = True
    p.add_run("Водії електромобілів (Tesla Model 3/Y, Volkswagen ID.4, Nissan Leaf, Hyundai Ioniq 5, китайські авто з портом GB/T), що здійснюють міські або міжміські поїздки в умовах дефіциту електроенергії, лімітів потужності та планових відключень світла.")

    p = add_p(space_before=2, space_after=3)
    p.add_run("• Цільова дія (Conversion Goal): ").bold = True
    p.add_run("Миттєва перевірка живого статусу («Вільний»/«Зайнятий») швидкісного роз'єму (120–150 кВт) на карті та побудова маршруту до найближчого автономного хабу з дизель-генератором.")

    p = add_p(space_before=2, space_after=6)
    p.add_run("• Архітектурне бізнес-правило: ").bold = True
    p.add_run("ChargeUA функціонує виключно як безкоштовний суспільний навігатор і телеметричний агрегатор. На сайті категорично відсутні будь-які форми оплати, білінгові системи, банківські реквізити, кошики покупок чи платні бронювання конекторів.")

    p = add_p(space_before=4, space_after=6)
    p.add_run("Посилання на опублікований реліз проєкту: ").bold = True
    r_link = p.add_run("https://chargeua-landing.netlify.app/")
    set_font(r_link, color_rgb=(0, 102, 204), bold=True)

    # =========================================================================
    # РОЗДІЛ 2. СТРУКТУРА ЛЕНДИНГУ ТА КАРТА СЕКЦІЙ
    # =========================================================================
    add_heading1("2. Структура лендингу та інформаційна архітектура")
    p = add_p(space_before=2, space_after=6)
    p.add_run("Згідно з методичними вказівками до Лабораторної роботи №7, повноцінний лендинг формується на базі логічного ланцюжка блоків, спрямованих на поступове проведення відвідувача від первинного знайомства до цільової дії.")

    # Таблиця структури
    headers = ["№", "Секція", "Семантичний тег", "Призначення та мета блоку", "Основний елемент дії (CTA)"]
    rows = [
        ["1", "Шапка (Header)", "<header>, <nav>", "Брендинг, навігація між розділами та адаптивне гамбургер-меню для смартфонів.", "Кнопка «Вільні хаби»"],
        ["2", "Головний екран (Hero)", "<section id='hero'>", "Заголовок H1, підзаголовок ціннісної пропозиції, бейджи переваг та візуальний інтерактивний блок хабу.", "Кнопка «Знайти найближчий хаб»"],
        ["3", "Про проєкт (About)", "<section id='about'>", "Позиціонування сервісу як некомерційного помічника без оплат і реєстрацій.", "Інформаційне ознайомлення"],
        ["4", "Переваги (Benefits)", "<section id='benefits'>", "3 ключові тези: стійкість до блекаутів (ДГ), потужність DC 120-150 кВт та відкритий моніторинг кожні 30 с.", "Картки з іконками FontAwesome"],
        ["5", "Каталог хабів (Hubs)", "<section id='hubs'>", "Адаптивна CSS Grid-сітка карток станцій (Київ, Львів, Одеса) з індикацією живих статусів портів.", "Кнопки «Показати на карті»"],
        ["6", "Мультимедіа Відео", "<section id='video'>", "Адаптивне відеоінструктування (YouTube embed) у семантичному контейнері aspect-ratio 16:9.", "Перегляд відеоінструкції"],
        ["7", "Динамічний віджет", "<aside aria-label='...'>", "Інформер погоди Львова (+14°C) та стійкості мережі (100% хабів на лінії, 72 год резерву ДГ).", "Інформаційна телеметрія"],
        ["8", "Інтерактивна карта", "<section id='map'>", "Вбудована адаптивна карта Google Maps з точним географічним розташуванням хабу.", "Прокладання маршруту"],
        ["9", "Відгуки (Reviews)", "<section id='reviews'>", "Соціальні докази: відгуки реальних власників авто з міст Київ, Львів, Одеса.", "Картки відгуків з рейтингом 5/5"],
        ["10", "Заклик до дії (CTA)", "<section id='cta'>", "Фінальний конверсійний блок з градієнтним фоном для переходу до пошуку на карті.", "Кнопка «Відкрити карту хабів»"],
        ["11", "Підвал (Footer)", "<footer>, <address>", "4-колонкова структура: Про сервіс, швидка навігація, правова інформація, служба підтримки.", "Контакти, телефон, Telegram"]
    ]
    
    tbl = doc.add_table(rows=len(rows)+1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Стилізація шапки
    for i, h in enumerate(headers):
        cell = tbl.rows[0].cells[i]
        cell.text = h
        set_cell_background(cell, "003366")
        set_cell_margins(cell, top=120, bottom=120, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], size_pt=9.5, bold=True, color_rgb=(255,255,255))
    
    for r_idx, r_data in enumerate(rows):
        row = tbl.rows[r_idx+1]
        bg = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p.runs[0], size_pt=9, bold=(c_idx==1))

    # =========================================================================
    # РОЗДІЛ 3. ТЕКСТ MASTER PROMPT ТА СИСТЕМНИЙ ПРОМПТИНГ
    # =========================================================================
    add_heading1("3. Текст Master Prompt та архітектура інженерного запиту")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Згідно з методичними вимогами, розробка повноцінного лендингу базується на формулі системного контекстного проєктування: ")
    p.add_run("Роль → Тематика → Структура → Стилістика → Обмеження.").bold = True

    p = add_p(space_before=2, space_after=4)
    p.add_run("Повний текст Master Prompt, надісланий у ШІ-середовище (Google Gemini / ChatGPT):").italic = True

    # Блок коду / цитата
    tbl_prompt = doc.add_table(rows=1, cols=1)
    tbl_prompt.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl_prompt.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    prompt_text = (
        "Ти — Senior Frontend Developer та UI/UX Engineer.\n"
        "Створи повноцінний адаптивний Landing Page для українського вебпроєкту «ChargeUA» (веб-помічник та агрегатор швидкісних зарядних станцій електромобілів в Україні).\n\n"
        "Специфікація та бізнес-правило:\n"
        "ChargeUA є безкоштовним інформаційним довідником і агрегатором станцій (пошук та моніторинг живих статусів у блекаути). Жодних фінансових транзакцій, оплат, кошиків чи бронювання конекторів.\n\n"
        "Структура лендингу згідно з методичкою:\n"
        "1. Шапка (Header) — логотип ChargeUA, навігація (десктоп горизонтальна, на мобільних бургер), кнопка швидкого пошуку найближчої станції.\n"
        "2. Головний екран (Hero-секція) — заголовок H1, підзаголовок з ціннісною пропозицією, чітка кнопка CTA («Знайти зарядку»), бейджи швидких переваг (150 кВт, 24/7).\n"
        "3. Переваги (Benefits) — картки ключових переваг: моніторинг енергопостачання та генераторів, живі статуси портів CCS2/CHAdeMO/GBT, точні тарифи.\n"
        "4. Каталог станцій (Services / Hubs) — адаптивна сітка карток міських зарядних комплексів (Київ, Львів, Одеса) з живими статусами портів («Вільний» / «Зайнятий»).\n"
        "5. Відгуки (Testimonials) — соціальні докази та цитати реальних власників електрокарів.\n"
        "6. Фінальний CTA-блок — конверсійний блок заклику скористатися картою та знайти вільний порт.\n"
        "7. Підвал (Footer) — семантичний футер: навігація, служба цілодобової підтримки, копірайт.\n\n"
        "Технічні вимоги:\n"
        "- Семантичний HTML5 (<header>, <nav>, <main>, <section>, <article>, <footer>).\n"
        "- Стилізація виключно через Tailwind CSS (utility-first) за принципом Mobile-First.\n"
        "- Палітра: Primary Blue (#2563EB / bg-blue-600), Dark Slate (#0F172A / bg-slate-900), Neutral Slate (#F8FAFC / bg-slate-50).\n"
        "- Доступність (a11y): контрастність кольорів, атрибути aria-label для кнопок, правильна ієрархія заголовків H1-H3.\n"
        "- Повністю адаптивний каркас (grid-cols-1 md:grid-cols-2 lg:grid-cols-3).\n\n"
        "Згенеруй чистий, валідний HTML-код сторінки та коротко опиши застосовані інженерні рішення."
    )
    p_pr = cell.paragraphs[0]
    p_pr.paragraph_format.line_spacing = 1.05
    r = p_pr.add_run(prompt_text)
    set_font(r, name="Courier New", size_pt=9.0, color_rgb=(15, 23, 42))

    # =========================================================================
    # РОЗДІЛ 4. ПОКРОКОВИЙ ХІД РОБОТИ ТА ІТЕРАЦІЙНИЙ ПРОМПТИНГ
    # =========================================================================
    add_heading1("4. Покроковий хід виконання роботи")

    add_heading2("Етап 1. Підготовка проєкту та матеріалів ЛР №2–6")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Для розробки лендингу використано раніше створені та затверджені активи: контент-стратегію та тексти з ЛР №2, векторний логотип Logo.svg та іконки з ЛР №3, колірну дизайн-систему з ЛР №4, семантичну структуру каркасу з ЛР №5 та адаптивні компоненти Tailwind з ЛР №6.")
    add_screenshot_figure("00_vscode_environment.png", "Рис. 1. Етап 1: Робоче середовище VS Code, компонентна структура лендингу ChargeUA та конфігурація Tailwind")

    add_heading2("Етап 2 та 3. Системний промптинг та генерація базового каркасу")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Взаємодія з ШІ здійснювалася через веб-інтерфейс Google Gemini та ChatGPT безпосередньо у браузері з веденням живого логу.")
    add_screenshot_figure("00_gemini_environment.png", "Рис. 2. Етап 3: Сесія генерації лендингу ChargeUA в середовищі ШІ-асистента Google Gemini")
    add_screenshot_figure("01_gemini_master_prompt_response.png", "Рис. 3. Етап 4: Генерація базової семантичної структури лендингу за результатами Master Prompt")

    add_heading2("Етап 5. Ітераційне вдосконалення (Iterative Prompting)")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Відповідно до методики ітераційного циклу, сторінка доопрацьовувалася 5 послідовними кроками:")

    p = add_p(space_before=2, space_after=2)
    p.add_run("• Ітерація 2 (Корекція Hero-секції): ").bold = True
    p.add_run("Оптимізація візуальної ієрархії: H1 став домінуючим елементом, підзаголовок чітко розкриває цінність, впроваджено двоколонкову сітку на десктопі (md:grid-cols-2) та вертикальний стек на мобільних.")
    add_screenshot_figure("02_gemini_iteration2_hero.png", "Рис. 4. Ітерація 2: Рефакторинг Hero-секції та налаштування двоколонкової розмітки")

    p = add_p(space_before=4, space_after=2)
    p.add_run("• Ітерація 3 (Уставляння реального контенту): ").bold = True
    p.add_run("Повна ліквідація заглушок «Lorem Ipsum». Впроваджено реальні характеристики хабів Києва, Львова та Одеси, точні тарифи та цитати реальних власників електрокарів.")
    add_screenshot_figure("03_gemini_iteration3_real_content.png", "Рис. 5. Ітерація 3: Інтеграція затвердженого контенту та відгуків водіїв з ЛР №2")

    p = add_p(space_before=4, space_after=2)
    p.add_run("• Ітерація 4 (Корекція дизайну відповідно до ЛР №4): ").bold = True
    p.add_run("ШІ провів строгий аудит кольорів (#2563EB, slate-900), радіусів (rounded-2xl) та тіней без створення зайвих стилів.")
    add_screenshot_figure("04_gemini_iteration4_design_audit.png", "Рис. 6. Ітерація 4: Результати дизайн-аудиту узгодженості зі стилістикою проєкту")

    p = add_p(space_before=4, space_after=2)
    p.add_run("• Ітерація 5 (Корекція адаптивності): ").bold = True
    p.add_run("Складання матриці брейкпоінтів та усунення потенційного горизонтального скролу на вузьких смартфонах (320px–375px).")
    add_screenshot_figure("05_gemini_iteration5_responsiveness.png", "Рис. 7. Ітерація 5: Таблиця аудиту адаптивності для брейкпоінтів від 320px до 1440px")

    add_heading2("Етап 6. Метод точкового рефакторингу Pick Element")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Метод Pick Element застосовано до головної кнопки CTA «Знайти найближчий хаб» та відступів Hero-секції. ШІ було суворо обмежено лише цим компонентом, що дозволило зменшити мобільні відступи до py-12 (md:py-24), забезпечити мінімальну ергономічну висоту кнопки min-h-[48px] та додати мікровзаємодії (hover:-translate-y-0.5, focus:ring-4) без використання JavaScript.")
    add_screenshot_figure("06_gemini_pick_element.png", "Рис. 8. Етап 6: Точковий рефакторинг CTA-кнопки та впровадження мікровзаємодій методом Pick Element")

    add_heading2("Етап 7. Інтеграція мультимедійних активів та сторонніх сервісів")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Згідно з методичкою, реалізовано 3 обов'язкові інтеграції:")
    p.add_run("\n1. YouTube Video Embed: вбудовано офіційну відеоінструкцію з використанням безпечного хостингу youtube-nocookie.com, обов'язковими атрибутами loading='lazy', title та адаптивним контейнером aspect-ratio: 16/9.")
    p.add_run("\n2. Google Maps Embed: інтерактивна карта розташування хабу у Львові (вул. Стрийська, 202) з loading='lazy', referrerpolicy='no-referrer-when-downgrade' та повною мобільною адаптивністю.")
    p.add_run("\n3. Динамічний віджет-інформер: загорнутий у семантичний тег <aside> (температура Львова +14°C та статус готовності 100% хабів на лінії).")
    add_screenshot_figure("07_gemini_multimedia_integration.png", "Рис. 9. Етап 7: Семантичний код інтеграції YouTube, Google Maps та інформера")

    # =========================================================================
    # РОЗДІЛ 5. РЕЗУЛЬТАТИ ВЕРСТКИ ТА ТЕСТУВАННЯ В БРАУЗЕРІ
    # =========================================================================
    add_heading1("5. Результати тестування верстки та візуальні артефакти")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Фінальний лендинг ChargeUA протестовано у Chrome DevTools на десктопних моніторах (1280px), планшетах (768px) та мобільних пристроях (375px iPhone SE). Перевірено працездатність усіх медіа-вбудовувань.")

    add_screenshot_figure("08_desktop_hero.png", "Рис. 10. Десктопний вигляд Hero-секції лендингу ChargeUA (роздільна здатність 1280x800)")
    add_screenshot_figure("13_desktop_video_embed.png", "Рис. 11. Працездатність адаптивного відеоплеєра YouTube (aspect-ratio 16:9) на десктопі")
    add_screenshot_figure("14_desktop_map_embed.png", "Рис. 12. Працездатність вбудованої інтерактивної карти Google Maps та інформера мережі")
    add_screenshot_figure("10_mobile_hero_375px.png", "Рис. 13. Мобільна версія Hero-секції (375px): складання колонок у вертикальний стек та адаптивні CTA")
    add_screenshot_figure("11_mobile_video_embed.png", "Рис. 14. Мобільна версія секції відео: адаптивний плеєр без порушення меж екрану")
    add_screenshot_figure("12_mobile_map_embed.png", "Рис. 15. Мобільна версія інтерактивної карти Google Maps та погодного інформера")

    # Результати аудиту
    add_heading2("Результати аудиту Google Lighthouse")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Комплексна перевірка сторінки через Google Lighthouse показала найвищі стандарти якості та доступності:")
    p.add_run("\n• Best Practices: 100/100 (абсолютне дотримання безпеки, відсутність вразливих API, коректні заголовки);")
    p.add_run("\n• Accessibility (Доступність): 96/100 (повна сумісність з екранними читцями WAI-ARIA, високий контраст тексту);")
    p.add_run("\n• SEO: 80/100 (наявність мета-тегів опису, канонічного посилання, robots та коректна ієрархія H1–H3).")

    # =========================================================================
    # РОЗДІЛ 6. ЛІСТИНГ КЛЮЧОВИХ БЛОКІВ КОДУ
    # =========================================================================
    add_heading1("6. Лістинг фінального коду лендингу index.html")
    p = add_p(space_before=2, space_after=4)
    p.add_run("Нижче наведено лістинг семантичних блоків медіаінтеграцій та рефакторингу з коментарями:")

    code_snippet = (
        "<!-- МУЛЬТИМЕДІА: АДАПТИВНИЙ YOUTUBE EMBED (ASPECT-RATIO 16/9 + LOADING LAZY) -->\n"
        "<section id=\"video\" class=\"py-16 md:py-24 bg-slate-900 text-white\" aria-labelledby=\"video-heading\">\n"
        "  <div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\">\n"
        "    <div class=\"media-video-container border border-slate-700/80\">\n"
        "      <iframe \n"
        "        src=\"https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?rel=0&modestbranding=1\" \n"
        "        title=\"Відеоінструкція: як заряджати електромобіль на швидкісних хабах ChargeUA\"\n"
        "        loading=\"lazy\" \n"
        "        allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"\n"
        "        allowfullscreen \n"
        "        class=\"w-full h-full border-0\">\n"
        "      </iframe>\n"
        "    </div>\n"
        "  </div>\n"
        "</section>\n\n"
        "<!-- ДИНАМІЧНИЙ ВІДЖЕТ-ІНФОРМЕР (СЕМАНТИЧНИЙ ТЕГ <ASIDE>) -->\n"
        "<aside class=\"bg-gradient-to-r from-blue-900 via-slate-900 to-slate-800 text-white p-6 rounded-2xl shadow-xl\"\n"
        "       aria-label=\"Оперативний статус енергосистеми та погоди\">\n"
        "  <div class=\"flex items-center gap-5\">\n"
        "    <div class=\"w-14 h-14 rounded-2xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-2xl\">\n"
        "      <i class=\"fa-solid fa-temperature-half\" aria-hidden=\"true\"></i>\n"
        "    </div>\n"
        "    <div>\n"
        "      <p class=\"text-xs uppercase font-extrabold text-blue-300\">Метеостанція хабів · Львів</p>\n"
        "      <p class=\"text-xl font-extrabold text-white\">+14°C · Сухо, без опадів</p>\n"
        "    </div>\n"
        "  </div>\n"
        "</aside>\n\n"
        "<!-- МУЛЬТИМЕДІА: АДАПТИВНА КАРТА GOOGLE MAPS З БЕЗПЕЧНИМ REFERRER -->\n"
        "<section id=\"map\" class=\"py-16 md:py-24 bg-white\" aria-labelledby=\"map-heading\">\n"
        "  <div class=\"media-map-container\">\n"
        "    <iframe \n"
        "      src=\"https://www.google.com/maps/embed?pb=...\" \n"
        "      title=\"Інтерактивна карта розташування хабів ChargeUA\" \n"
        "      loading=\"lazy\" \n"
        "      referrerpolicy=\"no-referrer-when-downgrade\" \n"
        "      allowfullscreen \n"
        "      class=\"w-full h-full border-0\">\n"
        "    </iframe>\n"
        "  </div>\n"
        "</section>"
    )
    tbl_code = doc.add_table(rows=1, cols=1)
    tbl_code.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl_code.rows[0].cells[0]
    c.width = Inches(6.5)
    set_cell_background(c, "F8FAFC")
    set_cell_margins(c, top=120, bottom=120, left=150, right=150)
    p = c.paragraphs[0]
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_snippet)
    set_font(r, name="Courier New", size_pt=8.5, color_rgb=(15, 23, 42))

    # =========================================================================
    # РОЗДІЛ 7. ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ
    # =========================================================================
    add_heading1("7. Відповіді на контрольні запитання")

    questions_answers = [
        (
            "1. В чому полягає суть методу «Ітераційного промптингу», який використовується в цій роботі, і яка його головна інженерна перевага?",
            "Суть методу полягає у поступовій, покроковій розробці вебінтерфейсу через послідовні уточнюючі запити замість одноразової спроби згенерувати весь сайт одним запитом. "
            "Головна інженерна перевага — повний контроль розробника над кодом, мінімізація «галюцинацій» ШІ, збереження існуючої дизайн-системи та можливість виявляти й виправляти помилки (наприклад, дефекти адаптивності чи семантики) на кожному окремому етапі."
        ),
        (
            "2. Пояснити суть методу точкового рефакторингу «Pick element». В яких ситуаціях його найдоцільніше використовувати?",
            "Метод Pick Element передбачає ізоляцію конкретного HTML-елемента чи компонента (наприклад, CTA-кнопки або відступів секції) та надання ШІ інструкції змінювати виключно цей фрагмент, не торкаючись решти структури сторінки. "
            "Його найдоцільніше використовувати під час тонкого тюнінгу (fine-tuning) мікровзаємодій, налаштування доступності (фокусні кільця), оптимізації мобільних відступів або виправлення локальних CSS-конфліктів без ризику зламати глобальну верстку."
        ),
        (
            "3. Що таке «ембединг» і який HTML-тег є основним інструментом для реалізації цієї технології на сторінці?",
            "Ембединг (embedding) — це технологія інтеграції стороннього інтерактивного контенту, медіаресурсів або функціональних віджетів безпосередньо у вебсторінку без необхідності зберігати сам ресурс на власному сервері. "
            "Основним інструментом реалізації ембедингу є HTML-тег <iframe> (Inline Frame), який створює вкладений браузерний контекст для відображення зовнішнього документа."
        ),
        (
            "4. Чому скопійований «з коробки» код <iframe> від YouTube чи Google Maps може зламати адаптивну верстку сайту, і як розробник має це виправити згідно з промптами до роботи?",
            "За замовчуванням сторонні сервіси генерують тег <iframe> із жорстко прописаними фіксованими піксельними атрибутами width=\"560\" та height=\"315\". На екранах смартфонів (шириною 320–375px) такий фрейм виходить за межі в'юпорту, спричиняючи небажаний горизонтальний скрол та руйнуючи адаптивну сітку. "
            "Розробник виправляє це видаленням фіксованих розмірів та застосуванням адаптивного контейнера з класами Tailwind w-full aspect-video (або CSS-властивістю aspect-ratio: 16/9 у зовнішньому файлі стилів)."
        ),
        (
            "5. З якою метою в промптах для ШІ до карт та відео додається вимога прописати атрибути title та loading=\"lazy\"?",
            "Атрибут title є обов'язковим за стандартом доступності WCAG (WAI-ARIA) — він озвучується екранними читцями для користувачів з вадами зору, пояснюючи вміст фрейму до його завантаження. "
            "Атрибут loading=\"lazy\" вмикає нативне ліниве завантаження браузера: фрейм починає завантажуватися лише тоді, коли користувач доскролює до нього, що колосально економить трафік, прискорює First Contentful Paint (FCP) та підвищує бал продуктивності у Google Lighthouse."
        ),
        (
            "6. Яку логічну структуру та послідовність блоків повинен мати повноцінний лендинг?",
            "Повноцінний лендинг будується за класичною маркетингово-інженерною моделлю AIDA: 1) Шапка (Header) з брендингом та навігацією; 2) Hero-секція з УТП (унікальною ціннісною пропозицією), заголовком H1 та першим CTA; 3) Секція «Про проєкт / Як це працює»; 4) Переваги продукту (Benefits); 5) Каталог послуг / товарів (Services / Hubs); 6) Мультимедійна демонстрація (відео / інтерактивна карта); 7) Соціальні докази (відгуки, цифри, сертифікати); 8) Фінальний конверсійний CTA-блок; 9) Підвал (Footer) з юридичною інформацією та контактами підтримки."
        ),
        (
            "7. В який семантичний тег згідно з системними промптами інструкції рекомендується загортати динамічні інформери (погоди/валют) сайдбару і чому?",
            "Динамічні інформери рекомендується загортати у семантичний HTML5-тег <aside> (з атрибутом aria-label). Цей тег позначає додатковий, дотичний контент, який не є основною інформацією документа, проте надає користувачеві корисний контекст (наприклад, стан енергомережі чи погоду для батареї електрокара), що сприяє правильному SEO-індексуванню пошуковими роботами."
        ),
        (
            "8. Якщо інформер погоди підключається не через <iframe>, а через зовнішній JavaScript-код, які атрибути тегу <script> варто використати і навіщо?",
            "Слід обов'язково використовувати атрибути defer або async: "
            "1) defer завантажує скрипт у фоні паралельно з парсингом HTML і виконує його лише після повної побудови DOM-дерева, гарантуючи збереження порядку виконання без блокування інтерфейсу; "
            "2) async виконує скрипт одразу після завантаження незалежно від парсингу, що підходить для цілком незалежних лічильників чи аналітики. Це усуває проблему блокування рендерингу (Render-blocking resources)."
        ),
        (
            "9. Як в стилістиці вашої сторінки поєднуються Tailwind CSS та нативні CSS-змінні в :root?",
            "Tailwind CSS використовується для швидкого компонування адаптивної структури, просторових відступів (p-*, m-*), гнучких сіток (flex, grid) та станів (hover, focus). "
            "Нативні CSS-змінні в блоці :root файлу style.css (--video-max-width: 960px, --video-radius: 1rem, брендові токени) служать централізованим джерелом правди для специфічних параметрів компонентів, що спрощує глобальну підтримку сайту та дозволяє перевикористовувати правила в кастомних класах."
        ),
        (
            "10. Як за допомогою Tailwind CSS налаштувати кнопки для підвищення конверсії сторінки?",
            "Для максимізації конверсії кнопкам задано: 1) Високий контраст та акцентний колір (bg-blue-600 hover:bg-blue-700 text-white); 2) Оптимальну сенсорну площу для мобільних пристроїв (w-full sm:w-auto min-h-[48px]); 3) Чіткі мікровзаємодії (hover:-translate-y-0.5 hover:shadow-lg transition-all duration-300); 4) Стан доступності для клавіатурного фокусу (focus:outline-none focus:ring-4 focus:ring-blue-300), що підвищує довіру та приємне відчуття відгуку інтерфейсу."
        ),
        (
            "11. Опишіть алгоритм ітераційного оновлення сайту на платформі Netlify, якщо перша версія проєкту вже була опублікована раніше.",
            "Алгоритм складається з таких кроків: 1) Авторизуватися у панелі керування Netlify; 2) Відкрити існуючий сайт у розділі Sites; 3) Перейти на вкладку Deploys; 4) У нижній частині сторінки знайти зону завантаження «Need to update your site? Drag and drop your site output folder here»; 5) Перетягнути оновлену локальну папку landing-project; 6) Netlify автоматично запустить атомарний деплой, оновить кеш CDN і перемкне продакшн-посилання на нову версію без простою сайту (zero downtime)."
        ),
        (
            "12. Що саме розробник має перевірити локально через «Live Server» перед тим, як завантажувати оновлення сайту на Netlify?",
            "Перед публікацією розробник зобов'язаний перевірити: 1) Відсутність помилок у консолі браузера (404 Not Found на картинки, скрипти, стилі); 2) Відносність усіх шляхів до файлів (шляхи не повинні починатися з абсолютних локальних дисків на кшталт D:/...); 3) Адаптивність макета в режимі Device Toolbar (відсутність горизонтального скролу на 320px, 375px, 768px); 4) Працездатність гамбургер-меню та всіх якорних посилань навігації; 5) Коректне завантаження вбудованих карт та відео без блокування браузером через змішаний контент (Mixed Content)."
        )
    ]

    for q, a in questions_answers:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(8)
        p_q.paragraph_format.space_after = Pt(2)
        p_q.paragraph_format.keep_with_next = True
        r_q = p_q.add_run(q)
        set_font(r_q, size_pt=11.5, bold=True, color_rgb=(0, 51, 102))

        p_a = doc.add_paragraph()
        p_a.paragraph_format.space_before = Pt(0)
        p_a.paragraph_format.space_after = Pt(6)
        p_a.paragraph_format.line_spacing = 1.15
        r_a = p_a.add_run(a)
        set_font(r_a, size_pt=11)

    # =========================================================================
    # РОЗДІЛ 8. ВИСНОВКИ
    # =========================================================================
    add_heading1("8. Висновки")
    p = add_p(space_before=4, space_after=6)
    p.add_run("Під час виконання Лабораторної роботи №7 досягнуто таких інженерних та практичних результатів:\n\n"
              "1. Проєктування цілісного лендингу: Усі окремі UI-компоненти, створені на попередніх етапах (ЛР №2–6), "
              "успішно інтегровано в єдиний, логічно структурований інформаційний Landing Page вебпроєкту «ChargeUA», "
              "який суворо дотримується бізнес-правила безкоштовного агрегатора швидкісних комплексів без оплат і бронювань.\n\n"
              "2. Ефективність ітераційного промптингу: Застосування 5-крокового циклу ітераційного промптингу та системного "
              "Master Prompt (Роль → Тематика → Структура → Стилістика → Обмеження) дозволило уникнути галюцинацій ШІ та сформувати "
              "чистий семантичний HTML5-код з високим рівнем людиночитаності та структурованості.\n\n"
              "3. Практика точкового рефакторингу Pick Element: Методика фокусування на виділених блоках дозволила ізольовано "
              "відкалібрувати розміри та мікровзаємодії головної кнопки CTA (min-h-[48px], hover:-translate-y-0.5, focus:ring-4) "
              "та оптимізувати вертикальні відступи секцій на мобільних екранах (py-12 vs md:py-24) без ризику деградації глобального макета.\n\n"
              "4. Безпечний та адаптивний ембединг мультимедіа: Успішно впроваджено інтерактивну карту Google Maps та відеоінструкцію YouTube "
              "з використанням сучасних контейнерів aspect-ratio: 16/9, обов'язкових атрибутів лінивого завантаження loading='lazy', "
              "політики захисту referrerpolicy='no-referrer-when-downgrade' та тегів доступності title, а також семантичного інформера в тегу <aside>.\n\n"
              "5. Контроль якості та доступності: Проєкт успішно пройшов комплексне тестування адаптивності на розмірах від 320px до 1440px, "
              "а в аудиті Google Lighthouse показав найвищі результати: 100/100 у категорії Best Practices та 96/100 у категорії Accessibility.")

    # Збереження DOCX
    print(f"Збереження звіту в DOCX: {DOCX_OUT}")
    doc.save(DOCX_OUT)
    print("DOCX успішно збережено!")

    # Конвертація в PDF через Word COM
    print(f"Конвертація в PDF через Word COM: {PDF_OUT}")
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc_com = word.Documents.Open(os.path.abspath(DOCX_OUT))
        doc_com.SaveAs(os.path.abspath(PDF_OUT), FileFormat=17) # 17 = wdFormatPDF
        doc_com.Close()
        word.Quit()
        print(f"PDF успішно створено: {PDF_OUT}")
    except Exception as e:
        print(f"Помилка при створенні PDF через COM: {e}")

if __name__ == "__main__":
    create_report()
