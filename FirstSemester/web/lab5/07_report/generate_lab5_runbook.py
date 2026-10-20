# -*- coding: utf-8 -*-
"""
Генератор детальної покрокової інструкції (Runbook / Хід роботи)
для Лабораторної роботи №5: «Семантична верстка, користувацькі стилі CSS, Flexbox/Grid макет та рефакторинг вебплатформи ChargeUA»
Автор: Лемішка Андрій Анатолійович, група ПП-24
"""

import os
import sys
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab5"
REPORT_DIR = os.path.join(BASE_DIR, "07_report")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")

COLOR_PRIMARY = RGBColor(0x00, 0x5E, 0xC9)     # ChargeUA синій
COLOR_DARK = RGBColor(0x0F, 0x17, 0x2A)        # Slate 900
COLOR_TEXT = RGBColor(0x1E, 0x29, 0x3B)        # Slate 800
COLOR_MUTED = RGBColor(0x64, 0x74, 0x8B)       # Slate 500
COLOR_ACCENT = RGBColor(0x00, 0x80, 0x80)      # Teal / Accent

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
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
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = COLOR_TEXT
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)

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
    p2.paragraph_format.space_after = Pt(6)
    r = p2.add_run("Кафедра «Систем автоматизованого проектування» (САПР)")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(10)
        r_logo = p_logo.add_run()
        r_logo.add_picture(coat_path, width=Inches(2.1))

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_before = Pt(4)
    p4.paragraph_format.space_after = Pt(4)
    r = p4.add_run("ПОКРОКОВА ІНСТРУКЦІЯ ТА ХІД РОБОТИ")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_PRIMARY

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(6)
    r = p5.add_run("до Лабораторної роботи №5\nз дисципліни «Вебтехнології та вебдизайн»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)

    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p6.paragraph_format.space_before = Pt(4)
    p6.paragraph_format.space_after = Pt(16)
    r = p6.add_run("«Семантична верстка, дизайн-токени в CSS, Flexbox/Grid макет та рефакторинг вебплатформи ChargeUA»")
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)
    r.italic = True

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.left_indent = Inches(3.2)
    p_meta.paragraph_format.space_before = Pt(12)
    p_meta.paragraph_format.space_after = Pt(28)
    p_meta.paragraph_format.line_spacing = 1.2
    
    r_meta = p_meta.add_run("Виконав:\n")
    r_meta.bold = True
    r_meta.font.name = "Times New Roman"
    r_meta.font.size = Pt(12)
    
    r_meta2 = p_meta.add_run("студент групи ПП-24\nЛемішка Андрій Анатолійович\n\n")
    r_meta2.font.name = "Times New Roman"
    r_meta2.font.size = Pt(12)
    
    r_meta3 = p_meta.add_run("Прийняла:\n")
    r_meta3.bold = True
    r_meta3.font.name = "Times New Roman"
    r_meta3.font.size = Pt(12)
    
    r_meta4 = p_meta.add_run("к.т.н., доцент кафедри САПР\nЮрчак Ірина Юріївна\n\n")
    r_meta4.font.name = "Times New Roman"
    r_meta4.font.size = Pt(12)

    p_city = doc.add_paragraph()
    p_city.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_city.paragraph_format.space_before = Pt(20)
    p_city.paragraph_format.space_after = Pt(0)
    r_city = p_city.add_run("Львів — 2026")
    r_city.bold = True
    r_city.font.name = "Times New Roman"
    r_city.font.size = Pt(12)

    doc.add_page_break()

def add_header_styled(doc, text, level):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Times New Roman"
    
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        run.font.size = Pt(15)
        run.font.color.rgb = COLOR_PRIMARY
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        run.font.size = Pt(13)
        run.font.color.rgb = COLOR_DARK
    else:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        run.font.size = Pt(12)
        run.font.color.rgb = COLOR_TEXT
    return p

def add_body_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11.5)
        r_pre.font.color.rgb = COLOR_DARK
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(11.5)
    r.font.color.rgb = COLOR_TEXT
    return p

