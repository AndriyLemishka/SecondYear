"""
Скрипт генерації презентації про DLSS 5 для студентської аудиторії
Стиль: Canva / Modern Dark Tech Keynote з живими ілюстраціями та простими поясненнями
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Ініціалізація та розміри 16:9 ---
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# --- Палітра кольорів Canva Dark Tech ---
BG_COLOR = RGBColor(11, 13, 18)           # Глибокий темний фон
CARD_BG = RGBColor(21, 24, 33)            # Колір карток
CARD_BORDER = RGBColor(38, 43, 58)        # Тонка рамка
PILL_BG = RGBColor(28, 34, 48)            # Фон бейджів

TEXT_WHITE = RGBColor(249, 250, 251)      # Основний білий текст
TEXT_MUTED = RGBColor(165, 172, 186)      # Читабельний світло-сірий
TEXT_DARK_MUTED = RGBColor(107, 114, 128)  # Підписи футера

ACCENT_GREEN = RGBColor(118, 185, 0)      # Фірмовий колір NVIDIA
ACCENT_CYAN = RGBColor(0, 229, 255)       # Неоновий циан (для акцентів)
ACCENT_RED = RGBColor(255, 82, 82)        # Червоний (баги, мінуси, FPS)
ACCENT_AMBER = RGBColor(255, 170, 0)      # Помаранчевий (попередження)

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def apply_slide_base(slide, slide_num, total_slides=10):
    """Створює преміальний фон у стилі Canva з акцентною смужкою та футером."""
    # Фон
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()

    # Верхня неонова смужка
    stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, Inches(0.06))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = ACCENT_GREEN
    stripe.line.fill.background()

    # Нижній фірмовий футер
    footer = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(11.733), Inches(0.32))
    tf = footer.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f"ТЕХНОЛОГІЧНИЙ ДАЙДЖЕСТ: NVIDIA DLSS 5 ПРОСТИМИ СЛОВАМИ  |  СЛАЙД {slide_num:02d} / {total_slides:02d}"
    p.font.size = Pt(8.5)
    p.font.color.rgb = TEXT_DARK_MUTED

def add_header(slide, title_text, category_text, slide_num, total_slides=10):
    """Створює заголовок з бейджем теми та лінією розділювача."""
    apply_slide_base(slide, slide_num, total_slides)

    # Бейдж категорії
    tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.42), Inches(3.6), Inches(0.28))
    tag.fill.solid()
    tag.fill.fore_color.rgb = PILL_BG
    tag.line.color.rgb = CARD_BORDER
    tf_tag = tag.text_frame
    tf_tag.margin_left = Inches(0.12)
    tf_tag.margin_top = Inches(0.02)
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = f"●  {category_text.upper()}"
    p_tag.font.size = Pt(9)
    p_tag.font.bold = True
    p_tag.font.color.rgb = ACCENT_GREEN

    # Номер слайда
    num_box = slide.shapes.add_textbox(Inches(10.533), Inches(0.42), Inches(2.0), Inches(0.3))
    tf_num = num_box.text_frame
    tf_num.margin_right = 0
    p_num = tf_num.paragraphs[0]
    p_num.alignment = PP_ALIGN.RIGHT
    p_num.text = f"ЧАСТИНА {slide_num:02d}"
    p_num.font.size = Pt(9.5)
    p_num.font.bold = True
    p_num.font.color.rgb = TEXT_DARK_MUTED

    # Великий заголовок
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.75))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(23)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE

    # Розділювальна лінія
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.58), Inches(11.733), Inches(0.015))
    divider.fill.solid()
    divider.fill.fore_color.rgb = CARD_BORDER
    divider.line.fill.background()

def create_card(slide, left, top, width, height, title, body_bullets, tag=None, title_color=ACCENT_GREEN, border_color=CARD_BORDER):
    """Створює стильну картку зі списком тез."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)

    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

    if tag:
        p_tag = tf.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(8.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = title_color
        p_tag.space_after = Pt(3)
        p0 = tf.add_paragraph()
    else:
        p0 = tf.paragraphs[0]

    p0.text = title
    p0.font.size = Pt(14.5)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_WHITE
    p0.space_after = Pt(8)

    for bullet in body_bullets:
        p = tf.add_paragraph()
        p.text = f"• {bullet}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(5)

def add_framed_image(slide, img_path, left, top, width, height, caption=""):
    """Додає зображення з витонченою рамкою та підписом."""
    if os.path.exists(img_path):
        # Фонова підкладка-рамка
        frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left - Inches(0.04), top - Inches(0.04), width + Inches(0.08), height + Inches(0.08))
        frame.fill.solid()
        frame.fill.fore_color.rgb = PILL_BG
        frame.line.color.rgb = CARD_BORDER
        frame.line.width = Pt(1)

        # Саме зображення
        slide.shapes.add_picture(img_path, left, top, width, height)

        if caption:
            cbox = slide.shapes.add_textbox(left, top + height + Inches(0.06), width, Inches(0.25))
            ctf = cbox.text_frame
            ctf.margin_top = ctf.margin_left = ctf.margin_bottom = ctf.margin_right = 0
            cp = ctf.paragraphs[0]
            cp.text = caption
            cp.font.size = Pt(8.5)
            cp.font.color.rgb = TEXT_DARK_MUTED
            cp.alignment = PP_ALIGN.CENTER

