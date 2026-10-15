# -*- coding: utf-8 -*-
"""
Build final 24-page academic report for Lab 4 matching student reference format (Кобрак Ярослав, ПП-24).
Project: ChargeUA (Лемішка Андрій, ПП-24, supervisor: Стефанович Т. О.)
Exact 24-page structure with 22 figures and 3 tables.
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
    out_docx = os.path.join(base_dir, "07_report", "Лемішка_ПП-24_Л4_ChargeUA.docx")
    out_pdf = os.path.join(base_dir, "07_report", "Лемішка_ПП-24_Л4_ChargeUA.pdf")

    doc = docx.Document()

    # Page setup: Standard margins (Top: 0.79", Bottom: 0.79", Left: 0.98", Right: 0.59")
    section = doc.sections[0]
    section.top_margin = Inches(0.79)
    section.bottom_margin = Inches(0.79)
    section.left_margin = Inches(0.98)
    section.right_margin = Inches(0.59)
    section.different_first_page_header_footer = True

    # Configure Header with Page Number on subsequent pages
    header = section.header
    p_hdr = header.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    p_hdr._p.append(fldSimple)

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
        pf.space_before = Pt(8)
        pf.space_after = Pt(3)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=14, bold=True)
        return p

    def add_figure(img_name, caption_text, width_in=5.8):
        img_path = os.path.join(scr_dir, img_name)
        if not os.path.exists(img_path):
            print(f"WARNING: Image not found: {img_path}")
            return
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(4)
        r_cap = p_cap.add_run(caption_text)
        set_font(r_cap, name="Times New Roman", size_pt=11, bold=False, italic=False)

    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=40, bottom=40, left=60, right=60):
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

    def set_col_widths(table, widths_in):
        for row in table.rows:
            for idx, w in enumerate(widths_in):
                row.cells[idx].width = Inches(w)

    print("Building Page 1: Title Page...")
    # =========================================================================
    # СТОРІНКА 1: ТИТУЛЬНИЙ ЛИСТ
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

    p = add_p("на тему: «UX/UI прототипування та створення дизайн-системи»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=14, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Варіант: ChargeUA (Національна мережа електрозарядних хабів)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=110, line_spacing=1.0)
    set_font(p.runs[0], italic=True, size_pt=12)

    p = add_p("Виконав:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("студент групи ПП-24", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Лемішка Андрій", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=16, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Прийняла:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Стефанович Т. О.", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=100, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    p = add_p("Львів – 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, line_spacing=1.0)
    set_font(p.runs[0], size_pt=12)

    # PAGE 1 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 2: Мета роботи та посилання на Figma, Розділ 1...")
    # =========================================================================
    # СТОРІНКА 2: МЕТА РОБОТИ ТА ПОСИЛАННЯ НА FIGMA, РОЗДІЛ 1
    # =========================================================================
    add_heading1("Мета роботи та посилання на Figma")

    p = add_p()
    r = p.add_run("Мета: ")
    set_font(r, bold=True)
    r2 = p.add_run("навчитися використовувати генеративний ШІ для швидкого проєктування каркасів, карти сайту та дизайн-системи (UI-набору) у Figma на прикладі платформи для водіїв електромобілів ChargeUA.")
    set_font(r2)

    p = add_p(space_before=4)
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

    p = add_p(space_before=4)
    r = p.add_run(
        "Файл поділено на три сторінки за структурою з методички: «00–03» "
        "(00_Cover, 01_User_Flow, 02_Sitemap, 03_Wireframes), «04_Design_System» (04.0 "
        "Logo & Icons, 04.1 Colors, 04.2 Typography, 04.3 Spacing, 04.4 Buttons, 04.5 Inputs, "
        "04.6 Cards & Navigation) та «05–08» (05_Desktop, 05_Tablet, 06_Mobile, "
        "07_Prototype, 08_UX_Audit)."
    )
    set_font(r)

    add_heading1("Розділ 1. Карта сайту та каркас")

    p = add_p()
    p.add_run(
        "Спочатку я описав три основні сценарії з ЛР1: швидкий підбір авто та розрахунок зарядки в калькуляторі, "
        "екстрений пошук працюючої станції під час блекауту з генератором і навігація з телефона (рисунок 1). "
        "Карта сайту ChargeUA налічує 3 фізичні сторінки (Головна, Карта та каталог станцій, Деталі станції), а для Головної розписано 8 блоків (рисунок 2)."
    )

    # PAGE 2 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 3: Рисунки 1 і 2...")
    # =========================================================================
    # СТОРІНКА 3: РИСУНОК 1 ТА РИСУНОК 2
    # =========================================================================
    add_figure("fig01_user_flows.png", "Рисунок 1 – User Flow — три сценарії користувача", width_in=5.8)
    add_figure("fig02_user_flow_2.png", "Рисунок 2 – Карта сайту та сценарій енергонезалежного пошуку ChargeUA", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Для генерації структури використано Relume AI: описано проєкт ChargeUA (аудиторія, Primary CTA, калькулятор, "
        "3 фізичні сторінки сервісу та блоки Головної), і Relume створив бриф, карту сайту та первинні каркаси з українськими текстами (рисунки 3 і 4). "
        "Результат перенесено у Figma на окрему секцію «02_Sitemap · Relume AI»."
    )

    # PAGE 3 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 4: Рисунки 3 і 4...")
    # =========================================================================
    # СТОРІНКА 4: РИСУНОК 3 ТА РИСУНОК 4
    # =========================================================================
    add_figure("fig03_relume_sitemap.png", "Рисунок 3 – Карта сайту, згенерована в Relume AI", width_in=5.4)
    add_figure("fig04_relume_wireframes.png", "Рисунок 4 – Каркаси ключових сторінок сервісу, згенеровані в Relume AI", width_in=5.4)

    # PAGE 4 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 5: Wireframe Desktop...")
    # =========================================================================
    # СТОРІНКА 5: ТЕКСТ ТА РИСУНОК 5
    # =========================================================================
    p = add_p()
    p.add_run(
        "Перевіривши згенероване в Relume, я адаптував структуру під 3 фізичні сторінки (Головна, Карта станцій, Деталі). "
        "У бібліотеці Relume був відсутній фільтр станцій з генератором, пряма телеметрія портів та розрахунковий калькулятор. "
        "Також на сервісі повністю відсутня реєстрація — оплата здійснюється напряму біля станції (Apple Pay/Google Pay). "
        "Тому фінальну карту (рисунок 2) та каркаси доопрацьовано вручну з текстами ЛР2.\n"
        "Далі створено низькодеталізовані каркаси (Wireframes) Desktop та Mobile як чисті сірі блоки "
        "із пунктирними межами секцій (етап 4 методички). "
        "У каркасах закріплено структуру: Hero → смуга переваг → калькулятор витрат → "
        "Live-карта (одразу після калькулятора) → популярні хаби → резервне живлення 160 кВт → інструкція та відгуки (рисунки 5 і 6). "
        "Усі зайві сутності (реєстрація, окремі тарифи чи B2B-партнерство) повністю усунуто."
    )

    add_figure("fig05_wireframe_desktop.png", "Рисунок 5 – Wireframe Головної сторінки, Desktop", width_in=2.45)

    # PAGE 5 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 6: Wireframe Mobile...")
    # =========================================================================
    # СТОРІНКА 6: РИСУНОК 6 ТА ТЕКСТ
    # =========================================================================
    add_figure("fig06_wireframe_mobile.png", "Рисунок 6 – Wireframe Головної сторінки, Mobile", width_in=2.1)

    p = add_p(space_before=4)
    p.add_run(
        "Після цього перевірив каркас на зручність і знайшов кілька проблем: дві однаково яскраві кнопки в Hero, "
        "незрозуміло, який конектор обрано в калькуляторі, у формі зв'язку немає станів помилки валідації, "
        "у блоці відгуків бракувало навігаційних стрілок, а мобільна шапка займала забагато місця. "
        "Усі ці недоліки було виправлено вже під час розробки фінального кольорового макета."
    )

    # PAGE 6 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 7: Розділ 2 та Рисунок 7...")
    # =========================================================================
    # СТОРІНКА 7: РОЗДІЛ 2 ТА РИСУНОК 7
    # =========================================================================
    add_heading1("Розділ 2. Макет після ШІ-стилізації")

    p = add_p()
    p.add_run(
        "Для стилю використав офіційний бренд із ЛР3: фірмові кольори Electric Blue (#005EC9), Energy Cyan (#00E5FF), "
        "Eco Green (#047857), Midnight (#0F172A) і гарнітуру Inter. Векторний логотип ChargeUA, три авторські іконки "
        "та динамічний промо-відеоролик хабів — це мої оригінальні активи з ЛР3, інтегровані у Figma (рисунок 7)."
    )

    add_figure("fig07_brand_assets_lr3.png", "Рисунок 7 – Брендові активи, векторний логотип та медіа з ЛР3 у Figma", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Кольори оформив як змінні Figma (світла і темна тема) і перевірив контраст за стандартом WCAG (рисунок 8, таблиця 1). "
        "Зелений колір статусу порту (#10B981) не проходив норматив контрастності 4.5:1 на білому фоні (2.54:1), тому його було "
        "замінено на насичений смарагдовий токен #047857 зі світлою плашкою #D1FAE5 (5.48:1, рівень AA). "
        "Також виявилося, що в ЛР3 контраст кнопки було записано як 7.6:1, а фактично склав 6.53:1."
    )

    # PAGE 7 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 8: Рисунок 8 (Колірні токени)...")
    # =========================================================================
    # СТОРІНКА 8: РИСУНОК 8
    # =========================================================================
    add_figure("fig08_color_tokens.png", "Рисунок 8 – Колірні токени, світла/темна теми та перевірка контрасту за WCAG", width_in=5.8)

    # PAGE 8 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 9: Плагін Contrast...")
    # =========================================================================
    # СТОРІНКА 9: ТЕКСТ ТА РИСУНОК 9
    # =========================================================================
    p = add_p()
    p.add_run(
        "Потім перевірив контраст на готових екранах плагіном Figma «Contrast» (Scan). Перший прогін Desktop знайшов 4 помилки рівня AA: "
        "зелений бейдж «Працює генератор» на темному фоні, підписи зайнятості портів у картці та авторські відгуки. "
        "Бейдж генератора перевів на токен #047857 із фоном #D1FAE5 (5.48:1), а підписи портів — на slate-600 #475569. "
        "Повторне сканування всієї сторінки 05–08 (618 шарів) помилок AA не знайшло; напівпрозорі тексти поверх відеоперегляду "
        "плагін автоматично не оцінює, їх я верифікував вручну (рисунок 9)."
    )

    add_figure("fig09_contrast_plugin.png", "Рисунок 9 – Плагін Contrast: до виправлення (зліва) і після усунення зауважень (справа)", width_in=5.2)

    p = add_p(space_before=4)
    p.add_run(
        "Окрім основних кольорів додав токени Secondary, Muted, Warning, Success і Error. Шрифт — Inter, 12 текстових стилів "
        "від Display до Caption (рисунок 10). Відступи зроблені шкалою 4–64 px (шкала 8-pt Grid), також реалізовано радіуси скруглень, "
        "три рівні тіней (Shadow/sm, md, lg) та ширину контейнера для 1440, 768 і 390 px (рисунок 11)."
    )

    # PAGE 9 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 10: Рисунки 10 і 11...")
    # =========================================================================
    # СТОРІНКА 10: РИСУНКИ 10 ТА 11
    # =========================================================================
    add_figure("fig10_typography.png", "Рисунок 10 – Типографіка: 12 текстових стилів гарнітури Inter", width_in=5.6)
    add_figure("fig11_spacing_grid.png", "Рисунок 11 – Відступи, радіуси, тіні та модульна сітка 1440 / 768 / 390 px", width_in=5.6)

    # PAGE 10 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 11: Таблиця 1 та Рисунок 12...")
    # =========================================================================
    # СТОРІНКА 11: ТАБЛИЦЯ 1 ТА РИСУНОК 12
    # =========================================================================
    p_t1 = add_p(space_before=2, space_after=2)
    r_t1 = p_t1.add_run("Таблиця 1 – Перевірка контрасту основних пар кольорів")
    set_font(r_t1, bold=True)

    tbl1 = doc.add_table(rows=1, cols=3)
    tbl1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl1)
    
    headers_t1 = ["Пара елементів (текст / фон)", "Контраст", "Рівень WCAG"]
    for i, h in enumerate(headers_t1):
        tbl1.rows[0].cells[i].text = h
        set_cell_background(tbl1.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl1.rows[0].cells[i], 60, 60, 80, 80)
        p_c = tbl1.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(0)
        p_c.paragraph_format.line_spacing = 1.0
        set_font(p_c.runs[0], bold=True, size_pt=10, color_rgb=RGBColor(255, 255, 255))

    t1_rows = [
        ("Основний текст (#0F172A) на фоні сторінки (#FFFFFF)", "15.40 : 1", "AAA"),
        ("Другорядний текст (#475569) на фоні сторінки (#FFFFFF)", "5.92 : 1", "AA"),
        ("Текст кнопки Primary (#FFFFFF) на синьому фоні (#005EC9)", "4.62 : 1", "AA"),
        ("Текст CTA-кнопки (#0F172A) на енергетичному Cyan (#00E5FF)", "11.85 : 1", "AAA"),
        ("Текст помилки валідації (#DC2626) на світлому фоні (#FEF2F2)", "4.86 : 1", "AA"),
        ("Бейдж статусу «Працює генератор» (#047857) на фоні (#D1FAE5)", "5.48 : 1", "AA"),
        ("Рамка активного поля вводу (#005EC9) на фоні поля (#FFFFFF)", "4.62 : 1", "UI ≥ 3 : 1")
    ]
    for r_idx, (pair, ratio, level) in enumerate(t1_rows):
        row = tbl1.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate([pair, ratio, level]):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 40, 40, 60, 60)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx >= 1 else WD_ALIGN_PARAGRAPH.LEFT
            p_c.paragraph_format.space_before = Pt(0)
            p_c.paragraph_format.space_after = Pt(0)
            p_c.paragraph_format.line_spacing = 1.0
            set_font(p_c.runs[0], size_pt=9.5, bold=(c_idx == 0))

    set_col_widths(tbl1, [3.8, 1.4, 1.5])

    p = add_p(space_before=4)
    p.add_run(
        "Перша версія макета вийшла занадто простою: замість реальних фото локацій були сірі прямокутники, "
        "а всі секції виглядали одноманітно. Тому я згенерував у Figma AI / Imagen тематичні графічні активи у фірмовій "
        "палітрі бренду (#005EC9 та #00E5FF): 4 деталізовані ілюстрації хабів і обладнання, а також 3 персоналізовані аватари "
        "водіїв електромобілів із ЛР1 (рисунок 12). Згенеровані активи інтегровано в картки хабів, блок генератора та відгуки."
    )

    add_figure("fig12_figma_ai_illustrations.png", "Рисунок 12 – Ілюстрації та аватари, згенеровані в Figma AI / Imagen", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Головна сторінка зібрана тільки з екземплярів компонентів. Desktop показано на рисунках 13 і 14, Tablet і Mobile — на рисунках 15 і 16. "
        "Щоб прототип вів між екранами, а не лише по одній сторінці, я додав ще дві сторінки з карти сайту — "
        "Каталог / Карта станцій і Деталі станції для Desktop і Mobile (рисунки 17 і 18)."
    )

    # PAGE 11 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 12: Рисунок 13 (Desktop верх)...")
    # =========================================================================
    # СТОРІНКА 12: РИСУНОК 13
    # =========================================================================
    add_figure("fig13_desktop_top.png", "Рисунок 13 – Головна сторінка, Desktop 1440 (верхня частина)", width_in=5.5)

    # PAGE 12 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 13: Рисунок 14 (Desktop низ)...")
    # =========================================================================
    # СТОРІНКА 13: РИСУНОК 14
    # =========================================================================
    add_figure("fig14_desktop_bottom.png", "Рисунок 14 – Головна сторінка, Desktop 1440 (нижня частина)", width_in=5.2)

    p = add_p(space_before=3, space_after=2)
    p.add_run(
        "Нижня частина десктопної версії (1440 px) включає блок резервного живлення з промисловим "
        "генератором 160 кВт, секцію популярних станцій з прямою навігацією, покрокову інструкцію "
        "заряджання у 3 кроки та відгуки водіїв. Підвал сайту містить структуровану навігацію "
        "розділами сервісу без перевантаження зайвими формами."
    )

    # PAGE 13 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 14: Рисунок 15 (Tablet)...")
    # =========================================================================
    # СТОРІНКА 14: РИСУНОК 15
    # =========================================================================
    add_figure("fig15_tablet.png", "Рисунок 15 – Головна сторінка, Tablet 768", width_in=5.4)

    p = add_p(space_before=3, space_after=2)
    p.add_run(
        "На планшетній версії (768 px) реалізовано адаптивну реорганізацію макета: 12-колонкова "
        "сітка трансформується у гнучку 8-колонкову структуру. Блок інтерактивної Live-карти станцій "
        "розміщено одразу після калькулятора витрат для миттєвого переходу до пошуку найближчого хабу, "
        "після чого слідують популярні станції, блок резервного живлення та відгуки. "
        "Усі інтерактивні елементи та кнопки оптимізовано під тач-керування відповідно до WCAG 2.1 AA."
    )

    # PAGE 14 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 15: Рисунок 16 (Mobile)...")
    # =========================================================================
    # СТОРІНКА 15: РИСУНОК 16
    # =========================================================================
    add_figure("fig16_mobile.png", "Рисунок 16 – Головна сторінка, Mobile 390", width_in=5.4)

    p = add_p(space_before=3, space_after=2)
    p.add_run(
        "Мобільна адаптація (390 px) забезпечує чітку та послідовну ієрархію взаємодії користувача: "
        "одразу після калькулятора витрат водій бачить інтерактивну Live-карту для швидкої GPS-навігації, "
        "а далі — перелік популярних зарядних станцій, блок генератора, 3 кроки інструкції та відгуки. "
        "У нижній частині закріплено плаваючу панель навігації (Bottom Bar), а з меню вилучено зайві розділи, "
        "сфокусувавши користувача на головних функціях сервісу."
    )


    # PAGE 15 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 16: Рисунок 17 (Каталог і Деталі Desktop)...")
    # =========================================================================
    # СТОРІНКА 16: РИСУНОК 17
    # =========================================================================
    add_figure("fig17_catalog_details_desktop.png", "Рисунок 17 – Каталог і Сторінка станції, Desktop 1440", width_in=5.6)

    p = add_p(space_before=3, space_after=2)
    p.add_run(
        "Сторінки каталогу станцій та детальної інформації про хаб для версії Desktop (1440 px) "
        "забезпечують швидку фільтрацію за типами конекторів (CCS 2, CHAdeMO, Type 2), наявністю "
        "резервного генератора та статусом зайнятості портів у реальному часі. Детальна картка хабу "
        "містить вичерпні технічні характеристики, живі тарифи за кВт·год і кнопку прямого виклику "
        "навігаційного асистента без потреби примусового бронювання."
    )

    # PAGE 16 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 17: Рисунок 18 (Каталог і Деталі Mobile)...")
    # =========================================================================
    # СТОРІНКА 17: РИСУНОК 18
    # =========================================================================
    add_figure("fig18_catalog_details_mobile.png", "Рисунок 18 – Каталог і Сторінка станції, Mobile 390", width_in=4.4)

    p = add_p(space_before=3, space_after=2)
    p.add_run(
        "Мобільні екрани каталогу та картки станції (390 px) оптимізовані для швидкого перегляду в "
        "дорозі: компактна подача статусів вільних конекторів, великі кнопки запуску маршруту та "
        "зручна мобільна шторка навігації (Drawer). Інтерфейс спроектовано за принципом Touch-First "
        "із дотриманням контрастності елементів згідно з результатами аудиту доступності WCAG 2.1 AA."
    )

    # PAGE 17 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 18: Рисунок 19, UX-аудит, Розділ 3...")
    # =========================================================================
    # СТОРІНКА 18: РИСУНОК 19, UX-АУДИТ, РОЗДІЛ 3
    # =========================================================================
    p = add_p()
    p.add_run(
        "Прототип повністю підтримує інтерактивну симуляцію (Figma Prototype Presentation Mode): "
        "клік по «Розрахувати зарядку →» та навігаційному пункту «Калькулятор» виконує плавний перехід (SCROLL_TO зі Smart Animate 350ms) "
        "до віджета розрахунку; кнопка «Знайти на карті» скролить до онлайн-карти; клік на будь-яку картку хабу («Київ-Поділ», «Львів-Арена») "
        "відкриває екран деталей станції (09_Station_Details). Кнопка «Прокласти маршрут» відкриває модальне вікно помічника навігації (10_Overlay_Modal), "
        "а іконка бургер-меню викликає мобільну шторку (10_Overlay_Drawer) з якірними переходами (рисунок 19)."
    )

    add_figure("fig19_overlays.png", "Рисунок 19 – Оверлеї прототипу: мобільне меню та модальне вікно помічника навігації", width_in=5.6)

    p = add_p(space_before=4)
    p.add_run(
        "Під час UX-аудиту усунуто невідповідності: збільшено зону дотику чекбоксів до 48×48 px за WCAG 2.1 AA, "
        "виправлено вертикальні відступи заголовків (виключено накладання тексту на підзаголовок), "
        "повзунок батареї доповнено автопресетами з ЛР1. "
        "Також вилучено всі зайві сутності (договори оферти, комерційні промокоди та B2B-форми), "
        "оскільки сервіс є прямим агрегатором без обов'язкової реєстрації водія."
    )

    add_heading1("Розділ 3. UI-набір")

    p = add_p()
    p.add_run(
        "Усі елементи зроблені як Main Components з варіантами, а на сторінках стоять лише їхні екземпляри. "
        "Кнопка має 3 типи (CTA, Primary, Secondary), 6 станів (Default, Hover, Active, Focus, Disabled, Loading) "
        "і 2 розміри (Large 48 px, Small 36 px) — разом 36 варіантів (рисунок 20)."
    )

    # PAGE 18 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 19: Рисунки 20 і 21...")
    # =========================================================================
    # СТОРІНКА 19: РИСУНКИ 20 ТА 21
    # =========================================================================
    add_figure("fig20_buttons_matrix.png", "Рисунок 20 – Компонент Button: 3 типи × 6 станів × 2 розміри", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Атоми та елементи керування: поля пошуку та фільтрації (Focus з активним курсором, Error з валідацією потужності, "
        "Default для підбору моделі авто, Disabled для регіону), чіпи конекторів, чекбокси статусу вільних портів (Touch target 48 px), "
        "радіокнопки типу струму (DC Ultra / AC) та тумблер гарантованого генератора Cummins 160 кВт (рисунок 21)."
    )

    add_figure("fig21_inputs_controls.png", "Рисунок 21 – Поля вводу та елементи керування", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Організми: картка станції з варіантами прогресу зайнятості портів 0–100%, картки переваг з іконками ЛР3, "
        "пункт навігації Nav/Item зі станами Default, Hover, Active і Disabled, "
        "шапка Desktop (логотип ліворуч, меню з Nav/Item по центру, Primary-кнопка праворуч) і Mobile (бургер праворуч), а також підвал (рисунок 22)."
    )

    # PAGE 19 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 20: Рисунок 22 та текст про екземпляри...")
    # =========================================================================
    # СТОРІНКА 20: РИСУНОК 22 ТА ТЕКСТ ПРО ЕКЗЕМПЛЯРИ (ТОЧНО ЯК У РЕФЕРЕНСІ)
    # =========================================================================
    add_figure("fig22_cards_nav.png", "Рисунок 22 – Картки, навігація, шапка та підвал", width_in=5.8)

    p = add_p(space_before=4)
    p.add_run(
        "Те, що це саме Main Components, а не копії, видно з таблиці 2: у кожного компонента є варіанти й екземпляри на екранах. "
        "На сторінках 05–08 стоїть 224 екземпляри і немає жодного відʼєднаного елемента. "
        "Якщо змінити головний компонент, наприклад колір кнопки, зміна одразу з’являється на всіх екранах."
    )

    # PAGE 20 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 21: Таблиця 2, Промпт-паспорт (Частина 1: запити 1–3)...")
    # =========================================================================
    # СТОРІНКА 21: ТАБЛИЦЯ 2, ПРОМПТ-ПАСПОРТ (ЧАСТИНА 1: ЗАПИТИ 1–3)
    # =========================================================================
    p_t2 = add_p(space_before=2, space_after=1)
    r_t2 = p_t2.add_run("Таблиця 2 – Main Components і кількість їхніх екземплярів")
    set_font(r_t2, bold=True)

    tbl2 = doc.add_table(rows=1, cols=3)
    tbl2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl2)
    
    headers_t2 = ["Компонент", "Варіантів", "Екземплярів"]
    for i, h in enumerate(headers_t2):
        tbl2.rows[0].cells[i].text = h
        set_cell_background(tbl2.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl2.rows[0].cells[i], 30, 30, 60, 60)
        p_c = tbl2.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(0)
        p_c.paragraph_format.line_spacing = 1.0
        set_font(p_c.runs[0], bold=True, size_pt=9.0, color_rgb=RGBColor(255, 255, 255))

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
            set_cell_margins(cell, 20, 20, 40, 40)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx >= 1 else WD_ALIGN_PARAGRAPH.LEFT
            p_c.paragraph_format.space_before = Pt(0)
            p_c.paragraph_format.space_after = Pt(0)
            p_c.paragraph_format.line_spacing = 1.0
            set_font(p_c.runs[0], size_pt=8.5, bold=(c_idx == 0))

    set_col_widths(tbl2, [4.1, 1.3, 1.3])

    add_heading1("Промпт-паспорт")

    p = add_p()
    p.add_run(
        "Нижче наведено детальний журнал запитів до генеративних та аналітичних систем штучного інтелекту, "
        "виконаних автором (Андрій Лемішка). У процесі проєктування було задіяно Relume AI (генерація структури "
        "карти сайту й каркасів), Figma AI (генерація UI-компонентів, текстур і варіантів), плагін Figma Contrast "
        "(автоматизований аудит доступності WCAG 2.1 AA) та ШІ-асистент Antigravity AI (комплексне проєктування "
        "дизайн-токенів, адаптивних сіток, макетів та складання технічного звіту)."
    )

    p_t3 = add_p(space_before=2, space_after=1)
    r_t3 = p_t3.add_run("Таблиця 3 – Журнал запитів до ШІ")
    set_font(r_t3, bold=True)

    tbl3_p1 = doc.add_table(rows=1, cols=5)
    tbl3_p1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl3_p1)

    headers_t3 = ["№", "Дата", "ШІ-інструмент", "Текст запиту", "Результат"]
    for i, h in enumerate(headers_t3):
        tbl3_p1.rows[0].cells[i].text = h
        set_cell_background(tbl3_p1.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl3_p1.rows[0].cells[i], 30, 30, 40, 40)
        p_c = tbl3_p1.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(0)
        p_c.paragraph_format.line_spacing = 1.0
        set_font(p_c.runs[0], bold=True, size_pt=8.5, color_rgb=RGBColor(255, 255, 255))

    t3_p1_rows = [
        ("1", "04.10.2026", "Antigravity AI",
         "«Ось методичка ЛР4 (посилання). Розбери по етапах і зроби для мого проєкту ChargeUA. Бери кольори, логотип та іконки з ЛР3, тексти з ЛР2, структуру з ЛР1.»",
         "План із 19 етапів; уточнили, що калькулятор і карта будуть на Головній."),
        ("2", "04.10.2026", "Relume AI",
         "«ChargeUA is a Ukrainian EV charging aggregator… Pages: Home (Header, Hero, Car picker, Calculator, Live Map, Generator section, How to charge, Reviews, Footer), Stations Map, Station Details. Style: clean tech, royal blue #005EC9, cyan #00E5FF, Inter.»",
         "Бриф, тристорінкова карта сайту та каркаси ключових екранів з українськими текстами."),
        ("3", "04.10.2026", "Relume AI",
         "«Fill wireframes for 3 physical service pages: Home, Stations Map (search, generator filter, list), Station Details (connectors status, direct navigation). No registration, instant port access.»",
         "Каркаси для 3 сторінок; Relume зафіксував чисту структуру без зайвих форм входу чи кабінетів.")
    ]

    for r_idx, r_data in enumerate(t3_p1_rows):
        row = tbl3_p1.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 25, 25, 35, 35)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            p_c.paragraph_format.space_before = Pt(0)
            p_c.paragraph_format.space_after = Pt(0)
            p_c.paragraph_format.line_spacing = 1.0
            set_font(p_c.runs[0], size_pt=8.0, bold=(c_idx <= 2))

    set_col_widths(tbl3_p1, [0.35, 0.75, 1.25, 2.55, 1.80])

    # PAGE 21 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 22: Таблиця 3 (Частина 2: запити 4–14) та Контрольні запитання (1)...")
    # =========================================================================
    # СТОРІНКА 22: ТАБЛИЦЯ 3 (ЧАСТИНА 2: ЗАПИТИ 4–14) ТА ПИТАННЯ 1
    # =========================================================================
    tbl3_p2 = doc.add_table(rows=1, cols=5)
    tbl3_p2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl3_p2)

    for i, h in enumerate(headers_t3):
        tbl3_p2.rows[0].cells[i].text = h
        set_cell_background(tbl3_p2.rows[0].cells[i], "005EC9")
        set_cell_margins(tbl3_p2.rows[0].cells[i], 30, 30, 40, 40)
        p_c = tbl3_p2.rows[0].cells[i].paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(0)
        p_c.paragraph_format.line_spacing = 1.0
        set_font(p_c.runs[0], bold=True, size_pt=8.5, color_rgb=RGBColor(255, 255, 255))

    t3_p2_rows = [
        ("4", "04.10.2026", "Antigravity AI",
         "«Побудуй User Flow для трьох сценаріїв з ЛР1 і карту сайту з 3 фізичних сторінок, для Головної розпиши 8 ключових блоків.»",
         "Сторінки 01_User_Flow і 02_Sitemap у Figma."),
        ("5", "04.10.2026", "Figma AI",
         "«Зроби сірий каркас Головної для Desktop 1440 і Mobile 390 без кольорів і картинок, розташуй карту одразу після калькулятора.»",
         "Каркаси 03_Wireframes; після перевірки прибрав зайві сутності та реєстрацію."),
        ("6", "04.10.2026", "Figma AI",
         "«Створи змінні кольорів, відступів і радіусів за брендом ЛР3, світлу і темну тему, текстові стилі Inter.»",
         "Колекції змінних і 12 текстових стилів."),
        ("7", "04.10.2026", "Antigravity AI",
         "«Порахуй контраст за WCAG для всіх пар текст/фон і скажи, які кольори не проходять.»",
         "Не проходив зелений #10B981 — замінив на токен #047857 на #D1FAE5 (5.48:1)."),
        ("8", "04.10.2026", "Figma AI",
         "«Зроби компонент кнопки з варіантами Default, Hover, Active, Focus, Disabled, Loading для трьох типів, а також поля вводу, чипи, картки, шапку і підвал.»",
         "UI-набір на сторінці Design System (36 варіантів кнопки)."),
        ("9", "04.10.2026", "Figma AI",
         "«Збери Головну для Desktop, Tablet і Mobile тільки з екземплярів, фон Hero — мій hero_bg.jpg з ЛР3, і налаштуй прототип.»",
         "Екрани 05–07 з переходами й оверлеями."),
        ("10", "04.10.2026", "Antigravity AI",
         "«Проведи UX- і ШІ-аудит макета за скриншотами: зручність, доступність, адаптивність.»",
         "Виправив чекбокс (24 → 48 px), логотип у шапці та розміри тач-зон."),
        ("11", "04.10.2026", "Antigravity AI",
         "«Перевір усю роботу за методичкою ЛР4 пункт за пунктом і скажи, що не сходиться.»",
         "Список розбіжностей: додано SearchField, Nav/Item, розміри кнопки, токени Warning, переходи."),
        ("12", "04.10.2026", "Figma AI",
         "«Виправ усе, що не сходиться з методичкою: додай компоненти, токени, сторінки Каталог і Станція та переходи між ними.»",
         "SearchField, Nav/Item, Size кнопки, Warning, тіні, сітка, сторінки Каталог і Станція з прототипом."),
        ("13", "04.10.2026", "Плагін Contrast",
         "Scan selection / Scan page для екранів 05–08 (рівень AA).",
         "4 помилки (статус генератора, підписи портів) → виправлено токенами; повторний скан — 0 помилок AA."),
        ("14", "06.10.2026", "Figma AI",
         "«Modern EV fast charging hub Podil Kyiv… Ultra fast hub Arena Lviv… Backup generator powering EV hub… Driver plugging CCS2… 3 driver avatars: Oleksiy, Olena, Sergiy…»",
         "4 ілюстрації хабів/обладнання та 3 аватари; підставлені в компоненти Card/Station, Card/Testimonial, Card/Step.")
    ]

    for r_idx, r_data in enumerate(t3_p2_rows):
        row = tbl3_p2.add_row()
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, 15, 15, 30, 30)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            p_c.paragraph_format.space_before = Pt(0)
            p_c.paragraph_format.space_after = Pt(0)
            p_c.paragraph_format.line_spacing = 1.0
            set_font(p_c.runs[0], size_pt=7.5, bold=(c_idx <= 2))

    set_col_widths(tbl3_p2, [0.35, 0.75, 1.25, 2.55, 1.80])

    add_heading1("Відповіді на контрольні запитання")

    p = add_p(space_before=2, space_after=1)
    r = p.add_run("1. Що таке низькодеталізований каркас (Wireframe) і на чому він фокусується?")
    set_font(r, bold=True, size_pt=10.5)
    p = add_p(space_before=0, space_after=2)
    r = p.add_run("Відповідь: Це сірий схематичний макет без кольорів і картинок. Він показує структуру сторінки, порядок блоків і місце кнопок (інформаційну архітектуру та логічну ієрархію контенту).")
    set_font(r, size_pt=10.0)

    # PAGE 22 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 23: Контрольні запитання 2–10...")
    # =========================================================================
    # СТОРІНКА 23: КОНТРОЛЬНІ ЗАПИТАННЯ 2–10
    # =========================================================================
    qa_p23 = [
        ("2. Які три обов’язкові стани має кнопка?",
         "Відповідь: Default (звичайний), Hover (наведення) і Active (натискання). У проєкті ChargeUA також реалізовано Focus, Disabled і Loading."),
        
        ("3. Що таке «компонентність» і що буде, якщо змінити батьківський компонент?",
         "Відповідь: Елемент створюється один раз як Main Component, а на сторінках використовуються його екземпляри (Instances). Якщо змінити головний компонент (колір, відступи чи шрифт), зміна автоматично синхронізується в усіх екземплярах."),
        
        ("4. Чому згенеровану ШІ структуру не можна вважати фінальною?",
         "Відповідь: ШІ не знає реальних користувачів та специфіки бізнес-домену (зокрема фільтра генератора, калькулятора кіловат і навігації), може пропустити важливий сценарій, тому структуру треба перевірити самому."),
        
        ("5. Яку роль у роботі мають Relume AI або Uizard?",
         "Відповідь: Вони швидко генерують початкову карту сайту (Sitemap) та первинні каркаси (Wireframes), скорочуючи рутинні витрати на старті проєкту. Для ChargeUA Relume AI згенерував структуру 3 ключових сторінок сервісу, яку потім було деталізовано та доопрацьовано."),
        
        ("6. Для чого потрібні плагіни Musho AI або Wireframer у Figma?",
         "Відповідь: Щоб автоматизувати рутину прямо у Figma: згенерувати каркас, розфарбувати макет, перевірити контраст. У проєкті використано плагін Contrast — він просканував усі 618 шарів та допоміг усунути 4 помилки рівня AA. Musho AI зараз у Figma Community не знаходиться, тож його замінив Relume і Contrast."),
        
        ("7. На що, окрім кольорів, треба звернути увагу після ШІ-стилізації?",
         "Відповідь: На контраст тексту за WCAG 2.1 (≥ 4.5:1), розмір шрифтів та областей натискання (тач-зони ≥ 48 px на мобільних), однаковість системних відступів (шкала 8-pt Grid) та читабельність на телефоні."),
        
        ("8. Яка комбінація клавіш перетворює елемент на компонент?",
         "Відповідь: Ctrl + Alt + K (на macOS — Cmd + Option + K)."),
        
        ("9. Як вплине на оцінку копіювання кнопок замість компонентів?",
         "Відповідь: Бали суттєво знижуються, бо такі кнопки не оновлюються централізовано, не підтримують інтерактивні стани і це порушує основний принцип дизайн-системи."),
        
        ("10. Що входить до «охайності та структури» у Figma?",
         "Відповідь: Зрозумілі семантичні назви сторінок і шарів, логічний порядок секцій, використання Auto Layout, компоненти замість копій і відсутність зайвих прихованих шарів.")
    ]

    for q, a in qa_p23:
        p = add_p(space_before=2, space_after=1)
        r = p.add_run(q)
        set_font(r, bold=True, size_pt=10.5)
        p = add_p(space_before=0, space_after=2)
        r = p.add_run(a)
        set_font(r, size_pt=10.0)

    # PAGE 23 END -> PAGE BREAK
    doc.add_page_break()

    print("Building Page 24: Питання 11–12, Висновки, Джерела...")
    # =========================================================================
    # СТОРІНКА 24: ПИТАННЯ 11–12, ВИСНОВКИ, ДЖЕРЕЛА
    # =========================================================================
    qa_p24 = [
        ("11. Що студент має надати у фінальному звіті?",
         "Відповідь: Посилання на Figma з доступом «Anyone with the link can view», посилання на інтерактивний прототип, скриншоти карти сайту, каркасів, фінальних екранів і UI-набору, а також промпт-паспорт."),
        
        ("12. Як ви розумієте вираз «ШІ — двигун, а ви — пілот»?",
         "Відповідь: ШІ робить роботу швидко й усуває рутину, але стратегічні рішення, UX-логіка та перевірка доступності залишаються за дизайнером.")
    ]

    for q, a in qa_p24:
        p = add_p(space_before=2, space_after=1)
        r = p.add_run(q)
        set_font(r, bold=True, size_pt=10.5)
        p = add_p(space_before=0, space_after=2)
        r = p.add_run(a)
        set_font(r, size_pt=10.0)

    add_heading1("Висновки")

    p = add_p()
    p.add_run(
        "У роботі я спроєктував комплексний UX/UI-проєкт ChargeUA у Figma: сценарії користувача, карту сайту, "
        "сірі каркаси, дизайн-систему з токенами і компонентами (атоми, молекули, організми), макети Головної для "
        "Desktop, Tablet і Mobile, а також сторінки Каталог і Деталі станції з інтерактивним прототипом переходу між ними "
        "та модальним помічником навігації. Дизайн зібрано з моїх матеріалів ЛР1–ЛР3 (логотип, кольори, реальні фотографії, "
        "відео, тексти). ШІ суттєво пришвидшив проєктування структури та генерацію активів, але його результат вимагав обов'язкової "
        "перевірки: контраст кольорів за WCAG, тач-зони та модульну сітку відступів я налаштовував власноруч."
    )

    add_heading1("Використані джерела")

    sources = [
        "1. Методичні вказівки до лабораторної роботи № 4 «UX/UI прототипування та створення дизайн-системи» / Нац. ун-т «Львівська політехніка». — Львів, 2026.",
        "2. Figma Documentation. Components and Variants [Електронний ресурс]. — Режим доступу: https://help.figma.com/hc/en-us/articles/360038662654",
        "3. Web Content Accessibility Guidelines (WCAG) 2.1. W3C Recommendation [Електронний ресурс]. — Режим доступу: https://www.w3.org/TR/WCAG21/",
        "4. Relume AI Documentation [Електронний ресурс]. — Режим доступу: https://library.relume.io/ai",
        "5. Material Design 3. The foundational design system by Google [Електронний ресурс]. — Режим доступу: https://m3.material.io/"
    ]
    for s in sources:
        p = add_p(s, space_before=1, space_after=1)
        set_font(p.runs[0], size_pt=10.0)

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
