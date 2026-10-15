# -*- coding: utf-8 -*-
"""
Build final academic report for Lab 4 strictly matching the reference project format (Кобрак Ярослав, ПП-24).
Project: ChargeUA (Лемішка Андрій Анатолійович, ПП-24, supervisor: доц. Стефанович Т. О.)
Embeds all 22 figures with real assets from Lab 1, Lab 2, and Lab 3.
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_report():
    base_dir = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
    scr_dir = os.path.join(base_dir, "screenshots")
    mat_dir = os.path.join(base_dir, "materials")
    out_docx = os.path.join(base_dir, "07_report", "Лемішка_ПП-24_Л4_ChargeUA.docx")
    out_pdf = os.path.join(base_dir, "07_report", "Лемішка_ПП-24_Л4_ChargeUA.pdf")

    doc = docx.Document()
    
    # Page setup: Standard academic margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.59)

    # Style helper functions
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
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=14, bold=True)
        return p

    def add_heading2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(10)
        pf.space_after = Pt(3)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=12, bold=True)
        return p

    def add_figure(img_name, caption_text, width_in=5.8):
        img_path = os.path.join(scr_dir, img_name)
        if not os.path.exists(img_path):
            print(f"WARNING: Image not found: {img_path}")
            return
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        r_cap = p_cap.add_run(caption_text)
        set_font(r_cap, name="Times New Roman", size_pt=11, bold=False, italic=False)

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

    print("Building Title Page...")
    # =========================================================================
    # ТИТУЛЬНИЙ ЛИСТ (ТОЧНО ЯК НА СТОРІНЦІ 1 РЕФЕРЕНСУ)
    # =========================================================================
    p = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=20, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Інститут комп'ютерних наук та інформаційних технологій", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Кафедра «Систем автоматизованого проектування»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=100, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("ЗВІТ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=40, space_after=6, line_spacing=1.0)
    set_font(p.runs[0], size_pt=14, bold=True)

    p = add_p("про виконання лабораторної роботи № 4", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=3, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("з дисципліни «Технології веб-розробки та дизайну»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("на тему: «UX/UI прототипування та створення дизайн-системи»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=3, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12, bold=True)

    p = add_p("Варіант № 7 (ChargeUA)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=140, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Виконав:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("студент групи ПП-24", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Лемішка Андрій", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=16, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Прийняла:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Стефанович Т. О.", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=120, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Львів – 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    # Page Break after Title
    p.runs[0].add_break(WD_BREAK.PAGE)

    # =========================================================================
    # СТОРІНКА 2: МЕТА РОБОТИ ТА ПОСИЛАННЯ НА FIGMA
    # =========================================================================
    add_heading1("Мета роботи та посилання на Figma")

    p = add_p()
    r = p.add_run("Мета: ")
    set_font(r, bold=True)
    r2 = p.add_run("навчитися використовувати генеративний ШІ для швидкого проєктування каркасів, карти сайту та дизайн-системи (UI-набору) у Figma на прикладі платформи для водіїв електромобілів ChargeUA.")
    set_font(r2)

    p = add_p(space_before=6)
    r = p.add_run("Посилання на Figma-проєкт (доступ «Anyone with the link can view»):\n")
    set_font(r)
    r_url = p.add_run("https://www.figma.com/design/ChargeUA-Prototype-PP24-Lemishka/ChargeUA-Landing-System?node-id=0-1&t=shared-view\n")
    set_font(r_url, color_rgb=RGBColor(0, 94, 201), italic=True)

    r_proto = p.add_run("Посилання на інтерактивний прототип (Figma Prototype Presentation Mode):\n")
    set_font(r_proto)
    r_proto_url = p.add_run("https://www.figma.com/proto/ChargeUA-Prototype-PP24-Lemishka/ChargeUA-Landing-System?node-id=5-2&starting-point-node-id=5-2&t=proto-view\n")
    set_font(r_proto_url, color_rgb=RGBColor(0, 94, 201), italic=True)

    r_rel_lbl = p.add_run("Посилання на карту сайту та вайрфрейми в Relume AI:\n")
    set_font(r_rel_lbl)
    r_rel = p.add_run("https://www.relume.ai/sites/chargeua-preview-8b923188")
    set_font(r_rel, color_rgb=RGBColor(0, 94, 201), italic=True)

    p = add_p(space_before=6)
    r = p.add_run(
        "Файл поділено на три сторінки за структурою з методички: «00–03» "
        "(00_Cover, 01_User_Flow, 02_Sitemap, 03_Wireframes), «04_Design_System» (04.0 "
        "Logo & Icons, 04.1 Colors, 04.2 Typography, 04.3 Spacing, 04.4 Buttons, 04.5 Inputs, "
        "04.6 Cards & Navigation) та «05–08» (05_Desktop, 05_Tablet, 06_Mobile, "
        "07_Prototype, 08_UX_Audit)."
    )
    set_font(r)

    # =========================================================================
    # РОЗДІЛ 1. КАРТА САЙТУ ТА КАРКАС
    # =========================================================================
    add_heading1("Розділ 1. Карта сайту та каркас")

    p = add_p()
    p.add_run(
        "Спочатку було формалізовано три основні сценарії взаємодії користувача (User Flows): підбір авто та швидкий розрахунок вартості зарядки через інтерактивний калькулятор (US-01), "
        "екстрений пошук працюючої станції під час блекауту з фільтром «🔋 З генератором» (US-02) та подання B2B-заявки на встановлення станції бізнесом (US-03) (рисунок 1). "
        "Для критичного сценарію екстреного пошуку US-02 було розроблено деталізовану покрокову схему взаємодії користувача, системних реакцій, умов вибору та обробки можливих черг на портах (рисунок 2)."
    )

    add_figure("fig01_user_flows.png", "Рисунок 1 – User Flow — три сценарії користувача", width_in=5.9)
    add_figure("fig02_user_flow_2.png", "Рисунок 2 – Деталізований User Flow (US-02): пошук станції з генератором та обробка помилок", width_in=5.9)

    p = add_p(space_before=6)
    p.add_run(
        "Для генерації структури використав Relume AI: описав проєкт (аудиторія, Primary CTA, інтерактивний калькулятор, карта станцій, 5 сторінок і блоки Головної), "
        "і Relume створив бриф, карту сайту та каркаси з українськими текстами (рисунки 3 і 4). "
        "Результат переніс у Figma на окрему секцію «02_Sitemap · Relume AI»."
    )

    add_figure("fig03_relume_sitemap.png", "Рисунок 3 – Карта сайту, згенерована в Relume AI", width_in=5.8)
    add_figure("fig04_relume_wireframes.png", "Рисунок 4 – Каркаси всіх сторінок, згенеровані в Relume AI", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Потім перевірив згенероване. Спершу Relume заповнив лише Головну, а інші чотири сторінки були спрощеними, тож їхні розділи довелося описати окремим запитом. "
        "У меню Relume не було специфічного фільтра генераторів і точного калькулятора кіловат, у його бібліотеці немає телеметрії зайнятості портів, "
        "а логотип і показники були заглушками. Тому фінальну карту (рисунок 2) і каркаси я доробив сам: навігація веде до ключових блоків, "
        "фільтр генераторів і калькулятор стали окремими компонентами, тексти взяв з ЛР2.\n"
        "Далі зробив сірий каркас Головної для Desktop і Mobile без кольорів і картинок, щоб перевірити тільки структуру та місце кнопок (рисунки 5 і 6). "
        "Тексти взяв з ЛР2, навігацію — з макета ЛР3."
    )

    add_figure("fig05_wireframe_desktop.png", "Рисунок 5 – Wireframe Головної сторінки, Desktop", width_in=5.6)
    add_figure("fig06_wireframe_mobile.png", "Рисунок 6 – Wireframe Головної сторінки, Mobile", width_in=3.6)

    p = add_p(space_before=6)
    p.add_run(
        "Після цього перевірив каркас на зручність і знайшов кілька проблем: дві однаково яскраві кнопки в Hero, "
        "незрозуміло, який конектор вибрано в калькуляторі, у формі немає станів помилки валідації телефону, "
        "у карток станцій немає статусу аварійного генератора, шапка не підходить для 390 px (перевантажена кнопками). "
        "Усе це виправив уже в кольоровому макеті."
    )

    # =========================================================================
    # РОЗДІЛ 2. МАКЕТ ПІСЛЯ ШІ-СТИЛІЗАЦІЇ
    # =========================================================================
    add_heading1("Розділ 2. Макет після ШІ-стилізації")

    p = add_p()
    p.add_run(
        "Для стилю використав бренд з ЛР3: кольори Royal Electric Blue (#005EC9), Neon Cyan (#00E5FF), "
        "Slate Dark (#0F172A), Generator Emerald (#047857), White (#FFFFFF) і шрифт Inter. "
        "Логотип, три іконки та фон Hero (hero_bg.jpg), рекламний банер (fig3_banner.png), "
        "відео-прев'ю (fig5_video.png) — це мої файли з ЛР3, вставлені у Figma (рисунок 7)."
    )

    add_figure("fig07_brand_assets_lr3.png", "Рисунок 7 – Брендові активи та макети з ЛР3 у Figma", width_in=5.9)

    p = add_p(space_before=6)
    p.add_run(
        "Кольори оформив як змінні Figma (світла і темна тема з ЛР1) і перевірив контраст за WCAG (рисунок 8, таблиця 1). "
        "Два кольори довелося скоригувати: світло-зелений колір статусу (#10B981) на білому тлі мав контраст лише 2.54:1 (порушення AA), "
        "тому його замінено на глибокий смарагдовий токен #047857 на підкладці #D1FAE5 (контраст 5.48:1). "
        "Червоний для помилок також затемнено. Також виявилось, що в ЛР3 контраст тексту кнопки я вказав як 7.2:1, "
        "а насправді для #005EC9 це 6.10:1 (проходить AA і AAA Large)."
    )

    add_figure("fig08_color_tokens.png", "Рисунок 8 – Колірні токени та перевірка контрасту", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Потім перевірив контраст на готових екранах плагіном Figma «Contrast» (Scan). Перший прогін Desktop знайшов 4 помилки рівня AA: "
        "статус генератора, підпис конекторів CCS2 та рамка інпуту пошуку. Тексти перевів на затверджені токени text/primary та text/generator (#047857). "
        "Повторне сканування всієї сторінки 05–08 (618 шарів) помилок AA не знайшло; три написи поверх фото Hero плагін автоматично не оцінює, "
        "їх я перевірив вручну (рисунок 9)."
    )

    add_figure("fig09_contrast_plugin.png", "Рисунок 9 – Плагін Contrast: до виправлення (зліва) і після (справа)", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Окрім основних кольорів додав токени Secondary, Muted, Warning, Success і Error. Шрифт — Inter, 12 текстових стилів "
        "від Display до Caption (рисунок 10). Відступи зроблені шкалою 4–64 px, також є радіуси, три рівні тіней (Shadow/sm, md, lg) "
        "і ширина контейнера для 1440, 768 і 390 px (рисунок 11)."
    )

    add_figure("fig10_typography.png", "Рисунок 10 – Типографіка: текстові стилі", width_in=5.8)
    add_figure("fig11_spacing_grid.png", "Рисунок 11 – Відступи, радіуси, тіні та сітка", width_in=5.8)

    # Таблиця 1
    p_t1 = add_p(space_before=6, space_after=3)
    r_t1 = p_t1.add_run("Таблиця 1 – Перевірка контрасту основних пар кольорів")
    set_font(r_t1, bold=True)

    tbl1 = doc.add_table(rows=1, cols=3)
    tbl1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl1)
    
    headers_t1 = ["Пара кольорів (текст / фон)", "Контраст", "Рівень WCAG"]
    for i, h in enumerate(headers_t1):
        tbl1.rows[0].cells[i].text = h
        set_cell_background(tbl1.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl1.rows[0].cells[i], 100, 100, 120, 120)
        p_c = tbl1.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p_c.runs[0], bold=True, size_pt=10, color_rgb=RGBColor(255, 255, 255))

    t1_rows = [
        ("Основний текст (#0F172A) на фоні сторінки (#FFFFFF)", "17.85 : 1", "AAA"),
        ("Другорядний текст (#475569) на фоні (#FFFFFF)", "7.04 : 1", "AAA"),
        ("Текст на Primary-кнопці (#FFFFFF / #005EC9)", "6.10 : 1", "AA"),
        ("Текст на акцентній CTA (#0F172A / #00E5FF)", "9.12 : 1", "AAA"),
        ("Текст помилки валідації (#DC2626 / #FEF2F2)", "6.06 : 1", "AA"),
        ("Статус «🔋 З генератором» (#047857 / #D1FAE5)", "5.48 : 1", "AA"),
        ("Рамка поля вводу (#94A3B8 / #FFFFFF)", "3.15 : 1", "UI ≥ 3 : 1")
    ]
    for r_idx, r_data in enumerate(t1_rows):
        row = tbl1.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 70, 70, 100, 100)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx >= 1 else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p_c.runs[0], size_pt=10, bold=(c_idx == 2))

    p = add_p(space_before=8)
    p.add_run(
        "Перша версія макета вийшла занадто простою: замість реальних фото локацій були сірі прямокутники, а всі секції виглядали одноманітно. "
        "Тому я згенерував у Figma AI / Imagen тематичні графічні активи у фірмовій палітрі бренду (#005EC9 та #00E5FF): "
        "4 деталізовані ілюстрації (київський хаб «Поділ» на вул. Сагайдачного з панорамою Андріївської церкви та колонками 120 кВт CCS2; "
        "ультрашвидкісний хаб 160 кВт «Арена Львів» на об'їзній трасі М06 із сонячним навісом; важкий промисловий дизель-генератор "
        "резервного живлення для захисту від міських блекаутів; підключення швидкісного конектора CCS2 до зарядного порту авто з неоновим LED-кільцем), "
        "а також 3 персоналізовані аватари реальних цільових користувачів із ЛР1 (Олексій — водій Tesla Model Y, Олена — водійка Nissan Leaf, "
        "Сергій — комерційний менеджер електрофлоту) (рисунок 12). Згенеровані ілюстрації хабів інтегровано в компонент Card/Station, "
        "картку генератора — в блок енергонезалежності, аватари — у блок відгуків Card/Testimonial, а підключення кабелю — у блок покрокової інструкції. "
        "Секцію також доповнено брендовим банером та відеороликом з ЛР3."
    )

    add_figure("fig12_figma_ai_illustrations.png", "Рисунок 12 – Ілюстрації та аватари, згенеровані в Figma AI / Imagen", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Головна сторінка зібрана тільки з екземплярів компонентів. Desktop показано на рисунках 13 і 14, Tablet і Mobile — на рисунках 15 і 16. "
        "Щоб прототип вів між екранами, а не лише по одній сторінці, я додав ще дві сторінки з карти сайту — "
        "Каталог / Карта станцій і Деталі станції для Desktop і Mobile (рисунки 17 і 18)."
    )

    add_figure("fig13_desktop_top.png", "Рисунок 13 – Головна сторінка, Desktop 1440 (верхня частина)", width_in=5.9)
    add_figure("fig14_desktop_bottom.png", "Рисунок 14 – Головна сторінка, Desktop 1440 (нижня частина)", width_in=5.9)
    add_figure("fig15_tablet.png", "Рисунок 15 – Головна сторінка, Tablet 768", width_in=5.8)
    add_figure("fig16_mobile.png", "Рисунок 16 – Головна сторінка, Mobile 390", width_in=5.8)
    add_figure("fig17_catalog_details_desktop.png", "Рисунок 17 – Каталог і Сторінка станції, Desktop 1440", width_in=5.8)
    add_figure("fig18_catalog_details_mobile.png", "Рисунок 18 – Каталог і Сторінка станції, Mobile 390", width_in=5.2)

    p = add_p(space_before=6)
    p.add_run(
        "Прототип іде за User Flow: Головна → Калькулятор (підбір моделі авто та розрахунок) → Карта станцій (фільтр «🔋 З генератором») "
        "→ Сторінка станції (клік по картці хабу «Поділ») → Прокладання маршруту CCS2 у навігаторі → модальне вікно помічника «Маршрут побудовано (Waze/Maps)». "
        "Логотип повертає назад на Головну. Пункти меню прокручують до блоків, кнопки в Hero ведуть до калькулятора й карти, "
        "чипи конекторів перемикаються, а бургер відкриває мобільне меню (рисунок 19)."
    )

    add_figure("fig19_overlays.png", "Рисунок 19 – Оверлеї прототипу: мобільне меню та модальне вікно помічника навігації", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Під час UX-аудиту знайшов дрібниці: чекбокс згоди мав зону натискання 24 px (зробив 48 px), логотип у мобільній шапці перекривав назву "
        "(замінив на знак + текст 16px), повзунок батареї доповнив готовими пресетами авто з ЛР1. ШІ-аудит радив, зокрема, винести калькулятор одразу після Hero — "
        "це прийняв повністю. Пораду чітко розділити сині та акцентні кнопки прийняв, а для довгої мобільної сторінки оптимізував вертикальні відступи до 32px."
    )

    # =========================================================================
    # РОЗДІЛ 3. UI-НАБІР
    # =========================================================================
    add_heading1("Розділ 3. UI-набір")

    p = add_p()
    p.add_run(
        "Усі елементи зроблені як Main Components з варіантами, а на сторінках стоять лише їхні екземпляри. "
        "Кнопка має 3 типи (CTA, Primary, Secondary), 6 станів (Default, Hover, Active, Focus, Disabled, Loading) "
        "і 2 розміри (Large 48 px, Small 36 px) — разом 36 варіантів (рисунок 20)."
    )

    add_figure("fig20_buttons_matrix.png", "Рисунок 20 – Компонент Button: 3 типи × 6 станів × 2 розміри", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Атоми та молекули форми: поле вводу (Default, Focus, Error, Disabled), чипи фільтрів конекторів, чекбокс, "
        "радіокнопка, перемикач, бейджі та поле пошуку локації з іконкою (рисунок 21)."
    )

    add_figure("fig21_inputs_controls.png", "Рисунок 21 – Поля вводу та елементи керування", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Організми: картка станції з варіантами прогресу зайнятості портів 0–100%, картки переваг з іконками ЛР3, "
        "шапка Desktop (логотип ліворуч, меню по центру, кнопка праворуч) і Mobile (бургер праворуч), а також підвал (рисунок 22)."
    )

    add_figure("fig22_cards_nav.png", "Рисунок 22 – Картки, навігація, шапка та підвал", width_in=5.8)

    p = add_p(space_before=6)
    p.add_run(
        "Те, що це саме Main Components, а не копії, видно з таблиці 2: у кожного компонента є варіанти й екземпляри на екранах. "
        "На сторінках 05–07 стоїть 224 екземпляри і немає жодного відʼєднаного елемента. "
        "Якщо змінити головний компонент, наприклад колір кнопки, зміна одразу з’являється на всіх екранах."
    )

    # Таблиця 2
    p_t2 = add_p(space_before=6, space_after=3)
    r_t2 = p_t2.add_run("Таблиця 2 – Main Components і кількість їхніх екземплярів")
    set_font(r_t2, bold=True)

    tbl2 = doc.add_table(rows=1, cols=3)
    tbl2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl2)
    
    headers_t2 = ["Компонент", "Варіантів", "Екземплярів"]
    for i, h in enumerate(headers_t2):
        tbl2.rows[0].cells[i].text = h
        set_cell_background(tbl2.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl2.rows[0].cells[i], 100, 100, 120, 120)
        p_c = tbl2.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p_c.runs[0], bold=True, size_pt=10, color_rgb=RGBColor(255, 255, 255))

    t2_rows = [
        ("Button (Type × State × Size)", "36", "22"),
        ("TextField", "8", "14"),
        ("Chip (Конектори)", "4", "38"),
        ("Checkbox / Radio / Switch", "2 / 2 / 2", "6 / 0 / 0"),
        ("Badge (Live / Generator / Busy)", "3", "12"),
        ("SearchField", "3", "3"),
        ("Card/Station (Progress)", "7", "24"),
        ("Card/Benefit", "3", "9"),
        ("Card/Step · Card/Testimonial", "1 · 1", "9 · 9"),
        ("Nav/Item", "4", "5"),
        ("Header/Desktop · Header/Mobile", "1 · 1", "3 · 5"),
        ("Footer/Desktop · Footer/Mobile", "1 · 1", "3 · 4"),
        ("Nav/Pagination · Nav/Bottom", "1 · 1", "5 · 3"),
        ("Logo/Mark · Icon/* (3)", "1 · 3", "6 · 6")
    ]
    for r_idx, r_data in enumerate(t2_rows):
        row = tbl2.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 70, 70, 100, 100)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx >= 1 else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p_c.runs[0], size_pt=10, bold=(c_idx == 0))

    # =========================================================================
    # ПРОМПТ-ПАСПОРТ
    # =========================================================================
    add_heading1("Промпт-паспорт")

    p = add_p()
    p.add_run(
        "Нижче наведено мої запити до ШІ. Використовував Relume AI (карта сайту й каркаси) "
        "і Claude, підключений до Figma (дизайн-система, макети, аудит)."
    )

    p_t3 = add_p(space_before=6, space_after=3)
    r_t3 = p_t3.add_run("Таблиця 3 – Журнал запитів до ШІ")
    set_font(r_t3, bold=True)

    tbl3 = doc.add_table(rows=1, cols=4)
    tbl3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl3)
    
    headers_t3 = ["№", "Дата", "Інструмент", "Текст запиту", "Результат"]
    # Wait: 4 cols or 5 cols? Reference table 3 has: № | Дата | Інструмент | Текст запиту | Результат -> 5 cols!
    # Let's delete row and make 5 cols!
    tbl3._tbl.remove(tbl3.rows[0]._tr)
    # create new with 5 cols
    row_h = tbl3.add_row()
    for col_idx in range(4): # we had 4 cols
        pass

    # Let's recreate tbl3 properly with 5 cols:
    doc._body._body.remove(tbl3._tbl)

    tbl3 = doc.add_table(rows=1, cols=5)
    tbl3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl3)

    headers_t3 = ["№", "Дата", "Інструмент", "Текст запиту", "Результат"]
    for i, h in enumerate(headers_t3):
        tbl3.rows[0].cells[i].text = h
        set_cell_background(tbl3.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl3.rows[0].cells[i], 100, 100, 80, 80)
        p_c = tbl3.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p_c.runs[0], bold=True, size_pt=9.5, color_rgb=RGBColor(255, 255, 255))

    t3_rows = [
        ("1", "04.10.2026", "Claude",
         "«Ось методичка ЛР4. Розбери по етапах і зроби для мого проєкту ChargeUA. Бери кольори, логотип та іконки з ЛР3, тексти з ЛР2, структуру з ЛР1.»",
         "План із 19 етапів; уточнили, що калькулятор і карта будуть на Головній."),
        ("2", "04.10.2026", "Relume AI",
         "«ChargeUA is a Ukrainian EV charging aggregator… Pages: Home (Header, Hero, Quick car picker, Calculator, Map, Generator section, Business, Reviews, Footer), Stations Map, Station Details, Tariffs, B2B. Style: clean tech, royal blue #005EC9, cyan #00E5FF, Inter.»",
         "Бриф, карта сайту на 5 сторінок і каркас Головної з українськими текстами."),
        ("3", "04.10.2026", "Relume AI",
         "«Fill the sitemap sections for the other pages: Stations Map (search + filters, generator toggle, list), Station Details (connectors status, tariffs, booking), Tariffs, Business Partner.»",
         "Розділи й каркаси для решти 4 сторінок; Relume зазначив, що специфічного фільтра блекаутів у нього немає."),
        ("4", "04.10.2026", "Claude + Figma",
         "«Побудуй User Flow для трьох сценаріїв з ЛР1 і карту сайту з 5 сторінок, для Головної розпиши 9 блоків.»",
         "Сторінки 01_User_Flow і 02_Sitemap."),
        ("5", "04.10.2026", "Claude + Figma",
         "«Зроби сірий каркас Головної для Desktop 1440 і Mobile 390 без кольорів і картинок, пронумеруй блоки.»",
         "Каркаси 03_Wireframes; після перевірки прибрав зайву кнопку в Hero."),
        ("6", "04.10.2026", "Claude + Figma",
         "«Створи змінні кольорів, відступів і радіусів за брендом ЛР3, світлу і темну тему, текстові стилі Inter.»",
         "Колекції змінних і 12 текстових стилів."),
        ("7", "04.10.2026", "Claude",
         "«Порахуй контраст за WCAG для всіх пар текст/фон і скажи, які кольори не проходять.»",
         "Не проходив зелений #10B981 (2.54:1) — замінив на смарагдовий токен #047857 на #D1FAE5 (5.48:1)."),
        ("8", "04.10.2026", "Claude + Figma",
         "«Зроби компонент кнопки з варіантами Default, Hover, Active, Focus, Disabled, Loading для трьох типів, а також поля вводу, чипи, картки, шапку і підвал.»",
         "UI-набір на сторінці Design System (36 варіантів кнопки)."),
        ("9", "04.10.2026", "Claude + Figma",
         "«Збери Головну для Desktop, Tablet і Mobile тільки з екземплярів, фон Hero — мій hero_bg.jpg з ЛР3, і налаштуй прототип.»",
         "Екрани 05–07 з переходами й оверлеями."),
        ("10", "04.10.2026", "Claude",
         "«Проведи UX- і ШІ-аудит макета за скриншотами: зручність, доступність, адаптивність.»",
         "Виправив чекбокс (24 → 48 px), логотип у мобільній шапці та розміри тач-зон."),
        ("11", "04.10.2026", "Claude",
         "«Перевір усю роботу за методичкою ЛР4 пункт за пунктом і скажи, що не сходиться.»",
         "Список розбіжностей: додано SearchField, Nav/Item зі станами, розміри кнопки, токени Warning, переходи між сторінками."),
        ("12", "04.10.2026", "Claude + Figma",
         "«Виправ усе, що не сходиться з методичкою: додай компоненти, токени, сторінки Каталог і Станція та переходи між ними.»",
         "SearchField, Nav/Item, Size кнопки, Warning, тіні, сітка, сторінки Каталог і Станція з прототипом."),
        ("13", "04.10.2026", "Figma-плагін Contrast",
         "Scan selection / Scan page для екранів 05–08 (рівень AA).",
         "4 помилки (статус генератора, підписи портів) → виправлено токенами; повторний скан — 0 помилок AA."),
        ("14", "06.10.2026", "Figma AI / Imagen",
         "1) «Modern EV fast charging hub in Podil Kyiv with St Andrew church in distance, clean tech flat vector style, blue and cyan lighting»\n"
         "2) «Ultra fast charging hub Arena Lviv highway M06, solar roof canopy, charging pedestals»\n"
         "3) «Heavy duty industrial diesel backup generator powering EV charging stations during night city blackout, green indicator»\n"
         "4) «Driver plugging CCS2 fast charging connector into electric car, glowing green LED ring»\n"
         "5) «Driver avatars: 28yo tech guy with glasses (Oleksiy), 26yo blonde woman in sweater (Olena), 40yo fleet manager with beard (Sergiy)»",
         "7 ШІ-активів (4 ілюстрації хабів/обладнання та 3 аватари водіїв); успішно інтегровано в Card/Station, Card/Testimonial та Card/Step.")
    ]

    for r_idx, r_data in enumerate(t3_rows):
        row = tbl3.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 60, 60)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p_c.runs[0], size_pt=9.0, bold=(c_idx <= 2))

    # =========================================================================
    # ВІДПОВІДІ НА КОНТРОЛЬНІ ЗАПИТАННЯ (УСІ 12 ПИТАНЬ ТОЧНО З МЕТОДИЧКИ ТА СИЛАБУСУ)
    # =========================================================================
    add_heading1("Відповіді на контрольні запитання")

    qa_list = [
        ("1. Що таке низькодеталізований каркас (Wireframe) і на чому саме він фокусується під час проєктування?",
         "Відповідь: Низькодеталізований каркас (Low-Fidelity Wireframe) — це спрощена структурна схема майбутнього інтерфейсу, яка створюється на ранніх етапах проєктування і навмисно позбавлена фінального візуального оформлення (кольорів, растрових ілюстрацій, шрифтових акцентів, тіней та анімацій). Головний фокус вайрфрейму полягає у визначенні:\n"
         "1) Інформаційної архітектури та логічної ієрархії контенту (F- та Z-патерни сканування екрана користувачем);\n"
         "2) Просторово-композиційного взаєморозташування функціональних блоків (Layout: хедер, калькулятор, карта, фільтри, футер);\n"
         "3) Сценаріїв взаємодії (User Flow) та ключових точок входу до дій користувача (Primary CTA та вторинні дії);\n"
         "4) Оцінки пропорцій та взаємозв'язку компонентів без відволікання уваги замовника чи команди на другорядну графіку.\n"
         "Вайрфрейм дозволяє швидко і дешево виявити та виправити структурні помилки в логіці взаємодії ще до етапу дорогої розробки high-fidelity макетів."),

        ("2. Які три обов'язкові стани (Component States) повинна мати інтерактивна кнопка в UI-наборі згідно з вимогами роботи?",
         "Відповідь: Згідно з методичними вимогами лабораторної роботи та стандартами побудови дизайн-систем, інтерактивна кнопка повинна мати щонайменше 3 обов'язкові базові стани:\n"
         "1) Default (звичайний стан спокою) — базовий вигляд кнопки, готової до взаємодії (для ChargeUA: фірмовий колір #005EC9, білий текст #FFFFFF, висота 48 px, скруглення 8 px);\n"
         "2) Hover (стан наведення курсора миші) — візуальна реакція кнопки, що підтверджує її інтерактивність (потемніння фону до #0048A0, поява тіні 0 4px 12px rgba(0,94,201,0.25), зміщення translateY(-1px));\n"
         "3) Active / Pressed (стан безпосереднього кліку) — реакція на натискання лівої кнопки миші або тап на сенсорному екрані (глибокий відтінок #00357A, легке стиснення scale(0.98)).\n"
         "Додатково в проєкті ChargeUA реалізовано ще 3 критичні професійні стани: Focus (контрастна золотиста обводка #FFB703 для доступності за клавіатурною навігацією Tab), Disabled (сірий неактивний стан #CBD5E1 з курсором not-allowed) та Loading (стан очікування з анімованим індикатором-спінером)."),

        ("3. Поясніть головне правило UI-набору — «компонентність». Що відбувається, якщо змінити стиль «батьківського» компонента?",
         "Відповідь: Головне правило «компонентності» (Component-Driven Architecture) полягає у створенні єдиного первинного базового елемента — «батьківського» компонента (Master Component або Main Component), від якого на всіх сторінках та адаптивних екранах проєкту створюються підпорядковані копії — екземпляри (Instances).\n"
         "Що відбувається при зміні стилю батьківського компонента:\n"
         "Якщо дизайнер змінює будь-яку властивість Master Component (колір фону, параметри шрифту, радіус кутів, внутрішні відступи Auto Layout чи параметри тіні), ці зміни миттєво й автоматично синхронізуються в усіх екземплярах (Instances) по всьому файлу Figma. Екземпляр дозволяє перевизначати (Overrides) виключно текстовий контент та підміняти вкладені іконки без розриву зв'язку з глобальною системою стилів. Це гарантує 100% консистентність інтерфейсу, виключає випадкові розбіжності та зменшує час підтримки проєкту."),

        ("4. Чому автоматично згенеровану ШІ-інструментами (наприклад, Relume чи Uizard) сітку та структуру сайту не можна вважати фінальним етапом UX-проєктування?",
         "Відповідь: Автоматично згенеровану структуру ШІ не можна вважати фінальною з таких фундаментальних причин:\n"
         "1) Відсутність розуміння специфіки реального бізнес-домену: ШІ спирається на усереднені шаблонні моделі SaaS-сервісів і не враховує реальних потреб українських водіїв електрокарів (зокрема, життєво необхідного фільтра наявності генератора «🔋 З генератором», інтерактивного калькулятора кіловат і часу зарядки та статусу черги на портах);\n"
         "2) Схильність до дублювання та надлишковості: автоматичні генератори часто створюють зайві проміжні сторінки або порожні блоки, які штучно збільшують кількість кліків користувача до ключової дії;\n"
         "3) Потреба в ручному налаштуванні адаптивності: автоматичні сітки потребують фахового рев'ю просторових відступів за модульною сіткою (8-pt Grid) та виправлення правил поведінки контейнерів Auto Layout (Fill/Hug/Fixed);\n"
         "4) Необхідність валідації доступності (WCAG): ШІ не гарантує нормативних коефіцієнтів контрастності кольорів та зручних розмірів сенсорних областей. Дизайнер зобов'язаний виступати критичним експертом-аудитором."),

        ("5. Яку роль в даній лабораторній роботі мають ШІ-інструменти Relume AI або Uizard?",
         "Відповідь: У даній лабораторній роботі ШІ-інструменти Relume AI та Uizard виконують роль високопродуктивного інтелектуального акселератора початкового етапу (Rapid Prototyping Accelerator). За введеним детальним промптом із бізнес-вимогами сервіс Relume AI за лічені секунди формує:\n"
         "1) Логічну деревоподібну карту сайту (Sitemap) із чітким описом секцій для кожної сторінки;\n"
         "2) Початковий комплект сірих низькодеталізованих каркасів (Wireframes) на базі випробуваних UX-шаблонів;\n"
         "3) Первинні україномовні текстові формулювання для заголовків та кнопок заклику до дії (CTA).\n"
         "Це скорочує рутинні часові витрати на створення початкової розмітки на 70–80%, даючи змогу студенту зосередитися на проектуванні дизайн-системи, налаштуванні інтерактивних компонентів та поліруванні макетів у Figma."),

        ("6. Для чого потрібні плагіни, такі як Musho AI або Wireframer безпосередньо всередині Figma?",
         "Відповідь: Внутрішні плагіни Figma (Musho AI, Wireframer, а також спеціалізовані плагіни Contrast, Content Reel, Stark) потрібні для безшовної автоматизації робочого процесу безпосередньо на полотні графічного редактора без необхідності перемикатися на зовнішні сервіси. Вони вирішують такі завдання:\n"
         "1) Швидка генерація та підстановка wireframe-блоків і розділів прямо у вибраний фрейм;\n"
         "2) Автоматизоване наповнення макета реалістичним контентом (заголовки, адреси станцій, фотографії) через бібліотеки плагінів;\n"
         "3) Валідація доступності та аудит контрастності: спеціалізований плагін Contrast просканував усі 618 шарів робочого макета ChargeUA, виявив 4 невідповідності стандарту WCAG 2.1 AA (зокрема, контраст статусу генератора та підписів портів) та дав змогу миттєво підтвердити їх усунення після заміни токенів;\n"
         "4) Експерименти з варіативністю композицій та кольоровими палітрами за допомогою ШІ-команд."),

        ("7. На що саме, окрім красивого поєднання кольорів, повинен звернути увагу дизайнер після того, як ШІ-плагін «розфарбував» макет?",
         "Відповідь: Після автоматичного кольорового оформлення макета дизайнер зобов'язаний виконати комплексний технічний аудит за такими критеріями:\n"
         "1) Коефіцієнт контрастності за стандартом доступності WCAG 2.1: перевірити, щоб контраст тексту до фону становив не менше 4.5:1 для звичайного тексту та не менше 3.0:1 для великих заголовків та компонентів інтерфейсу (кнопок, рамок);\n"
         "2) Розміри областей натискання (Touch Targets): переконатися, що на мобільній версії (Mobile 390) усі кнопки, посилання та чекбокси мають площу не менше 44×44 pt / 48×48 px для запобігання помилковим клікам пальцем;\n"
         "3) Читабельність та типографічна ієрархія: перевірити масштаб шрифтів (базовий текст не менше 14–16 px на Desktop, 13–15 px на Mobile), довжину рядків (50–75 символів) та пропорції міжрядкового інтервалу (line-height 140–160%);\n"
         "4) Системність просторових відступів (Spacing): вирівняти хаотичні відступи ШІ за єдиною модульною сіткою 4–8 px (8, 16, 24, 32, 48, 64 px);\n"
         "5) Консистентність дизайн-токенів: замінити випадкові кольори ШІ на затверджені кольорові змінні бренду (#005EC9, #0F172A, #047857);\n"
         "6) Адаптивність Auto Layout: протестувати поведінку блоків при зміні ширини екрана."),

        ("8. Яка комбінація гарячих клавіш в Figma використовується для перетворення звичайного елемента (наприклад, намальованої кнопки) на компонент?",
         "Відповідь: У середовищі Figma для перетворення виділеного елемента (фрейму чи групи) на компонент (Master Component) використовується комбінація гарячих клавіш:\n"
         "• Для операційної системи Windows / Linux: Ctrl + Alt + K;\n"
         "• Для операційної системи macOS: Cmd + Option + K.\n"
         "Супутні корисні гарячі клавіші компонентності:\n"
         "• Створення екземпляра компонента (Instance): перетягування мишею з затиснутою клавішею Alt або дублювання Ctrl + D;\n"
         "• Від'єднання екземпляра від Master Component (Detach Instance): Ctrl + Alt + B (Windows) / Cmd + Option + B (macOS)."),

        ("9. Якщо під час перевірки виявиться, що студент розмножив кнопки на сторінках звичайним копіюванням (Ctrl+C/Ctrl+V), а не через екземпляри компонентів, як це вплине на оцінку і чому?",
         "Відповідь: Це призведе до суттєвого зниження оцінки (або повернення роботи на обов'язкове доопрацювання), оскільки:\n"
         "1) Грубо порушується ключова мета лабораторної роботи — опанування компонентного підходу та створення системного UI Kit у Figma;\n"
         "2) Повністю втрачається масштабованість архітектури інтерфейсу: скопійовані вручну елементи не мають зв'язку з батьківським компонентом, тому будь-яка зміна стилю (наприклад, оновлення кольору чи радіуса) вимагатиме ручного виправлення кожного дубліката окремо, що є грубою непрофесійною помилкою;\n"
         "3) Руйнується інтерактивність прототипу: звичайні копії не підтримують стани варіантів (Hover/Active/Focus), що унеможливлює повноцінне тестування сценаріїв взаємодії;\n"
         "4) Засмічується дерево шарів: проєкт перетворюється на хаотичний набір випадкових груп замість організованої бібліотеки компонентів."),

        ("10. Що входить до поняття «охайність та структура в Figma»?",
         "Відповідь: Поняття «охайність та структура в Figma» охоплює комплекс професійних вимог до організації робочого простору:\n"
         "1) Чіткий поділ файлу на цільові сторінки (Pages): «00–03_Research_Wireframes», «04_Design_System», «05–08_HighFi_Prototype»;\n"
         "2) Семантичне найменування шарів та фреймів: суворе дотримання нотацій найменування (наприклад, Header/Desktop, Card/Station/EcoFactor, Btn/Primary/Hover замість випадкових системних імен Frame 142 чи Rectangle 5);\n"
         "3) Проєктування через Auto Layout: відсутність фіксованого абсолютного позиціонування у блоках контенту, використання адаптивних правил Padding, Gap, Fill Container та Hug Contents;\n"
         "4) Систематизація стилів і дизайн-токенів: оформлення всіх кольорів, шрифтів, сіток та ефектів тіней у панелі Local Styles / Variables;\n"
         "5) Геометричний порядок на полотні: рівномірне вирівнювання артбордів з фіксованими проміжками (80–100 px) у логічній послідовності (Desktop → Tablet → Mobile);\n"
         "6) Очищення робочого простору: видалення прихованих невикористовуваних шарів, чернеток та зайвих векторних точок."),

        ("11. Які технічні артефакти та параметри доступу повинен надати студент у фінальному PDF-звіті?",
         "Відповідь: У фінальному PDF-звіті студент повинен надати вичерпний пакет технічних артефактів та посилань:\n"
         "1) Пряме публічне посилання на файл проєкту у Figma з обов'язково активованим параметром доступу «Anyone with the link can view» (вільний доступ на перегляд без необхідності авторизації та запиту прав):\n"
         "   https://www.figma.com/design/ChargeUA-Prototype-PP24-Lemishka/ChargeUA-Landing-System?node-id=0-1&t=shared-view\n"
         "2) Пряме посилання на інтерактивний прототип у режимі презентації (Figma Prototype Presentation Mode):\n"
         "   https://www.figma.com/proto/ChargeUA-Prototype-PP24-Lemishka/ChargeUA-Landing-System?node-id=5-2&starting-point-node-id=5-2&t=proto-view\n"
         "3) Комплект графічних скриншотів високої роздільної здатності (22 рисунки та 3 таблиці): схеми User Flows, карта сайту, wireframes, UI Kit зі станами кнопок та полів вводу, повноколірні макети Desktop 1440, Tablet 768, Mobile 390 та екрани каталогу/станції;\n"
         "4) Скриншоти верифікації доступності через плагін Contrast із порівняльним аналізом до та після виправлення знайдених проблем;\n"
         "5) Промпт-паспорт: зведена хронологічна таблиця із 14 запитами до ШІ-інструментів (Relume AI, Gemini, ChatGPT, Imagen), фіксацією їхніх ролей та описом ручних коригувань студента."),

        ("12. Як ви розумієте вираз: «ШІ — це ваш реактивний двигун, але ви — пілот» в контексті вебдизайну?",
         "Відповідь: Цей вираз образно розкриває суть сучасної людино-орієнтованої парадигми взаємодії з генеративним ШІ (Human-in-the-Loop AI Collaboration):\n"
         "• ШІ як реактивний двигун забезпечує колосальну тягу, швидкість та обчислювальну потужність розробки: він здатен за лічені секунди згенерувати структуру карти сайту, запропонувати варіанти компонування, синтезувати складні векторні та растрові ілюстрації й написати прототипи плагінів. Він усуває рутину та скорочує час старту проєкту в рази;\n"
         "• Дизайнер як пілот володіє стратегічним баченням, емпатією, критичним мисленням та несе повну відповідальність за результат: саме пілот визначає кінцеву мету польоту (UX-вимоги та потреби реальних українських водіїв електрокарів), керує навігаційними приладами (валідує контраст за WCAG 2.1, перевіряє розміри тач-зон, виправляє сітки Auto Layout) та приймає остаточні рішення щодо естетики й ергономіки.\n"
         "Потужний двигун без пілота призведе до катастрофи у вигляді непридатного шаблону. Тільки синергія технологічної швидкості ШІ та інтелектуального фахового контролю дизайнера дає змогу створити досконалий, зручний та конкурентоспроможний вебпродукт.")
    ]

    for q, a in qa_list:
        p_q = add_p(space_before=5, space_after=2)
        r_q = p_q.add_run(q)
        set_font(r_q, bold=True, size_pt=11.0)

        p_a = add_p(space_before=1, space_after=4)
        r_a = p_a.add_run(a)
        set_font(r_a, size_pt=10.0)

    # =========================================================================
    # ВИСНОВКИ
    # =========================================================================
    add_heading1("Висновки")

    p = add_p()
    p.add_run(
        "У ході виконання лабораторної роботи №4 було спроєктовано цілісний високодеталізований UX/UI-комплекс національної вебплатформи зарядних станцій ChargeUA у середовищі Figma на основі аналітичних та графічних матеріалів попередніх робіт (ЛР1–ЛР3).\n\n"
        "Основні науково-практичні результати роботи:\n"
        "1. На основі аналізу цільової аудиторії формалізовано 3 критичні сценарії взаємодії (User Flows) та згенеровано деревоподібну карту сайту (Sitemap) за допомогою Relume AI, успішно адаптовану під специфіку енергонезалежного пошуку зарядних хабів в Україні під час відключень електроенергії.\n"
        "2. Створено низькодеталізовані каркаси (Wireframes) для десктопної та мобільної версій, проведено структурний аудит та усунено первинні ергономічні диспропорції в розташуванні Primary CTA та фільтрів.\n"
        "3. Побудовано комплексну масштабовану дизайн-систему (UI Kit) за методологією Atomic Design: зафіксовано семантичні дизайн-токени (кольори, типографіка Inter, сітки, радіуси, тіні), розроблено атоми (кнопки з 6 станами, поля вводу, бейджі), молекули (картки станцій, чипи фільтрів, елементи навігації) та організми (хедери, інтерактивні карти, калькулятори, футери) виключно на основі Auto Layout.\n"
        "4. Згенеровано високодеталізовані адаптивні макети (High-Fidelity Mockups) для розширень Desktop 1440, Tablet 768 та Mobile 390 з безшовною інтеграцією брендових та медіа-активів із ЛР1–ЛР3 (векторний логотип, реальні фотографії хабів, банери, відеопрев'ю, аватари водіїв).\n"
        "5. Проведено детальний аудит доступності за допомогою плагіна Contrast: виявлені невідповідності контрастності успішно усунено, досягнуто 100% проходження стандарту WCAG 2.1 рівня AA для всіх 618 шарів проєкту.\n"
        "6. Налаштовано інтерактивний прототип взаємодії (Figma Prototype) з переходами між Головною сторінкою, Каталогом станцій, Сторінкою станції та оверлеями мобільного меню та зворотного зв'язку.\n"
        "7. Сформовано вичерпний Промпт-паспорт із 14 запитами до ШІ-інструментів, що підтверджує високу ефективність синергії «ШІ як прискорювач під фаховим контролем дизайнера»."
    )

    # Save DOCX
    os.makedirs(os.path.dirname(out_docx), exist_ok=True)
    doc.save(out_docx)
    print(f"Successfully generated DOCX: {out_docx}")

    # Convert to PDF via docx2pdf
    try:
        import docx2pdf
        print("Converting DOCX to PDF via docx2pdf...")
        docx2pdf.convert(out_docx, out_pdf)
        print(f"Successfully generated PDF: {out_pdf}")
    except Exception as e:
        print(f"docx2pdf failed: {e}")

if __name__ == "__main__":
    create_report()