# ==============================================================================
# СЛАЙД 1: Титульний — Просто та інтригуюче
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
apply_slide_base(s1, 1, 10)

s1_tag = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(4.2), Inches(0.32))
s1_tag.fill.solid()
s1_tag.fill.fore_color.rgb = PILL_BG
s1_tag.line.color.rgb = CARD_BORDER
tf_s1tag = s1_tag.text_frame
tf_s1tag.margin_top = Inches(0.04)
p_s1tag = tf_s1tag.paragraphs[0]
p_s1tag.text = "●  ГЕЙМІНГ ТА ШТУЧНИЙ ІНТЕЛЕКТ 2026"
p_s1tag.font.size = Pt(9.5)
p_s1tag.font.bold = True
p_s1tag.font.color.rgb = ACCENT_GREEN

tbox1 = s1.shapes.add_textbox(Inches(0.8), Inches(2.15), Inches(11.733), Inches(3.2))
tf1 = tbox1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = 0

p_main = tf1.paragraphs[0]
p_main.text = "Що таке DLSS 5 і чому про нього всі говорять?"
p_main.font.size = Pt(38)
p_main.font.bold = True
p_main.font.color.rgb = TEXT_WHITE
p_main.space_after = Pt(12)

p_sub = tf1.add_paragraph()
p_sub.text = "Як штучний інтелект навчився домальовувати ігри: від порятунку слабких ПК до скандального «AI-макіяжу» та відеокарт на 800 Ват."
p_sub.font.size = Pt(17)
p_sub.font.color.rgb = TEXT_MUTED
p_sub.space_after = Pt(26)

p_author = tf1.add_paragraph()
p_author.text = "Доповідь для студентів: розбираємося «на пальцях» без складної математики"
p_author.font.size = Pt(12)
p_author.font.color.rgb = ACCENT_CYAN

pills = [
    ("ПРОСТА АНАЛОГІЯ", "ШІ як художник-помічник", ACCENT_GREEN),
    ("ГОЛОВНИЙ ПАРАДОКС", "Чому нова версія знижує FPS?", ACCENT_RED),
    ("ГУЧНИЙ СКАНДАЛ", "«Б'юті-фільтр» у горор-грі", ACCENT_AMBER),
]
for idx, (p_cat, p_val, p_col) in enumerate(pills):
    c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + idx * 3.95), Inches(5.5), Inches(3.8), Inches(1.05))
    c.fill.solid()
    c.fill.fore_color.rgb = CARD_BG
    c.line.color.rgb = CARD_BORDER
    c_tf = c.text_frame
    c_tf.margin_left = Inches(0.2)
    c_tf.margin_top = Inches(0.12)
    cp0 = c_tf.paragraphs[0]
    cp0.text = p_cat
    cp0.font.size = Pt(8.5)
    cp0.font.bold = True
    cp0.font.color.rgb = p_col
    cp0.space_after = Pt(3)
    cp1 = c_tf.add_paragraph()
    cp1.text = p_val
    cp1.font.size = Pt(12)
    cp1.font.bold = True
    cp1.font.color.rgb = TEXT_WHITE

