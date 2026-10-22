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
DOCX_OUT = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.docx")
PDF_OUT = os.path.join(REPORT_DIR, "Лемішка_ПП-24_Л6_ChargeUA.pdf")
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
    p.add_run("За допомогою ШІ-чату було сформульовано системний промпт для створення кнопки Primary CTA Button «Знайти станцію» "
              "із дотриманням суворих вимог доступності (WCAG) та ергономіки тач-пристроїв.")

    add_heading4("Промпт-лог створення кнопки")
    p = add_p(space_before=2, space_after=2)
    r = p.add_run("Крок 1. Початковий системний запит (Модель: Claude 3.5 Sonnet / Antigravity Agent)")
    set_font(r, bold=True)

    add_callout(
        "Запит:",
        "«Ти — Senior Frontend Developer та UI/UX Engineer. Створи Primary CTA Button «Знайти станцію» для вебплатформи ChargeUA "
        "виключно за допомогою HTML5 та Tailwind CSS. Вимоги до кнопки: "
        "- синій фірмовий фон #2563EB (bg-blue-600); "
        "- білий текст, розмір 16px, font-semibold; "
        "- симетричні відступи px-6 py-3; "
        "- радіус скруглення 12px (rounded-xl); "
        "- інтерактивні стани hover (bg-blue-500) та active (bg-blue-700); "
        "- плавна анімація transition duration-200; "
        "- мінімальна висота 44px для підтримки тач-інтерфейсів (WCAG Touch Target Size); "
        "- контур фокусу focus-visible для клавіатурної навігації. "
        "Кнопка має бути суто пошуковою (ніяких кнопок бронювання чи оплати). Поясни всі застосовані класи.»"
    )

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат генерації: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Отримано семантичний код кнопки із вбудованою SVG-іконкою стрілки, ефектами плавної зміни фону та розміром 44px.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Кнопка потребувала валідації в реальному темному оточенні поруч із карткою зарядної станції у пісочниці Tailwind Play.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r = p.add_run("Крок 2. Коригувальний запит та тестування у Tailwind Play")
    set_font(r, bold=True)

    add_callout(
        "Запит:",
        "«Додай до кнопки ефект світіння shadow-lg shadow-blue-600/30 і розмісти її всередині демонстраційної картки станції "
        "з темним фоном bg-slate-800, зеленим пульсуючим бейджем вільного порту (120 кВт CCS2) та адресою в Києві для тестування в Tailwind Play.»"
    )

    p = add_p(space_before=2, space_after=4)
    r1 = p.add_run("Результат тестування: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Код було протестовано у Tailwind Play. Змінено параметри bg-*, px-*, rounded-* та зафіксовано готовність компонента.")
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
    add_heading3("Етап 13. Процес підготовки до деплою на сервісі Netlify")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Проєкт було підготовлено для розгортання на платформі Netlify Drop (https://app.netlify.com/drop). "
              "Файлову структуру організовано з кореневим файлом index.html та відносними шляхами до ресурсів. "
              "При переході на форму деплою сервіс Netlify зажадав авторизації користувача (Login / Sign Up). "
              "Згідно з регламентом виконання роботи та суворою інструкцією щодо безпеки облікових даних, процес було зупинено на етапі запиту входу в акаунт, "
              "а стан інтерфейсу авторизації зафіксовано на знімку екрана:")

    add_screenshot_figure("13_netlify_login_prompt.png", "Рис. 13. Етап 13: Інтерфейс авторизації сервісу Netlify (зупинка процесу перед введенням персональних облікових даних)")

    # ЕТАП 14
    add_heading3("Етап 14. Валідація верстки у сервісі W3C Nu HTML Checker")
    p = add_p(space_before=2, space_after=3)
    p.add_run("Вихідний HTML-код сторінки ChargeUA було перевірено за допомогою офіційного валідатора консорціуму W3C "
              "(The W3C Nu HTML Checker, https://validator.w3.org/nu/). "
              "Перевірка підтвердила 100% синтаксичну валідність документа: повну відповідність специфікації HTML5, коректне закриття всіх тегів, "
              "наявність обов'язкових атрибутів alt у зображень та правильне використання aria-лейблів доступності:")

    add_screenshot_figure("14_w3c_html_validator.png", "Рис. 14. Етап 14: Результати успішної перевірки синтаксичної валідності верстки у валідаторі W3C Nu HTML Checker")

    # =========================================================================
    # РОЗДІЛ 5. ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ
    # =========================================================================
    print("Формування Розділу 5 (Контрольні запитання)...")
    add_heading1("Розділ 5. Відповіді на контрольні запитання")

    questions_data = [
        (
            "1. Що таке Tailwind CSS і чим він відрізняється від традиційних CSS-фреймворків (наприклад, Bootstrap)?",
            "Tailwind CSS — це сучасний utility-first (утилітарно-орієнтований) CSS-фреймворк, який замість надання готових монолітних UI-компонентів "
            "(як-от .btn, .card, .navbar у Bootstrap) пропонує набір низькорівневих атомарних класів-утиліт (наприклад, flex, pt-4, text-center, bg-blue-600). "
            "Ключова відмінність полягає в архітектурній свободі: Bootstrap нав'язує стандартизований дизайн і призводить до однотипного вигляду сайтів, "
            "тоді як Tailwind діє як «будівельні блоки», дозволяючи створювати абсолютно унікальний та кастомний дизайн безпосередньо в розмітці HTML. "
            "Крім того, завдяки механізму JIT (Just-In-Time) Tailwind компілює в кінцевий бандл лише ті класи, які реально зустрічаються у проєкті, "
            "що забезпечує розмір збірки у межах 10–25 Кб проти сотень кілобайт нерозібраного коду в Bootstrap."
        ),
        (
            "2. Що таке utility-first підхід? Які його переваги та недоліки?",
            "Utility-first (спочатку утиліти) — це методологія верстки, за якої інтерфейс створюється шляхом комбінування дрібних, спеціалізованих утилітарних "
            "класів із єдиною відповідальністю (Single Responsibility Principle) прямо в HTML-шаблоні.\n"
            "Переваги підходу:\n"
            "• Відсутність потреби вигадувати абстрактні імена класів (наприклад, .station-card-wrapper-inner);\n"
            "• CSS перестає розростатися зі збільшенням проєкту — нові сторінки перекористовують уже існуючі утиліти;\n"
            "• Безпека модифікації: зміна класів одного елемента гарантовано не ламає стилі інших блоків сторінки;\n"
            "• Висока швидкість прототипування та підтримка адаптивності через лаконічні префікси прямо в розмітці.\n"
            "Недоліки підходу:\n"
            "• Візуальне перевантаження HTML-розмітки великою кількістю класів у атрибутах class=\"...\";\n"
            "• Необхідність запам'ятовувати або мати постійний доступ до довідника назв утиліт Tailwind;\n"
            "• Складність прямого дублювання стилів однакових елементів без компонентного підходу (вирішується через компоненти React/Vue або директиву @apply)."
        ),
        (
            "3. Як підключити Tailwind CSS до проєкту через CDN? Для чого цей спосіб підходить, а для чого — ні?",
            "Для підключення через CDN у секцію <head> HTML-документа додається один рядок скрипта:\n"
            "<script src=\"https://cdn.tailwindcss.com\"></script>\n"
            "Цей скрипт містить повноцінний рушій Tailwind Play CDN, який аналізує DOM-дерево сторінки під час завантаження в браузері та динамічно генерує необхідні стилі.\n"
            "Для чого підходить:\n"
            "• Навчальні цілі, швидкі лабораторні роботи та демонстраційні стенди;\n"
            "• Швидке інтерактивне прототипування інтерфейсів;\n"
            "• Експерименти в середовищі Tailwind Play.\n"
            "Для чого НЕ підходить (промисловий Production):\n"
            "• Для реальних високонавантажених сайтів використання Play CDN суворо заборонено розробниками фреймворку, оскільки клієнт завантажує важкий рушій компілятора (близько 3 Мб нестисненого JS), що спричиняє затримку рендерингу (FOUC — Flash of Unstyled Content) і погіршує показники Core Web Vitals (LCP, CLS)."
        ),
        (
            "4. Що таке Tailwind Play і як його можна використовувати в процесі розробки?",
            "Tailwind Play (https://play.tailwindcss.com/) — це офіційна хмарна пісочниця (sandbox) для розробки та тестування коду на базі Tailwind CSS. "
            "Вона містить повноцінне середовище редактора з трьома вкладками (HTML-розмітка, кастомний CSS, конфігурація tailwind.config.js / @theme), "
            "інтегрований IntelliSense, панель миттєвого попереднього перегляду (Live Preview) та генератор кінцевого CSS.\n"
            "Використання в розробці:\n"
            "• Ізольоване верстання складних UI-компонентів (кнопок, дропдаунів, карток) без розгортання локального оточення;\n"
            "• Тестування адаптивності через вбудований перемикач в'юпортів (Mobile, Tablet, Desktop);\n"
            "• Перевірка сумісності колірних палітр, шрифтових пар та станів темної теми (Dark Mode);\n"
            "• Спільне обговорення коду в команді за допомогою кнопки «Share», яка генерує унікальне посилання на стан проєкту."
        ),
        (
            "5. Що таке mobile-first підхід? Як він реалізований у Tailwind CSS за допомогою брейкпоінтів (sm, md, lg)?",
            "Mobile-first — це методологія веброзробки та проєктування інтерфейсів, за якої спочатку проєктується та стилізується версія для найменших екранів "
            "(мобільних смартфонів), а потім поступово додаються ускладнення та перебудови для більших екранів (планшетів, ноутбуків, моніторів).\n"
            "Реалізація в Tailwind CSS:\n"
            "Всі базові класи без префіксів діють на всіх екранах починаючи від найменших (0px і вище). "
            "Адаптивні префікси (breakpoints) генерують CSS-медіазапити на основі властивості min-width (а не max-width):\n"
            "• sm: — @media (min-width: 640px) — смартфони в альбомній орієнтації та малі планшети;\n"
            "• md: — @media (min-width: 768px) — стандартні планшети;\n"
            "• lg: — @media (min-width: 1024px) — ноутбуки та десктопи;\n"
            "• xl: — @media (min-width: 1280px) — монітори високої чіткості;\n"
            "• 2xl: — @media (min-width: 1536px) — надширокі екрани.\n"
            "Приклад у проєкті ChargeUA: клас class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3\" означає: на мобільних пристроях 1 колонка, від 768px — 2 колонки, від 1024px — 3 колонки."
        ),
        (
            "6. Як створити адаптивний Header з гамбургер-меню для мобільних пристроїв та повною навігацією для десктопу?",
            "Для реалізації адаптивного Header використовується комбінація Flexbox та класів видимості (display):\n"
            "1. Головний контейнер отримує класи flex items-center justify-between для рознесення логотипу ліворуч, а навігації та дій праворуч;\n"
            "2. Блок десктопної навігації <nav> отримує класи hidden md:flex items-center gap-8. "
            "Клас hidden повністю приховує меню на мобільних екранах (display: none), а md:flex активує горизонтальний флекс-контейнер на екранах від 768px;\n"
            "3. Кнопка виклику гамбургер-меню огортається в семантичний тег <button> з класами md:hidden p-2 rounded-lg text-slate-300 hover:text-white. "
            "Це гарантує, що гамбургер відображається виключно на мобільних пристроях і зникає на десктопі;\n"
            "4. Відкриття випадного мобільного списку реалізується через перемикання класу hidden за допомогою легкого JS або нативного CSS :focus-within / peer."
        ),
        (
            "7. Як працює CSS Grid у Tailwind CSS? Як створити сітку карток, яка автоматично перебудовується на різну кількість колонок залежно від розміру екрана?",
            "CSS Grid у Tailwind активується класом display: grid (клас grid). Кількість колонок визначається утилітами grid-cols-{n}, "
            "а проміжки між елементами — класами gap-{size} (наприклад, gap-6 = 1.5rem = 24px).\n"
            "Для створення адаптивної сітки, яка автоматично реконфігурується під розмір екрана, комбінують базовий мобільний клас із адаптивними префіксами:\n"
            "<div class=\"grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-6\">\n"
            "  <!-- Картки станцій ChargeUA -->\n"
            "</div>\n"
            "Логіка поведінки:\n"
            "• Мобільні пристрої (< 640px) отримують grid-cols-1 (одна колонка на 100% ширини);\n"
            "• Планшети (>= 768px) отримують md:grid-cols-2 (дві рівні колонки по 50%);\n"
            "• Десктопи (>= 1024px) отримують lg:grid-cols-3 (три колонки по 33.33%).\n"
            "Це повністю усуває необхідність ручного написання медіазапитів."
        ),
        (
            "8. Що таке стани елементів (hover, focus, active, disabled) і як вони стилізуються за допомогою префіксів Tailwind?",
            "Стани елементів (State Variants / Pseudo-classes) відображають реакцію інтерфейсу на дії користувача (наведення курсора, табуляція з клавіатури, "
            "момент кліку або неактивний стан контролу).\n"
            "У Tailwind стилізація станів здійснюється додаванням назви псевдокласу перед утилітою через двокрапку:\n"
            "• hover: — стан наведення миші (hover:bg-blue-500, hover:shadow-xl);\n"
            "• focus: та focus-visible: — отримання елементом фокусу, критично для клавіатурної доступності (focus:ring-2 focus:ring-blue-500/50 focus:outline-none);\n"
            "• active: — момент фізичного натискання клавіші миші або пальця на тачскріні (active:bg-blue-700 active:scale-95);\n"
            "• disabled: — стан блокування взаємодії з елементом (disabled:opacity-50 disabled:cursor-not-allowed);\n"
            "• group-hover: — зміна стилів дочірнього елемента при наведенні курсора на батьківський контейнер із класом group."
        ),
        (
            "9. Як забезпечити контрастність тексту та доступність (accessibility) при використанні Tailwind CSS?",
            "Доступність (WCAG 2.1 AA/AAA) при використанні Tailwind забезпечується дотриманням системних правил:\n"
            "1. Коефіцієнт контрастності кольорів (Color Contrast Ratio): нормальний текст повинен мати контраст не менше ніж 4.5:1 щодо фону. "
            "У проєкті ChargeUA на темному фоні bg-slate-900 (#0f172a) використано білий text-white (#ffffff, контраст 16.5:1) та світло-сірий text-slate-300 (#cbd5e1, контраст 9.8:1);\n"
            "2. Розмір клікабельних зон (Touch Target Size): кнопки та інтерактивні елементи отримують класи min-h-[44px] min-w-[44px] або відповідні падінги py-3 px-6;\n"
            "3. Помітний фокус для скрінрідерів та клавіатури: обов'язкове використання класів focus-visible:ring-2 focus-visible:ring-offset-2;\n"
            "4. Семантичний прихований текст: утиліта sr-only (screen-reader only) дозволяє додати текстовий опис для незрячих користувачів, "
            "приховуючи його з екрана, але залишаючи доступним для асистивних технологій;\n"
            "5. Семантичні HTML5-теги: використання <header>, <nav>, <main>, <section>, <article>, <button>, <footer> замість нескінченних <div>."
        ),
        (
            "10. Які інструменти DevTools використовуються для тестування адаптивності та емуляції мобільних пристроїв?",
            "В інструментах розробника Chrome DevTools для тестування адаптивності використовується комплекс засобів:\n"
            "1. Device Mode (Device Toolbar, комбінація Ctrl+Shift+M) — вмикає віртуальний екран із можливістю вільного перетягування меж ширини/висоти "
            "або вибору пресетів популярних гаджетів (iPhone 14/15, Samsung Galaxy, iPad Pro);\n"
            "2. Емуляція сенсорного введення (Touch Simulation) — курсор миші трансформується у круговий імітатор дотику пальця для перевірки реакції hover/active;\n"
            "3. Мережеве дротелювання (Network Throttling) — симуляція повільних мобільних мереж (Fast 3G, Slow 3G) для оцінки завантаження шрифтів та CDN;\n"
            "4. Емуляція орієнтації пристрою (Landscape / Portrait) для тестування поведінки розмітки при повороті екрана;\n"
            "5. Панель Elements & Computed Styles — дозволяє інспектувати діючі CSS-медіазапити (@media min-width) та перевіряти, який саме клас Tailwind спрацював на поточному брейкпоінті."
        ),
        (
            "11. Як підготувати проєкт до деплою на Netlify через drag-and-drop? Які файли обов'язково мають бути в корені?",
            "Для успішного деплою статичного вебпроєкту на Netlify через інтерфейс Netlify Drop (drag-and-drop) необхідно дотримуватися структури:\n"
            "1. Головний файл index.html обов'язково повинен знаходитися безпосередньо у корені папки, яку перетягують у вікно браузера (не всередині додаткових підпапок);\n"
            "2. Усі шляхи до підключених ресурсів (CSS-стилів, зображень, шрифтів, скриптів) повинні бути відносними (наприклад, href=\"css/style.css\" або src=\"assets/images/logo.svg\"), а не абсолютними локальними шляхами файлової системи (як-от D:/...);\n"
            "3. У проєкті не повинно бути зайвих бінарних архівів, тимчасових системних файлів (.DS_Store, Thumbs.db) чи незакритих текстових нотаток;\n"
            "4. Якщо сервіс вимагає авторизації (входу через GitHub/Google/Email), користувач проходить автентифікацію, після чого папка завантажується на сервери Netlify і сервіс генерує глобальну публічну URL-адресу з безкоштовним SSL-сертифікатом (HTTPS)."
        ),
        (
            "12. Що перевіряє валідатор W3C і чому важливо валідувати HTML-код після використання утилітарних класів?",
            "Валідатор W3C (World Wide Web Consortium Nu HTML Checker) перевіряє синтаксичну та структурну коректність HTML-коду відповідно до офіційних стандартів W3C і WHATWG. "
            "Він виявляє:\n"
            "• Пропущені або незакриті теги, порушення ієрархії вкладеності (наприклад, розміщення блочного <div> всередині строкового <span>);\n"
            "• Відсутність обов'язкових атрибутів (alt у <img>, lang у <html>, charset у <head>);\n"
            "• Дублювання унікальних ідентифікаторів id=\"...\";\n"
            "• Використання застарілих або неіснуючих тегів та атрибутів.\n"
            "Чому це критично після використання Tailwind CSS:\n"
            "При активному додаванні великої кількості утилітарних класів (class=\"...\") розробник може випадково пошкодити лапки, сплутати закриття тегів або "
            "втратити семантичний фокус, перетворивши розмітку на «div-soup». Валідація W3C підтверджує, що попри утилітарну стилізацію семантичний каркас сторінки "
            "залишається ідеальним, доступним для пошукових роботів (SEO) та асистивних технологій."
        ),
        (
            "13. Як оптимізувати розмір кінцевого CSS-файлу при використанні повної збірки Tailwind CSS (PostCSS / Tailwind CLI)?",
            "Для промислового середовища розмір стилів Tailwind мінімізується за допомогою офіційного механізму очищення (Purging / Tree-shaking), інтегрованого в рушій Tailwind CLI / PostCSS:\n"
            "1. Конфігурація сканування контенту: у файлі tailwind.config.js у масиві content задаються точні патерни всіх вихідних файлів проєкту:\n"
            "   content: ['./*.html', './src/**/*.{js,ts,jsx,tsx}']\n"
            "2. Механізм Purge / Tree-shaking: під час складання рушій сканує всі зазначені файли регулярними виразами, фіксує лише ті назви класів, "
            "які реально зустрічаються у розмітці та скриптах, і видаляє абсолютно всі невикористані класи зі стандартної багатомегабайтної бази;\n"
            "3. CSS-мініфікація: запуск Tailwind CLI з прапорцем --minify додатково видаляє всі пробіли, коментарі та скорочує кольорові коди;\n"
            "4. Результат: розмір кінцевого production CSS-файлу зазвичай становить лише 8–20 Кб (у стисненому Gzip/Brotli форматі — 3–6 Кб), "
            "що забезпечує практично миттєве завантаження сторінки навіть на слабких мобільних з'єднаннях."
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
        
        # Also copy/export root PDF
        doc2 = word.Documents.Open(os.path.abspath(ROOT_DOCX))
        doc2.SaveAs(os.path.abspath(ROOT_PDF), FileFormat=17)
        doc2.Close()
        
        word.Quit()
        pythoncom.CoUninitialize()
        print(f"PDF згенеровано успішно: {PDF_OUT} та {ROOT_PDF}")
    except Exception as e:
        print(f"Помилка експорту в PDF через Word COM: {e}")

if __name__ == "__main__":
    create_report()
    convert_to_pdf()
