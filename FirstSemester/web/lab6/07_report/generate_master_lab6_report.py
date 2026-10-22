# -*- coding: utf-8 -*-
"""
Майстер-генератор повного розширеного звіту та інструкції до Лабораторної роботи №6
з навчальної дисципліни «Вебтехнології та вебдизайн»
Тема: «Компонентна верстка, стилізація та адаптивність»
Проєкт: Вебплатформа зарядної мережі електромобілів «ChargeUA»

Автор: студент групи ПП-24 Лемішка Андрій Андрійович
Викладач: к.т.н., доцент кафедри САПР Юрчак Ірина Юріївна
Національний університет «Львівська політехніка» — 2026
"""

import os
import sys
import shutil
import zipfile
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
PROJECT_DIR = os.path.join(BASE_DIR, "lab-06-tailwind-components")

COLOR_PRIMARY = RGBColor(0x00, 0x5E, 0xC9)     # ChargeUA синій (#005EC9)
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
        r_logo.add_picture(coat_path, width=Inches(1.9))

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
    r = p5.add_run("до Лабораторної роботи №6\nз навчальної дисципліни «Вебтехнології та вебдизайн»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13.5)

    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p6.paragraph_format.space_before = Pt(2)
    p6.paragraph_format.space_after = Pt(14)
    r = p6.add_run("«Компонентна верстка, стилізація та адаптивність за допомогою Tailwind CSS,\nмобільно-орієнтований підхід Mobile-First та відповіді на контрольні запитання»")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12.0)
    r.italic = True

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.left_indent = Inches(3.2)
    p_meta.paragraph_format.space_before = Pt(8)
    p_meta.paragraph_format.space_after = Pt(20)
    p_meta.paragraph_format.line_spacing = 1.2
    
    r_meta = p_meta.add_run("Виконав:\n")
    r_meta.bold = True
    r_meta.font.name = "Times New Roman"
    r_meta.font.size = Pt(12)
    
    r_meta2 = p_meta.add_run("студент групи ПП-24\nЛемішка Андрій Андрійович\n\n")
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
    p_city.paragraph_format.space_before = Pt(16)
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