s1.notes_slide.notes_text_frame.text = (
    "Слова для початку доповіді:\n"
    "Привіт усім! Підніміть руки, хто любить грати в комп'ютерні ігри на ПК або ноутбуці? "
    "Майже всі стикалися з тим, що нова крута гра починає безбожно гальмувати, кулери ревуть, "
    "а замість плавної картинки ми бачимо слайдшоу. Сьогодні ми поговоримо про магічну кнопку під назвою DLSS — "
    "як компанія NVIDIA використовує штучний інтелект, щоб рятувати наші відеокарти, і чому новітня 5-та версія "
    "викликала справжній бунт серед геймерів та розробників."
)

# ==============================================================================
# СЛАЙД 2: Що таке DLSS? Пояснення на пальцях + ІНФОГРАФІКА
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Що взагалі таке DLSS? Проста аналогія з художником", "ОСНОВИ НА ПАЛЬЦЯХ", 2, 10)

# Вставляємо інфографіку зліва
img_s2 = os.path.join(ASSETS_DIR, "dlss_concept.jpg")
add_framed_image(s2, img_s2, Inches(0.8), Inches(1.85), Inches(6.0), Inches(4.45), "Схема: Від ескізу 1080p до чіткого 4K через нейромережу")

# Картки пояснення справа
create_card(
    s2,
    Inches(7.1),
    Inches(1.85),
    Inches(5.433),
    Inches(2.15),
    "1. У чому проблема відеокарти?",
    [
        "Сучасні монітори мають роздільність 4K — це понад 8 000 000 пікселів!",
        "Відеокарта мусить малювати цю величезну картину 60 або 120 разів на секунду.",
        "Результат: Карта перегрівається, не встигає, і гра починає моторошно лагати."
    ],
    tag="ПРОБЛЕМА: НАВАНТАЖЕННЯ",
    title_color=ACCENT_RED
)

create_card(
    s2,
    Inches(7.1),
    Inches(4.15),
    Inches(5.433),
    Inches(2.45),
    "2. Як DLSS рятує ситуацію?",
    [
        "Аналогія: Замість малювання гігантської картини, відеокарта малює швидкий маленький ескіз (наприклад, 1080p — це в 4 рази легше!).",
        "Тут підключається ШІ: Спеціальний нейропомічник домальовує відсутні пікселі.",
        "Фінал: Ви бачите чітку 4K картинку, а гра летить у 2 рази швидше!"
    ],
    tag="РІШЕННЯ: ШТУЧНИЙ ІНТЕЛЕКТ",
    title_color=ACCENT_GREEN
)

s2.notes_slide.notes_text_frame.text = (
    "Як пояснити цей слайд аудиторії:\n"
    "Уявіть, що вам на іспиті треба за 10 хвилин написати твір на 10 сторінок дрібним ідеальним почерком. "
    "Ви фізично зламаєте руку. Але якщо ви швидко напишете чернетку тезами, а ваш сусід-відмінник (ШІ) "
    "за секунду розгорне це в каліграфічний шедевр — ви встигнете на відмінно!\n"
    "Ось це і робить класичний DLSS: відеокарта малює полегшену картинку, а тензорні ядра за допомогою нейромережі "
    "перетворюють її на чітке 4K без втрати якості."
)

# ==============================================================================
# СЛАЙД 3: Еволюція DLSS (Від 1 до 5) — Зрозумілими словами
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Як розвивалася технологія: Від простої лупи до генератора світла", "ХРОНОЛОГІЯ", 3, 10)

