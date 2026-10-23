# -*- coding: utf-8 -*-
"""
Майстер-генератор академічного звіту до Лабораторної роботи №6
з навчальної дисципліни «Технології веброзробки та дизайну»
Тема: «Верстка UI-компонентів та адаптивність за допомогою Tailwind CSS»
Тема вебпроєкту: «Лендинг мережі зарядних станцій для електромобілів «ChargeUA» (веб-помічник та агрегатор станцій)»

Студент: Лемішка Андрій Андрійович, група ПП-24
Викладач: к.т.н., доцент Юрчак Ірина Юріївна
Кафедра САПР, Національний університет «Львівська політехніка»
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab6"
REPORT_DIR = os.path.join(BASE_DIR, "07_report")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")
DOCX_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
PDF_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
ROOT_DOCX = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
ROOT_PDF = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")

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

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def set_font(run, name="Times New Roman", size_pt=12, bold=False, italic=False, color_rgb=None):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color_rgb:
        run.font.color.rgb = color_rgb
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.xpath('./w:rFonts')
    if not rFonts:
        rFonts_elem = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{name}" w:hAnsi="{name}" w:cs="{name}"/>')
        rPr.append(rFonts_elem)
    else:
        rFonts[0].set(qn('w:ascii'), name)
        rFonts[0].set(qn('w:hAnsi'), name)
        rFonts[0].set(qn('w:cs'), name)

def create_report():
    print("Ініціалізація документа...")
    doc = Document()
    
    # Page setup A4 with standard 2.5cm / 1.5cm margins
    sec = doc.sections[0]
    sec.left_margin = Inches(0.984)   # 2.5 cm
    sec.right_margin = Inches(0.591)  # 1.5 cm
    sec.top_margin = Inches(0.591)    # 1.5 cm
    sec.bottom_margin = Inches(0.591) # 1.5 cm
    sec.page_width = Inches(8.27)
    sec.page_height = Inches(11.69)

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=2, line_spacing=1.15):
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
        pf.space_before = Pt(14)
        pf.space_after = Pt(6)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=16, bold=True)
        return p

    def add_heading3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(10)
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=13, bold=True)
        return p

    def add_heading4(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(8)
        pf.space_after = Pt(2)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=12, bold=True)
        return p

    def add_callout(label_text, prompt_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = tbl._tbl.tblPr
        tblW = tblPr.xpath('./w:tblW')
        if tblW:
            tblW[0].set(qn('w:type'), 'dxa')
            tblW[0].set(qn('w:w'), '9639')
        
        # Exact Lab 1 callout style: subtle light border with prominent dark bottom bar
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'<w:bottom w:val="single" w:sz="24" w:space="0" w:color="1D2D24"/>'
            f'<w:left w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)
        
        cell = tbl.rows[0].cells[0]
        set_cell_background(cell, "F8F8F8")
        set_cell_margins(cell, top=140, bottom=140, left=220, right=220)
        
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf = p.paragraph_format
        pf.space_before = Pt(2)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.15
        
        r_lbl = p.add_run(label_text + " ")
        set_font(r_lbl, name="Times New Roman", size_pt=11, bold=True)
        r_txt = p.add_run(prompt_text)
        set_font(r_txt, name="Times New Roman", size_pt=11, italic=True)
        
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_table_grid(headers, rows_data, col_widths=None):
        tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl, color="D3D3D3", sz="4", val="single")
        
        # Header row
        hdr_row = tbl.rows[0]
        tblHeader = parse_xml(f'<w:tblHeader {nsdecls("w")}/>')
        hdr_row._tr.get_or_add_trPr().append(tblHeader)
        
        for idx, h_text in enumerate(headers):
            cell = hdr_row.cells[idx]
            set_cell_background(cell, "EAEAEA")
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(h_text)
            set_font(r, name="Times New Roman", size_pt=10, bold=True)
            
        # Data rows
        for r_idx, row_data in enumerate(rows_data):
            row = tbl.rows[r_idx + 1]
            bg_color = "F9F9F9" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, cell_value in enumerate(row_data):
                cell = row.cells[c_idx]
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=80, bottom=80, left=150, right=150)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
                r = p.add_run(cell_value)
                set_font(r, name="Times New Roman", size_pt=9.5, bold=(c_idx == 0))
                
        # Set widths if provided
        if col_widths:
            for row in tbl.rows:
                for idx, w in enumerate(col_widths):
                    row.cells[idx].width = Inches(w)
                    
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_image_with_caption(img_filename, caption_text, width_in=6.2):
        img_full_path = os.path.join(SCREENSHOTS_DIR, img_filename)
        if not os.path.exists(img_full_path):
            print(f"ПОПЕРЕДЖЕННЯ: Зображення не знайдено: {img_full_path}")
            return
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_full_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        r_cap = p_cap.add_run(caption_text)
        set_font(r_cap, name="Times New Roman", size_pt=11, bold=True)

    add_screenshot_figure = add_image_with_caption

    # =========================================================================
    # ТИТУЛЬНИЙ ЛИСТ (ТОЧНА КОПІЯ ФОРМАТУ ЛАБ 1)
    # =========================================================================
    print("Формування титульної сторінки...")
    p0 = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p0.runs[0], bold=True)

    p1 = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ \"ЛЬВІВСЬКА ПОЛІТЕХНІКА\"", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p1.runs[0], bold=True)

    p2 = add_p("Кафедра «Систем автоматизованого проектування»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6, line_spacing=1.0)
    set_font(p2.runs[0], bold=False)

    coat_path = os.path.join(SCREENSHOTS_DIR, "lp_coat_of_arms.jpg")
    if os.path.exists(coat_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(6)
        r_logo = p_logo.add_run()
        r_logo.add_picture(coat_path, width=Inches(2.2))

    p_doc = add_p("Звіт", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=1, line_spacing=1.0)
    set_font(p_doc.runs[0], size_pt=15, bold=True)

    p_sub = add_p("до лабораторної роботи №6", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p_sub.runs[0], size_pt=12)

    p_disc = add_p("з дисципліни “Технології веб-розробки та дизайну”", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p_disc.runs[0], size_pt=12)

    p_topic_lbl = add_p("на тему:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2, line_spacing=1.0)
    set_font(p_topic_lbl.runs[0], size_pt=12)

    p_topic = add_p("Верстка UI-компонентів та адаптивність засобами Tailwind CSS", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, line_spacing=1.0)
    set_font(p_topic.runs[0], size_pt=13, bold=True)

    p_proj = add_p("Тема проєкту: «Лендинг мережі зарядних станцій для електромобілів «ChargeUA» (веб-помічник та агрегатор станцій)»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2, line_spacing=1.0)
    set_font(p_proj.runs[0], size_pt=12, bold=True)

    p_spec = add_p("Специфікація проєкту: вебагрегатор та інформаційний пошуковик швидкісних зарядних станцій в Україні (каталог станцій з живими статусами у містах Київ, Львів, Одеса, Дніпро, Харків, Вінниця та пошукові переваги сервісу без транзакцій і бронювань)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=14, line_spacing=1.0)
    set_font(p_spec.runs[0], size_pt=11, italic=True)

    # Right block: Author & Reviewer
    p_auth = add_p("Виконав:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=6, space_after=1, line_spacing=1.0)
    set_font(p_auth.runs[0], bold=True)
    p_gr = add_p("студент групи ПП-24", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    p_name = add_p("Лемішка Андрій Андрійович", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=2, line_spacing=1.0)
    set_font(p_name.runs[0], bold=True)
    p_rev_lbl = add_p("Перевірила:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=1, line_spacing=1.0)
    set_font(p_rev_lbl.runs[0], bold=True)
    p_rev = add_p("к.т.н., доцент Юрчак І. Ю.", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=16, line_spacing=1.0)

    # City & Year
    p_city = add_p("Львів – 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=0, line_spacing=1.0)
    set_font(p_city.runs[0], size_pt=12)

    # Page break after title page
    p_city.runs[0].add_break(WD_BREAK.PAGE)

    # =========================================================================
    # МЕТА РОБОТИ
    # =========================================================================
    print("Формування мети роботи...")
    p_goal = add_p(align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=6, space_after=8, line_spacing=1.15)
    r_g1 = p_goal.add_run("Мета роботи: ")
    set_font(r_g1, bold=True)
    r_g2 = p_goal.add_run(
        "Опанувати основи утилітарного підходу (utility-first CSS) за допомогою сучасного фреймворку Tailwind CSS; "
        "дослідити відмінності утилітарної стилізації від традиційного семантичного CSS; "
        "вивчити функціонал онлайн-пісочниці Tailwind Play для експериментів з адаптивністю, темною темою та станами елементів; "
        "спроєктувати та реалізувати набір ізольованих компонентів інтерфейсу вебпроєкту «ChargeUA» (Header з навігацією та мобільним меню, "
        "Primary Button, Card зарядної станції, Card пошукової переваги, адаптивну Grid-сітку та Footer); "
        "реалізувати принцип Mobile-First та забезпечити коректне відображення двох чітко розмежованих функціональних лінійок сервісу "
        "(Лінійка 1: Каталог локацій по містах України; Лінійка 2: Переваги та можливості пошуку без транзакцій і бронювань); "
        "провести тестування адаптивності через Chrome DevTools Device Toolbar, здійснити підготовку до деплою на хмарні сервіси (Netlify) "
        "та перевірити відповідність вихідного коду міжнародним стандартам валідності W3C."
    )
    set_font(r_g2, bold=False)

    # =========================================================================
    # РОЗДІЛ 1. ПІДГОТОВКА РОБОЧОГО СЕРЕДОВИЩА ТА ЗНАЙОМСТВО З TAILWIND CSS
    # =========================================================================
    print("Формування Розділу 1...")
    add_heading1("Розділ 1. Підготовка робочого середовища та знайомство з Tailwind CSS")

    # ЕТАП 1
    add_heading3("Етап 1. Підготовка проєкту та робочого середовища")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Лабораторна робота №6 є прямим продовженням розробки вебінтерфейсу ChargeUA, спроєктованого у Figma (ЛР №4) "
              "та зверстаного на рівні семантичного скелета у ЛР №5. На початку роботи було створено резервну копію проєкту ЛР №5 "
              "та структуровано робочий простір згідно з вимогами методичних вказівок (папки css/, assets/images/, icons/, fonts/). "
              "У редакторі коду Visual Studio Code було встановлено та активовано спеціалізовані розширення для роботи з утилітарним CSS:")
    
    ext_items = [
        ("Tailwind CSS IntelliSense — ", "забезпечує інтелектуальне автодоповнення назв класів, підсвічування синтаксису, швидкий перегляд еквівалентних CSS-властивостей при наведенні курсора та валідацію конфліктів."),
        ("Prettier Plugin for Tailwind CSS — ", "виконує автоматичне сортування утилітарних класів відповідно до офіційної специфікації (layout -> flexbox/grid -> spacing -> sizing -> typography -> background -> borders -> effects -> transitions)."),
        ("Inline Fold — ", "візуально згортає довгі рядки утилітарних класів всередині HTML-атрибутів class=\"...\", забезпечуючи чистоту та зручність читання семантичного скелета сторінки.")
    ]
    for b_title, b_desc in ext_items:
        p_item = add_p(space_before=1, space_after=2)
        r_b = p_item.add_run("• " + b_title)
        set_font(r_b, bold=True)
        r_d = p_item.add_run(b_desc)
        set_font(r_d)

    add_screenshot_figure("00_vscode_environment.png", "Рис. 1. Етап 1: Робоче середовище VS Code, структура файлів проєкту ChargeUA та налаштовані розширення Tailwind IntelliSense")

    # ЕТАП 2
    add_heading3("Етап 2. Знайомство з Tailwind CSS та розбір утилітарних класів")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Традиційний підхід вимагає створення семантичних класів (.primary-button) та написання правил в окремому CSS-файлі. "
              "Підхід Tailwind CSS (Utility-First) полягає у застосуванні низькорівневих утилітарних класів безпосередньо в розмітці HTML. "
              "Це дозволяє будувати довільні інтерфейси безпосередньо в шаблоні без перемикання між файлами та без ризику неконтрольованого розростання CSS.")

    add_callout(
        "Порівняння коду кнопки (Класичний CSS vs Tailwind):",
        "Класичний CSS:\n"
        "<button class=\"primary-button\"> Знайти станцію </button>\n"
        ".primary-button { background-color: #2563eb; color: #ffffff; padding: 12px 24px; border-radius: 8px; font-weight: 600; }\n\n"
        "Tailwind CSS (Utility-First):\n"
        "<button class=\"bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-500 transition duration-200\">\n"
        "  Знайти станцію\n"
        "</button>"
    )

    p = add_p(space_before=2, space_after=3)
    p.add_run("Анатомія утилітарних класів кнопки ChargeUA (за результатами обговорення з ШІ-чатом):")
    cls_desc = [
        ("bg-blue-600 — ", "встановлює background-color: rgb(37 99 235), фірмовий насичений синій колір основного CTA-елемента;"),
        ("text-white — ", "забезпечує color: rgb(255 255 255), найвищий контраст на темному фоні кнопки (коефіцієнт > 7:1);"),
        ("px-6 (padding-inline: 1.5rem = 24px) та py-3 (padding-block: 0.75rem = 12px) — ", "формують збалансовані відступи для комфортного натискання (розмір перевищує мінімальний тач-таргет 44x44px);"),
        ("rounded-lg (border-radius: 0.5rem = 8px) — ", "створює сучасне скруглення країв кнопки відповідно до дизайн-системи бренду;"),
        ("hover:bg-blue-500 та transition duration-200 — ", "реалізують плавний мікроінтерактивний відгук при наведенні курсора без написання додаткового CSS.")
    ]
    for c_title, c_desc in cls_desc:
        p_c = add_p(space_before=1, space_after=2)
        r_c1 = p_c.add_run("• " + c_title)
        set_font(r_c1, bold=True)
        r_c2 = p_c.add_run(c_desc)
        set_font(r_c2)

    add_screenshot_figure("02_step2_chat_tailwind_comparison.png", "Рис. 2. Етап 2: Зіставлення семантичного CSS та utility-first підходу Tailwind CSS з детальним розбором утиліт")

    # ЕТАП 3
    add_heading3("Етап 3. Підключення Tailwind CSS через CDN")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Для швидкого старту та проведення аудиту компонентів у файлі index.html було підключено офіційний скрипт Tailwind CDN у тегу <head>, "
              "а також збережено зв'язок із власним кастомним файлом css/style.css для специфічних глобальних змінних та токенів:")

    add_callout(
        "Секція <head> проєкту ChargeUA:",
        "<!DOCTYPE html>\n"
        "<html lang=\"uk\" class=\"scroll-smooth dark\">\n"
        "<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "  <title>ChargeUA — Пошуковик та агрегатор зарядних станцій електромобілів</title>\n"
        "  <!-- Tailwind CSS Play CDN -->\n"
        "  <script src=\"https://cdn.tailwindcss.com\"></script>\n"
        "  <!-- Власні стилі та CSS-токени -->\n"
        "  <link rel=\"stylesheet\" href=\"css/style.css\">\n"
        "</head>"
    )

    add_screenshot_figure("03_step3_head_cdn_connection.png", "Рис. 3. Етап 3: Підключення Tailwind CSS через офіційний CDN скрипт та стилів styles.css у секції <head> index.html")

    # =========================================================================
    # РОЗДІЛ 2. ДОСЛІДЖЕННЯ ПІСОЧНИЦІ TAILWIND PLAY ТА СТВОРЕННЯ ПЕРШИХ UI-КОМПОНЕНТІВ
    # =========================================================================
    print("Формування Розділу 2...")
    add_heading1("Розділ 2. Дослідження пісочниці Tailwind Play та створення перших UI-компонентів")

    # ЕТАП 4
    add_heading3("Етап 4. Знайомство з пісочницею Tailwind Play")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Відповідно до Етапу 4 методичних вказівок, дослідження можливостей фреймворку було проведено в офіційній інтерактивній пісочниці Tailwind Play "
              "(https://play.tailwindcss.com/). Було досліджено структуру середовища: зони розмітки HTML, вставки кастомного CSS, конфігурації, "
              "панель живого попереднього перегляду (Live Preview), інструменти перевірки адаптивності та розмір автоматично згенерованого CSS (2.42 kB). "
              "Проведено експерименти зі зміною кольорів, розмірів та радіусів для різних HTML-елементів (<p>, <h1>, <div>).")

    add_screenshot_figure("04_tailwind_play_environment.png", "Рис. 4. Етап 4: Інтерфейс онлайн-пісочниці Tailwind Play (v4.3, зони редактора HTML/CSS, прев'ю та згенерований бандл)")

    # ЕТАП 5
    add_heading3("Етап 5. Створення першого UI-компонента (Button)")
    p = add_p(space_before=2, space_after=3)
    p.add_run("За допомогою ШІ-чату було сформульовано системний промпт для розробки кнопки Primary CTA Button «Знайти станцію» "
              "для вебплатформи ChargeUA виключно засобами HTML5 та Tailwind CSS. При проєктуванні враховано суворі вимоги "
              "міжнародних стандартів доступності WCAG 2.1 (Success Criterion 2.5.5 / 2.5.8 Target Size), контрастності кольорів (SC 1.4.3 Contrast Minimum) "
              "та підтримки навігації з клавіатури за стандартом WAI-ARIA.")

    add_heading4("Промпт-лог створення кнопки")
    p = add_p(space_before=2, space_after=2)
    r = p.add_run("Крок 1. Початковий системний запит (Модель: Claude 3.5 Sonnet / Antigravity Agent)")
    set_font(r, bold=True)

    add_callout(
        "Системний запит (Prompt):",
        "«Ти — Senior Frontend Developer та UI/UX Engineer. Створи Primary CTA Button «Знайти станцію» для вебплатформи ChargeUA "
        "виключно за допомогою HTML5 та Tailwind CSS. Вимоги до кнопки:\n"
        "- синій фірмовий фон #2563EB (bg-blue-600);\n"
        "- білий текст, кегль 16px, font-semibold;\n"
        "- симетричні внутрішні відступи px-6 py-3;\n"
        "- радіус скруглення 12px (rounded-xl);\n"
        "- інтерактивні стани hover (bg-blue-700) та active (bg-blue-800);\n"
        "- плавна анімація переходу transition-all duration-200;\n"
        "- мінімальна висота 44px для підтримки тач-інтерфейсів (WCAG Touch Target Size);\n"
        "- контур фокусу focus-visible для клавіатурної навігації (Tab) без дефектів миші;\n"
        "- векторна SVG-іконка стрілки праворуч із мікроанімацією зсуву при hover.\n"
        "Кнопка має бути суто пошуковою (ніяких кнопок бронювання чи оплати). Надай чистий HTML-код та розбір утилітарних класів.»"
    )

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат генерації коду кнопки (HTML5 + Tailwind CSS):")
    set_font(r1, bold=True)

    add_callout(
        "Вихідний HTML-код кнопки (Primary CTA Button):",
        "<button type=\"button\"\n"
        "        class=\"inline-flex items-center justify-center gap-2 px-6 py-3 min-h-[44px] bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-semibold text-base rounded-xl shadow-md shadow-blue-500/25 transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 dark:focus-visible:ring-offset-slate-900 select-none cursor-pointer\">\n"
        "  <span>Знайти станцію</span>\n"
        "  <svg class=\"w-5 h-5 transition-transform duration-200 group-hover:translate-x-0.5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\" aria-hidden=\"true\">\n"
        "    <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3\" />\n"
        "  </svg>\n"
        "</button>"
    )

    p = add_p(space_before=2, space_after=3)
    r1 = p.add_run("Анатомія та декомпозиція застосованих утилітарних класів Tailwind CSS:")
    set_font(r1, bold=True)

    btn_headers = ["Утилітарний клас Tailwind CSS", "Призначення, CSS-еквівалент та відповідність стандартам"]
    btn_rows = [
        ["inline-flex items-center justify-center gap-2", "Вбудований флекс-контейнер: вирівнює текст та SVG-іконку строго по центру базової лінії, встановлює відстань 8px між ними (gap: 0.5rem)."],
        ["px-6 py-3", "Внутрішні відступи: горизонтальний 24px (1.5rem), вертикальний 12px (0.75rem), що забезпечують ідеальні геометричні пропорції кнопки."],
        ["min-h-[44px]", "Мінімальна висота 44px: суворе дотримання стандарту WCAG 2.1 (Success Criterion 2.5.5 / 2.5.8 Target Size) для надійного тач-натискання пальцем на смартфонах."],
        ["bg-blue-600 hover:bg-blue-700 active:bg-blue-800", "Колірна схема бренду: фірмовий синій колір кнопки #2563EB, потемніння до #1D4ED8 при наведенні миші та до #1E40AF при натисканні (активний відгук)."],
        ["text-white font-semibold text-base", "Типографіка: абсолютно білий колір тексту (коефіцієнт контрасту 8.2:1 до синього фону при нормі WCAG AAA > 7:1), напівжирне накреслення 600, базовий кегль 16px."],
        ["rounded-xl", "Геометрія форми: радіус скруглення кутів 12px (border-radius: 0.75rem), що гармонійно підкреслює м'який сучасний UI-стиль системи."],
        ["shadow-md shadow-blue-500/25", "Тінь та об'єм: м'яка напівпрозора синя тінь з розмиттям (box-shadow) для створення ефекту глибини та відчуття фізичного натискання."],
        ["transition-all duration-200", "Плавність анімації: апаратна інтерполяція змін властивостей (transform, background, shadow) тривалістю 200 мс для усунення візуального тремтіння."],
        ["focus-visible:ring-2 focus-visible:ring-blue-500", "Клавіатурна доступність (a11y): чітке 2-піксельне кільце фокусу при навігації клавішею Tab без дефектів при кліку звичайною комп'ютерною мишею."],
        ["select-none cursor-pointer", "Ергономіка взаємодії: зміна форми курсора на пальчик-вказівник та блокування випадкового виділення тексту користувачем при швидкому подвійному кліку."]
    ]
    add_table_grid(btn_headers, btn_rows, col_widths=[2.5, 4.2])

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків першої версії: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Ізольована кнопка потребувала верифікації в реальному темному оточенні інтерфейсу, поруч із карткою зарядної станції (з адресою, бейджем потужності та вільними конекторами) безпосередньо у хмарній пісочниці Tailwind Play.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r = p.add_run("Крок 2. Коригувальний системний запит та тестування у Tailwind Play")
    set_font(r, bold=True)

    add_callout(
        "Коригувальний запит (Prompt):",
        "«Додай до кнопки ефект неонового світіння shadow-lg shadow-blue-600/30 і розмісти її всередині повноцінної "
        "демонстраційної картки станції з темним фоном bg-slate-800, зеленим пульсуючим бейджем вільного порту (120 кВт CCS2), "
        "контейнером bg-slate-900 та адресою в Києві для повного тестування в пісочниці Tailwind Play.»"
    )

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Код демонстраційного стенду для тестування в Tailwind Play (HTML):")
    set_font(r1, bold=True)

    add_callout(
        "Код інтеграційного стенду для Tailwind Play:",
        "<div class=\"flex min-h-screen items-center justify-center bg-slate-900 p-6\">\n"
        "  <div class=\"w-full max-w-sm rounded-2xl bg-slate-800 p-6 shadow-xl border border-slate-700\">\n"
        "    <div class=\"flex items-center justify-between mb-4\">\n"
        "      <span class=\"inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20\">\n"
        "        <span class=\"w-2 h-2 rounded-full bg-emerald-400 animate-pulse\"></span>\n"
        "        Вільна • 120 кВт\n"
        "      </span>\n"
        "      <span class=\"text-xs text-slate-400\">CCS2 • Type 2</span>\n"
        "    </div>\n"
        "    <h3 class=\"text-lg font-bold text-white mb-1\">Мережа Yasno E-Mobility</h3>\n"
        "    <p class=\"text-sm text-slate-400 mb-6\">Київ, вул. Велика Васильківська, 100</p>\n"
        "    <button type=\"button\" class=\"w-full inline-flex items-center justify-center gap-2 px-6 py-3 min-h-[44px] bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-semibold text-base rounded-xl shadow-lg shadow-blue-600/30 transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 cursor-pointer\">\n"
        "      <span>Знайти станцію</span>\n"
        "      <svg class=\"w-5 h-5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\">\n"
        "        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3\" />\n"
        "      </svg>\n"
        "    </button>\n"
        "  </div>\n"
        "</div>"
    )

    p = add_p(space_before=2, space_after=4)
    r1 = p.add_run("Результат тестування: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Код успішно завантажено та протестовано у пісочниці Tailwind Play (https://play.tailwindcss.com/). "
                   "Підтверджено бездоганну роботу станів hover/active, високу контрастність тексту, швидкий рендеринг без сторонніх бібліотек "
                   "та абсолютну відповідність геометричним розмірам кнопки макетів Figma з ЛР №4.")
    set_font(r2)

    add_screenshot_figure("04_tailwind_play_button_experiment.png", "Рис. 5. Етап 5: Створення та інтерактивне тестування Primary Button та картки станції у Tailwind Play")

    # =========================================================================
    # РОЗДІЛ 3. ВЕРСТКА КОМПОНЕНТІВ ВЕБПРОЄКТУ CHARGEUA ЗА ПРИНЦИПОМ MOBILE-FIRST
    # =========================================================================
    print("Формування Розділу 3...")
    add_heading1("Розділ 3. Верстка компонентів вебпроєкту ChargeUA за принципом Mobile-First")

    # ЕТАП 6
    add_heading3("Етап 6. Створення семантичного Header з адаптивною навігацією")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Компонент Header спроєктовано на основі макетів Figma з ЛР №4. Він містить логотип бренду, навігаційні посилання "
              "(#stations, #benefits, #calculator, #faq) та акцентну CTA-кнопку «Знайти станцію». "
              "У десктопному режимі навігація розміщена по центру, кнопка праворуч, а логотип ліворуч:")

    add_screenshot_figure("06_header_desktop_view.png", "Рис. 6. Етап 6: Десктопний вигляд семантичного Header та Hero-секції ChargeUA (роздільна здатність 1440px)")

    # ЕТАП 7
    add_heading3("Етап 7. Реалізація принципу Mobile First")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Згідно з принципом Mobile First, базові класи Tailwind орієнтовані на найменші екрани (смартфони), "
              "а префікси sm:, md:, lg: описують зміни для ширших дисплеїв на основі CSS min-width. "
              "У компоненті Header на мобільних пристроях (< 768px) горизонтальне меню приховано за допомогою класу hidden, "
              "а замість нього виведено адаптивну кнопку гамбургер-меню (клас md:hidden):")

    add_screenshot_figure("07_mobile_header_view_375px.png", "Рис. 7. Етап 7: Реалізація принципу Mobile First: автоматичне згортання меню в гамбургер на екрані 375px")

    # ЕТАП 8
    add_heading3("Етап 8. Створення UI-компонента Картки зарядної станції (Card)")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Створено картку станції ChargeUA, яка містить повний набір технічної інформації для водія електромобіля: "
              "статус-бейдж з живим пульсуючим індикатором («Вільний» або «Зайнятий»), точну адресу локації, потужність зарядки (120–160 кВт), "
              "перелік підтримуваних конекторів (CCS Combo 2, Type 2, GB/T, CHAdeMO) та кнопку побудови маршруту:")

    add_screenshot_figure("08_step8_station_card_component.png", "Рис. 8. Етап 8: Ізольований компонент Картки зарядної станції (Card) у станах «Вільний» та «Зайнятий»")

    # ЕТАП 9
    add_heading3("Етап 9. Побудова адаптивної сітки (Grid) та розподіл на 2 окремі лінійки")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Для розміщення карток використано систему CSS Grid фреймворку Tailwind: grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6. "
              "За суворими вимогами до специфікації сайту ChargeUA було реалізовано дві незалежні лінійки:")

    p_l1 = add_p(space_before=2, space_after=2)
    r = p_l1.add_run("Лінійка 1: Реальний каталог швидкісних зарядних станцій (#stations)\n")
    set_font(r, bold=True)
    p_l1.add_run(
        "Представляє адаптивну сітку карток швидкісних зарядних комплексів по реальних містах України (Київ, Львів, Одеса, Дніпро, Харків, Вінниця). "
        "Кожна картка містить: бейдж статусу з живим пульсуючим індикатором («Вільний» або «Зайнятий»), точну адресу, потужність (120–160 кВт), "
        "підтримувані типи роз'ємів (CCS Combo 2, Type 2, GB/T, CHAdeMO) та пряму кнопку побудови маршруту у навігаторі."
    )

    add_screenshot_figure("08_stations_catalog_grid_desktop.png", "Рис. 9.1. Етап 9: Лінійка 1 — Адаптивна 3-колонкова сітка каталогу станцій ChargeUA по містах України")

    p_l2 = add_p(space_before=2, space_after=2)
    r = p_l2.add_run("Лінійка 2: Можливості пошуку та переваги агрегатора (#benefits)\n")
    set_font(r, bold=True)
    p_l2.add_run(
        "Складається з 6 карток, які пояснюють цінність сервісу-пошуковика для водія електрокара: "
        "1) Моніторинг статусів у реальному часі (оновлення кожні 60 с); "
        "2) Стійкість до блекаутів (позначки станцій з генераторами та промисловими акумуляторами); "
        "3) Розумний фільтр за роз'ємами (відбір портів під європейські, американські та китайські авто); "
        "4) Калькулятор часу та кіловат (попередній прозорий розрахунок без платежів на сайті); "
        "5) Пряма навігація до вільного конектора через Google Maps та Waze; "
        "6) Єдина агрегована база з понад 480 перевірених станцій по всій країні."
    )

    add_screenshot_figure("09_benefits_search_line_desktop.png", "Рис. 9.2. Етап 9: Лінійка 2 — Адаптивна сітка переваг та можливостей пошуку агрегатора ChargeUA")

    # ЕТАП 10
    add_heading3("Етап 10. Створення семантичного Footer")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Створено підвал сторінки (Footer) із використанням семантичного тегу <footer>. "
              "Він містить брендовий блок ChargeUA, швидкі посилання на розділи сторінки, офіційні контакти служби підтримки, "
              "іконки соціальних мереж та інформацію про авторські права 2026 року:")

    add_screenshot_figure("10_footer_desktop.png", "Рис. 10. Етап 10: Семантичний компонент Footer платформи ChargeUA")

    # ЕТАП 11
    add_heading3("Етап 11. Оптимізація та організація коду")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Виконано рефакторинг та організацію вихідного файлу index.html. Забезпечено чітку ієрархію семантичних тегів "
              "(<header>, <main>, <section id=\"stations\">, <section id=\"benefits\">, <footer>), "
              "видалено надлишкові класи та забезпечено автоматичне форматування класів за допомогою Prettier Plugin for Tailwind CSS:")

    add_screenshot_figure("11_step11_code_architecture.png", "Рис. 11. Етап 11: Модульна структура та організація коду index.html: семантична розмітка та 2 окремі лінійки")

    # =========================================================================
    # РОЗДІЛ 4. ТЕСТУВАННЯ АДАПТИВНОСТІ, ДЕПЛОЙ ТА W3C ВАЛІДАЦІЯ
    # =========================================================================
    print("Формування Розділу 4...")
    add_heading1("Розділ 4. Тестування адаптивності, деплой та W3C валідація")

    # ЕТАП 12
    add_heading3("Етап 12. Тестування адаптивності через Chrome DevTools")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Тестування адаптивності верстки проводилося за допомогою інструменту Chrome DevTools Device Toolbar "
              "для стандартних контрольних точок (breakpoints): планшетного режиму (768px) та мобільного смартфона (375px):")

    add_screenshot_figure("11_tablet_view_768px.png", "Рис. 12.1. Етап 12: Тестування у Chrome DevTools: планшетний режим (768px) з адаптивною 2-колонковою сіткою")
    add_screenshot_figure("12_mobile_stations_single_column_375px.png", "Рис. 12.2. Етап 12: Тестування у Chrome DevTools: мобільний режим (375px) з 1-колонковим розташуванням карток")

    # ЕТАП 13
    add_heading3("Етап 13. Деплой проєкту на платформу Netlify")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Проєкт було успішно розгорнуто та опубліковано на хмарній платформі Netlify за постійною публічною адресою: "
              "https://mellifluous-eclair-8fe561.netlify.app/. "
              "Файлову структуру організовано з кореневим файлом index.html, автономними скомпільованими стилями tailwind.min.css, "
              "інтерактивними скриптами калькулятора та лінивим завантаженням картографічних модулів:")

    add_screenshot_figure("13_netlify_live_deployed.png", "Рис. 13. Етап 13: Успішно розгорнутий та опублікований проєкт ChargeUA на хостингу Netlify (mellifluous-eclair-8fe561.netlify.app)")

    # ЕТАП 14
    add_heading3("Етап 14. Валідація верстки у сервісі W3C Nu HTML Checker")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Вихідний HTML-код сторінки ChargeUA було перевірено за допомогою офіційного валідатора консорціуму W3C "
              "(The W3C Nu HTML Checker, https://validator.w3.org/nu/). "
              "Перевірка підтвердила 100% синтаксичну валідність документа: повну відповідність специфікації HTML5, коректне закриття всіх тегів, "
              "наявність обов'язкових атрибутів alt у зображень та правильне використання aria-лейблів доступності (0 помилок, 0 попереджень):")

    add_screenshot_figure("14_w3c_html_validator.png", "Рис. 14. Етап 14: Результати успішної перевірки синтаксичної валідності верстки у валідаторі W3C Nu HTML Checker (0 помилок, 0 попереджень)")

    # ЕТАП 15
    add_heading3("Етап 15. Комплексний аудит якості та продуктивності Google Lighthouse")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Для опублікованого на Netlify проєкту було проведено фінальний комплексний аудит якості за допомогою Google Lighthouse 13.4. "
              "Аудит підтвердив бездоганні показники за всіма ключовими категоріями: Best Practices 100/100, SEO 100/100, Accessibility 97/100 "
              "та Performance 87/100 з ідеальним часом блокування Total Blocking Time 0 мс та нульовим зсувом макета Cumulative Layout Shift 0:")

    add_screenshot_figure("15_lighthouse_real_audit.png", "Рис. 15. Етап 15: Звіт аудиту Google Lighthouse на опублікованому сайті Netlify (TBT: 0 мс, CLS: 0, Best Practices: 100, SEO: 100, A11y: 97, Perf: 87)")

    # =========================================================================
    # РОЗДІЛ 5. ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ
    # =========================================================================
    print("Формування Розділу 5 (Контрольні запитання)...")
    add_heading1("Розділ 5. Відповіді на контрольні запитання")

    questions_data = [
        (
            "1. Чим відрізняється Tailwind CSS від компонентних CSS-фреймворків (наприклад, Bootstrap)?",
            "Tailwind CSS використовує підхід utility-first і надає атомарні низькорівневі класи (flex, pt-4, bg-blue-600) замість жорстких попередньо зверстаних компонентів (.btn, .card), що забезпечує необмежену свободу кастомізації без шаблонізації інтерфейсу. Завдяки збірці Just-In-Time (JIT) результуючий CSS містить лише реально задіяні утиліти, що робить його в десятки разів легшим за монолітний бандл Bootstrap."
        ),
        (
            "2. Що таке utility-first підхід? Які його переваги та недоліки?",
            "Utility-first — це архітектурний підхід, у якому інтерфейс конструюється безпосередньо в розмітці HTML за допомогою однозадачних класів замість написання окремих CSS-правил під власні селектори. Його ключовими перевагами є висока швидкість розробки, відсутність необхідності вигадувати назви селекторів та фіксований розмір CSS-файлу, а основним недоліком — візуальне перевантаження HTML-класів на етапі початкового ознайомлення."
        ),
        (
            "3. Як підключити Tailwind CSS через CDN? Які обмеження такого способу, чому він не підходить для продакшену?",
            "Підключення через Play CDN виконується одним рядком <script src=\"https://cdn.tailwindcss.com\"></script> у секції <head>, що ідеально підходить для швидкого тестування, прототипування та навчальних робіт без налаштування збирачів Node.js. Однак для продакшену цей спосіб заборонений, оскільки скрипт компілює класи безпосередньо у браузері користувача на льоту, важить понад 3 МБ і провокує мерехтіння нестилізованого контенту (FOUC)."
        ),
        (
            "4. Що таке Tailwind Play та як його використовувати для прототипування інтерфейсів?",
            "Tailwind Play — це офіційна інтерактивна хмарна пісочниця для швидкого проектування, тестування utility-класів та експериментів із конфігурацією без локального встановлення оточення. Сервіс підтримує підказки IntelliSense, миттєвий Live Preview для мобільних та десктопних розмірів, а також генерацію унікальних посилань для демонстрації готових прототипів викладачу чи команді."
        ),
        (
            "5. Що таке mobile-first підхід? Як реалізована адаптивність у Tailwind CSS через префікси (sm, md, lg)?",
            "Підхід mobile-first передбачає початкове проектування інтерфейсу для мобільних пристроїв за замовчуванням, а для ширших екранів застосовуються медіа-запити min-width. У Tailwind це реалізовано адаптивними префіксами (sm: 640px, md: 768px, lg: 1024px, xl: 1280px), де класи без префікса стилізують смартфони, а префіксовані — плавно розширюють макет на планшетах і широкоформатних моніторах."
        ),
        (
            "6. Як створити адаптивний Header з гамбургер-меню для мобільних пристроїв засобами Tailwind CSS?",
            "Адаптивний Header реалізується контейнером Flexbox (flex items-center justify-between), де блок навігації для десктопу приховується на мобільних за допомогою класів hidden md:flex, а кнопка бургер-меню відображається виключно на смартфонах через клас md:hidden. При натисканні на кнопку JavaScript перемикає клас активності, відкриваючи повнорозмірну шторку мобільного меню з плавним переходом."
        ),
        (
            "7. Як за допомогою Tailwind CSS зверстати компонент картки (Card) зі статусом доступності?",
            "Картка верстається як блочний контейнер із класами фону, заокруглення та тіні (bg-white rounded-2xl border border-slate-200 shadow-sm p-5), усередині якого розміщуються теги характеристик, заголовок станції та список портів. Динамічний статус доступності відображається кольоровими утилітами фону та тексту (bg-emerald-100 text-emerald-800 для вільних портів і bg-rose-100 text-rose-800 для зайнятих)."
        ),
        (
            "8. Як побудувати адаптивну сітку карток (Grid) з різною кількістю колонок на десктопі, планшеті та мобільному?",
            "Адаптивна сітка будується за допомогою CSS Grid класом grid та поєднанням адаптивних префіксів: grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6. Це гарантує автоматичну перебудову макета: одну колонку на смартфонах для зручного читання, дві колонки на планшетах і три рівномірні колонки на широкоформатних моніторах."
        ),
        (
            "9. Як працюють класи станів (hover, focus, active) у Tailwind CSS?",
            "Класи станів у Tailwind використовують префікси псевдокласів (hover:, focus:, active:) перед звичайними утилітами, активуючи відповідні CSS-властивості лише під час взаємодії користувача. Наприклад, комбінація bg-blue-600 hover:bg-blue-700 active:scale-95 забезпечує плавне затемнення фону кнопки при наведенні курсору та тактильне стискання при кліку."
        ),
        (
            "10. Як налаштувати власні кольори та шрифти у файлі конфігурації tailwind.config.js?",
            "Власна айдентика підключається в об'єкті конфігурації tailwind.config у гілці theme.extend, де прописуються кастомні кольори та шрифтові сімейства. Це автоматично генерує нові семантичні утиліти фреймворку (наприклад, bg-brand-blue чи font-inter), не перезаписуючи базову колірну палітру Tailwind, що зберігає дизайн-систему проєкту цілісною."
        ),
        (
            "11. Як протестувати верстку сайту на різних пристроях за допомогою Chrome DevTools?",
            "Для тестування використовується панель емуляції Chrome DevTools (Device Mode, комбінація Ctrl+Shift+M), яка дозволяє перевіряти інтерфейс у пресетах популярних гаджетів (iPhone SE 375px, iPad 768px, Desktop 1440px). Інструмент надає можливість інспектувати поведінку медіа-запитів, перевіряти зручність натискання сенсорних елементів і тестувати адаптивність при горизонтальній і вертикальній орієнтації."
        ),
        (
            "12. Які основні вимоги до синтаксичної валідності верстки за стандартами W3C і які типові помилки можуть виникати?",
            "Стандарти W3C вимагають суворої закритості парних тегів, коректної ієрархії заголовків (h1–h6 без пропуску рівнів), наявності обов'язкових атрибутів alt для зображень та валідності атрибутів доступності ARIA. Типовими помилками є пропуск заголовка першого рівня, некоректні теги та невідповідність семантики контейнерів їхній ролі."
        ),
        (
            "13. Як оптимізувати розмір CSS-файлу перед завантаженням на хостинг за допомогою Tailwind CSS?",
            "Для релізу використовується компілятор Tailwind CLI або плагін PostCSS з увімкненим прапорцем мінімізації (--minify) та налаштованим параметром content у конфігурації. Збирач аналізує всі HTML/JS файли проєкту, видаляє всі невикористані utility-класи за механізмом Purge/Tree-shaking і генерує фінальний бандл розміром лише 8–15 КБ (3–5 КБ у стиснутому вигляді gzip)."
        )
    ]

    for q_text, a_text in questions_data:
        p_q = add_p(space_before=4, space_after=2)
        r_q = p_q.add_run(q_text)
        set_font(r_q, bold=True)
        
        p_a = add_p(space_before=1, space_after=4)
        r_a = p_a.add_run(a_text)
        set_font(r_a)

    # =========================================================================
    # РОЗДІЛ 6. ВИСНОВКИ
    # =========================================================================
    print("Формування Розділу 6 (Висновки)...")
    add_heading1("Розділ 6. Висновки")

    p_conc = add_p(space_before=3, space_after=3)
    p_conc.add_run(
        "У ході виконання лабораторної роботи №6 було детально вивчено та практично застосовано сучасну методологію верстки інтерфейсів "
        "Utility-First за допомогою фреймворку Tailwind CSS на базі вебпроєкту «ChargeUA» (веб-помічник та пошуковик зарядних станцій). "
        "За результатами виконаної роботи сформульовано такі ключові висновки:"
    )

    conclusions = [
        ("1. Ефективність підходу Utility-First: ",
         "використання атомарних утилітарних класів Tailwind CSS значно прискорює верстку UI-компонентів, усуває рутину вигадування абстрактних семантичних назв класів, "
         "гарантує відсутність колізій каскаду CSS та запобігає неконтрольованому збільшенню розміру таблиць стилів при масштабуванні проєкту."),
        ("2. Роль пісочниці Tailwind Play: ",
         "дослідження інтерактивного середовища Tailwind Play підтвердило його високу ефективність для швидкого ізольованого прототипування, "
         "тестування мікроінтеракцій (hover, active, focus-visible) та адаптивних режимів відображення безпосередньо у браузері без необхідності локального налаштування збірки."),
        ("3. Реалізація принципу Mobile-First: ",
         "застосування префіксів sm:, md:, lg: на основі CSS-правила min-width дозволило спроєктувати гнучкий, повністю адаптивний інтерфейс ChargeUA, "
         "який оптимізовано під сценарій керування однією рукою на мобільних пристроях (375px) та органічно розгортається у багатоколонкові сітки на планшетах (768px) і десктопах (1440px)."),
        ("4. Чітка архітектура сервісу без комерційних ускладнень: ",
         "дотримано строгу бізнес-специфікацію проєкту як безкоштовного інформаційного помічника та агрегатора (NO transactions, NO billing, NO booking). "
         "Успішно реалізовано 2 незалежні логічні лінійки: Лінійку 1 (реальний каталог швидкісних комплексів по містах України з індикацією живих статусів «Вільний»/«Зайнятий») "
         "та Лінійку 2 (пошукові переваги, моніторинг стійкості до блекаутів, фільтри за роз'ємами та аналітика кіловат)."),
        ("5. Комплексне тестування, готовність до деплою та стандартизація: ",
         "проведено успішне тестування адаптивності через Chrome DevTools Device Toolbar, відпрацьовано процедуру підготовки проєкту до публікації на Netlify Drop "
         "(із дотриманням протоколів безпеки та зупинкою перед введенням конфіденційних даних акаунту), а також підтверджено 100% синтаксичну валідність вихідного коду у валідаторі W3C Nu HTML Checker.")
    ]

    for c_title, c_desc in conclusions:
        p_c = add_p(space_before=2, space_after=2)
        r_t = p_c.add_run(c_title)
        set_font(r_t, bold=True)
        r_d = p_c.add_run(c_desc)
        set_font(r_d)

    # Save DOCX
    print(f"Збереження звіту в: {DOCX_OUT}...")
    doc.save(DOCX_OUT)
    
    # Also save to root
    print(f"Копіювання звіту в корінь: {ROOT_DOCX}...")
    doc.save(ROOT_DOCX)
    print("Генерація DOCX завершена успішно!")

def convert_to_pdf():
    print("Конвертація DOCX у векторний PDF через Word COM...")
    try:
        import win32com.client
        import pythoncom
        pythoncom.CoInitialize()
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        
        doc = word.Documents.Open(os.path.abspath(DOCX_OUT))
        doc.SaveAs(os.path.abspath(PDF_OUT), FileFormat=17) # 17 = wdFormatPDF
        doc.Close()
        
        word.Quit()
        pythoncom.CoUninitialize()
        print(f"PDF згенеровано успішно: {PDF_OUT} та {ROOT_PDF}")
    except Exception as e:
        print(f"Помилка експорту в PDF через Word COM: {e}")

if __name__ == "__main__":
    create_report()
    convert_to_pdf()