def add_prompt_box(doc, title, prompt_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "F0F7FF")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="005EC9"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    r_t = p.add_run(f"💬 {title}\n")
    r_t.bold = True
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(11)
    r_t.font.color.rgb = COLOR_PRIMARY
    
    r_body = p.add_run(prompt_text)
    r_body.font.name = "Consolas"
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(2)

def add_action_table(doc, action_items):
    tbl = doc.add_table(rows=len(action_items), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, "E2E8F0")
    
    for idx, (label, val) in enumerate(action_items):
        cell_lbl = tbl.cell(idx, 0)
        cell_val = tbl.cell(idx, 1)
        cell_lbl.width = Inches(1.8)
        cell_val.width = Inches(5.0)
        
        set_cell_background(cell_lbl, "F8FAFC")
        set_cell_margins(cell_lbl, top=80, bottom=80, left=120, right=120)
        set_cell_margins(cell_val, top=80, bottom=80, left=120, right=120)
        
        p_l = cell_lbl.paragraphs[0]
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        r_l = p_l.add_run(label)
        r_l.bold = True
        r_l.font.name = "Times New Roman"
        r_l.font.size = Pt(10.5)
        r_l.font.color.rgb = COLOR_DARK
        
        p_v = cell_val.paragraphs[0]
        p_v.paragraph_format.space_before = Pt(0)
        p_v.paragraph_format.space_after = Pt(0)
        p_v.paragraph_format.line_spacing = 1.15
        r_v = p_v.add_run(val)
        r_v.font.name = "Times New Roman"
        r_v.font.size = Pt(10.5)
        r_v.font.color.rgb = COLOR_TEXT
        
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def add_code_snippet(doc, title, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:left w:val="single" w:sz="16" w:space="0" w:color="005EC9"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_t = p.add_run(f"📋 {title}\n")
    r_t.bold = True
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(10.5)
    r_t.font.color.rgb = COLOR_PRIMARY
    
    r_c = p.add_run(code_text)
    r_c.font.name = "Consolas"
    r_c.font.size = Pt(9.0)
    r_c.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def add_screenshot_figure(doc, img_name, caption, width=Inches(5.9)):
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if not os.path.exists(img_path):
        print(f"Warning: Screenshot {img_name} not found in {SCREENSHOTS_DIR}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    r = p_img.add_run()
    r.add_picture(img_path, width=width)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(1)
    p_cap.paragraph_format.space_after = Pt(8)
    r_cap = p_cap.add_run(caption)
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(10)
    r_cap.italic = True
    r_cap.font.color.rgb = COLOR_MUTED

def generate_full_runbook():
    print("=== STARTING LAB 5 RUNBOOK GENERATION ===")
    doc = Document()
    setup_document_styles(doc)
    add_title_page(doc)
    
    # ---------------- ВСТУП ----------------
    add_header_styled(doc, "ВСТУП ТА ТЕХНОЛОГІЧНИЙ РЕГЛАМЕНТ", 1)
    add_body_p(doc, 
        "Цей документ є вичерпною покроковою інструкцією («Runbook / Хід виконання роботи») "
        "до Лабораторної роботи №5, в якій зафіксовано кожну практичну дію студента: які файли створювалися, "
        "які конкретні пункти меню та кнопки обиралися в середовищі Visual Studio Code, які точні промпти "
        "задавались системам генеративного штучного інтелекту, що саме та в які рядки вставлялося, "
        "як налаштовувався локальний сервер Live Server, та як проводився аудит доступності за стандартом WCAG 2.2 AA.")
    
    add_action_table(doc, [
        ("Проєкт:", "Вебплатформа швидкісних зарядних станцій електромобілів в Україні «ChargeUA»"),
        ("Дисципліна:", "Вебтехнології та вебдизайн (2 курс, 1 семестр, спеціальність 121 «Інженерія програмного забезпечення»)"),
        ("Середовище розробки:", "Visual Studio Code 1.95+, розширення Live Server (ritwickdey.liveserver v5.7.10)"),
        ("Стек технологій:", "HTML5 Semantic Elements, CSS3 (Custom Properties :root, CSS Grid, Flexbox), Font Awesome 6, Google Fonts (Inter)"),
        ("ШІ-асистенти:", "Claude 3.5 Sonnet (генерація, рефакторинг), Google Gemini Thinking (порівняння), Chrome DevTools MCP (аудит)"),
        ("Обмеження етапу:", "Суворе дотримання вимог ЛР №5: 0% JavaScript (чистий семантичний HTML/CSS), статичний фон hero_bg.jpg")
    ])
    
    add_screenshot_figure(doc, "00_vscode_environment.png", 
        "Рис. 1. Робоче середовище розробника VS Code з файловою структурою проєкту ChargeUA")

    # ---------------- ЕТАП 1 ----------------
    add_header_styled(doc, "ЕТАП 1. ПІДГОТОВКА СТРУКТУРИ ПРОЄКТУ ТА ФАЙЛОВОЇ ІЄРАРХІЇ", 1)
    add_body_p(doc, 
        "Першим етапом є підготовка ізольованої кореневої директорії для чистої семантичної верстки. "
        "Відповідно до вимог стандартизації проєктів, структура каталогу організована наступним чином:")
    
    add_action_table(doc, [
        ("1. Де створювали:", "Шлях на диску: D:\\Studing\\SecondYear\\FirstSemester\\web\\lab5\\lab-05-semantic-layout"),
        ("2. Які папки створили:", "• css/ — таблиці стилів (style.css)\n• assets/images/ — графічні ресурси (hero_bg.jpg, map_lviv.jpg, logo.svg)\n• screenshots/ — фіксація етапів розробки"),
        ("3. Які файли створили:", "• index.html — основний семантичний документ\n• index_div_soup.html — несемантичний демонстраційний каркас\n• css/style.css — єдиний стиль зі змінними та макетами"),
        ("4. Що обрали для фону:", "Автентичний статичний файл hero_bg.jpg (електромобіль біля зарядної станції з дизайн-матеріалів ЛР4)")
    ])

    # ---------------- ЕТАП 2-7: DIV SOUP & REFECTORING ----------------
    add_header_styled(doc, "ЕТАПИ 2–7. ЕКСПЕРИМЕНТ З «DIV-SOUP» ТА СЕМАНТИЧНИЙ РЕФАКТОРИНГ HTML5", 1)
    add_body_p(doc, 
        "Для виконання пунктів методичних вказівок щодо демонстрації проблеми «div-мішанини» було реалізовано порівняльний експеримент: "
        "спочатку згенеровано каркас суто на <div> елементах, проаналізовано його вади для екранних дикторів та SEO, "
        "після чого проведено повний семантичний рефакторинг коду.")

    add_prompt_box(doc, "Промпт 1. Створення несемантичного каркасу «Div-Soup» для експерименту",
        "Дій як Senior Frontend Developer.\n"
        "На основі мого проєкту вебплатформи зарядних станцій «ChargeUA» створи початковий базовий HTML-каркас index.html.\n"
        "Вимоги:\n"
        "1. Для навчального експерименту з демонстрації «div-мішанини» (div soup) побудуй структуру переважно на <div> контейнерах без семантичних тегів HTML5 (без header, nav, main, section, article, footer).\n"
        "2. Секції сайту: Шапка, Hero, Каталог станцій DC/AC, Карта з фільтрами, Переваги, Відгуки, Підвал.\n"
        "3. Додай <!DOCTYPE html>, lang=\"uk\", UTF-8, viewport, базові класи для всіх блоків.\n"
        "4. Надай цілісний код index.html."
    )

    add_screenshot_figure(doc, "01_prompt1_div_layout_claude.png", 
        "Рис. 2. Процес відправки запиту та генерації каркасу на <div> у діалоговому вікні Claude 3.5 Sonnet")

    add_screenshot_figure(doc, "01_prompt1_div_code_claude.png", 
        "Рис. 3. Фрагмент сформованого коду div-мішанини в артефакті Claude (збережено як index_div_soup.html)")

    add_screenshot_figure(doc, "01_prompt1_gemini_comparison.png", 
        "Рис. 4. Порівняльний аналіз запиту в Google Gemini Thinking (фіксація блокування в корпоративному профілі)")

    add_body_p(doc, "Наступним кроком подано запит на повний семантичний рефакторинг та очищення від div soup:")

    add_prompt_box(doc, "Промпт 2. Семантичний рефакторинг та впровадження стандарту WCAG 2.2 AA",
        "Проаналізуй попередній файл index.html. Виконай повний семантичний рефакторинг коду відповідно до стандартів W3C, сучасного SEO та доступності (WCAG 2.2 AA).\n"
        "Вимоги:\n"
        "1. Заміни всі несемантичні контейнери <div> на семантичні елементи HTML5 (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>).\n"
        "2. Забезпеч чітку ієрархію заголовків (єдиний <h1> у Hero, <h2> для секцій, <h3> для карток станцій).\n"
        "3. Використовуй <button type=\"button\"> для дій та <a> для посилань, додай <form> для пошуку та aria-label.\n"
        "4. Винеси стилі у зовнішній файл css/style.css (<link rel=\"stylesheet\" href=\"css/style.css\").\n"
        "5. Надай фінальний чистий семантичний код index.html та звіт зі списком змін."
    )

    add_screenshot_figure(doc, "02_prompt2_semantic_refactoring_claude.png", 
        "Рис. 5. Звіт Claude про заміну 42 тегів <div> на семантичні теги HTML5 та оптимізацію ієрархії")

    add_action_table(doc, [
        ("Куди вставлявся код:", "Файл index.html (повна заміна початкового вмісту)"),
        ("Шапка сайту:", "<header class=\"site-header\"> з орієнтиром banner, логотипом і блоком навігації"),
        ("Головна навігація:", "<nav class=\"nav\" aria-label=\"Головна навігація\"> зі списком <ul>/<li>"),
        ("Основний контент:", "<main id=\"main\"> як єдиний семантичний контейнер сторінки"),
        ("Hero-секція:", "<section class=\"hero\" id=\"hero\"> з єдиним заголовком <h1> слогану ChargeUA"),
        ("Каталог послуг:", "<section class=\"section\" id=\"stations\"> з сіткою карток <article class=\"card\">"),
        ("Інтерактивна карта:", "<aside class=\"map-filters\" aria-label=\"Фільтри пошуку станцій\">"),
        ("Підвал:", "<footer class=\"site-footer\"> з контактною інформацією в тегу <address>"),
        ("Клавіатурний перехід:", "Додано <a class=\"skip-link\" href=\"#main\"> на початку <body> для WCAG 2.4.1")
    ])

    # ---------------- ЕТАП 8: CSS ТОКЕНИ ----------------
    add_header_styled(doc, "ЕТАП 8. СТВОРЕННЯ КОРИСТУВАЦЬКИХ СТИЛІВ CSS ТА ТОКЕНИ В :ROOT", 1)
    add_body_p(doc, 
        "На восьмому етапі проведено оцифрування та перенесення дизайн-системи вебплатформи ChargeUA "
        "з Лабораторної роботи №4 у користувацькі властивості CSS Custom Properties (псевдоклас :root). "
        "Всі змінні згруповані за категоріями призначення:")

    add_code_snippet(doc, "Фрагмент :root токенів у css/style.css",
        ":root {\n"
        "  /* 1. Брендові та інтерфейсні кольори */\n"
        "  --color-primary: #005EC9;          /* Фірмовий синій ChargeUA */\n"
        "  --color-primary-hover: #004BA0;\n"
        "  --color-secondary: #0F172A;        /* Глибокий темний фон секцій */\n"
        "  --color-accent: #00B4D8;           /* Бірюзовий акцент швидкої зарядки */\n"
        "  --color-bg: #FFFFFF;               /* Основне світле полотно */\n"
        "  --color-surface: #F8FAFC;          /* Поверхня карток */\n"
        "  --color-text: #1E293B;\n"
        "  --color-muted: #64748B;\n\n"
        "  /* 2. Статуси зарядних портів */\n"
        "  --color-status-free: #10B981;      /* Вільний порт (зелений) */\n"
        "  --color-status-busy: #EF4444;      /* Зайнятий порт (червоний) */\n"
        "  --color-status-reserved: #F59E0B;  /* Заброньований (бурштиновий) */\n\n"
        "  /* 3. Типографіка та розміри шрифтів */\n"
        "  --font-base: 'Inter', system-ui, -apple-system, sans-serif;\n"
        "  --fs-sm: 0.875rem;                 /* 14px */\n"
        "  --fs-base: 1rem;                   /* 16px */\n"
        "  --fs-lg: 1.25rem;                  /* 20px */\n"
        "  --fs-xl: 1.75rem;                  /* 28px */\n"
        "  --fs-hero: clamp(2rem, 5vw, 3.25rem); /* Адаптивний слоган */\n\n"
        "  /* 4. Система відступів */\n"
        "  --space-1: 4px;  --space-2: 8px;   --space-3: 12px; --space-4: 16px;\n"
        "  --space-5: 24px; --space-6: 32px;  --space-7: 40px; --space-8: 48px;\n\n"
        "  /* 5. Радіуси, тіні та тач-таргети */\n"
        "  --radius-sm: 6px; --radius-md: 12px; --radius-lg: 20px; --radius-pill: 9999px;\n"
        "  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05); --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);\n"
        "  --target-size: 44px;               /* WCAG 2.5.5 мінімальний тач-таргет */\n"
        "  --container-max: 1200px;\n"
        "  --transition: 0.2s ease-in-out;\n"
        "}"
    )

    add_screenshot_figure(doc, "03_vscode_css_tokens.png", 
        "Рис. 6. Редактор VS Code з файлом css/style.css та оголошеними дизайн-токенами ChargeUA")

    # ---------------- ЕТАП 9: FLEXBOX & GRID ----------------
    add_header_styled(doc, "ЕТАП 9. ПОБУДОВА МАКЕТА ЗА ДОПОМОГОЮ CSS FLEXBOX ТА CSS GRID", 1)
    add_body_p(doc, 
        "Згідно з методичними рекомендаціями, формується сучасна гібридна блочна модель: "
        "для глобального двовимірного розташування секцій та сітки карток застосовано CSS Grid, "
        "а для одновимірного вирівнювання (шапка, меню навігації, кнопки, внутрішнє компонування карток) — CSS Flexbox.")

    add_action_table(doc, [
        ("CSS Grid у каталозі станцій:", 
         ".grid {\n"
         "  display: grid;\n"
         "  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n"
         "  gap: var(--space-6);\n"
         "} — забезпечує автоматичне адаптивне розташування карток без фіксованої ширини."),
        ("CSS Flexbox у шапці сайту:", 
         ".header-inner {\n"
         "  display: flex;\n"
         "  align-items: center;\n"
         "  justify-content: space-between;\n"
         "  gap: var(--space-4);\n"
         "} — логотип ліворуч, меню по центру, кнопки входу/реєстрації праворуч."),
        ("CSS Flexbox всередині карток:", 
         ".card {\n"
         "  display: flex;\n"
         "  flex-direction: column;\n"
         "  justify-content: space-between;\n"
         "} — гарантує однакову висоту карток і притискання кнопки дії донизу."),
        ("CSS Flexbox для кнопок і бейджів:", 
         ".btn, .status {\n"
         "  display: inline-flex;\n"
         "  align-items: center;\n"
         "  justify-content: center;\n"
         "  gap: var(--space-2);\n"
         "} — ідеальне вертикальне центрування тексту та іконки.")
    ])

    add_screenshot_figure(doc, "03_prompt3_css_code_claude.png", 
        "Рис. 7. Генерація модулів Flexbox та Grid у стильовому документі style.css")

    # ---------------- ЕТАП 10: БАЗОВА СТИЛІЗАЦІЯ ТА ФОН ----------------
    add_header_styled(doc, "ЕТАП 10. БАЗОВА СТИЛІЗАЦІЯ СТОРІНКИ ТА АВТЕНТИЧНИЙ СТАТИЧНИЙ ФОН", 1)
    add_body_p(doc, 
        "На цьому етапі реалізовано вимогу відтворення оригінальної дизайн-системи з Лабораторної роботи №4. "
        "Ключове завдання — інтеграція статичного фону hero_bg.jpg (автомобіль біля швидкісної зарядної станції) "
        "як чистого CSS-бекграунду з градієнтним затемненням, що вирішує проблему накладання тексту на автомобіль без створення зайвих контейнерів.")

    add_code_snippet(doc, "Стилізація Hero-секції у css/style.css зі статичним фоном",
        ".hero {\n"
        "  position: relative;\n"
        "  background-color: var(--color-secondary);\n"
        "  background-image: \n"
        "    linear-gradient(90deg, \n"
        "      rgba(15, 23, 42, 0.94) 0%, \n"
        "      rgba(15, 23, 42, 0.80) 45%, \n"
        "      rgba(15, 23, 42, 0.25) 100%),\n"
        "    url('../assets/images/hero_bg.jpg');\n"
        "  background-size: cover;\n"
        "  background-position: center right;\n"
        "  background-repeat: no-repeat;\n"
        "  color: #FFFFFF;\n"
        "  padding: var(--space-8) 0;\n"
        "}\n\n"
        "/* Текстовий контент розташовано зліва з високою читабельністю */\n"
        ".hero-content {\n"
        "  max-width: 640px;\n"
        "}"
    )

    add_screenshot_figure(doc, "04_browser_desktop_view.png", 
        "Рис. 8. Візуалізація стилізованої Hero-секції: текстовий блок зліва, чисте зображення авто та станції справа")

    add_screenshot_figure(doc, "04_browser_desktop_overview.png", 
        "Рис. 9. Загальний вигляд головної сторінки ChargeUA з каталогом станцій, картою та відгуками")

    # ---------------- ЕТАП 11: FONTS & ICONS ----------------
    add_header_styled(doc, "ЕТАП 11. ПІДКЛЮЧЕННЯ GOOGLE FONTS ТА ІКОНКОВОГО ШРИФТУ", 1)
    add_body_p(doc, 
        "У файлі index.html підключено оптимізований вебшрифт Inter (з попереднім встановленням з'єднання preconnect) "
        "та іконочний шрифт Font Awesome 6 через надійну CDN-мережу Cloudflare:")

    add_action_table(doc, [
        ("Куди вставлявся код:", "Розділ <head> файлу index.html перед підключенням style.css"),
        ("1. Preconnect Google Fonts:", 
         "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
         "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>"),
        ("2. Шрифт Inter:", 
         "<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap\" rel=\"stylesheet\">"),
        ("3. Іконки Font Awesome 6:", 
         "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css\">"),
        ("4. Застосування в CSS:", 
         "body { font-family: var(--font-base); }\n"
         "h1, h2, h3 { font-weight: 700; }")
    ])

    add_screenshot_figure(doc, "03_prompt3_html_semantic_code_claude.png", 
        "Рис. 10. Фрагмент секції <head> файлу index.html з підключеними шрифтами та іконками")

    # ---------------- ЕТАП 12-13: РЕФАКТОРИНГ ТА ДОСТУПНІСТЬ ----------------
    add_header_styled(doc, "ЕТАПИ 12–13. РЕФАКТОРИНГ CSS ТА АУДИТ ДОСТУПНОСТІ (WCAG 2.2 AA)", 1)
    add_body_p(doc, 
        "За допомогою ШІ-промпту в ролі Senior CSS Engineer було проведено аудит стильового файлу: "
        "виявлено та усунуто дублювання кольорів, замінено жорстко закодовані значення на CSS-змінні, "
        "вилучено зайві файли стилів (залишено єдиний файл css/style.css), налаштовано доступні стани :focus-visible. "
        "Після цього за допомогою Chrome DevTools Lighthouse проведено комплексну перевірку доступності.")

    add_action_table(doc, [
        ("Lighthouse Accessibility Score:", "100 / 100 — ідеальний показник доступності (всі 27 автоматичних перевірок пройдено)"),
        ("Lighthouse Best Practices:", "100 / 100 — чистий код без застарілих API та безпечні зовнішні посилання rel=\"noopener\""),
        ("Кольоровий контраст (WCAG 1.4.3):", "Усі текстові пари мають коефіцієнт контрасту не менше 4.5:1 (заголовки > 7:1)"),
        ("Підтримка скрінрідерів (WCAG 1.4.1):", "Статуси портів передаються одночасно кольором, текстом та іконкою"),
        ("Клавіатурна навігація (WCAG 2.1.1):", "Повний доступ до всіх інтерактивних елементів клавішею Tab з підсвіткою :focus-visible")
    ])

    add_screenshot_figure(doc, "04_browser_desktop_fullpage.png", 
        "Рис. 11. Повний вертикальний макет сторінки ChargeUA після фінального семантичного рефакторингу")

    # ---------------- ЕТАП 14: LIVE SERVER RUNBOOK ----------------
    add_header_styled(doc, "ЕТАП 14. ПОКРОКОВА РОБОТА З LIVE SERVER У VISUAL STUDIO CODE", 1)
    add_body_p(doc, 
        "Важливим практичним моментом лабораторної роботи є правильне керування локальним вебсервером "
        "Live Server (розширення ritwickdey.liveserver) у редакторі Visual Studio Code. Нижче наведено точні інструкції, "
        "що саме натискати та як розпізнавати поточний стан сервера:")

    add_action_table(doc, [
        ("1. Де шукати кнопку на екрані:", 
         "У ПРАВОМУ НИЖНЬОМУ КУТКУ статус-бару VS Code (синій або темний рядок у самому низу вікна)."),
        ("2. Стан «Вимкнено» (Go Live):", 
         "Якщо сервер не запущений, на панелі відображається піктограма антени та напис «((•)) Go Live».\n"
         "Дія: клацнути лівою кнопкою миші один раз."),
        ("3. Стан «Запущено» (Port : 5500):", 
         "Коли сервер стартує, текст кнопки змінюється на «⊘ Port : 5500».\n"
         "Це означає, що локальний сервер активний і веде трансляцію за адресою http://127.0.0.1:5500/.\n"
         "Повторний клік по «Port : 5500» зупиняє сервер і повертає напис «Go Live»."),
        ("4. Запуск через контекстне меню:", 
         "Клікнути правою кнопкою миші у редакторі на відкритому файлі index.html -> вибрати пункт «Open with Live Server»."),
        ("5. Запуск гарячими клавішами:", 
         "Натиснути комбінацію клавіш Alt + L, а потім одразу Alt + O."),
        ("6. Перевірка в браузері:", 
         "Відкрити Google Chrome і перейти за посиланням: http://127.0.0.1:5500/index.html")
    ])

    add_screenshot_figure(doc, "06_vscode_go_live_button.png", 
        "Рис. 12. Кнопка «((•)) Go Live» у правому нижньому кутку статус-бару VS Code (стан готовності до запуску)")

    add_screenshot_figure(doc, "06_vscode_port_5500_active.png", 
        "Рис. 13. Індикатор активного сервера «⊘ Port : 5500» у статус-барі VS Code")

    add_screenshot_figure(doc, "07_browser_chargeua_port_5500.png", 
        "Рис. 14. Працююча вебплатформа ChargeUA у Google Chrome за адресою http://127.0.0.1:5500/ з автентичним фоном")

    # ---------------- ПІДСУМКОВА ТАБЛИЦЯ ----------------
    add_header_styled(doc, "ЗВЕДЕНА ТАБЛИЦЯ ВИКОНАНИХ ДІЙ (ШО / ДЕ / КУДИ)", 1)
    
    table_data = [
        ("Етап", "Що вибирали / де клікали", "Що вводили / промпт", "Куди вставляли / результат"),
        ("Етап 1", "Провідник Windows / VS Code", "Створення папок css, assets/images", "Структура lab-05-semantic-layout"),
        ("Етап 2", "Чат Claude 3.5 Sonnet", "Промпт 1 на div soup", "Файл index_div_soup.html"),
        ("Етап 3-7", "Чат Claude 3.5 Sonnet", "Промпт 2 на семантичний рефакторинг", "Файл index.html (header, nav, main, footer)"),
        ("Етап 8", "style.css в редакторі VS Code", "Дизайн-токени бренду ChargeUA", "Секція :root у файлі css/style.css"),
        ("Етап 9", "style.css в редакторі VS Code", "CSS Grid repeat(auto-fit...) та Flexbox", "Класи .grid, .header-inner, .card"),
        ("Етап 10", "Папка assets/images/hero_bg.jpg", "CSS linear-gradient + url('hero_bg.jpg')", "Селектор .hero у css/style.css"),
        ("Етап 11", "<head> файлу index.html", "Теги preconnect, Inter та Font Awesome", "Підключення шрифтів та іконок без помилок"),
        ("Етап 12", "Чат Claude / VS Code", "Запит Senior CSS Engineer на рефакторинг", "Очищений style.css без дублікатів"),
        ("Етап 13", "Chrome DevTools -> Lighthouse", "Запуск аудиту Accessibility & Best Practices", "100/100 Accessibility, 100/100 Best Practices"),
        ("Етап 14", "Правий нижній куток VS Code", "Клік по ((•)) Go Live або Alt+L, Alt+O", "Запуск на http://127.0.0.1:5500 у Chrome")
    ]
    
    tbl = doc.add_table(rows=len(table_data), cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, "CBD5E1")
    
    col_widths = [Inches(1.0), Inches(2.0), Inches(2.0), Inches(1.8)]
    
    for row_idx, row in enumerate(table_data):
        for col_idx, val in enumerate(row):
            cell = tbl.cell(row_idx, col_idx)
            cell.width = col_widths[col_idx]
            is_hdr = (row_idx == 0)
            
            if is_hdr:
                set_cell_background(cell, "005EC9")
                txt_color = RGBColor(0xFF, 0xFF, 0xFF)
                bold = True
                align = WD_ALIGN_PARAGRAPH.CENTER
            else:
                bg = "F8FAFC" if (row_idx % 2 == 1) else "FFFFFF"
                set_cell_background(cell, bg)
                txt_color = COLOR_TEXT
                bold = (col_idx == 0)
                align = WD_ALIGN_PARAGRAPH.LEFT
                
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = align
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.bold = bold
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5 if not is_hdr else 10.0)
            r.font.color.rgb = txt_color

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(12)

    # ---------------- ВИСНОВКИ ----------------
    add_header_styled(doc, "ВИСНОВКИ", 1)
    add_body_p(doc, 
        "1. У ході виконання лабораторної роботи №5 успішно опановано повний стек сучасної семантичної верстки HTML5 "
        "та дворівневої організації таблиць стилів CSS3 на базі призначених для користувача властивостей (CSS Custom Properties :root).")
    add_body_p(doc, 
        "2. Практично продемонстровано переваги семантичних тегів (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>) "
        "над застарілою практикою «div soup»: покращено Accessibility Tree, увімкнено швидкі орієнтири для скрінрідерів, "
        "гарантовано логічну ієрархію заголовків h1–h3 та підвищено потенціал SEO-індексації.")
    add_body_p(doc, 
        "3. Реалізовано чистий компонувальний макет без використання сторонніх CSS-фреймворків: "
        "для каталогу карток зарядних станцій побудовано гнучкий CSS Grid (repeat(auto-fit, minmax(280px, 1fr))), "
        "а для шапки, меню навігації та внутрішнього розташування компонентів — CSS Flexbox.")
    add_body_p(doc, 
        "4. Інтегровано автентичний статичний фон hero_bg.jpg за допомогою CSS-градієнтного перекриття, що забезпечило "
        "ідеальну читабельність слогану без створення штучних рамок і текстового нашарування.")
    add_body_p(doc, 
        "5. Забезпечено найвищий стандарт доступності за критеріями WCAG 2.2 AA, що підтверджено аудитом Lighthouse (100 / 100 Accessibility).")
    add_body_p(doc, 
        "6. Налаштовано та протестовано роботу розширення Live Server у VS Code, зафіксовано алгоритм переходу між станами "
        "«((•)) Go Live» та «⊘ Port : 5500», що забезпечує автоматичне перезавантаження вебсторінки у браузері при будь-яких змінах вихідного коду.")

    # Збереження файлу
    out_docx_report = os.path.join(REPORT_DIR, "Покрокова_інструкція_хід_роботи_Лаб5.docx")
    out_docx_root = os.path.join(BASE_DIR, "Покрокова_інструкція_хід_роботи_Лаб5.docx")
    
    doc.save(out_docx_report)
    shutil.copy(out_docx_report, out_docx_root)
    print(f"Successfully generated DOCX:\n  - {out_docx_report}\n  - {out_docx_root}")
    return out_docx_report

if __name__ == "__main__":
    generate_full_runbook()
