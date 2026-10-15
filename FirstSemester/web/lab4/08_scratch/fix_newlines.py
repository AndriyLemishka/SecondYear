# -*- coding: utf-8 -*-
source_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\generate_final_figma_plugin.py"

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix line 817:
old_str_1 = 'helperText(fModalOverlay, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв.\n\nЖодних передоплат чи депозитів — оплата за фактом спожитих кВт·год.", 13, "Regular", cMuted, 30, 115, 480);'
new_str_1 = 'helperText(fModalOverlay, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв.\\\\n\\\\nЖодних передоплат чи депозитів — оплата за фактом спожитих кВт·год.", 13, "Regular", cMuted, 30, 115, 480);'

old_str_2 = 'helperText(specBox1, "• Тригер: Натискання на іконку ☰ у шапці Mobile\n• Анімація: Dissolve 250ms (Ease In & Out)\n• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей\n• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map\n• Стан: Активний розділ «Головна сторінка»\n• Zero-booking: Доступ до довідки та тарифів", 13, "Regular", cMuted, 24, 65, 370);'
new_str_2 = 'helperText(specBox1, "• Тригер: Натискання на іконку ☰ у шапці Mobile\\\\n• Анімація: Dissolve 250ms (Ease In & Out)\\\\n• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей\\\\n• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map\\\\n• Стан: Активний розділ «Головна сторінка»\\\\n• Zero-booking: Доступ до довідки та тарифів", 13, "Regular", cMuted, 24, 65, 370);'

old_str_3 = 'helperText(specBox2, "• Тригер: Натискання «Прокласти маршрут» на станції\n• Анімація: Центрований модальний оверлей 250ms\n• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)\n• Дія кнопки: Запуск зовнішнього додатку навігатора\n• Закриття: Клік на кнопку Waze або ✕ закриває оверлей\n• Живий статус: 3 з 4 вільні, генератор активний", 13, "Regular", cMuted, 24, 65, 370);'
new_str_3 = 'helperText(specBox2, "• Тригер: Натискання «Прокласти маршрут» на станції\\\\n• Анімація: Центрований модальний оверлей 250ms\\\\n• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)\\\\n• Дія кнопки: Запуск зовнішнього додатку навігатора\\\\n• Закриття: Клік на кнопку Waze або ✕ закриває оверлей\\\\n• Живий статус: 3 з 4 вільні, генератор активний", 13, "Regular", cMuted, 24, 65, 370);'

assert old_str_1 in text, "old_str_1 not found"
assert old_str_2 in text, "old_str_2 not found"
assert old_str_3 in text, "old_str_3 not found"

text = text.replace(old_str_1, new_str_1, 1)
text = text.replace(old_str_2, new_str_2, 1)
text = text.replace(old_str_3, new_str_3, 1)

with open(source_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed newlines successfully!")