cards_s3 = [
    ("DLSS 1 & 2 (2018–2020)", "«РОЗУМНЕ ЗБІЛЬШЕННЯ»", [
        "Що робить: Збільшує маленьку картинку до великої (1080p $\\to$ 4K).",
        "Аналогія: Розумний Photoshop, який знає, як виглядають текстури цегли, трави чи металу.",
        "Результат для гравця: +50–100% безкоштовного приросту FPS!"
    ], ACCENT_GREEN),
    ("DLSS 3 (2022)", "«КАДРИ З ПОВІТРЯ»", [
        "Що робить: ШІ сам вигадує цілі проміжні кадри (Frame Generation).",
        "Аналогія: Мультиплікатор, який домальовує рух персонажа між двома малюнками.",
        "Результат для гравця: Гра стає плавною, навіть якщо процесор старий і не тягне."
    ], ACCENT_GREEN),
    ("DLSS 5 (2026)", "«НЕЙРОХУДОЖНИК СВІТЛА»", [
        "Що робить: Більше НЕ додає FPS! ШІ бере на себе малювання фізики світла.",
        "Аналогія: Замість симуляції мільярдів променів сонця, ШІ 'фарбує' сцену за фотографіями.",
        "Результат для гравця: Нереальна кінематографічна картинка, але FPS падає вдвічі!"
    ], ACCENT_RED),
]

for idx, (t_title, t_tag, t_bullets, t_color) in enumerate(cards_s3):
    create_card(
        s3,
        Inches(0.8 + idx * 3.95),
        Inches(1.85),
        Inches(3.83),
        Inches(4.2),
        t_title,
        t_bullets,
        tag=t_tag,
        title_color=t_color
    )

bot_s3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.72))
bot_s3.fill.solid()
bot_s3.fill.fore_color.rgb = PILL_BG
bot_s3.line.color.rgb = CARD_BORDER
bot_tf = bot_s3.text_frame
bot_tf.margin_left = Inches(0.25)
bot_tf.margin_top = Inches(0.12)
p_b1 = bot_tf.paragraphs[0]
p_b1.text = "ГОЛОВНИЙ ПОВОРОТ:"
p_b1.font.size = Pt(9.5)
p_b1.font.bold = True
p_b1.font.color.rgb = ACCENT_AMBER
p_b2 = bot_tf.add_paragraph()
p_b2.text = "Раніше DLSS означав 'увімкни, щоб не гальмувало'. У 2026 році з DLSS 5 все навпаки: це режим 'зроби фільм, навіть якщо комп'ютер закипить'."
p_b2.font.size = Pt(10.5)
p_b2.font.color.rgb = TEXT_WHITE

s3.notes_slide.notes_text_frame.text = (
    "Як подати еволюцію:\n"
    "Студенти мають запам'ятати просту річ: раніше DLSS був прискорювачем. "
    "Він рятував старі відеокарти. А DLSS 5 — це вже не прискорювач, це суперважкий генератор реалізму. "
    "NVIDIA зберегла ту саму назву з чотирьох літер просто для маркетингу, але сутність технології змінилася на 180 градусів."
)

# ==============================================================================
# СЛАЙД 4: Як працює DLSS 5 (Neural Skin) + ПОРІВНЯЛЬНЕ ФОТО
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "DLSS 5 на практиці: Як ШІ оживляє комп'ютерну графіку", "ПОРІВНЯННЯ В РЕАЛЬНОСТІ", 4, 10)

img_s4 = os.path.join(ASSETS_DIR, "dlss5_neural_skin.jpg")
add_framed_image(s4, img_s4, Inches(0.8), Inches(1.85), Inches(6.4), Inches(4.45), "Порівняння: Звичайний 3D-рендер (зліва) проти нейрорендерингу DLSS 5 (справа)")

create_card(
    s4,
    Inches(7.5),
    Inches(1.85),
    Inches(5.033),
    Inches(2.15),
    "1. Що таке 3D-каркас?",
    [
        "Гра не вигадує світ з голови (як звичайний ChatGPT чи Midjourney).",
        "Гра дає точні координати: де стоїть герой, куди повернута голова, де стіна.",
        "Тому персонажі не провалюються крізь підлогу, а зброя стріляє точно в ціль."
    ],
    tag="ГЕОМЕТРІЯ З РУШІЯ",
    title_color=ACCENT_CYAN
)

create_card(
    s4,
    Inches(7.5),
    Inches(4.15),
    Inches(5.033),
    Inches(2.45),
    "2. Магія живого світла",
    [
        "Подивіться на вуха й щоки на картинці: світло сонця проходить крізь шкіру (ефект Subsurface Scattering).",
        "Очі виглядають вологими та живими, а не скляними кульками.",
        "Замість того, щоб годинами прораховувати кожен промінь сонця, нейромережа малює це за 8 мілісекунд!"
    ],
    tag="НЕЙРОННЕ ОСВІТЛЕННЯ",
    title_color=ACCENT_GREEN
)

