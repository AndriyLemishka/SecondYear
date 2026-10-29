import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_gorgeous_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Premium NVIDIA Obsidian Palette
    BG_OBSIDIAN = RGBColor(10, 13, 20)      # #0A0D14
    CARD_BG = RGBColor(18, 24, 38)          # #121826
    CARD_BORDER = RGBColor(34, 45, 68)      # #222D44
    NV_GREEN = RGBColor(118, 185, 0)        # #76B900
    NV_GREEN_BG = RGBColor(20, 36, 12)      # Deep green tint
    CYAN_ACCENT = RGBColor(34, 211, 238)    # #22D3EE
    AMBER_ACCENT = RGBColor(251, 191, 36)   # #FBBF24
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_SLATE = RGBColor(156, 163, 175)    # #9CA3AF
    TEXT_LIGHT_SLATE = RGBColor(209, 213, 219)

    assets_dir = r"D:\Studing\SecondYear\FirstSemester\web\assets"

    def apply_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_OBSIDIAN
        bg.line.fill.background()
        return bg

    def add_top_bar(slide, slide_num, tag_text, title_text):
        # Category Tag Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(4.5), Inches(0.36))
        badge.fill.solid()
        badge.fill.fore_color.rgb = NV_GREEN_BG
        badge.line.color.rgb = NV_GREEN
        btf = badge.text_frame
        btf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = btf.paragraphs[0]
        p.text = f"●  {tag_text.upper()}   |   СЛАЙД {slide_num:02d} / 12"
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = NV_GREEN

        # Slide Title
        tbox = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.75))
        tf = tbox.text_frame
        tf.word_wrap = True
        p2 = tf.paragraphs[0]
        p2.text = title_text
        p2.font.name = "Arial"
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: CINEMATIC TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1)

    # Hero visual on right (large, high impact)
    img_hero = os.path.join(assets_dir, "hero_title.jpg")
    if os.path.exists(img_hero):
        s1.shapes.add_picture(img_hero, Inches(6.8), Inches(0.8), Inches(5.8), Inches(5.9))

    # Decorative left card
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(5.6), Inches(5.9))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = NV_GREEN
    ctf = c1.text_frame
    ctf.word_wrap = True
    ctf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = ctf.paragraphs[0]
    p.text = "ТЕХНОЛОГІЇ ВЕБРОЗРОБКИ ТА ДИЗАЙНУ · КАФЕДРА САПР"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = NV_GREEN

    p_title = ctf.add_paragraph()
    p_title.text = "\nNVIDIA DLSS 5:"
    p_title.font.size = Pt(36)
    p_title.font.bold = True
    p_title.font.color.rgb = NV_GREEN

    p_sub = ctf.add_paragraph()
    p_sub.text = "3D-Guided Neural Rendering"
    p_sub.font.size = Pt(24)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_WHITE

    p_desc = ctf.add_paragraph()
    p_desc.text = "Прорив нейронного світла та жовтневе оновлення продуктивності 2026 року"
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = TEXT_SLATE

    p_auth = ctf.add_paragraph()
    p_auth.text = "\n\nДоповідач: Лемішка Андрій (ПП-24)"
    p_auth.font.size = Pt(14)
    p_auth.font.bold = True
    p_auth.font.color.rgb = TEXT_WHITE

    p_inst = ctf.add_paragraph()
    p_inst.text = "Національний університет «Львівська політехніка» · 2026"
    p_inst.font.size = Pt(11)
    p_inst.font.color.rgb = CYAN_ACCENT

    # -------------------------------------------------------------
    # SLIDE 2: КОНТЕКСТ ЕВОЛЮЦІЇ (2018–2026)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2)
    add_top_bar(s2, 2, "Вступний контекст", "Еволюція технології за 8 років: від простого масштабування до нейронного світла")

    evo_steps = [
        ("2018", "DLSS 1.0", "Окремі моделі", "Тренування для кожної гри окремо. Відсутність історії кадрів, часті артефакти й мило."),
        ("2020", "DLSS 2.0", "Super Resolution", "Просторово-часова історія (Temporal) + вектори руху. Домальовує 4K із 1080p у 4 рази швидше."),
        ("2022–25", "DLSS 3 & 4", "Frame Generation", "ШІ генерує проміжні штучні кадри за допомогою Optical Flow. Множники плавності 2x та 4x MFG."),
        ("Жовтень 2026", "DLSS 5", "Neural Rendering", "ШІ прораховує світло та матеріали замість Path Tracing. Жовтневий стрибок швидкості у 2 рази.")
    ]

    for idx, (yr, name, subtitle, desc) in enumerate(evo_steps):
        x = Inches(0.8 + idx * 2.95)
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(5.0))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = NV_GREEN if idx == 3 else CARD_BORDER
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = yr
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = NV_GREEN if idx == 3 else TEXT_SLATE

        p2 = ctf.add_paragraph()
        p2.text = name
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

        p3 = ctf.add_paragraph()
        p3.text = subtitle
        p3.font.size = Pt(12)
        p3.font.bold = True
        p3.font.color.rgb = CYAN_ACCENT if idx == 3 else NV_GREEN

        p4 = ctf.add_paragraph()
        p4.text = "\n" + desc
        p4.font.size = Pt(11)
        p4.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 3: 1. МЕТА НОВИНКИ (VISUAL + TEXT)
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    apply_bg(s3)
    add_top_bar(s3, 3, "Регламент: Пункт 1", "1. Мета новинки: навіщо створено DLSS 5")

    # Left: High impact image
    img_pipe = os.path.join(assets_dir, "pipeline_dragon.jpg")
    if os.path.exists(img_pipe):
        s3.shapes.add_picture(img_pipe, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))

    # Right: Purpose details
    c3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(1.8), Inches(5.8), Inches(4.9))
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_BG
    c3.line.color.rgb = NV_GREEN
    ctf = c3.text_frame
    ctf.word_wrap = True

    p = ctf.paragraphs[0]
    p.text = "🎯 ГОЛОВНА МЕТА РОЗРОБКИ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NV_GREEN

    p2 = ctf.add_paragraph()
    p2.text = "Заміна математичного Path Tracing генеративним ШІ світла"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    bullets3 = [
        ("Подолання обчислювального бар'єру", "Чесне трасування мільярдів променів світла фізично неможливе в 4K при 60 FPS навіть на найкращому залізі."),
        ("Від математики до інтелекту", "Замість прорахунку траєкторії кожного фотона, нейромережа генерує фотореалістичний стан світла на основі навчених фізичних патернів."),
        ("Збереження інтерактивності", "Досягти кінематографічного рівня фільмів Pixar у реальному часі без затримок відгуку.")
    ]
    for h, b in bullets3:
        p_h = ctf.add_paragraph()
        p_h.text = "\n✦ " + h
        p_h.font.size = Pt(12)
        p_h.font.bold = True
        p_h.font.color.rgb = CYAN_ACCENT
        p_b = ctf.add_paragraph()
        p_b.text = b
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 4: 2. АКТУАЛЬНІСТЬ РОЗРОБКИ
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4)
    add_top_bar(s4, 4, "Регламент: Пункт 2", "2. Актуальність розробки: виклики сучасного рендерингу")

    cards4 = [
        ("⏱️ Виклик 16,7 мілісекунди", "Часовий ліміт для 60 FPS", "Для плавності в 60 FPS на повний конвеєр є 16,7 мс. У нативному 4K потрібно щомиті рахувати 8,3 мільйона пікселів. Відеокарта задихається без ШІ."),
        ("⚡ Глухий кут кремнію", "Сповільнення закону Мура", "Неможливо безкінечно збільшувати кількість транзисторів: сучасні флагмани вже споживають по 500-600 Вт і виділяють шалене тепло. Потрібен архітектурний стрибок."),
        ("🎭 Проблема «воскової шкіри»", "Межі класичних шейдерів", "Звичайні растеризатори не вміють реалістично симулювати проникнення світла під шкіру людини. Персонажі виглядали як пластикові манекени без життя.")
    ]

    for idx, (title, sub, body) in enumerate(cards4):
        x = Inches(0.8 + idx * 3.95)
        c = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.8), Inches(4.9))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = AMBER_ACCENT if idx == 1 else (NV_GREEN if idx == 0 else CYAN_ACCENT)
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(15)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE

        p2 = ctf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = NV_GREEN

        p3 = ctf.add_paragraph()
        p3.text = "\n" + body
        p3.font.size = Pt(11.5)
        p3.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 5: АРХІТЕКТУРА 3D-GUIDED NEURAL RENDERING (DIAGRAM)
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5)
    add_top_bar(s5, 5, "Архітектура технології", "Конвеєр DLSS 5: 3D-буфери рушія та нейронний синтез світла")

    # Diagram from assets
    img_diag = os.path.join(assets_dir, "image-8-1.png")
    if os.path.exists(img_diag):
        s5.shapes.add_picture(img_diag, Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.6))

    # Architecture Explanation Cards
    arch_cards = [
        ("1. 3D-контекст рушія", "Гра передає буфери глибини (Depth), нормалей поверхонь та вектори руху. ШІ знає просторове розташування кожного пікселя."),
        ("2. Семантична сегментація", "Модель розпізнає матеріали: біологічні тканини (шкіру), тканину одягу, скло, волосся та тип джерела світла."),
        ("3. Творчий контроль", "Розробники керують параметрами Structure, Tone Intensity та масками, зберігаючи задум режисера.")
    ]
    for idx, (title, desc) in enumerate(arch_cards):
        x = Inches(0.8 + idx * 3.95)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.6), Inches(3.8), Inches(2.2))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = NV_GREEN

        p2 = ctf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 6: ВІЗУАЛЬНИЙ ЕФЕКТ: SUBSURFACE SCATTERING (BEFORE / AFTER)
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6)
    add_top_bar(s6, 6, "Візуальне порівняння", "Subsurface Scattering: як DLSS 5 оживляє персонажів")

    # Visual side-by-side skin comparison
    img_skin = os.path.join(assets_dir, "dlss5_neural_skin.jpg")
    if os.path.exists(img_skin):
        s6.shapes.add_picture(img_skin, Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.9))

    c6 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(1.8), Inches(4.9), Inches(4.9))
    c6.fill.solid()
    c6.fill.fore_color.rgb = CARD_BG
    c6.line.color.rgb = NV_GREEN
    ctf = c6.text_frame
    ctf.word_wrap = True

    p = ctf.paragraphs[0]
    p.text = "ЩО ЗМІНЮЄ НЕЙРОННЕ СВІТЛО:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NV_GREEN

    points6 = [
        ("Жива шкіра (Subsurface Scattering)", "Світло проникає крізь епідерміс і розсіюється зсередини. Обличчя втрачає восковий блиск, видно природний тон і мікротіні."),
        ("Волосся та вії", "ШІ формує індивідуальні відблиски на окремих пасмах замість однорідної пласкої плашки шейдера."),
        ("Тканини та шовк", "Фізично точний відблиск і матовість матеріалів одягу залежно від кута падіння променя."),
        ("Незмінна 3D-геометрія", "Полігональна сітка моделі не змінюється ні на міліметр — перетворюється виключно світло.")
    ]
    for h, b in points6:
        p_h = ctf.add_paragraph()
        p_h.text = "\n✦ " + h
        p_h.font.size = Pt(11.5)
        p_h.font.bold = True
        p_h.font.color.rgb = TEXT_WHITE
        p_b = ctf.add_paragraph()
        p_b.text = b
        p_b.font.size = Pt(10)
        p_b.font.color.rgb = TEXT_SLATE

    # -------------------------------------------------------------
    # SLIDE 7: ЖОВТНЕВИЙ ПРОРИВ 2026: ОПТИМІЗАЦІЯ МОДЕЛІ
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7)
    add_top_bar(s7, 7, "Головна новинка осені 2026", "Оновлення від 16 жовтня 2026 року: подолання кризи продуктивності")

    # Banner
    ban = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(0.9))
    ban.fill.solid()
    ban.fill.fore_color.rgb = RGBColor(35, 25, 12)
    ban.line.color.rgb = AMBER_ACCENT
    btf = ban.text_frame
    btf.word_wrap = True
    bp = btf.paragraphs[0]
    bp.text = "⚠️ Початковий виклик: у вересневому релізі важка модель знижувала FPS на 50–60%. Жовтневий драйвер перевернув ситуацію:"
    bp.font.size = Pt(12)
    bp.font.bold = True
    bp.font.color.rgb = AMBER_ACCENT

    # 4 Key Metrics
    metrics = [
        ("У 2x", "Швидша модель", "Оптимізація інференсу вдвічі скоротила час генерації кадру на тензорних ядрах."),
        ("-24%", "Розмір мережі", "Архітектурне стиснення ваг дозволило завантажувати модель у кеш без затримок."),
        ("-20%", "VRAM у 4K", "Звільнено понад 3 ГБ відеопам'яті в роздільності 4K для текстур надвисокої чіткості."),
        ("+35%", "Preset C", "Спеціальний легкий режим, що дав змогу запускати нейронне світло на масових картах RTX 5060.")
    ]

    for idx, (val, title, desc) in enumerate(metrics):
        x = Inches(0.8 + idx * 2.95)
        c = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.95), Inches(2.8), Inches(3.8))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = NV_GREEN
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(36)
        p1.font.bold = True
        p1.font.color.rgb = NV_GREEN

        p2 = ctf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

        p3 = ctf.add_paragraph()
        p3.text = "\n" + desc
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 8: 3. СФЕРА ЗАСТОСУВАННЯ
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8)
    add_top_bar(s8, 8, "Регламент: Пункт 3", "3. Сфера застосування: від геймінгу до віртуального кіновиробництва")

    app_cards = [
        ("🎮 AAA-геймінг нового покоління", "Флагманські проекти (NBA 2K27, Cyberpunk Next). Гравці отримують кінематографічний фотореалізм без лагів."),
        ("🛠️ Графічні веб-рушії та Unreal Engine", "Офіційні плагіни для Unreal Engine 5.5 / 6 та Unity дозволяють студіям вмикати нейронне світло одним перемикачем."),
        ("🎬 Віртуальне кіно (Virtual Production)", "Зйомки фільмів на світлодіодних LED-стінах у реальному часі без необхідності місяцями рендерити сцени на серверах."),
        ("🌐 Хмарний геймінг (GeForce NOW у Web)", "Трансляція ігор наступного покоління через браузер Chrome/Edge на слабкі ноутбуки та смартфони.")
    ]

    for idx, (title, desc) in enumerate(app_cards):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(1.8 + row * 2.5)
        c = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(2.25))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = CYAN_ACCENT if idx % 2 == 1 else NV_GREEN

        p2 = ctf.add_paragraph()
        p2.text = "\n" + desc
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 9: 4. ДОСТУПНІСТЬ ДЛЯ СПОЖИВАЧІВ
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9)
    add_top_bar(s9, 9, "Регламент: Пункт 4", "4. Доступність для споживачів: вимоги, ліцензія та підтримка")

    access_items = [
        ("💻 Апаратні вимоги", "Відеокарти серії GeForce RTX 50 (Blackwell) та RTX 40 з оновленими тензорними ядрами."),
        ("📦 Безкоштовність для гравців", "Технологія активується в налаштуваннях гри без додаткової плати; потрібен лише свіжий драйвер від жовтня 2026."),
        ("👨‍💻 Відкритий SDK розробника", "NVIDIA надає відкритий DLSS 5 SDK без роялті та ліцензійних платежів для авторів ігор і веб-сервісів."),
        ("🎯 Демократизація через Preset C", "Полегшений режим роботи дозволяє запустити нейронний рендеринг навіть на народних відеокартах класу RTX 5060.")
    ]

    for idx, (title, desc) in enumerate(access_items):
        y = Inches(1.8 + idx * 1.25)
        c = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.1))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = title + "  ➔  "
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = NV_GREEN

        run = p1.add_run()
        run.text = desc
        run.font.size = Pt(12)
        run.font.bold = False
        run.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 10: 5. ЕФЕКТ ВІД ВИКОРИСТАННЯ (БЕНЧМАРКИ)
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10)
    add_top_bar(s10, 10, "Регламент: Пункт 5", "5. Ефект від використання: тести у 4K Ultra RT (NBA 2K27, RTX 5090)")

    # Left: FPS Benchmarks Visual Card
    c10_left = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.9))
    c10_left.fill.solid()
    c10_left.fill.fore_color.rgb = CARD_BG
    c10_left.line.color.rgb = NV_GREEN
    ctf = c10_left.text_frame
    ctf.word_wrap = True

    p = ctf.paragraphs[0]
    p.text = "РЕЗУЛЬТАТИ ТЕСТУВАННЯ У 4K ULTRA RT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = NV_GREEN

    fps_stats = [
        ("Без DLSS 5 (Базовий RT)", "128 FPS", TEXT_SLATE, "Традиційне трасування: висока частота, але пластикова шкіра."),
        ("DLSS 5 (До оптимізації)", "63 FPS", AMBER_ACCENT, "Початкова модель: падіння на 51% через складність розрахунку."),
        ("DLSS 5 (Після 16 жовтня)", "105+ FPS", NV_GREEN, "Жовтневий прорив: повний фотореалізм шкіри з комфортним FPS!")
    ]
    for name, fps_val, col, comment in fps_stats:
        p1 = ctf.add_paragraph()
        p1.text = f"\n{name}: {fps_val}"
        p1.font.size = Pt(15)
        p1.font.bold = True
        p1.font.color.rgb = col
        p2 = ctf.add_paragraph()
        p2.text = comment
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT_SLATE

    # Right: Visual Render
    img_beauty = os.path.join(assets_dir, "dlss5_beauty_artifact.jpg")
    if os.path.exists(img_beauty):
        s10.shapes.add_picture(img_beauty, Inches(7.0), Inches(1.8), Inches(5.5), Inches(4.9))

    # -------------------------------------------------------------
    # SLIDE 11: 6. ПЕРСПЕКТИВИ РОЗВИТКУ
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11)
    add_top_bar(s11, 11, "Регламент: Пункт 6", "6. Перспективи розвитку: майбутнє комп'ютерної графіки")

    f_points = [
        ("1. Neural World Models (Світоглядний ШІ)", "Повний відхід від класичної растеризації. ШІ генеруватиме цілі віртуальні світи безпосередньо з фізичних законів і текстових промптів."),
        ("2. Єдина генеративна нейромодель", "Об'єднання масштабування (Super Resolution), генерації кадрів, світла й звуку в одну уніфіковану мультимодальну модель реального часу."),
        ("3. Портування на портативні пристрої та NPU", "Спеціалізована квантизація дозволить запускати нейронний рендеринг на смартфонах, планшетах і портативних консолях майбутнього.")
    ]

    for idx, (title, desc) in enumerate(f_points):
        y = Inches(1.8 + idx * 1.65)
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.4))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = NV_GREEN if idx == 0 else CARD_BORDER
        ctf = c.text_frame
        ctf.word_wrap = True

        p1 = ctf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = NV_GREEN if idx == 0 else TEXT_WHITE

        p2 = ctf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_LIGHT_SLATE

    # -------------------------------------------------------------
    # SLIDE 12: ЗАВЕРШЕННЯ ТА Q&A
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    apply_bg(s12)

    c12 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(1.5), Inches(8.9), Inches(4.5))
    c12.fill.solid()
    c12.fill.fore_color.rgb = CARD_BG
    c12.line.color.rgb = NV_GREEN
    ctf = c12.text_frame
    ctf.word_wrap = True
    ctf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = ctf.paragraphs[0]
    p.text = "ДЯКУЮ ЗА УВАГУ!"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NV_GREEN

    p2 = ctf.add_paragraph()
    p2.text = "\nГотовий відповісти на ваші запитання (Q&A)"
    p2.alignment = PP_ALIGN.CENTER
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    p3 = ctf.add_paragraph()
    p3.text = "\nДоповідач: Лемішка Андрій · ПП-24 · Кафедра САПР"
    p3.alignment = PP_ALIGN.CENTER
    p3.font.size = Pt(13)
    p3.font.color.rgb = CYAN_ACCENT

    out_file = r"D:\Studing\SecondYear\FirstSemester\web\DLSS_Presentation_2026.pptx"
    prs.save(out_file)
    print("SUCCESS: Beautiful presentation saved to", out_file)

if __name__ == "__main__":
    build_gorgeous_deck()
