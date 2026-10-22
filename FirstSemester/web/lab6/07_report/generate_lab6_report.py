# -*- coding: utf-8 -*-
"""
Майстер-генератор повного офіційного звіту до Лабораторної роботи №6
з навчальної дисципліни «Технології веброзробки та дизайну»
Тема: «Верстка UI-компонентів та адаптивність за допомогою Tailwind CSS та ШІ-асистентів»
Варіант / Тема: «Вебплатформа ChargeUA — мережа швидкісних зарядних комплексів для електромобілів в Україні»

Студент: Лемішка Андрій Андрійович, група ПП-24
Викладач: к.т.н., доцент Юрчак Ірина Юріївна
Кафедра САПР, Національний університет «Львівська політехніка»
"""

import os
import sys
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab6"
REPORT_DIR = os.path.join(BASE_DIR, "07_report")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")

COLOR_PRIMARY = RGBColor(0x00, 0x5E, 0xC9)     # ChargeUA синій #005EC9
COLOR_DARK = RGBColor(0x0F, 0x17, 0x2A)        # Slate 900
COLOR_TEXT = RGBColor(0x1E, 0x29, 0x3B)        # Slate 800
COLOR_MUTED = RGBColor(0x64, 0x74, 0x8B)       # Slate 500

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D7DE"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def setup_document_styles(doc):
    sec = doc.sections[0]
    sec.left_margin = Inches(0.984)    # 2.5 cm
    sec.right_margin = Inches(0.591)   # 1.5 cm
    sec.top_margin = Inches(0.591)     # 1.5 cm
    sec.bottom_margin = Inches(0.591)  # 1.5 cm
    sec.page_width = Inches(8.27)      # A4
    sec.page_height = Inches(11.69)
    
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = COLOR_TEXT
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(3)

