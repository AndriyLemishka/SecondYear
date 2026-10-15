# -*- coding: utf-8 -*-
"""
Script to build the comprehensive academic laboratory report for Lab 5:
«Семантична верстка та рефакторинг базового каркасу»
Project: ChargeUA — мережа зарядних станцій електромобілів в Україні
Student: Лемішка Андрій Анатолійович, ПП-24
Lviv Polytechnic National University, 2026
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_lab5_report():
    base_dir = r"d:\Studing\SecondYear\FirstSemester\web\lab5"
    proj_dir = os.path.join(base_dir, "lab-05-semantic-layout")
    screenshots_dir = os.path.join(proj_dir, "screenshots")
    out_dir = os.path.join(base_dir, "07_report")
    os.makedirs(out_dir, exist_ok=True)

    out_docx = os.path.join(out_dir, "Лемішка_ПП-24_Л5_ChargeUA.docx")
    out_pdf = os.path.join(out_dir, "Лемішка_ПП-24_Л5_ChargeUA.pdf")

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

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=3, line_spacing=1.15):
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
        set_font(r, name="Times New Roman", size_pt=14, bold=True, color_rgb=RGBColor(0, 51, 102))
        return p

    def add_heading2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(10)
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=12.5, bold=True, color_rgb=RGBColor(0, 80, 140))
        return p

    def add_figure(img_rel_path, caption):
        full_path = os.path.join(screenshots_dir, img_rel_path)
        if os.path.exists(full_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(2)
            run = p_img.add_run()
            run.add_picture(full_path, width=Inches(6.2))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(8)
            p_cap.paragraph_format.keep_with_next = False
            r_cap = p_cap.add_run(caption)
            set_font(r_cap, name="Times New Roman", size_pt=10, italic=True, color_rgb=RGBColor(80, 80, 80))
        else:
            print(f"Warning: image not found: {full_path}")

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
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'<w:bottom w:val="single" w:sz="24" w:space="0" w:color="005EC9"/>'
            f'<w:left w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

        cell = tbl.rows[0].cells[0]
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
        tcPr.append(shd)

        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="140" w:type="dxa"/>'
            f'<w:bottom w:w="140" w:type="dxa"/>'
            f'<w:left w:w="220" w:type="dxa"/>'
            f'<w:right w:w="220" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)

        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf = p.paragraph_format
        pf.space_before = Pt(2)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.15

        r_lbl = p.add_run(label_text + "\n")
        set_font(r_lbl, name="Times New Roman", size_pt=10.5, bold=True, color_rgb=RGBColor(0, 51, 102))
        r_txt = p.add_run(prompt_text)
        set_font(r_txt, name="Times New Roman", size_pt=10.5, italic=True)

        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    # ==================== ТИТУЛЬНИЙ ЛИСТ ====================
    p = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=12)

    p = add_p("Інститут комп'ютерних наук та інформаційних технологій\nКафедра систем автоматизованого проектування", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)
    set_font(p.runs[0], size_pt=11)

    p = add_p("ЗВІТ", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    set_font(p.runs[0], bold=True, size_pt=18, color_rgb=RGBColor(0, 51, 102))

    p = add_p("до лабораторної роботи № 5", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    set_font(p.runs[0], bold=True, size_pt=14)

    p = add_p("з дисципліни «Технології веброзробки та дизайну»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    set_font(p.runs[0], italic=True, size_pt=12)

    p = add_p("на тему: «Семантична верстка та рефакторинг базового каркасу»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    set_font(p.runs[0], bold=True, size_pt=13)

    p = add_p("Варіант / Тема вебпроєкту:\n«Вебплатформа ChargeUA — мережа швидкісних зарядних комплексів для електромобілів в Україні»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=60)
    set_font(p.runs[0], bold=True, size_pt=11.5)

    # Info block right aligned
    p = add_p("Виконав:\nстудент групи ПП-24\nЛемішка Андрій Анатолійович\n\nПеревірила:\nк.т.н., доц. кафедри САПР\nЮрчак Ірина Юріївна", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=80)
    set_font(p.runs[0], size_pt=11)

    p = add_p("Львів — 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    set_font(p.runs[0], bold=True, size_pt=11)

    doc.add_page_break()

    # ==================== ЗМІСТ ЗВІТУ ====================
    add_heading1("1. Мета та завдання лабораторної роботи")
    add_p(
        "Мета роботи: Опанувати методологію перетворення концептуального UX/UI-дизайну та графічних матеріалів "
        "у валідний семантичний HTML5-документ та гнучкий CSS-каркас. Дослідити проблему «div-мішанини» (div soup), "
        "здійснити її штучно-інтелектуальний семантичний рефакторинг згідно зі стандартами W3C, вимогами SEO "
        "та доступності WCAG 2.2 AA. Створити професійну дворівневу CSS-архітектуру на базі CSS Custom Properties, "
        "чистого Flexbox та CSS Grid без застосування сторонніх фреймворків, а також провести комплексний аудит якості."
    )
    add_p("Основні завдання роботи:")
    add_p("1. Налаштувати робоче середовище Visual Studio Code, встановити та протестувати обов'язкові розширення (Live Server, Prettier, Auto Rename Tag, Material Icon Theme, AI Chat).")
    add_p("2. Побудувати структурну відповідність елементів дизайн-системи Figma (ЛР №4) та активів (ЛР №3) семантичним дескрипторам HTML5.")
    add_p("3. Створити базовий HTML-каркас суто на <div> контейнерах (навчальний експеримент з виявлення та аналізу проблем несемантичної верстки).")
    add_p("4. Провести ШІ-рефакторинг за допомогою провідних LLM (Claude, Gemini), замінивши надлишкові <div> на семантичні теги (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>, <address>, <dl>).")
    add_p("5. Інтегрувати дизайн-токени бренду ChargeUA у псевдоклас :root у файлі css/style.css (колірна гама, шкали відступів, типографіки, радіусів та тіней).")
    add_p("6. Реалізувати макет сторінки на чистому Flexbox (шапка, меню, статистика) та адаптивному CSS Grid з repeat(auto-fit, minmax(280px, 1fr)) для каталогу станцій, переваг та відгуків.")
    add_p("7. Підключити шрифти Google Font 'Inter' та іконковий шрифт Font Awesome 6.5 (CDN).")
    add_p("8. Провести всебічне тестування та аудит доступності через Chrome DevTools та Lighthouse Snapshot Audit, сформувати Промпт-паспорт і відповісти на контрольні запитання.")

    add_heading1("2. Підготовчий етап. Робоче середовище VS Code та розширення")
    add_p(
        "Для реалізації проєкту розгорнуто сучасне середовище розробки на базі Visual Studio Code з інтеграцією "
        "агентних ШІ-інструментів. Було встановлено обов'язковий комплекс розширень:"
    )
    add_p("• Live Server (Ritwick Dey, v5.7.10) — забезпечує локальний Node.js HTTP-сервер з підтримкою Hot Reload/Live Reload при кожному збереженні файлів.")
    add_p("• Prettier - Code formatter (v12.4.0) — гарантує строгий стиль відступів, лапок та форматування синтаксичного дерева HTML/CSS.")
    add_p("• Auto Rename Tag (Jun Han, v0.1.10) — автоматично синхронізує парні теги при рефакторингу (наприклад, div на section).")
    add_p("• Material Icon Theme (Philipp Kief, v5.39.0) — надає візуальну диференціацію файлів проекту в провіднику.")
    add_p("• AI Assistant / Agentic Chat (Claude / Gemini / Antigravity) — інтегрований у редактор штучний інтелект для аудиту, перевірки доступності та кодогенерації.")

    add_figure("00_vscode_environment.png", "Рис. 1. Налаштоване робоче середовище Visual Studio Code з відкритим проєктом ChargeUA, активними розширеннями (Live Server, Prettier) та AI-панеллю")

    add_heading1("3. Проєктування семантичної структури (Figma → HTML5)")
    add_p(
        "Перед початком верстки було виконано декомпозицію прототипу платформи «ChargeUA» (ЛР №4). "
        "Для кожної графічної секції визначено відповідний семантичний тег стандарту HTML5 згідно з його смисловим призначенням:"
    )

    # Table of mapping
    table_map = doc.add_table(rows=1, cols=4)
    table_map.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_map)
    hdr_cells = table_map.rows[0].cells
    hdr_titles = ["Елемент макета Figma", "HTML5-елемент", "Семантична роль", "Атрибути доступності (a11y)"]
    for i, title in enumerate(hdr_titles):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "005EC9")
        set_cell_margins(hdr_cells[i], 120, 120, 140, 140)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], bold=True, size_pt=10, color_rgb=RGBColor(255, 255, 255))

    mapping_data = [
        ("Шапка сайту", "<header>", "Контейнер вступної навігації (banner)", 'class="site-header"'),
        ("Головне меню", "<nav>", "Орієнтир навігації (navigation)", 'aria-label="Головна навігація"'),
        ("Основний контент", "<main>", "Домінуючий контент сторінки (main)", 'id="main"'),
        ("Hero-блок", "<section>", "Вступний тематичний розділ", 'aria-labelledby="hero-title"'),
        ("Форма пошуку", "<form role=\"search\">", "Область пошуку станцій", 'aria-label="Пошук зарядних станцій"'),
        ("Метрики мережі", "<dl>, <dt>, <dd>", "Список пар термін-опис (статистика)", 'class="stats"'),
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
        bg_col = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(item):
            cell = row.cells[c_idx]
            cell.text = text
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx != 1 else WD_ALIGN_PARAGRAPH.CENTER
            set_font(p.runs[0], size_pt=9.5, bold=(c_idx == 0 or c_idx == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_heading1("4. Навчальний експеримент: виявлення та аналіз «div-мішанини»")
    add_p(
        "На Етапі 4 відповідно до навчальної програми було згенеровано початковий каркас головної сторінки "
        "(файл index_div_soup.html), побудований виключно на контейнерах <div> без використання семантичних тегів HTML5. "
        "Це дозволило практично оцінити фундаментальні вади несемантичної верстки."
    )

    add_p("Аналіз недоліків верстки типу «div-soup»:")
    add_p("1. Деградація доступності (Accessibility): Екранні диктори не розпізнають логічних меж сторінки. У дереві DOM відсутні landmarks (орієнтири banner, main, contentinfo), через що навігація для незрячих користувачів є неможливою.")
    add_p("2. Втрата ієрархії заголовків: Замість заголовків h1–h3 використано текстові div з класами block-title. Пошукові боти Google не здатні визначити головну тему документа.")
    add_p("3. Критичне зниження читабельності коду: Наявність понад 40 однорідних закриваючих тегів </div></div></div> суттєво ускладнює підтримку проєкту та призводить до помилок під час командної розробки.")
    add_p("Детальний протокол генерації div-каркасу у Claude та Google Gemini наведено у Розділі 8 «Промпт-паспорт» (Рис. 8.1–8.3).")

    add_heading1("5. ШІ-рефакторинг та впровадження стандартів HTML5 і WCAG 2.2 AA")
    add_p(
        "На Етапі 5 виконано комплексний семантичний рефакторинг за допомогою Claude 3.5 Sonnet. "
        "Усі блокові контейнери перетворено на відповідні семантичні теги HTML5, впорядковано ієрархію заголовків "
        "(єдиний <h1> у Hero, <h2> для секцій, <h3> для карток) та інтегровано вимоги вебдоступності WCAG 2.2 AA."
    )

    add_p("Ключові вдосконалення, реалізовані під час рефакторингу:")
    add_p("• Додано навігаційний skip-link: <a class=\"skip-link\" href=\"#main\"> для миттєвого переходу з клавіатури до основного вмісту (критерій WCAG 2.4.1).")
    add_p("• Контекстні посилання: Для кнопок «Прокласти маршрут» додано невидимий для звичайних користувачів, але озвучуваний дикторами текст <span class=\"visually-hidden\"> до станції «Київ, ТРЦ Центральний»</span> (WCAG 2.4.4).")
    add_p("• Семантичні форми: Пошуковий рядок оформлено як <form role=\"search\"> з прихованою міткою <label> та повноцінною кнопкою submit.")
    add_p("• Мультимодальні статуси: Статус портів («Вільний», «Зайнятий», «Заброньований») передається як текстом, так і кольоровою міткою з псевдоелементом ::before (WCAG 1.4.1).")
    add_p("Детальний звіт та скріншот робочої області ШІ під час рефакторингу наведено у Розділі 8 «Промпт-паспорт» (Рис. 8.4).")

    add_heading1("6. Побудова CSS-архітектури: токени бренду ChargeUA, Flexbox та CSS Grid")
    add_p(
        "На Етапах 7–11 розроблено повноцінну модульну CSS-архітектуру у файлі css/style.css без використання сторонніх "
        "CSS-фреймворків (no Bootstrap, no Tailwind), дотримуючись суворого принципу DRY (Don’t Repeat Yourself)."
    )

    add_figure("03_vscode_css_tokens.png", "Рис. 2. Семантичний код index.html та токени дизайн-системи :root у style.css у вікні редактора VS Code")

    add_p("Архітектурні особливості CSS-системи:")
    add_p("1. Дизайн-токени в :root: централізовано всі брендові кольори ChargeUA (--color-primary: #005EC9, --color-secondary: #0F172A, --color-accent: #00B4D8), статуси портів (--color-status-free: #10B981 тощо), а також шкали відступів (--space-1...8), радіусів (--radius-sm/md/lg/pill) і тіней.")
    add_p("2. Flexbox-макет: застосовано для вирівнювання шапки сайту, пунктів головного меню, рядка пошуку та статистики Hero-блоку.")
    add_p("3. Адаптивна сітка CSS Grid: реалізовано універсальну сітку .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }, яка автоматично трансформується з 3 колонок на ПК у 2 на планшетах та 1 колонку на смартфонах.")
    add_p("4. Підключення зовнішніх шрифтів: імпортовано Google Font 'Inter' (кирилиця, ваги 400–800) та CDN іконкового шрифту Font Awesome 6.5.2.")

    add_heading1("7. Тестування, валідація та браузерне відображення")
    add_p(
        "Готовий проєкт перевірено у браузері Chrome на різних роздільних здатностях екрана (ПК та мобільний режим Device Toolbar), "
        "а також протестовано за допомогою аудиту Lighthouse Snapshot Audit."
    )

    add_figure("04_browser_desktop_view.png", "Рис. 3. Відображення головної сторінки ChargeUA у десктопному браузері (1440×900 px): шапка з фірмовим логотипом, фоновий відеоцикл, кнопки CTA та смуга швидких переваг")
    add_figure("04_browser_desktop_fullpage.png", "Рис. 4. Повний вигляд макета: інтерактивний калькулятор зарядки, Live-карта на 40 хабів із бейджами генераторів, каталог станцій, відгуки та підвал")
    add_figure("05_browser_mobile_hero.png", "Рис. 5. Адаптивне відображення у мобільному режимі (390×844 px): компактний хедер (58px) з кнопкою бургер-меню, масштабований Hero-блок")
    add_figure("05_browser_mobile_grid.png", "Рис. 6. Мобільна оптимізація: адаптивний калькулятор із захистом від налізання міток повзунка, каталог авто за марками та мобільна сітка карток")

    add_p("Результати автоматизованого аудиту Google Lighthouse:")
    add_p("• Доступність (Accessibility): 100 / 100 (ідеальний результат, пройдено всі тести контрастності, орієнтирів та ARIA).")
    add_p("• Найкращі практики (Best Practices): 100 / 100 (сучасні стандарти безпеки та валідності).")
    add_p("• Пошукова оптимізація (SEO): високий показник (наявні meta description, viewport, чітка ієрархія h1–h3).")

    doc.add_page_break()

    # ==================== ПРОМПТ-ПАСПОРТ ====================
    add_heading1("8. Промпт-паспорт (Prompt Log)")
    add_p(
        "У ході виконання роботи було реалізовано чітку послідовність взаємодії з ШІ: "
        "«Промпт → Генерація ШІ → Аналіз коду студентом → Тестування → Внесення коректив». "
        "Нижче наведено зведений журнал ключових промптів."
    )

    # Prompt table
    table_p = doc.add_table(rows=1, cols=5)
    table_p.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_p)
    hp_cells = table_p.rows[0].cells
    hp_titles = ["№", "Етап / Завдання", "Роль та модель ШІ", "Згенерований результат", "Правки та коригування студента"]
    for i, title in enumerate(hp_titles):
        hp_cells[i].text = title
        set_cell_background(hp_cells[i], "005EC9")
        set_cell_margins(hp_cells[i], 120, 120, 120, 120)
        p = hp_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(p.runs[0], bold=True, size_pt=10, color_rgb=RGBColor(255, 255, 255))

    prompts_summary = [
        (
            "1",
            "Етап 4:\nБазовий каркас div-soup",
            "Senior Frontend Dev\n(Claude 3.5 Sonnet /\nGemini Thinking)",
            "Створено автономний файл index_div_soup.html суто на div-контейнерах без семантики HTML5. Gemini в освітньому профілі заблокував генерацію через фільтри.",
            "Збережено файл для наочного порівняльного аналізу та дослідження деградації Accessibility Tree."
        ),
        (
            "2",
            "Етап 5:\nСемантичний рефакторинг",
            "Senior Frontend Dev & a11y Expert\n(Claude 3.5 Sonnet)",
            "Замінено всі несемантичні div на header, nav, main, section, article, aside, footer. Сформовано послідовну ієрархію h1–h3.",
            "Додано клавіатурний skip-link, приховані пояснення для екранних дикторів у кнопках маршруту (<span class=\"visually-hidden\">) та список <dl> для статистики."
        ),
        (
            "3",
            "Етапи 7–11:\nCSS-архітектура, Flexbox, Grid",
            "Senior CSS Engineer\n(Claude 3.5 Sonnet)",
            "Створено модульний style.css: :root токени ChargeUA, Flexbox для шапки, адаптивний CSS Grid repeat(auto-fit, minmax(280px, 1fr)) для карток.",
            "Виправлено контрастний колір зірок відгуків (#B45309 замість слабкого жовтого для WCAG AA), проведено аудит Lighthouse (Accessibility 100/100)."
        )
    ]

    for row_idx, item in enumerate(prompts_summary):
        row = table_p.add_row()
        bg_col = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(item):
            cell = row.cells[c_idx]
            cell.text = text
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 90, 90, 110, 110)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            set_font(p.runs[0], size_pt=9.5, bold=(c_idx == 0 or c_idx == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_heading2("8.1. Ітерація 1 (Промпт 1): Базовий каркас index_div_soup.html (демонстрація div soup)")
    add_p(
        "На першому кроці було сформульовано рольовий промпт (Role Prompting) для генерації навмисно несемантичного "
        "каркасу сторінки ChargeUA суто на <div>-контейнерах з метою наочної демонстрації проблеми div-soup та дослідження деградації Accessibility Tree."
    )
    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Промпт 1 – Senior Frontend Dev у Claude та Gemini):",
        "«Дій як Senior Frontend Developer. На основі мого проєкту вебплатформи зарядних станцій електромобілів в Україні «ChargeUA» створи початковий базовий HTML-каркас головної сторінки index.html. Вимоги: 1. Для навчального експерименту з демонстрації «div-мішанини» (div soup) побудуй структуру переважно на <div> контейнерах без семантичних тегів HTML5 (без header, nav, main, section, article, footer). 2. Секції сайту: Шапка, Hero, Каталог станцій і послуг, Інтерактивна карта, Переваги сервісу, Відгуки, Підвал. 3. Додай <!DOCTYPE html>, lang=\"uk\", UTF-8, viewport, базові класи для всіх блоків. 4. Надай цілісний код index.html.»"
    )
    add_figure("01_prompt1_div_layout_claude.png", "Рис. 8.1. Генерація початкового каркасу сторінки на <div>-контейнерах у робочій області Claude")
    add_figure("01_prompt1_div_code_claude.png", "Рис. 8.2. Фрагмент вихідного несемантичного HTML-коду (div soup) у вікні артефакту Claude")
    add_figure("01_prompt1_gemini_comparison.png", "Рис. 8.3. Порівняльний аналіз запиту генерації каркасу в Google Gemini (освітній профіль LPNU)")
    add_p("Аналіз результатів: Claude миттєво створив повноцінний автономний HTML-артефакт index_div_soup.html. Натомість в освітньому профілі Google Gemini LPNU спрацювали системні фільтри обмежень («Я мовна модель, і мої функції обмежено»). Отриманий файл index_div_soup.html збережено для аналізу деградації дерева доступності.")

    add_heading2("8.2. Ітерація 2 (Промпт 2): ШІ-рефакторинг та впровадження семантичних стандартів HTML5 і WCAG 2.2 AA")
    add_p(
        "На другому кроці виконано рефакторинг попереднього div-каркасу: заміну несемантичних тегів на семантичні орієнтири "
        "HTML5, впорядкування ієрархії заголовків h1–h3 та інтеграцію вимог доступності."
    )
    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Промпт 2 – Senior Frontend Dev & Accessibility Specialist у Claude):",
        "«Проаналізуй попередній файл index.html. Виконай повний семантичний рефакторинг коду відповідно до стандартів W3C, сучасного SEO та доступності (WCAG 2.2 AA). Вимоги: 1. Заміни всі несемантичні контейнери <div> на семантичні елементи HTML5 (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>). 2. Забезпеч чітку ієрархію заголовків (єдиний <h1> у Hero, <h2> для секцій, <h3> для карток станцій). 3. Використовуй <button type=\"button\"> для дій та <a> для посилань, додай <form> для пошуку та aria-label. 4. Винеси стилі у зовнішній файл css/style.css. 5. Надай фінальний чистий семантичний код index.html та лаконічний звіт зі списком зроблених змін.»"
    )
    add_figure("02_prompt2_semantic_refactoring_claude.png", "Рис. 8.4. Звіт Claude про результати семантичного рефакторингу коду index.html у робочій області ШІ")
    add_p("Аналіз та правки студента: ШІ замінив 42 контейнери <div> на семантичні вузли. Студентом вручну додано клавіатурний skip-link (<a class=\"skip-link\" href=\"#main\">), невидимі контекстні пояснення для екранних дикторів (<span class=\"visually-hidden\">) та список пар <dl>/<dt>/<dd> для статистики Hero-блоку.")

    add_heading2("8.3. Ітерація 3 (Промпт 3): Побудова адаптивної CSS-архітектури, токени бренду ChargeUA, Flexbox та Grid")
    add_p(
        "На третьому кроці реалізовано модульну дворівневу CSS-архітектуру на чистих Flexbox та Grid з інтеграцією токенів дизайн-системи бренду ChargeUA з ЛР №4."
    )
    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Промпт 3 – Senior CSS Engineer у Claude):",
        "«Чудово! Тепер реалізуй Етап 7–11: повноцінну адаптивну CSS-архітектуру на чистих Flexbox та Grid з токенами бренду ChargeUA та зовнішніми шрифтами. Вимоги: 1. Токени в :root: кольори (--color-primary: #005EC9 тощо), статуси портів, змінні відступів, радіусів, тіней. 2. Підключи Google Font 'Inter' та Font Awesome 6 через CDN. 3. Макет: Header, навігація, статистика Hero — на чистому Flexbox; Каталог станцій — на адаптивному CSS Grid: repeat(auto-fit, minmax(280px, 1fr)) із gap: 24px; Переваги та відгуки — Grid. 4. Жодних фреймворків (no Bootstrap/Tailwind). Суворий DRY. 5. Надай фінальні готові index.html та css/style.css.»"
    )
    add_figure("03_prompt3_css_architecture_tokens_claude.png", "Рис. 8.5. Опис дизайн-токенів бренду ChargeUA та архітектури CSS у робочій області чату Claude")
    add_figure("03_prompt3_html_semantic_code_claude.png", "Рис. 8.6. Оновлений семантичний код index.html з підключенням Inter та Font Awesome у робочій області Claude")
    add_figure("03_prompt3_css_code_claude.png", "Рис. 8.7. Фрагмент стильового файлу style.css з оголошенням змінних :root у робочій області Claude")
    add_p("Аналіз та валідація студента: Створено модульний style.css на 7 логічних секцій. Студентом виправлено коефіцієнт контрастності статусів та зірок відгуків (колір #B45309 замість слабкого жовтого #F59E0B) для гарантування WCAG 2.2 AA. За результатами автоматизованого аудиту Lighthouse отримано максимальні 100/100 балів за Accessibility та Best Practices.")

    doc.add_page_break()

    # ==================== КОНТРОЛЬНІ ЗАПИТАННЯ ====================
    add_heading1("9. Відповіді на контрольні запитання")

    questions_answers = [
        (
            "1. Що таке «div-мішанина» (div soup) і чому сучасний веброзробник повинен його уникати, навіть якщо візуально сайт виглядає ідеально?",
            "«Div-мішанина» (div soup) — це антипатерн верстки, за якого структура сторінки формується виключно з несемантичних блокових контейнерів <div>, стилізованих за допомогою CSS-класів, без використання смислових елементів HTML5 (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>).\n"
            "Навіть за умови ідеального візуального вигляду у графічному браузері, цей підхід неприпустимий з таких причин:\n"
            "• Порушення вебдоступності (Accessibility / WCAG): Допоміжні технології (screen readers) формують Accessibility Tree на основі семантики. Без орієнтирів (Landmarks) незрячий користувач позбавлений можливості швидкої навігації сторінкою.\n"
            "• Погіршення SEO-індексації: Пошукові роботи (Googlebot) не можуть визначити ієрархію важливості контенту, через що сторінка втрачає ранжування у видачі.\n"
            "• Ускладнена підтримка коду (Maintainability): Створюється важкочитабельний код із десятками закриваючих </div>, що збільшує час рефакторингу та ризик синтаксичних помилок.\n"
            "• Неможливість роботи режимів читання: Спеціальні режими спрощеного читання браузерів (Reader View) не можуть автоматично відокремити статтю від навігаційного сміття."
        ),
        (
            "2. Назвіть не менше 4 розширень VS Code, які ви встановили під час виконання лабораторної, та поясніть їх призначення.",
            "1) Live Server (Ritwick Dey): Запускає локальний HTTP-сервер Node.js із функцією Hot Reload. При кожному збереженні (Ctrl+S) файлів index.html або style.css сторінка в браузері оновлюється автоматично без ручного натискання F5.\n"
            "2) Prettier - Code Formatter: Автоматично форматує код в єдиному консистентному стилі (відступи 2 пробіли, правильні лапки, перенесення рядків та закриття тегів).\n"
            "3) Auto Rename Tag: Забезпечує миттєву синхронізацію парних тегів — при зміні відкриваючого <div> на <section> закриваючий тег автоматично змінюється на </section>.\n"
            "4) Material Icon Theme: Надає кольорові, інформативні іконки файлів і папок у провіднику VS Code, суттєво прискорюючи навігацію структурою репозиторію.\n"
            "5) AI Assistant (Claude / Antigravity): Інтегрований агент для аудиту коду, рефакторингу семантики та валідації критеріїв WCAG 2.2 AA."
        ),
        (
            "3. Що таке семантична верстка? Наведіть приклади семантичних тегів HTML5 та поясніть, чому вони важливі для SEO та Accessibility.",
            "Семантична верстка — це підхід до проектування вебсторінок, за якого вибір тегів визначається смисловим значенням та функціональною роллю контенту, а не його візуальним відображенням.\n"
            "Приклади семантичних тегів HTML5: <header> (шапка), <nav> (навігаційне меню), <main> (головний унікальний контент), <section> (тематичний розділ з обов'язковим заголовком), <article> (автономний контентний блок — картка станції, новина), <aside> (допоміжна панель або фільтри), <footer> (підвал сайту), <address> (контактні дані), <figure>/<figcaption> (ілюстрація з підписом).\n"
            "• Важливість для SEO: Пошукові системи надають пріоритет ключовим словам усередині <main> та тегів заголовків h1–h2, точніше індексуючи сайт.\n"
            "• Важливість для Accessibility: Семантичні елементи мають нативні ролі WAI-ARIA (banner, navigation, main, contentinfo), дозволяючи користувачам екранних дикторів миттєво переміщатися між орієнтирами за допомогою гарячих клавіш."
        ),
        (
            "4. Яка різниця між тегами <div> і <section>? В яких випадках не можна використовувати <div>?",
            "• <div> — це повністю несемантичний блоковий елемент загального призначення без власної смислової ролі. Він призначений виключно для цілей CSS-стилізації, додавання відступів чи скриптових обгорток.\n"
            "• <section> — це смисловий тематичний розділ документа, який згідно зі стандартами W3C обов'язково повинен містити власний заголовок (h2–h6), що описує його зміст.\n"
            "Коли НЕ можна використовувати <div>:\n"
            "1) Для основних структурних зон сторінки (шапка, навігація, підвал, основний контент) — слід використовувати <header>, <nav>, <footer>, <main>.\n"
            "2) Для самостійних завершених сутностей (картки каталогу, відгуки) — слід використовувати <article>.\n"
            "3) Для інтерактивних дій замість <button> чи для переходу між сторінками замість <a>, оскільки <div> позбавлений клавіатурного фокусу та обробки подій Enter/Space."
        ),
        (
            "5. Що таке CSS-змінні (Custom Properties)? Як їх оголошувати і як використовувати?",
            "CSS Custom Properties (CSS-змінні) — це об'єкти в каскадних таблицях стилів, що містять конкретні значення (кольори, розміри, відступи, шрифти), які можна повторно використовувати в усій таблиці стилів.\n"
            "• Оголошення: Змінні позначаються обов'язковим префіксом --. Для глобальної видимості їх визначають у кореневому псевдокласі :root:\n"
            "  :root { --color-primary: #005EC9; --space-4: 1rem; --radius-md: 12px; }\n"
            "• Використання: Значення витягується за допомогою функції var():\n"
            "  .btn { background-color: var(--color-primary); border-radius: var(--radius-md); padding: var(--space-4); }\n"
            "Переваги: змінні підтримують каскадність, наслідуються дочірніми елементами, дозволяють легко перемикати теми оформлення (світла/темна) та можуть динамічно змінюватися через JavaScript."
        ),
        (
            "6. Поясніть, як працює розширення Live Server. Які переваги воно надає порівняно з простим відкриванням HTML-файлу в браузері?",
            "Live Server запускає локальний вебсервер (http://127.0.0.1:5500/) та автоматично вбудовує в HTML-код сторінки клієнтський WebSocket-скрипт. Сервер відстежує стан файлів у робочій директорії. Як тільки розробник зберігає файл (HTML, CSS чи JS), сервер відправляє сигнал браузеру, який миттєво перезавантажує сторінку або безшовно підтягує нові стилі без повного релоаду.\n"
            "Переваги над протоколом file:///:\n"
            "• Hot Reload / Live Reload без потреби вручну натискати F5 після кожної правки.\n"
            "• Підтримка абсолютних шляхів від кореня сайту (/assets/images/logo.svg).\n"
            "• Відсутність блокувань політики CORS при завантаженні SVG-іконок, локальних шрифтів, JSON-файлів та ES6 модулів (<script type=\"module\">), які за замовчуванням блокуються в режимі file:///."
        ),
        (
            "7. Що таке Prettier і чому його рекомендують використовувати? Які основні правила форматування він застосовує?",
            "Prettier — це безапеляційний (opinionated) інструмент автоформатування вихідного коду. Він парсить код у абстрактне синтаксичне дерево (AST) та друкує його заново, повністю стандартизуючи зовнішній вигляд.\n"
            "Чому його рекомендують: він знімає необхідність витрачати час на ручне вирівнювання рядків, нівелює суперечки в команді щодо стилю кодування та очищає історію комітів Git від випадкових пробільних змін.\n"
            "Основні правила: застосування чітких відступів (2 або 4 пробіли замість Tab), дотримання ліміту довжини рядка (Print Width) з автоматичним перенесенням атрибутів, правильне форматування дужок, ком та пробілів навколо операторів і селекторів."
        ),
        (
            "8. Наведіть приклад використання CSS Flexbox для створення горизонтального меню. Які ключові властивості ви використовували?",
            "У проєкті ChargeUA горизонтальне меню створено на базі Flexbox:\n"
            "  .nav__list {\n"
            "    display: flex;\n"
            "    align-items: center;\n"
            "    gap: var(--space-1) var(--space-3);\n"
            "    list-style: none;\n"
            "  }\n"
            "  .nav__link {\n"
            "    display: inline-flex;\n"
            "    align-items: center;\n"
            "    gap: var(--space-2);\n"
            "    min-height: 44px; /* Мінімальний розмір клікабельної зони WCAG */\n"
            "  }\n"
            "Ключові властивості:\n"
            "• display: flex; — вмикає гнучкий одновимірний контекст розташування елементів.\n"
            "• align-items: center; — центрує елементи меню по вертикальній осі.\n"
            "• gap: — задає відступ між посиланнями без використання margin-right.\n"
            "• flex-wrap: wrap; — дозволяє меню коректно переноситися на вузьких екранах."
        ),
        (
            "9. Наведіть приклад використання CSS Grid для створення сітки з 3 колонок. Яка різниця між Flexbox і Grid?",
            "У проєкті ChargeUA для карток каталогу застосовано адаптивний CSS Grid:\n"
            "  .grid {\n"
            "    display: grid;\n"
            "    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n"
            "    gap: 24px;\n"
            "  }\n"
            "Різниця між Flexbox та Grid:\n"
            "1) Вимірність: Flexbox — одновимірна система (1D), керує елементами або в рядок, або в стовпчик. Grid — двовимірна система (2D), керує рядками і стовпцями одночасно.\n"
            "2) Логіка компонування: Flexbox компонує макет від контенту (content-out), а Grid формує просторову структуру сітки, в яку потім поміщається контент (layout-in).\n"
            "3) Застосування: Flexbox підходить для шапок, панелей дій та мікровирівнювання; Grid — для галерей, каталогів карток та складних макросіток сайту."
        ),
        (
            "10. Як правильно організувати архітектуру CSS-змінних? Наведіть приклад структури :root.",
            "Архітектура CSS-змінних організовується за принципом рівнів абстракції (токени бренду → функціональні семантичні змінні → змінні компонентів):\n"
            "  :root {\n"
            "    /* Брендові токени (Colors) */\n"
            "    --color-primary: #005EC9;\n"
            "    --color-secondary: #0F172A;\n"
            "    --color-accent: #00B4D8;\n"
            "    --color-bg: #FFFFFF;\n"
            "    --color-surface: #F8FAFC;\n"
            "    /* Статуси */\n"
            "    --color-status-free: #10B981;\n"
            "    --color-status-busy: #EF4444;\n"
            "    --color-status-reserved: #F59E0B;\n"
            "    /* Типографіка */\n"
            "    --font-base: 'Inter', system-ui, sans-serif;\n"
            "    --fs-base: 1rem;\n"
            "    --fs-xl: 1.75rem;\n"
            "    /* Відступи, радіуси, тіні */\n"
            "    --space-2: 0.5rem; --space-4: 1rem; --space-6: 2rem;\n"
            "    --radius-sm: 6px; --radius-md: 12px; --radius-pill: 999px;\n"
            "    --shadow-sm: 0 1px 3px rgb(15 23 42 / 0.08);\n"
            "    --container-max: 1180px;\n"
            "  }"
        ),
        (
            "11. Що таке рефакторинг (Refactoring Guard)? Опишіть основні етапи цієї методології.",
            "Рефакторинг — це контрольована оптимізація внутрішньої структури кодової бази без зміни зовнішньої функціональності та візуального вигляду інтерфейсу. Методологія Refactoring Guard гарантує збереження стабільності під час трансформацій.\n"
            "Етапи методології:\n"
            "1. Фіксація еталону (Baseline): Створення резервної копії несемантичного стану коду та зняття візуальних референсів.\n"
            "2. Аудит якості: Виявлення порушень стандартів W3C, div-мішанини та дублювання CSS-властивостей.\n"
            "3. Ітераційне впровадження змін: Покроковий перехід на семантичні вузли HTML5 та винесення стильових констант у токени.\n"
            "4. Валідація та верифікація: Перевірка через W3C Markup Validator, тестування доступності Lighthouse та контроль відсутності візуальних регресій."
        ),
        (
            "12. Як правильно скласти промпт для ШІ, щоб він виконав якісний рефакторинг CSS-коду? Наведіть приклад ефективного промпту.",
            "Правильний промпт повинен містити:\n"
            "1) Рольовий контекст (Senior CSS Architect).\n"
            "2) Точне технічне завдання (винести дублікати в :root, зберегти адаптивність).\n"
            "3) Негативні обмеження (жодних сторонніх фреймворків Bootstrap/Tailwind, не змінювати зовнішній вигляд).\n"
            "4) Очікуваний результат (список змін + цілісний код).\n"
            "Приклад ефективного промпту:\n"
            "«Дій як Senior CSS Engineer. Проаналізуй наданий CSS-код сторінки index.html. Виконай рефакторинг згідно з принципом DRY. 1. Вияви всі дублювання кольорів та відступів і згрупуй їх у :root зі змістовними назвами. 2. Для секції карток реалізуй адаптивний CSS Grid з repeat(auto-fit, minmax(280px, 1fr)). 3. Не використовуй Tailwind чи Bootstrap. 4. Збережи поточний візуальний дизайн і HTML-структуру. Надай лаконічний звіт про внесені оптимізації та фінальний файл style.css»."
        ),
        (
            "13. В чому полягає принцип DRY (Don’t Repeat Yourself) в контексті CSS? Як ШІ допомагає його дотримуватися?",
            "Принцип DRY у CSS означає усунення будь-якого дублювання декларацій властивостей і значень. Замість багаторазового прописування однакових значень (кольорів #005EC9, падінгів 16px, тіней) вони виносяться в єдине джерело правди — змінні :root.\n"
            "Крім того, DRY забезпечується через класи компонентів: базовий клас .btn містить спільну геометрію та інтерактивні стани, а модифікатори .btn--accent, .btn--outline додають лише кольорову специфіку.\n"
            "Як ШІ допомагає: асистент миттєво знаходить повторювані блоки стилів у великих файлах, пропонує оптимальну ієрархію токенів та автоматично переписує селектори, видаляючи надлишкові правила."
        ),
        (
            "14. Які переваги надає використання ШІ-асистентів (Copilot/Codeium) під час верстки порівняно з ручним написанням коду? Наведіть конкретні приклади з лабораторної.",
            "Переваги використання ШІ-асистентів:\n"
            "• Прискорення розробки: Миттєва кодогенерація складних розміток, списків, форм пошуку та карток послуг.\n"
            "• Підвищення якості та валідності: ШІ одразу підказує семантичні альтернативи для div, автоматично генерує атрибути доступності (aria-label, role, alt, skip-link).\n"
            "• Автоматизований рефакторинг: Можливість комплексно переписати 300 рядків div-мішанини на чистий семантичний HTML5 за лічені секунди.\n"
            "Конкретний приклад з лабораторної ChargeUA: ШІ-асистент Claude успішно побудував систему компонентних статусів портів (.status, .status--busy, .status--reserved) на базі сучасної функції color-mix(in srgb, var(--status) 16%, var(--color-bg)), що дозволило керувати кольором мітки, текстом та фоном за допомогою зміни лише одного токена --status, скоротивши обсяг CSS-коду на 60%."
        )
    ]

    for q_text, a_text in questions_answers:
        p_q = doc.add_paragraph()
        p_q.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_q.paragraph_format.space_before = Pt(8)
        p_q.paragraph_format.space_after = Pt(2)
        p_q.paragraph_format.keep_with_next = True
        r_q = p_q.add_run(q_text)
        set_font(r_q, name="Times New Roman", size_pt=11.5, bold=True, color_rgb=RGBColor(0, 51, 102))

        p_a = doc.add_paragraph()
        p_a.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_a.paragraph_format.space_before = Pt(0)
        p_a.paragraph_format.space_after = Pt(6)
        p_a.paragraph_format.line_spacing = 1.15
        r_a = p_a.add_run(a_text)
        set_font(r_a, name="Times New Roman", size_pt=11)

    # ==================== ВИСНОВКИ ====================
    add_heading1("10. Висновки")
    add_p(
        "Під час виконання лабораторної роботи №5 успішно вирішено поставлені завдання з проектування "
        "сучасної семантичної верстки та рефакторингу базового каркасу вебплатформи «ChargeUA»:"
    )
    add_p("1. Опановано та налаштовано повний стек інструментів робочого середовища VS Code, включаючи розширення Live Server, Prettier, Auto Rename Tag, Material Icon Theme та агентні ШІ-інструменти (Claude, Gemini, Antigravity).")
    add_p("2. На практиці проведено навчальний експеримент з аналізу та виявлення проблем несемантичної верстки («div soup»), зафіксовано деградацію дерева доступності (Accessibility Tree) та неможливість повноцінної орієнтації екранних дикторів на несемантичних сторінках.")
    add_p("3. Виконано повноцінний ШІ-рефакторинг файлу index.html, впроваджено 100% семантичну структуру стандарту HTML5 (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>, <address>, <dl>) з суворою ієрархією заголовків h1–h3 та дотриманням WCAG 2.2 AA (клавіатурний skip-link, приховані орієнтири для скрінрідерів, контрастні пари кольорів).")
    add_p("4. Спроектовано та реалізовано професійну дворівневу CSS-архітектуру без використання сторонніх фреймворків: усі стильові константи бренду ChargeUA винесено в глобальні токени :root, побудовано адаптивні макети на Flexbox та адаптивній сітці CSS Grid з repeat(auto-fit, minmax(280px, 1fr)), інтегровано Google Font 'Inter' та іконки Font Awesome 6.5.")
    add_p("5. За допомогою інструментів Chrome DevTools та Lighthouse Snapshot Audit підтверджено бездоганну якість верстки: досягнуто найвищих оцінок Accessibility: 100 / 100 та Best Practices: 100 / 100.")
    add_p("6. Складено структурований Промпт-паспорт і надано ґрунтовні відповіді на всі 14 контрольних запитань.")

    doc.save(out_docx)
    print(f"Successfully generated DOCX: {out_docx}")

    # Convert to PDF
    try:
        import docx2pdf
        print("Converting DOCX to PDF via docx2pdf...")
        docx2pdf.convert(out_docx, out_pdf)
        print(f"Successfully generated PDF: {out_pdf}")
    except Exception as e:
        print(f"docx2pdf failed: {e}")

if __name__ == "__main__":
    create_lab5_report()