s4.notes_slide.notes_text_frame.text = (
    "Коментар до візуального порівняння:\n"
    "Покажіть аудиторії на екран: зліва — звичайна графіка, яку ми бачимо у більшості сучасних ігор. "
    "Шкіра виглядає як пластик або матовий гіпс, тіні рубані, обличчя пласке.\n"
    "Праворуч — DLSS 5. Зверніть увагу на м'якість світла, пори шкіри, живе відбиття у зіницях. "
    "Це виглядає як реальний кадр із дорогого голлівудського фільму. І все це домальовано нейромережею прямо на ходу!"
)

# ==============================================================================
# СЛАЙД 5: Парадокс продуктивності (Простими цифрами)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Парадокс швидкодії: Чому комп'ютер починає грітися як праска?", "ЦІНА РЕАЛІЗМУ", 5, 10)

def create_simple_kpi(slide, left, top, width, height, val, title, desc, color):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BORDER
    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0
    p0 = tf.paragraphs[0]
    p0.text = val
    p0.font.size = Pt(36)
    p0.font.bold = True
    p0.font.color.rgb = color
    p0.space_after = Pt(2)
    p1 = tf.add_paragraph()
    p1.text = title.upper()
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(4)
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED

create_simple_kpi(s5, Inches(0.8), Inches(1.85), Inches(3.8), Inches(2.2), "-60%", "Мінус половина FPS", "Увімкнули DLSS 5 у грі — лічильник кадрів миттєво обвалився з 190 до 95 FPS.", ACCENT_RED)
create_simple_kpi(s5, Inches(4.75), Inches(1.85), Inches(3.8), Inches(2.2), "800 Вт", "Пекельне енергоспоживання", "Відеокарта тягне струм як електричний чайник або потужний масляний обігрівач.", ACCENT_AMBER)
create_simple_kpi(s5, Inches(8.7), Inches(1.85), Inches(3.83), Inches(2.2), "8 GB = Смерть", "Брак відеопам'яті", "Дешеві карти просто вилітають на робочий стіл, бо нейромережа не влазить у пам'ять.", ACCENT_RED)

create_card(
    s5,
    Inches(0.8),
    Inches(4.3),
    Inches(11.733),
    Inches(2.55),
    "Логічне запитання: Якщо FPS падає, нащо воно взагалі треба?",
    [
        "Справжнє порівняння: Порівнювати DLSS 5 треба не зі звичайною грою, а зі спробою порахувати таке світло «по-чесному» (через трасування променів).",
        "Якби карта рахувала кожен промінь сонця вручну: Навіть найдорожча карта за $2000 видала б не 98 кадрів, а всього 5–8 кадрів на секунду (неграбельне слайдшоу).",
        "Висновок: Для нас падіння FPS виглядає як мінус, але для розробників це диво — вони отримали графіку майбутнього вже сьогодні."
    ],
    tag="ПОЯСНЕННЯ ДЛЯ СКЕПТИКІВ",
    title_color=ACCENT_GREEN
)

s5.notes_slide.notes_text_frame.text = (
    "Слова для пояснення парадоксу:\n"
    "Уявіть шок пересічного геймера. Він купує новеньку відеокарту за шалені гроші, вмикає гру, бачить напис DLSS 5, "
    "натискає 'Увімкнути'... і замість приросту швидкості отримує мінус 60% FPS! Всі фанатські форуми гудуть від люті.\n"
    "Але фокус у тому, що без цього ШІ таку картинку ми взагалі змогли б запустити лише десь у 2035 році. "
    "NVIDIA просто перестрибнула час ціною шаленого енергоспоживання."
)

# ==============================================================================
# СЛАЙД 6: Скандал з обличчям Грейс (Resident Evil) + ІЛЮСТРАЦІЯ
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Головний скандал: Як ШІ перетворив горор на гламурний кліп", "КОНФЛІКТ АРТУ ТА АЛГОРИТМІВ", 6, 10)

