import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_report():
    base_dir = r"d:\Studing\SecondYear\FirstSemester\web\lab1"
    template_path = os.path.join(base_dir, "лаб 1_backup.docx")
    output_path = os.path.join(base_dir, "Звіт_Лаб1_Лемішка_ChargeUA.docx")

    # Load template document to preserve exact styles, settings, and margins
    doc = docx.Document(template_path)

    # Clear existing body contents (paragraphs, tables) while retaining sectPr
    body = doc._body._body
    for el in list(body):
        if not el.tag.endswith('sectPr'):
            body.remove(el)

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

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=2, line_spacing=1.15, style="Normal"):
        p = doc.add_paragraph(style=style)
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
        p = doc.add_paragraph(style="Heading 1")
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(14)
        pf.space_after = Pt(6)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=16, bold=True)
        return p

    def add_heading3(text):
        p = doc.add_paragraph(style="Heading 3")
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf = p.paragraph_format
        pf.space_before = Pt(10)
        pf.space_after = Pt(4)
        pf.keep_with_next = True
        r = p.add_run(text)
        set_font(r, name="Times New Roman", size_pt=13, bold=True)
        return p

    def add_heading4(text):
        p = doc.add_paragraph(style="Heading 4")
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
        
        # borders: subtle light border with prominent bottom bar
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
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8F8F8"/>')
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
        
        r_lbl = p.add_run(label_text + " ")
        set_font(r_lbl, name="Times New Roman", size_pt=11, bold=True)
        r_txt = p.add_run(prompt_text)
        set_font(r_txt, name="Times New Roman", size_pt=11, italic=True)
        
        # Add a subtle empty spacing paragraph after callout table
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_image_with_caption(img_rel_path, caption_text, width_in=6.2):
        img_full_path = os.path.join(base_dir, img_rel_path)
        if not os.path.exists(img_full_path):
            print(f"WARNING: Image not found: {img_full_path}")
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
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption_text)
        set_font(r_cap, name="Times New Roman", size_pt=11, bold=True)

    print("Setup completed, building sections...")

    # =========================================================================
    # ТИТУЛЬНИЙ ЛИСТ
    # =========================================================================
    p0 = add_p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p0.runs[0], bold=True)

    p1 = add_p("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ \"ЛЬВІВСЬКА ПОЛІТЕХНІКА\"", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p1.runs[0], bold=True)

    p2 = add_p("Кафедра «Систем автоматизованого проектування»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6, line_spacing=1.0)
    set_font(p2.runs[0], bold=False)

    # University Emblem
    logo_path = os.path.join(base_dir, "extracted_images_sample", "rId7_image1.jpeg")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(6)
        r_logo = p_logo.add_run()
        r_logo.add_picture(logo_path, width=Inches(2.6))

    p_doc = add_p("Звіт", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=1, line_spacing=1.0)
    set_font(p_doc.runs[0], size_pt=14, bold=True)

    p_sub = add_p("до лабораторної роботи №1", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p_sub.runs[0], size_pt=12)

    p_disc = add_p("з дисципліни “Технології веб-розробки та дизайну”", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.0)
    set_font(p_disc.runs[0], size_pt=12)

    p_topic_lbl = add_p("на тему:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2, line_spacing=1.0)
    set_font(p_topic_lbl.runs[0], size_pt=12)

    p_topic = add_p("ШІ-асистенти та основи промпт-інжинірингу", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, line_spacing=1.0)
    set_font(p_topic.runs[0], size_pt=13, bold=True)

    p_proj = add_p("Тема проєкту: «Лендинг мережі зарядних станцій для електромобілів «ChargeUA» (веб-помічник та агрегатор станцій)»", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2, line_spacing=1.0)
    set_font(p_proj.runs[0], size_pt=12, bold=True)

    p_spec = add_p("Специфікація проєкту: інтерактивний калькулятор вартості зарядки з вибором моделі електромобіля (або введенням ємності батареї), відсотка заряду та тарифу, плюс карта зарядних станцій з відображенням потужності та актуальних цін", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12, line_spacing=1.0)
    set_font(p_spec.runs[0], size_pt=11, italic=True)

    # Right block: Author & Reviewer
    p_auth = add_p("Виконав:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=8, space_after=1, line_spacing=1.0)
    set_font(p_auth.runs[0], bold=True)
    p_gr = add_p("студент групи ПП-24", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=1, line_spacing=1.0)
    p_name = add_p("Лемішка Андрій Андрійович", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=2, line_spacing=1.0)
    set_font(p_name.runs[0], bold=True)
    p_rev_lbl = add_p("Перевірила:", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=1, line_spacing=1.0)
    set_font(p_rev_lbl.runs[0], bold=True)
    p_rev = add_p("Стефанович Т.О.", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=16, line_spacing=1.0)

    # City & Year
    p_city = add_p("Львів – 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=0, line_spacing=1.0)
    set_font(p_city.runs[0], size_pt=12)

    # Explicit page break
    p_city.runs[0].add_break(WD_BREAK.PAGE)

    # =========================================================================
    # МЕТА РОБОТИ
    # =========================================================================
    p_goal = add_p(align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=6, space_after=8, line_spacing=1.15)
    r_g1 = p_goal.add_run("Мета роботи: ")
    set_font(r_g1, bold=True)
    r_g2 = p_goal.add_run("Навчитися формулювати ефективні запити (системні, Few-Shot, Chain-of-Thought) для аналізу бізнес-ніші, збору трендів та формування первинної архітектури сайту. Опанувати синергію різних ШІ-моделей (ChatGPT, Claude, Grok), використовуючи їхні сильні сторони на різних етапах аналітики.")
    set_font(r_g2, bold=False)

    # =========================================================================
    # РОЗДІЛ 1. АНАЛІТИЧНИЙ БРИФ (ТРЕНДИ)
    # =========================================================================
    add_heading1("Розділ 1. Аналітичний бриф (Тренди)")

    add_heading3("Промпт-логи")

    p = add_p(space_before=4, space_after=2)
    r = p.add_run("Крок 1. Початковий системний запит (Моделі: ChatGPT, Claude, Grok)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Ти — Senior Business Analyst & UI/UX Expert з 15-річним досвідом розробки цифрових продуктів. Твоє завдання — допомогти мені спроектувати архітектуру та логіку для вебсайту за темою: Лендинг мережі зарядних станцій для електромобілів «ChargeUA». Специфікація: інтерактивний калькулятор вартості зарядки з вибором моделі електромобіля (або введенням ємності батареї), відсотка заряду та тарифу, плюс інтерактивна карта зарядних станцій з відображенням потужності конекторів (Type 2, CCS2, GBT, CHAdeMO), зайнятості та актуальних цін за кВт·год. Твої відповіді мають бути структурованими, технічно грамотними, без «води», в форматі професійних артефактів (таблиці, списки, markdown). Чи зрозуміла тобі твоя роль та специфікація проєкту?»")
    set_font(r2, italic=False)

    p = add_p(space_before=2, space_after=4)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Кожна модель успішно підтвердила свою роль Senior Business Analyst & UI/UX Expert, зафіксувала контекст проєкту «ChargeUA», ключові модулі (калькулятор і карту) та підтвердила готовність генерувати технічні артефакти.")
    set_font(r2)

    add_heading4("Запит до Grok (Аналіз ринку)")

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 1. Початковий запит (Модель: Grok)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Проаналізуй ринок вебсайтів та додатків для зарядних станцій електромобілів (EV charging networks, таких як Tesla Supercharger, Ionity, Yasno E-Mobility, EcoFactor, GO TO-U) за останні 6-12 місяців в Україні та світі. Які головні візуальні та функціональні тренди зараз домінують? Які інтерактивні функції очікують побачити водії електромобілів на сучасному лендингу? Виділи 5 ключових інсайтів простою, зрозумілою українською мовою без надмірних англіцизмів.»")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Отримано розгорнутий аналіз ринку з актуальними глобальними даними, але текст містив надмірну кількість неадаптованих англомовних термінів.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Забагато складних англомовних понять (Site Maps, roaming, sticky CTA, real-time connector occupancy), які ускладнюють сприйняття. Крім того, був недостатньо акцентований критичний для України фактор енергонезалежності (робота ЕЗС від генераторів під час вимкнень світла) та значна частка китайських електромобілів із портом GB/T.")
    set_font(r2)

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 2. Коригувальний запит (Модель: Grok)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Заміни складні англіцизми та терміни простими українськими словами (замість «Site Maps» — детальна схема паркомісць та стовпів, замість «роумінг» — перегляд станцій різних операторів на одній карті). Зроби текст максимально простим і зрозумілим, підкресливши специфіку України (наявність китайських портів GB/T та фактор енергонезалежності/роботи від генераторів).»")
    set_font(r2)

    p = add_p(space_before=2, space_after=6)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Сформовано остаточний адаптований варіант аналітичного брифу ринку зарядних сервісів, наведений нижче.")
    set_font(r2)

    add_heading3("Результат аналізу ринку (Розділ 1)")

    add_heading3("Що зараз добре працює у світі та в Україні")

    p = add_p(space_before=2, space_after=2)
    r = p.add_run("Як виглядають сучасні сайти")
    set_font(r, bold=True)

    items_ui = [
        ("Карта — центр усього інтерфейсу. ", "Майже всі сучасні цифрові рішення (Tesla, Ionity, PlugShare, Yasno E-Mobility, EcoFactor, GO TO-U) будують взаємодію навколо інтерактивної карти. Маркери станцій кодуються інтуїтивними кольорами: зелений — є вільні порти, жовтий — усі зайняті, червоний/сірий — станція тимчасово недоступна або вимкнена."),
        ("Деталізація на рівні окремого конектора. ", "Провідні мережі (зокрема Tesla у 2026 році) впровадили схематичні плани локацій з точним розташуванням кожного стовпа та індикацією його зайнятості. Це вже сприймається як стандарт якості."),
        ("Чистий, мінімалістичний та контрастний дизайн. ", "Багато вільного простору, великі контрастні кнопки (для комфортного читання з екрана на сонці), опційна темна тема за замовчуванням. Інформація про потужність, ціну за кВт·год і тип роз’єму виводиться одразу на картці станції без зайвих переходів."),
        ("Мобільний пріоритет (Mobile-First). ", "Сайти та веб-додатки оптимізовані під швидке керування однією рукою, оскільки основний сценарій використання — пошук зарядки водієм безпосередньо за кермом або на під'їзді до станції.")
    ]
    for b_title, b_desc in items_ui:
        p_item = add_p(space_before=1, space_after=2)
        r_b = p_item.add_run("• " + b_title)
        set_font(r_b, bold=True)
        r_d = p_item.add_run(b_desc)
        set_font(r_d)

    p = add_p(space_before=4, space_after=2)
    r = p.add_run("Що водії очікують від сервісу-помічника")
    set_font(r, bold=True)

    items_exp = [
        ("Живий статус зайнятості кожного роз’єму ", "із оновленням даних у реальному часі (кожні кілька хвилин)."),
        ("Швидкий та зручний відбір ", "за типами роз’ємів (Type 2, CCS2, GB/T, CHAdeMO), вихідною потужністю (AC до 22 кВт / швидкісні DC від 50 кВт) та тарифом."),
        ("Інтерактивний калькулятор ", "розрахунку вартості та тривалості зарядки на основі моделі електрокара або ємності його батареї та бажаного відсотка."),
        ("Прозору ціну за 1 кВт·год ", "без прихованих комісій за простій, а також можливість зіставити тарифи різних операторів."),
        ("Позначки енергонезалежності ", "— чітка індикація того, чи працює станція під час віялових або аварійних відключень світла за рахунок власного генератора чи накопичувача.")
    ]
    for b_title, b_desc in items_exp:
        p_item = add_p(space_before=1, space_after=2)
        r_b = p_item.add_run("• " + b_title)
        set_font(r_b, bold=True)
        r_d = p_item.add_run(b_desc)
        set_font(r_d)

    add_heading3("П’ять головних висновків")

    insights = [
        ("1. Карта з живим статусом — базова обов'язкова вимога.",
         "Якщо на сайті відсутня інтерактивна карта з кольоровими позначками зайнятості та доступності кожного конкретного порту — користувач практично миттєво залишає сервіс, оскільки не має впевненості у можливості зарядки."),
        ("2. Розрахунок вартості і часу зарядки став стандартом.",
         "Інтерактивний калькулятор знімає психологічний бар'єр тривожності запасу ходу (range anxiety): водій заздалегідь знає, скільки коштуватиме зарядка саме його моделі до 80% або 100% і скільки часу це триватиме."),
        ("3. Прозорість ціни та фільтри за конекторами є критичними.",
         "Автопарк електромобілів в Україні надзвичайно різноманітний (європейські авто з CCS2/Type 2, американські з адаптерами та величезна кількість авто з Китаю з портами GB/T). Водій прагне миттєво бачити лише ті станції, які підходять його роз'єму, та реальну вартість за кВт·год."),
        ("4. Енергонезалежність станцій та робота від генераторів.",
         "В умовах викликів енергосистеми України інформація про наявність резервного живлення (генераторів, промислових батарей) на станції є вирішальним фактором вибору локації для зарядки, що має бути винесено в окремий пріоритетний фільтр."),
        ("5. Агрегація даних різних операторів на одній платформі.",
         "Можливість бачити на єдиній карті станції Yasno, EcoFactor, GO TO-U та інших мереж із єдиним інтерфейсом розрахунку позбавляє користувача потреби перемикатися між багатьма розрізненими додатками, забезпечуючи високу лояльність до сервісу-агрегатора.")
    ]
    for in_title, in_desc in insights:
        p_in = add_p(space_before=2, space_after=1)
        r_t = p_in.add_run(in_title + "\n")
        set_font(r_t, bold=True)
        r_d = p_in.add_run(in_desc)
        set_font(r_d)

    # =========================================================================
    # РОЗДІЛ 2. АНАЛІЗ ЦІЛЬОВОЇ АУДИТОРІЇ (ЦА)
    # =========================================================================
    add_heading1("Розділ 2. Аналіз цільової аудиторії (ЦА)")

    add_heading4("Системний запит до моделі ШІ (Claude)")

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 1. Початковий системний запит (Модель: Claude)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«На основі раніше визначених трендів проаналізуй цільову аудиторію нашого сайту-помічника. Думай крок за кроком (Chain-of-Thought): Крок 1 — Виділи 2 основні сегменти аудиторії. Крок 2 — Для кожного сегмента визнач 3 головні потреби (проблеми, страхи, незручності), з якими вони стикаються в інтернеті під час пошуку зарядної станції. Крок 3 — Запропонуй, як саме наш майбутній сайт (завдяки інтерфейсу чи функціям) може закрити ці потреби. Оформи результат у вигляді чіткої Markdown-таблиці та додай короткий підсумок для архітектури сайту.»")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Claude виконав покрокову декомпозицію аудиторії за ланцюжком міркувань, виділивши два полярні сегменти та сформувавши системне бачення їхніх потреб.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Необхідно було глибше пропрацювати архітектурний зв'язок між потребами водіїв та інтерактивними віджетами (передача обраного тарифу з карти в калькулятор).")
    set_font(r2)

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 2. Коригувальний запит (Модель: Claude)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Оформи результат чітко за кроками (Крок 1 — сегменти, Крок 2 — проблеми, Крок 3 — рішення у вигляді акуратної таблиці) та деталізуй архітектурний підсумок про взаємодію калькулятора й карти станцій.»")
    set_font(r2)

    p = add_p(space_before=2, space_after=6)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Зведено все у фінальну таблицю та сформовано архітектурні висновки.")
    set_font(r2)

    add_heading3("Результат аналізу цільової аудиторії (Розділ 2)")

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Сегмент 1 — «Досвідчений EV-власник»")
    set_font(r1, bold=True)
    r2 = p.add_run(" (постійний водій) — вже має електромобіль, регулярно заряджається на публічних станціях, вільно володіє термінологією (CCS2, Type 2, GB/T, кВт). Його пріоритет — швидкість пошуку вільного швидкісного порту, відсутність черг, достовірність даних про зайнятість та об'єктивне порівняння тарифів різних операторів.")
    set_font(r2)

    p = add_p(space_before=2, space_after=4)
    r1 = p.add_run("Сегмент 2 — «Потенційний / новий EV-власник»")
    set_font(r1, bold=True)
    r2 = p.add_run(" (новачок або потенційний покупець) — розглядає перехід на електротягу або щойно придбав авто. Відчуває сильний страх «не доїхати до розетки» (range anxiety), не розуміє різниці між AC/DC чи кВт і кВт·год, побоюється прихованих витрат і не знає, як розрахувати час та вартість заряду.")
    set_font(r2)

    # TABLE: AUDIENCE
    t_aud = doc.add_table(rows=7, cols=3)
    t_aud.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Border & padding setup
    set_table_borders(t_aud, color="C4C7C5", sz="6")
    
    col_widths = [Inches(1.15), Inches(2.45), Inches(3.32)]
    
    headers = ["Сегмент", "Проблема / Страх / Незручність", "Рішення на сайті-помічнику"]
    for c_idx, h_text in enumerate(headers):
        cell = t_aud.rows[0].cells[c_idx]
        set_cell_background(cell, "F0F0F0")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p_c = cell.paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(2)
        p_c.paragraph_format.space_after = Pt(2)
        r_c = p_c.add_run(h_text)
        set_font(r_c, bold=True, size_pt=10.5)

    aud_data = [
        ("Досвідчений EV-власник",
         "1. Range anxiety в дорозі — потрібно швидко знайти вільну станцію поруч із маршрутом, не гортаючи 3 різні застосунки.",
         "Карта з фільтром «Вільно зараз» + геолокація + швидке сортування «найближче вільне»."),
        ("Досвідчений EV-власник",
         "2. Несумісність конектора — приїхав на станцію, а потрібного роз'єму (CCS2/GB/T/CHAdeMO) немає або він зайнятий.",
         "Фільтр карти за типом конектора з візуальним індикатором наявності/статусу по кожному роз'єму окремо (не по станції загалом)."),
        ("Досвідчений EV-власник",
         "3. Непрозорість ціни та фінального рахунку — тарифи різняться по годинах/операторах, важко спрогнозувати витрату наперед.",
         "Калькулятор із прив'язкою до тарифу конкретної станції + попередній розрахунок вартості до поїздки."),
        ("Потенційний / новий EV-власник",
         "1. Страх «не вистачить заряду» — не розуміє, скільки км дає % заряду, чи вистачить на маршрут.",
         "Калькулятор з вводом ємності батареї/моделі авто → наочний переклад % в кВт·год і орієнтовний запас ходу в км."),
        ("Потенційний / новий EV-власник",
         "2. Незнання термінології (Type 2 vs CCS2, AC vs DC, кВт vs кВт·год) — губиться при виборі станції.",
         "Підказки (tooltips) біля технічних термінів у калькуляторі та на карті; проста мова замість жаргону."),
        ("Потенційний / новий EV-власник",
         "3. Невпевненість у витратах на «заправку» — не може порівняти з бензином, боїться непередбачуваних платежів.",
         "Калькулятор одразу показує вартість у ₴ + опційно порівняння з вартістю пального на АЗС для тієї ж дистанції.")
    ]

    for r_idx, (seg, prob, sol) in enumerate(aud_data, start=1):
        row = t_aud.rows[r_idx]
        for c_idx, val in enumerate([seg, prob, sol]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if c_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            p_c.paragraph_format.space_before = Pt(2)
            p_c.paragraph_format.space_after = Pt(2)
            p_c.paragraph_format.line_spacing = 1.1
            r_c = p_c.add_run(val)
            set_font(r_c, size_pt=10, bold=(c_idx == 0))

    # Apply column widths across all rows
    for row in t_aud.rows:
        for c_idx, w in enumerate(col_widths):
            row.cells[c_idx].width = w

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(2)
    p_sp.paragraph_format.space_after = Pt(2)

    p = add_p(space_before=4, space_after=2)
    r = p.add_run("Підсумок для архітектури сайту")
    set_font(r, bold=True)

    arch_points = [
        ("Карта станцій — головний інструмент для Сегмента 1 (досвідчені): ", "фільтри мають бути орієнтовані на конкретні конектори (Type 2, CCS2, GB/T, CHAdeMO), а статус (вільно/зайнято) та вихідна потужність повинні показуватися для кожного роз'єму індивідуально в режимі реального часу."),
        ("Калькулятор — головний інструмент конверсії та зняття страхів для Сегмента 2 (нові): ", "має працювати як за вибором моделі авто, так і з ручним введенням ємності батареї (якщо моделі немає в базі), містити спливаючі підказки для технічних термінів та переводити абстрактні відсотки у гривні, час та кілометри запасу ходу."),
        ("Точка перетину сегментів: ", "калькулятор і карта мають бути пов'язані двостороннім безшовним переходом (вибрав станцію на карті → її тариф автоматично підвантажується в калькулятор; розрахував необхідний заряд у калькуляторі → карта одразу фільтрує відповідні станції). Це кардинально знижує когнітивне навантаження для обох аудиторій одночасно.")
    ]
    for a_title, a_desc in arch_points:
        p_pt = add_p(space_before=1, space_after=2)
        r_t = p_pt.add_run("• " + a_title)
        set_font(r_t, bold=True)
        r_d = p_pt.add_run(a_desc)
        set_font(r_d)

    # =========================================================================
    # РОЗДІЛ 3. СПЕЦИФІКАЦІЯ ФУНКЦІОНАЛУ (USER STORIES)
    # =========================================================================
    add_heading1("Розділ 3. Специфікація функціоналу (User Stories)")

    add_heading3("Промпт-логи")

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 1. Початковий системний запит (Моделі: ChatGPT, Claude)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Грунтуючись на потребах цільової аудиторії, розроби набір технічних User Stories для нашого сайту-помічника «ChargeUA». Мені потрібні історії як для звичайного відвідувача, так і для водія, який активно взаємодіє з нашими ключовими модулями — інтерактивним калькулятором вартості/часу та картою зарядних станцій. Надаю приклад правильного формату (Few-Shot):\n"
                   "- Як новий власник EV, я хочу ввести ємність батареї вручну (якщо моєї моделі немає в базі), щоб отримати точний розрахунок вартості зарядки. (Технічний коментар: Перемикач вибору, валідація діапазону 10-200 кВт·год з інлайн-попередженням).\n"
                   "- Як досвідчений водій EV, я хочу задати поточний і цільовий % заряду двома повзунками, щоб миттєво бачити обсяг необхідної енергії без ручних обчислень. (Технічний коментар: Two-thumb range slider, формула ΔkWh = battery_kwh * (target% - current%) / 100 / ККД).\n"
                   "Напиши повний перелік із 12 детальних User Stories, які розбиті за модулями: Калькулятор, Карта, Навігація, Форма зв'язку.»")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Моделі згенерували повний спектр користувацьких сценаріїв, проте первинний варіант містив надмірні англіцизми (payload, two-thumb slider, shared state, lazy-render, lookup-table).")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Необхідно замінити зайві англіцизми зрозумілою інженерною українською термінологією, зберегти глибину технічних коментарів та сформувати матрицю простежуваності вимог.")
    set_font(r2)

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 2. Коригувальний запит (Моделі: ChatGPT, Claude)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Перепиши технічні коментарі зрозумілою інженерною українською мовою, прибери зайві англіцизми, чітко розбий історії на 4 модулі від US-01 до US-12 та побудуй матрицю покриття вимог (Requirements Traceability Matrix).»")
    set_font(r2)

    p = add_p(space_before=2, space_after=6)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Отримано остаточний структурований набір із 12 користувацьких історій та зведену матрицю відповідності, наведені нижче.")
    set_font(r2)

    add_heading3("Результат специфікації функціоналу (Розділ 3)")

    p = add_p(space_before=2, space_after=4)
    p.add_run("Для опису функціональних вимог до платформи «ChargeUA» використано міжнародний стандарт бізнес-аналізу — користувацькі історії (User Stories) за шаблоном «Як [роль], я хочу [дія], щоб [мета]» із детальними технічними коментарями щодо реалізації.")

    user_stories = [
        # Module 1
        ("Модуль 1. Інтерактивний калькулятор вартості та часу зарядки", [
            ("US-01. ", "Як новий власник EV, я хочу обрати модель свого авто зі спадного списку або ввести ємність батареї вручну (якщо моделі немає в базі), щоб отримати точний розрахунок вартості та необхідної енергії.",
             "Технічний коментар: На формі передбачено перемикач між двома режимами («Вибрати модель» та «Ввести вручну»); поле custom_battery_kwh містить клієнтську валідацію допустимого діапазону (10–200 кВт·год) з інлайн-попередженням при введенні некоректних даних."),
            
            ("US-02. ", "Як користувач-початківець, я хочу бачити спливаючі підказки (tooltips) біля технічних позначень (різниця між AC/DC, кВт та кВт·год) безпосередньо біля полів вводу, щоб легко розібратися у параметрах без пошуку пояснень в інтернеті.",
             "Технічний коментар: Інтерактивний компонент спливаючої підказки біля іконки зі знаком питання; контент підвантажується з локального словника термінів при наведенні курсора чи тапі на сенсорному екрані."),
            
            ("US-03. ", "Як досвідчений водій EV, я хочу налаштувати поточний і бажаний відсоток заряду за допомогою зручного подвійного повзунка (де цільове значення завжди більше за початкове), щоб миттєво побачити точну кількість кіловат-годин до дозаправки.",
             "Технічний коментар: Використано повзунок з двома точками регулювання діапазону (range slider); встановлено логічне обмеження min/max, що блокує вибір цільового значення меншим за поточне. Обсяг енергії розраховується за формулою: ΔkWh = battery_kwh × (target% - current%) / 100 / ККД, де враховуються втрати на перетворення струму (коефіцієнт 0.90 для AC та 0.95 для DC)."),
            
            ("US-04. ", "Як користувач сервісу, я хочу, щоб калькулятор автоматично підтягував тариф станції, обраної на інтерактивній карті (або дозволяв ручне коригування тарифу), щоб бачити точну вартість сесії в гривнях для конкретної локації.",
             "Технічний коментар: Спільний стан застосунку (selectedStationId) синхронізує модулі Карти та Калькулятора; при виборі станції на карті виконується зчитування її актуального тарифу (₴/кВт·год) та автозаповнення відповідного поля калькулятора."),
            
            ("US-05. ", "Як досвідчений водій, я хочу бачити розрахунковий час зарядки з урахуванням потужності конектора (повільна AC на 22 кВт або швидка DC на 60–120 кВт), щоб планувати тривалість своєї зупинки в дорозі.",
             "Технічний коментар: Розрахунок часу триває за формулою: time_min = (ΔkWh / connector_power_kw) × 60. Для швидких станцій постійного струму закладено алгоритм корекції швидкості заряду: після подолання порогу 80% закладено поправочний коефіцієнт уповільнення прийому струму згідно з типовою кривою зарядки сучасних батарей."),
            
            ("US-06. ", "Як потенційний покупець електрокара, я хочу бачити порівняння вартості розрахованого заряду з еквівалентною вартістю бензину на аналогічний пробіг, щоб наочно оцінити власну фінансову економію.",
             "Технічний коментар: Калькулятор перераховує отримані кВт·год у приблизний запас ходу за середньою витратою 16 кВт·год/100 км та зіставляє витрати з бензиновим авто (розрахунок на 8 л пального на 100 км за актуальною середньою ціною А-95).")
        ]),
        
        # Module 2
        ("Модуль 2. Інтерактивна карта зарядних станцій", [
            ("US-07. ", "Як водій у дорозі, я хочу бачити інтерактивну карту із кольоровими маркерами станцій (зелений — вільні порти, жовтий — усі зайняті, червоний/сірий — офлайн), щоб миттєво оцінити доступність зарядки в радіусі поїздки.",
             "Технічний коментар: Картографічний віджет на базі векторної бібліотеки (Leaflet/Mapbox); маркери мають 3 класи статусу, що динамічно оновлюються на основі агрегованого стану доступності портів конкретної станції."),
            
            ("US-08. ", "Як власник авто з китайським або європейським портом, я хочу відфільтрувати маркери за моїм типом роз'єму (GB/T, CCS2, Type 2, CHAdeMO) та потужністю, щоб бачити тільки повністю сумісні станції.",
             "Технічний коментар: Клієнтська фільтрація масиву об'єктів станцій за значенням connector_types та power_kw; миттєве оновлення видимих маркерів на полотні карти без повторних важких запитів."),
            
            ("US-09. ", "Як користувач, я хочу натиснути на маркер станції та відкрити інформаційну картку з адресою, оператором, переліком усіх портів зі статусами, ціною та часом останнього оновлення даних, щоб прийняти рішення про виїзд.",
             "Технічний коментар: Спливаюче модальне вікно або висувна бічна панель (Drawer); відображення картки станції з міткою часу останнього оновлення даних (last_updated) та кнопкою швидкого переходу «Розрахувати для цієї станції»."),
            
            ("US-10. ", "Як український водій, я хочу скористатися фільтром «Працює під час відключень світла (генератор / акумулятор)», щоб гарантовано знайти робочу станцію під час аварійних або стабілізаційних блекаутів.",
             "Технічний коментар: Булевий прапорець has_backup_power у моделі станції; візуальний бейдж «🔋 Генератор / Безперебійник» на картці станції та можливість швидкої фільтрації карти за цим параметром.")
        ]),
        
        # Module 3
        ("Модуль 3. Навігація та інтеграція інтерфейсу", [
            ("US-11. ", "Як мобільний відвідувач, я хочу мати закріплену шапку з меню та кнопкою швидкого переходу між калькулятором і картою (Sticky Header), щоб зручно керувати сервісом на смартфоні без повторного прокручування сторінки.",
             "Технічний коментар: Адаптивна навігаційна панель із фіксованим позиціонуванням (position: sticky); збереження стану форми калькулятора та масштабу карти при перемиканні вкладок без втрати введених користувачем даних.")
        ]),
        
        # Module 4
        ("Модуль 4. Зворотний зв'язок та валідація даних", [
            ("US-12. ", "Як свідомий користувач або партнер, я хочу надіслати повідомлення про виявлену неточність даних (наприклад, зміну тарифу, непрацюючий роз'єм чи зміну графіка), щоб підтримувати базу агрегатора актуальною.",
             "Технічний коментар: Форма зворотного зв'язку з випадаючим списком тем («Неточні дані», «Технічна проблема», «Пропозиція»), перевіркою коректності email/телефону та фіксацією звернення в системі з повідомленням про успішну доставку.")
        ])
    ]

    for mod_title, stories in user_stories:
        p_m = add_p(space_before=4, space_after=2)
        r_m = p_m.add_run(mod_title)
        set_font(r_m, bold=True)
        
        for prefix, story_text, comment in stories:
            p_us = add_p(space_before=2, space_after=1)
            r_pre = p_us.add_run(prefix)
            set_font(r_pre, bold=True)
            r_st = p_us.add_run(story_text)
            set_font(r_st)
            
            p_comm = add_p(space_before=1, space_after=3)
            r_lbl = p_comm.add_run(comment[:19])  # "Технічний коментар:"
            set_font(r_lbl, bold=True, italic=True)
            r_cbody = p_comm.add_run(comment[19:])
            set_font(r_cbody, italic=True)

    add_heading3("Таблиця покриття вимог (Requirements Traceability Matrix)")

    p = add_p(space_before=2, space_after=4)
    p.add_run("Щоб переконатися, що жоден етап користувацького шляху та технічного функціоналу не пропущено, нижче наведено матрицю зв'язку між ключовими функціональними областями платформи та розробленими User Stories:")

    # TABLE: RTM
    t_rtm = doc.add_table(rows=7, cols=2)
    t_rtm.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_rtm, color="C4C7C5", sz="6")
    
    rtm_widths = [Inches(4.1), Inches(2.82)]
    
    rtm_headers = ["Область функціоналу", "Відповідні User Stories"]
    for c_idx, h_text in enumerate(rtm_headers):
        cell = t_rtm.rows[0].cells[c_idx]
        set_cell_background(cell, "F0F0F0")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p_c = cell.paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(2)
        p_c.paragraph_format.space_after = Pt(2)
        r_c = p_c.add_run(h_text)
        set_font(r_c, bold=True, size_pt=10.5)

    rtm_data = [
        ("Розрахунок параметрів батареї та обсягу енергії", "US-01, US-02, US-03"),
        ("Розрахунок часу зарядки та економічного ефекту проти ДВЗ", "US-04, US-05, US-06"),
        ("Інтерактивна карта, кольорові маркери та статуси конекторів", "US-07, US-09"),
        ("Фільтрація конекторів та енергонезалежність станцій", "US-08, US-10"),
        ("Глобальна навігація, мобільна адаптивність та інтеграція модулів", "US-11"),
        ("Зворотний зв'язок та підтримка якості даних агрегатора", "US-12")
    ]

    for r_idx, (area, us_ids) in enumerate(rtm_data, start=1):
        row = t_rtm.rows[r_idx]
        for c_idx, val in enumerate([area, us_ids]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p_c = cell.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            p_c.paragraph_format.space_before = Pt(2)
            p_c.paragraph_format.space_after = Pt(2)
            p_c.paragraph_format.line_spacing = 1.1
            r_c = p_c.add_run(val)
            set_font(r_c, size_pt=10, bold=(c_idx == 1))

    for row in t_rtm.rows:
        for c_idx, w in enumerate(rtm_widths):
            row.cells[c_idx].width = w

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(2)
    p_sp.paragraph_format.space_after = Pt(2)

    # =========================================================================
    # РОЗДІЛ 4. АРХІТЕКТУРА ТА СТРУКТУРА САЙТУ (SITEMAP)
    # =========================================================================
    add_heading1("Розділ 4. Архітектура та структура сайту (Sitemap)")

    add_heading3("Промпт-логи")

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Запит до моделі ШІ (Claude)")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Створи детальну і логічну текстову карту сайту (Sitemap) для вебпроєкту «ChargeUA» (веб-помічник та агрегатор станцій) у форматі дворівневих маркованих списків Markdown у моноширинному блоці. Структура повинна відображати роль платформи саме як сервісу-агрегатора (порівняння тарифів різних мереж, живий статус конекторів, енергонезалежність). Включи Головну сторінку з усіма функціональними блоками (Header, Hero, Блок переваг, Інтерактивний віджет Калькулятор + Карта, Інструкція «Як це працює», Блок джерел даних / партнерських операторів, Форма зворотного зв'язку, Footer з дисклеймером) та додаткові сторінки (/map, /calculator, /pricing, /about, /support, /legal). Додай архітектурний висновок про інтеграцію калькулятора та карти.»")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Отримано розгорнуту карту сайту у форматі дворівневого списку Markdown.")
    set_font(r2)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Аналіз недоліків: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Первинний варіант містив надмірні акценти на власній інфраструктурі мережі («наші тарифи», «наші станції»). Потрібно було перевести акцент на агрегацію відкритих даних, об'єднати калькулятор та карту в єдиний конверсійний віджет на головній сторінці та виділити дисклеймер агрегатора.")
    set_font(r2)

    p = add_p(space_before=3, space_after=2)
    r = p.add_run("Крок 2. Коригування та фіналізація архітектури")
    set_font(r, bold=True)

    p = add_p(space_before=2, space_after=2)
    r1 = p.add_run("Запит: ")
    set_font(r1, bold=True)
    r2 = p.add_run("«Скоригуй текстову карту сайту (Sitemap) для Головної сторінки «ChargeUA» з акцентом на сервіс-помічник / агрегатор. Заміни власні тарифи на порівняння тарифів операторів, додай позначку часу оновлення даних та покроковий блок для новачків «Як це працює».»")
    set_font(r2)

    p = add_p(space_before=2, space_after=6)
    r1 = p.add_run("Результат: ")
    set_font(r1, bold=True)
    r2 = p.add_run("Сформовано остаточну інформаційну архітектуру веб-ресурсу «ChargeUA».")
    set_font(r2)

    add_heading3("Результат архітектурного проєктування (Розділ 4)")

    p = add_p(space_before=2, space_after=4)
    p.add_run("Архітектура платформи «ChargeUA» спроєктована на основі концепції utility-first (миттєвий доступ до практичних інструментів). Центральним конверсійним вузлом є Головна сторінка, на якій ключове місце займає інтерактивний віджет, що синхронізує калькулятор вартості з картою станцій.")

    p = add_p(space_before=2, space_after=4)
    p.add_run("Нижче наведено детальну текстову карту сайту (Sitemap) у вигляді дворівневої структури Markdown:")

    # SITEMAP MONOSPACE BLOCK
    sitemap_lines = [
        "- Головна сторінка (Home - /)",
        "  - Шапка сайту (Header)",
        "    - Логотип «ChargeUA» (з підписом «сервіс пошуку та розрахунку зарядок»)",
        "    - Головне навігаційне меню (Карта станцій / Калькулятор / Порівняння тарифів / Про сервіс / Підтримка)",
        "    - Закріплена кнопка швидкої дії «Знайти станцію» (Sticky Quick CTA)",
        "    - Мобільне гамбургер-меню (Mobile Navigation Drawer)",
        "  - Головний екран (Hero-section)",
        "    - Головний заголовок ціннісної пропозиції: «Усі зарядні станції України — в одному місці»",
        "    - Підзаголовок: «Порівнюй тарифи операторів, розраховуй вартість та знаходь вільний роз'єм за лічені секунди»",
        "    - Головна кнопка дії «Розрахувати вартість» (Primary CTA -> якір до калькулятора)",
        "    - Другорядна кнопка «Подивитись карту» (Secondary CTA -> якір до карти)",
        "    - Короткі показники масштабу агрегатора: кількість станцій у базі, кількість охоплених мереж, географія покриття",
        "  - Блок переваг агрегатора (Value Proposition)",
        "    - Перевага 1: «Все в одному місці» — доступ до провідних мереж без необхідності тримати 5 додатків",
        "    - Перевага 2: «Об'єктивне порівняння» — прозорі тарифи різних операторів на одному екрані",
        "    - Перевага 3: «Живий статус конекторів» — оперативне оновлення інформації про зайнятість портів",
        "    - Перевага 4: «Енергонезалежність» — чіткі позначки станцій із резервним живленням від генераторів",
        "  - Блок з інтерактивним віджетом (Core Feature Widget)",
        "    - Перемикач вкладок віджета (Tabs)",
        "    - Вкладка 1: «Калькулятор вартості та часу зарядки»",
        "      - Вибір марки та моделі електромобіля з бази або перемикач на ручний ввід ємності батареї (кВт·год)",
        "      - Двоточковий інтерактивний повзунок рівня заряду (поточний % -> цільовий %)",
        "      - Поле тарифу (автоматичне підтягування з обраної станції або ручне введення ₴/кВт·год)",
        "      - Блок миттєвого результату: загальна вартість (₴), необхідна енергія (кВт·год), приблизний час сесії",
        "      - Блок економічного порівняння: зіставлення вартості зарядки з еквівалентом витрат на бензин",
        "      - Кнопка «Знайти станцію з цим тарифом» (автоматичне перемикання на вкладку карти)",
        "    - Вкладка 2: «Карта зарядних станцій»",
        "      - Панель швидких фільтрів: тип роз'єму (Type 2, CCS2, GB/T, CHAdeMO), потужність (AC/DC), оператор, статус («Тільки вільні»), бейдж «Працює від генератора»",
        "      - Інтерактивна карта з кластеризацією та кольоровими маркерами доступності",
        "      - Спливаюча інформаційна картка станції (назва, оператор, адреса, список конекторів з потужністю і статусом, актуальний тариф за 1 кВт·год, мітка останнього оновлення)",
        "      - Кнопка «Розрахувати вартість для цієї станції» (передача тарифу у вкладку калькулятора)",
        "      - Кнопка «Повідомити про неточність даних»",
        "  - Інструкція «Як це працює» (How It Works)",
        "    - Крок 1: Оберіть ваше авто або вкажіть потрібний тип роз'єму",
        "    - Крок 2: Отримайте точний розрахунок вартості, часу зарядки та прогнозованого запасу ходу",
        "    - Крок 3: Оберіть найближчу вільну станцію на карті та прокладіть маршрут",
        "  - Блок операторів-партнерів та джерел даних (Data Providers)",
        "    - Логотипи підключених мереж (Yasno E-Mobility, EcoFactor, GO TO-U, Ionity та інші)",
        "    - Пояснювальний текст про періодичність синхронізації та використання відкритих API",
        "    - Посилання «Дізнатися більше про джерела даних»",
        "  - Форма зворотного зв'язку (Contact & Feedback Form)",
        "    - Тема звернення: «Неточні дані про станцію», «Технічна проблема», «Пропозиція додати мережу», «Інше»",
        "    - Поля вводу: контактний email/телефон, текстове поле повідомлення, прив'язка до станції",
        "    - Чекбокс згоди з правилами обробки даних та кнопка «Надіслати»",
        "    - Екран підтвердження успішної реєстрації повідомлення",
        "  - Підвал сайту (Footer)",
        "    - Колонка «Навігація» (посилання на основні розділи та карту)",
        "    - Колонка «Юридична інформація» (політика конфіденційності, умови користування)",
        "    - Офіційний дисклеймер агрегатора: «ChargeUA є незалежним інформаційним сервісом і не є власником зарядного обладнання»",
        "    - Колонка «Контакти» (електронна пошта підтримки, посилання на спільноти в месенджерах)",
        "    - Копірайт «© 2026 ChargeUA»",
        "",
        "- Додаткові сторінки сервісу:",
        "  - Сторінка «Карта станцій» (/map) — повноекранна версія карти з поглибленими інструментами радіального пошуку та прокладання маршрутів",
        "  - Сторінка «Калькулятор» (/calculator) — повнорозмірний калькулятор із візуалізацією кривої зарядки та порівняльним графіком витрат ДВЗ проти EV",
        "  - Сторінка «Порівняння тарифів» (/pricing) — зведена динамічна таблиця актуальних тарифів операторів за типами станцій",
        "  - Сторінка «Про сервіс» (/about) — місія агрегатора, принципи верифікації даних та пропозиція партнерства для операторів",
        "  - Сторінка «Підтримка та FAQ» (/support) — поширені запитання, довідник типів портів та технічна допомога",
        "  - Юридичні сторінки (/legal) — публічна оферта та положення про конфіденційність"
    ]

    for line in sitemap_lines:
        p_c = doc.add_paragraph()
        p_c.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(1)
        p_c.paragraph_format.line_spacing = 1.0
        p_c.paragraph_format.left_indent = Inches(0.2)
        r_c = p_c.add_run(line if line else " ")
        set_font(r_c, name="Courier New", size_pt=9.5)

    add_heading3("Архітектурний висновок")

    p = add_p(space_before=4, space_after=6)
    p.add_run("Завдяки такій структурі веб-ресурс ChargeUA витримує баланс між швидким сервісом-помічником та повноцінною аналітичною платформою. Об'єднання інтерактивного калькулятора та карти в єдиний конверсійний вузол на головній сторінці повністю усуває тертя при взаємодії: користувач із будь-якого етапу може перемкнутися між точним розрахунком витрат і пошуком найближчої вільної станції з відповідним тарифом та конектором.")

    # =========================================================================
    # РОЗДІЛ 5. ПРОМПТ-ПАСПОРТ (PROMPT LOG)
    # =========================================================================
    add_heading1("Розділ 5. Промпт-паспорт (Prompt Log)")

    p = add_p(space_before=2, space_after=6)
    p.add_run("Нижче наведено повний хронологічний протокол генерацій, що фіксує взаємодію з трьома моделями штучного інтелекту (ChatGPT, Grok, Claude) на всіх етапах розробки передпроєктної документації.")

    # --- ЕТАП 0: РОЛЬОВЕ ПОЗИЦІОНУВАННЯ ---
    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Етап 0 – Текст системного запиту ролі):",
        "«Ти — Senior Business Analyst & UI/UX Expert з 15-річним досвідом розробки цифрових продуктів. Твоє завдання — допомогти мені спроектувати архітектуру та логіку для вебсайту за темою: Лендинг мережі зарядних станцій для електромобілів «ChargeUA». Специфікація: інтерактивний калькулятор вартості зарядки з вибором моделі електромобіля (або введенням ємності батареї), відсотка заряду та тарифу, плюс інтерактивна карта зарядних станцій з відображенням потужності конекторів (Type 2, CCS2, GBT, CHAdeMO), зайнятості та актуальних цін за кВт·год. Твої відповіді мають бути структурованими, технічно грамотними, без «води», в форматі професійних артефактів (таблиці, списки, markdown). Чи зрозуміла тобі твоя роль та специфікація проєкту?»"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId10_image4.png"),
        "Рис. 5.1 – Ініціалізація ролі Senior Business Analyst & UI/UX Expert та структуризація модулів проєкту ChargeUA у ChatGPT"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId7_image1.png"),
        "Рис. 5.2 – Підтвердження ролі та специфікації функціоналу проєкту ChargeUA в системі Grok"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId11_image5.png"),
        "Рис. 5.3 – Закріплення аналітичної ролі та параметризація модуля калькулятора в Claude"
    )

    # --- ІТЕРАЦІЯ 1: ДОСЛІДЖЕННЯ РИНКУ ---
    p_it1 = add_p(space_before=6, space_after=4)
    r1 = p_it1.add_run("Ітерація 1: Дослідження ринку та передача контексту між моделями (Context Chaining у Grok)\n")
    set_font(r1, bold=True)
    r2 = p_it1.add_run("За допомогою нейромережі Grok було проведено поглиблений аналіз трендів ринку електрозарядних станцій за останні 6–12 місяців в Україні та світі. На другому кроці було проведено адаптацію термінології та враховано специфіку українського енергоринку (робота станцій від генераторів під час вимкнень).")
    set_font(r2)

    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Ітерація 1 – Текст запиту до Grok):",
        "«Проаналізуй ринок вебсайтів та додатків для зарядних станцій електромобілів (EV charging networks, таких як Tesla Supercharger, Ionity, Yasno E-Mobility, EcoFactor, GO TO-U) за останні 6-12 місяців в Україні та світі. Які головні візуальні та функціональні тренди зараз домінують? Які інтерактивні функції очікують побачити водії електромобілів на сучасному лендингу? Виділи 5 ключових інсайтів простою, зрозумілою українською мовою без надмірних англіцизмів.»"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId8_image2.png"),
        "Рис. 5.4 – Початковий ринковий аналіз тенденцій сервісів для електромобілів у Grok (Крок 1)"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId9_image3.png"),
        "Рис. 5.5 – Адаптація та коригування аналітичного брифу ринку українською термінологією у Grok (Крок 2)"
    )

    # --- ІТЕРАЦІЯ 2: АНАЛІЗ АУДИТОРІЇ ---
    p_it2 = add_p(space_before=6, space_after=4)
    r1 = p_it2.add_run("Ітерація 2: Багатокроковий аналіз цільової аудиторії (Chain-of-Thought у Claude)\n")
    set_font(r1, bold=True)
    r2 = p_it2.add_run("На основі зібраних ринкових трендів модель Claude виконала покрокову декомпозицію цільової аудиторії за технікою ланцюжка міркувань (Chain-of-Thought), сформувавши матрицю проблем та їх інженерних рішень.")
    set_font(r2)

    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Ітерація 2 – Текст запиту Chain-of-Thought):",
        "«На основі раніше визначених трендів проаналізуй цільову аудиторію нашого сайту-помічника. Думай крок за кроком (Chain-of-Thought): Крок 1 — Виділи 2 основні сегменти аудиторії. Крок 2 — Для кожного сегмента визнач 3 головні потреби (проблеми, страхи, незручності), з якими вони стикаються в інтернеті під час пошуку зарядної станції. Крок 3 — Запропонуй, як саме наш майбутній сайт (завдяки інтерфейсу чи функціям) може закрити ці потреби. Оформи результат у вигляді чіткої Markdown-таблиці та додай короткий підсумок для архітектури.»"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId12_image6.png"),
        "Рис. 5.6 – Сегментація та аналіз потреб цільової аудиторії за технікою Chain-of-Thought у Claude"
    )

    # --- ІТЕРАЦІЯ 3: USER STORIES ---
    p_it3 = add_p(space_before=6, space_after=4)
    r1 = p_it3.add_run("Ітерація 3: Специфікація функціональних вимог (Few-Shot Prompting у Claude)\n")
    set_font(r1, bold=True)
    r2 = p_it3.add_run("Використано техніку Few-Shot із наданням чітких зразків історій користувача та інженерних коментарів для формування 12 User Stories, розбитих за модулями калькулятора, карти, навігації та зворотного зв'язку.")
    set_font(r2)

    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Ітерація 3 – Текст запиту Few-Shot):",
        "«Грунтуючись на потребах цільової аудиторії, розроби набір технічних User Stories для нашого сайту-помічника «ChargeUA». Мені потрібні історії як для звичайного відвідувача, так і для водія, який активно взаємодіє з інтерактивним калькулятором вартості та картою станцій. Надаю приклад правильного формату (Few-Shot): Як новий власник EV, я хочу ввести ємність батареї вручну, щоб розрахувати вартість (Технічний коментар: Перемикач вибору, валідація діапазону 10-200 кВт·год). Напиши 12 детальних User Stories, які розбиті за модулями: Калькулятор, Карта, Навігація, Форма зв'язку.»"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId15_image9.png"),
        "Рис. 5.7 – Початкова специфікація користувацьких історій User Stories із технічними коментарями в Claude (Крок 1)"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId13_image7.png"),
        "Рис. 5.8 – Адаптація та коригування User Stories зрозумілою інженерною термінологією в Claude (Крок 2)"
    )

    # --- ІТЕРАЦІЯ 4: SITEMAP ---
    p_it4 = add_p(space_before=6, space_after=4)
    r1 = p_it4.add_run("Ітерація 4: Інформаційна архітектура та синтез карти сайту (Sitemap у Claude)\n")
    set_font(r1, bold=True)
    r2 = p_it4.add_run("Фінальний етап проєктування присвячено побудові ієрархічної карти сторінок та інформаційних блоків платформи ChargeUA з акцентом на роль сервісу як незалежного агрегатора даних.")
    set_font(r2)

    add_callout(
        "ВХІДНИЙ ЗАПИТ ДО МОДЕЛІ (Ітерація 4 – Текст запиту Sitemap):",
        "«Створи детальну і логічну карту сайту (Sitemap) для вебпроєкту «ChargeUA» (сервіс-помічник та агрегатор станцій) у форматі дворівневих списків Markdown. Структура має включати Головну сторінку з усіма блоками (Header, Hero, Переваги агрегатора, Інтерактивний віджет Калькулятор + Карта, Інструкція, Оператори-партнери, Форма зворотного зв'язку, Footer з дисклеймером) та додаткові сторінки (/map, /calculator, /pricing, /about, /support, /legal).»"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId14_image8.png"),
        "Рис. 5.9 – Проєктування початкової ієрархічної карти сторінок сайту (Sitemap) у Claude (Крок 1)"
    )

    add_image_with_caption(
        os.path.join("extracted_images_draft", "rId16_image10.png"),
        "Рис. 5.10 – Фіналізація карти інформаційної архітектури ChargeUA як сервісу-агрегатора в Claude (Крок 2)"
    )

    # =========================================================================
    # ВИСНОВКИ
    # =========================================================================
    add_heading1("Висновки")

    p_intro = add_p(space_before=4, space_after=4)
    p_intro.add_run("У ході виконання лабораторної роботи №1 було детально опановано практичні методи промпт-інжинірингу та досліджено ефект синергії між провідними генеративними моделями штучного інтелекту (ChatGPT, Grok, Claude) на етапі передпроєктного дослідження та проєктування цифрового вебресурсу «ChargeUA».")

    p_subc = add_p(space_before=2, space_after=4)
    r_sub = p_subc.add_run("Головні практичні результати та висновки роботи:")
    set_font(r_sub, bold=True)

    concl_items = [
        ("1. Ефективність сучасних технік промпт-інжинірингу: ",
         "Застосування рольової рамки (Role Prompting) дозволило з першого кроку усунути розмовний стиль моделей та перевести генерацію в формат структурованих інженерних артефактів. Техніка Few-Shot Prompting з наданням зразка структури забезпечила генерацію 12 повноцінних User Stories із високим рівнем технічної деталізації (стани інтерфейсу, клієнтські валідації, формули розрахунку втрат енергії та алгоритми нелінійного спаду швидкості заряду). Метод Chain-of-Thought дозволив послідовно декомпозувати болі та бар'єри водіїв електрокарів, перетворивши їх на чіткі інтерфейсні рішення."),
        
        ("2. Синергетичний розподіл завдань між генеративними моделями ШІ: ",
         "Кожна з використаних нейромереж проявила свої унікальні сильні сторони під час виконання проєкту:\n"
         "• Grok зарекомендував себе як найкращий інструмент для збору актуальної ринкової інформації за 2025–2026 рр. завдяки прямому доступу до даних у режимі реального часу, виділивши критичні тренди українського ринку (фактор автономності від генераторів та зростання популярності портів GB/T);\n"
         "• Claude продемонстрував найвищий рівень системно-інженерного аналізу при проєктуванні матриці цільової аудиторії, формулюванні точних технічних коментарів до User Stories та побудові дворівневої структури інформаційної архітектури (Sitemap);\n"
         "• ChatGPT забезпечив надійний концептуальний фундамент на етапі формулювання ролі, окреслив мобільні UX-принципи та допоміг виявити ризики функціональної ізоляції калькулятора від карти."),
        
        ("3. Практична цінність розробленого ТЗ для проєкту «ChargeUA»: ",
         "Сформований аналітичний пакет артефактів (ринковий бриф, матриця сегментів аудиторії, 12 деталізованих користувацьких історій, матриця відповідності вимог RTM, дворівнева карта сайту та промпт-паспорт) являє собою повноцінне, несуперечливе технічне завдання. Розроблена архітектура усуває бар'єри фрагментованого українського ринку електрозарядок, а отримані матеріали повністю готові до наступних стадій розробки — прототипування UI/UX дизайну у Figma та створення фронтенд-компонентів лендингу.")
    ]

    for c_title, c_text in concl_items:
        p_c = add_p(space_before=3, space_after=3)
        r_t = p_c.add_run(c_title)
        set_font(r_t, bold=True)
        r_txt = p_c.add_run(c_text)
        set_font(r_txt)

    # Save document
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    create_report()
