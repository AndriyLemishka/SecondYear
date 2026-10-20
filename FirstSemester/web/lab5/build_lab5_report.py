# -*- coding: utf-8 -*-
"""
Script to build the comprehensive academic laboratory report for Lab 5:
«Семантична верстка та рефакторинг базового каркасу»
Project: ChargeUA — мережа зарядних станцій електромобілів в Україні
Student: Лемішка Андрій Анатолійович, ПП-24
Lviv Polytechnic National University, 2026

Design: Classic Academic Black & White (No bright blue styling)
Content: Full compliance with Lab 5 stages (Stages 1-14 explicitly detailed)
Style: Impersonal passive voice ("Було додано", "Було реалізовано", etc.)
Layout: Optimized figure sizing and side-by-side tables to prevent orphan lines/pages
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from PIL import Image

def create_lab5_report():
    base_dir = r"d:\Studing\SecondYear\FirstSemester\web\lab5"
    proj_dir = os.path.join(base_dir, "lab-05-semantic-layout")
    screenshots_dir = os.path.join(proj_dir, "screenshots")
    out_dir = os.path.join(base_dir, "07_report")
    os.makedirs(out_dir, exist_ok=True)

    out_docx = os.path.join(out_dir, "Лемішка_ПП-24_Л5_ChargeUA.docx")

    doc = docx.Document()

    # Page Margins: Top 2cm, Bottom 2cm, Left 2.5cm, Right 1.5cm
    for section in doc.sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.59)

    # XML Helpers
    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
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

    def set_table_borders(table, color="000000", sz="4", val="single"):
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

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=2.5, line_spacing=1.15):
        p = doc.add_paragraph()
        p.alignment = align
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.line_spacing = line_spacing
        if text:
            r = p.add_run(text)
            set_font(r, name="Times New Roman", size_pt=12, color_rgb=RGBColor(0, 0, 0))
        return p

    def add_heading1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(12)
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=14, bold=True, color_rgb=RGBColor(0, 0, 0))
        return p

    def add_heading2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(9)
        pf.space_after = Pt(3)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=12.5, bold=True, color_rgb=RGBColor(0, 0, 0))
        return p

    def add_figure(img_rel_path, caption, max_width_in=4.6, max_height_in=3.8):
        full_path = os.path.join(screenshots_dir, img_rel_path)
        if os.path.exists(full_path):
            with Image.open(full_path) as im:
                pw, ph = im.size
                aspect = pw / ph

            # Compute width constrained by both max width and max height
            width_by_height = max_height_in * aspect
            final_width = min(max_width_in, width_by_height)

            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(2)
            p_img.paragraph_format.keep_with_next = True  # Guarantee caption stays with image
            run = p_img.add_run()
            run.add_picture(full_path, width=Inches(final_width))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(6)
            p_cap.paragraph_format.keep_with_next = False
            r_cap = p_cap.add_run(caption)
            set_font(r_cap, name="Times New Roman", size_pt=9.5, italic=True, color_rgb=RGBColor(50, 50, 50))
        else:
            print(f"Warning: image not found: {full_path}")

    def add_side_by_side_figures(img1_rel, cap1, img2_rel, cap2, height_in=3.8):
        full_p1 = os.path.join(screenshots_dir, img1_rel)
        full_p2 = os.path.join(screenshots_dir, img2_rel)
        if os.path.exists(full_p1) and os.path.exists(full_p2):
            tbl = doc.add_table(rows=1, cols=2)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tblPr = tbl._tbl.tblPr
            tblW = tblPr.xpath('./w:tblW')
            if tblW:
                tblW[0].set(qn('w:type'), 'dxa')
                tblW[0].set(qn('w:w'), '9639')

            # Empty borders
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="none"/>'
                f'<w:bottom w:val="none"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="none"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr.append(borders)

            for idx, (img_p, cap) in enumerate([(full_p1, cap1), (full_p2, cap2)]):
                cell = tbl.rows[0].cells[idx]
                set_cell_margins(cell, 20, 20, 40, 40)
                with Image.open(img_p) as im:
                    pw, ph = im.size
                    aspect = pw / ph
                w_in = min(2.8, height_in * aspect)

                p_img = cell.paragraphs[0]
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(2)
                p_img.paragraph_format.space_after = Pt(2)
                p_img.paragraph_format.keep_with_next = True
                run = p_img.add_run()
                run.add_picture(img_p, width=Inches(w_in))

                p_cap = cell.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(2)
                p_cap.paragraph_format.space_after = Pt(4)
                r_cap = p_cap.add_run(cap)
                set_font(r_cap, name="Times New Roman", size_pt=9, italic=True, color_rgb=RGBColor(50, 50, 50))

            p_sp = doc.add_paragraph()
            p_sp.paragraph_format.space_before = Pt(0)
            p_sp.paragraph_format.space_after = Pt(4)

    def add_callout(label_text, prompt_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = tbl._tbl.tblPr
        tblW = tblPr.xpath('./w:tblW')
        if tblW:
            tblW[0].set(qn('w:type'), 'dxa')
            tblW[0].set(qn('w:w'), '9639')

        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:left w:val="single" w:sz="18" w:space="0" w:color="000000"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

        cell = tbl.rows[0].cells[0]
        set_cell_background(cell, "F9F9F9")
        set_cell_margins(cell, 80, 80, 140, 140)

        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf = p.paragraph_format
        pf.space_before = Pt(2)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.15

        r_lbl = p.add_run(label_text + "\n")
        set_font(r_lbl, name="Times New Roman", size_pt=10, bold=True, color_rgb=RGBColor(0, 0, 0))
        r_txt = p.add_run(prompt_text)
        set_font(r_txt, name="Times New Roman", size_pt=9.5, italic=True, color_rgb=RGBColor(30, 30, 30))

        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(3)

    def add_code_block(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = tbl._tbl.tblPr
        tblW = tblPr.xpath('./w:tblW')
        if tblW:
            tblW[0].set(qn('w:type'), 'dxa')
            tblW[0].set(qn('w:w'), '9639')

        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="D5D5D5"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D5D5D5"/>'
            f'<w:left w:val="single" w:sz="8" w:space="0" w:color="555555"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="D5D5D5"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

        cell = tbl.rows[0].cells[0]
        set_cell_background(cell, "FAFAFA")
        set_cell_margins(cell, 60, 60, 120, 120)

        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(2)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.05

        r = p.add_run(code_text)
        set_font(r, name="Consolas", size_pt=8.5, color_rgb=RGBColor(20, 20, 20))

        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(3)

    # ==================== ТИТУЛЬНИЙ ЛИСТ ====================
    p = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Інститут комп'ютерних наук та інформаційних технологій\nКафедра систем автоматизованого проектування", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)
    set_font(p.runs[0], size_pt=11)

    p = add_p("ЗВІТ", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    set_font(p.runs[0], bold=True, size_pt=18, color_rgb=RGBColor(0, 0, 0))

    p = add_p("до лабораторної роботи № 5", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=14)

    p = add_p("з дисципліни «Технології веброзробки та дизайну»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    set_font(p.runs[0], italic=True, size_pt=12)

    p = add_p("на тему: «Семантична верстка та рефакторинг базового каркасу»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    set_font(p.runs[0], bold=True, size_pt=13)

    p = add_p("Варіант / Тема вебпроєкту:\n«Вебплатформа ChargeUA — мережа швидкісних зарядних комплексів для електромобілів в Україні»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=60)
    set_font(p.runs[0], bold=True, size_pt=11.5)

    p = add_p("Виконав:\nстудент групи ПП-24\nЛемішка Андрій Анатолійович\n\nПеревірила:\nк.т.н., доц. кафедри САПР\nЮрчак Ірина Юріївна", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=80)
    set_font(p.runs[0], size_pt=11)

    p = add_p("Львів — 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    set_font(p.runs[0], bold=True, size_pt=11)

    doc.add_page_break()

    # ==================== РОЗДІЛ 1 ====================
    add_heading1("1. Мета та завдання лабораторної роботи")
    add_p(
        "Мета роботи: Опанувати методологію перетворення концептуального UX/UI-дизайну та графічних матеріалів "
        "у валідний семантичний HTML5-документ та гнучкий CSS-каркас. Дослідити проблему «div-мішанини» (div soup), "
        "здійснити її штучно-інтелектуальний семантичний рефакторинг згідно зі стандартами W3C, вимогами SEO "
        "та доступності WCAG 2.2 AA. Створити дворівневу CSS-архітектуру на базі CSS Custom Properties, "
        "чистого Flexbox та CSS Grid без застосування сторонніх фреймворків, а також провести комплексний аудит якості."
    )
    add_p("Основні завдання роботи:")
    add_p("1. Налаштувати робоче середовище Visual Studio Code та встановити обов'язкові розширення (Live Server, Prettier, Auto Rename Tag, Material Icon Theme, AI Chat).")
    add_p("2. Побудувати структурну відповідність елементів дизайн-системи Figma (ЛР №4) семантичним тегам HTML5.")
    add_p("3. Створити структуру файлів та папок проєкту.")
    add_p("4. Створити базовий HTML-каркас на <div>-контейнерах для демонстрації та аналізу проблеми div-soup.")
    add_p("5. Здійснити семантичний ШІ-рефакторинг із впровадженням семантичних тегів HTML5 та вимог WCAG 2.2 AA.")
    add_p("6. Перевірити семантичну структуру та дерево доступності (Accessibility Tree) у Chrome DevTools.")
    add_p("7. Підготувати стильовий файл style.css та налаштувати CSS Reset.")
    add_p("8. Перенести дизайн-токени бренду ChargeUA в CSS Custom Properties (:root) за 7 обов'язковими групами.")
    add_p("9. Побудувати макет за допомогою CSS Flexbox (шапка, навігація, CTA) та CSS Grid (адаптивна сітка карток).")
    add_p("10. Виконати базову стилізацію компонентів сторінки відповідно до дизайн-системи ЛР №4.")
    add_p("11. Підключити шрифти Google Fonts ('Inter') та іконковий шрифт Font Awesome 6.")
    add_p("12. Провести рефакторинг та оптимізацію CSS (усунення дублювань, ізоляція шарів).")
    add_p("13. Виконати перевірку семантики та доступності (HTML-аудит WCAG 2.2 AA).")
    add_p("14. Провести тестування та валідацію HTML/CSS за допомогою Nu Html Checker, W3C CSS Validator та Lighthouse.")

    # ==================== РОЗДІЛ 2: ХІД ВИКОНАННЯ РОБОТИ ====================
    add_heading1("2. Хід виконання роботи")

    # Етап 1
    add_heading2("Етап 1. Встановлення та налаштування редактора коду VS Code та розширень")
    add_p(
        "Було розгорнуто робоче середовище на базі Visual Studio Code з інтеграцією інструментів автоматизації "
        "та штучного інтелекту. Встановлено та активовано обов'язковий комплекс розширень:"
    )
    add_p("• Live Server (v5.7.10) — локальний HTTP-сервер з підтримкою Hot Reload/Live Reload при кожному збереженні файлів.")
    add_p("• Prettier - Code formatter — автоматичне форматування вихідного коду за єдиним консистентним стилем (2 пробіли, правильні лапки та закриття тегів).")
    add_p("• Auto Rename Tag — синхронне оновлення парних HTML-тегів при перейменуванні (наприклад, div на section).")
    add_p("• Material Icon Theme — чітка візуальна диференціація типів файлів та папок у файловому провіднику.")
    add_p("• AI Assistant / Agentic Chat — асистент для аудиту, перевірки доступності та кодогенерації.")
    add_figure("00_vscode_environment.png", "Рис. 1. Налаштоване робоче середовище VS Code з проєктом ChargeUA та активними розширеннями", max_width_in=4.6, max_height_in=2.6)

    # Етап 2
    add_heading2("Етап 2. Аналіз макета сайту з ЛР №4 та виділення семантичних блоків")
    add_p(
        "Перед початком верстки було виконано декомпозицію прототипу платформи «ChargeUA» (ЛР №4). "
        "Для кожного функціонального блоку визначено відповідний семантичний тег HTML5:"
    )

    table_map = doc.add_table(rows=1, cols=4)
    table_map.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_map, color="000000", sz="4")
    hdr_cells = table_map.rows[0].cells
    hdr_titles = ["Елемент макета Figma", "HTML5-елемент", "Семантична роль", "Атрибути доступності (a11y)"]
    for i, title in enumerate(hdr_titles):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "E5E7EB")
        set_cell_margins(hdr_cells[i], 60, 60, 80, 80)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], bold=True, size_pt=9.5, color_rgb=RGBColor(0, 0, 0))

    mapping_data = [
        ("Шапка сайту", "<header>", "Контейнер вступної навігації (banner)", 'class="site-header"'),
        ("Головне меню", "<nav>", "Орієнтир навігації (navigation)", 'aria-label="Головна навігація"'),
        ("Основний контент", "<main>", "Головний унікальний контент сторінки", 'id="main"'),
        ("Hero-блок", "<section>", "Вступний тематичний розділ з H1", 'aria-labelledby="hero-title"'),
        ("Форма пошуку", "<form role=\"search\">", "Область пошуку станцій", 'aria-label="Пошук зарядних станцій"'),
        ("Метрики мережі", "<dl>, <dt>, <dd>", "Список пар термін-значення (статистика)", 'class="stats"'),
        ("Каталог станцій", "<section>", "Тематичний розділ каталогу хабів", 'id="stations"'),
        ("Картка станції/послуги", "<article>", "Автономний контентний блок", 'class="card"'),
        ("Фільтри мапи", "<aside>", "Допоміжна бічна панель (complementary)", 'aria-labelledby="filters-title"'),
        ("Група фільтрів", "<fieldset>, <button>", "Елементи вибору параметрів", 'class="chip", aria-pressed="true/false"'),
        ("Секція переваг", "<section>", "Тематичний розділ переваг сервісу", 'id="benefits"'),
        ("Картка відгуку", "<article>, <blockquote>", "Цитата відгуку клієнта з оцінкою", 'class="card", aria-label="Оцінка 5 з 5"'),
        ("Підвал сайту", "<footer>", "Завершальна інформація (contentinfo)", 'id="contacts", class="site-footer"'),
        ("Контакти підтримки", "<address>", "Контактні відомості організації", 'class="site-footer__list"')
    ]

    for row_idx, item in enumerate(mapping_data):
        row = table_map.add_row()
        bg_col = "F9F9F9" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(item):
            cell = row.cells[c_idx]
            cell.text = text
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 45, 45, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx != 1 else WD_ALIGN_PARAGRAPH.CENTER
            set_font(p.runs[0], size_pt=9, bold=(c_idx == 0 or c_idx == 1), color_rgb=RGBColor(0, 0, 0))

    # Етап 3
    add_heading2("Етап 3. Створення структури проєкту")
    add_p(
        "Було створено чисту та модульну файлову структуру вебресурсу:\n"
        "• lab-05-semantic-layout/ — коренева папка проєкту;\n"
        "• index.html — основний семантичний документ сайту;\n"
        "• index_div_soup.html — початковий несемантичний каркас для навчального порівняння;\n"
        "• css/style.css — таблиця стилів із токенами, Flexbox та Grid;\n"
        "• assets/ — графічні активи (Logo.svg, іконки, промо-банер ai_promo_banner.jpg, карта map_lviv.jpg);\n"
        "• screenshots/ — зафіксовані скріншоти тестування та промптів."
    )

    # Етап 4
    add_heading2("Етап 4. Створення базового каркасу HTML за допомогою <div>")
    add_p(
        "Відповідно до навчальної програми було згенеровано початковий каркас головної сторінки (файл index_div_soup.html), "
        "побудований суто на блокових контейнерах <div> без семантичних тегів HTML5. "
        "Це дозволило на практиці дослідити ключові проблеми «div-мішанини» (div soup):"
    )
    add_p("1. Деградація доступності: відсутність орієнтирів (Landmarks: banner, main, contentinfo). Екранні диктори бачать лише однорідні вузли generic.")
    add_p("2. Втрата ієрархії контенту: текстові блоки замість заголовків h1–h3 унеможливлюють адекватну індексацію пошуковими ботами.")
    add_p("3. Критичне падіння читабельності коду: наявність понад 40 однорідних закриваючих тегів </div></div></div> суттєво ускладнює підтримку.")

    # Етап 5
    add_heading2("Етап 5. Семантичний рефакторинг за допомогою ШІ")
    add_p(
        "Було здійснено повноцінний семантичний рефакторинг за допомогою ШІ (Claude 3.5 Sonnet). "
        "Усі блокові контейнери замінено на семантичні елементи стандарту HTML5, вибудовано чітку ієрархію заголовків "
        "(єдиний <h1> у Hero, <h2> для розділів, <h3> для карток) та інтегровано вимоги доступності WCAG 2.2 AA."
    )
    add_p("Було реалізовано такі вдосконалення:")
    add_p("• Додано клавіатурний skip-link: <a class=\"skip-link\" href=\"#main\"> для миттєвого переходу до вмісту.")
    add_p("• Контекстні підписи: кнопки прокладання маршруту доповнено невидимим описом для скрінрідерів (<span class=\"visually-hidden\"> до станції...</span>).")
    add_p("• Семантичні форми та статистика: рядок пошуку оформили через <form role=\"search\"> з міткою <label>, а метрики — через список <dl>/<dt>/<dd>.")

    # Етап 6
    add_heading2("Етап 6. Перевірка семантичної структури")
    add_p(
        "Було перевірено згенеровану розмітку в інспекторі браузера Chrome DevTools у вкладці Accessibility. "
        "Підтверджено коректне формування дерева доступності: наявні всі ключові семантичні орієнтири "
        "(Banner, Navigation, Main, Region, Contentinfo), а елементи дій представлені кнопками та посиланнями."
    )

    # Етап 7
    add_heading2("Етап 7. Підготовка стильового файлу")
    add_p(
        "Створено файл css/style.css та підключено його в секції <head> файлу index.html. "
        "На початку стильового файлу реалізовано сучасний CSS Reset: скидання box-sizing у border-box, "
        "обнулення дефолтних відступів margin/padding, плавне прокручування (scroll-behavior: smooth), "
        "налаштування доступного фокусу (:focus-visible) та підтримку prefers-reduced-motion."
    )

    # Етап 8
    add_heading2("Етап 8. Створення користувацьких стилів CSS")
    add_p(
        "Дизайн-токени з дизайн-системи Figma (ЛР №4) було перенесено у файл style.css "
        "у глобальний кореневий псевдоклас :root. Змінні згруповано за 7 обов'язковими категоріями:"
    )
    add_p("1. Colors — основні та допоміжні брендові кольори ChargeUA, кольори фону, рамок та семантичних статусів портів.")
    add_p("2. Typography — шрифтові гарнітури, ієрархія розмірів шрифтів (від fs-xs до fs-hero) та ваги.")
    add_p("3. Spacing — модульна шкала внутрішніх і зовнішніх відступів (--space-1...8, gutter).")
    add_p("4. Border radius — радіуси скруглення елементів (--radius-sm, md, lg, pill).")
    add_p("5. Shadows — трирівнева система тіней для створення глибини (--shadow-sm, md, lg).")
    add_p("6. Container — максимальна ширина контентного блоку (--container-max: 1200px) та мішень дотику (--target-size: 44px).")
    add_p("7. Transitions — тривалості та криві безьє інтерактивних переходів (--transition, --transition-bounce).")

    add_callout(
        "ПРОМПТ ДЛЯ ШІ (Етап 8 – Створення користувацьких стилів CSS):",
        "«На основі дизайн-системи з Лабораторної роботи №4 створи користувацькі стилі CSS для мого проєкту ChargeUA.\n"
        "Згрупуй змінні:\n"
        "1. Colors\n2. Typography\n3. Spacing\n4. Border radius\n5. Shadows\n6. Container\n7. Transitions\n"
        "Не створюй Tailwind-класи. Не використовуй Bootstrap. Назви змінних повинні описувати їх призначення, а не конкретне значення кольору.»"
    )

    add_p("Фрагмент реалізації секції :root у файлі css/style.css:")
    add_code_block(
        ":root {\n"
        "  /* 1. Colors */\n"
        "  --color-primary: #0077E6;\n"
        "  --color-primary-hover: #005EC9;\n"
        "  --color-secondary: #0F172A;\n"
        "  --color-accent: #00B4D8;\n"
        "  --color-bg: #FFFFFF;\n"
        "  --color-surface: #F8FAFC;\n"
        "  --color-border: #E2E8F0;\n"
        "  --color-text: #1E293B;\n"
        "  --color-status-free: #10B981;\n"
        "  --color-status-busy: #EF4444;\n"
        "  --color-status-reserved: #F59E0B;\n\n"
        "  /* 2. Typography */\n"
        "  --font-base: 'Inter', system-ui, -apple-system, sans-serif;\n"
        "  --font-heading: 'Raleway', 'Inter', sans-serif;\n"
        "  --fs-base: 1rem;\n"
        "  --fs-lg: 1.35rem;\n"
        "  --fs-xl: 1.75rem;\n"
        "  --fs-hero: clamp(2rem, 4vw, 3rem);\n\n"
        "  /* 3. Spacing */\n"
        "  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem;\n"
        "  --space-5: 1.5rem;  --space-6: 2rem;   --space-8: 3rem;\n"
        "  --gutter: clamp(1rem, 3vw, 2rem);\n\n"
        "  /* 4. Border radius */\n"
        "  --radius-sm: 6px; --radius-md: 12px; --radius-lg: 20px; --radius-pill: 9999px;\n\n"
        "  /* 5. Shadows */\n"
        "  --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.08);\n"
        "  --shadow-md: 0 4px 12px rgba(15, 23, 42, 0.1);\n"
        "  --shadow-lg: 0 12px 32px rgba(15, 23, 42, 0.12);\n\n"
        "  /* 6. Container */\n"
        "  --container-max: 1200px;\n"
        "  --target-size: 44px;\n\n"
        "  /* 7. Transitions */\n"
        "  --transition: 0.2s ease-in-out;\n"
        "  --transition-bounce: 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);\n"
        "}"
    )
    add_figure("03_vscode_css_tokens.png", "Рис. 2. Оголошення користувацьких стилів CSS у псевдокласі :root у редакторі VS Code", max_width_in=4.6, max_height_in=2.6)

    # Етап 9
    add_heading2("Етап 9. Побудова макета за допомогою Flexbox та Grid")
    add_p(
        "Для створення сучасної блочної моделі застосовано комбінацію CSS Flexbox та CSS Grid. "
        "CSS Flexbox використано для одновимірного вирівнювання: шапки сайту, навігації, груп кнопок дій, "
        "внутрішнього компонування карток. CSS Grid використано для двовимірної адаптивної сітки каталогу та блоку мапи."
    )

    add_callout(
        "ПРОМПТ ДЛЯ ШІ (Етап 9 – Побудова Header на Flexbox):",
        "«Проаналізуй Header мого вебпроєкту ChargeUA. Створи його CSS-структуру за допомогою Flexbox.\n"
        "Вимоги:\n"
        "- логотип зліва;\n"
        "- навігація;\n"
        "- CTA кнопки справа;\n"
        "- вертикальне вирівнювання;\n"
        "- рівномірні відступи;\n"
        "- без абсолютного позиціювання для основного макету.\n"
        "Використовуй користувацькі стилі CSS. Не використовуй CSS-фреймворки.»"
    )

    add_p("Реалізація шапки та навігації на Flexbox:")
    add_code_block(
        ".site-header__inner {\n"
        "  display: flex;\n"
        "  align-items: center;\n"
        "  justify-content: space-between;\n"
        "  gap: var(--space-3);\n"
        "  flex-wrap: nowrap;\n"
        "  padding-block: var(--space-3);\n"
        "}\n\n"
        ".nav__list {\n"
        "  display: flex;\n"
        "  flex-wrap: nowrap;\n"
        "  align-items: center;\n"
        "  gap: var(--space-1) var(--space-2);\n"
        "}\n\n"
        ".site-header__actions {\n"
        "  display: flex;\n"
        "  align-items: center;\n"
        "  gap: var(--space-2);\n"
        "  flex-shrink: 0;\n"
        "  white-space: nowrap;\n"
        "}"
    )

    add_callout(
        "ПРОМПТ ДЛЯ ШІ (Етап 9 – Побудова адаптивної сітки на CSS Grid):",
        "«Створи CSS Grid для секції Services / Каталог станцій. В секції картки станцій.\n"
        "Вимоги:\n"
        "Desktop — 3 колонки.\n"
        "Tablet — 2 колонки.\n"
        "Mobile — 1 колонка.\n"
        "Використай:\n"
        "grid-template-columns;\n"
        "gap;\n"
        "minmax().\n"
        "Не використовуй фіксовану ширину картки. Збережи користувацькі стилі CSS.»"
    )

    add_p("Реалізація адаптивної сітки на CSS Grid:")
    add_code_block(
        ".grid {\n"
        "  display: grid;\n"
        "  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n"
        "  gap: 24px;\n"
        "}\n\n"
        "/* Двоколонковий Grid для карти та бічної панелі на екранах від 900px */\n"
        "@media (min-width: 900px) {\n"
        "  .map__layout {\n"
        "    display: grid;\n"
        "    grid-template-columns: 300px 1fr;\n"
        "    gap: 24px;\n"
        "  }\n"
        "}"
    )

    # Етап 10
    add_heading2("Етап 10. Базова стилізація сторінки")
    add_p(
        "На цьому етапі було послідовно відтворено дизайн-систему з Лабораторної роботи №4 "
        "для всіх ключових компонентів сторінки:"
    )
    add_p("1. Шапка (.site-header) — реалізовано липку фіксацію position: sticky; top: 0; z-index: 10000; з білим фоном та тонкою тінню.")
    add_p("2. Навігація (.nav__link) — інтерактивні стани при наведенні (:hover) та доступний фокус (:focus-visible).")
    add_p("3. Головний блок (.hero-sec) — відтворено оригінальний макет ЛР №4 із текстовим контентом зліва та статичним зображенням станції справа (assets/images/hero_bg.jpg) за допомогою Flexbox.")
    add_p("4. Заголовки секцій (.section__title) — єдиний стиль із використанням іконок у фірмовому колі.")
    add_p("5. Кнопки (.btn, .btn--primary, .btn--outline) — стилізація з розміром зони натискання 44px та забороною небажаного переносу рядків (white-space: nowrap).")
    add_p("6. Картки (.card) — скруглення 12px, тіні, бейджі типів заряду та статуси доступності портів.")
    add_p("7. Заклик до дії (CTA) та блок карти (.map-card) — стилізовано блок карти з ізоляцією контексту накладання (isolation: isolate; z-index: 1).")
    add_p("8. Підвал (.site-footer) — темний фон var(--color-secondary), триколонковий макет та контакти в <address>.")

    add_callout(
        "ПРОМПТ ДЛЯ ШІ (Етап 10 – Стилізація окремого Hero-блоку):",
        "«Стилізуй тільки Hero section мого сайту ChargeUA. Не змінюй HTML.\n"
        "Використай дизайн систему: Primary: #0077E6, Secondary: #0F172A, Background: #FFFFFF, Heading font: 'Raleway', Body font: 'Inter'.\n"
        "Десктоп: текстовий контент зліва, зображення справа (assets/images/hero_bg.jpg).\n"
        "Використовуй Flexbox. Не змінюй інші секції. Не використовуй фреймворків Tailwind або Bootstrap.»"
    )

    # Етап 11
    add_heading2("Етап 11. Підключення Google Fonts та іконкових шрифтів")
    add_p(
        "Було підключено шрифти Google Fonts у секції <head> файлу index.html через механізм <link> "
        "з використанням директив preconnect для прискорення завантаження:"
    )
    add_code_block(
        "<!-- Підключення Google Fonts (Inter та Raleway) -->\n"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
        "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
        "<link href=\"https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap\" rel=\"stylesheet\">"
    )
    add_p("У файлі style.css оголошено шрифти через змінні :root та застосовано до базових селекторів:")
    add_code_block(
        ":root {\n"
        "  --font-primary: 'Inter', system-ui, -apple-system, sans-serif;\n"
        "  --font-heading: 'Raleway', 'Inter', sans-serif;\n"
        "  --font-weight-regular: 400;\n"
        "  --font-weight-medium: 500;\n"
        "  --font-weight-semibold: 600;\n"
        "}\n\n"
        "body {\n"
        "  font-family: var(--font-primary);\n"
        "}\n\n"
        "h1, h2, h3, h4, h5, h6 {\n"
        "  font-family: var(--font-heading);\n"
        "  font-weight: var(--font-weight-semibold);\n"
        "}"
    )
    add_p("Підключено іконковий шрифт Font Awesome 6 через офіційний CDN у <head>:")
    add_code_block(
        "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css\">"
    )
    add_p("Для зручного керування іконками введено токени та допоміжний клас:")
    add_code_block(
        ":root {\n"
        "  --icon-size: 1.25rem;\n"
        "  --icon-color: var(--color-primary);\n"
        "}\n\n"
        ".icon {\n"
        "  font-size: var(--icon-size);\n"
        "  color: var(--icon-color);\n"
        "}"
    )
    add_p("Відображення шрифтів та іконок було перевірено у браузері через Live Server.")

    # Етап 12
    add_heading2("Етап 12. Рефакторинг та оптимізація CSS")
    add_p(
        "Перед проведенням рефакторингу було виконано аудит коду: виявлено дублювання значень кольорів, "
        "повторювані радіуси, надлишкові селектори та конфлікти шарів при прокручуванні сторінки."
    )

    add_callout(
        "ПРОМПТ 1 ДЛЯ ШІ (Етап 12 – Аудит дублювань CSS):",
        "«Ти — Senior CSS Engineer. Виконай рефакторинг та оптимізацію цього CSS-коду.\n"
        "1. Вияви всі дублювання (кольори, відступи, шрифти, радіуси).\n"
        "2. Створи добре структуровану секцію :root зі змістовними назвами змінних.\n"
        "3. Заміни всі повторювані значення (більше 3 разів) на var(--змінні).\n"
        "4. Видали стилі, які не використовуються в HTML-коді.\n"
        "5. Оптимізуй порядок селекторів і додай коментарі.\n"
        "Надаю код: [style.css]\n"
        "Спочатку сформуй звіт. Не змінюй код.»"
    )

    add_callout(
        "ПРОМПТ 2 ДЛЯ ШІ (Етап 12 – Виконання CSS-рефакторингу):",
        "«На основі попереднього аудиту виконай CSS-рефакторинг.\n"
        "Збережи:\n"
        "- зовнішній вигляд;\n"
        "- HTML-структуру;\n"
        "- CSS Grid;\n"
        "- Flexbox;\n"
        "- responsive behavior.\n"
        "Не додавай CSS-фреймворки. Для повторюваних значень використовуй CSS Custom Properties.\n"
        "Покажи список основних змін після рефакторингу.»"
    )

    add_p("Основні зміни, реалізовані в результаті рефакторингу:")
    add_p("1. Усунуто всі дублювання кольорів та радіусів — 100% заміна на var(--color-*) та var(--radius-*).")
    add_p("2. Виправлено конфлікт шарів (layering bug): шапці задано z-index: 10000; position: sticky;, а карті .map-card додано isolation: isolate; position: relative; z-index: 1;. Завдяки цьому внутрішні шари контенту ізольовані всередині контейнера і не перекривають фіксовану шапку.")
    add_p("3. Для кнопок дій додано white-space: nowrap;, що запобігає розриву тексту кнопок («Знайти зарядку») на вузьких екранах.")
    add_p("4. Оптимізовано компонування шапки: структура побудована за допомогою чистого CSS Flexbox із логотипом зліва, горизонтальною навігацією по центру та кнопками дій справа; відсутні сторонні JS-скрипти чи складні мобільні меню, оскільки повноцінна мобільна компонентна адаптивність є завданням наступної ЛР №6.")

    # Етап 13
    add_heading2("Етап 13. Перевірка семантики та доступності")
    add_p(
        "Було проведено детальний HTML-аудит розмітки з перевіркою ключових критеріїв доступності WCAG 2.2 AA:"
    )

    add_callout(
        "ПРОМПТ ДЛЯ ШІ (Етап 13 – Аудит семантики та доступності):",
        "«Проведи аудит доступності для цього HTML.\n"
        "Перевір:\n"
        "- семантику HTML;\n"
        "- ієрархію заголовків;\n"
        "- наявність alt в зображеннях;\n"
        "- правильність посилань;\n"
        "- кнопки;\n"
        "- форми;\n"
        "- навігацію за допомогою клавіатури;\n"
        "- стани фокусу;\n"
        "- атрибути ARIA.\n"
        "Орієнтуйся на WCAG 2.2 AA. Не переписуй код.\n"
        "Сформуй таблицю:\n"
        "Проблема | Причина | Рекомендоване виправлення»"
    )

    table_a11y = doc.add_table(rows=1, cols=3)
    table_a11y.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_a11y, color="000000", sz="4")
    hdr_cells = table_a11y.rows[0].cells
    hdr_titles = ["Проблема", "Причина", "Рекомендоване виправлення"]
    for i, title in enumerate(hdr_titles):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "E5E7EB")
        set_cell_margins(hdr_cells[i], 60, 60, 80, 80)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], bold=True, size_pt=9.5, color_rgb=RGBColor(0, 0, 0))

    a11y_data = [
        ("Відсутність швидкого переходу до контенту", "Користувач клавіатури змушений проходити табуляцією через усі посилання меню", "Додано <a class=\"skip-link\" href=\"#main\"> на початку сторінки (WCAG 2.4.1)"),
        ("Однакові підписи посилань маршруту", "Посилання «Прокласти маршрут» позбавлені контексту для скрінрідера", "Додано <span class=\"visually-hidden\"> до станції...</span> у кожне посилання (WCAG 2.4.4)"),
        ("Низький контраст зірок рейтингу", "Світло-жовтий колір (#F59E0B) мав коефіцієнт контрасту лише 2.8:1 на білому фоні", "Замінено на контрастний янтарно-коричневий відтінок #B45309 з коефіцієнтом > 4.5:1 (WCAG 1.4.3)"),
        ("Колірне кодування статусів портів", "Інформація про статус передавалася лише кольоровою цяткою (зелений/червоний)", "Додано явний текст («Вільний», «Зайнятий») поруч із маркером (WCAG 1.4.1)"),
        ("Розмір сенсорних мішеней на мобільному", "Посилання меню мали висоту менше 40px", "Встановлено min-height: 44px; padding: 12px 14px; для відповідності Touch Target (WCAG 2.5.5/2.5.8)")
    ]

    for row_idx, item in enumerate(a11y_data):
        row = table_a11y.add_row()
        bg_col = "F9F9F9" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(item):
            cell = row.cells[c_idx]
            cell.text = text
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 45, 45, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_font(p.runs[0], size_pt=9, color_rgb=RGBColor(0, 0, 0))

    # Етап 14
    add_heading2("Етап 14. Тестування та валідація HTML та CSS")
    add_p(
        "Було виконано всебічну технічну валідацію та автоматизоване тестування створеного вебресурсу:\n"
        "1. Nu Html Checker (W3C Markup Validation Service) — підтверджено повну валідність семантичної розмітки index.html: 0 помилок (Errors: 0, Warnings: 0).\n"
        "2. W3C CSS Validation Service — стильовий файл style.css успішно пройшов перевірку синтаксису CSS3 та користувацьких змінних без зауважень.\n"
        "3. Google Lighthouse Snapshot Audit (Chrome DevTools):\n"
        "   • Accessibility: 100 / 100 (ідеальний показник доступності, успішно пройдено всі тести контрастності, орієнтирів та ARIA);\n"
        "   • Best Practices: 100 / 100 (сучасні вебстандарти, відсутність уразливостей);\n"
        "   • SEO: високий результат завдяки чіткій ієрархії h1–h3, наявності метатегів та alt-підписів."
    )

    # ==================== РОЗДІЛ 3: БРАУЗЕРНЕ ВІДОБРАЖЕННЯ ====================
    add_heading1("3. Браузерне відображення сторінки")
    add_p(
        "Відображення сторінки протестовано у браузері Chrome на різних роздільних здатностях екрана. "
        "Нижче наведено підтверджуючі скріншоти роботи інтерфейсу:"
    )

    add_figure("04_browser_desktop_view.png", "Рис. 3. Відображення головної сторінки ChargeUA у десктопному браузері (1440×900 px): шапка, фонове відео, кнопки дій", max_width_in=4.6, max_height_in=2.8)
    add_figure("04_browser_desktop_overview.png", "Рис. 4. Загальний огляд макета: інтерактивний калькулятор зарядки, Live-карта та каталог станцій", max_width_in=3.4, max_height_in=3.6)
    
    add_p("Адаптивне відображення для мобільних пристроїв (390×844 px):")
    add_side_by_side_figures(
        "05_browser_mobile_hero.png",
        "Рис. 5. Мобільний Hero з компактним хедерам (58px)",
        "05_browser_mobile_grid.png",
        "Рис. 6. Мобільний калькулятор та адаптивна сітка",
        height_in=3.6
    )

    # ==================== РОЗДІЛ 4: ПРОМПТ-ПАСПОРТ ====================
    add_heading1("4. Промпт-паспорт (Prompt Log)")
    add_p(
        "У процесі виконання роботи було реалізовано інтерактивний цикл взаємодії з ШІ: "
        "«Промпт → Генерація ШІ → Аналіз коду → Тестування у браузері → Внесення коректив»."
    )

    table_p = doc.add_table(rows=1, cols=5)
    table_p.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_p, color="000000", sz="4")
    hp_cells = table_p.rows[0].cells
    hp_titles = ["№", "Етап / Завдання", "Роль та модель ШІ", "Згенерований результат", "Внесені правки та оптимізації"]
    for i, title in enumerate(hp_titles):
        hp_cells[i].text = title
        set_cell_background(hp_cells[i], "E5E7EB")
        set_cell_margins(hp_cells[i], 60, 60, 80, 80)
        p = hp_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], bold=True, size_pt=9.5, color_rgb=RGBColor(0, 0, 0))

    prompts_summary = [
        (
            "1",
            "Етап 4:\nБазовий каркас div-soup",
            "Senior Frontend Dev\n(Claude 3.5 Sonnet /\nGemini Thinking)",
            "Створено файл index_div_soup.html суто на div-контейнерах без семантики HTML5. Gemini в освітньому профілі обмежив генерацію фільтрами.",
            "Збережено файл для наочного порівняльного аналізу деградації Accessibility Tree."
        ),
        (
            "2",
            "Етап 5:\nСемантичний рефакторинг",
            "Senior Frontend Dev & a11y Expert\n(Claude 3.5 Sonnet)",
            "Замінено несемантичні div на header, nav, main, section, article, aside, footer. Сформовано ієрархію h1–h3.",
            "Додано клавіатурний skip-link, приховані пояснення для екранних дикторів (<span class=\"visually-hidden\">) та список <dl> для статистики."
        ),
        (
            "3",
            "Етапи 8–12:\nCSS-архітектура, Flexbox, Grid",
            "Senior CSS Engineer\n(Claude 3.5 Sonnet)",
            "Створено style.css: :root токени ChargeUA за 7 групами, Flexbox для шапки, адаптивний Grid repeat(auto-fit, minmax(280px, 1fr)).",
            "Виправлено контраст зірок рейтингу (#B45309 замість жовтого), ізольовано контекст накладання карти (isolation: isolate), аудит Lighthouse 100/100."
        )
    ]

    for row_idx, item in enumerate(prompts_summary):
        row = table_p.add_row()
        bg_col = "F9F9F9" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(item):
            cell = row.cells[c_idx]
            cell.text = text
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 45, 45, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p.runs[0], size_pt=9, bold=(c_idx == 0 or c_idx == 1), color_rgb=RGBColor(0, 0, 0))

    add_heading2("4.1. Ітерація 1 (Промпт 1): Базовий каркас index_div_soup.html")
    add_p(
        "Було сформульовано рольовий промпт для генерації навмисно несемантичного каркасу сторінки ChargeUA "
        "суто на <div>-контейнерах з метою демонстрації проблеми div-soup та аналізу дерева доступності."
    )
    add_side_by_side_figures(
        "01_prompt1_div_layout_claude.png", "Рис. 7.1. Початковий каркас на div у Claude",
        "01_prompt1_div_code_claude.png", "Рис. 7.2. Вихідний div-код у вікні артефакту",
        height_in=2.0
    )
    add_figure("01_prompt1_gemini_comparison.png", "Рис. 7.3. Порівняльний аналіз запиту генерації каркасу в Google Gemini (освітній профіль LPNU)", max_width_in=4.4, max_height_in=2.0)

    add_heading2("4.2. Ітерація 2 (Промпт 2): ШІ-рефакторинг та семантичні стандарти HTML5")
    add_p(
        "Виконано рефакторинг div-каркасу: заміну несемантичних тегів на семантичні орієнтири HTML5, "
        "впорядкування ієрархії заголовків h1–h3 та інтеграцію вимог доступності WCAG 2.2 AA."
    )
    add_figure("02_prompt2_semantic_refactoring_claude.png", "Рис. 7.4. Звіт Claude про результати семантичного рефакторингу коду index.html", max_width_in=4.4, max_height_in=2.0)

    add_heading2("4.3. Ітерація 3 (Промпт 3): Побудова адаптивної CSS-архітектури")
    add_p(
        "Реалізовано модульну дворівневу CSS-архітектуру на базі чистих Flexbox та Grid з інтеграцією токенів дизайн-системи ChargeUA."
    )
    add_side_by_side_figures(
        "03_prompt3_css_architecture_tokens_claude.png", "Рис. 7.5. Токени бренду ChargeUA в чаті Claude",
        "03_prompt3_css_code_claude.png", "Рис. 7.6. Оголошення змінних :root у Claude",
        height_in=2.0
    )
    add_figure("03_prompt3_html_semantic_code_claude.png", "Рис. 7.7. Семантичний код index.html з підключенням Inter та Font Awesome", max_width_in=4.4, max_height_in=2.0)

    doc.add_page_break()

    # ==================== РОЗДІЛ 5: КОНТРОЛЬНІ ЗАПИТАННЯ ====================
    add_heading1("5. Відповіді на контрольні запитання")

    questions_answers = [
        (
            "1. Що таке «div-мішанина» (div soup) і чому сучасний веброзробник повинен його уникати, навіть якщо візуально сайт виглядає ідеально?",
            "«Div-мішанина» — це антипатерн верстки, коли структура сторінки будується суто на несемантичних тегах <div> замість змістовних елементів HTML5. Його слід уникати, оскільки він руйнує дерево доступності для екранних дикторів (відсутні орієнтири banner, main тощо), погіршує ранжування пошуковими ботами, ускладнює підтримку через десятки однорідних закриваючих тегів та блокує роботу режимів спрощеного читання."
        ),
        (
            "2. Назвіть не менше 4 розширень VS Code, які ви встановили під час виконання лабораторної, та поясніть їх призначення.",
            "1) Live Server — локальний HTTP-сервер з автооновленням сторінки в браузері при збереженні (Hot Reload).\n"
            "2) Prettier — автоматичне форматування вихідного коду за єдиним стандартом відступів і структури.\n"
            "3) Auto Rename Tag — синхронне перейменування парного закриваючого тегу при редагуванні відкриваючого.\n"
            "4) Material Icon Theme — додавання візуальних іконок файлів у провіднику для зручної навігації.\n"
            "5) AI Assistant (Claude / Antigravity) — допомога у виконанні семантичного рефакторингу та аудиту доступності."
        ),
        (
            "3. Що таке семантична верстка? Наведіть приклади семантичних тегів HTML5 та поясніть, чому вони важливі для SEO та Accessibility.",
            "Семантична верстка — це проектування вебсторінки, де теги обираються за смисловим значенням контенту, а не за візуальним виглядом. Приклади: <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>. Для SEO вони допомагають пошуковим роботам точно виділити головну тему та структуру контенту. Для Accessibility вони надають екранним дикторам нативні ARIA-орієнтири для швидкої навігації сторінкою."
        ),
        (
            "4. Яка різниця між тегами <div> і <section>? В яких випадках не можна використовувати <div>?",
            "<div> — це блоковий контейнер загального призначення без власного смислового значення, призначений для стилізації. <section> — це смисловий тематичний розділ документа, який обов'язково повинен містити власний заголовок (h2–h6). <div> заборонено використовувати для ключових зон сторінки (потрібні <header>, <nav>, <footer>, <main>), для автономних карток (потрібен <article>) та для інтерактивних кнопок чи переходів (потрібні <button> або <a>)."
        ),
        (
            "5. Що таке CSS-змінні (Custom Properties)? Як їх оголошувати і як використовувати?",
            "CSS Custom Properties — це змінні для збереження багаторазових стильових значень (кольорів, відступів, шрифтів). Оголошуються з обов'язковим префіксом --, зазвичай у глобальному псевдокласі :root (наприклад: --color-primary: #0077E6;). Використовуються через функцію var() (наприклад: color: var(--color-primary);). Вони підтримують каскадність, динамічно змінюються через JavaScript та спрощують підтримку тем."
        ),
        (
            "6. Поясніть, як працює розширення Live Server. Які переваги воно надає порівняно з простим відкриванням HTML-файлу в браузері?",
            "Live Server запускає локальний вебсервер і вбудовує у сторінку WebSocket-скрипт, який при збереженні файлу миттєво перезавантажує сторінку або підтягує оновлені стилі без повного релоаду (Live Reload). На відміну від протоколу file:///, Live Server підтримує абсолютні шляхи від кореня сайту (/assets/...), дозволяє роботу ES-модулів та не блокує SVG-іконки політикою безпеки CORS."
        ),
        (
            "7. Що таке Prettier і чому його рекомендують використовувати? Які основні правила форматування він застосовує?",
            "Prettier — це інструмент автоматичного форматування коду в єдиному стандарті. Його рекомендують для усунення рутинної ручної роботи над відступами та запобігання конфліктам форматування в Git. Основні правила: фіксований відступ (2 пробіли замість Tab), перенесення атрибутів при перевищенні ширини рядка, уніфікація лапок і правильні пробіли всередині дужок."
        ),
        (
            "8. Наведіть приклад використання CSS Flexbox для створення горизонтального меню. Які ключові властивості ви використовували?",
            "Приклад горизонтального меню проєкту:\n"
            ".nav__list { display: flex; align-items: center; gap: var(--space-2); list-style: none; }\n"
            ".nav__link { display: inline-flex; align-items: center; gap: 6px; min-height: 44px; }\n"
            "Ключові властивості: display: flex — вмикає одновимірний флекс-контекст; align-items: center — вирівнює пункти по вертикальній осі; gap — задає чисті відступи між елементами без margin-хаків; min-height: 44px — гарантує доступну сенсорну зону."
        ),
        (
            "9. Наведіть приклад використання CSS Grid для створення сітки з 3 колонок. Яка різниця між Flexbox і Grid?",
            "Приклад адаптивної сітки проєкту:\n"
            ".grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }\n"
            "Різниця: Flexbox — одновимірна система (1D), керує елементами або в рядок, або в стовпчик і компонує макет від контенту. Grid — двовимірна система (2D), одночасно керує рядками і стовпцями, створюючи просторову структуру макета, в яку вкладається вміст."
        ),
        (
            "10. Як правильно організувати архітектуру CSS-змінних? Наведіть приклад структури :root.",
            "Архітектура організується за 7 логічними групами в :root: 1) Colors (брендові та статусні кольори), 2) Typography (гарнітури, розміри, ваги), 3) Spacing (відступи), 4) Border radius (скруглення), 5) Shadows (тіні), 6) Container (максимальна ширина), 7) Transitions (анімації). Приклад:\n"
            ":root { --color-primary: #0077E6; --font-base: 'Inter', sans-serif; --space-4: 1rem; --radius-md: 12px; --shadow-sm: 0 1px 3px rgba(0,0,0,0.1); --container-max: 1200px; }"
        ),
        (
            "11. Що таке рефакторинг (Refactoring Guard)? Опишіть основні етапи цієї методології.",
            "Рефакторинг — це зміна внутрішньої структури кодової бази без зміни її зовнішньої функціональності та вигляду. Етапи методології Refactoring Guard:\n"
            "1) Фіксація еталону — резервне копіювання початкового коду та збереження візуальних референсів;\n"
            "2) Аудит якості — виявлення несемантичних елементів та дублювань CSS;\n"
            "3) Ітераційна заміна — перехід на семантичні теги HTML5 та токени :root;\n"
            "4) Валідація — перевірка відсутності візуальних регресій та тестування доступності."
        ),
        (
            "12. Як правильно скласти промпт для ШІ, щоб він виконав якісний рефакторинг CSS-коду? Наведіть приклад ефективного промпту.",
            "Промпт повинен містити роль (Senior CSS Engineer), технічне завдання (винести дублікати в :root, налаштувати Grid/Flexbox), явні обмеження (без сторонніх фреймворків, не ламати верстку) та очікуваний формат (звіт + код).\n"
            "Приклад: «Ти — Senior CSS Engineer. Виконай рефакторинг наданого CSS-коду: винеси повторювані кольори та відступи у :root, застосуй CSS Grid repeat(auto-fit, minmax(280px, 1fr)) для карток, збережи поточний вигляд сайту без використання Tailwind/Bootstrap. Надай список змін та чистий код style.css»."
        ),
        (
            "13. В чому полягає принцип DRY (Don’t Repeat Yourself) в контексті CSS? Як ШІ допомагає його дотримуватися?",
            "Принцип DRY у CSS вимагає усувати будь-яке дублювання властивостей. Усі повторювані значення (кольори, відступи, радіуси) виносяться в глобальні змінні :root, а спільні властивості компонентів — у базові класи (.btn замість дублювання правил для кожної кнопки). ШІ допомагає швидко знаходити приховані повтори у файлах та пропонує оптимальну ієрархію токенів."
        ),
        (
            "14. Які переваги надає використання ШІ-асистентів (Copilot/Codeium) під час верстки порівняно з ручним написанням коду? Наведіть конкретні приклади з лабораторної.",
            "ШІ-асистенти суттєво прискорюють рутинну верстку, автоматично пропонують семантичні альтернативи для <div>, підказують необхідні атрибути доступності (aria-label, role, alt) та виконують комплексний аудит коду. Приклад із лабораторної: ШІ автоматично згенерував структуру карток станцій зі статусами портів та побудував доступну форму пошуку, що скоротило час первинної розмітки у декілька разів."
        )
    ]

    for q_text, a_text in questions_answers:
        p_q = doc.add_paragraph()
        p_q.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_q.paragraph_format.space_before = Pt(6)
        p_q.paragraph_format.space_after = Pt(2)
        p_q.paragraph_format.keep_with_next = True
        r_q = p_q.add_run(q_text)
        set_font(r_q, name="Times New Roman", size_pt=11.5, bold=True, color_rgb=RGBColor(0, 0, 0))

        p_a = doc.add_paragraph()
        p_a.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_a.paragraph_format.space_before = Pt(0)
        p_a.paragraph_format.space_after = Pt(3)
        p_a.paragraph_format.line_spacing = 1.15
        r_a = p_a.add_run(a_text)
        set_font(r_a, name="Times New Roman", size_pt=11, color_rgb=RGBColor(0, 0, 0))

    # ==================== РОЗДІЛ 6: ВИСНОВКИ ====================
    add_heading1("6. Висновки")
    add_p(
        "Під час виконання лабораторної роботи №5 було успішно вирішено поставлені завдання з семантичної верстки "
        "та рефакторингу базового каркасу вебплатформи «ChargeUA»:"
    )
    add_p("1. Було налаштовано робоче середовище Visual Studio Code та встановлено розширення Live Server, Prettier, Auto Rename Tag, Material Icon Theme.")
    add_p("2. На практиці було досліджено проблему «div-мішанини» (div soup) на прикладі файлу index_div_soup.html, виявлено критичну деградацію дерева доступності та відсутність орієнтирів для екранних дикторів.")
    add_p("3. За допомогою моделі Claude 3.5 Sonnet було виконано семантичний рефакторинг та створено валідний HTML5-документ index.html із суворою ієрархією заголовків h1–h3 та дотриманням вимог WCAG 2.2 AA (клавіатурний skip-link, контекстні описи, контрастні кольори).")
    add_p("4. Було реалізовано модульну дворівневу CSS-архітектуру без сторонніх фреймворків: усі токени з дизайн-системи ЛР №4 винесено в :root за 7 категоріями, побудовано адаптивні макети на Flexbox та адаптивній сітці CSS Grid repeat(auto-fit, minmax(280px, 1fr)), інтегровано шрифт Google Fonts 'Inter' та іконки Font Awesome 6.")
    add_p("5. Було проведено аудит та оптимізацію CSS: усунуто конфлікт шарів (layering bug) за допомогою isolation: isolate на блоці карти та z-index: 10000 на шапці сайту, захищено кнопки CTA від небажаного переносу рядків.")
    add_p("6. За допомогою інструментів Nu Html Checker, W3C CSS Validator та Lighthouse підтверджено бездоганну якість верстки з оцінками Accessibility: 100 / 100 та Best Practices: 100 / 100. Сформовано Промпт-паспорт та надано лаконічні відповіді на всі 14 контрольних запитань.")

    doc.save(out_docx)
    print(f"Successfully generated DOCX: {out_docx}")

if __name__ == "__main__":
    create_lab5_report()
