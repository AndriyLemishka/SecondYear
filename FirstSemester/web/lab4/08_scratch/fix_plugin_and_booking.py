# -*- coding: utf-8 -*-
import os, sys, re

plugin_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js"

with open(plugin_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix literal newlines in quotes
fixes = [
    ('helperText(dHero, "Швидка та надійна зарядка\nелектромобілів по всій Україні", 42, "Bold", cDark, 60, 85);',
     'helperText(dHero, "Швидка та надійна зарядка\\nелектромобілів по всій Україні", 42, "Bold", cDark, 60, 85);'),
    ('helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 60, 210, 500);',
     'helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 60, 210, 500);'),
    ('helperText(dGenSec, "Заряджайте авто навіть\nпід час повних блекаутів", 32, "Bold", cWhite, 40, 70);',
     'helperText(dGenSec, "Заряджайте авто навіть\\nпід час повних блекаутів", 32, "Bold", cWhite, 40, 70);'),
    ('helperText(dVidSec, "Як зарядитися за 3 кроки:\nвід пошуку до повної батареї", 28, "Bold", cDark, 660, 80);',
     'helperText(dVidSec, "Як зарядитися за 3 кроки:\\nвід пошуку до повної батареї", 28, "Bold", cDark, 660, 80);'),
    ('helperText(tHero, "Швидка та надійна\nзарядка по Україні", 32, "Bold", cDark, 30, 65);',
     'helperText(tHero, "Швидка та надійна\\nзарядка по Україні", 32, "Bold", cDark, 30, 65);'),
    ('helperText(mHero, "Заряджайте авто\nбез стресу", 28, "Bold", cDark, 20, 45);',
     'helperText(mHero, "Заряджайте авто\\nбез стресу", 28, "Bold", cDark, 20, 45);')
]

for old, new in fixes:
    if old in text:
        text = text.replace(old, new)
        print("Fixed newline in string!")
    else:
        print("Pattern not directly matched:", old[:30])

# Fix booking wording
booking_replacements = [
    ('"  Бронювання CCS2"', '"  Маршрут та навігатор"'),
    ('helperText(bookBtn, "Забронювати слот CCS2", 13, "Bold", cWhite, 100, 12);',
     'helperText(bookBtn, "Прокласти маршрут CCS2", 13, "Bold", cWhite, 95, 12);'),
    ('helperText(fOverlays, "Мобільне меню та модальне вікно підтвердження бронювання", 15, "Regular", cMuted, 60, 80);',
     'helperText(fOverlays, "Мобільне меню та модальне вікно асистента навігації ChargeUA", 15, "Regular", cMuted, 60, 80);'),
    ('helperText(mSuccessPill, "• Бронювання підтверджено", 11, "Bold", cSuccess, 10, 6);',
     'helperText(mSuccessPill, "• Маршрут передано у навігатор", 11, "Bold", cSuccess, 10, 6);'),
    ('helperText(modalBox, "Дякуємо! Слот CCS2 заброньовано", 22, "Bold", cDark, 30, 75);',
     'helperText(modalBox, "Помічник ChargeUA: Станцію обрано!", 20, "Bold", cDark, 30, 75);'),
    ('helperText(modalBox, "Вам надіслано SMS із кодом доступу до станції «Київ-Поділ». Час резерву: 20 хвилин. Станція автоматично утримує чергу для вас.", 14, "Regular", cMuted, 30, 115, 460);',
     'helperText(modalBox, "Станцію «Київ-Поділ» (120 кВт CCS2) додано до вашої поїздки. Помічник автоматично відстежує зайнятість портів та роботу генератора в дорозі.", 14, "Regular", cMuted, 30, 115, 460);'),
    ('helperText(modalBtn, "Зрозуміло, відкрити маршрут", 14, "Bold", cWhite, 110, 14);',
     'helperText(modalBtn, "Відкрити Waze / Google Maps", 14, "Bold", cWhite, 100, 14);'),
    ('helperText(sBtn, "Забронювати конектор", 13, "Bold", cWhite, 110, 11);',
     'helperText(sBtn, "Прокласти маршрут", 13, "Bold", cWhite, 120, 11);'),
    ('helperText(mSb, "Забронювати CCS2", 12, "Bold", cWhite, 95, 12);',
     'helperText(mSb, "Прокласти маршрут", 12, "Bold", cWhite, 95, 12);'),
    ('helperText(detBookBtn, "Забронювати слот на 20 хв", 16, "Bold", cWhite, 100, 17);',
     'helperText(detBookBtn, "Прокласти маршрут у навігаторі", 16, "Bold", cWhite, 75, 17);')
]

for old, new in booking_replacements:
    if old in text:
        text = text.replace(old, new)
        print("Replaced booking term!")
    else:
        print("Booking pattern not matched:", old[:30])

# Also check any remaining 'бронюв'
pattern = re.compile(r'бронюв\w*', re.IGNORECASE)
found = pattern.findall(text)
print("Remaining mentions of бронюв:", set(found))

with open(plugin_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated figma_builder_plugin.js successfully.")
