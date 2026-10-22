# -*- coding: utf-8 -*-
"""
Майстер-генератор повного розширеного звіту до Лабораторної роботи №6
з навчальної дисципліни «Вебтехнології та вебдизайн»
Тема: «Уставляння зовнішніх сервісів»

Автор: студент групи ПП-24 Лемішка Андрій Андрійович
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
    p4.paragraph_format.space_before = Pt(6)
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
    r = p5.add_run("до Лабораторної роботи №6\nз навчальної дисципліни «Вебтехнології та вебдизайн»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(13.5)

    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p6.paragraph_format.space_before = Pt(2)
    p6.paragraph_format.space_after = Pt(16)
    r = p6.add_run("«Уставляння зовнішніх сервісів: інтеграція Google Maps, панорам Street View 360°, YouTube/Vimeo, HTML5 Audio, інформерів та соціальних плагінів»")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(12.5)
    r.font.color.rgb = COLOR_DARK

    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell_left = tbl.cell(0, 0)
    cell_right = tbl.cell(0, 1)
    cell_left.width = Inches(3.2)
    cell_right.width = Inches(3.5)
    set_cell_margins(cell_left, 50, 50, 50, 50)
    set_cell_margins(cell_right, 50, 50, 50, 50)

    p_right = cell_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_right.paragraph_format.line_spacing = 1.2
    
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
    
    r_chk = p_right.add_run("Прийняла:\n")
    r_chk.font.size = Pt(11)
    r_chk.font.name = "Times New Roman"
    
    r_teach = p_right.add_run("к.т.н., доцент кафедри САПР\nЮрчак Ірина Юріївна\n\n")
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
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(14)
        r.font.color.rgb = COLOR_PRIMARY
    elif level == 2:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(12.5)
        r.font.color.rgb = COLOR_DARK
    else:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11.5)
        r.font.color.rgb = COLOR_TEXT
    return p

def add_body_p(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
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

def add_code_callout(doc, code_text, caption="Лістинг коду:"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.7)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, 80, 80, 120, 120)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_cap = p.add_run(caption + "\n")
    r_cap.bold = True
    r_cap.font.name = "Consolas"
    r_cap.font.size = Pt(9.5)
    r_cap.font.color.rgb = COLOR_PRIMARY

    r_code = p.add_run(code_text)
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(9.0)
    r_code.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_screenshot_figure(doc, img_name, fig_num, caption):
    img_path = os.path.join(SCREENSHOTS_DIR, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(3)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Inches(6.2))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(8)
        r_cap = p_cap.add_run(f"Рис. {fig_num} — {caption}")
        r_cap.italic = True
        r_cap.font.name = "Times New Roman"
        r_cap.font.size = Pt(10)
        r_cap.font.color.rgb = COLOR_MUTED

def add_qa_card(doc, q_num, question, short_ans, academic_ans, code_sample=None):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.7)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, 90, 90, 120, 120)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    r_num = p.add_run(f"Контрольне запитання №{q_num}:\n")
    r_num.bold = True
    r_num.font.name = "Times New Roman"
    r_num.font.size = Pt(11)
    r_num.font.color.rgb = COLOR_PRIMARY

    r_q = p.add_run(f"{question}\n\n")
    r_q.bold = True
    r_q.font.name = "Times New Roman"
    r_q.font.size = Pt(11.5)
    r_q.font.color.rgb = COLOR_DARK

    p_a1 = cell.add_paragraph()
    p_a1.paragraph_format.space_before = Pt(0)
    p_a1.paragraph_format.space_after = Pt(4)
    r_t1 = p_a1.add_run("1. Коротка змістовна відповідь: ")
    r_t1.bold = True
    r_t1.font.name = "Times New Roman"
    r_t1.font.size = Pt(11)
    r_t1.font.color.rgb = RGBColor(0x05, 0x96, 0x69)
    r_c1 = p_a1.add_run(short_ans)
    r_c1.font.name = "Times New Roman"
    r_c1.font.size = Pt(11)

    p_a2 = cell.add_paragraph()
    p_a2.paragraph_format.space_before = Pt(0)
    p_a2.paragraph_format.space_after = Pt(4)
    r_t2 = p_a2.add_run("2. Академічне пояснення та принцип роботи: ")
    r_t2.bold = True
    r_t2.font.name = "Times New Roman"
    r_t2.font.size = Pt(11)
    r_t2.font.color.rgb = COLOR_DARK
    r_c2 = p_a2.add_run(academic_ans)
    r_c2.font.name = "Times New Roman"
    r_c2.font.size = Pt(11)

    if code_sample:
        p_a3 = cell.add_paragraph()
        p_a3.paragraph_format.space_before = Pt(2)
        p_a3.paragraph_format.space_after = Pt(2)
        r_t3 = p_a3.add_run("3. Практичний приклад у проєкті ChargeUA:\n")
        r_t3.bold = True
        r_t3.font.name = "Times New Roman"
        r_t3.font.size = Pt(10.5)
        r_t3.font.color.rgb = COLOR_PRIMARY
        r_c3 = p_a3.add_run(code_sample)
        r_c3.font.name = "Consolas"
        r_c3.font.size = Pt(9.0)
        r_c3.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def build_complete_lab6_document():
    doc = Document()
    setup_document_styles(doc)

    # 1. ТИТУЛЬНА СТОРІНКА
    add_title_page(doc)

    # 2. МЕТА ТА ЗАВДАННЯ РОБОТИ
    add_header_styled(doc, "МЕТА РОБОТИ ТА ТЕХНІЧНЕ ЗАВДАННЯ", 1)
    add_body_p(doc, 
        "Мета роботи: Опанувати методи практичної інтеграції хмарних картографічних сервісів, потокового відео та аудіо, "
        "метеорологічних та фінансових інформерів, а також плагінів соціальних мереж у структуру сучасного вебсайту. "
        "Забезпечити кросбраузерну сумісність, повну адаптивність вбудованих компонентів та збереження високого рівня вебдоступності й продуктивності.")

    add_body_p(doc, "Завдання дослідження та практичної розробки:", "Основні завдання: ")
    tasks = [
        "1. Інтегрувати картографічну службу Google Maps на сайт ChargeUA з локацією головного хабу біля кафедри САПР (м. Львів, вул. С. Бандери, 12) та прокладеним маршрутом.",
        "2. Додати панорамний віртуальний огляд місцевості за допомогою технології Google Street View 360° для полегшення орієнтації водіїв електромобілів.",
        "3. Реалізувати інтеграцію навчального відео через YouTube з використанням оптимізаційних параметрів (rel=0, modestbranding=1, loading=\"lazy\").",
        "4. Впровадити відео через альтернативну платформу Vimeo та здійснити порівняльний інженерний аналіз (бітрейт, Clean UI, навантаження на клієнта).",
        "5. Розмістити нативне аудіо стандартного елемента HTML5 <audio> із мультиформатною підтримкою (MP3, WAV) та звуковим асистентом старту зарядки.",
        "6. Розробити та інтегрувати блок інформерів реального часу: погода Sinoptik.ua, валютний курс НБУ, синхронізований годинник Time.is та плагіни соцмереж (Telegram, Facebook, Instagram).",
        "7. Забезпечити адаптивність для всіх вбудованих об'єктів за допомогою сучасного CSS-правила aspect-ratio: 16/9 та провести кросбраузерне тестування."
    ]
    for t in tasks:
        add_body_p(doc, t, space_after=2)

    # ---------------- РОЗДІЛ 1: ПОКРОКОВИЙ ХІД РОБОТИ ----------------
    add_header_styled(doc, "РОЗДІЛ 1. ПОКРОКОВИЙ ХІД ВИКОНАННЯ РОБОТИ", 1)

    add_header_styled(doc, "Етап 1. Архітектурна підготовка та підключення базових сервісів", 2)
    add_body_p(doc, 
        "Створено структуру проєкту 'lab-06-external-services' з директоріями assets/ (audio, icons, images), css/ та js/. "
        "У секції <head> підключено нормалізований шрифт Google Fonts Inter з підтримкою розширеної кирилиці та CDN-бібліотеку Font Awesome 6.5.2 "
        "для векторних піктограм сервісів. У верхній частині документа розгорнуто інформаційний бар .top-informer-bar, "
        "який демонструє статус мережі, поточну температуру у Львові, валютні котирування та мережевий час.")
    add_screenshot_figure(doc, "lab6_01_hero_informer.png", 1, "Головний екран платформи ChargeUA із верхнім інформаційним баром та студентським бейджем")

    add_header_styled(doc, "Етап 2. Інтеграція Google Maps із позначенням кафедри САПР", 2)
    add_body_p(doc, 
        "Відповідно до п. 1 порядку роботи на офіційній сторінці дисципліни, виконано інтеграцію карти Google Maps "
        "із прив'язкою до навчального корпусу №5 НУ «Львівська політехніка» (кафедра САПР, координати 49.8362° N, 24.0085° E). "
        "Карта оформлена всередині інтерактивної картки .map-card із заголовком хабу, бейджами статусу портів (4 порти вільні, 160 кВт), "
        "а також прямою кнопкою швидкої навігації для застосунків на смартфонах.")
    add_screenshot_figure(doc, "lab6_02_google_maps.png", 2, "Інтерактивна Google Maps із локацією швидкісного хабу біля кафедри САПР")

    add_header_styled(doc, "Етап 3. Інтеграція кругової панорами Google Street View 360°", 2)
    add_body_p(doc, 
        "Згідно з п. 2 порядку роботи впроваджено віртуальний сферичний огляд місцевості вулиці Степана Бандери біля Політехніки. "
        "Використано iframe з параметром 6m8!1m7!1s... для відтворення фотопанорами високої роздільної здатності. "
        "Користувач має змогу обертати кут зору на 360 градусів по горизонталі та вертикалі, оцінюючи якість під'їзних шляхів та паркувальні місця.")
    add_screenshot_figure(doc, "lab6_03_street_view.png", 3, "Віртуальний сферичний тур Google Street View 360° на під'їзді до хабу")

    add_header_styled(doc, "Етап 4 та 5. Порівняльне вбудовування відеоплеєрів: YouTube та Vimeo", 2)
    add_body_p(doc, 
        "Відповідно до пп. 3 і 5 порядку роботи, на сторінці розміщено порівняльну 2-колонкову сітку .video-grid. "
        "Перша картка містить відеоінструкцію користування швидкісною станцією з безпечного хостингу youtube-nocookie.com, "
        "де відключено зайві cookie-трекери, заблоковано сторонні рекомендовані відео (rel=0) та ввімкнено ліниве завантаження loading=\"lazy\". "
        "Друга картка містить відеопрезентацію з платформою Vimeo через player.vimeo.com із параметрами чистого інтерфейсу (?title=0&byline=0).")
    add_screenshot_figure(doc, "lab6_04_youtube_vimeo.png", 4, "Порівняльне розміщення відеосервісів YouTube та Vimeo в адаптивних картках")

    add_header_styled(doc, "Етап 6. Впровадження нативного аудіоплеєра стандарту HTML5", 2)
    add_body_p(doc, 
        "Згідно з п. 4 порядку роботи реалізовано відтворення аудіо за допомогою тегу <audio controls preload=\"metadata\">. "
        "Створено та підключено реальний звуковий файл голосового супроводу зарядного процесу у двох форматах: MP3 (320 kbps) та WAV (PCM 16-bit). "
        "Аудіоплеєр поміщено у брендовану картку .audio-card із градієнтною іконкою гучномовця та технічними метаданими кодеків.")
    add_screenshot_figure(doc, "lab6_05_audio_player.png", 5, "Нативний HTML5 аудіоплеєр із мультиформатним резервуванням джерел")

    add_header_styled(doc, "Етап 7. Інформери реального часу та соціальні кнопки", 2)
    add_body_p(doc, 
        "Відповідно до п. 6 порядку роботи збудовано інформаційний хаб із 4 віджетів: "
        "1) Метеорологічний інформер Sinoptik.ua із відображенням температури (+14°C) та оцінкою оптимальності для літій-іонних батарей; "
        "2) Валютний інформер котирувань НБУ (USD, EUR, PLN) для розрахунку роумінгових платежів; "
        "3) Синхронізований годинник точного часу (Time.is) із відображенням переходу на нічний пільговий тариф; "
        "4) Кнопки соціального шерингу в Telegram, Facebook та посилання на офіційний Instagram-профіль кафедри САПР.")
    add_screenshot_figure(doc, "lab6_06_widgets_social.png", 6, "Інформери Sinoptik, курсів валют НБУ, годинника Time.is та плагінів соцмереж")

    add_header_styled(doc, "Етап 8. Кросбраузерна валідація, адаптивність та футер", 2)
    add_body_p(doc, 
        "Виконано тестування в браузерах Chromium (Google Chrome, Edge) та Gecko (Mozilla Firefox). "
        "Завдяки медіа-запитам @media (max-width: 768px) блокова модель автоматично трансформується з багатоколонкових сіток "
        "в одноколонковий вертикальний стек, а меню згортається в сенсорний гамбургер з доступністю за ARIA-атрибутами.")
    add_screenshot_figure(doc, "lab6_07_footer_testing.png", 7, "Блок валідації та семантичний футер сайту з авторськими відомостями")
    add_screenshot_figure(doc, "lab6_09_mobile_view.png", 8, "Мобільний рендеринг сторінки у в'юпорті 390px (Chrome DevTools)")
    add_screenshot_figure(doc, "lab6_08_full_page.png", 9, "Повний панорамний вигляд зверстаної вебсторінки ChargeUA ЛР №6")

    # ---------------- РОЗДІЛ 2: АНАТОМІЯ КОДУ ----------------
    add_header_styled(doc, "РОЗДІЛ 2. АНАТОМІЯ КЛЮЧОВИХ СЕМАНТИЧНИХ КОНСТРУКЦІЙ", 1)
    add_body_p(doc, "Нижче наведено технічний розбір ключових блоків розмітки та стилів, реалізованих у роботі:")

    add_code_callout(doc, 
'''<!-- Адаптивне вбудовування Google Maps із захисними атрибутами -->
<div class="responsive-map-wrapper">
  <iframe 
    title="Google Maps локація кафедри САПР Львівської політехніки"
    src="https://www.google.com/maps/embed?pb=..." 
    width="100%" 
    height="450" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade">
  </iframe>
</div>''', "Лістинг 1. Структура вбудовування карти Google Maps:")

    add_code_callout(doc,
'''/* Сучасна адаптивність медіа без застарілих padding-bottom хаків */
.responsive-video-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background-color: #000;
  border-radius: var(--radius-md);
  overflow: hidden;
}
.responsive-video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}''', "Лістинг 2. CSS-правило aspect-ratio для відеофреймів 16:9:")

    add_code_callout(doc,
'''<!-- Нативний плеєр з мультиформатним фолбеком -->
<audio controls preload="metadata" class="native-audio-player">
  <source src="assets/audio/chargeua_assistant.mp3" type="audio/mpeg">
  <source src="assets/audio/chargeua_assistant.wav" type="audio/wav">
  Ваш браузер не підтримує елемент аудіо стандарту HTML5.
</audio>''', "Лістинг 3. Розмітка мультиформатного аудіоплеєра:")

    # ---------------- РОЗДІЛ 3: ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ ----------------
    add_header_styled(doc, "РОЗДІЛ 3. ВІДПОВІДІ НА ВСІ 10 КОНТРОЛЬНИХ ЗАПИТАНЬ", 1)
    add_body_p(doc, 
        "Відповіді підготовлено згідно з офіційним планом кафедри САПР за адресою: "
        "https://www.victoria.lviv.ua/library/students/wd/work6.html. "
        "Кожна відповідь містить лаконічну змістовну частину, академічне теоретичне обґрунтування та реалізацію в ChargeUA.")

    # Питання 1
    add_qa_card(doc, 1,
        "Які існують способи підключення карт на вебсторінку, та які переваги й недоліки кожного (API vs Iframe)?",
        "Основні способи: статичне зображення, вбудовування через <iframe> та програмне підключення через JavaScript Maps API.",
        "Вбудовування через <iframe> є найпростішим і не вимагає платного API-ключа. Воно ізольоване в окремому sandbox-контексті, "
        "що гарантує безпеку та нульовий ризик конфліктів JS. Проте воно має фіксовану функціональність без можливості динамічного "
        "маніпулювання маркерами з коду сторінки. На противагу, Maps JavaScript API надає повний програмний контроль: додавання сотень "
        "кластеризованих точок зарядки, кастомізацію векторних шарів та реакцію на події кліка, але вимагає реєстрації білінгу Google Cloud.",
        '''<iframe src="https://www.google.com/maps/embed?pb=..." loading="lazy"></iframe>'''
    )

    # Питання 2
    add_qa_card(doc, 2,
        "Які параметри передаються в URL-запиті Google Maps для налаштування координат, масштабу та мови інтерфейсу?",
        "Параметри pb=!1m... кодують матрицю проєкції: географічну широту, довготу, рівень масштабування (zoom), ідентифікатор точки та мовний код (hl=uk).",
        "У сучасному протоколі вбудовування Google Maps Embed API використовується структурований серіалізований рядок protobuf (префікс pb). "
        "У ньому !1d та !2d визначають географічні координати (довготу та широту), !3d — радіус охоплення сцени, !2s — мову інтерфейсу підписів (uk для української), "
        "а !5m2 — регіональні налаштування локалі.",
        '''https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2573.32!2d24.0084!3d49.8362!...!2suk!2sua'''
    )

    # Питання 3
    add_qa_card(doc, 3,
        "У чому полягають особливості використання сферичних панорам Google Street View (інтеграція та обмеження ліцензії)?",
        "Street View надає повноцінне 360-градусне занурення з фотографій реальної місцевості; вимагає суворого дотримання ліцензії Google та атрибуції авторських прав.",
        "Панорама формується зі зшитих екіректангулярних знімків високої роздільної здатності. Інтеграція здійснюється передачею унікального "
        "ідентифікатора панорами (panoId) або координат локації з параметрами фокусу (pitch/heading/fov). Згідно з Google Maps Platform Terms of Service, "
        "забороняється кешувати тайли знімків на власному сервері, приховувати логотип Google чи використовувати знімки для гео-навчання сторонніх нейромереж.",
        '''<iframe src="https://www.google.com/maps/embed?pb=!4v...!6m8!1m7!1sCAoSLEFGMVFpcE...!2m2!1d49.8359!2d24.0142!3f240!4f0"></iframe>'''
    )

    # Питання 4
    add_qa_card(doc, 4,
        "Порівняйте методи вставляння відео: нативний тег <video> проти спеціалізованих платформ (YouTube, Vimeo).",
        "Нативний <video> забезпечує повний контроль над дизайном і нульову сторонню аналітику, але навантажує власний сервер трафіком. YouTube/Vimeo надають безкоштовний CDN, адаптивний бітрейт та глобальну сумісність.",
        "Використання нативного <video> змушує власника самостійно кодувати відео у формати MP4 (H.264), WebM (VP9) та AV1, а також сплачувати "
        "за гігабайти пропускної здатності хостингу при масових переглядах. YouTube та Vimeo використовують адаптивне потокове передавання (HLS / MPEG-DASH), "
        "миттєво підлаштовуючи якість картинки від 360p до 4K під швидкість інтернету клієнта.",
        '''<!-- YouTube Iframe vs Native Video -->
<iframe src="https://www.youtube-nocookie.com/embed/S_8qM8QJpEU?rel=0" allowfullscreen></iframe>'''
    )

    # Питання 5
    add_qa_card(doc, 5,
        "Яке призначення атрибутів безпеки та оптимізації для <iframe> (allow, allowfullscreen, loading=\"lazy\", sandbox)?",
        "Вони регулюють права доступу до апаратних функцій клієнта (мікрофон, повний екран), захищають від XSS та запобігають блокуванню рендерингу сторінки.",
        "Атрибут loading=\"lazy\" відкладає завантаження важкого вмісту фрейму до моменту, поки користувач не наблизиться до нього при скролі (економія до 80% трафіку). "
        "Атрибут allow декларує Feature Policy (акселерометр, гіроскоп, автоплей). Атрибут sandbox створює строгий ізольований контекст, блокуючи "
        "виконання небезпечних сценаріїв, спливаючих вікон (popups) та доступ до cookie головного вікна.",
        '''<iframe src="..." loading="lazy" allow="accelerometer; encrypted-media" allowfullscreen sandbox="allow-scripts allow-same-origin"></iframe>'''
    )

    # Питання 6
    add_qa_card(doc, 6,
        "Яка підтримка аудіоформатів (MP3, WAV, OGG, AAC) у сучасних браузерах, та навіщо використовувати множинні джерела <source>?",
        "MP3 підтримується 100% браузерів; WAV забезпечує найвищу якість без стиснення; використання кількох <source> гарантує резервування на випадок відсутності кодека.",
        "Браузер опитує теги <source> зверху вниз за списком і бере перший файл, чий MIME-тип (type=\"audio/mpeg\") він підтримує. "
        "Це забезпечує повний фолбек: сучасні браузери відтворюють стиснений оптимальний MP3 або AAC, а системні аудіошини можуть використовувати прямий нестиснений WAV.",
        '''<audio controls preload="metadata">
  <source src="assets/audio/chargeua.mp3" type="audio/mpeg">
  <source src="assets/audio/chargeua.wav" type="audio/wav">
  Ваш браузер не підтримує аудіо HTML5.
</audio>'''
    )

    # Питання 7
    add_qa_card(doc, 7,
        "Як забезпечити коректну адаптивність вбудованих медіаелементів за допомогою CSS (aspect-ratio vs Padding-Bottom Hack)?",
        "Сучасний стандарт: CSS-властивість aspect-ratio: 16 / 9; застарілий метод: відносний контейнер із відсотковим padding-bottom: 56.25%.",
        "Застарілий hack спирався на специфікацію CSS 2.1, де вертикальний padding у відсотках розраховувався від ширини батьківського блоку (9/16 = 56.25%). "
        "Він вимагав двох вкладених тегів і абсолютного позиціонування iframe. Сучасна властивість aspect-ratio: 16 / 9 (CSS Box Sizing Level 4) "
        "нативно резервує геометрію блоку ще до завантаження зовнішнього контенту, запобігаючи стрибкам макета (Cumulative Layout Shift, CLS).",
        '''.responsive-video-wrapper {
  width: 100%;
  aspect-ratio: 16 / 9;
}'''
    )

    # Питання 8
    add_qa_card(doc, 8,
        "У чому різниця між синхронним, async та defer завантаженням скриптів сторонніх інформерів (погода, валюта, час)?",
        "Синхронне завантаження повністю блокує парсинг HTML; async завантажує скрипт у фоні та виконує негайно після завантаження; defer зберігає чергу виконання після повного парсингу DOM.",
        "Для незалежних інформерів (як-от віджет курсу валют або лічильник аналітики) оптимальним є async, оскільки він завантажується паралельно "
        "і не затримує відображення інтерфейсу. Для модулів, що взаємодіють із DOM-деревом після його готовності (наприклад, годинник, що шукає елемент #clock-display), "
        "слід використовувати defer, або викликати оновлення в події DOMContentLoaded.",
        '''<script src="https://informer.sinoptik.ua/widget.js" async></script>
<script src="js/currency-calculator.js" defer></script>'''
    )

    # Питання 9
    add_qa_card(doc, 9,
        "Як функціонують кнопки та плагіни соціальних мереж, та яку роль відіграє протокол Open Graph (OG-теги)?",
        "Кнопки генерують прямі URL-запити до інтерфейсу шерингу; Open Graph розмітка передає заголовок, опис і банер сайту для створення привабливої прев'ю-картки.",
        "Прямий шеринг через Intent URL (t.me/share/url, facebook.com/sharer) не вимагає завантаження важких SDK і трекерів від соцмереж. "
        "Коли користувач натискає посилання, бот соцмережі відвідує сторінку сайту і зчитує мета-теги стандарту Open Graph (<meta property=\"og:title\">, "
        "og:description, og:image), формуючи багату інформаційну прев'ю-картку в чаті чи стрічці новин.",
        '''<meta property="og:title" content="ChargeUA — Швидкісні зарядні станції">
<meta property="og:image" content="https://chargeua.ua/assets/images/og-preview.jpg">
<a href="https://t.me/share/url?url=https://chargeua.ua&text=Заряджайся">Telegram</a>'''
    )

    # Питання 10
    add_qa_card(doc, 10,
        "Які проблеми продуктивності та захисту приватності виникають при використанні сторонніх віджетів, і як їх мінімізувати (GDPR, трекери)?",
        "Проблеми: блокування основного потоку виконання JS (Third-Party Blocking Time), затримка TBT/LCP та витік персональних даних клієнтів (IP-адреса, User-Agent) без їхньої згоди.",
        "Для дотримання міжнародного регламенту GDPR необхідно забороняти встановлення аналітичних і рекламних cookie до моменту явної згоди "
        "відвідувача в Cookie-банері. Для оптимізації слід використовувати youtube-nocookie.com, застосовувати rel=\"noopener noreferrer\" "
        "для зовнішніх лінків (захист від викрадення вікна window.opener) та фасадні прев'ю-картинки (Facade pattern), які завантажують важкий iframe лише після кліка користувача.",
        '''<a href="..." target="_blank" rel="noopener noreferrer">Зовнішній сервіс</a>
<iframe src="https://www.youtube-nocookie.com/embed/..." loading="lazy"></iframe>'''
    )

    # ---------------- РОЗДІЛ 4: ВИСНОВКИ ----------------
    add_header_styled(doc, "РОЗДІЛ 4. ВИСНОВКИ", 1)
    conclusions = [
        "1. У ході виконання Лабораторної роботи №6 здобуто практичний досвід комплексної інтеграції хмарних та зовнішніх вебсервісів у вебплатформу ChargeUA.",
        "2. Успішно впроваджено інтерактивну карту Google Maps із прив'язкою до навчального корпусу кафедри САПР Львівської політехніки (вул. С. Бандери, 12), прокладанням маршруту навігації та 360-градусною сферичною панорамою Google Street View.",
        "3. Проведено інженерне порівняння медіаплатформ YouTube та Vimeo: підтверджено переваги YouTube для масового навчання водіїв (CDN Google, адаптивний бітрейт, субтитри) та Vimeo для презентаційного Clean UI без реклами.",
        "4. Реалізовано апаратний HTML5 аудіоплеєр з підтримкою резервування форматів (MP3 320 kbps та безстиснений PCM WAV), інтегрований у фірмову картку звукового супроводу старту зарядної сесії.",
        "5. Розроблено та адаптовано 4 функціональні інформери (метеорологічний Sinoptik.ua, валютні котирування НБУ, синхронізований мережевий годинник Time.is та соціальні плагіни з відкритим шерингом), забезпечивши високу швидкість завантаження сторінки та нульовий ризик витоку конфіденційних даних клієнтів."
    ]
    for c in conclusions:
        add_body_p(doc, c)

    # Збереження файлу
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
    build_complete_lab6_document()