def add_screenshot_figure(doc, img_name, caption, width=Inches(5.8)):
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
    
    r_s_tag = p.add_run("\n🎯 1. Коротка відповідь (для усного захисту): ")
    r_s_tag.bold = True
    r_s_tag.font.name = "Times New Roman"
    r_s_tag.font.size = Pt(10.0)
    r_s_tag.font.color.rgb = RGBColor(0x06, 0x5F, 0x46)
    
    r_s_txt = p.add_run(short_ans + "\n")
    r_s_txt.font.name = "Times New Roman"
    r_s_txt.font.size = Pt(10.0)
    
    r_d_tag = p.add_run("\n📚 2. Поглиблене академічне обґрунтування: ")
    r_d_tag.bold = True
    r_d_tag.font.name = "Times New Roman"
    r_d_tag.font.size = Pt(10.0)
    r_d_tag.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)
    
    r_d_txt = p.add_run(deep_ans + "\n")
    r_d_txt.font.name = "Times New Roman"
    r_d_txt.font.size = Pt(10.0)
    
    if code_sample:
        r_c_tag = p.add_run("\n💻 3. Практична реалізація та приклад у проєкті ChargeUA:\n")
        r_c_tag.bold = True
        r_c_tag.font.name = "Times New Roman"
        r_c_tag.font.size = Pt(10.0)
        r_c_tag.font.color.rgb = COLOR_DARK
        
        r_c_txt = p.add_run(code_sample + "\n")
        r_c_txt.font.name = "Consolas"
        r_c_txt.font.size = Pt(8.5)
        r_c_txt.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def build_complete_master_document():
    doc = Document()
    setup_document_styles(doc)

    # 1. ТИТУЛЬНА СТОРІНКА
    add_title_page(doc)

    # 2. ВСТУП ТА ТЕХНІЧНЕ ЗАВДАННЯ
    add_header_styled(doc, "ВСТУП ТА ТЕХНІЧНЕ ЗАВДАННЯ", 1)
    
    add_body_p(doc, 
        "Лабораторна робота №6 присвячена практичному опануванню компонентної верстки, швидкої стилізації за допомогою утилітарного CSS-фреймворку "
        "Tailwind CSS та забезпеченню бездоганної мобільної адаптивності на основі парадигми Mobile-First. "
        "У ході роботи реалізовано міграцію семантичного каркасу вебплатформи національної мережі швидкісних зарядних станцій електромобілів «ChargeUA» "
        "(створеного в ЛР №5) на сучасні утилітарні класи Tailwind, згенеровано та протестовано ізольовані UI-компоненти, налаштовано брейкпоїнти "
        "адаптивності (sm, md, lg, xl), проведено рефакторинг згенерованого штучним інтелектом коду та виконано комплексне тестування у DevTools, "
        "Lighthouse та хмарному середовищі.",
        "Тематична спрямованість: ")

    add_body_p(doc, 
        "Опанувати концепцію Utility-First CSS, навчитися застосовувати інструменти Tailwind Play та VS Code IntelliSense для швидкого прототипування, "
        "побудувати повноцінний цикл Prompt-to-UI взаємодії з ШІ-моделями (Claude 3.5 Sonnet, Google Gemini, Sequential Thinking MCP), "
        "реалізувати адаптивне гамбургер-меню з доступністю WCAG 2.2 AA (клавіатурний фокус, ARIA-атрибути), перенести токени власної дизайн-системи "
        "з Figma (ЛР №4) у конфігурацію Tailwind, здійснити адаптивне тестування в Chrome DevTools Device Toolbar та перевірити відповідність стандартам W3C.",
        "Мета роботи: ")

    add_body_p(doc, 
        "1) Веббраузер Google Chrome / Microsoft Edge з активними інструментами розробника DevTools (Device Toolbar, Lighthouse, Console, Elements);\n"
        "2) Редактор вихідного коду Visual Studio Code з офіційним розширенням Tailwind CSS IntelliSense;\n"
        "3) Інтерактивна хмарна пісочниця Tailwind Play (play.tailwindcss.com);\n"
        "4) ШІ-асистенти та інженерні протоколи: Claude 3.5 Sonnet, Google Gemini, Sequential Thinking MCP Server, Chrome DevTools MCP;\n"
        "5) Сервіси перевірки стандартів W3C Markup Validation Service та W3C CSS Validation Service;\n"
        "6) Хостингова платформа Netlify для деплою вебдодатку.",
        "Застосоване інженерне середовище: ")

    # 3. РОЗДІЛ 1: ДЕТАЛЬНИЙ ПОКРОКОВИЙ ХІД РОБОТИ (19 ЕТАПІВ)
    add_header_styled(doc, "РОЗДІЛ 1. ДЕТАЛЬНИЙ ПОКРОКОВИЙ ХІД РОБОТИ", 1)

    # Етап 1
    add_header_styled(doc, "Етап 1. Підготовка проєкту та робочого середовища", 2)
    add_step_box(doc, 1, "Створення резервної копії та структурування робочого каталогу",
        "Файловий провідник Windows та термінал PowerShell у каталозі D:\\Studing\\SecondYear\\FirstSemester\\web\\lab6",
        "Виконано копіювання вихідних файлів проєкту ЛР №5 (assets, js, стилі), створено цільовий робочий каталог lab-06-tailwind-components із підкаталогами components, css, js, assets.",
        "Створено файл index.html, скопійовано медіафайли (hero_bg.jpg, map_lviv.jpg, ai_promo_banner.jpg, Logo.svg) та підготовлено файли ізольованих компонентів.",
        "Сформовано автономну структуру проєкту my-web-project, готову для інтеграції утиліт Tailwind CSS.")

    # Етап 2
    add_header_styled(doc, "Етап 2. Знайомство з Tailwind CSS та парадигмою Utility-First", 2)
    add_step_box(doc, 2, "Порівняльний аналіз традиційного CSS проти Utility-First",
        "Офіційна документація tailwindcss.com/docs та код кнопки з ЛР №5",
        "Проаналізовано різницю між написанням власних BEM-класів (.primary-button) та нанизуванням атомарних класів безпосередньо у розмітці.",
        "Зіставлено класичний CSS:\n.primary-button { background-color: #005EC9; padding: 12px 24px; border-radius: 12px; }\nта еквівалентний Tailwind:\nclass=\"bg-blue-600 px-6 py-3 rounded-xl font-semibold text-white hover:bg-blue-700 transition\"",
        "Зрозуміло переваги: відсутність перемикання між файлами CSS та HTML, усунення конфліктів специфічності, автоматичне видалення невикористаного CSS (Purge/JIT).")

    # Етап 3
    add_header_styled(doc, "Етап 3. Підключення Tailwind CSS через Play CDN", 2)
    add_step_box(doc, 3, "Інтеграція офіційного CDN-скрипту та файлу custom-styles.css",
        "Файл index.html всередині секції <head>",
        "Додано тег <script src=\"https://cdn.tailwindcss.com\"></script> та підключено файл користувацьких стилів css/custom-styles.css.",
        "<script src=\"https://cdn.tailwindcss.com\"></script>\n<link rel=\"stylesheet\" href=\"css/custom-styles.css\">",
        "Утиліти Tailwind CSS успішно завантажуються в браузері через офіційний CDN, стилі Preflight нормалізують відступи.")

    # Етап 4
    add_header_styled(doc, "Етап 4. Знайомство з онлайн-пісочницею Tailwind Play", 2)
    add_step_box(doc, 4, "Дослідження інтерфейсу Tailwind Play (play.tailwindcss.com)",
        "Веббраузер Chrome, відкриття ресурсу https://play.tailwindcss.com",
        "Досліджено зони редагування: HTML, CSS, Config/Settings, інтерактивне прев'ю в реальному часі, інструменти зміни ширини viewport (Mobile, Tablet, Desktop) та кнопку генерації лінка Share.",
        "Введено базовий тестовий код:\n<button class=\"bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition\">\n  Замовити зарядку\n</button>",
        "Протестовано інтерактивну реакцію елемента на зміну відступів, кольору та скруглення без локальної компіляції.")

    # Етап 5
    add_header_styled(doc, "Етап 5. Створення першого UI-компонента: Primary CTA Button", 2)
    add_prompt_box(doc, "Промпт генерації кнопки (Button Prompt)", 
        "Ти — Senior Frontend Developer та UI Engineer.\n"
        "Створи Primary CTA Button «Дізнатися більше» за допомогою HTML5 + Tailwind CSS.\n"
        "Використай: синій фон #2563EB, білий текст, 16px / font-semibold, padding 12px 24px, border-radius 12px, hover та active стани, disabled стан, transition, мінімальну висоту 44px.\n"
        "Кнопка має відповідати принципам accessibility (WCAG 2.2 AA).")
    
    add_step_box(doc, 5, "Реалізація та тестування інтерактивних станів кнопки",
        "Каталог components/button.html та пісочниця Tailwind Play",
        "Сформовано компонент із класами min-h-[44px], px-6, py-3, bg-blue-600, hover:bg-blue-700, active:scale-95, focus-visible:ring-4, focus-visible:ring-blue-300.",
        "Додано SVG-іконку стрілки з анімацією зміщення при hover: group-hover:translate-x-1, створено стан disabled з opacity-60 та cursor-not-allowed.",
        "Створено зразок кнопки з повною підтримкою стандартів доступності.")

    add_screenshot_figure(doc, "08_component_button.png", "Рис. 1. Ізольований компонент Primary CTA Button з демонстрацією станів (Default, Disabled, Ghost) та поясненням утиліт")

    # Етап 6
    add_header_styled(doc, "Етап 6. Створення Header з адаптивною навігацією", 2)
    add_prompt_box(doc, "Промпт генерації Header (Navbar Prompt)",
        "Ти — Senior Frontend Developer. Створи ізольований семантичний компонент Header для ChargeUA.\n"
        "Структура: логотип зліва, десктопна навігація по центру (посилання + dropdown «Ресурси»), кнопки входу та дії справа.\n"
        "Адаптивність: на mobile (< 768px) навігація прихована (hidden), показується кнопка гамбургера. На md:flex навігація відображається горизонтально, а гамбургер приховується (md:hidden).\n"
        "Додай ARIA-атрибути та плавні hover/focus ефекти.")

    add_step_box(doc, 6, "Інтеграція шапки сайту та скрипта мобільного меню",
        "Файл components/header.html та секція <header> в index.html",
        "Застосовано контейнер max-w-7xl mx-auto px-4 sm:px-6 lg:px-8, вирівнювання flex items-center justify-between h-20, закріплення sticky top-0 bg-white/95 backdrop-blur-md.",
        "Підключено обробник подій click для mobile-menu-btn, що перемикає aria-expanded та клас hidden на блоці mobile-menu, додано закриття клавішею Escape.",
        "Створено повноцінний адаптивний Navbar з висувним меню для смартфонів.")

    add_screenshot_figure(doc, "09_component_header.png", "Рис. 2. Ізольований компонент Header: логотип, центральні посилання, випадний список та кнопки авторизації")

    # Етап 7
    add_header_styled(doc, "Етап 7. Застосування та розуміння принципу Mobile First", 2)
    add_step_box(doc, 7, "Побудова стилів за принципом Mobile First",
        "CSS-архітектура проєкту та розмітка карток і секцій",
        "Проаналізовано поведінку префіксів Tailwind: базові класи без префікса діють на екранах від 0px (смартфони), а префікси sm: (>=640px), md: (>=768px), lg: (>=1024px) перевизначають стилі для більших дисплеїв на основі медіа-запитів min-width.",
        "Застосовано патерн: class=\"flex flex-col md:flex-row gap-4\", що означає вертикальний стовпчик на смартфонах і горизонтальний ряд на планшетах та десктопах.",
        "Забезпечено відсутність непотрібних медіа-запитів та плавне масштабування інтерфейсу.")

    # Етап 8
    add_header_styled(doc, "Етап 8. Створення інтерактивної Картки зарядної станції (Card)", 2)
    add_prompt_box(doc, "Промпт генерації картки станції (Card Prompt)",
        "Ти — Senior UI Engineer. Створи компонент Card «Картка зарядної станції» для ChargeUA.\n"
        "Картка містить: фото з оверлеєм, бейдж статусу «Вільна (3/4)» з пульсуючою крапкою, бейдж потужності «DC 150 кВт», адресу локації, чіпи конекторів (CCS2, CHAdeMO, Type 2), вартість за кВт·год та кнопку CTA.\n"
        "Використовуй hover:-translate-y-1.5, hover:shadow-2xl, transition-all duration-300.")

    add_step_box(doc, 8, "Розробка семантичного блоку <article> для картки",
        "Файл components/card.html та секція каталогу в index.html",
        "Створено картку на базі тегу <article> з обмежувачем group, заокругленням rounded-2xl, внутрішніми відступами p-6 та ефектом збільшення фото group-hover:scale-105.",
        "Додано ціновий блок з великим шрифтом text-lg font-black та кнопкою min-h-[44px] px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-xl.",
        "Картка отримала привабливий вигляд та плавний відгук на рухи курсора.")

    add_screenshot_figure(doc, "10_component_card.png", "Рис. 3. Ізольований компонент Картка зарядної станції «Victoria Gardens DC-150» із бейджами та конекторами")

    # Етап 9
    add_header_styled(doc, "Етап 9. Створення адаптивної сітки компонентів (Grid)", 2)
    add_step_box(doc, 9, "Компонування каталогу станцій у сітку Grid",
        "Файл components/grid.html та секція #stations у головному файлі",
        "Застосовано контейнер grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8, додано верхню смугу тач-фільтрів з класом overflow-x-auto.",
        "Розміщено 6 карток реальних швидкісних хабів України (Львів Victoria Gardens, Київ Ocean Plaza, траса М-06 Київ-Чоп, Сокільники King Cross Leopolis, Дніпро River Hub, Одеса Port Express).",
        "Сітка бездоганно перелаштовується: 1 колонка на мобільних пристроях, 2 колонки на планшетах та 3 колонки на ноутбуках і десктопах.")

    add_screenshot_figure(doc, "05_adaptive_grid_cards.png", "Рис. 4. Адаптивна сітка карток каталогу хабів ChargeUA у 3-колонковому десктопному компонуванні")

    # Етап 10
    add_header_styled(doc, "Етап 10. Створення 4-колонкового Footer", 2)
    add_prompt_box(doc, "Промпт генерації підвалу (Footer Prompt)",
        "Створи 4-колонковий підвал для сайту ChargeUA на базі HTML5 + Tailwind CSS.\n"
        "Колонка 1: бренд, місія та іконки соцмереж (GitHub, Telegram, LinkedIn).\n"
        "Колонка 2: продукти (DC 150-300 кВт, AC 22 кВт, комерційні хаби, автопарки).\n"
        "Колонка 3: компанія (про нас, енергостійкість, відновлювана енергія, кар'єра, контакти).\n"
        "Колонка 4: підписка на оновлення (форма email + кнопка) та live-індикатор статусу системи («Всі хаби онлайн 100%»).\n"
        "Адаптивність: mobile grid-cols-1, md:grid-cols-2, lg:grid-cols-4. Фон bg-slate-900, текст text-slate-300.")

    add_step_box(doc, 10, "Верстка семантичного підвалу <footer>",
        "Файл components/footer.html та секція <footer> в index.html",
        "Використано тег <footer> з aria-labelledby=\"footer-heading\", контейнером max-w-7xl mx-auto py-16 та сіткою grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10.",
        "Додано форму підписки з полем <input type=\"email\" id=\"footer-email\" required> та бейдж статусу з анімованим маячком animate-ping.",
        "Створено сучасний багатофункціональний підвал відповідно до вимог варіанта бізнес-проєкту.")

    add_screenshot_figure(doc, "07_footer_4_columns.png", "Рис. 5. Чотириколонковий підвал сайту ChargeUA з формою розсилки та індикатором System Status")

    # Етап 11
    add_header_styled(doc, "Етап 11. Тестування компонентів у пісочниці Tailwind Play", 2)
    add_step_box(doc, 11, "Хмарна валідація компонентів на play.tailwindcss.com",
        "Онлайн-середовище Tailwind Play у браузері Chrome",
        "Завантажено код кнопки, шапки, картки та футера у робоче поле HTML, перевірено вкладки Config та Preview.",
        "Протестовано інтерактивні стани кнопок, розкриття меню та зміну розмірів екрана за допомогою повзунка адаптивності вбудованого вікна перегляду.",
        "Підтверджено коректність компіляції всіх утилітарних класів Tailwind без синтаксичних помилок.")

    # Етап 12
    add_header_styled(doc, "Етап 12. Аналіз та рефакторинг ШІ-коду (Refinement Workflow)", 2)
    add_step_box(doc, 12, "Критичний розбір згенерованого коду",
        "Вихідні коди у редакторі VS Code та діалог із ШІ-асистентом",
        "Здійснено пошук: 1) бездоганного рішення, 2) сумнівного рішення, 3) самостійної несанкціонованої зміни ШІ.",
        "1. Бездоганно: використання min-h-[44px] та ring-4 для доступності.\n"
        "2. Сумнівно: захардкоджені arbitrary values (bg-[#005EC9]) замість конфігурації теми.\n"
        "3. Самостійно: додавання незапитаних SVG-іконок стрілочок.\n"
        "Виправлення: винесено кольори у tailwind.config, стандартизовано класи та додано текстові назви для іконок.",
        "Код оптимізовано, позбавлено надлишковості та підготовлено для довгострокової підтримки.")

    # Етап 13
    add_header_styled(doc, "Етап 13. Інтеграція компонентів у проєкт ChargeUA з ЛР №5", 2)
    add_step_box(doc, 13, "Збірка повноцінної головної сторінки index.html",
        "Файл lab-06-tailwind-components/index.html",
        "Об'єднано Header, Hero-секцію з Primary Button, секцію каталогу станцій на адаптивній сітці Grid, інтерактивний калькулятор витрат, Live-карту хабів Leaflet, промо-блок завантаження мобільного додатка та 4-колонковий Footer.",
        "Підключено скрипти навігації (nav.js), Leaflet Map (map.js) та обчислювальний модуль калькулятора (calculator.js).",
        "Сформовано цілісний, працюючий вебдодаток, який повністю зберігає функціонал ЛР №5 і набув сучасної Tailwind-стилізації.")

    add_screenshot_figure(doc, "06_calculator_and_map.png", "Рис. 6. Інтерактивний калькулятор вартості зарядки та географічна карта хабів України")

    # Етап 14
    add_header_styled(doc, "Етап 14. Перенесення дизайн-системи Figma в Tailwind Config", 2)
    add_step_box(doc, 14, "Синхронізація токенів ЛР №4 із конфігурацією теми",
        "Скрипт tailwind.config у <head> файлу index.html та css/custom-styles.css",
        "Перенесено токени кольорів: primary (#005EC9), primary-hover (#004BA0), secondary (#0F172A), accent (#00B4D8), статусні кольори (free #10B981, busy #EF4444, reserved #F59E0B), шрифт Inter та радіуси скруглення.",
        "tailwind.config = {\n  theme: {\n    extend: {\n      colors: {\n        brand: { 500: '#005EC9', 600: '#2563EB', 700: '#1D4ED8', 900: '#0F172A' },\n        accent: { 500: '#00B4D8' }\n      }\n    }\n  }\n}",
        "Дизайн-система з Figma стала доступна як рідні класи Tailwind (bg-brand-500, text-accent-500).")

    # Етап 15
    add_header_styled(doc, "Етап 15. Налаштування адаптивності та брейкпоїнтів", 2)
    add_step_box(doc, 15, "Конфігурація та перевірка поведінки елементів на брейкпоїнтах",
        "Розмітка index.html, перевірка у браузері",
        "Перевірено брейкпоїнти sm (640px), md (768px), lg (1024px), xl (1280px).",
        "Header: mobile -> кнопка гамбургера, md+ -> горизонтальний ряд.\n"
        "Hero: mobile -> вертикальні кнопки, sm+ -> горизонтальні кнопки.\n"
        "Grid карток: mobile -> 1 колонка, md -> 2 колонки, lg -> 3 колонки.\n"
        "Footer: mobile -> 1 колонка, md -> 2 колонки, lg -> 4 колонки.",
        "Інтерфейс плавно адаптується без зламу блоків та горизонтальної смуги прокрутки.")

    # Етап 16
    add_header_styled(doc, "Етап 16. Тестування сумісності в браузері через Chrome DevTools", 2)
    add_step_box(doc, 16, "Тестування у режимі Device Toolbar (Ctrl+Shift+M)",
        "Панель Chrome DevTools, режим Toggle Device Toolbar",
        "Протестовано відображення на мобільних пристроях (iPhone SE 375x812, iPhone 14 Pro 390x844), планшетах (iPad Mini 768x1024) та десктопах (1440x900).",
        "Перевірено роботу тач-подій, відкриття і закриття висувного меню навігації, читабельність типографіки та контрастність тексту.",
        "Підтверджено 100% сумісність та збереження макета на всіх типах пристроїв.")

    add_screenshot_figure(doc, "01_desktop_1440px_overview.png", "Рис. 7. Десктопний вигляд головної сторінки ChargeUA (1440px): Hero-секція, навігація, KPI-статистика")
    add_screenshot_figure(doc, "02_tablet_768px_view.png", "Рис. 8. Планшетний вигляд сторінки (768px): двоколонкова трансформація та адаптивне меню")
    add_screenshot_figure(doc, "03_mobile_375px_hero.png", "Рис. 9. Мобільний вигляд (375px, iPhone SE): компактна шапка з кнопкою гамбургера та вертикальний стек кнопок")
    add_screenshot_figure(doc, "04_mobile_375px_menu_open.png", "Рис. 10. Активне висувне мобільне навігаційне меню (Drawer) з підтримкою клавіатурного закриття Escape")

    # Етап 17
    add_header_styled(doc, "Етап 17. Фінальне рафінування та доступність (WCAG 2.2 AA)", 2)
    add_step_box(doc, 17, "Покращення семантики HTML5 та доступності",
        "Файл index.html, аудит доступності Google Lighthouse",
        "Додано посилання швидкого переходу skip-link: <a href=\"#main-content\" class=\"sr-only focus:not-sr-only ...\">Перейти до основного контенту</a>.",
        "Перевірено атрибути alt для всіх фотокарток, зв'язку label for з id елементів форми, атрибути aria-expanded та aria-controls для гамбургера, aria-hidden для декоративних іконок.",
        "Отримано максимальний бал в аудиті доступності (Accessibility 100/100) та Best Practices.")

    # Етап 18
    add_header_styled(doc, "Етап 18. Хмарний деплой та публікація на хостингу Netlify", 2)
    add_step_box(doc, 18, "Розгортання робочої версії на вебхостингу",
        "Панель керування Netlify (app.netlify.com)",
        "Підготовлено каталог lab-06-tailwind-components, перевірено відносні шляхи до медіафайлів та скриптів.",
        "Виконано деплой через Netlify CLI / Drag&Drop інтерфейс хостингу, отримано публічну адресу вебплатформи ChargeUA.",
        "Сайт успішно доступний у глобальній мережі інтернет за постійною захищеною адресою HTTPS.")

    # Етап 19
    add_header_styled(doc, "Етап 19. Перевірка відповідності стандартам W3C (HTML & CSS)", 2)
    add_step_box(doc, 19, "Валідація розмітки та таблиць стилів у сервісах W3C",
        "Онлайн-сервіси validator.w3.org (HTML) та jigsaw.w3.org/css-validator (CSS)",
        "Завантажено файл index.html та custom-styles.css на перевірку синтаксису.",
        "Виправлено дрібні зауваження (відсутність обов'язкових атрибутів опису), усунено помилки вкладеності блокових елементів в інлайнові.",
        "Отримано офіційний статус: Document checking completed. No errors or warnings to show.")

    doc.add_page_break()

    # 4. РОЗДІЛ 2: АНАТОМІЯ КЛЮЧОВИХ КОНСТРУКЦІЙ TAILWIND CSS
    add_header_styled(doc, "РОЗДІЛ 2. АНАТОМІЯ КЛЮЧОВИХ КОНСТРУКЦІЙ ТА АРХІТЕКТУРА MOBILE-FIRST", 1)
    
    add_body_p(doc, 
        "У ході виконання роботи спроєктовано та впроваджено 5 фундаментальних компонентних модулів, які демонструють усю потужність утилітарного підходу. "
        "Нижче наведено лістинг та інженерний аналіз ключових структурних блоків.")

    add_code_snippet(doc, "Конфігурація теми tailwind.config (Figma Design Tokens)",
        "tailwind.config = {\n"
        "  theme: {\n"
        "    extend: {\n"
        "      colors: {\n"
        "        brand: {\n"
        "          50: '#EBF5FF', 500: '#005EC9', 600: '#2563EB', 700: '#1D4ED8', 900: '#0F172A'\n"
        "        },\n"
        "        accent: { 400: '#38BDF8', 500: '#00B4D8' },\n"
        "        status: { free: '#10B981', busy: '#EF4444', reserved: '#F59E0B' }\n"
        "      },\n"
        "      fontFamily: {\n"
        "        sans: ['Inter', 'system-ui', 'sans-serif']\n"
        "      }\n"
        "    }\n"
        "  }\n"
        "}"
    )

    add_code_snippet(doc, "Адаптивний Header з мобільним гамбургером та ARIA-доступністю",
        "<header class=\"sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200\">\n"
        "  <div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20\">\n"
        "    <!-- Логотип -->\n"
        "    <a href=\"/\" class=\"flex items-center gap-3\">\n"
        "      <div class=\"w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black\">⚡</div>\n"
        "      <span class=\"font-extrabold text-xl text-slate-900\">ChargeUA</span>\n"
        "    </a>\n"
        "    <!-- Десктопна навігація: hidden md:flex -->\n"
        "    <nav class=\"hidden md:flex items-center gap-8\">\n"
        "      <a href=\"#stations\" class=\"text-sm font-semibold text-slate-700 hover:text-blue-600\">Станції</a>\n"
        "      <a href=\"#tariffs\" class=\"text-sm font-semibold text-slate-700 hover:text-blue-600\">Тарифи</a>\n"
        "      <a href=\"#map\" class=\"text-sm font-semibold text-slate-700 hover:text-blue-600\">Live-карта</a>\n"
        "    </nav>\n"
        "    <!-- Кнопка гамбургера: flex md:hidden -->\n"
        "    <button id=\"mobile-menu-btn\" class=\"flex md:hidden p-2.5 rounded-xl text-slate-700\" aria-expanded=\"false\">\n"
        "      <svg class=\"w-6 h-6\"><path stroke=\"currentColor\" stroke-width=\"2\" d=\"M4 6h16M4 12h16m-7 6h7\"/></svg>\n"
        "    </button>\n"
        "  </div>\n"
        "</header>"
    )

    add_code_snippet(doc, "Адаптивна сітка каталогу карток (Grid Mobile-First)",
        "<div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8\">\n"
        "  <!-- Картка станції -->\n"
        "  <article class=\"group bg-white rounded-2xl overflow-hidden border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300\">\n"
        "    <div class=\"relative h-48 bg-slate-900\">\n"
        "      <img src=\"assets/images/map_lviv.jpg\" alt=\"Хаб Victoria Gardens\" class=\"w-full h-full object-cover group-hover:scale-105 transition duration-500\">\n"
        "      <span class=\"absolute top-3 left-3 px-3 py-1 bg-emerald-500 text-white text-xs font-bold rounded-full\">Вільна (3/4)</span>\n"
        "      <span class=\"absolute top-3 right-3 px-2.5 py-1 bg-blue-600 text-white text-xs font-extrabold rounded-lg\">DC 150 кВт</span>\n"
        "    </div>\n"
        "    <div class=\"p-6\">\n"
        "      <h3 class=\"text-lg font-bold text-slate-900 group-hover:text-blue-600\">Хаб «Victoria Gardens DC-150»</h3>\n"
        "      <p class=\"text-xs text-slate-500 mt-2\">Автономний дизель-генератор, кав'ярня, цілодобовий паркінг.</p>\n"
        "      <div class=\"mt-4 pt-4 border-t border-slate-100 flex items-center justify-between\">\n"
        "        <span class=\"text-base font-black text-slate-900\">13.50 ₴ / кВт·год</span>\n"
        "        <a href=\"#map\" class=\"min-h-[44px] px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs rounded-xl inline-flex items-center\">Зарядити</a>\n"
        "      </div>\n"
        "    </div>\n"
        "  </article>\n"
        "</div>"
    )

    doc.add_page_break()

    # 5. РОЗДІЛ 3: ВСІ 13 КОНТРОЛЬНИХ ЗАПИТАНЬ З 3-КОМПОНЕНТНИМИ ВІДПОВІДЯМИ
    add_header_styled(doc, "РОЗДІЛ 3. ВІДПОВІДІ НА ВСІ КОНТРОЛЬНІ ЗАПИТАННЯ", 1)

    add_qa_card(doc, 1, 
        "Що таке Tailwind CSS і в чому полягає концепція Utility-First?",
        "Tailwind CSS — це утилітарний CSS-фреймворк низького рівня. Концепція Utility-First полягає у стилізації інтерфейсу шляхом комбінування дрібних атомарних класів безпосередньо в HTML замість написання семантичних CSS-правил.",
        "У традиційному CSS розробник вигадує назви класів (.card, .primary-btn) та пише для них десятки властивостей у окремому файлі. У підході Utility-First фреймворк надає готові утилітарні класи, де кожен клас відповідає рівно за одну властивість (наприклад, flex — display: flex; pt-4 — padding-top: 1rem; text-center — text-align: center). Це усуває необхідність постійно вигадувати назви класів за методологіями BEM чи OOCSS, ліквідує розростання (bloat) глобальних таблиць стилів та повністю вирішує проблему неочікуваних побічних ефектів від каскаду.",
        "<!-- Приклад Utility-First у ChargeUA -->\n<div class=\"flex items-center justify-between p-4 bg-white rounded-xl shadow-md\">\n  <span class=\"text-sm font-bold text-slate-900\">Victoria Gardens</span>\n</div>"
    )

    add_qa_card(doc, 2, 
        "Які переваги Tailwind CSS порівняно з традиційним підходом написання CSS?",
        "Висока швидкість розробки, відсутність конфліктів специфічності, компактний результуючий CSS завдяки JIT-компілятору, консистентність дизайн-системи та зручність підтримки.",
        "1) Відсутність перемикання контексту: верстка та дизайн відбуваються синхронно в одному файлі HTML.\n"
        "2) Незмінність розміру CSS: скільки б нових компонентів не додавалося на сайт, результуючий CSS-бандл практично не росте, оскільки всі утилітарні класи повторно перевикористовуються.\n"
        "3) Стандартизація дизайну: Tailwind накладає сувору шкалу відступів, кольорів та розмірів шрифту, унеможливлюючи хаотичне використання випадкових пікселів (на зразок margin: 13px чи padding: 19px).\n"
        "4) Безпечний рефакторинг: видалення або зміна HTML-блоку гарантує повне видалення його стилів без ризику зламати інші сторінки сайту.",
        "/* Традиційний CSS: ризик конфлікту класів .btn */\n.btn { padding: 10px; }\n/* Tailwind: ізольовані утиліти без конфлікту каскаду */\n<button class=\"px-4 py-2 bg-blue-600 text-white rounded-lg\"></button>"
    )

    add_qa_card(doc, 3, 
        "Яке призначення сервісу Tailwind Play?",
        "Tailwind Play (play.tailwindcss.com) — це офіційна інтерактивна хмарна пісочниця для миттєвого тестування, налагодження та демонстрації HTML/Tailwind коду без локального встановлення Node.js та збірки.",
        "Сервіс надає повноцінне браузерне середовище з підтримкою компілятора Tailwind JIT, автодоповненням класів, вкладкою редагування конфігурації tailwind.config.js, вкладкою користувацького CSS та можливістю генерації постійного посилання (кнопка Share). Також він має вбудований емулятор мобільних та планшетних екранів (viewport resize), що робить його незамінним для швидкої ізольованої перевірки промптів до ШІ перед переносом коду в основний репозиторій.",
        "https://play.tailwindcss.com -> швидкий поділ кодом ізольованого компонента кнопки чи шапки."
    )

    add_qa_card(doc, 4, 
        "Що таке адаптивний дизайн і як він реалізується в Tailwind CSS?",
        "Адаптивний дизайн — це підхід до веброзробки, за якого інтерфейс автоматично підлаштовує своє компонування під розміри екрана пристрою. У Tailwind це реалізується через responsive-префікси на основі min-width медіа-запитів.",
        "Tailwind використовує суворий мобільно-орієнтований підхід (Mobile-First). Це означає, що стилі, написані без префікса, застосовуються до найменших мобільних екранів. Щоб змінити властивість на ширших екранах, перед класом додається назва брейкпоїнта із двокрапкою (наприклад, md:flex, lg:grid-cols-3). Властивості плавно нашаровуються від меншого екрана до більшого.",
        "<!-- 1 колонка на мобільному, 2 на планшеті (md), 3 на десктопі (lg) -->\n<div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6\">\n  <!-- Картки хабів ChargeUA -->\n</div>"
    )

    add_qa_card(doc, 5, 
        "Яке призначення брейкпоїнтів sm:, md:, lg:, xl: та 2xl:?",
        "Це контрольні точки (breakpoints), які встановлюють мінімальну ширину в'юпорту (@media (min-width: ...)), починаючи з якої набувають чинності відповідні утилітарні класи.",
        "Стандартна шкала контрольних точок Tailwind:\n"
        "• sm: 640px — великі смартфони та ландшафтна орієнтація;\n"
        "• md: 768px — планшети (iPad, тач-пристрої);\n"
        "• lg: 1024px — невеликі ноутбуки та комп'ютери;\n"
        "• xl: 1280px — повнорозмірні монітори та десктопи;\n"
        "• 2xl: 1536px — широкі монітори Ultra-HD / 2K / 4K.\n"
        "Завдяки Mobile First класу sm:text-base md:text-lg lg:text-xl розмір шрифту послідовно збільшується зі зростанням діагоналі дисплея.",
        "/* Еквівалентний медіа-запит, який генерує md:hidden */\n@media (min-width: 768px) {\n  .md\\:hidden {\n    display: none;\n  }\n}"
    )

    add_qa_card(doc, 6, 
        "Для чого використовуються модифікатори станів hover:, focus:, active: та focus-visible:?",
        "Вони дозволяють стилізувати інтерактивні псевдокласи браузера (:hover, :focus, :active, :focus-visible) безпосередньо всередині атрибута class елемента.",
        "• hover: спрацьовує при наведенні курсора миші (наприклад, hover:bg-blue-700);\n"
        "• active: активується в момент кліку або фізичного натискання сенсорного екрана (active:scale-95 створює тактильний ефект вдавлювання кнопки);\n"
        "• focus: спрацьовує, коли елемент отримує фокус введення;\n"
        "• focus-visible: сучасний стандарт доступності, що вмикає візуальне обведення (ring) ТІЛЬКИ при клавіатурній навігації (Tab) і не дратує користувачів мишкою.",
        "<button class=\"bg-blue-600 hover:bg-blue-700 active:scale-95 focus-visible:ring-4 focus-visible:ring-blue-300 transition-all\">\n  Зарядити зараз\n</button>"
    )

    add_qa_card(doc, 7, 
        "Які можливості надає розширення Tailwind CSS IntelliSense для VS Code?",
        "Автодоповнення назв утилітарних класів, підказка точних числових CSS-значень при наведенні курсора, попередній перегляд кольорів безпосередньо в редакторі та валідація синтаксису.",
        "Розширення аналізує конфігураційний файл tailwind.config та HTML-розмітку. Під час набору тексту воно виводить випадаючий список релевантних класів. При наведенні миші на клас (наприклад, p-6) спливає підказка: padding: 1.5rem; /* 24px */. Якщо клас містить колір (наприклад, bg-blue-600), ліворуч у рядку відображається кольоровий квадратик. Також плагін підкреслює помилки та конфліктні класи (Class Sorting & Linting).",
        "VS Code Extension ID: bradlc.vscode-tailwindcss\nПідказка при наведенні на py-3: padding-top: 0.75rem; padding-bottom: 0.75rem;"
    )

    add_qa_card(doc, 8, 
        "Чому згенерований штучним інтелектом код потребує рефакторингу (Refinement Workflow)?",
        "ШІ-моделі часто допускають «галюцинації», використовують захардкоджені довільні значення (arbitrary values), ігнорують специфічні правила доступності (ARIA) або додають зайві незапитані елементи.",
        "Під час генерації модель оптимізує результат під загальний візуальний вигляд, але часто не знає контексту повної дизайн-системи. Як результат:\n"
        "1) Використання неекономних довільних класів типу bg-[#005EC9] замість семантичних токенів теми;\n"
        "2) Відсутність обов'язкових атрибутів aria-expanded, aria-controls для інтерактивних скриптів;\n"
        "3) Відсутність розмірів touch-target для мобільних екранів (кнопки менше 44px);\n"
        "4) Надлишкові обгортки div. Студент як інженер зобов'язаний критично верифікувати код перед інтеграцією.",
        "<!-- До рефакторингу (код ШІ) -->\n<div class=\"h-[38px] bg-[#005EC9]\">Кнопка</div>\n<!-- Після рефакторингу студентом -->\n<button class=\"min-h-[44px] bg-blue-600 focus-visible:ring-4\">Кнопка</button>"
    )

    add_qa_card(doc, 9, 
        "Які вимоги до доступності вебінтерфейсу (Accessibility) перевірено під час виконання роботи?",
        "Дотримання стандарту WCAG 2.2 рівня AA: контрастність тексту, мінімальний розмір сенсорних цілей 44x44px, доступність із клавіатури, наявність skip-link та ARIA-атрибути.",
        "У проєкті ChargeUA перевірено:\n"
        "1) Контраст кольорів: відношення яскравості білого тексту до фону #005EC9 становить понад 4.6:1 (успішно для нормального тексту);\n"
        "2) Сенсорні зони (Touch Target Minimum WCAG 2.5.8): всі интерактивні елементи мають клас min-h-[44px];\n"
        "3) Клавіатурна навігація: підтримка фокусу через focus-visible та закриття меню клавішею Escape;\n"
        "4) Скрінрідери: наявність описових alt=\"...\" для зображень, aria-label для кнопок-іконок та sr-only для заголовків.",
        "<!-- Посилання для швидкого переходу -->\n<a href=\"#main-content\" class=\"sr-only focus:not-sr-only focus:absolute z-50 bg-blue-600 text-white p-3\">Перейти до вмісту</a>"
    )

    add_qa_card(doc, 10, 
        "Для чого використовується режим Device Toolbar в Chrome DevTools?",
        "Для повноцінної емуляції мобільних смартфонів і планшетів: тестування брейкпоїнтів, сенсорного введення (touch events), орієнтації екрана та обмеження швидкості мережі (Throttling).",
        "Гарячі клавіші Ctrl+Shift+M активують вікно адаптивного тестування. Розробник може вибрати популярні профілі пристроїв (iPhone SE, iPhone 14 Pro, iPad Mini, Samsung Galaxy) або вручну тягнути за край вікна, відстежуючи точки перелому медіа-запитів. Режим дозволяє наочно побачити перемикання класів hidden / md:flex, перевірити відсутність горизонтального скролу та протестувати роботу висувного мобільного меню.",
        "Комбінація клавіш: F12 -> Ctrl + Shift + M -> вибір iPhone SE (375x812) -> тест меню."
    )

    add_qa_card(doc, 11, 
        "Які компоненти вебінтерфейсу створено за допомогою ШІ в лабораторній роботі?",
        "Створено 5 ключових компонентів: 1) Primary CTA Button, 2) Адаптивний Header з мобільним Drawer, 3) Station Card (картка станції), 4) Адаптивна сітка Grid, 5) 4-колонковий Footer.",
        "Кожен компонент пройшов шлях від текстового опису в інженерному промпті до автономного тестового файлу в каталозі components/ та подальшої збірки в головному файлі index.html:\n"
        "• Кнопка отримала мікроанімації та гарантовану доступність 44px;\n"
        "• Шапка реалізує перетворення списку посилань на мобільний бургер;\n"
        "• Картка містить динамічні статусні бейджі та цінові тарифи;\n"
        "• Сітка автоматично балансує картки між 1, 2 та 3 колонками;\n"
        "• Футер містить форму розсилки та живий статус доступності хабів мережі.",
        "components/button.html | header.html | card.html | grid.html | footer.html"
    )

    add_qa_card(doc, 12, 
        "Що таке Preflight в Tailwind CSS і яке його призначення?",
        "Preflight — це вбудований у Tailwind базовий набір нормалізуючих CSS-стилів, побудований на базі modern-normalize, який приводить стандартні стилі браузерів до єдиного нейтрального вигляду.",
        "Браузери за замовчуванням мають різні відступи та стилі елементів (User Agent Stylesheets). Preflight виконує:\n"
        "1) Скидання зовнішніх відступів: margin: 0 для всіх тегів (body, h1-h6, p, ul);\n"
        "2) Заголовки h1-h6 позбавляються вбудованого збільшеного розміру та жирності (вони стають font-size: inherit; font-weight: inherit);\n"
        "3) Списки ul, ol позбавляються маркерів та відступів;\n"
        "4) Зображення стають блочними елементами з display: block та max-width: 100% для запобігання виходу за межі батьківського контейнера;\n"
        "5) Рамки за замовчуванням мають border: 0 solid #e5e7eb.",
        "/* Preflight автоматично запобігає вильоту зображень */\nimg, svg, video, canvas {\n  display: block;\n  max-width: 100%;\n  height: auto;\n}"
    )

    add_qa_card(doc, 13, 
        "Які переваги має використання переходів (transition) та мікроанімацій (hover, active, focus) у вебінтерфейсі?",
        "Плавні переходи надають користувачу миттєвий тактильний зворотний зв'язок (Micro-Interactions), підвищують сприйняття якості інтерфейсу, покращують UX та орієнтацію на сторінці.",
        "Без використання переходів зміна кольору чи положення елемента відбувається миттєво і виглядає різко. Класи transition-all duration-200 ease-in-out вмикають апаратне прискорення браузера (GPU Rendering). Коли користувач наводить курсор на кнопку ChargeUA, фон м'яко темнішає, тінь глибшає, а стрілочка робить плавний зсув праворуч. При натисканні (active:scale-95) кнопка пружно стискається, підтверджуючи успішність кліку перед відкриттям форми.",
        "class=\"transition-all duration-200 hover:shadow-lg active:scale-95 ease-in-out\""
    )

    doc.add_page_break()

    # 6. РОЗДІЛ 4: ВИСНОВКИ
    add_header_styled(doc, "РОЗДІЛ 4. ВИСНОВКИ", 1)

    add_body_p(doc, 
        "1. У ході виконання Лабораторної роботи №6 успішно опановано парадигму компонентної верстки та утилітарного підходу "
        "Utility-First за допомогою фреймворку Tailwind CSS на прикладі вебплатформи мережі швидкісних зарядних хабів «ChargeUA».")
    add_body_p(doc, 
        "2. Реалізовано повний інженерний цикл Prompt-to-UI взаємодії з ШІ-моделями (Claude 3.5 Sonnet, Google Gemini, Sequential Thinking MCP): "
        "здійснено проєктування промптів, генерацію автономних UI-компонентів, критичний аналіз коду та обов'язкове рафінування (Refinement Workflow).")
    add_body_p(doc, 
        "3. Впроваджено мобільно-орієнтований підхід (Mobile-First): базова верстка проєкту оптимізована для смартфонів (375px), "
        "а утилітарні префікси sm:, md:, lg: та xl: плавно перебудовують інтерфейс для планшетів та десктопів без виникнення горизонтального скролу.")
    add_body_p(doc, 
        "4. Синхронізовано дизайн-систему проєкту, розроблену в Figma у ЛР №4, із конфігурацією Tailwind через об'єкт tailwind.config, "
        "що забезпечило централізоване керування палітрою бренду (синій #005EC9, акцентний бірюзовий #00B4D8, нейтральний темний #0F172A).")
    add_body_p(doc, 
        "5. Забезпечено найвищий рівень доступності за міжнародним стандартом WCAG 2.2 рівня AA (клас min-h-[44px] для сенсорного введення, "
        "skip-link, чіткий контур focus-visible:ring-4, закриття мобільного меню клавішею Escape), а також проведено перевірку сумісності у DevTools та W3C.")

    # Збереження файлу
    out_docx = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
    out_docx_alt = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_Хід_роботи_та_Контрольні_запитання.docx")
    out_root_docx = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
    out_root_docx_alt = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_Хід_роботи_та_Контрольні_запитання.docx")
    
    doc.save(out_docx)
    shutil.copy(out_docx, out_docx_alt)
    shutil.copy(out_docx, out_root_docx)
    shutil.copy(out_docx, out_root_docx_alt)
    print(f"Master DOCX generated successfully:\n  - {out_docx}\n  - {out_root_docx}")

    # Конвертація в PDF за допомогою Word COM
    try:
        import win32com.client
        print("Starting Word COM automation to convert DOCX to PDF...")
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        doc_com = word.Documents.Open(os.path.abspath(out_docx))
        out_pdf = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
        out_pdf_alt = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_Хід_роботи_та_Контрольні_запитання.pdf")
        out_root_pdf = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
        out_root_pdf_alt = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_Хід_роботи_та_Контрольні_запитання.pdf")

        # 17 = wdFormatPDF
        doc_com.SaveAs(os.path.abspath(out_pdf), FileFormat=17)
        doc_com.Close()
        word.Quit()

        shutil.copy(out_pdf, out_pdf_alt)
        shutil.copy(out_pdf, out_root_pdf)
        shutil.copy(out_pdf, out_root_pdf_alt)
        print(f"Master PDF generated successfully:\n  - {out_pdf}\n  - {out_root_pdf}")
    except Exception as e:
        print(f"Warning: Word COM PDF generation encountered: {e}")

    # Створення фінального ZIP-архіву
    zip_path = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_Код_ChargeUA.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, BASE_DIR)
                zipf.write(full_p, rel_p)
        # Додати звіт та промпт-паспорт
        if os.path.exists(out_docx):
            zipf.write(out_docx, os.path.relpath(out_docx, BASE_DIR))
        out_pdf = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
        if os.path.exists(out_pdf):
            zipf.write(out_pdf, os.path.relpath(out_pdf, BASE_DIR))
        prompt_log_p = os.path.join(REPORT_DIR, "Prompt_Log_Lab6.md")
        if os.path.exists(prompt_log_p):
            zipf.write(prompt_log_p, os.path.relpath(prompt_log_p, BASE_DIR))

    print(f"Archive created successfully: {zip_path}")

if __name__ == "__main__":
    build_complete_master_document()