img_s6 = os.path.join(ASSETS_DIR, "dlss5_beauty_artifact.jpg")
add_framed_image(s6, img_s6, Inches(0.8), Inches(1.85), Inches(6.4), Inches(4.45), "Інцидент Capcom: Автентичний виснажений горор (зліва) проти 'AI б'юті-фільтра' (справа)")

create_card(
    s6,
    Inches(7.5),
    Inches(1.85),
    Inches(5.033),
    Inches(2.15),
    "1. Що сталося на показі гри?",
    [
        "NVIDIA показала трейлер горору Resident Evil Requiem.",
        "Головна героїня Грейс цілу ніч тікала від монстрів, була в крові, бруді та поті.",
        "Але DLSS 5 вирішив: 'Шкіра має бути ідеальною!' — і замазав усі зморшки та бруд глянцевим блиском."
    ],
    tag="ІНЦИДЕНТ CAPCOM",
    title_color=ACCENT_RED
)

create_card(
    s6,
    Inches(7.5),
    Inches(4.15),
    Inches(5.033),
    Inches(2.45),
    "2. Чому геймери обурилися?",
    [
        "Втрата атмосфери: Замість страшного горору картинка стала схожою на рекламу шампуню чи макіяжу з Instagram.",
        "Ефект 'Мертвої ляльки' (Uncanny Valley): Обличчя виглядає восковим і лякає, бо рухи не відповідають глянцю.",
        "Розробники гри були шоковані тим, що ШІ самовільно спотворив їхній авторський стиль."
    ],
    tag="ЕФЕКТ AI SLOP",
    title_color=ACCENT_AMBER
)

s6.notes_slide.notes_text_frame.text = (
    "Історія для живого виступу (дуже заходить аудиторії!):\n"
    "Ось тут починається найцікавіше! Подивіться на зображення. Зліва — те, що малювали художники Capcom: "
    "виснажена жінка, яка бореться за виживання в підземеллі. Справа — те, що з нею зробив DLSS 5. "
    "Нейромережа натренована на мільйонах красивих фоточок із софітами, тому вона вважає, що брудне обличчя — "
    "це дефект, який треба 'замазати тональним кремом'.\n"
    "Цей випадок показав, що ШІ не має естетичного смаку: для нього краса — це просто статистика."
)

# ==============================================================================
# СЛАЙД 7: Хроніка дефектів (Від вазеліну до ботоксу)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Хроніка дефектів: З якими багами боролися в різні роки?", "ІСТОРІЯ АРТЕФАКТІВ", 7, 10)

s7_cards = [
    ("DLSS 1.0 (2018)", "«ЕПОХА ВАЗЕЛІНУ»", [
        "Картинка розмивалася в динаміці так, ніби монітор змастили жиром.",
        "Тексти на вивісках у грі ставали нечитабельними.",
        "Причина: ШІ ще не розумів, як рухаються предмети."
    ], ACCENT_RED),
    ("DLSS 2 та 3 (2020–2023)", "«ПРИМАРНІ ШЛЕЙФИ»", [
        "Ghosting: За машинами, птахами та прицілами зброї тягнулися темні 'хвости'.",
        "Тремтіння інтерфейсу: ШІ плутав міні-карту з фоном гри, і карта дрижала.",
        "Причина: Помилки прорахунку векторів швидкості."
    ], ACCENT_AMBER),
    ("DLSS 5 (2026)", "«ВОСКОВИЙ БОТОКС»", [
        "Всі персонажі виглядають так, ніби намазалися олією для засмаги.",
        "Штучні яскраві відблиски там, де мала бути темна брудна печера.",
        "Причина: Перенавчання моделі на глянцевих фотографіях."
    ], ACCENT_RED),
]

for idx, (t_title, t_tag, t_bullets, t_color) in enumerate(s7_cards):
    create_card(
        s7,
        Inches(0.8 + idx * 3.95),
        Inches(1.85),
        Inches(3.83),
        Inches(5.0),
        t_title,
        t_bullets,
        tag=t_tag,
        title_color=t_color
    )