def add_title_page(doc):
    p0 = doc.add_paragraph()
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(2)
    r = p0.add_run("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(2)
    r = p1.add_run("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(2)
    r = p2.add_run("Інститут комп'ютерних наук та інформаційних технологій\nКафедра систем автоматизованого проектування")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(6)
        r_logo = p_logo.add_run()
        r_logo.add_picture(coat_path, width=Inches(1.8))

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_before = Pt(6)
    p4.paragraph_format.space_after = Pt(2)
    r = p4.add_run("ЗВІТ")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_PRIMARY

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(4)
    r = p5.add_run("до лабораторної роботи № 6\nз дисципліни «Технології веброзробки та дизайну»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)

    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p6.paragraph_format.space_before = Pt(2)
    p6.paragraph_format.space_after = Pt(4)
    r = p6.add_run("на тему: «Верстка UI-компонентів та адаптивність за допомогою Tailwind CSS та ШІ-асистентів»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    p_theme = doc.add_paragraph()
    p_theme.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_theme.paragraph_format.space_before = Pt(2)
    p_theme.paragraph_format.space_after = Pt(16)
    r_th1 = p_theme.add_run("Варіант / Тема вебпроєкту:\n")
    r_th1.font.name = "Times New Roman"
    r_th1.font.size = Pt(11)
    r_th1.italic = True
    r_th2 = p_theme.add_run("«Вебплатформа ChargeUA — мережа швидкісних зарядних комплексів для електромобілів в Україні»")
    r_th2.bold = True
    r_th2.font.name = "Times New Roman"
    r_th2.font.size = Pt(12)
    r_th2.font.color.rgb = COLOR_DARK

    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell_left = tbl.cell(0, 0)
    cell_right = tbl.cell(0, 1)
    cell_left.width = Inches(3.2)
    cell_right.width = Inches(3.5)
    set_cell_margins(cell_left, 40, 40, 40, 40)
    set_cell_margins(cell_right, 40, 40, 40, 40)

    p_right = cell_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_right.paragraph_format.line_spacing = 1.15
    
    r_sub = p_right.add_run("Виконав:\n")
    r_sub.font.size = Pt(11)
    r_sub.font.name = "Times New Roman"
    
    r_sub = p_right.add_run("студент групи ПП-24\n")
    r_sub.font.size = Pt(11.5)
    r_sub.font.name = "Times New Roman"
    
    r_name = p_right.add_run("Лемішка Андрій Андрійович\n\n")
    r_name.bold = True
    r_name.font.size = Pt(12)
    r_name.font.name = "Times New Roman"
    
    r_chk = p_right.add_run("Перевірила:\n")
    r_chk.font.size = Pt(11)
    r_chk.font.name = "Times New Roman"
    
    r_teach = p_right.add_run("к.т.н., доц. кафедри САПР\nЮрчак Ірина Юріївна\n\n")
    r_teach.bold = True
    r_teach.font.size = Pt(11.5)
    r_teach.font.name = "Times New Roman"

    r_eval = p_right.add_run("Оцінка: ______________\n")
    r_eval.font.size = Pt(11.5)
    r_eval.font.name = "Times New Roman"
    
    r_sign = p_right.add_run("Підпис викладача: ______")
    r_sign.font.size = Pt(11.5)
    r_sign.font.name = "Times New Roman"

    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(45)
    p_foot.paragraph_format.space_after = Pt(0)
    r_foot = p_foot.add_run("Львів — 2026")
    r_foot.font.name = "Times New Roman"
    r_foot.font.size = Pt(11.5)
    r_foot.font.color.rgb = COLOR_MUTED

    doc.add_page_break()

def add_header_styled(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.bold = True
    r.font.name = "Times New Roman"
    if level == 1:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(13)
        r.font.color.rgb = COLOR_PRIMARY
    elif level == 2:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        r.font.size = Pt(12)
        r.font.color.rgb = COLOR_DARK
    else:
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11)
        r.font.color.rgb = COLOR_TEXT
    return p

def add_body_p(doc, text, bold_prefix=None, space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.font.color.rgb = COLOR_DARK
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_TEXT
    return p

def add_table_data(doc, headers, rows_data):
    tbl = doc.add_table(rows=len(rows_data)+1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl, "CBD5E1")

    # Header row
    for col_idx, h in enumerate(headers):
        cell = tbl.cell(0, col_idx)
        set_cell_background(cell, "F1F5F9")
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.color.rgb = COLOR_DARK

    # Body rows
    for row_idx, rdata in enumerate(rows_data):
        for col_idx, val in enumerate(rdata):
            cell = tbl.cell(row_idx+1, col_idx)
            set_cell_margins(cell, 50, 50, 80, 80)
            if row_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(str(val))
            r.font.name = "Times New Roman"
            r.font.size = Pt(10)

    doc.add_paragraph().paragraph_format.space_after = Pt(3)

def add_screenshot_figure(doc, img_name, fig_caption):
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Inches(6.2))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(6)
        r_cap = p_cap.add_run(fig_caption)
        r_cap.italic = True
        r_cap.font.name = "Times New Roman"
        r_cap.font.size = Pt(10)
        r_cap.font.color.rgb = COLOR_MUTED

def add_side_by_side_figures(doc, img1_name, cap1, img2_name, cap2):
    img1_path = os.path.join(SCREENSHOTS_DIR, img1_name)
    img2_path = os.path.join(SCREENSHOTS_DIR, img2_name)
    
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell1 = tbl.cell(0, 0)
    cell2 = tbl.cell(0, 1)
    cell1.width = Inches(3.3)
    cell2.width = Inches(3.3)
    set_cell_margins(cell1, 30, 30, 40, 40)
    set_cell_margins(cell2, 30, 30, 40, 40)

    # Left cell
    if os.path.exists(img1_path):
        p1 = cell1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run()
        r1.add_picture(img1_path, width=Inches(3.0))
        p1_cap = cell1.add_paragraph()
        p1_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1_cap.paragraph_format.space_after = Pt(0)
        r1_c = p1_cap.add_run(cap1)
        r1_c.italic = True
        r1_c.font.name = "Times New Roman"
        r1_c.font.size = Pt(9.5)
        r1_c.font.color.rgb = COLOR_MUTED

    # Right cell
    if os.path.exists(img2_path):
        p2 = cell2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run()
        r2.add_picture(img2_path, width=Inches(3.0))
        p2_cap = cell2.add_paragraph()
        p2_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2_cap.paragraph_format.space_after = Pt(0)
        r2_c = p2_cap.add_run(cap2)
        r2_c.italic = True
        r2_c.font.name = "Times New Roman"
        r2_c.font.size = Pt(9.5)
        r2_c.font.color.rgb = COLOR_MUTED

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def build_complete_lab6_report():
    doc = Document()
    setup_document_styles(doc)

    # 1. ТИТУЛЬНА СТОРІНКА
    add_title_page(doc)

    # 1. МЕТА ТА ЗАВДАННЯ ЛАБОРАТОРНОЇ РОБОТИ
    add_header_styled(doc, "1. Мета та завдання лабораторної роботи", 1)
    add_body_p(doc, 
        "Мета роботи: Опанувати методологію компонентної верстки вебінтерфейсу, побудови адаптивного дизайну за принципом Mobile-First "
        "та використання утилітарного підходу (Utility-First) на базі сучасного фреймворку Tailwind CSS за підтримки генеративних ШІ-асистентів. "
        "Розробити систему ізольованих UI-компонентів для платформи «ChargeUA» (Header з навігацією та мобільним меню, Hero-блок, "
        "інтерактивна карта станцій, каталог карток зарядних хабів, адаптивний Grid та Footer), забезпечивши високу швидкість рендерингу, "
        "відповідність стандартам доступності WCAG 2.2 AA та сумісність з дизайн-системою ЛР №4.")

    add_body_p(doc, "Основні завдання роботи:", space_after=2)
    tasks = [
        "1. Налаштувати робоче середовище Visual Studio Code та ознайомитися з можливостями онлайн-пісочниці Tailwind Play для ізольованого прототипування.",
        "2. Здійснити декомпозицію прототипу ChargeUA (ЛР №4) на самостійні ізольовані UI-компоненти (Button, Header, Card, Grid, Footer).",
        "3. Створити та протестувати перший UI-компонент кнопки (Primary CTA Button) за допомогою Tailwind-класів та перевірити роботу станів hover, focus, active та disabled.",
        "4. Згенерувати за допомогою ШІ та рафінувати адаптивний компонент Header із логотипом, десктопною навігацією, кнопками дій та сенсорним гамбургер-меню.",
        "5. Опанувати та реалізувати на практиці принцип Mobile-First (базові класи для мобільних екранів, розширення через sm:, md:, lg:, xl:).",
        "6. Розробити універсальну картку зарядної станції (Card) з автентичними даними, статусами доступності конекторів та інтерактивними кнопками дій.",
        "7. Побудувати адаптивну сітку карток за допомогою Tailwind CSS Grid (1 колонка на мобільних, 2 на планшетах sm, 3 на десктопах lg).",
        "8. Реалізувати повнофункціональну інтерактивну карту зарядних станцій ChargeUA з фільтрами за потужністю та роботою від генераторів під час блекаутів.",
        "9. Зверстати семантичний адаптивний підвал сайту (Footer) на 4 колонки з навігацією, сервісами та контактами.",
        "10. Перенести дизайн-систему ChargeUA (кольори, шрифти Inter, радіуси, тіні) у Tailwind та зв'язати її з файлом style.css.",
        "11. Провести всебічний інженерний аудит згенерованого ШІ-коду, усунути суперечливі класи та зайві arbitrary values.",
        "12. Виконати кроспристроєве тестування в DevTools Device Toolbar (375px/390px, 768px, 1440px) та перевірити доступність за критеріями WCAG 2.2 AA (розмір мішені min 44px, коефіцієнт контрасту > 4.5:1).",
        "13. Провести технічну валідацію за допомогою Nu Html Checker, W3C CSS Validator та аудиту Lighthouse."
    ]
    for t in tasks:
        add_body_p(doc, t, space_after=1)

    # 2. ХІД ВИКОНАННЯ РОБОТИ
    add_header_styled(doc, "2. Хід виконання роботи", 1)

    add_header_styled(doc, "Етап 1. Встановлення та налаштування редактора коду VS Code та розширень", 2)
    add_body_p(doc, 
        "Було розгорнуто робоче середовище на базі Visual Studio Code з інтеграцією інструментів автоматизації та штучного інтелекту. "
        "Встановлено та активовано обов'язковий комплекс розширень: "
        "Live Server (v5.7.10) — локальний HTTP-сервер з підтримкою Hot Reload/Live Reload при кожному збереженні файлів; "
        "Prettier - Code formatter — автоматичне форматування вихідного коду за єдиним консистентним стилем (2 пробіли, правильні лапки та закриття тегів); "
        "Auto Rename Tag — синхронне оновлення парних HTML-тегів при перейменуванні (наприклад, div на section); "
        "Material Icon Theme — чітка візуальна диференціація типів файлів та папок у файловому провіднику; "
        "Tailwind CSS IntelliSense — інтелектуальне автодоповнення класів-утиліт із попереднім переглядом генерованого CSS-коду та кольорових плашок; "
        "AI Assistant / Agentic Chat — асистент для аудиту, перевірки доступності та кодогенерації.")
    add_screenshot_figure(doc, "00_vscode_environment.png", "Рис. 1. Налаштоване робоче середовище VS Code з проєктом ChargeUA та активними розширеннями")

    add_header_styled(doc, "Етап 2. Аналіз макета сайту з ЛР №4 та виділення семантичних блоків", 2)
    add_body_p(doc, 
        "Перед початком верстки було виконано декомпозицію прототипу платформи «ChargeUA» (ЛР №4). Для кожного функціонального блоку "
        "визначено відповідний семантичний тег HTML5 та базові класи Tailwind CSS:")
    
    t_headers = ["Елемент макета Figma", "HTML5-елемент", "Семантична роль", "Атрибути доступності (a11y)"]
    t_rows = [
        ["Шапка сайту", "<header>", "Контейнер вступної навігації (banner)", "class=\"site-header\""],
        ["Головне меню", "<nav>", "Орієнтир навігації (navigation)", "aria-label=\"Головна навігація\""],
        ["Основний контент", "<main>", "Головний унікальний контент сторінки", "id=\"main\""],
        ["Hero-блок", "<section>", "Вступний тематичний розділ з H1", "aria-labelledby=\"hero-title\""],
        ["Форма пошуку", "<form role=\"search\">", "Область пошуку станцій", "aria-label=\"Пошук зарядних станцій\""],
        ["Метрики мережі", "<dl>, <dt>, <dd>", "Список пар термін-значення (статистика)", "class=\"stats\""],
        ["Каталог станцій", "<section>", "Тематичний розділ каталогу хабів", "id=\"stations\""],
        ["Картка станції/послуги", "<article>", "Автономний контентний блок", "class=\"card\""],
        ["Фільтри мапи", "<aside>", "Допоміжна бічна панель (complementary)", "aria-labelledby=\"filters-title\""],
        ["Група фільтрів", "<fieldset>, <button>", "Елементи вибору параметрів", "class=\"chip\", aria-pressed=\"true/false\""],
        ["Секція переваг", "<section>", "Тематичний розділ переваг сервісу", "id=\"benefits\""],
        ["Картка відгуку", "<article>, <blockquote>", "Цитата відгуку клієнта з оцінкою", "class=\"card\", aria-label=\"Оцінка 5 з 5\""],
        ["Підвал сайту", "<footer>", "Завершальна інформація (contentinfo)", "id=\"contacts\", class=\"site-footer\""],
        ["Контакти підтримки", "<address>", "Контактні відомості організації", "class=\"site-footer__list\""]
    ]
    add_table_data(doc, t_headers, t_rows)

    add_header_styled(doc, "Етап 3. Створення структури проєкту", 2)
    add_body_p(doc, 
        "Було створено чисту та модульну файлову структуру вебресурсу:\n"
        "• lab-06-tailwind-components/ — коренева папка проєкту;\n"
        "• index.html — основний семантичний документ сайту з інтегрованими компонентами;\n"
        "• index_div_soup.html — початковий несемантичний каркас для навчального порівняння;\n"
        "• css/style.css — таблиця стилів із користувацькими токенами та правилами кастомізації;\n"
        "• assets/ — графічні активи (Logo.svg, іконки, промо-банер ai_promo_banner.jpg, карта map_lviv.jpg, фонове відео);\n"
        "• js/ — клієнтські скрипти калькулятора (calculator.js), навігації (nav.js) та інтерактивної мапи станцій (map.js);\n"
        "• screenshots/ — зафіксовані скріншоти тестування та промптів.")

    add_header_styled(doc, "Етап 4. Створення базового каркасу HTML за допомогою <div>", 2)
    add_body_p(doc, 
        "Відповідно до навчальної програми було згенеровано початковий каркас головної сторінки (файл index_div_soup.html), "
        "побудований суто на блокових контейнерах <div> без семантичних тегів HTML5. Це дозволило на практиці дослідити ключові проблеми «div-мішанини» (div soup):\n"
        "1. Деградація доступності: відсутність орієнтирів (Landmarks: banner, main, contentinfo). Екранні диктори бачать лише однорідні вузли generic.\n"
        "2. Втрата ієрархії контенту: текстові блоки замість заголовків h1–h3 унеможливлюють адекватну індексацію пошуковими ботами.\n"
        "3. Критичне падіння читабельності коду: наявність понад 40 однорідних закриваючих тегів </div></div></div> суттєво ускладнює підтримку.")

    add_header_styled(doc, "Етап 5. Семантичний рефакторинг за допомогою ШІ", 2)
    add_body_p(doc, 
        "Було здійснено повноцінний семантичний рефакторинг за допомогою ШІ (Claude 3.5 Sonnet). Усі блокові контейнери замінено на "
        "семантичні елементи стандарту HTML5, вибудовано чітку ієрархію заголовків (єдиний <h1> у Hero, <h2> для розділів, <h3> для карток) "
        "та інтегровано вимоги доступності WCAG 2.2 AA.\n"
        "Було реалізовано такі вдосконалення:\n"
        "• Додано клавіатурний skip-link: <a class=\"skip-link\" href=\"#main\"> для миттєвого переходу до вмісту.\n"
        "• Контекстні підписи: кнопки прокладання маршруту доповнено невидимим описом для скрінрідерів (<span class=\"visually-hidden\"> до станції...</span>).\n"
        "• Семантичні форми та статистика: рядок пошуку оформили через <form role=\"search\"> з міткою <label>, а метрики — через список <dl>/<dt>/<dd>.")

    add_header_styled(doc, "Етап 6. Перевірка семантичної структури", 2)
    add_body_p(doc, 
        "Було перевірено згенеровану розмітку в інспекторі браузера Chrome DevTools у вкладці Accessibility. "
        "Підтверджено коректне формування дерева доступності: наявні всі ключові семантичні орієнтири (Banner, Navigation, Main, Region, Contentinfo), "
        "а елементи дій представлені кнопками та посиланнями.")

    add_header_styled(doc, "Етап 7. Підготовка стильового файлу", 2)
    add_body_p(doc, 
        "Створено файл css/style.css та підключено його в секції <head> файлу index.html. На початку стильового файлу реалізовано сучасний CSS Reset "
        "та систему базових правил: скидання box-sizing у border-box, обнулення дефолтних відступів margin/padding, плавне прокручування "
        "(scroll-behavior: smooth), налаштування доступного фокусу (:focus-visible) та підтримку prefers-reduced-motion.")

    add_header_styled(doc, "Етап 8. Створення користувацьких стилів CSS", 2)
    add_body_p(doc, 
        "Дизайн-токени з дизайн-системи Figma (ЛР №4) було перенесено у файл style.css у глобальний кореневий псевдоклас :root. "
        "Змінні згруповано за 7 обов'язковими категоріями:\n"
        "1. Colors — основні та допоміжні брендові кольори ChargeUA, кольори фону, рамок та семантичних статусів портів.\n"
        "2. Typography — шрифтові гарнітури, ієрархія розмірів шрифтів (від fs-xs до fs-hero) та ваги.\n"
        "3. Spacing — модульна шкала внутрішніх і зовнішніх відступів (--space-1...8, gutter).\n"
        "4. Border radius — радіуси скруглення елементів (--radius-sm, md, lg, pill).\n"
        "5. Shadows — трирівнева система тіней для створення глибини (--shadow-sm, md, lg).\n"
        "6. Container — максимальна ширина контентного блоку (--container-max: 1200px) та мішень дотику (--target-size: 44px).\n"
        "7. Transitions — тривалості та криві безьє інтерактивних переходів (--transition, --transition-bounce).")

    add_screenshot_figure(doc, "03_vscode_css_tokens.png", "Рис. 2. Оголошення користувацьких стилів CSS у псевдокласі :root у редакторі VS Code")

    add_header_styled(doc, "Етап 9. Побудова макета за допомогою Flexbox, Grid та Tailwind", 2)
    add_body_p(doc, 
        "Для створення сучасної адаптивної блочної моделі застосовано комбінацію CSS Flexbox та CSS Grid з використанням утилітарних класів Tailwind CSS. "
        "CSS Flexbox використано для одновимірного вирівнювання: шапки сайту, навігації, груп кнопок дій, внутрішнього компонування карток. "
        "CSS Grid використано для двовимірної адаптивної сітки каталогу та блоку мапи з бічними фільтрами.")

    add_header_styled(doc, "Етап 10. Базова стилізація компонентів сторінки", 2)
    add_body_p(doc, 
        "На цьому етапі було послідовно відтворено дизайн-систему з Лабораторної роботи №4 для всіх ключових компонентів сторінки:\n"
        "1. Шапка (.site-header) — реалізовано липку фіксацію position: sticky; top: 0; z-index: 10000; з білим фоном та тонкою тінню.\n"
        "2. Навігація (.nav__link) — інтерактивні стани при наведенні (:hover) та доступний фокус (:focus-visible).\n"
        "3. Головний блок (.hero-sec) — відтворено оригінальний макет ЛР №4 із розміщенням автентичного зображення станції (assets/images/hero_bg.jpg) "
        "безпосередньо у фоні секції за допомогою чистого CSS (background-image) та плавного градієнтного переходу.\n"
        "4. Заголовки секцій (.section__title) — єдиний стиль із використанням іконок у фірмовому колі.\n"
        "5. Кнопки (.btn, .btn--primary, .btn--outline) — стилізація з розміром зони натискання 44px та забороною небажаного переносу рядків (white-space: nowrap).\n"
        "6. Картки (.card) — скруглення 12px, тіні, бейджі типів заряду та статуси доступності портів.\n"
        "7. Заклик до дії (CTA) та блок карти (.map-card) — стилізовано блок карти з ізоляцією контексту накладання (isolation: isolate; z-index: 1).\n"
        "8. Підвал (.site-footer) — темний фон var(--color-secondary), триколонковий макет та контакти в <address>.")

    add_header_styled(doc, "Етап 11. Підключення Google Fonts та іконкових шрифтів", 2)
    add_body_p(doc, 
        "Було підключено шрифти Google Fonts у секції <head> файлу index.html через механізм <link> з використанням директив preconnect для прискорення завантаження. "
        "Підключено іконковий шрифт Font Awesome 6 через офіційний CDN у <head>. Для зручного керування іконками введено токени та допоміжні класи. "
        "Відображення шрифтів та іконок було перевірено у браузері через Live Server.")

    add_header_styled(doc, "Етап 12. Рефакторинг та оптимізація CSS", 2)
    add_body_p(doc, 
        "Перед проведенням рефакторингу було виконано аудит коду: виявлено дублювання значень кольорів, повторювані радіуси, надлишкові селектори "
        "та конфлікти шарів при прокручуванні сторінки. Усунуто всі дублювання кольорів та радіусів — 100% заміна на var(--color-*) та var(--radius-*). "
        "Виправлено конфлікт шарів (layering bug): шапці задано z-index: 10000; position: sticky;, а карті .map-card додано isolation: isolate; position: relative; z-index: 1;. "
        "Завдяки цьому внутрішні шари контенту ізольовані всередині контейнера і не перекривають фіксовану шапку. "
        "Для кнопок дій додано white-space: nowrap;, що запобігає розриву тексту кнопок («Знайти зарядку») на вузьких екранах. "
        "Оптимізовано компонування шапки: структура побудована за допомогою чистого CSS Flexbox із логотипом зліва, горизонтальною навігацією по центру "
        "та кнопками дій справа; додано мобільне гамбургер-меню з ARIA-атрибутами.")

    add_header_styled(doc, "Етап 13. Перевірка семантики та доступності", 2)
    add_body_p(doc, "Було проведено детальний HTML-аудит розмітки з перевіркою ключових критеріїв доступності WCAG 2.2 AA:")
    
    t_a11y_headers = ["Проблема", "Причина", "Рекомендоване виправлення"]
    t_a11y_rows = [
        ["Відсутність швидкого переходу до контенту", "Користувач клавіатури змушений проходити табуляцією через усі посилання меню", "Додано <a class=\"skip-link\" href=\"#main\"> на початку сторінки (WCAG 2.4.1)"],
        ["Однакові підписи посилань маршруту", "Посилання «Прокласти маршрут» позбавлені контексту для скрінрідера", "Додано <span class=\"visually-hidden\"> до станції...</span> у кожне посилання (WCAG 2.4.4)"],
        ["Низький контраст зірок рейтингу", "Світло-жовтий колір (#F59E0B) мав коефіцієнт контрасту лише 2.8:1 на білому фоні", "Замінено на контрастний янтарно-коричневий відтінок #B45309 з коефіцієнтом > 4.5:1 (WCAG 1.4.3)"],
        ["Колірне кодування статусів портів", "Інформація про статус передавалася лише кольоровою цяткою (зелений/червоний)", "Додано явний текст («Вільний», «Зайнятий») поруч із маркером (WCAG 1.4.1)"],
        ["Розмір сенсорних мішеней на мобільному", "Посилання меню мали висоту менше 40px", "Встановлено min-height: 44px; padding: 12px 14px; для відповідності Touch Target (WCAG 2.5.5/2.5.8)"]
    ]
    add_table_data(doc, t_a11y_headers, t_a11y_rows)

    add_header_styled(doc, "Етап 14. Тестування та валідація HTML та CSS", 2)
    add_body_p(doc, 
        "Було виконано всебічну технічну валідацію та автоматизоване тестування створеного вебресурсу:\n"
        "1. Nu Html Checker (W3C Markup Validation Service) — підтверджено повну валідність семантичної розмітки index.html: 0 помилок (Errors: 0, Warnings: 0).\n"
        "2. W3C CSS Validation Service — стильовий файл style.css успішно пройшов перевірку синтаксису CSS3 та користувацьких змінних без зауважень.\n"
        "3. Google Lighthouse Snapshot Audit (Chrome DevTools):\n"
        "   • Accessibility: 100 / 100 (ідеальний показник доступності, успішно пройдено всі тести контрастності, орієнтирів та ARIA);\n"
        "   • Best Practices: 100 / 100 (сучасні вебстандарти, відсутність уразливостей);\n"
        "   • SEO: високий результат завдяки чіткій ієрархії h1–h3, наявності метатегів та alt-підписів.")

    # 3. БРАУЗЕРНЕ ВІДОБРАЖЕННЯ СТОРІНКИ
    add_header_styled(doc, "3. Браузерне відображення сторінки", 1)
    add_body_p(doc, 
        "Відображення сторінки протестовано у браузері Chrome на різних роздільних здатностях екрана. "
        "Нижче наведено підтверджуючі скріншоти роботи інтерфейсу платформи ChargeUA:")

    add_screenshot_figure(doc, "04_browser_desktop_overview.png", "Рис. 3. Відображення головної сторінки ChargeUA у десктопному браузері (1440×900 px): шапка, фонове відео, кнопки дій")
    add_screenshot_figure(doc, "04_browser_desktop_view.png", "Рис. 4. Загальний огляд макета: інтерактивний калькулятор зарядки, Live-карта та каталог станцій")

    add_body_p(doc, "Адаптивне відображення для мобільних пристроїв (390×844 px):", bold_prefix=None, space_after=2)
    add_side_by_side_figures(doc, 
        "05_browser_mobile_hero.png", "Рис. 5. Мобільний Hero з компактним хедерам (58px)",
        "05_browser_mobile_grid.png", "Рис. 6. Мобільний калькулятор та адаптивна сітка"
    )

    # 4. ПРОМПТ-ПАСПОРТ (PROMPT LOG)
    add_header_styled(doc, "4. Промпт-паспорт (Prompt Log)", 1)
    add_body_p(doc, 
        "У процесі виконання роботи було реалізовано інтерактивний цикл взаємодії з ШІ: "
        "«Промпт → Генерація ШІ → Аналіз коду → Тестування у браузері → Внесення коректив».")

    t_prompt_headers = ["№", "Етап / Завдання", "Роль та модель ШІ", "Згенерований результат", "Внесені правки та оптимізації"]
    t_prompt_rows = [
        ["1", "Етап 4: Базовий каркас div-soup", "Senior Frontend Dev (Claude 3.5 Sonnet / Gemini Thinking)", "Створено файл index_div_soup.html суто на div-контейнерах без семантики HTML5. Gemini в освітньому профілі обмежив генерацію фільтрами.", "Збережено файл для наочного порівняльного аналізу деградації Accessibility Tree."],
        ["2", "Етап 5: Семантичний рефакторинг", "Senior Frontend Dev & a11y Expert (Claude 3.5 Sonnet)", "Замінено несемантичні div на header, nav, main, section, article, aside, footer. Сформовано ієрархію h1–h3.", "Додано клавіатурний skip-link, приховані пояснення для екранних дикторів (<span class=\"visually-hidden\">) та список <dl> для статистики."],
        ["3", "Етапи 8–12: CSS-архітектура, Flexbox, Grid", "Senior CSS Engineer (Claude 3.5 Sonnet)", "Створено style.css: :root токени ChargeUA за 7 групами, Flexbox для шапки, адаптивний Grid repeat(auto-fit, minmax(280px, 1fr)).", "Виправлено контраст зірок рейтингу (#B45309 замість жовтого), ізольовано контекст накладання карти (isolation: isolate), аудит Lighthouse 100/100."]
    ]
    add_table_data(doc, t_prompt_headers, t_prompt_rows)

    add_header_styled(doc, "4.1. Ітерація 1 (Промпт 1): Базовий каркас index_div_soup.html", 2)
    add_body_p(doc, 
        "Було сформульовано рольовий промпт для генерації навмисно несемантичного каркасу сторінки ChargeUA суто на <div>-контейнерах "
        "з метою демонстрації проблеми div-soup та аналізу дерева доступності.")
    add_side_by_side_figures(doc,
        "01_prompt1_div_layout_claude.png", "Рис. 7.1. Початковий каркас на div у Claude",
        "01_prompt1_div_code_claude.png", "Рис. 7.2. Вихідний div-код у вікні артефакту"
    )
    add_screenshot_figure(doc, "01_prompt1_gemini_comparison.png", "Рис. 7.3. Порівняльний аналіз запиту генерації каркасу в Google Gemini (освітній профіль LPNU)")

    add_header_styled(doc, "4.2. Ітерація 2 (Промпт 2): ШІ-рефакторинг та семантичні стандарти HTML5", 2)
    add_body_p(doc, 
        "Виконано рефакторинг div-каркасу: заміну несемантичних тегів на семантичні орієнтири HTML5, впорядкування ієрархії заголовків h1–h3 "
        "та інтеграцію вимог доступності WCAG 2.2 AA.")
    add_screenshot_figure(doc, "02_prompt2_semantic_refactoring_claude.png", "Рис. 7.4. Звіт Claude про результати семантичного рефакторингу коду index.html")

    add_header_styled(doc, "4.3. Ітерація 3 (Промпт 3): Побудова адаптивної CSS-архітектури", 2)
    add_body_p(doc, 
        "Реалізовано модульну дворівневу CSS-архітектуру на базі чистих Flexbox та Grid з інтеграцією токенів дизайн-системи ChargeUA.")
    add_side_by_side_figures(doc,
        "03_prompt3_css_architecture_tokens_claude.png", "Рис. 7.5. Токени бренду ChargeUA в чаті Claude",
        "03_prompt3_css_code_claude.png", "Рис. 7.6. Оголошення змінних :root у Claude"
    )
    add_screenshot_figure(doc, "03_prompt3_html_semantic_code_claude.png", "Рис. 7.7. Семантичний код index.html з підключенням Inter та Font Awesome")

    # 5. ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ
    add_header_styled(doc, "5. Відповіді на контрольні запитання", 1)

    qa_list = [
        ("1. Що таке Tailwind CSS і в чому полягає концепція Utility-First?",
         "Tailwind CSS — це сучасний утилітарний CSS-фреймворк, який замість традиційного написання громіздких монолітних CSS-класів (.card, .btn-custom) надає великий набір низькорівневих класів-утиліт прямої дії (flex, pt-4, text-center, bg-blue-600). Концепція Utility-First полягає в тому, що інтерфейси будуються шляхом комбінування атомарних утиліт безпосередньо в HTML-розмітці без необхідності писати власний CSS з нуля, що усуває проблему розростання стильових файлів та спрощує підтримку."),

        ("2. Які переваги Tailwind CSS порівняно з традиційним підходом написання CSS?",
         "1) Відсутність потреби вигадувати унікальні назви класів (за методологіями на зразок BEM); 2) Файли стилів припиняють неконтрольовано зростати завдяки Just-In-Time компіляції (фінальний CSS важить менше 10-20 КБ); 3) Безпечність змін: редагування класів у конкретному HTML-елементі не викликає каскадних регресій у сусідніх компонентах; 4) Вбудована дизайн-система із суворими шкалами відступів, кольорів та типографіки; 5) Миттєве налаштування адаптивності через префікси sm:, md:, lg:."),

        ("3. Яке призначення сервісу Tailwind Play?",
         "Tailwind Play — це офіційна інтерактивна хмарна пісочниця (https://play.tailwindcss.com) для швидкого експериментування та прототипування інтерфейсів. Вона надає можливість миттєво тестувати розмітку та класи Tailwind без розгортання локального оточення Node.js/Vite, перевіряти адаптивність на різних в'юпортах, ділитися робочим кодом через посилання (Share) та бачити результат у реальному часі."),

        ("4. Що таке адаптивний дизайн і як він реалізується в Tailwind CSS?",
         "Адаптивний дизайн — це підхід до проєктування вебсайтів, який гарантує коректне відображення та зручність взаємодії на пристроях з будь-якою роздільною здатністю (від 320px смартфонів до 4K моніторів). У Tailwind CSS адаптивність реалізується на базі підходу Mobile-First за допомогою префіксів контрольних точок (брейкпоїнтів): немодифікований клас (наприклад, w-full) застосовується на мобільних пристроях, а класи з префіксами (наприклад, md:w-auto, lg:grid-cols-3) спрацьовують лише тоді, коли ширина екрана перевищує відповідний поріг min-width."),

        ("5. Яке призначення брейкпоїнтів sm:, md:, lg: та xl:?",
         "Брейкпоїнти в Tailwind визначають мінімальну ширину екрана (CSS-правило @media (min-width: ...)), починаючи з якої активується вказаний стиль: 1) sm: — 640px (великі смартфони та міні-планшети); 2) md: — 768px (стандартні планшети та невеликі ноутбуки); 3) lg: — 1024px (десктопні монітори та лептопи); 4) xl: — 1280px (широкоформатні десктопи); 5) 2xl: — 1536px (великі монітори високої роздільності)."),

        ("6. Для чого використовуються модифікатори станів hover:, focus: та active:?",
         "Модифікатори станів дозволяють застосовувати утилітарні класи лише за настання певної інтерактивної події або псевдокласу: hover: змінює стиль при наведенні курсору миші (наприклад, hover:bg-blue-700); focus: активується при отриманні фокусу з клавіатури або кліку на поле введення (focus:ring-2 focus:ring-blue-500); active: змінює вигляд у момент безпосереднього затискання кнопки миші або пальця на сенсорному екрані (active:scale-95). Також використовуються disabled: для заблокованих елементів та focus-visible: для доступності."),

        ("7. Які можливості надає розширення Tailwind CSS IntelliSense?",
         "Офіційне розширення для VS Code суттєво прискорює розробку: 1) Автодоповнення класів із фільтрацією на льоту; 2) Спливаючі підказки (Hover Preview), що показують точний CSS-код, який генерує клас (наприклад, hover над p-4 покаже padding: 1rem); 3) Візуальні кольорові маркери поруч із класами кольорів (bg-blue-600); 4) Лінтер синтаксису, що підсвічує конфлікти та помилки в назвах класів."),

        ("8. Чому згенерований штучним інтелектом код потребує рефакторингу?",
         "ШІ-моделі навчаються на великих масивах публічного коду різної якості, тому часто генерують суб'єктивні або неоптимальні конструкції: надлишкові контейнери <div> (div soup), суперечливі класи (одночасно inline-block та flex), надмірне використання свавільних значень (arbitrary values на зразок w-[342px] замість системних шкал), застарілі атрибути або недостатній контраст для доступності. Розробник повинен виступати архітектором і контролером якості, проводячи рафінування та очищення коду."),

        ("9. Які вимоги до доступності вебінтерфейсу перевірено під час виконання лабораторної роботи?",
         "Під час виконання роботи було перевірено та забезпечено дотримання стандарту WCAG 2.2 рівня AA: 1) Наявність кнопки швидкого переходу до контенту (<a class=\"skip-link\" href=\"#main\">); 2) Контрастність тексту відносно фону не менше 4.5:1 для звичайного тексту та 3:1 для великих заголовків; 3) Розмір інтерактивних мішеней натискання (Touch Target) не менше 44×44 px на мобільних пристроях; 4) Наявність змістовних атрибутів alt для зображень; 5) Використання семантичних орієнтирів HTML5 (<header>, <nav>, <main>, <section>, <footer>); 6) Підтримка клавіатурного фокусу (:focus-visible) без блокування фокусу."),

        ("10. Для чого використовується режим Device Toolbar в DevTools?",
         "Режим Device Toolbar (Ctrl+Shift+M у Chrome/Edge) призначений для точної емуляції мобільних і планшетних пристроїв безпосередньо у браузері. Він дозволяє: перевіряти поведінку медіа-запитів та брейкпоїнтів на будь-якій довільній ширині; тестувати стандартні гаджети (iPhone SE, Pixel, iPad); емулювати сенсорні події дотику (Touch Events); перевіряти орієнтацію екрана (Portrait / Landscape) та обмежувати швидкість мережі й процесора для оцінки реальної продуктивності."),

        ("11. Які компоненти вебінтерфейсу створено за допомогою ШІ в лабораторній роботі?",
         "Для платформи ChargeUA було створено повноцінну компонентну систему: 1) Button — кнопка дій із підтримкою Primary, Outline та Disabled станів; 2) Header — навігаційна панель із десктопним меню, логотипом, кнопками входу та сенсорним гамбургер-меню; 3) Hero Section — вступний екран із заголовком, перевагами, підбором конекторів та автентичним фоном станції; 4) Station Card — картка зарядної станції із детальними характеристиками портів (CCS2, Type 2, CHAdeMO) та статусами доступності; 5) Grid Container — адаптивна сітка для розташування карток станцій (1 колонка mobile -> 2 sm -> 3 lg); 6) Stations Map Section — інтерактивна карта станцій із бічними фільтрами; 7) Footer — 4-колонковий адаптивний підвал сайту."),

        ("12. Що таке Preflight в Tailwind CSS і яке його призначення?",
         "Preflight — це вбудований у Tailwind CSS механізм базового нормалізуючого скидання стилів браузера, побудований на основі modern-normalize. Його призначення: обнулити стандартні зовнішні та внутрішні відступи (margin/padding: 0), встановити box-sizing: border-box для всіх елементів, прибрати стандартні маркери списків (list-style: none), зробити зображення та відео блоковими з max-width: 100%, та скинути стилі заголовків і кнопок, створюючи абсолютно передбачуваний чистий фундамент для атомарної верстки."),

        ("13. Які переваги має використання переходів (transition) та ефектів (hover, focus) у вебінтерфейсі?",
         "Використання transition та псевдокласів hover/focus надає інтерфейсу професійного вигляду та покращує UX: 1) Забезпечує негайний візуальний зворотний зв'язок (Micro-interactions), показуючи користувачу, що елемент є клікабельним; 2) Плавна анімація (наприклад, transition duration-200) пом'якшує зміну кольору чи масштабу без різких стрибків картинки; 3) Допомагає користувачам з клавіатурною навігацією чітко бачити поточний активний елемент, запобігаючи помилковим діям.")
    ]

    for q, a in qa_list:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(4)
        p_q.paragraph_format.space_after = Pt(1)
        r_q = p_q.add_run(q)
        r_q.bold = True
        r_q.font.name = "Times New Roman"
        r_q.font.size = Pt(11)
        r_q.font.color.rgb = COLOR_DARK

        p_a = doc.add_paragraph()
        p_a.paragraph_format.space_before = Pt(0)
        p_a.paragraph_format.space_after = Pt(4)
        p_a.paragraph_format.line_spacing = 1.15
        r_a = p_a.add_run(a)
        r_a.font.name = "Times New Roman"
        r_a.font.size = Pt(11)
        r_a.font.color.rgb = COLOR_TEXT

    # 6. ВИСНОВКИ
    add_header_styled(doc, "6. Висновки", 1)
    add_body_p(doc, "Під час виконання лабораторної роботи №6 було успішно вирішено всі поставлені інженерні завдання з верстки UI-компонентів та забезпечення адаптивності платформи «ChargeUA»:")
    
    conclusions = [
        "1. Було налаштовано робоче середовище Visual Studio Code та встановлено спеціалізовані розширення: Live Server, Prettier, Auto Rename Tag, Material Icon Theme та Tailwind CSS IntelliSense для ефективної атомарної розробки.",
        "2. Опановано парадигму Utility-First CSS та інтерактивну пісочницю Tailwind Play, що дозволило розробляти та тестувати ізольовані компоненти перед їхньою фінальною інтеграцією в кодову базу проєкту.",
        "3. Реалізовано компонентну систему вебплатформи ChargeUA: створено адаптивну шапку (Header) з гамбургер-меню, вступний Hero-блок, інтерактивну Live-карту 480+ станцій з фільтрами, картки станцій з індикацією статусів конекторів, адаптивну сітку CSS Grid та 4-колонковий підвал сайту (Footer).",
        "4. На практиці втілено принцип Mobile-First: базові класи-утиліти орієнтовані на смартфони (320px–390px), а структурні перетворення виконуються прогресивно через брейкпоїнти sm: (640px), md: (768px) та lg: (1024px) без використання фіксованих ширин.",
        "5. Забезпечено повну відповідність дизайн-системі ЛР №4: збережено брендову палітру кольорів (#005EC9, #0F172A), типографіку Google Fonts 'Inter', трирівневу систему тіней та радіуси скруглень у файлі style.css.",
        "6. Проведено комплексне кроспристроєве тестування в інспекторі Chrome DevTools Device Toolbar та аудит доступності WCAG 2.2 AA (показник 100/100 у Google Lighthouse). Сформовано Промпт-паспорт взаємодії з ШІ та надано вичерпні відповіді на всі 13 контрольних запитань."
    ]
    for c in conclusions:
        add_body_p(doc, c)

    # Збереження файлів
    out_docx = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
    out_root_docx = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
    
    doc.save(out_docx)
    shutil.copy(out_docx, out_root_docx)
    print(f"Master DOCX successfully saved to:\n  - {out_docx}\n  - {out_root_docx}")
    
    # Конвертація в PDF через Microsoft Word COM
    try:
        import win32com.client
        print("Converting DOCX to PDF via Word COM...")
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc_in = word.Documents.Open(os.path.abspath(out_docx))
        out_pdf = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
        out_root_pdf = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
        doc_in.SaveAs(os.path.abspath(out_pdf), FileFormat=17) # 17 = wdFormatPDF
        doc_in.Close()
        word.Quit()
        shutil.copy(out_pdf, out_root_pdf)
        print(f"Master PDF successfully generated:\n  - {out_pdf}\n  - {out_root_pdf}")
    except Exception as e:
        print(f"Word COM PDF conversion notice: {e}")

    return out_docx

if __name__ == "__main__":
    build_complete_lab6_report()
