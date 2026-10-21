# -*- coding: utf-8 -*-
"""
Майстер-генератор повного розширеного звіту та інструкції до Лабораторної роботи №5
Включає:
- Титульна сторінка згідно з ДСТУ
- Вступ та технічне завдання
- РОЗДІЛ 1. Детальний покроковий хід роботи (14 Етапів, Кроки 1-30 без пропусків)
  з детальними інструкціями: "Де вибирав", "Що натискав", "Що куди вставляв", "Отриманий результат"
- 16 Скріншотів реального процесу виконання
- РОЗДІЛ 2. Анатомія ключових семантичних та CSS-конструкцій
- РОЗДІЛ 3. Всі 20 контрольних запитань з 3-компонентними відповідями
- РОЗДІЛ 4. Висновки

Автор: Лемішка Андрій Анатолійович, група ПП-24
Викладач: к.т.н., доцент Юрчак Ірина Юріївна
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
    style_normal.font.size = Pt(11.5)
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
    r = p4.add_run("ЗВІТ ТА ДЕТАЛЬНИЙ ХІД РОБОТИ")
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

def add_step_box(doc, step_num, step_title, where_selected, what_clicked, what_inserted, result_text):
    """Створює окремий деталізований блок конкретного кроку з 4 пунктами."""
    p_title = doc.add_paragraph()
    p_title.paragraph_format.keep_with_next = True
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(2)
    r_num = p_title.add_run(f"Крок {step_num}. {step_title}")
    r_num.bold = True
    r_num.font.name = "Times New Roman"
    r_num.font.size = Pt(11.5)
    r_num.font.color.rgb = COLOR_PRIMARY

    tbl = doc.add_table(rows=4, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, "CBD5E1")

    items = [
        ("📍 Де вибирав / що відкрив:", where_selected),
        ("⚙️ Що натиснув / як діяв:", what_clicked),
        ("📝 Що куди вставив / код:", what_inserted),
        ("✅ Отриманий результат:", result_text)
    ]

    for idx, (label, val) in enumerate(items):
        c_lbl = tbl.cell(idx, 0)
        c_val = tbl.cell(idx, 1)
        c_lbl.width = Inches(2.2)
        c_val.width = Inches(4.6)
        set_cell_background(c_lbl, "F8FAFC" if idx % 2 == 0 else "F1F5F9")
        set_cell_background(c_val, "FFFFFF")
        set_cell_margins(c_lbl, top=60, bottom=60, left=90, right=90)
        set_cell_margins(c_val, top=60, bottom=60, left=90, right=90)

        p_l = c_lbl.paragraphs[0]
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        r_l = p_l.add_run(label)
        r_l.bold = True
        r_l.font.name = "Times New Roman"
        r_l.font.size = Pt(10.0)
        r_l.font.color.rgb = COLOR_DARK

        p_v = c_val.paragraphs[0]
        p_v.paragraph_format.space_before = Pt(0)
        p_v.paragraph_format.space_after = Pt(0)
        p_v.paragraph_format.line_spacing = 1.15
        r_v = p_v.add_run(val)
        r_v.font.name = "Times New Roman"
        r_v.font.size = Pt(10.0)
        r_v.font.color.rgb = COLOR_TEXT

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def add_prompt_box(doc, title, prompt_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "F0F7FF")
    set_cell_margins(cell, top=70, bottom=70, left=130, right=130)
    
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
    r_body.font.size = Pt(8.8)
    r_body.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(2)

def add_code_snippet(doc, title, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=60, bottom=60, left=120, right=120)
    
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
    r_c.font.size = Pt(8.5)
    r_c.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def add_screenshot_figure(doc, img_name, caption, width=Inches(5.6)):
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if not os.path.exists(img_path):
        print(f"Warning: Screenshot {img_name} not found in {SCREENSHOTS_DIR}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
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
    set_cell_margins(cell, top=70, bottom=70, left=110, right=110)
    
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
    
    r_q = p.add_run(f"Запитання {num}. {q_text}\n")
    r_q.bold = True
    r_q.font.name = "Times New Roman"
    r_q.font.size = Pt(11.0)
    r_q.font.color.rgb = COLOR_PRIMARY
    
    r_s_tag = p.add_run("\n🎯 Коротка відповідь (на захисті): ")
    r_s_tag.bold = True
    r_s_tag.font.name = "Times New Roman"
    r_s_tag.font.size = Pt(10.0)
    r_s_tag.font.color.rgb = RGBColor(0x06, 0x5F, 0x46)
    
    r_s_txt = p.add_run(short_ans + "\n")
    r_s_txt.font.name = "Times New Roman"
    r_s_txt.font.size = Pt(10.0)
    
    r_d_tag = p.add_run("\n📚 Поглиблене академічне пояснення: ")
    r_d_tag.bold = True
    r_d_tag.font.name = "Times New Roman"
    r_d_tag.font.size = Pt(10.0)
    r_d_tag.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)
    
    r_d_txt = p.add_run(deep_ans + "\n")
    r_d_txt.font.name = "Times New Roman"
    r_d_txt.font.size = Pt(10.0)
    
    if code_sample:
        r_c_tag = p.add_run("\n💻 Приклад у проєкті ChargeUA:\n")
        r_c_tag.bold = True
        r_c_tag.font.name = "Times New Roman"
        r_c_tag.font.size = Pt(9.5)
        r_c_tag.font.color.rgb = RGBColor(0x37, 0x41, 0x51)
        
        r_c_txt = p.add_run(code_sample)
        r_c_txt.font.name = "Consolas"
        r_c_txt.font.size = Pt(8.5)
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
        "рефакторингу стильового коду, а також забезпеченню відповідності міжнародним критеріям доступності WCAG 2.2 AA (Lighthouse 100/100).")
    
    table_intro = doc.add_table(rows=5, cols=2)
    table_intro.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_intro, "E2E8F0")
    intro_rows = [
        ("Об'єкт розробки:", "Вебплатформа єдиної національної мережі швидкісних зарядних станцій електромобілів «ChargeUA»"),
        ("Мета роботи:", "Перетворити несемантичну модель на чистий валідний HTML5-документ, винести всі дизайн-токени бренду в :root, побудувати адаптивну сітку на Flexbox/Grid та успішно захистити роботу"),
        ("Обмеження етапу:", "Суворе дотримання вимог ЛР №5: 0% стороннього JavaScript (чистий семантичний HTML/CSS), заборона використання CSS-фреймворків (Bootstrap, Tailwind)"),
        ("Інструменти ШІ:", "Claude 3.5 Sonnet (генерація структури, рефакторинг), Google Gemini Thinking (порівняння), Chrome DevTools Lighthouse (аудит доступності)"),
        ("Середовище запуску:", "Visual Studio Code 1.95+, локальний вебсервер Live Server (ritwickdey.liveserver на порті 5500), Google Chrome")
    ]
    for idx, (lbl, val) in enumerate(intro_rows):
        c0 = table_intro.cell(idx, 0)
        c1 = table_intro.cell(idx, 1)
        c0.width = Inches(1.8)
        c1.width = Inches(5.0)
        set_cell_background(c0, "F8FAFC")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(lbl)
        r0.bold = True
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10.0)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10.0)

    p_after_intro = doc.add_paragraph()
    p_after_intro.paragraph_format.space_before = Pt(4)
    p_after_intro.paragraph_format.space_after = Pt(4)

    add_screenshot_figure(doc, "00_vscode_environment.png", 
        "Рис. 1. Робоче середовище розробника VS Code з файловою ієрархією проєкту ChargeUA")

    # ---------------- РОЗДІЛ 1: ХІД РОБОТИ (ВСІ 14 ЕТАПІВ, КРОКИ 1-30) ----------------
    add_header_styled(doc, "РОЗДІЛ 1. ДЕТАЛЬНИЙ ПОКРОКОВИЙ ХІД ВИКОНАННЯ РОБОТИ (ЕТАПИ 1–14, КРОКИ 1–30)", 1)
    add_body_p(doc, 
        "Нижче наведено вичерпний опис кожного окремого етапу та кроку розробки без пропусків. Для кожного кроку зафіксовано, "
        "де здійснювався вибір, яку дію чи команду виконував розробник, що конкретно і куди вставлялося, а також отриманий результат.")

    # Етап 1
    add_header_styled(doc, "Етап 1. Підготовка середовища, структури каталогів та файлової ієрархії", 2)
    add_body_p(doc, "На цьому етапі підготовлено базовий ізольований робочий простір для виконання ЛР №5.")
    
    add_step_box(doc, 1, "Створення робочого каталогу та структури папок проєкту",
        "VS Code / Провідник Windows у шляху D:\\Studing\\SecondYear\\FirstSemester\\web\\lab5",
        "Створено нову папку lab-05-semantic-layout, а всередині неї — підпапки css/, assets/images/, assets/icons/, screenshots/.",
        "Файлова ієрархія для розміщення вихідних кодів, стилів, зображень та звітної документації.",
        "Сформовано чистий ізольований каталог без конфліктів із попередніми лабораторними роботами.")

    add_step_box(doc, 2, "Імпорт та перевірка графічних активів бренду ChargeUA",
        "Каталог lab4/05_figma_exports та materials/",
        "Скопійовано логотипи (Logo.svg, Logo-white.svg, logo.png), карту Львова (map_lviv.jpg), іконки (Calculator.svg, Location.svg, Information.svg).",
        "Перенесено у каталог lab-05-semantic-layout/assets/images/ та assets/icons/.",
        "Усі графічні ресурси доступні для локального відносного підключення у верстці.")

    add_step_box(doc, 3, "Налаштування середовища розробника та перевірка розширень VS Code",
        "Вікно розширень VS Code (Extensions: Ctrl+Shift+X)",
        "Перевірено наявність та статус активності розширення Ritwick Dey Live Server (ritwickdey.liveserver, v5.7.9).",
        "Увімкнено нижній статус-бар (Status Bar) для візуалізації кнопки підняття локального сервера.",
        "Редактор VS Code повністю готовий до верстки з підтримкою Hot Reload.")

    # Етап 2
    add_header_styled(doc, "Етап 2. Початковий каркас сторінки на div-контейнерах (Div-Soup)", 2)
    add_body_p(doc, "Згідно з методичними вказівками, для демонстрації проблеми «div soup» перед рефакторингом спочатку було згенеровано навмисно несемантичний каркас.")

    add_step_box(doc, 4, "Формулювання інженерного промпту для створення несемантичного каркаса",
        "Діалогове вікно вебклієнта Claude 3.5 Sonnet (Anthropic)",
        "Введено рольову установку Senior Frontend Developer та сформульовано вимоги до структури сайту на базі виключно <div> тегів.",
        "Текст Промпту 1 (наведено у блоці нижче).",
        "Модель згенерувала автономний HTML-код сторінки без використання семантичних тегів HTML5.")

    add_prompt_box(doc, "Промпт 1. Створення навчального каркаса Div-Soup",
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

    # Етап 3
    add_header_styled(doc, "Етап 3. Формування та збереження вихідного файлу index_div_soup.html", 2)
    
    add_step_box(doc, 5, "Збереження та аналіз структури файлу index_div_soup.html",
        "VS Code: Створення нового файлу в lab-05-semantic-layout/",
        "Натиснуто New File -> введено назву index_div_soup.html.",
        "Вставлено згенерований ШІ код (понад 42 контейнери div, класи .site-header-wrap, .nav-wrap, .catalog-wrap).",
        "Файл збережено на диску для використання як контрольний зразок до рефакторингу.")

    add_screenshot_figure(doc, "01_prompt1_div_code_claude.png", 
        "Рис. 3. Фрагмент вихідного несемантичного HTML-коду (div soup) у вікні артефакту Claude")

    # Етап 4
    add_header_styled(doc, "Етап 4. Порівняльне тестування ШІ-моделей (Claude vs Gemini Thinking)", 2)
    
    add_step_box(doc, 6, "Тестування промпту в Google Gemini Thinking під освітнім акаунтом LPNU",
        "Браузер Chrome: Google Gemini Advanced з активованим корпоративним профілем andrii.lemishka.pp.2025@lpnu.ua",
        "Вставлено ідентичний текст Промпту 1 у вікно Gemini та натиснуто кнопку відправки.",
        "Промпт 1 без змін.",
        "Спрацював системний фільтр освітнього профілю Google Workspace («Функції обмежено»), зафіксовано різницю між публічними та академічними AI-профілями.")

    add_screenshot_figure(doc, "01_prompt1_gemini_comparison.png", 
        "Рис. 4. Порівняльний аналіз запиту в Google Gemini Thinking (фіксація системного фільтра)")

    # Етап 5
    add_header_styled(doc, "Етап 5. Аудит дерева доступності (Accessibility Tree) несемантичного каркаса", 2)
    
    add_step_box(doc, 7, "Інспектування DOM-дерева несемантичної моделі в Chrome DevTools",
        "Google Chrome: DevTools (F12) -> вкладка Elements -> бічна панель Accessibility",
        "Клікнуто по черзі на блоки .site-header-wrap, .nav-wrap та .catalog-wrap.",
        "Перевірка властивостей Role, Name, Description у дереві доступності.",
        "Виявлено критичні проблеми: всі вузли мають тип 'generic', скрінрідери не бачать орієнтирів (banner, main, contentinfo), навігація з клавіатури неможлива.")

    # Етап 6
    add_header_styled(doc, "Етап 6. Семантичний рефакторинг та впровадження стандарту HTML5", 2)
    add_body_p(doc, "На цьому етапі здійснено кардинальну перебудову коду: заміну технічних обгорток div на семантичні вузли W3C.")

    add_step_box(doc, 8, "Формулювання промпту для семантичного рефакторингу коду",
        "Діалогове вікно Claude 3.5 Sonnet",
        "Задано роль Senior Frontend Developer & Accessibility Specialist та сформульовано вимоги рефакторингу за стандартом WCAG 2.2 AA.",
        "Текст Промпту 2 (наведено нижче).",
        "Модель сформувала семантичний код index.html та структурований звіт про проведені заміни.")

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
        "Рис. 5. Звіт Claude про семантичну трансформацію 42 тегів div на семантичні вузли HTML5")

    add_step_box(doc, 9, "Збереження семантичного файлу index.html у VS Code",
        "VS Code: Файл lab-05-semantic-layout/index.html",
        "Створено файл index.html, скопійовано код від Claude та збережено (Ctrl+S).",
        "Розмітка: <header>, <nav aria-label='Головна навігація'>, <main id='main'>, <section id='stations'>, <article class='card'>, <aside>, <footer>.",
        "Отримано валідний семантичний документ з повною підтримкою ARIA Landmark Roles.")

    # Етап 7
    add_header_styled(doc, "Етап 7. Реалізація спеціальних механізмів вебдоступності a11y (WCAG 2.2 AA)", 2)
    add_body_p(doc, "Ручні доопрацювання студента для забезпечення повної доступності для скрінрідерів та клавіатурної навігації.")

    add_step_box(doc, 10, "Впровадження механізму швидкої навігації .skip-link (WCAG 2.4.1)",
        "VS Code: файл index.html, одразу після відкриваючого тегу <body>",
        "Додано рядок: <a class=\"skip-link\" href=\"#main\">Перейти до основного вмісту</a>.",
        "У style.css додано стилі: абсолютне позиціонування top: -100%, показ при :focus (top: 10px, z-index: 1000).",
        "Користувач клавіатури першим натисканням Tab бачить кнопку переходу одразу до контенту, минаючи шапку.")

    add_step_box(doc, 11, "Додавання прихованих описів для скрінрідерів .visually-hidden (WCAG 2.4.4)",
        "VS Code: картки станцій у index.html",
        "Вставлено теги <span class=\"visually-hidden\">до станції «Київ, ТРЦ Центральний»</span> всередину посилань дій.",
        "У CSS додано клас .visually-hidden (clip: rect(0 0 0 0), clip-path: inset(50%), overflow: hidden).",
        "Екранні диктори озвучують повну контекстну дію замість сухого 'Детальніше', усуваючи неоднозначність.")

    add_step_box(doc, 12, "Семантичний опис характеристик Hero через <dl>, <dt>, <dd>",
        "VS Code: Hero-блок файлу index.html",
        "Замінено звичайні спани на семантичний список визначень <dl class=\"stats-list\">.",
        "Вставлено пари: <dt>Потужність</dt><dd>до 320 кВт</dd>, <dt>Мережа</dt><dd>140+ станцій</dd>.",
        "Семантична зв'язка термін-значення правильно зчитується пошуковими ботами та скрінрідерами.")

    # Етап 8
    add_header_styled(doc, "Етап 8. Оцифрування дизайн-системи та оголошення токенів у :root", 2)
    
    add_step_box(doc, 13, "Створення файлу css/style.css та конфігурація дизайн-токенів у :root",
        "VS Code: створення файлу lab-05-semantic-layout/css/style.css",
        "Прописано селектор :root та згруповано всі токени бренду ChargeUA (кольори, відступи, радіуси, тіні, типографіка).",
        "CSS Custom Properties (наведено у лістингу нижче).",
        "Створено централізоване сховище параметрів оформлення; будь-яка зміна токена миттєво оновлює весь сайт.")

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
        "Рис. 6. Редактор VS Code з файлом css/style.css та оголошеними токенами")

    # Етап 9
    add_header_styled(doc, "Етап 9. Побудова адаптивного макета на Flexbox та CSS Grid", 2)
    
    add_step_box(doc, 14, "Базовий CSS Reset та налаштування поведінки клавіатурного фокусу",
        "VS Code: файл css/style.css, розділ 2 (Reset & Base)",
        "Прописано універсальне скидання box-sizing, smooth scroll та псевдоклас :focus-visible.",
        "Код: *, *::before, *::after { box-sizing: border-box; } :focus-visible { outline: 3px solid var(--color-primary); outline-offset: 2px; }.",
        "Усунуто небажані відступи браузера, забезпечено видимий контур фокусу лише при навігації клавіатурою (Tab).")

    add_step_box(doc, 15, "Реалізація одновимірних модулів інтерфейсу на CSS Flexbox",
        "VS Code: стилізація класів .header-inner, .nav-list, .card у css/style.css",
        "Задано display: flex для шапки (justify-content: space-between), меню навігації (gap: var(--space-5)) та карток станцій (flex-direction: column).",
        "Вирівнювання компонентів в один рядок або стовпчик з рівномірним розподілом проміжків.",
        "Шапка адаптивно реагує на зміну розміру вікна, кнопка дії у картках надійно притиснута донизу.")

    add_step_box(doc, 16, "Побудова двовимірної сітки каталогу станцій на CSS Grid",
        "VS Code: селектор .grid у css/style.css",
        "Впроваджено функцію repeat(auto-fit, minmax(280px, 1fr)) із gap: var(--space-6).",
        "CSS Grid без жодних сторонніх CSS-фреймворків (no Bootstrap).",
        "Повністю адаптивна матриця карток, що самостійно трансформується з 4 колонок у 2 або 1 залежно від ширини екрана.")

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
        "Рис. 7. Генерація модулів Flexbox та Grid у стильовому документі style.css")

    # Етап 10
    add_header_styled(doc, "Етап 10. Базова стилізація та інтеграція статичного фону Hero", 2)
    
    add_step_box(doc, 17, "Інтеграція статичного бекграунду hero_bg.jpg через CSS оверлей",
        "VS Code: селектор .hero у css/style.css",
        "Сформовано властивість background-image, яка поєднує linear-gradient(90deg, rgba(...) 0%, rgba(...) 100%) та url('../assets/images/hero_bg.jpg').",
        "Параметри: background-size: cover; background-position: center right; background-repeat: no-repeat;.",
        "Фото електромобіля чітко видно праворуч, а зліва створено плавне затемнення, що гарантує 100% читабельність білого тексту слогану.")

    add_screenshot_figure(doc, "04_browser_desktop_view.png", 
        "Рис. 8. Стилізована Hero-секція з автентичним фоном hero_bg.jpg")

    # Етап 11
    add_header_styled(doc, "Етап 11. Підключення Google Fonts та Font Awesome 6", 2)
    
    add_step_box(doc, 18, "Оптимізоване підключення шрифтів Google Fonts через preconnect",
        "VS Code: секція <head> файлу index.html",
        "Вставлено теги <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"> та gstatic з атрибутом crossorigin, а також підключено шрифт Inter.",
        "Шрифтовий лінк: https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap.",
        "DNS/TLS-з'єднання встановлюється заздалегідь, завантаження шрифту прискорюється на 200 мс, шрифт Inter застосовано до body.")

    add_step_box(doc, 19, "Підключення CDN векторних іконок Font Awesome 6",
        "VS Code: секція <head> index.html та розмітка секцій",
        "Підключено all.min.css версії 6.5.1 через CDN cdnjs.cloudflare.com.",
        "Додано іконки <i class=\"fa-solid fa-charging-station\" aria-hidden=\"true\"></i> до кнопок, фільтрів та карток.",
        "Усі графічні символи завантажуються бездоганно, атрибут aria-hidden захищає екранні диктори від зайвого шуму.")

    add_screenshot_figure(doc, "03_prompt3_html_semantic_code_claude.png", 
        "Рис. 9. Фрагмент секції <head> файлу index.html з підключеними шрифтами та CDN")

    # Етап 12
    add_header_styled(doc, "Етап 12. Рефакторинг та повна оптимізація кольорів CSS (Колірний аудит)", 2)
    add_body_p(doc, "На цьому етапі реалізовано вимогу користувача щодо повного усунення хардкод-кольорів та очищення шапки.")

    add_step_box(doc, 20, "Очищення шапки сайту від сторонньої смуги телеметрії",
        "VS Code: файли index.html та css/style.css",
        "Видалено блок темної верхньої плашки (top telemetry bar) та відповідні класи .topbar.",
        "Очищення коду розмітки та стилів.",
        "Шапка набула чистого, естетичного та лаконічного вигляду згідно з прототипом Figma.")

    add_step_box(doc, 21, "Аудит захардкодzone-кольорів у файлі style.css",
        "VS Code: панель пошуку по файлу (Ctrl+F) у css/style.css",
        "Здійснено пошук значень #0077E6, #005EC9, #0F172A, #334155, #64748B, #E2E8F0.",
        "Виявлено 23 входження хардкод-синього кольору, 15 текстових кольорів та 6 рамок, прописаних напряму.",
        "Складено повний реєстр елементів для переведення на глобальні дизайн-токени :root.")

    add_step_box(doc, 22, "Масова заміна хардкод-значень на семантичні токени :root",
        "VS Code: масова заміна по виділеному файлу css/style.css",
        "Замінено всі 23 входження #0077E6 на var(--color-primary), #0F172A на var(--color-text), #64748B на var(--color-muted), рамки — на var(--color-border).",
        "CSS-правила для кнопок, бейджів, рамок фільтрів, карток та іконок.",
        "100% кольорів сайту тепер живляться виключно від змінних у блоці :root.")

    add_step_box(doc, 23, "Додавання правила наслідування кольорів для елементів форми",
        "VS Code: блок базових стилів у css/style.css",
        "Додано правило: input, select, textarea, button { font-family: inherit; color: inherit; }.",
        "Усунення скидання кольорів браузером за замовчуванням для полів вводу.",
        "Зміна змінної :root моментально перефарбовує як звичайний текст, так і селекти, інпути та форми.")

    add_screenshot_figure(doc, "08_clean_header_without_topbar.png", 
        "Рис. 10. Оновлена шапка сайту без зайвих смуг після повного колірного рефакторингу")

    # Етап 13
    add_header_styled(doc, "Етап 13. Запуск, налаштування та верифікація Live Server у VS Code", 2)
    add_body_p(doc, "Тестування локального вебсервера для забезпечення безперервної трансляції сторінки при верстці.")

    add_step_box(doc, 24, "Запуск розширення Live Server через статус-бар VS Code",
        "Нижній правий куток робочої області VS Code (Status Bar)",
        "Наведено курсор миші та виконано лівий клік на кнопку «((•)) Go Live» (або натиснуто Alt+L, Alt+O).",
        "Команда розширення ritwickdey.liveserver: Open with Live Server.",
        "Ініціалізовано внутрішній Node.js HTTP-вебсервер; статус кнопки перейшов у «⊘ Port : 5500».")

    add_screenshot_figure(doc, "06_vscode_go_live_button.png", 
        "Рис. 11. Кнопка «Go Live» у правому нижньому кутку статус-бару VS Code")

    add_step_box(doc, 25, "Відображення та перевірка сайту за адресою http://127.0.0.1:5500",
        "Браузер Google Chrome: адресний рядок URL",
        "Автоматично відкрито вкладку http://127.0.0.1:5500/lab-05-semantic-layout/index.html.",
        "Перевірка відображення блоків, рендерингу hero_bg.jpg, стилів шрифту Inter та іконок Font Awesome.",
        "Сайт успішно відображається; вебсокети Hot Reload забезпечують моментальне оновлення сторінки без натискання F5.")

    add_screenshot_figure(doc, "06_vscode_port_5500_active.png", 
        "Рис. 12. Фіксація активного сокета ⊘ Port : 5500 у статус-барі VS Code")

    add_screenshot_figure(doc, "07_browser_chargeua_port_5500.png", 
        "Рис. 13. Рендеринг вебплатформи ChargeUA у браузері Chrome за адресою 127.0.0.1:5500")

    add_step_box(doc, 26, "Тестування процедури коректної зупинки сервера",
        "Статус-бар VS Code: активний індикатор «⊘ Port : 5500»",
        "Виконано повторний клік по напису «⊘ Port : 5500».",
        "Команда Live Server: Stop Live Server.",
        "Сокет закрито, з'єднання розірвано, кнопка повернулася в початковий стан «((•)) Go Live».")

    # Етап 14
    add_header_styled(doc, "Етап 14. Аудит доступності WCAG 2.2 AA у Lighthouse, освітній портал та фіналізація", 2)
    
    add_step_box(doc, 27, "Проведення аудиту доступності Google Lighthouse у Chrome DevTools",
        "Google Chrome: DevTools -> панель Lighthouse",
        "Обрано категорії Accessibility та Best Practices, профіль Desktop, натиснуто «Analyze page load».",
        "Автоматизована перевірка контрастності, семантичної структури, ARIA-атрибутів та міток форм.",
        "Досягнуто найвищого результату: Accessibility — 100 / 100, Best Practices — 100 / 100!")

    add_step_box(doc, 28, "Розробка інтерактивного навчального вебпорталу підготовки у папці preparing/",
        "Каталог D:\\Studing\\SecondYear\\FirstSemester\\web\\preparing",
        "Створено автономний навчальний портал: index.html (теорія, анатомія коду), style.css (адаптив, темна/світла теми), app.js (пошук, квіз).",
        "Повний інтерактивний комплект навчальних матеріалів для швидкої підготовки до захисту ЛР №5.",
        "Створено повноцінний освітній вебсайт із живою демонстрацією семантики та CSS-змінних.")

    add_step_box(doc, 29, "Публікація навчального порталу на хмарній платформі Netlify",
        "Хмарний сервіс Netlify Drop (Netlify CDN Hosting)",
        "Розгорнуто навчальний вебпортал із публічною постійною адресою.",
        "Деплой продакшн-білда: http://phenomenal-mooncake-af82f0.netlify.app.",
        "Портал доступний 24/7 з будь-якого комп'ютера чи смартфона для демонстрації викладачу.")

    add_step_box(doc, 30, "Формування підсумкового звіту та синхронізація з репозиторієм Git",
        "Термінал PowerShell / Python-генератор Word COM",
        "Виконано скрипт generate_master_lab5_pdf.py для збірки DOCX та трансляції у PDF.",
        "Команди: git add ., git commit -m '...', git push origin main.",
        "Звіт оформлено згідно з ДСТУ, всі матеріали синхронізовано з віддаленим репозиторієм GitHub.")

    # ---------------- РОЗДІЛ 2: АНАТОМІЯ КОДУ ----------------
    add_header_styled(doc, "РОЗДІЛ 2. АНАТОМІЯ КЛЮЧОВИХ СЕМАНТИЧНИХ ТА CSS-КОНСТРУКЦІЙ", 1)
    add_body_p(doc, 
        "Нижче наведено технічний розбір ключових рішень семантики та стилізації, реалізованих у проєкті ChargeUA, "
        "які забезпечили найвищу оцінку аудиту та бездоганну роботу інтерфейсу.")

    add_code_snippet(doc, "1. Механізм швидкого пропуску навігації (.skip-link)",
        "/* index.html: одразу після <body> */\n"
        "<a class=\"skip-link\" href=\"#main\">Перейти до основного вмісту</a>\n\n"
        "/* css/style.css: прихована до натискання Tab */\n"
        ".skip-link {\n"
        "  position: absolute;\n"
        "  top: -100%;\n"
        "  left: var(--space-4);\n"
        "  background: var(--color-primary);\n"
        "  color: #FFFFFF;\n"
        "  padding: var(--space-3) var(--space-4);\n"
        "  z-index: 1000;\n"
        "  transition: top 0.2s ease;\n"
        "}\n"
        ".skip-link:focus {\n"
        "  top: var(--space-4);\n"
        "}"
    )

    add_code_snippet(doc, "2. Приховані підписи для скрінрідерів (.visually-hidden)",
        ".visually-hidden {\n"
        "  position: absolute;\n"
        "  width: 1px;\n"
        "  height: 1px;\n"
        "  padding: 0;\n"
        "  margin: -1px;\n"
        "  overflow: hidden;\n"
        "  clip: rect(0, 0, 0, 0);\n"
        "  white-space: nowrap;\n"
        "  border: 0;\n"
        "}"
    )

    add_code_snippet(doc, "3. Адаптивна типографіка без медіа-запитів через clamp()",
        "h1, .hero-title {\n"
        "  font-size: clamp(1.75rem, 4vw, 2.75rem);\n"
        "  line-height: 1.15;\n"
        "}\n"
        "/* clamp(MIN, VAL, MAX) гарантує:\n"
        "   - на мобільних (320px) шрифт не буде меншим за 28px;\n"
        "   - на десктопі (1440px) не перевищить 44px;\n"
        "   - на планшетах плавно масштабується без різких стрибків! */"
    )

    # ---------------- РОЗДІЛ 3: 20 КОНТРОЛЬНИХ ЗАПИТАНЬ ----------------
    add_header_styled(doc, "РОЗДІЛ 3. ПОВНИЙ КОМПЛЕКТ КОНТРОЛЬНИХ ЗАПИТАНЬ ТА ЕТАЛОННИХ ВІДПОВІДЕЙ (ВСІ 20 ЗАПИТАНЬ)", 1)
    add_body_p(doc, 
        "Цей розділ містить вичерпні відповіді на всі 20 контрольних запитань до Лабораторної роботи №5. "
        "Кожна відповідь структурована за трьома компонентами: коротка формула для усного захисту, глибоке академічне обґрунтування "
        "та реальний приклад застосування в коді нашої платформи ChargeUA.")

    add_qa_card(doc, 1, 
        "Що таке семантична верстка і чому використання виключно тегів <div> («div soup») є поганою практикою?",
        "Семантична верстка — це використання тегів HTML відповідно до їхнього змістовного призначення (<header>, <main>, <article>), а не зовнішнього вигляду.",
        "Використання виключно тегів <div> позбавляє DOM-дерево змісту. Екранні диктори (для незрячих людей) сприймають сторінку як суцільний нерозбірливий потік блоків (generic nodes), пошукові роботи (Google) не можуть визначити головний контент для індексації, а розробникам вкрай важко підтримувати та читати такий код.",
        "<!-- Погано (div soup): -->\n<div class=\"header\"><div class=\"nav\">...</div></div>\n\n<!-- Ідеально (семантично в ChargeUA): -->\n<header class=\"site-header\"><nav class=\"nav\">...</nav></header>"
    )

    add_qa_card(doc, 2, 
        "Яка принципова різниця між елементами <section> та <article>?",
        "<article> є абсолютно автономним незалежним матеріалом (можна вирізати і вставити на інший сайт), а <section> — це просто логічний тематичний розділ більшого документа.",
        "<article> представляє завершену сутність: статтю блогу, картку товару, відгук або картку зарядної станції. <section> групує пов'язаний вміст (наприклад, секція фільтрів, секція контактів) і, за правилами W3C, ЗАВЖДИ повинна містити всередині заголовок (h2–h6).",
        "<!-- Секція каталогу містить автономні картки станцій: -->\n<section class=\"section\" id=\"stations\">\n  <h2>Швидкісні хаби</h2>\n  <article class=\"card\">...</article>\n</section>"
    )

    add_qa_card(doc, 3, 
        "Коли слід використовувати тег <aside>?",
        "Для контенту, який дотично пов'язаний з основним змістом, але може бути вилучений без втрати сенсу головної сторінки.",
        "У специфікації HTML5 <aside> використовується для бічних панелей (сайдбарів), блоків фільтрації каталогу, приміток, блоків цитат або рекламних віджетів. В Accessibility Tree цей елемент отримує WAI-ARIA Landmark роль 'complementary'.",
        "<aside class=\"map-filters\" aria-label=\"Фільтри зарядних станцій\">\n  <h3>Фільтрація за типом порту</h3>\n  <!-- Фільтри CCS2, Type2, CHAdeMO -->\n</aside>"
    )

    add_qa_card(doc, 4, 
        "Чому на сторінці повинен бути лише один заголовок <h1> і як правильно вибудовувати ієрархію h1–h6?",
        "<h1> визначає головну тему всієї вебсторінки. Один <h1> необхідний для коректного SEO та навігації скрінрідерів.",
        "Заголовки утворюють деревоподібний скелет сторінки. Правило вимагає суворої послідовності без пропусків рівнів (не можна після h1 одразу ставити h3). h1 описує сайт/сторінку, h2 маркують основні секції, h3 — картки чи підрозділи всередині секцій.",
        "<h1>ChargeUA — Мережа швидкісних зарядних станцій</h1> <!-- Єдиний на сторінці -->\n  <h2>Каталог станцій</h2>\n    <h3>Київ, ТРЦ River Mall</h3>\n    <h3>Львів, пл. Ринок</h3>"
    )

    add_qa_card(doc, 5, 
        "Яке золоте правило вибору між тегами <button> та <a> (посилання)?",
        "<a> — переходить кудись (зміна URL чи скрол до якоря); <button> — виконує дію на сторінці без переходу.",
        "Використовуйте <a href=\"...\">, коли змінюється стан маршрутизатора, відкривається нова сторінка або здійснюється перехід до секції (#map). Використовуйте <button type=\"button\">, коли відкривається модальне вікно, змінюється фільтр станцій, запускається розрахунок калькулятора або надсилається форма (type=\"submit\").",
        "<a href=\"#stations\" class=\"btn\">Переглянути станції</a> <!-- Перехід -->\n<button type=\"button\" class=\"btn\">Забронювати конектор</button> <!-- Дія -->"
    )

    add_qa_card(doc, 6, 
        "Навіщо потрібен псевдоклас :root у CSS і чим він відрізняється від селектора html?",
        ":root представляє кореневий елемент дерева документа (<html>) і слугує глобальним сховищем для CSS Custom Properties (змінних).",
        "Хоча :root обирає той самий елемент, що й html, псевдоклас :root має вищу специфічність (specificity 0,0,1,0 проти 0,0,0,1 у тега html). Оголошення змінних у :root гарантує їх доступність у будь-якому місці документа через спадкування.",
        ":root {\n  --color-primary: #005EC9;\n  --space-4: 16px;\n}\n\n.btn {\n  background: var(--color-primary);\n}"
    )

    add_qa_card(doc, 7, 
        "Як працюють призначені для користувача властивості CSS (CSS Custom Properties) та яка функція var()?",
        "Це змінні в нативному CSS. Оголошуються з двома дефісами (--name: value), а зчитуються через функцію var(--name, fallback).",
        "На відміну від змінних SASS/SCSS, CSS Custom Properties є живими (динамічними): вони існують у runtime браузера, беруть участь у каскаді, успадковуються дочірніми елементами і можуть миттєво змінюватися через класи або JavaScript.",
        ":root {\n  --brand: #005EC9;\n}\n.card {\n  /* Якщо --brand не знайдено, буде використано синій колір */\n  border-color: var(--brand, #0077E6);\n}"
    )

    add_qa_card(doc, 8, 
        "У чому полягає фундаментальна відмінність між CSS Flexbox та CSS Grid?",
        "Flexbox — одновимірний (1D, керує або рядком, або стовпчиком); CSS Grid — двовимірний (2D, одночасно керує і рядками, і стовпчиками).",
        "Flexbox компонує елементи від їхнього внутрішнього вмісту (content-first) вздовж головної осі (main-axis). Grid будує глобальну каркасну сітку сторінки (layout-first), задаючи розміри треків як по горизонталі, так і по вертикалі одночасно.",
        "/* Flexbox для горизонтального меню: */\n.nav-list { display: flex; gap: 16px; }\n\n/* Grid для матриці карток: */\n.grid { display: grid; grid-template-columns: repeat(3, 1fr); }"
    )

    add_qa_card(doc, 9, 
        "Як працює магічне CSS Grid правило: repeat(auto-fit, minmax(280px, 1fr))?",
        "Це правило створює адаптивну сітку карток без жодних @media-запитів.",
        "• repeat() — генерує стовпчики автоматично.\n• auto-fit — створює стільки колонок, скільки поміщається в контейнер, і розтягує наявні на всю ширину (згортаючи порожні треки).\n• minmax(280px, 1fr) — картка ніколи не буде вужчою за 280px, а вільне місце порівну ділиться частками (fr).",
        ".stations-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: 24px;\n}"
    )

    add_qa_card(doc, 10, 
        "Яка різниця між auto-fill та auto-fit у CSS Grid?",
        "auto-fill зберігає порожні стовпчики, якщо для них є місце; auto-fit згортає порожні треки до 0px і розтягує наявні картки.",
        "Якщо у вас 2 картки на великому моніторі 1920px: auto-fill залишить місце для ще 4 уявних колонок (картки залишаться малими), а auto-fit розширить ваші 2 картки на всю доступну ширину екрана.",
        "/* auto-fit гарантує відсутність порожніх дірок у каталозі */\ngrid-template-columns: repeat(auto-fit, minmax(300px, 1fr));"
    )

    add_qa_card(doc, 11, 
        "Навіщо потрібен клас .skip-link і яку вимогу доступності він реалізує?",
        "Це приховане посилання для користувачів клавіатури, що дозволяє миттєво перейти до основного контенту, пропустивши довгу шапку.",
        "Вимога критерію успіху WCAG 2.4.1 «Bypass Blocks» (Рівень A). Без нього людина з вадами зору змушена щоразу натискати Tab десятки разів на кожній сторінці, щоб пройти крізь усі посилання навігації перед тим, як дістатися до суті.",
        "<a class=\"skip-link\" href=\"#main\">Перейти до основного змісту</a>\n\n.skip-link:not(:focus) {\n  position: absolute;\n  left: -9999px;\n}"
    )

    add_qa_card(doc, 12, 
        "Як правильно реалізувати клас .visually-hidden (прихований текст для скрінрідерів)?",
        "Текст ховається візуально з екрана, але залишається доступним для екранних дикторів. Використовувати display: none категорично заборонено!",
        "display: none та visibility: hidden видаляють вузол з Accessibility Tree, тому сліпа людина його не почує. Патерн .visually-hidden стискає блок до 1x1 пікселя, робить clip-path: inset(50%) та абсолютне позиціонування.",
        ".visually-hidden {\n  position: absolute;\n  width: 1px;\n  height: 1px;\n  padding: 0;\n  margin: -1px;\n  overflow: hidden;\n  clip: rect(0, 0, 0, 0);\n  white-space: nowrap;\n  border: 0;\n}"
    )

    add_qa_card(doc, 13, 
        "Що таке адаптивна типографіка через clamp() і як вона працює?",
        "clamp(MIN, VAL, MAX) дозволяє плавно змінювати розмір шрифту залежно від ширини екрана без використання десятків @media-запитів.",
        "Функція приймає три параметри: мінімальний поріг (наприклад, 2rem), бажане відносне значення (4vw — 4% ширини в'юпорту) та максимальний поріг (3.25rem). Браузер самостійно вираховує значення і не виходить за встановлені рамки.",
        ":root {\n  --fs-hero: clamp(1.75rem, 4vw, 2.75rem);\n}\nh1 {\n  font-size: var(--fs-hero);\n}"
    )

    add_qa_card(doc, 14, 
        "Як у нашому проєкті реалізовано статичний фон hero_bg.jpg, щоб він не конфліктував із текстом?",
        "За допомогою CSS-градієнтного оверлею безпосередньо у властивості background-image контейнера .hero.",
        "Використано поєднання linear-gradient(90deg, rgba(15,23,42,0.94) 0%, rgba(15,23,42,0.25) 100%) та фонового зображення url('hero_bg.jpg'). Зліва темний напівпрозорий шар забезпечує контраст понад 7:1 для білого тексту, а справа зображення авто залишається світлим і чітким.",
        ".hero {\n  background-image: \n    linear-gradient(90deg, rgba(15,23,42,0.95), rgba(15,23,42,0.3)),\n    url('../assets/images/hero_bg.jpg');\n  background-size: cover;\n}"
    )

    add_qa_card(doc, 15, 
        "Чому для елементів форми (input, select, button) потрібно явно прописувати color: inherit та font-family: inherit?",
        "Тому що елементи форм за специфікацією браузерів (User Agent Stylesheet) НЕ успадковують шрифти та кольори від батьківського <body>.",
        "Браузери застосовують до <input> та <button> власні застарілі системні стилі (часто шрифт Arial/Segoe UI та власний сірий колір). Правило inherit примушує їх прийняти токени нашої дизайн-системи.",
        "input, select, textarea, button {\n  font-family: inherit;\n  font-size: inherit;\n  color: inherit;\n}"
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