s7.notes_slide.notes_text_frame.text = (
    "Смішні аналогії для виступу:\n"
    "Якщо подивитися на історію, ШІ завжди хворів на якісь 'дитячі хвороби'.\n"
    "У першій версії ми бігали ніби в окулярах із сильними діоптріями. У другій версії за кожним патроном "
    "летів примарний хвіст, як у фільмах про привидів. А в п'ятій версії всі шахтарі, орки та монстри "
    "виглядають так, ніби щойно вийшли з дорогого корейського спа-салону!"
)

# ==============================================================================
# СЛАЙД 8: Лінь розробників (Головна біль індустрії)
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Чому гравці зляться? Лінь розробників та криза оптимізації", "РЕАЛЬНІСТЬ ІНДУСТРІЇ", 8, 10)

create_card(
    s8,
    Inches(0.8),
    Inches(1.85),
    Inches(5.75),
    Inches(4.9),
    "ШІ як «милиця» замість нормального коду",
    [
        "Сумна тенденція: Ігри виходять сирими та неоптимізованими.",
        "Відмазка студій: 'Навіщо ми будемо пів року оптимізувати гру, якщо гравець може просто натиснути кнопку DLSS?'.",
        "Скорочення штату: Компанії звільняють інженерів та тестувальників, перекладаючи роботу на штучний інтелект.",
        "У підсумку: Гра з графікою 2018 року вимагає відеокарту 2026 року."
    ],
    tag="ХВОРОБА СУЧАСНОГО ГЕЙМДЕВУ",
    title_color=ACCENT_RED
)

create_card(
    s8,
    Inches(6.8),
    Inches(1.85),
    Inches(5.733),
    Inches(4.9),
    "А що робити нереалістичним іграм?",
    [
        "Стилізовані ігри під загрозою: Що робити шедеврам на кшталт Valheim, Dishonored або Hades, де краса полягає у малюнку від руки?",
        "Спроба все зрівняти: Якщо прогнати мультяшну гру через DLSS 5, ШІ спробує зробити її фотореалістичною і повністю вб'є стиль.",
        "Рішення: NVIDIA додала повзунки сили впливу ШІ, але більшість лінивих розробників навіть не будуть їх налаштовувати."
    ],
    tag="ЗАГРОЗА ДЛЯ МИСТЕЦТВА",
    title_color=ACCENT_CYAN
)

s8.notes_slide.notes_text_frame.text = (
    "Спілкування з аудиторією:\n"
    "Тут можна звернутися до залу: згадайте останні релізи ігор. Скільки разів ви купували гру на релізі, "
    "а вона лагала навіть на потужному компі? Розробники просто розлінилися. Замість того, щоб вичищати баги, "
    "вони кажуть: 'Ну, увімкніть генерацію кадрів і DLSS, і буде 60 FPS'. Це нечесно щодо гравців, "
    "бо замість прогресу ми отримуємо просто милицю для ледачих програмістів."
)

# ==============================================================================
# СЛАЙД 9: Студенти й моддери рятують ситуацію (ReShade)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Як ентузіасти й моддери переграли корпорацію NVIDIA", "СИЛА СПІЛЬНОТИ", 9, 10)

create_card(
    s9,
    Inches(0.8),
    Inches(1.85),
    Inches(5.75),
    Inches(4.9),
    "Злом та запуск на старіших відеокартах",
    [
        "Офіційно: NVIDIA заявила, що DLSS 5 працюватиме ТІЛЬКИ на найновіших і шалено дорогих картах RTX 50.",
        "Реальність: Вже через тиждень після витоку файлів фанати створили безкоштовні моди через програму ReShade.",
        "Диво народної оптимізації: Технологію змогли запустити навіть на старій відеокарті RTX 2070 шестирічної давнини!",
        "Підтримка улюблених ігор: Моддери додали нейрорендер у «Відьмака 3», Cyberpunk та S.T.A.L.K.E.R. 2."
    ],
    tag="ПЕРЕМОГА ЕНТУЗІАСТІВ",
    title_color=ACCENT_GREEN
)

