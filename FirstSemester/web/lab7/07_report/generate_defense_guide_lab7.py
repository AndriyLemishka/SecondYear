# -*- coding: utf-8 -*-
"""
Генератор пам'ятки / підготовки до захисту лабораторної роботи №7
Тема: «Проєктування та реалізація повноцінного лендингу»
Проєкт: ChargeUA
Студент: Лемішка Андрій Андрійович, ПП-24
НУ «Львівська політехніка», Кафедра САПР
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"D:\Studing\SecondYear\FirstSemester\web\lab7"
DOCX_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л7_Підготовка_до_захисту.docx")
PDF_OUT = os.path.join(BASE_DIR, "Лемішка_ПП-24_Л7_Підготовка_до_захисту.pdf")

COLOR_PRIMARY = RGBColor(0, 80, 160)     # Академічний синій
COLOR_DARK = RGBColor(15, 23, 42)        # Slate 900
COLOR_MUTED = RGBColor(71, 85, 105)      # Slate 600

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

def create_guide():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    def set_font(run, size=11, bold=False, italic=False, color=COLOR_DARK):
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.LEFT, before=2, after=4, line_spacing=1.15):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            r = p.add_run(text)
            set_font(r)
        return p

    def add_h1(text):
        p = add_p(before=12, after=4)
        r = p.add_run(text)
        set_font(r, size=13.5, bold=True, color=COLOR_PRIMARY)
        return p

    def add_h2(text):
        p = add_p(before=8, after=2)
        r = p.add_run(text)
        set_font(r, size=12, bold=True, color=COLOR_DARK)
        return p

    # Шапка
    p_title = add_p("ШПАРГАЛКА ТА ПАМ'ЯТКА ДО ЗАХИСТУ ЛР №7", align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=2)
    set_font(p_title.runs[0], size=15, bold=True, color=COLOR_PRIMARY)
    
    p_sub = add_p("Тема: «Проєктування та реалізація повноцінного лендингу» | Вебпроєкт «ChargeUA»\nСтудент: Лемішка Андрій Андрійович, ПП-24 | Викладач: к.т.н., доц. Юрчак І. Ю.", align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=12)
    set_font(p_sub.runs[0], size=10.5, italic=True)

    add_h1("1. Ключові концепції та терміни ЛР №7 (Глосарій)")
    terms = [
        ("Ітераційний промптинг (Iterative Prompting)", "Поетапне нарощування функціоналу вебінтерфейсу через серію послідовних запитів до ШІ (від каркасу до точкового рефакторингу). Головна перевага — 100% збереження контролю розробника над кодом та виключення галюцинацій нейромережі."),
        ("Метод Pick Element", "Точковий рефакторинг ізольованого елемента або компонента. Розробник явно обмежує ШІ у промпті: «працюй тільки з кнопкою CTA, не змінюй решту сайту», що дозволяє тонко відкалібрувати класи без ризику поламати макет."),
        ("Ембединг (Embedding) та <iframe>", "Технологія безпечного вбудовування стороннього медіа-вмісту (карти Google Maps, відео YouTube, віджети) через тег <iframe>. Створює ізольований контекст браузера."),
        ("Адаптивність через aspect-ratio: 16/9", "Сучасна нативна CSS-властивість (або клас aspect-video в Tailwind), яка замінила застарілі «padding-bottom 56.25% хаки» і гарантує збереження пропорцій відео на будь-якому розмірі екрану без переповнення."),
        ("Атрибути безпеки та продуктивності", "loading='lazy' — відкладає завантаження важких карт та відео до моменту наближення до зони видимості; referrerpolicy='no-referrer-when-downgrade' — захищає приватність користувача; title — обов'язковий за стандартом WCAG (доступність екранних читачів WAI-ARIA)."),
        ("Семантичний тег <aside>", "Призначений для дотичного та додаткового контенту. У нашому лендингу в <aside> загорнуто віджет погоди Львова та статусу енергосистеми хабів.")
    ]
    for name, desc in terms:
        p = add_p(before=2, after=3)
        r1 = p.add_run(f"• {name}: ")
        set_font(r1, size=11, bold=True)
        r2 = p.add_run(desc)
        set_font(r2, size=10.5)

    add_h1("2. Готові відповіді на топ-запитання викладача під час захисту")
    qa = [
        ("Чому не можна копіювати <iframe> YouTube 'з коробки'?", 
         "Тому що за замовчуванням YouTube дає фіксовані розміри (width='560' height='315'). На смартфонах шириною 320–375px такий фрейм вилазить за межі екрана і створює горизонтальний скрол. Ми обгорнули фрейм у контейнер із класом aspect-video (або aspect-ratio: 16/9 у CSS) та width: 100%."),
        ("Як у вас поєднано Tailwind CSS та зовнішній style.css?", 
         "Tailwind CSS підключено через CDN для швидкої утилітарної верстки каркасу, сіток та станів. А в :root файлу style.css винесено дизайн-токени за методичкою (--video-max-width: 960px, --video-radius: 1rem, кольори бренду) для централізованого керування медіа-контейнерами."),
        ("Чому в проєкті ChargeUA немає кошика чи форми оплати?", 
         "Згідно з офіційною специфікацією та бізнес-правилом проєкту, ChargeUA є виключно безкоштовним навігаційним помічником та агрегатором живих статусів у блекаути. Усі форми оплати, білінгу чи бронювання категорично заборонені специфікацією."),
        ("Які результати показав аудит Google Lighthouse?", 
         "100/100 Best Practices, 96/100 Accessibility (високий контраст тексту та WCAG ARIA-мітки), 0 мс блокування потоку, 100% адаптивність без горизонтального скролу.")
    ]
    for q, a in qa:
        add_h2(q)
        p = add_p(before=1, after=4)
        r = p.add_run(a)
        set_font(r, size=10.5)

    add_h1("3. Фінальний чек-лист перед показом викладачу")
    checks = [
        "[+] Запустити проєкт через Live Server (http://localhost:5500 або http://127.0.0.1:5500).",
        "[+] Перевірити F12 Console: 0 помилок 404 (всі картинки та стилі відносні).",
        "[+] Відкрити режим емуляції мобільних (Ctrl+Shift+M, iPhone SE 375px): протестувати гамбургер-меню, переконатися у відсутності горизонтального скролу.",
        "[+] Прокрутити до карти Google Maps та відео YouTube: показати коректне вбудовування з loading='lazy'.",
        "[+] Мати відкритим підготовлений звіт у PDF (Лемішка_ПП-24_Л7_ChargeUA.pdf)."
    ]
    for c in checks:
        p = add_p(before=1, after=2)
        r = p.add_run(c)
        set_font(r, size=10.5, bold=True)

    print("Збереження пам'ятки...")
    doc.save(DOCX_OUT)
    
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc_com = word.Documents.Open(os.path.abspath(DOCX_OUT))
        doc_com.SaveAs(os.path.abspath(PDF_OUT), FileFormat=17)
        doc_com.Close()
        word.Quit()
        print("PDF пам'ятки успішно створено!")
    except Exception as e:
        print(f"Помилка створення PDF пам'ятки: {e}")

if __name__ == "__main__":
    create_guide()
