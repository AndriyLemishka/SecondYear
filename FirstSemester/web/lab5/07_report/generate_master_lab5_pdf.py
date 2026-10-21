# -*- coding: utf-8 -*-
"""
Майстер-генератор повного звіту та інструкції до Лабораторної роботи №5
Включає: Титулку ДСТУ, Мета/Завдання, Повний хід роботи (Етапи 1-14),
20 Контрольних запитань з еталонними відповідями, Анатомію коду, Тести, Висновки.
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
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab5"
REPORT_DIR = os.path.join(BASE_DIR, "07_report")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")

COLOR_PRIMARY = RGBColor(0x00, 0x5E, 0xC9)     # ChargeUA синій
COLOR_DARK = RGBColor(0x0F, 0x17, 0x2A)        # Slate 900
COLOR_TEXT = RGBColor(0x1E, 0x29, 0x3B)        # Slate 800
COLOR_MUTED = RGBColor(0x64, 0x74, 0x8B)       # Slate 500

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
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
    p2.paragraph_format.space_after = Pt(4)
    r = p2.add_run("Кафедра «Систем автоматизованого проектування» (САПР)")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(8)
        r_logo = p_logo.add_run()
        r_logo.add_picture(coat_path, width=Inches(2.0))

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_before = Pt(4)
    p4.paragraph_format.space_after = Pt(4)
    r = p4.add_run("ЗВІТ ТА ПОКРОКОВИЙ ХІД РОБОТИ")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_PRIMARY

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(4)
    r = p5.add_run("до Лабораторної роботи №5\nз навчальної дисципліни «Вебтехнології та вебдизайн»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13.5)

    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p6.paragraph_format.space_before = Pt(2)
    p6.paragraph_format.space_after = Pt(14)
    r = p6.add_run("«Семантична верстка, користувацькі стилі CSS, Flexbox/Grid макет, рефакторинг та відповіді на контрольні запитання»")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12.5)
    r.italic = True

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.left_indent = Inches(3.2)
    p_meta.paragraph_format.space_before = Pt(10)
    p_meta.paragraph_format.space_after = Pt(24)
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
    p_city.paragraph_format.space_before = Pt(18)
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
        run.font.size = Pt(14)
        run.font.color.rgb = COLOR_PRIMARY
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        run.font.size = Pt(12.5)
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
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "F0F7FF")
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="20" w:space="0" w:color="005EC9"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_t = p.add_run(f"💬 {title}\n")
    r_t.bold = True
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(10.5)
    r_t.font.color.rgb = COLOR_PRIMARY
    
    r_body = p.add_run(prompt_text)
    r_body.font.name = "Consolas"
    r_body.font.size = Pt(9.0)
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
        set_cell_margins(cell_lbl, top=70, bottom=70, left=110, right=110)
        set_cell_margins(cell_val, top=70, bottom=70, left=110, right=110)
        
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
    set_cell_margins(cell, top=70, bottom=70, left=130, right=130)
    
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
    r_t.font.size = Pt(10.0)
    r_t.font.color.rgb = COLOR_PRIMARY
    
    r_c = p.add_run(code_text)
    r_c.font.name = "Consolas"
    r_c.font.size = Pt(8.8)
    r_c.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def add_screenshot_figure(doc, img_name, caption, width=Inches(5.8)):
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if not os.path.exists(img_path):
        print(f"Warning: Screenshot {img_name} not found in {SCREENSHOTS_DIR}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(5)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    r = p_img.add_run()
    r.add_picture(img_path, width=width)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(1)
    p_cap.paragraph_format.space_after = Pt(6)
    r_cap = p_cap.add_run(caption)
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(9.5)
    r_cap.italic = True
    r_cap.font.color.rgb = COLOR_MUTED

def add_qa_card(doc, num, q_text, short_ans, deep_ans, code_sample=None):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "FFFFFF")
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="005EC9"/>
            <w:left w:val="single" w:sz="6" w:space="0" w:color="005EC9"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="005EC9"/>
            <w:right w:val="single" w:sz="6" w:space="0" w:color="005EC9"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    
    # Title
    r_q = p.add_run(f"Запитання {num}. {q_text}\n")
    r_q.bold = True
    r_q.font.name = "Times New Roman"
    r_q.font.size = Pt(11.5)
    r_q.font.color.rgb = COLOR_PRIMARY
    
    # Short Answer
    r_s_tag = p.add_run("\n🎯 Коротка відповідь (на захисті): ")
    r_s_tag.bold = True
    r_s_tag.font.name = "Times New Roman"
    r_s_tag.font.size = Pt(10.5)
    r_s_tag.font.color.rgb = RGBColor(0x06, 0x5F, 0x46) # Emerald dark
    
    r_s_txt = p.add_run(short_ans + "\n")
    r_s_txt.font.name = "Times New Roman"
    r_s_txt.font.size = Pt(10.5)
    
    # Deep Answer
    r_d_tag = p.add_run("\n📚 Поглиблене академічне пояснення: ")
    r_d_tag.bold = True
    r_d_tag.font.name = "Times New Roman"
    r_d_tag.font.size = Pt(10.5)
    r_d_tag.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF) # Blue dark
    
    r_d_txt = p.add_run(deep_ans + "\n")
    r_d_txt.font.name = "Times New Roman"
    r_d_txt.font.size = Pt(10.5)
    
    # Code sample if any
    if code_sample:
        r_c_tag = p.add_run("\n💻 Приклад у проєкті ChargeUA:\n")
        r_c_tag.bold = True
        r_c_tag.font.name = "Times New Roman"
        r_c_tag.font.size = Pt(10.0)
        r_c_tag.font.color.rgb = RGBColor(0x37, 0x41, 0x51)
        
        r_c_txt = p.add_run(code_sample)
        r_c_txt.font.name = "Consolas"
        r_c_txt.font.size = Pt(8.8)
        r_c_txt.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def build_complete_master_document():
    print("=== STARTING MASTER LAB 5 DOCUMENT GENERATION ===")
    doc = Document()
    setup_document_styles(doc)
    add_title_page(doc)
    
    # ---------------- ВСТУП ----------------
    add_header_styled(doc, "ВСТУП ТА ТЕХНІЧНЕ ЗАВДАННЯ", 1)
    add_body_p(doc, 
        "Лабораторна робота №5 присвячена практичному опануванню сучасної семантичної верстки вебсторінок "
        "стандарту HTML5, формуванню чистої модульної блочної моделі на базі специфікацій CSS Grid та Flexbox, "
        "перенесенню дизайн-токенів у користувацькі властивості CSS Custom Properties (:root), оптимізації та "
        "рефакторингу стильового коду, а також забезпеченню відповідності критеріям доступності WCAG 2.2 AA (Lighthouse 100/100).")
    
    add_action_table(doc, [
        ("Об'єкт розробки:", "Вебплатформа єдиної національної мережі швидкісних зарядних станцій електромобілів «ChargeUA»"),
        ("Мета роботи:", "Перетворити несемантичну модель на чистий валідний HTML5-документ, винести всі дизайн-токени бренду в :root, побудувати адаптивну сітку на Flexbox/Grid та успішно захистити роботу"),
        ("Обмеження етапу:", "Суворе дотримання вимог ЛР №5: 0% стороннього JavaScript (чистий семантичний HTML/CSS), заборона використання CSS-фреймворків (Bootstrap, Tailwind)"),
        ("Інструменти ШІ:", "Claude 3.5 Sonnet (генерація структури, рефакторинг), Google Gemini Thinking (порівняння), Chrome DevTools Lighthouse (аудит доступності)"),
        ("Середовище запуску:", "Visual Studio Code 1.95+, локальний вебсервер Live Server (ritwickdey.liveserver на порті 5500), Google Chrome")
    ])

    add_screenshot_figure(doc, "00_vscode_environment.png", 
        "Рис. 1. Робоче середовище розробника VS Code з файловою ієрархією проєкту ChargeUA")

    # ---------------- РОЗДІЛ 1: ХІД РОБОТИ ----------------
    add_header_styled(doc, "РОЗДІЛ 1. ПОКРОКОВИЙ ХІД ВИКОНАННЯ РОБОТИ (ЕТАПИ 1–14)", 1)
    
    # Етап 1
    add_header_styled(doc, "Етап 1. Підготовка структури проєкту та файлової ієрархії", 2)
    add_body_p(doc, "Створено кореневий каталог lab-05-semantic-layout з ізольованими підпапками css/, assets/images/ та screenshots/. "
                    "У папку assets/images перенесено автентичний статичний файл hero_bg.jpg (авто біля зарядної станції з ЛР №4).")
    
    # Етапи 2-7
    add_header_styled(doc, "Етапи 2–7. Експеримент з «Div Soup» та семантичний рефакторинг HTML5", 2)
    add_body_p(doc, "Для наочної демонстрації проблеми «div-мішанини» спочатку було сформовано навмисно несемантичний каркас index_div_soup.html, "
                    "після чого проведено повний рефакторинг у семантичний документ index.html.")

    add_prompt_box(doc, "Промпт 1. Створення навчального каркасу Div-Soup",
        "Дій як Senior Frontend Developer.\n"
        "На основі проєкту зарядних станцій ChargeUA створи початковий базовий HTML-каркас index.html.\n"
        "Вимоги:\n"
        "1. Для експерименту з демонстрації div-мішанини побудуй структуру виключно на <div> контейнерах без семантичних тегів HTML5.\n"
        "2. Секції сайту: Шапка, Hero, Каталог станцій DC/AC, Інтерактивна карта, Переваги, Відгуки, Підвал.\n"
        "3. Додай <!DOCTYPE html>, lang=\"uk\", UTF-8, viewport, базові класи.\n"
        "4. Надай цілісний код index.html."
    )

    add_screenshot_figure(doc, "01_prompt1_div_layout_claude.png", 
        "Рис. 2. Відправка запиту на створення div soup у діалоговому вікні Claude 3.5 Sonnet")

    add_screenshot_figure(doc, "01_prompt1_gemini_comparison.png", 
        "Рис. 3. Порівняльний аналіз запиту в Google Gemini Thinking (фіксація блокування в освітньому профілі)")

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
        "Рис. 4. Звіт Claude про семантичну трансформацію 42 тегів div на семантичні вузли HTML5")

    # Етап 8
    add_header_styled(doc, "Етап 8. Перенесення токенів дизайн-системи в CSS :root", 2)
    add_body_p(doc, "Оцифровано дизайн-систему ChargeUA з ЛР №4. У псевдоклас :root винесено глобальні CSS Custom Properties, "
                    "згруповані за категоріями призначення:")

    add_code_snippet(doc, "Секція :root у файлі css/style.css",
        ":root {\n"
        "  /* Бренд */\n"
        "  --color-primary: #005EC9;          /* Фірмовий синій ChargeUA */\n"
        "  --color-primary-hover: #004BA0;\n"
        "  --color-primary-light: #F0F7FF;\n"
        "  --color-secondary: #0F172A;        /* Глибокий темний фон */\n"
        "  --color-accent: #00B4D8;           /* Бірюзовий статус DC зарядки */\n"
        "  --color-bg: #FFFFFF;\n"
        "  --color-surface: #F8FAFC;\n\n"
        "  /* Статуси портів */\n"
        "  --color-status-free: #10B981;      /* Вільний */\n"
        "  --color-status-busy: #EF4444;      /* Зайнятий */\n"
        "  --color-status-reserved: #F59E0B;  /* Заброньовано */\n\n"
        "  /* Похідні */\n"
        "  --color-text: var(--color-secondary);\n"
        "  --color-muted: #64748B;\n"
        "  --color-border: #E2E8F0;\n"
        "  --target-size: 44px;               /* WCAG 2.5.5 тач-таргет */\n"
        "}"
    )

    add_screenshot_figure(doc, "03_vscode_css_tokens.png", 
        "Рис. 5. Редактор VS Code з файлом css/style.css та оголошеними токенами")

    # Етап 9
    add_header_styled(doc, "Етап 9. Побудова макета за допомогою CSS Flexbox та Grid", 2)
    add_body_p(doc, "Побудовано комбіновану блочну модель: двовимірний CSS Grid для каталогу карток та одновимірний Flexbox для шапки, меню та кнопок:")

    add_code_snippet(doc, "CSS Grid та Flexbox у css/style.css",
        "/* 1. CSS Grid для каталогу карток */\n"
        ".grid {\n"
        "  display: grid;\n"
        "  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n"
        "  gap: var(--space-6);\n"
        "}\n\n"
        "/* 2. Flexbox для шапки сайту */\n"
        ".header-inner {\n"
        "  display: flex;\n"
        "  align-items: center;\n"
        "  justify-content: space-between;\n"
        "  gap: var(--space-4);\n"
        "}"
    )

    add_screenshot_figure(doc, "03_prompt3_css_code_claude.png", 
        "Рис. 6. Генерація модулів Flexbox та Grid у стильовому документі style.css")

    # Етап 10
    add_header_styled(doc, "Етап 10. Базова стилізація та інтеграція статичного фону", 2)
    add_body_p(doc, "Автентичний статичний файл hero_bg.jpg підключено як чистий бекграунд із градієнтним затемненням зліва, "
                    "що гарантує чітку контрастність білого тексту слогану без накладання на авто та станцію праворуч:")

    add_screenshot_figure(doc, "04_browser_desktop_view.png", 
        "Рис. 7. Стилізована Hero-секція з автентичним фоном hero_bg.jpg")

    # Етап 11
    add_header_styled(doc, "Етап 11. Підключення Google Fonts та Font Awesome 6", 2)
    add_body_p(doc, "У розділі <head> файлу index.html підключено оптимізований вебшрифт Inter (з preconnect) та іконки Font Awesome 6 через CDN:")
    add_screenshot_figure(doc, "03_prompt3_html_semantic_code_claude.png", 
        "Рис. 8. Фрагмент секції <head> файлу index.html з підключеними шрифтами та CDN")

    # Етап 12
    add_header_styled(doc, "Етап 12. Рефакторинг та повна оптимізація кольорів CSS", 2)
    add_body_p(doc, "Виконано вимоги Етапу 12: замінено всі 23 захардкоджені кольори #0077E6 на var(--color-primary), "
                    "текстові кольори #0F172A та #334155 — на var(--color-text), а рамки — на var(--color-border). "
                    "Додано наслідування color: inherit для form-контролів. Тепер зміна :root миттєво перефарбовує весь сайт!")

    add_screenshot_figure(doc, "08_clean_header_without_topbar.png", 
        "Рис. 9. Загальний оновлений вигляд сайту ChargeUA після фінального рефакторингу")

    # Етап 13
    add_header_styled(doc, "Етап 13. Аудит доступності WCAG 2.2 AA (Lighthouse)", 2)
    add_body_p(doc, "За допомогою інструменту Chrome DevTools Lighthouse проведено комплексну верифікацію доступності. "
                    "Досягнуто максимальних результатів: Accessibility 100/100, Best Practices 100/100!")

    add_screenshot_figure(doc, "04_browser_desktop_fullpage.png", 
        "Рис. 10. Повний вертикальний макет сторінки ChargeUA після аудиту")

    # Етап 14
    add_header_styled(doc, "Етап 14. Запуск та робота з Live Server у Visual Studio Code", 2)
    add_body_p(doc, "Розширення ritwickdey.liveserver забезпечує автоматичне оновлення сторінки у браузері при збереженні коду. "
                    "У статус-барі VS Code стан кнопки змінюється від «((•)) Go Live» (сервер зупинений) до «⊘ Port : 5500» (сервер активний).")

    add_screenshot_figure(doc, "06_vscode_go_live_button.png", 
        "Рис. 11. Кнопка «((•)) Go Live» у правому нижньому кутку статус-бару VS Code")

    add_screenshot_figure(doc, "06_vscode_port_5500_active.png", 
        "Рис. 12. Індикатор активного локального сервера «⊘ Port : 5500» у статус-барі VS Code")

    add_screenshot_figure(doc, "07_browser_chargeua_port_5500.png", 
        "Рис. 13. Робота вебплатформи ChargeUA у Google Chrome за адресою http://127.0.0.1:5500/")

    # ---------------- РОЗДІЛ 2: АНАТОМІЯ КОДУ ----------------
    add_header_styled(doc, "РОЗДІЛ 2. АНАТОМІЯ КОДУ ТА УТИЛІТИ ДОСТУПНОСТІ", 1)
    
    add_action_table(doc, [
        (".skip-link (WCAG 2.4.1):", "<a class=\"skip-link\" href=\"#main\"> — приховане посилання, що спливає при натисканні Tab та дозволяє обійти всю шапку і перейти до головного змісту."),
        (".visually-hidden (WCAG 2.4.4):", "clip: rect(0 0 0 0); width: 1px; — приховує елемент від очей, але зберігає для скрінрідера (наприклад, контекстні підписи кнопок маршруту)."),
        (":focus-visible (WCAG 2.4.7):", "Показує контрастний контур фокусу лише при переміщенні з клавіатури, зберігаючи естетику для користувачів з мишкою."),
        ("clamp() fluid типографіка:", "--fs-hero: clamp(2rem, 5vw, 3.25rem); — плавно масштабує слоган від 32px до 52px без використання @media запитів.")
    ])

    # ---------------- РОЗДІЛ 3: 20 КОНТРОЛЬНИХ ЗАПИТАНЬ ----------------
    add_header_styled(doc, "РОЗДІЛ 3. 20 КОНТРОЛЬНИХ ЗАПИТАНЬ ВИКЛАДАЧА З ЕТАЛОННИМИ ВІДПОВІДЯМИ", 1)
    add_body_p(doc, 
        "Нижче наведено 20 ключових контрольних запитань доц. Юрчак І. Ю. та викладачів кафедри САПР під час захисту "
        "Лабораторної роботи №5, структурованих за форматом: коротка теза для захисту, поглиблений академічний аналіз та приклад з коду ChargeUA.")

    # Питання 1-20
    add_qa_card(doc, 1, 
        "Чим семантична розмітка HTML5 відрізняється від традиційної на div-контейнерах?",
        "Семантичні теги несуть смислове навантаження про тип контенту для пошукових роботів та скрінрідерів, тоді як div є беззмістовним візуальним блоком.",
        "Кожен семантичний тег автоматично транслюється браузером у відповідний вузол Accessibility Tree з ролями WAI-ARIA Landmark (header → banner, nav → navigation, main → main, footer → contentinfo). Це забезпечує повноцінне SEO та навігацію незрячих користувачів.",
        "<header class=\"site-header\">\n  <nav class=\"nav\" aria-label=\"Головна навігація\">...</nav>\n</header>"
    )

    add_qa_card(doc, 2, 
        "Чому на всій сторінці має бути лише один тег <h1>?",
        "Тег <h1> позначає єдину глобальну тему всього документа. Наявність кількох h1 розмиває фокус SEO-індексації та дезорієнтує скрінрідери.",
        "Згідно зі стандартами консорціуму W3C та алгоритмами ранжування Google, документ повинен мати чітку деревоподібну ієрархію: один h1 (книга / стаття), h2 для секцій, h3 для окремих карток всередині секцій. Не можна перескакувати рівні.",
        "<section class=\"hero\">\n  <h1 class=\"hero-h1\">Швидка та надійна зарядка електромобілів по всій Україні</h1>\n</section>"
    )

    add_qa_card(doc, 3, 
        "У чому полягає різниця між тегами <section> та <article>?",
        "<article> — це повністю самодостатній блок контенту, який зберігає сенс при вилученні зі сторінки. <section> — це тематичний розділ, пов'язаний із контекстом усього документа.",
        "<article> може бути синдикований у RSS, мобільний додаток чи розшарений окремо (картка станції, пост блогу). <section> обов'язково групує тематичний контент сторінки і повинен містити власний заголовок h2–h6.",
        "<!-- Секція каталогу -->\n<section id=\"stations\">\n  <h2>Швидкісні станції ChargeUA</h2>\n  <article class=\"card\"><h3>Київ, ТРЦ Lavina — DC 150 кВт</h3></article>\n</section>"
    )

    add_qa_card(doc, 4, 
        "Коли слід використовувати <button>, а коли посилання <a>?",
        "Посилання <a> (з href) використовується виключно для навігації (переходу між сторінками чи до якоря). Кнопка <button> використовується для виконання дії на поточній сторінці без зміни URL.",
        "Скрінрідери озвучують посилання як «link», а кнопку як «button». Посилання активується клавішею Enter, а кнопка — і Enter, і Space (пробілом). Змішування їх ролей є грубим порушенням WCAG 4.1.2.",
        "<!-- Перехід на сторінку / якір -->\n<a href=\"#calculator\" class=\"btn-primary\">Розрахувати зарядку</a>\n<!-- Дія без зміни URL -->\n<button type=\"button\" id=\"btn-calc-find\">Знайти станцію</button>"
    )

    add_qa_card(doc, 5, 
        "Що таке «Accessibility Tree» (Дерево доступності) і як воно працює?",
        "Це спеціальне дерево об'єктів доступності, яке браузер будує паралельно з DOM для трансляції інтерфейсу в екранні диктори та допоміжні технології.",
        "Браузерний рушій перетворює вузли DOM у структуру Accessibility Tree за протоколами UI Automation (Windows) або NSAccessibility (macOS). Кожен доступний елемент отримує 4 параметри: Role, Name, State та Value.",
        "<!-- Браузер створює Landmark вузол role='navigation' name='Головна навігація' -->\n<nav class=\"nav\" aria-label=\"Головна навігація\">"
    )

    add_qa_card(doc, 6, 
        "Для чого потрібен тег <aside> і де він використаний у ChargeUA?",
        "<aside> позначає другорядний (дотичний) контент, який доповнює основний, але може бути вилучений без втрати головного змісту.",
        "У дереві доступності тег <aside> створює орієнтир complementary. У ChargeUA він застосований для бічної панелі фільтрів пошуку біля карти станцій.",
        "<aside class=\"map-filters\" aria-label=\"Фільтри пошуку станцій\">\n  <button class=\"filter-chip\">Type 2 (22 кВт)</button>\n</aside>"
    )

    add_qa_card(doc, 7, 
        "Як працює псевдоклас :root та механізм каскадування змінних у CSS?",
        ":root відповідає кореню документа (<html>), але має вищу специфічність. Оголошені в ньому змінні каскадуються по всьому дереву стилів.",
        "Змінні створюються з префіксом --ім'я. Вони наслідуються дочірніми елементами і можуть бути локально перевизначені всередині будь-якого компонента через каскад (наприклад, .hero { --color-text: #fff; }).",
        ":root {\n  --color-primary: #005EC9;\n  --color-text: var(--color-secondary);\n}"
    )

    add_qa_card(doc, 8, 
        "Чому змінні CSS слід називати за призначенням, а не за конкретним кольором?",
        "Щоб забезпечити масштабованість, редизайн та зміну тем (Light/Dark) без потреби перейменовувати класи по всьому коду.",
        "Якщо назвати змінну --blue: #005EC9, а потім бренд оновить колір на смарагдовий, доведеться писати безглуздий запис --blue: #10B981 або правити сотні рядків. Семантична назва --color-primary змінюється в 1 рядку.",
        "/* Правильно: за призначенням */\n--color-primary: #005EC9;\n--color-status-free: #10B981;\n/* Неправильно: за кольором */\n--blue: #005EC9;\n--green: #10B981;"
    )

    add_qa_card(doc, 9, 
        "У чому полягає принципова різниця між макетами CSS Flexbox та CSS Grid?",
        "Flexbox є одновимірним (1D — рядок або колонка), а CSS Grid є повноцінним двовимірним (2D — керує рядками і стовпчиками одночасно).",
        "Flexbox розраховує розміри від контенту елементів вздовж однієї осі. CSS Grid формує глобальну координатну сітку площини, де елементи прив'язуються до ліній і треків матриці.",
        "/* 2D матриця */\n.grid { display: grid; grid-template-columns: repeat(3, 1fr); }\n/* 1D ланцюжок */\n.header { display: flex; justify-content: space-between; }"
    )

    add_qa_card(doc, 10, 
        "Як працює правило repeat(auto-fit, minmax(280px, 1fr))?",
        "Воно автоматично створює стільки колонок по 280px, скільки поміщається в екран, і пропорційно розтягує їх на весь контейнер.",
        "minmax(280px, 1fr) не дає картці стиснутися менше 280px. auto-fit розраховує кількість треків під поточну ширину вікна і згортає порожні, роблячи сітку повністю чуйною без медіа-запитів.",
        ".grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: var(--space-6);\n}"
    )

    add_qa_card(doc, 11, 
        "Чим відрізняється auto-fit від auto-fill у CSS Grid?",
        "Поведінкою при нестачі елементів: auto-fit розтягує наявні колонки на всю ширину, а auto-fill залишає порожні фантомні треки праворуч.",
        "auto-fit 'схлопує' порожні колонки до нульової ширини (collapse empty tracks), тому 2 картки займуть по 50% контейнера. auto-fill залишить під них фіксовані 280px і пусте місце поруч.",
        "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));"
    )

    add_qa_card(doc, 12, 
        "Як працює функція clamp(MIN, PREFERRED, MAX) у типографіці?",
        "Вона обмежує динамічний розмір шрифту між мінімальним та максимальним порогом, плавно масштабуючи його під ширину вікна.",
        "clamp(2rem, 5vw, 3.25rem) обчислює розмір як 5% від ширини екрана (5vw), але на смартфонах не дає йому впасти нижче 2rem (32px), а на великих моніторах — роздутися вище 3.25rem (52px).",
        "--fs-hero: clamp(2rem, 5vw, 3.25rem);"
    )

    add_qa_card(doc, 13, 
        "Що таке .skip-link і якому критерію WCAG 2.2 він відповідає?",
        "Це приховане посилання на початку <body>, що веде на #main і дозволяє клавіатурою пропустити навігацію (WCAG 2.4.1 Bypass Blocks).",
        "Користувачі без мишки змушені натискати Tab 20 разів у шапці, щоб дійти до контенту. Skip-link стає видимим при фокусі і переміщує фокус одразу на <main id='main'>.",
        "<a class=\"skip-link\" href=\"#main\">Перейти до основного вмісту</a>"
    )

    add_qa_card(doc, 14, 
        "Як правильно приховати елемент для очей, але залишити для скрінрідера (.visually-hidden)?",
        "Використовувати CSS-патерн зі стисканням розміру до 1px та clip-path, а не display: none.",
        "display: none повністю видаляє елемент з Accessibility Tree. Патерн .visually-hidden ховає елемент з поля зору, зберігаючи доступність для скрінрідера.",
        ".visually-hidden {\n  position: absolute;\n  width: 1px;\n  height: 1px;\n  clip-path: inset(50%);\n  overflow: hidden;\n}"
    )

    add_qa_card(doc, 15, 
        "Як перевірити кольоровий контраст тексту згідно з WCAG 2.2 AA?",
        "Коефіцієнт контрасту звичайного тексту має бути не менше 4.5:1, а великого — не менше 3:1 (перевіряється в Chrome DevTools або Lighthouse).",
        "Критерій WCAG 1.4.3 Contrast (Minimum) забезпечує читабельність для людей з вадами зору. У ChargeUA для тексту на світлому фоні контраст становить 12.5:1, а на темному — понад 14:1.",
        "/* Контраст 14.8:1 */\ncolor: #FFFFFF; background-color: #0F172A;"
    )

    add_qa_card(doc, 16, 
        "Як працює псевдоклас :focus-visible і чим він кращий за :focus?",
        ":focus-visible вмикає обведення ТІЛЬКИ при клавіатурній навігації (Tab) і не показує синю рамку при кліку мишкою.",
        "Це вирішує вічну проблему дизайну: зберігається чистий візуальний вигляд для мишки і гарантується обов'язкова підсвітка фокусу для людей з клавіатурою (WCAG 2.4.7).",
        ":focus-visible {\n  outline: 3px solid var(--color-primary);\n  outline-offset: 2px;\n}"
    )

    add_qa_card(doc, 17, 
        "Навіщо використовувати <link rel='preconnect'> для Google Fonts?",
        "Для прискорення завантаження шрифтів (покращення метрики LCP у Core Web Vitals).",
        "rel='preconnect' заздалегідь встановлює DNS, TCP та TLS з'єднання з серверами Google Fonts до того, як браузер почне завантажувати CSS-файли, що економить 150-300 мс.",
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>"
    )

    add_qa_card(doc, 18, 
        "Чому в ЛР №5 заборонено використовувати сторонні CSS-фреймворки (Bootstrap, Tailwind)?",
        "Метою лабораторної є опанування фундаментальних можливостей нативного CSS3 (Flexbox, Grid, :root), а не використання готових чужих абстракцій.",
        "Чистий CSS демонструє глибоке розуміння блочної моделі браузера, відсутність конфліктів специфічності та 100% відповідність розробленій у ЛР №4 дизайн-системі.",
        "/* Чистий CSS Grid без Bootstrap .col-md-4 */\ndisplay: grid;\ngrid-template-columns: repeat(auto-fit, minmax(280px, 1fr));"
    )

    add_qa_card(doc, 19, 
        "Що означає перехід кнопки у VS Code з «((•)) Go Live» на «⊘ Port : 5500»?",
        "Це означає, що локальний сервер Live Server успішно піднято і він веде активну трансляцію сторінки за адресою http://127.0.0.1:5500.",
        "Кнопка у правому нижньому кутку статус-бару VS Code відображає поточний стан розширення ritwickdey.liveserver. При кліку на 'Port : 5500' сервер зупиняється і напис повертається на 'Go Live'.",
        "Гарячі клавіші запуску: Alt + L, потім Alt + O."
    )

    add_qa_card(doc, 20, 
        "Як у нашому проєкті було досягнуто показника 100/100 в аудиті доступності Lighthouse?",
        "Завдяки повній семантичній розмітці HTML5, наявності skip-link, високому контрасту кольорів (> 4.5:1), атрибутам alt для зображень та підтримці :focus-visible.",
        "Усі форми мають зв'язані label for з input id, статуси портів дублюються текстом і кольором (WCAG 1.4.1), а навігація повністю доступна з клавіатури без блокування фокусу.",
        "Lighthouse Accessibility Audit: 100 / 100 | Best Practices: 100 / 100"
    )

    # ---------------- РОЗДІЛ 4: ВИСНОВКИ ----------------
    add_header_styled(doc, "ВИСНОВКИ", 1)
    add_body_p(doc, 
        "1. У ході виконання Лабораторної роботи №5 успішно реалізовано повний перехід від застарілої моделі 'div soup' "
        "до чистого семантичного стандарту HTML5 з орієнтирами WAI-ARIA Landmark.")
    add_body_p(doc, 
        "2. Сформовано сучасну гібридну блочну модель: для глобального двовимірного каркасу та сітки станцій використано "
        "CSS Grid (repeat(auto-fit, minmax(280px, 1fr))), а для шапки, навігації та внутрішнього компонування карток — CSS Flexbox.")
    add_body_p(doc, 
        "3. Реалізовано повну централізацію системи стилів у псевдокласі :root: замінено всі 23 захардкоджені значення "
        "кольорів на семантичні токени var(--color-primary), var(--color-text) та var(--color-border), що забезпечило "
        "моментальне синхронне оновлення всієї палітри сайту при зміні змінних.")
    add_body_p(doc, 
        "4. Інтегровано автентичний статичний фон hero_bg.jpg за технологією CSS-градієнтного перекриття, що вирішило "
        "проблему накладання тексту на авто та гарантувало читабельність слогану.")
    add_body_p(doc, 
        "5. Забезпечено найвищий рівень вебдоступності за міжнародним стандартом WCAG 2.2 AA (підтверджено результатом 100/100 в аудиті Google Lighthouse).")

    # Збереження файлу
    out_docx = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л5_Хід_роботи_та_Контрольні_запитання.docx")
    out_root_docx = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л5_Хід_роботи_та_Контрольні_запитання.docx")
    
    doc.save(out_docx)
    shutil.copy(out_docx, out_root_docx)
    print(f"Master DOCX saved to:\n  - {out_docx}\n  - {out_root_docx}")
    return out_docx

if __name__ == "__main__":
    build_complete_master_document()
