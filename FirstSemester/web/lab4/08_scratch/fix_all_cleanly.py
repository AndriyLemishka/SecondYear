# -*- coding: utf-8 -*-
import re

source_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\generate_final_figma_plugin.py"

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace modal body text
m_modal = re.search(r'helperText\(fModalOverlay,\s*"Маршрут до швидкісного хабу.*?\);', text, re.DOTALL)
if m_modal:
    rep_modal = 'helperText(fModalOverlay, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв. Жодних передоплат чи депозитів — оплата за фактом спожитих кВт·год.", 13, "Regular", cMuted, 30, 115, 480);'
    text = text[:m_modal.start()] + rep_modal + text[m_modal.end():]
    print("Fixed modal body text!")

# 2. Replace specBox1
m_sb1 = re.search(r'helperText\(specBox1,\s*"• Тригер:.*?\);', text, re.DOTALL)
if m_sb1:
    rep_sb1 = """const specLines1 = [
    "• Тригер: Натискання на іконку ☰ у шапці Mobile",
    "• Анімація: Dissolve 250ms (Ease In & Out)",
    "• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей",
    "• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map",
    "• Стан: Активний розділ «Головна сторінка»",
    "• Zero-booking: Доступ до довідки та тарифів"
  ];
  specLines1.forEach((ln, lIdx) => {{
    helperText(specBox1, ln, 13, "Regular", cMuted, 24, 65 + lIdx * 25, 370);
  }});"""
    text = text[:m_sb1.start()] + rep_sb1 + text[m_sb1.end():]
    print("Fixed specBox1!")

# 3. Replace specBox2
m_sb2 = re.search(r'helperText\(specBox2,\s*"• Тригер:.*?\);', text, re.DOTALL)
if m_sb2:
    rep_sb2 = """const specLines2 = [
    "• Тригер: Натискання «Прокласти маршрут» на станції",
    "• Анімація: Центрований модальний оверлей 250ms",
    "• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)",
    "• Дія кнопки: Запуск зовнішнього додатку навігатора",
    "• Закриття: Клік на кнопку Waze або ✕ закриває оверлей",
    "• Живий статус: 3 з 4 вільні, генератор активний"
  ];
  specLines2.forEach((ln, lIdx) => {{
    helperText(specBox2, ln, 13, "Regular", cMuted, 24, 65 + lIdx * 25, 370);
  }});"""
    text = text[:m_sb2.start()] + rep_sb2 + text[m_sb2.end():]
    print("Fixed specBox2!")

with open(source_path, "w", encoding="utf-8") as f:
    f.write(text)

print("All replacements done!")
