# -*- coding: utf-8 -*-
import os, sys, re, subprocess

v2_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\build_all_figures_v2.py"

with open(v2_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace booking terms in build_all_figures_v2.py
replacements = [
    ('<div class="step">Бронювання на 20 хв</div><div class="arrow">→</div>',
     '<div class="step">Вибір вільного порту</div><div class="arrow">→</div>'),
    ('<div class="item">Бронювання конектора CCS2</div>',
     '<div class="item">Маршрут у Waze / Maps</div>'),
    ('<button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Забронювати порт CCS2</button>',
     '<button style="width:100%; height:38px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-weight:700; font-size:12px;">Прокласти маршрут CCS2</button>'),
    ('«Для комерційного флоту функція бронювання слотів — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.»',
     '«Для комерційного флоту зручний моніторинг вільних станцій та генераторів — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.»'),
    ('<button style="width:100%; height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:10px; font-weight:700;">Забронювати CCS2</button>',
     '<button style="width:100%; height:32px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:10px; font-weight:700;">Прокласти маршрут</button>'),
    ('<button style="width:100%; height:40px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px; margin-bottom:8px;">Забронювати порт CCS2 на 20 хв</button>',
     '<button style="width:100%; height:40px; background:#005EC9; color:#FFF; border:none; border-radius:8px; font-weight:700; font-size:12.5px; margin-bottom:8px;">Прокласти маршрут у навігаторі</button>'),
    ('<button style="width:100%; height:34px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Забронювати CCS2</button>',
     '<button style="width:100%; height:34px; background:#005EC9; color:#FFF; border:none; border-radius:6px; font-size:11px; font-weight:700;">Прокласти маршрут</button>'),
    ('● Бронювання підтверджено',
     '● Маршрут побудовано'),
    ('Дякуємо! Слот CCS2 заброньовано',
     'Помічник ChargeUA: Станцію обрано!'),
    ('Вам надіслано SMS із кодом доступу до станції «Київ-Поділ». Час резерву: <strong>20 хвилин</strong>.',
     'Хаб «Київ-Поділ» (120 кВт CCS2) додано до маршруту. Додаток автоматично моніторить статус портів та світла.'),
    ('Зрозуміло, відкрити маршрут',
     'Відкрити Waze / Google Maps'),
    ('<div>Booking Slot Modal</div>',
     '<div>Waze / Maps Navigation</div>'),
    ('<div class="wire-block">Booking Form Modal</div>',
     '<div class="wire-block">Waze / Maps Route Modal</div>')
]

for old, new in replacements:
    if old in code:
        code = code.replace(old, new)
        print("Replaced in figures:", old[:35], "->", new[:35])
    else:
        print("Figures pattern not matched:", old[:35])

with open(v2_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_all_figures_v2.py!")
