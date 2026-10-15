# -*- coding: utf-8 -*-
import re

source_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\generate_final_figma_plugin.py"

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

m1 = re.search(r'helperText\(specBox1,.*?\);', text, re.DOTALL)
if m1:
    print("Found specBox1!")
    replacement1 = 'helperText(specBox1, "• Тригер: Натискання на іконку ☰ у шапці Mobile\\\\n• Анімація: Dissolve 250ms (Ease In & Out)\\\\n• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей\\\\n• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map\\\\n• Стан: Активний розділ «Головна сторінка»\\\\n• Zero-booking: Доступ до довідки та тарифів", 13, "Regular", cMuted, 24, 65, 370);'
    text = text[:m1.start()] + replacement1 + text[m1.end():]

m2 = re.search(r'helperText\(specBox2,.*?\);', text, re.DOTALL)
if m2:
    print("Found specBox2!")
    replacement2 = 'helperText(specBox2, "• Тригер: Натискання «Прокласти маршрут» на станції\\\\n• Анімація: Центрований модальний оверлей 250ms\\\\n• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)\\\\n• Дія кнопки: Запуск зовнішнього додатку навігатора\\\\n• Закриття: Клік на кнопку Waze або ✕ закриває оверлей\\\\n• Живий статус: 3 з 4 вільні, генератор активний", 13, "Regular", cMuted, 24, 65, 370);'
    text = text[:m2.start()] + replacement2 + text[m2.end():]

with open(source_path, "w", encoding="utf-8") as f:
    f.write(text)

print("fix_specbox.py completed successfully!")