create_card(
    s9,
    Inches(6.8),
    Inches(1.85),
    Inches(5.733),
    Inches(4.9),
    "Налаштування, які мали зробити інженери",
    [
        "Повернення 60 FPS: Моддери додали простий повзунок роздільності моделі (можна знизити апетит ШІ на 25% і грати плавно).",
        "Захист інтерфейсу: Приціл зброї та карта більше не розмиваються.",
        "Вимкнення 'ботоксу': Можна легко зменшити глянець на обличчях, повернувши героям їхній брудний і суворий вигляд.",
        "Мораль: Спільнота довела, що технологія чудова, якщо не закривати її в жадібні корпоративні рамки."
    ],
    tag="ФАНАТСЬКІ ПОКРАЩЕННЯ",
    title_color=ACCENT_CYAN
)

s9.notes_slide.notes_text_frame.text = (
    "Чому цей слайд важливий:\n"
    "Це найпозитивніша частина доповіді. Студенти та ентузіасти по всьому світу зібралися на Reddit і GitHub, "
    "розібрали закритий код NVIDIA і зробили його зручним для людей. Вони показали: нам не потрібні штучні "
    "маркетингові обмеження. Якщо дати гравцям прості повзунки регулювання, технологія стає справжнім шедевром!"
)

# ==============================================================================
# СЛАЙД 10: Підсумки та відкриті питання
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Підсумок: Куди котиться графіка і запитання до вас", "ВИСНОВКИ & ОБГОВОРЕННЯ", 10, 10)

create_card(
    s10,
    Inches(0.8),
    Inches(1.85),
    Inches(5.75),
    Inches(4.1),
    "Головні висновки простими словами",
    [
        "1. Назад дороги немає: Епоха, коли відеокарта чесно малювала кожен піксель за математичними формулами, закінчилася.",
        "2. Майбутнє вже тут: Графіка майбутнього буде гібридною — проста 3D-модель від гри плюс розумне нейродомальовування від ШІ.",
        "3. Головне випробування: Чи потягне DLSS 5 майбутню GTA VI на ПК без вибухів блоків живлення та дивних артефактів?"
    ],
    tag="ФАКТИ",
    title_color=ACCENT_GREEN
)

create_card(
    s10,
    Inches(6.8),
    Inches(1.85),
    Inches(5.733),
    Inches(4.1),
    "Питання до залу (Давайте посперечаємося!)",
    [
        "Питання №1 (Геймерське):\n«Ви готові змиритися з тим, що у вас буде 45 кадрів замість 100, зате персонажі будуть виглядати як живі люди з кіно?»",
        "Питання №2 (Філософське):\n«Якщо обличчя героя та світло в кімнаті домалював штучний інтелект за фотографіями — це ще гра розробників чи вже мультик від нейромережі?»"
    ],
    tag="ДИСКУСІЯ",
    title_color=ACCENT_AMBER
)

fin_box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.12), Inches(11.733), Inches(0.72))
fin_box.fill.solid()
fin_box.fill.fore_color.rgb = PILL_BG
fin_box.line.color.rgb = ACCENT_GREEN
fin_tf = fin_box.text_frame
fin_tf.margin_left = Inches(0.25)
fin_tf.margin_top = Inches(0.12)
fin_p = fin_tf.paragraphs[0]
fin_p.text = "ДЯКУЮ ЗА УВАГУ! ЧЕКАЮ НА ВАШІ ДУМКИ ТА ВІДПОВІДІ НА ЗАПИТАННЯ."
fin_p.font.size = Pt(11.5)
fin_p.font.bold = True
fin_p.font.color.rgb = ACCENT_GREEN
fin_p.alignment = PP_ALIGN.CENTER

s10.notes_slide.notes_text_frame.text = (
    "Фінальні слова:\n"
    "Дякую всім за увагу! Я сподіваюся, тепер абревіатура DLSS не лякає вас складними термінами. "
    "Перед тим, як ми розійдемося, мені дуже цікаво почути ваші відповіді на ці два питання. "
    "Особливо перше: що оберете ви — максимальну плавність і 120 FPS чи кінематографічну графіку ціною нагріву кімнати?"
)

# --- Збереження оновленої презентації ---
output_filename = "DLSS5_Student_Visual_Keynote.pptx"
prs.save(output_filename)
print(f"Оновлену презентацію з картинками збережено: {output_filename}")
