import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # blank layout

    # Color Palette
    BG_DARK = RGBColor(11, 15, 23)      # #0B0F17
    CARD_BG = RGBColor(22, 30, 49)      # #161E31
    ACCENT_GREEN = RGBColor(118, 185, 0) # NVIDIA Green #76B900
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(156, 163, 175) # Slate 400
    ACCENT_CYAN = RGBColor(6, 182, 212) # Cyan
    ACCENT_AMBER = RGBColor(245, 158, 11)

    assets_dir = r"D:\Studing\SecondYear\FirstSemester\web\assets"

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, slide_num, category, title):
        # Header category badge
        badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf = badge_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"●  {category.upper()}   |   СЛАЙД {slide_num:02d} / 12"
        p.font.name = "Arial"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        tf2 = title_box.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(24)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Hero visual container
    hero_img = os.path.join(assets_dir, "hero_title.jpg")
    if os.path.exists(hero_img):
        s1.shapes.add_picture(hero_img, Inches(7.2), Inches(1.2), Inches(5.3), Inches(5.1))

    # Badge
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.8), Inches(0.45))
    b1.fill.solid()
    b1.fill.fore_color.rgb = RGBColor(18, 40, 10)
    b1.line.color.rgb = ACCENT_GREEN
    b1.text_frame.text = "ТЕХНОЛОГІЇ ВЕБРОЗРОБКИ ТА ДИЗАЙНУ · ШІ-НОВИНКИ 2026"
    b1.text_frame.paragraphs[0].font.size = Pt(10)
    b1.text_frame.paragraphs[0].font.bold = True
    b1.text_frame.paragraphs[0].font.color.rgb = ACCENT_GREEN

    # Title
    t1 = s1.shapes.add_textbox(Inches(0.8), Inches(2.1), Inches(6.2), Inches(2.2))
    tf = t1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "NVIDIA DLSS 5:"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    
    p2 = tf.add_paragraph()
    p2.text = "3D-Guided Neural Rendering"
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    p3 = tf.add_paragraph()
    p3.text = "Прорив нейронного світла та жовтневе оновлення 2026 року"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED

    # Author
    a1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.7), Inches(5.8), Inches(1.6))
    a1.fill.solid()
    a1.fill.fore_color.rgb = CARD_BG
    a1.line.color.rgb = RGBColor(40, 55, 80)
    atf = a1.text_frame
    atf.word_wrap = True
    ap1 = atf.paragraphs[0]
    ap1.text = "Доповідач: Лемішка Андрій"
    ap1.font.bold = True
    ap1.font.size = Pt(15)
    ap1.font.color.rgb = TEXT_WHITE
    ap2 = atf.add_paragraph()
    ap2.text = "Група: ПП-24 · Кафедра САПР"
    ap2.font.size = Pt(12)
    ap2.font.color.rgb = ACCENT_GREEN
    ap3 = atf.add_paragraph()
    ap3.text = "Національний університет «Львівська політехніка»"
    ap3.font.size = Pt(11)
    ap3.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 2: КОНТЕКСТ ТА ЕВОЛЮЦІЯ (2018-2026)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, 2, "Вступний контекст", "Еволюція технології: від апскейлу до нейронного рендерингу")

    cards = [
        ("DLSS 1.0 (2018)", "Окремі мережі", "Тренувалася індивідуально для кожної гри. Часто створювала мильну картинку й артефакти."),
        ("DLSS 2.0 (2020)", "Super Resolution", "Універсальна модель: просторово-часова історія (temporal) + вектори руху. Домальовує 4K з 1080p."),
        ("DLSS 3 & 4 (2022-2025)", "Frame Generation", "Генерація проміжних кадрів за допомогою Optical Flow. Множники кадрів від 2x до 4x MFG."),
        ("DLSS 5 (Осінь 2026)", "Neural Rendering", "ШІ бере на себе повний розрахунок освітлення, шкіри та матеріалів замість Path Tracing.")
    ]

    for idx, (ver, name, desc) in enumerate(cards):
        x = Inches(0.8 + idx * 2.95)
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.8))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_GREEN if "DLSS 5" in ver else RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = ver
        cp1.font.bold = True
        cp1.font.size = Pt(13)
        cp1.font.color.rgb = ACCENT_GREEN if "DLSS 5" in ver else TEXT_MUTED

        cp2 = ctf.add_paragraph()
        cp2.text = name
        cp2.font.bold = True
        cp2.font.size = Pt(15)
        cp2.font.color.rgb = TEXT_WHITE

        cp3 = ctf.add_paragraph()
        cp3.text = "\n" + desc
        cp3.font.size = Pt(11)
        cp3.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 3: 1. МЕТА НОВИНКИ
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, 3, "Регламент: Пункт 1", "1. Мета новинки: для чого створено DLSS 5")

    # Left Card
    c3_1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c3_1.fill.solid()
    c3_1.fill.fore_color.rgb = CARD_BG
    c3_1.line.color.rgb = ACCENT_GREEN
    ctf = c3_1.text_frame
    ctf.word_wrap = True
    p = ctf.paragraphs[0]
    p.text = "🎯 ГОЛОВНА МЕТА"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = ACCENT_GREEN

    p2 = ctf.add_paragraph()
    p2.text = "Заміна математичного трасування променів генеративним ШІ"
    p2.font.bold = True
    p2.font.size = Pt(18)
    p2.font.color.rgb = TEXT_WHITE

    points = [
        "• Подолати межу класичного рендерингу: фізичний розрахунок світла (Path Tracing) вимагає нереальних обчислювальних ресурсів.",
        "• Замість мільярдів математичних променів використати нейромережу, навчену на законах оптики.",
        "• Забезпечити кінематографічний фотореалізм без втрати інтерактивності в реальному часі."
    ]
    for pt in points:
        cp = ctf.add_paragraph()
        cp.text = "\n" + pt
        cp.font.size = Pt(12)
        cp.font.color.rgb = TEXT_MUTED

    # Right Card: Concept visual
    c3_2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c3_2.fill.solid()
    c3_2.fill.fore_color.rgb = CARD_BG
    c3_2.line.color.rgb = RGBColor(40, 55, 80)
    
    img_concept = os.path.join(assets_dir, "dlss_concept.jpg")
    if os.path.exists(img_concept):
        s3.shapes.add_picture(img_concept, Inches(7.0), Inches(2.0), Inches(5.3), Inches(2.8))

    txt_box = s3.shapes.add_textbox(Inches(7.0), Inches(4.9), Inches(5.3), Inches(1.5))
    ttf = txt_box.text_frame
    ttf.word_wrap = True
    tp1 = ttf.paragraphs[0]
    tp1.text = "Ключова зміна парадигми:"
    tp1.font.bold = True
    tp1.font.size = Pt(13)
    tp1.font.color.rgb = ACCENT_CYAN
    tp2 = ttf.add_paragraph()
    tp2.text = "Раніше ШІ допомагав рендерити швидше (апскейл). У DLSS 5 нейромережа безпосередньо створює світло, матеріали та атмосферу сцени."
    tp2.font.size = Pt(11)
    tp2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 4: 2. АКТУАЛЬНІСТЬ РОЗРОБКИ
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, 4, "Регламент: Пункт 2", "2. Актуальність розробки: чому це потрібно саме зараз")

    reasons = [
        ("Виклик 16,7 мілісекунди", "Для плавності 60 FPS на повний кадр є менше ніж 17 мс. У нативному 4K це понад 8 мільйонів пікселів — кремній не встигає."),
        ("Глухий кут «грубої сили»", "Закон Мура сповільнився. Збільшення кількості транзисторів призводить до шаленого енергоспоживання (до 500-600 Вт)."),
        ("Ефект «воскової шкіри»", "Класичні шейдери не можуть правдоподібно передати проникнення світла крізь шкіру та волосся без катастрофічного падіння FPS.")
    ]

    for idx, (title, text) in enumerate(reasons):
        y = Inches(1.8 + idx * 1.65)
        c = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.4))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = f"Проблема {idx+1}: {title}"
        cp1.font.bold = True
        cp1.font.size = Pt(14)
        cp1.font.color.rgb = ACCENT_AMBER if idx == 1 else (ACCENT_GREEN if idx == 0 else ACCENT_CYAN)

        cp2 = ctf.add_paragraph()
        cp2.text = text
        cp2.font.size = Pt(12)
        cp2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 5: ТЕХНОЛОГІЧНА СУТЬ 3D-GUIDED NEURAL RENDERING
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, 5, "Архітектура технології", "Як працює 3D-Guided Neural Rendering під капотом")

    img_skin = os.path.join(assets_dir, "dlss5_neural_skin.jpg")
    if os.path.exists(img_skin):
        s5.shapes.add_picture(img_skin, Inches(0.8), Inches(1.8), Inches(5.5), Inches(4.8))

    c5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.6), Inches(1.8), Inches(5.9), Inches(4.8))
    c5.fill.solid()
    c5.fill.fore_color.rgb = CARD_BG
    c5.line.color.rgb = ACCENT_GREEN
    ctf = c5.text_frame
    ctf.word_wrap = True

    p = ctf.paragraphs[0]
    p.text = "КЛЮЧОВІ МЕХАНІЗМИ ТЕХНОЛОГІЇ"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_GREEN

    points5 = [
        ("Семантичне розуміння сцени", "Модель бачить не просто пікселі, а розпізнає матеріали: біологічну тканину (шкіру), шовк, метал, пасма волосся."),
        ("Підповерхневе розсіювання (Subsurface Scattering)", "Імітація проходження світла під шкіру — зникає ефект пластикового мерця, з'являються живі пори та капілярний тон."),
        ("Збереження 3D-геометрії", "ШІ не змінює форму персонажа. Геометрія і текстури контролюються рушієм гри, а нейромережа відповідає суто за світло."),
        ("Повний контроль розробника", "Художники мають маски та колірні коефіцієнти, щоб режисерське бачення гри не спотворювалося.")
    ]
    for h, b in points5:
        p1 = ctf.add_paragraph()
        p1.text = "\n✦ " + h
        p1.font.bold = True
        p1.font.size = Pt(12)
        p1.font.color.rgb = TEXT_WHITE
        p2 = ctf.add_paragraph()
        p2.text = b
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 6: ПРОРИВ ЖОВТНЯ 2026 РОКУ
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, 6, "Жовтневий прорив 2026", "Оновлення від 16 жовтня 2026: подолання кризи продуктивності")

    banner = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = RGBColor(30, 20, 10)
    banner.line.color.rgb = ACCENT_AMBER
    btf = banner.text_frame
    btf.word_wrap = True
    bp = btf.paragraphs[0]
    bp.text = "⚠️ Початкова проблема: DLSS 5 на першому релізі знижував FPS на 50–60% через складність моделі."
    bp.font.bold = True
    bp.font.size = Pt(13)
    bp.font.color.rgb = ACCENT_AMBER

    # 4 Breakthrough Metric Cards
    metrics = [
        ("У 2 рази швидша", "Швидкість моделі", "Оптимізація архітектури нейромережі подвоїла швидкість генерації світла."),
        ("-24% розмір", "Стиснення ваг", "Зменшено обсяг мережі без втрати візуальної точності."),
        ("-20% VRAM", "Відеопам'ять у 4K", "Звільнено критичні гігабайти пам'яті для текстур ультра-високої роздільності."),
        ("Preset C", "Для RTX 5060", "Полегшений режим для народних карт: до +35% приросту швидкості обробки.")
    ]

    for idx, (val, title, desc) in enumerate(metrics):
        x = Inches(0.8 + idx * 2.95)
        c = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(3.2), Inches(2.8), Inches(3.5))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_GREEN
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = val
        cp1.font.bold = True
        cp1.font.size = Pt(20)
        cp1.font.color.rgb = ACCENT_GREEN

        cp2 = ctf.add_paragraph()
        cp2.text = title
        cp2.font.bold = True
        cp2.font.size = Pt(12)
        cp2.font.color.rgb = TEXT_WHITE

        cp3 = ctf.add_paragraph()
        cp3.text = "\n" + desc
        cp3.font.size = Pt(10.5)
        cp3.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 7: 3. СФЕРА ЗАСТОСУВАННЯ
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, 7, "Регламент: Пункт 3", "3. Сфера застосування: де впроваджується технологія")

    apps = [
        ("🎮 AAA-геймінг наступного покоління", "Провідні ігрові студії інтегрують DLSS 5 для досягнення фотореалістичної графіки у відкритих світах (NBA 2K27, Cyberpunk 2077 Next)."),
        ("🛠️ Графічні рушії (Unreal Engine 5.5 / 6)", "Вбудований плагін дозволяє розробникам ігор в 1 клік підключати нейронний рендеринг матеріалів без переписування коду гри."),
        ("🎬 Віртуальне кіновиробництво (Virtual Production)", "Створення кінодекорацій у реальному часі на світлодіодних екранах (LED volumes) для голлівудських студій."),
        ("🌐 Хмарний веб-геймінг (GeForce NOW у браузері)", "Трансляція ігор кінематографічного рівня через WebRTC прямо у вікно браузера Chrome без потреби мати суперкомп'ютер вдома.")
    ]

    for idx, (title, desc) in enumerate(apps):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(1.8 + row * 2.5)
        c = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(2.2))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = title
        cp1.font.bold = True
        cp1.font.size = Pt(14)
        cp1.font.color.rgb = ACCENT_CYAN if idx % 2 == 1 else ACCENT_GREEN

        cp2 = ctf.add_paragraph()
        cp2.text = "\n" + desc
        cp2.font.size = Pt(11)
        cp2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 8: 4. ДОСТУПНІСТЬ ДЛЯ СПОЖИВАЧІВ
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, 8, "Регламент: Пункт 4", "4. Доступність для споживачів: залізо, софт та ціна")

    items8 = [
        ("💻 Апаратні вимоги", "Відеокарти серії GeForce RTX 50 (Blackwell) та RTX 40 з оновленими тензорними ядрами 5-го покоління."),
        ("📦 Безкоштовність для гравця", "Технологія безкоштовно активується в налаштуваннях гри; потрібен лише драйвер NVIDIA Game Ready від жовтня 2026."),
        ("👨‍💻 Відкритий SDK розробника", "NVIDIA надає безкоштовний DLSS 5 SDK та плагіни для ігрових рушіїв без роялті."),
        ("⚙️ Демократизація через Preset C", "Оптимізований режим дозволяє запускати технологію навіть на масових картах класу RTX 5060.")
    ]

    for idx, (title, desc) in enumerate(items8):
        y = Inches(1.8 + idx * 1.25)
        c = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.1))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = title + "  ➔  "
        cp1.font.bold = True
        cp1.font.size = Pt(13)
        cp1.font.color.rgb = ACCENT_GREEN
        
        run = cp1.add_run()
        run.text = desc
        run.font.bold = False
        run.font.size = Pt(12)
        run.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 9: 5. ЕФЕКТ ВІД ВИКОРИСТАННЯ (БЕНЧМАРКИ)
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, 9, "Регламент: Пункт 5", "5. Ефект від використання: реальні тести у 4K (NBA 2K27, RTX 5090)")

    # Comparison Table
    table_shape = s9.shapes.add_table(5, 3, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
    t = table_shape.table
    t.columns[0].width = Inches(3.2)
    t.columns[1].width = Inches(4.2)
    t.columns[2].width = Inches(4.3)

    data = [
        ("Параметр сцени", "Без DLSS 5 (Класика)", "З DLSS 5 (Оновлення 16 жовтня)"),
        ("Шкіра персонажа", "Гладка, пластикова, без розсіювання", "Живе розсіювання (Subsurface), пори, мікротіні"),
        ("Тканини та волосся", "Спрощені однорідні відблиски", "Шовковий блиск тканин, світло на пасмах"),
        ("4K Ultra RT (RTX 5090)", "128 FPS (базовий)", "105+ FPS (після оптимізації драйвера)"),
        ("1080p Ultra RT", "180 FPS (упор у CPU)", "134 FPS (стабільний фреймрейт)")
    ]

    for row_idx, row in enumerate(data):
        for col_idx, text in enumerate(row):
            cell = t.cell(row_idx, col_idx)
            cell.text = text
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            if row_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(25, 35, 55)
                p.font.bold = True
                p.font.color.rgb = ACCENT_GREEN if col_idx == 2 else TEXT_WHITE
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = CARD_BG if row_idx % 2 == 0 else RGBColor(18, 25, 40)
                p.font.color.rgb = ACCENT_GREEN if col_idx == 2 else TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 10: 6. ПЕРСПЕКТИВИ РОЗВИТКУ
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, 10, "Регламент: Пункт 6", "6. Перспективи розвитку: майбутнє комп'ютерної графіки")

    f_cards = [
        ("1. Neural World Models", "Повний відхід від класичної растеризації. ШІ генеруватиме цілі віртуальні світи безпосередньо з текстових промптів або фізичних моделей."),
        ("2. Єдина генеративна модель", "Об'єднання апскейлу, генерації кадрів, світла і звуку в одну уніфіковану мультимодальну мережу реального часу."),
        ("3. Енергоефективність на NPU", "Портування полегшених моделей DLSS на мобільні чіпи та портативні консолі наступного покоління (Switch 2, смартфони).")
    ]

    for idx, (title, desc) in enumerate(f_cards):
        y = Inches(1.8 + idx * 1.65)
        c = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.4))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_GREEN if idx == 0 else RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = title
        cp1.font.bold = True
        cp1.font.size = Pt(14)
        cp1.font.color.rgb = ACCENT_GREEN if idx == 0 else TEXT_WHITE

        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.size = Pt(12)
        cp2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 11: ПІДСУМОК (РЕЗЮМЕ ЗА 6 ПУНКТАМИ)
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, 11, "Підсумки", "Зведене резюме доповіді за встановленим регламентом")

    summary_items = [
        ("1. Мета:", "Заміна важкої фізики трасування променів нейронним розрахунком світла."),
        ("2. Актуальність:", "Подолання кризи 16,7 мс у роздільності 4K та ліквідація пластикової графіки."),
        ("3. Сфера:", "AAA-ігри (NBA 2K27), Unreal Engine 5.5/6, віртуальне кіновиробництво."),
        ("4. Доступність:", "Безкоштовно для гравців з картами RTX через Game Ready Driver (жовтень 2026)."),
        ("5. Ефект:", "Кінематографічне світло шкіри та тканин; +35% швидкості в Preset C."),
        ("6. Перспективи:", "Перехід до Neural World Models — повної генерації світів нейромережами.")
    ]

    for idx, (label, val) in enumerate(summary_items):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(1.8 + row * 1.65)
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(1.4))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = RGBColor(40, 55, 80)
        ctf = c.text_frame
        ctf.word_wrap = True
        
        cp1 = ctf.paragraphs[0]
        cp1.text = label
        cp1.font.bold = True
        cp1.font.size = Pt(13)
        cp1.font.color.rgb = ACCENT_GREEN

        cp2 = ctf.add_paragraph()
        cp2.text = val
        cp2.font.size = Pt(11.5)
        cp2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------
    # SLIDE 12: ДЯКУЮ ЗА УВАГУ
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)

    c12 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(1.5), Inches(8.9), Inches(4.5))
    c12.fill.solid()
    c12.fill.fore_color.rgb = CARD_BG
    c12.line.color.rgb = ACCENT_GREEN
    ctf = c12.text_frame
    ctf.word_wrap = True

    p = ctf.paragraphs[0]
    p.text = "ДЯКУЮ ЗА УВАГУ!"
    p.alignment = PP_ALIGN.CENTER
    p.font.bold = True
    p.font.size = Pt(36)
    p.font.color.rgb = ACCENT_GREEN

    p2 = ctf.add_paragraph()
    p2.text = "\nГотовий відповісти на ваші запитання (Q&A)"
    p2.alignment = PP_ALIGN.CENTER
    p2.font.bold = True
    p2.font.size = Pt(20)
    p2.font.color.rgb = TEXT_WHITE

    p3 = ctf.add_paragraph()
    p3.text = "\nДоповідач: Лемішка Андрій · ПП-24 · Кафедра САПР"
    p3.alignment = PP_ALIGN.CENTER
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED

    output_path = r"D:\Studing\SecondYear\FirstSemester\web\DLSS що це і як працює.pptx"
    prs.save(output_path)
    print("SUCCESS: Saved presentation to", output_path)

if __name__ == "__main__":
    create_deck()
