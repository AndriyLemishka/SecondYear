# -*- coding: utf-8 -*-
"""
Update generate_final_figma_plugin.py to include:
1. Centered Hero Video (from video_content.mp4 / video_frame_30.jpg)
2. Interactive Calculator with SLIDER (повзунок) with handle knob, progress fill, and tooltip badge
3. Live Map with Charging Hub Pins across Ukraine
4. Mobile layout matching user reference photo media_1791486163413_08bf9f1b.png pixel-for-pixel
"""

import os, re

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
GEN_SCRIPT = os.path.join(BASE_DIR, "08_scratch", "generate_final_figma_plugin.py")

with open(GEN_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update b64_video to use video_frame_30.jpg instead of fig5_video.png
code = code.replace(
    'b64_video = get_b64_jpeg("fig5_video.png", 400, 200, 75)',
    'b64_video = get_b64_jpeg("video_frame_30.jpg", 640, 360, 80)'
)

# New Desktop, Tablet, Mobile definitions
new_desktop_tablet_mobile = """  // FRAME 05: FULL DESKTOP (1440 × 4150)
  const fDesktop = figma.createFrame();
  fDesktop.name = "05_Desktop";
  fDesktop.resize(1440, 4150);
  fDesktop.x = 0; fDesktop.y = 2300;
  fDesktop.fills = [{ type: "SOLID", color: cWhite }];

  // Top Bar
  const dTop = figma.createFrame();
  dTop.resize(1440, 40);
  dTop.fills = [{ type: "SOLID", color: cDark }];
  fDesktop.appendChild(dTop);
  helperText(dTop, "● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі", 12, "Medium", cWhite, 60, 12);
  helperText(dTop, "Гаряча лінія 24/7: 0 800 300 400 | UA", 12, "Medium", cWhite, 1150, 12);

  // Header
  const dHead = figma.createFrame();
  dHead.resize(1440, 76);
  dHead.y = 40;
  dHead.fills = [{ type: "SOLID", color: cWhite }];
  dHead.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dHead);
  addSvgNode(dHead, "logo", 60, 20, 36, 36);
  helperText(dHead, "ChargeUA", 22, "Bold", cPrimary, 105, 24);
  helperText(dHead, "Головна        Калькулятор        Карта станцій        Тарифи        Для бізнесу", 14, "Semi Bold", cDark, 420, 28);
  const dHeadCta = figma.createFrame();
  dHeadCta.resize(160, 42);
  dHeadCta.x = 1220; dHeadCta.y = 17;
  dHeadCta.cornerRadius = 8;
  dHeadCta.fills = [{ type: "SOLID", color: cPrimary }];
  dHead.appendChild(dHeadCta);
  helperText(dHeadCta, "Знайти зарядку", 13, "Bold", cWhite, 26, 12);

  // Hero Section - CENTERED WITH VIDEO PLAYER
  const dHero = figma.createFrame();
  dHero.resize(1440, 890);
  dHero.y = 116;
  dHero.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }];
  fDesktop.appendChild(dHero);

  helperText(dHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ", 11, "Bold", cPrimary, 550, 35);
  helperText(dHero, "Швидка та надійна зарядка\\nелектромобілів по всій Україні", 42, "Bold", cDark, 320, 65, 800);
  helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 360, 185, 720);

  const dHeroBtn1 = figma.createFrame();
  dHeroBtn1.resize(230, 48);
  dHeroBtn1.x = 470; dHeroBtn1.y = 255;
  dHeroBtn1.cornerRadius = 8;
  dHeroBtn1.fills = [{ type: "SOLID", color: cPrimary }];
  dHero.appendChild(dHeroBtn1);
  helperText(dHeroBtn1, "Розрахувати зарядку →", 14, "Bold", cWhite, 32, 15);

  const dHeroBtn2 = figma.createFrame();
  dHeroBtn2.resize(180, 48);
  dHeroBtn2.x = 720; dHeroBtn2.y = 255;
  dHeroBtn2.cornerRadius = 8;
  dHeroBtn2.fills = [{ type: "SOLID", color: cWhite }];
  dHeroBtn2.strokes = [{ type: "SOLID", color: cBorder }];
  dHero.appendChild(dHeroBtn2);
  helperText(dHeroBtn2, "Знайти на карті", 14, "Semi Bold", cDark, 30, 15);

  const heroChips = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 З генератором"];
  heroChips.forEach((ch, idx) => {
    const chBox = figma.createFrame();
    chBox.resize(130, 32);
    chBox.x = 440 + idx * 145; chBox.y = 325;
    chBox.cornerRadius = 16;
    chBox.fills = [{ type: "SOLID", color: idx === 3 ? cSuccessBg : cWhite }];
    chBox.strokes = [{ type: "SOLID", color: idx === 3 ? cSuccess : cBorder }];
    dHero.appendChild(chBox);
    helperText(chBox, ch, 11, "Bold", idx === 3 ? cSuccess : cDark, 12, 8);
  });

  // Centered Video Showcase Container (LR3 video_content.mp4)
  const dHeroVideo = figma.createFrame();
  dHeroVideo.resize(1100, 460);
  dHeroVideo.x = 170; dHeroVideo.y = 380;
  dHeroVideo.cornerRadius = 18;
  dHeroVideo.fills = [{ type: "SOLID", color: cDark }];
  dHeroVideo.strokes = [{ type: "SOLID", color: cBorder }];
  dHero.appendChild(dHeroVideo);

  addImageRect(dHeroVideo, "video", 0, 0, 1100, 460, 18);

  // Play Button Overlay
  const dPlayBtn = figma.createFrame();
  dPlayBtn.resize(68, 68);
  dPlayBtn.x = 516; dPlayBtn.y = 196;
  dPlayBtn.cornerRadius = 34;
  dPlayBtn.fills = [{ type: "SOLID", color: cPrimary }];
  dHeroVideo.appendChild(dPlayBtn);
  helperText(dPlayBtn, "▶", 24, "Bold", cWhite, 25, 20);

  // Video Tag & Bottom Player Bar
  const dVTag = figma.createFrame();
  dVTag.resize(460, 32);
  dVTag.x = 20; dVTag.y = 20;
  dVTag.cornerRadius = 6;
  dVTag.fills = [{ type: "SOLID", color: cDark, opacity: 0.85 }];
  dHeroVideo.appendChild(dVTag);
  helperText(dVTag, "⚡ Відеопрезентація ChargeUA 4K · 100% автономність (video_content.mp4)", 11, "Bold", cWhite, 14, 8);

  const dVBar = figma.createFrame();
  dVBar.resize(1100, 44);
  dVBar.x = 0; dVBar.y = 416;
  dVBar.fills = [{ type: "SOLID", color: cDark, opacity: 0.85 }];
  dHeroVideo.appendChild(dVBar);
  helperText(dVBar, "▶ 0:45 / 1:30 · Презентація швидкої зарядної станції 160 кВт | 1080p 60fps", 12, "Medium", cWhite, 20, 13);
  helperText(dVBar, "480+ станцій онлайн", 12, "Bold", { r: 0, g: 229/255, b: 255/255 }, 950, 13);

  // Benefits Strip
  const dStrip = figma.createFrame();
  dStrip.resize(1440, 140);
  dStrip.y = 1006;
  dStrip.fills = [{ type: "SOLID", color: cBgSurface }];
  dStrip.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dStrip);

  const stripItems = [
    { svg: "calc", title: "Точний калькулятор витрат", desc: "Автоматичний підбір моделі авто та тарифу" },
    { svg: "loc", title: "Live-карта 480+ станцій", desc: "Актуальний статус зайнятості та світла" },
    { svg: "info", title: "100% Енергонезалежність", desc: "Робота від генераторів у блекаути" }
  ];
  stripItems.forEach((st, idx) => {
    const card = figma.createFrame();
    card.resize(400, 90);
    card.x = 60 + idx * 450; card.y = 25;
    card.cornerRadius = 12;
    card.fills = [{ type: "SOLID", color: cWhite }];
    card.strokes = [{ type: "SOLID", color: cBorder }];
    dStrip.appendChild(card);
    addSvgNode(card, st.svg, 20, 20, 48, 48);
    helperText(card, st.title, 15, "Bold", cDark, 80, 22);
    helperText(card, st.desc, 12, "Regular", cMuted, 80, 48);
  });

  // Interactive Calculator with SLIDER (повзунок)
  const dCalcSec = figma.createFrame();
  dCalcSec.resize(1320, 360);
  dCalcSec.x = 60; dCalcSec.y = 1170;
  dCalcSec.cornerRadius = 16;
  dCalcSec.fills = [{ type: "SOLID", color: cWhite }];
  dCalcSec.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dCalcSec);

  helperText(dCalcSec, "Розрахуйте точну вартість та час зарядки ChargeUA", 24, "Bold", cDark, 40, 30);
  helperText(dCalcSec, "Оберіть марку електромобіля та налаштуйте бажаний рівень батареї за допомогою повзунка:", 14, "Regular", cMuted, 40, 65);

  const carPills = ["Volkswagen ID.4 (77 кВт·год)", "Tesla Model 3 (60 кВт·год)", "Nissan Leaf (40 кВт·год)", "Hyundai Ioniq 5 (72 кВт·год)"];
  carPills.forEach((cp, idx) => {
    const cPill = figma.createFrame();
    cPill.resize(250, 38);
    cPill.x = 40 + idx * 265; cPill.y = 105;
    cPill.cornerRadius = 8;
    cPill.fills = [{ type: "SOLID", color: idx === 0 ? cPrimary : cBgSurface }];
    if (idx !== 0) cPill.strokes = [{ type: "SOLID", color: cBorder }];
    dCalcSec.appendChild(cPill);
    helperText(cPill, cp, 12, "Semi Bold", idx === 0 ? cWhite : cDark, 12, 10);
  });

  // Calculator SLIDER Box (Повзунок)
  const dSliderBox = figma.createFrame();
  dSliderBox.resize(760, 160);
  dSliderBox.x = 40; dSliderBox.y = 165;
  dSliderBox.cornerRadius = 12;
  dSliderBox.fills = [{ type: "SOLID", color: cBgSurface }];
  dSliderBox.strokes = [{ type: "SOLID", color: cBorder }];
  dCalcSec.appendChild(dSliderBox);

  helperText(dSliderBox, "Регулювання рівня заряду (Повзунок %):", 13, "Bold", cDark, 20, 18);
  helperText(dSliderBox, "20% → 80% (Додано +46.2 кВт·год)", 13, "Bold", cPrimary, 490, 18);

  // Slider Track & Fill
  const dSliderTrack = figma.createFrame();
  dSliderTrack.resize(720, 10);
  dSliderTrack.x = 20; dSliderTrack.y = 65;
  dSliderTrack.cornerRadius = 5;
  dSliderTrack.fills = [{ type: "SOLID", color: cBorder }];
  dSliderBox.appendChild(dSliderTrack);

  const dSliderFill = figma.createFrame();
  dSliderFill.resize(432, 10);
  dSliderFill.x = 144; dSliderFill.y = 65;
  dSliderFill.cornerRadius = 5;
  dSliderFill.fills = [{ type: "SOLID", color: cPrimary }];
  dSliderBox.appendChild(dSliderFill);

  // Slider Knob at 80% (576px mark)
  const dSliderKnob = figma.createFrame();
  dSliderKnob.resize(26, 26);
  dSliderKnob.x = 563; dSliderKnob.y = 57;
  dSliderKnob.cornerRadius = 13;
  dSliderKnob.fills = [{ type: "SOLID", color: cWhite }];
  dSliderKnob.strokes = [{ type: "SOLID", color: cPrimary }];
  dSliderBox.appendChild(dSliderKnob);

  // Tooltip Badge
  const dSliderTip = figma.createFrame();
  dSliderTip.resize(80, 24);
  dSliderTip.x = 536; dSliderTip.y = 26;
  dSliderTip.cornerRadius = 4;
  dSliderTip.fills = [{ type: "SOLID", color: cPrimary }];
  dSliderBox.appendChild(dSliderTip);
  helperText(dSliderTip, "80% (Ціль)", 10, "Bold", cWhite, 10, 5);

  helperText(dSliderBox, "0% (Розряджена)       20% (Старт)               50%                 80% (Рекомендовано DC)      100%", 11, "Medium", cMuted, 20, 95);

  // Result Card on Right
  const calcRes = figma.createFrame();
  calcRes.resize(440, 160);
  calcRes.x = 840; calcRes.y = 165;
  calcRes.cornerRadius = 12;
  calcRes.fills = [{ type: "SOLID", color: { r: 240/255, g: 247/255, b: 255/255 } }];
  calcRes.strokes = [{ type: "SOLID", color: { r: 191/255, g: 219/255, b: 254/255 } }];
  dCalcSec.appendChild(calcRes);

  helperText(calcRes, "ОРІЄНТОВНА ВАРТІСТЬ СЕСІЇ:", 11, "Bold", cMuted, 24, 20);
  helperText(calcRes, "652.50 ₴", 32, "Bold", cPrimary, 24, 45);
  helperText(calcRes, "Тариф: 14.12 ₴ / кВт·год · 46.2 кВт·год", 12, "Regular", cDark, 24, 88);
  helperText(calcRes, "● Час на DC 120 кВт: ~28 хв", 12, "Bold", cDark, 24, 115);

  // LIVE MAP SECTION (Карта з зарядками)
  const dMapSec = figma.createFrame();
  dMapSec.resize(1320, 420);
  dMapSec.x = 60; dMapSec.y = 1560;
  dMapSec.cornerRadius = 16;
  dMapSec.fills = [{ type: "SOLID", color: cWhite }];
  dMapSec.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dMapSec);

  helperText(dMapSec, "Live-карта зарядної мережі України", 22, "Bold", cDark, 30, 24);
  helperText(dMapSec, "Актуальний статус зайнятості та наявність резервного живлення в реальному часі", 13, "Regular", cMuted, 30, 56);

  // Filter Chips on Map
  const mapChips = ["Всі хаби (480+)", "⚡ Ultra-Fast (>100 кВт)", "🔋 Працює від генератора"];
  mapChips.forEach((mc, idx) => {
    const mcBox = figma.createFrame();
    mcBox.resize(170, 32);
    mcBox.x = 760 + idx * 180; mcBox.y = 28;
    mcBox.cornerRadius = 6;
    mcBox.fills = [{ type: "SOLID", color: idx === 0 ? cPrimary : cBgSurface }];
    dMapSec.appendChild(mcBox);
    helperText(mcBox, mc, 11, "Bold", idx === 0 ? cWhite : cDark, 12, 8);
  });

  // Map Canvas Box
  const dMapCanvas = figma.createFrame();
  dMapCanvas.resize(1260, 310);
  dMapCanvas.x = 30; dMapCanvas.y = 85;
  dMapCanvas.cornerRadius = 12;
  dMapCanvas.fills = [{ type: "SOLID", color: cBgSurface }];
  dMapCanvas.strokes = [{ type: "SOLID", color: cBorder }];
  dMapSec.appendChild(dMapCanvas);

  // Pins on Map Canvas
  const mapPinsData = [
    { name: "Хаб «Київ-Поділ» · 120 кВт (3/4 вільно) 🔋", x: 620, y: 70, color: cPrimary },
    { name: "Хаб «Львів-Арена» · 160 кВт (5/6 вільно) 🔋", x: 180, y: 110, color: cSuccess },
    { name: "Хаб «Одеса-Порт» · 100 кВт (1/2 вільно) 🔋", x: 680, y: 220, color: cWarning },
    { name: "Хаб «Дніпро-Сіті» · 120 кВт (2/2 вільно) 🔋", x: 960, y: 160, color: cPrimary }
  ];
  mapPinsData.forEach(pin => {
    const pDot = figma.createFrame();
    pDot.resize(14, 14);
    pDot.x = pin.x; pDot.y = pin.y;
    pDot.cornerRadius = 7;
    pDot.fills = [{ type: "SOLID", color: pin.color }];
    pDot.strokes = [{ type: "SOLID", color: cWhite }];
    dMapCanvas.appendChild(pDot);

    const pTag = figma.createFrame();
    pTag.resize(250, 26);
    pTag.x = pin.x - 110; pTag.y = pin.y + 18;
    pTag.cornerRadius = 5;
    pTag.fills = [{ type: "SOLID", color: cDark }];
    dMapCanvas.appendChild(pTag);
    helperText(pTag, pin.name, 10, "Bold", cWhite, 8, 6);
  });

  // Popular Charging Hubs (3 Cards)
  helperText(fDesktop, "Популярні зарядні хаби по Україні", 28, "Bold", cDark, 60, 2010);
  helperText(fDesktop, "Перевірені локації з високою потужністю та гарантованим резервним живленням", 15, "Regular", cMuted, 60, 2050);

  stationsData.slice(0, 3).forEach((st, idx) => {
    const sCard = figma.createFrame();
    sCard.resize(420, 380);
    sCard.x = 60 + idx * 450; sCard.y = 2090;
    sCard.cornerRadius = 16;
    sCard.fills = [{ type: "SOLID", color: cWhite }];
    sCard.strokes = [{ type: "SOLID", color: cBorder }];
    fDesktop.appendChild(sCard);

    addImageRect(sCard, st.img, 0, 0, 420, 190, 0);
    helperText(sCard, st.title, 16, "Bold", cDark, 20, 205);
    helperText(sCard, st.addr, 13, "Regular", cMuted, 20, 232);

    const sPill = figma.createFrame();
    sPill.resize(170, 26);
    sPill.x = 20; sPill.y = 265;
    sPill.cornerRadius = 6;
    sPill.fills = [{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }];
    sCard.appendChild(sPill);
    helperText(sPill, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 6);

    const sBtn = figma.createFrame();
    sBtn.resize(380, 44);
    sBtn.x = 20; sBtn.y = 315;
    sBtn.cornerRadius = 8;
    sBtn.fills = [{ type: "SOLID", color: cPrimary }];
    sCard.appendChild(sBtn);
    helperText(sBtn, "Прокласти маршрут", 13, "Bold", cWhite, 120, 13);
  });

  // Generator Blackout Section
  const dGenSec = figma.createFrame();
  dGenSec.resize(1320, 320);
  dGenSec.x = 60; dGenSec.y = 2500;
  dGenSec.cornerRadius = 16;
  dGenSec.fills = [{ type: "SOLID", color: cDark }];
  fDesktop.appendChild(dGenSec);

  addImageRect(dGenSec, "generator", 760, 20, 540, 280, 12);

  const genBadge = figma.createFrame();
  genBadge.resize(230, 28);
  genBadge.x = 40; genBadge.y = 35;
  genBadge.cornerRadius = 6;
  genBadge.fills = [{ type: "SOLID", color: { r: 34/255, g: 197/255, b: 94/255 }, opacity: 0.2 }];
  dGenSec.appendChild(genBadge);
  helperText(genBadge, "⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%", 11, "Bold", { r: 74/255, g: 222/255, b: 128/255 }, 12, 6);

  helperText(dGenSec, "Заряджайте авто навіть\\nпід час повних блекаутів", 32, "Bold", cWhite, 40, 75);
  helperText(dGenSec, "Понад 180 станцій мережі ChargeUA обладнані промисловими дизель-генераторами потужністю від 160 кВт. Автоматичний запуск за 15 секунд після знеструмлення мережі гарантує стабільний струм та безперебійне живлення.", 14, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 40, 160, 680);

  // How it works / Steps (CLEAN: NO video box! Text & 3 Step Cards)
  const dStepsSec = figma.createFrame();
  dStepsSec.resize(1320, 350);
  dStepsSec.x = 60; dStepsSec.y = 2850;
  dStepsSec.cornerRadius = 16;
  dStepsSec.fills = [{ type: "SOLID", color: cWhite }];
  dStepsSec.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dStepsSec);

  helperText(dStepsSec, "⚡ ПРОСТИЙ ТА ПРОЗОРИЙ ПРОЦЕС", 11, "Bold", cPrimary, 40, 30);
  helperText(dStepsSec, "Як зарядитися за 3 кроки: від пошуку до повної батареї", 26, "Bold", cDark, 40, 55);
  helperText(dStepsSec, "Швидкий алгоритм підключення без заплутаних депозитів, тривалих реєстрацій чи черг на локації.", 14, "Regular", cMuted, 40, 95);

  const stepsList = [
    { num: "1", title: "Знайдіть вільну станцію", desc: "Фільтруйте за потужністю, конектором або наявністю генератора на онлайн-карті ChargeUA." },
    { num: "2", title: "Підключіть конектор CCS2", desc: "Вставте кабель у роз'єм електромобіля — розумний індикатор спалахне зеленим кольором." },
    { num: "3", title: "Оплатіть у 1 клік", desc: "Apple Pay, Google Pay або картка без жодних передплат — списується лише фактично спожита енергія." }
  ];

  stepsList.forEach((sp, idx) => {
    const sCol = figma.createFrame();
    sCol.resize(390, 180);
    sCol.x = 40 + idx * 420; sCol.y = 140;
    sCol.cornerRadius = 12;
    sCol.fills = [{ type: "SOLID", color: cBgSurface }];
    sCol.strokes = [{ type: "SOLID", color: cBorder }];
    dStepsSec.appendChild(sCol);

    const sCircle = figma.createFrame();
    sCircle.resize(44, 44);
    sCircle.x = 24; sCircle.y = 24;
    sCircle.cornerRadius = 22;
    sCircle.fills = [{ type: "SOLID", color: cPrimary }];
    sCol.appendChild(sCircle);
    helperText(sCircle, sp.num, 18, "Bold", cWhite, 16, 10);

    helperText(sCol, sp.title, 16, "Bold", cDark, 24, 85);
    helperText(sCol, sp.desc, 13, "Regular", cMuted, 24, 115, 340);
  });

  // Reviews Section
  helperText(fDesktop, "Відгуки реальних водіїв", 28, "Bold", cDark, 60, 3230);
  helperText(fDesktop, "Що кажуть власники електромобілів про сервіс швидкої зарядки ChargeUA", 15, "Regular", cMuted, 60, 3270);

  const reviewsList = [
    { name: "Олексій Коваленко", car: "Tesla Model Y", text: "Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, станція стабільна, кава поруч. Найкращий сервіс!", av: "av1" },
    { name: "Олена Мельник", car: "Nissan Leaf", text: "Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів.", av: "av2" },
    { name: "Сергій Васильчук", car: "Керівник автопарку", text: "Для комерційного автопарку зручний моніторинг вільних станцій — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.", av: "av3" }
  ];

  reviewsList.forEach((rv, idx) => {
    const rCard = figma.createFrame();
    rCard.resize(420, 200);
    rCard.x = 60 + idx * 450; rCard.y = 3310;
    rCard.cornerRadius = 16;
    rCard.fills = [{ type: "SOLID", color: cWhite }];
    rCard.strokes = [{ type: "SOLID", color: cBorder }];
    fDesktop.appendChild(rCard);

    helperText(rCard, "★★★★★", 14, "Bold", { r: 245/255, g: 158/255, b: 11/255 }, 24, 20);
    helperText(rCard, `«${rv.text}»`, 13, "Medium", cDark, 24, 48, 370);
    addImageRect(rCard, rv.av, 24, 130, 44, 44, 22);
    helperText(rCard, rv.name, 14, "Bold", cDark, 80, 132);
    helperText(rCard, rv.car, 12, "Regular", cMuted, 80, 152);
  });

  // B2B Lead Form
  const dFormSec = figma.createFrame();
  dFormSec.resize(1320, 220);
  dFormSec.x = 60; dFormSec.y = 3540;
  dFormSec.cornerRadius = 16;
  dFormSec.fills = [{ type: "SOLID", color: cBgSurface }];
  dFormSec.strokes = [{ type: "SOLID", color: cBorder }];
  fDesktop.appendChild(dFormSec);

  helperText(dFormSec, "Маєте локацію? Встановіть станцію ChargeUA", 24, "Bold", cDark, 40, 30);
  helperText(dFormSec, "Отримуйте стабільний пасивний дохід від зарядки авто ваших клієнтів", 14, "Regular", cMuted, 40, 65);

  const inp1 = figma.createFrame(); inp1.resize(360, 46); inp1.x = 40; inp1.y = 110; inp1.cornerRadius = 8; inp1.fills = [{ type: "SOLID", color: cWhite }]; inp1.strokes = [{ type: "SOLID", color: cBorder }]; dFormSec.appendChild(inp1);
  helperText(inp1, "Ваше ім'я", 13, "Regular", cMuted, 16, 14);
  const inp2 = figma.createFrame(); inp2.resize(360, 46); inp2.x = 430; inp2.y = 110; inp2.cornerRadius = 8; inp2.fills = [{ type: "SOLID", color: cWhite }]; inp2.strokes = [{ type: "SOLID", color: cBorder }]; dFormSec.appendChild(inp2);
  helperText(inp2, "Номер телефону (+380...)", 13, "Regular", cMuted, 16, 14);
  const dFormBtn = figma.createFrame(); dFormBtn.resize(260, 46); dFormBtn.x = 820; dFormBtn.y = 110; dFormBtn.cornerRadius = 8; dFormBtn.fills = [{ type: "SOLID", color: cPrimary }]; dFormSec.appendChild(dFormBtn);
  helperText(dFormBtn, "Подати заявку на монтаж", 14, "Bold", cWhite, 35, 14);

  // Desktop Footer
  const dFooter = figma.createFrame();
  dFooter.resize(1440, 350);
  dFooter.y = 3800;
  dFooter.fills = [{ type: "SOLID", color: cDark }];
  fDesktop.appendChild(dFooter);

  addSvgNode(dFooter, "logo", 60, 45, 38, 38);
  helperText(dFooter, "ChargeUA", 24, "Bold", cWhite, 110, 50);
  helperText(dFooter, "Національний агрегатор та веб-помічник зарядної інфраструктури України.\\nШвидкий пошук та моніторинг станцій у блекаути.", 13, "Regular", { r: 148/255, g: 163/255, b: 184/255 }, 60, 100, 380);

  helperText(dFooter, "Навігація\\n\\nГоловна\\nКалькулятор\\nКарта станцій\\nТарифи", 13, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 560, 50);
  helperText(dFooter, "Для бізнесу\\n\\nВстановити хаб\\nB2B-калькулятор\\nПартнерство\\nРезервне живлення", 13, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 780, 50);
  helperText(dFooter, "Контакти\\n\\n0 800 300 400\\nsupport@charge.ua\\nм. Київ, вул. Подолу, 12\\nTelegram Бот", 13, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 1020, 50);

  const dFootLine = figma.createFrame(); dFootLine.resize(1320, 1); dFootLine.x = 60; dFootLine.y = 260; dFootLine.fills = [{ type: "SOLID", color: { r: 30/255, g: 41/255, b: 59/255 } }]; dFooter.appendChild(dFootLine);
  helperText(dFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", { r: 100/255, g: 116/255, b: 139/255 }, 60, 290);
  helperText(dFooter, "Політика приватності · Умови використання", 12, "Regular", { r: 100/255, g: 116/255, b: 139/255 }, 1120, 290);

  // FRAME 06: FULL TABLET (768 × 3650)
  const fTablet = figma.createFrame();
  fTablet.name = "06_Tablet";
  fTablet.resize(768, 3650);
  fTablet.x = 1600; fTablet.y = 2300;
  fTablet.fills = [{ type: "SOLID", color: cWhite }];

  // Tablet Header
  const tHead = figma.createFrame(); tHead.resize(768, 70); tHead.fills = [{ type: "SOLID", color: cWhite }]; tHead.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tHead);
  addSvgNode(tHead, "logo", 30, 18, 32, 32);
  helperText(tHead, "ChargeUA", 20, "Bold", cPrimary, 70, 22);
  helperText(tHead, "Головна     Калькулятор     Карта     Тарифи", 13, "Semi Bold", cDark, 260, 26);
  const tHeadCta = figma.createFrame(); tHeadCta.resize(120, 36); tHeadCta.x = 618; tHeadCta.y = 17; tHeadCta.cornerRadius = 6; tHeadCta.fills = [{ type: "SOLID", color: cPrimary }]; tHead.appendChild(tHeadCta);
  helperText(tHeadCta, "Знайти", 12, "Bold", cWhite, 36, 10);

  // Tablet Hero - CENTERED WITH VIDEO
  const tHero = figma.createFrame(); tHero.resize(768, 560); tHero.y = 70; tHero.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; fTablet.appendChild(tHero);
  helperText(tHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР", 10, "Bold", cPrimary, 290, 25);
  helperText(tHero, "Швидка та надійна зарядка\\nпо всій Україні", 30, "Bold", cDark, 180, 50, 450);
  helperText(tHero, "Знаходьте найближчі станції та подорожуйте без стресу у блекаути.", 13, "Regular", cMuted, 160, 125, 450);

  const tBtn1 = figma.createFrame(); tBtn1.resize(220, 42); tBtn1.x = 274; tBtn1.y = 175; tBtn1.cornerRadius = 8; tBtn1.fills = [{ type: "SOLID", color: cPrimary }]; tHero.appendChild(tBtn1);
  helperText(tBtn1, "Розрахувати зарядку →", 12, "Bold", cWhite, 36, 13);

  // Centered Video Box on Tablet
  const tVidBox = figma.createFrame(); tVidBox.resize(708, 300); tVidBox.x = 30; tVidBox.y = 235; tVidBox.cornerRadius = 14; tVidBox.fills = [{ type: "SOLID", color: cDark }]; tHero.appendChild(tVidBox);
  addImageRect(tVidBox, "video", 0, 0, 708, 300, 14);
  const tPlay = figma.createFrame(); tPlay.resize(56, 56); tPlay.x = 326; tPlay.y = 122; tPlay.cornerRadius = 28; tPlay.fills = [{ type: "SOLID", color: cPrimary }]; tVidBox.appendChild(tPlay);
  helperText(tPlay, "▶", 20, "Bold", cWhite, 21, 16);

  // Tablet Benefits Strip
  const tStrip = figma.createFrame(); tStrip.resize(708, 80); tStrip.x = 30; tStrip.y = 650; tStrip.cornerRadius = 12; tStrip.fills = [{ type: "SOLID", color: cBgSurface }]; tStrip.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tStrip);
  helperText(tStrip, "⚡ 480+ станцій онлайн", 13, "Bold", cDark, 25, 30);
  helperText(tStrip, "🔋 100% робота в блекаути", 13, "Bold", cSuccess, 260, 30);
  helperText(tStrip, "⏱ Розрахунок за 3 секунди", 13, "Bold", cPrimary, 510, 30);

  // Tablet Calculator with SLIDER
  const tCalc = figma.createFrame(); tCalc.resize(708, 300); tCalc.x = 30; tCalc.y = 750; tCalc.cornerRadius = 14; tCalc.fills = [{ type: "SOLID", color: cWhite }]; tCalc.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tCalc);
  helperText(tCalc, "Калькулятор вартості зарядки", 18, "Bold", cDark, 24, 20);
  helperText(tCalc, "Volkswagen ID.4 (77 кВт·год) · 20% → 80%", 13, "Medium", cPrimary, 24, 50);

  // Slider on Tablet
  const tSlTrack = figma.createFrame(); tSlTrack.resize(660, 8); tSlTrack.x = 24; tSlTrack.y = 100; tSlTrack.cornerRadius = 4; tSlTrack.fills = [{ type: "SOLID", color: cBorder }]; tCalc.appendChild(tSlTrack);
  const tSlFill = figma.createFrame(); tSlFill.resize(396, 8); tSlFill.x = 132; tSlFill.y = 100; tSlFill.cornerRadius = 4; tSlFill.fills = [{ type: "SOLID", color: cPrimary }]; tCalc.appendChild(tSlFill);
  const tSlKnob = figma.createFrame(); tSlKnob.resize(22, 22); tSlKnob.x = 517; tSlKnob.y = 93; tSlKnob.cornerRadius = 11; tSlKnob.fills = [{ type: "SOLID", color: cWhite }]; tSlKnob.strokes = [{ type: "SOLID", color: cPrimary }]; tCalc.appendChild(tSlKnob);
  helperText(tCalc, "0%                                  20% (Старт)                                 80% (Ціль)                      100%", 11, "Medium", cMuted, 24, 120);

  helperText(tCalc, "652.50 ₴ · ~28 хв на DC 120 кВт", 22, "Bold", cDark, 24, 160);
  helperText(tCalc, "Тариф: 14.12 ₴ / кВт·год · Спожито: 46.2 кВт·год", 12, "Regular", cMuted, 24, 195);
  const tCalcBtn = figma.createFrame(); tCalcBtn.resize(240, 42); tCalcBtn.x = 24; tCalcBtn.y = 230; tCalcBtn.cornerRadius = 8; tCalcBtn.fills = [{ type: "SOLID", color: cPrimary }]; tCalc.appendChild(tCalcBtn);
  helperText(tCalcBtn, "Знайти вільну станцію", 13, "Bold", cWhite, 45, 12);

  // Tablet Map Section
  const tMapSec = figma.createFrame(); tMapSec.resize(708, 250); tMapSec.x = 30; tMapSec.y = 1070; tMapSec.cornerRadius = 14; tMapSec.fills = [{ type: "SOLID", color: cBgSurface }]; tMapSec.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tMapSec);
  helperText(tMapSec, "Live-карта зарядної мережі України", 16, "Bold", cDark, 20, 16);
  mapPinsData.slice(0, 3).forEach((pin, pidx) => {
    const pt = figma.createFrame(); pt.resize(200, 24); pt.x = 20 + pidx * 220; pt.y = 200; pt.cornerRadius = 5; pt.fills = [{ type: "SOLID", color: cDark }]; tMapSec.appendChild(pt);
    helperText(pt, pin.name.slice(0, 26) + "...", 9, "Bold", cWhite, 6, 6);
  });

  // Tablet Popular Stations (2 cards)
  helperText(fTablet, "Популярні зарядні хаби", 22, "Bold", cDark, 30, 1345);
  stationsData.slice(0, 2).forEach((st, idx) => {
    const tSc = figma.createFrame(); tSc.resize(708, 280); tSc.x = 30; tSc.y = 1385 + idx * 300; tSc.cornerRadius = 14; tSc.fills = [{ type: "SOLID", color: cWhite }]; tSc.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tSc);
    addImageRect(tSc, st.img, 0, 0, 708, 150, 0);
    helperText(tSc, st.title, 16, "Bold", cDark, 20, 170);
    helperText(tSc, st.addr, 13, "Regular", cMuted, 20, 195);
    const tSp = figma.createFrame(); tSp.resize(170, 24); tSp.x = 20; tSp.y = 225; tSp.cornerRadius = 6; tSp.fills = [{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }]; tSc.appendChild(tSp);
    helperText(tSp, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 5);
  });

  // Tablet Generator Section
  const tGenSec = figma.createFrame(); tGenSec.resize(708, 260); tGenSec.x = 30; tGenSec.y = 2005; tGenSec.cornerRadius = 14; tGenSec.fills = [{ type: "SOLID", color: cDark }]; fTablet.appendChild(tGenSec);
  addImageRect(tGenSec, "generator", 420, 15, 270, 230, 10);
  helperText(tGenSec, "⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%", 11, "Bold", { r: 74/255, g: 222/255, b: 128/255 }, 20, 25);
  helperText(tGenSec, "Заряджайте авто\\nпід час блекаутів", 22, "Bold", cWhite, 20, 60);
  helperText(tGenSec, "180+ станцій мережі обладнані потужними генераторами 160 кВт.", 13, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 20, 130, 380);

  // Tablet Steps
  helperText(fTablet, "Як зарядитися за 3 кроки", 22, "Bold", cDark, 30, 2290);
  stepsList.forEach((sp, idx) => {
    const tSt = figma.createFrame(); tSt.resize(708, 75); tSt.x = 30; tSt.y = 2330 + idx * 85; tSt.cornerRadius = 10; tSt.fills = [{ type: "SOLID", color: cBgSurface }]; tSt.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tSt);
    const tCirc = figma.createFrame(); tCirc.resize(32, 32); tCirc.x = 16; tCirc.y = 21; tCirc.cornerRadius = 16; tCirc.fills = [{ type: "SOLID", color: cPrimary }]; tSt.appendChild(tCirc);
    helperText(tCirc, sp.num, 14, "Bold", cWhite, 11, 7);
    helperText(tSt, sp.title, 14, "Bold", cDark, 60, 18);
    helperText(tSt, sp.desc, 12, "Regular", cMuted, 60, 42, 620);
  });

  // Tablet Reviews
  helperText(fTablet, "Відгуки водіїв", 22, "Bold", cDark, 30, 2615);
  reviewsList.slice(0, 2).forEach((rv, idx) => {
    const tRev = figma.createFrame(); tRev.resize(344, 180); tRev.x = 30 + idx * 364; tRev.y = 2655; tRev.cornerRadius = 12; tRev.fills = [{ type: "SOLID", color: cWhite }]; tRev.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tRev);
    helperText(tRev, "★★★★★", 12, "Bold", { r: 245/255, g: 158/255, b: 11/255 }, 18, 16);
    helperText(tRev, `«${rv.text}»`, 12, "Medium", cDark, 18, 42, 308);
    addImageRect(tRev, rv.av, 18, 120, 36, 36, 18);
    helperText(tRev, rv.name, 13, "Bold", cDark, 64, 122);
    helperText(tRev, rv.car, 11, "Regular", cMuted, 64, 140);
  });

  // Tablet B2B Form
  const tForm = figma.createFrame(); tForm.resize(708, 200); tForm.x = 30; tForm.y = 2865; tForm.cornerRadius = 14; tForm.fills = [{ type: "SOLID", color: cBgSurface }]; tForm.strokes = [{ type: "SOLID", color: cBorder }]; fTablet.appendChild(tForm);
  helperText(tForm, "Встановіть станцію ChargeUA на вашій локації", 18, "Bold", cDark, 24, 24);
  const tInp1 = figma.createFrame(); tInp1.resize(310, 42); tInp1.x = 24; tInp1.y = 70; tInp1.cornerRadius = 6; tInp1.fills = [{ type: "SOLID", color: cWhite }]; tInp1.strokes = [{ type: "SOLID", color: cBorder }]; tForm.appendChild(tInp1);
  helperText(tInp1, "Ваше ім'я", 12, "Regular", cMuted, 14, 13);
  const tInp2 = figma.createFrame(); tInp2.resize(310, 42); tInp2.x = 374; tInp2.y = 70; tInp2.cornerRadius = 6; tInp2.fills = [{ type: "SOLID", color: cWhite }]; tInp2.strokes = [{ type: "SOLID", color: cBorder }]; tForm.appendChild(tInp2);
  helperText(tInp2, "Телефон (+380...)", 12, "Regular", cMuted, 14, 13);
  const tSubBtn = figma.createFrame(); tSubBtn.resize(240, 42); tSubBtn.x = 24; tSubBtn.y = 130; tSubBtn.cornerRadius = 8; tSubBtn.fills = [{ type: "SOLID", color: cPrimary }]; tForm.appendChild(tSubBtn);
  helperText(tSubBtn, "Подати заявку на монтаж", 13, "Bold", cWhite, 35, 12);

  // Tablet Footer
  const tFooter = figma.createFrame(); tFooter.resize(768, 280); tFooter.y = 3095; tFooter.fills = [{ type: "SOLID", color: cDark }]; fTablet.appendChild(tFooter);
  addSvgNode(tFooter, "logo", 30, 35, 32, 32);
  helperText(tFooter, "ChargeUA", 20, "Bold", cWhite, 72, 40);
  helperText(tFooter, "Національний агрегатор зарядної інфраструктури України.", 12, "Regular", { r: 148/255, g: 163/255, b: 184/255 }, 30, 80, 260);
  helperText(tFooter, "Навігація:\\n• Головна\\n• Калькулятор\\n• Карта станцій\\n• Тарифи", 12, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 330, 40);
  helperText(tFooter, "Контакти:\\n• 0 800 300 400\\n• support@charge.ua\\n• м. Київ, Сагайдачного 12", 12, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 530, 40);
  helperText(tFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24", 11, "Regular", { r: 100/255, g: 116/255, b: 139/255 }, 30, 230);

  // FRAME 07: FULL MOBILE (390 × 3650) - MATCHING USER PHOTO PIXEL-FOR-PIXEL
  const fMobile = figma.createFrame();
  fMobile.name = "07_Mobile";
  fMobile.resize(390, 3650);
  fMobile.x = 2500; fMobile.y = 2300;
  fMobile.fills = [{ type: "SOLID", color: cWhite }];

  // Mobile Topbar
  const mTop = figma.createFrame(); mTop.resize(390, 34); mTop.fills = [{ type: "SOLID", color: cDark }]; fMobile.appendChild(mTop);
  helperText(mTop, "● 480+ станцій онлайн | 0 800 300 400", 10, "Medium", cWhite, 16, 9);

  // Mobile Header
  const mHead = figma.createFrame(); mHead.resize(390, 56); mHead.y = 34; mHead.fills = [{ type: "SOLID", color: cWhite }]; mHead.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mHead);
  addSvgNode(mHead, "logo", 16, 14, 28, 28);
  helperText(mHead, "ChargeUA", 19, "Bold", cPrimary, 52, 17);
  helperText(mHead, "☰", 22, "Bold", cDark, 350, 14);

  // Mobile Hero (EXACTLY MATCHING USER'S SCREENSHOT)
  const mHero = figma.createFrame(); mHero.resize(390, 430); mHero.y = 90; mHero.fills = [{ type: "SOLID", color: cWhite }]; fMobile.appendChild(mHero);
  helperText(mHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР", 10, "Bold", cPrimary, 20, 18);
  helperText(mHero, "Заряджайте авто\\nбез стресу", 28, "Bold", cDark, 20, 42);
  helperText(mHero, "Усі мережі на одній карті з фільтром генераторів у блекаути.", 13, "Regular", cMuted, 20, 120, 350);

  // Hero Video/Car Visual with Play Button
  const mHeroImgBox = figma.createFrame(); mHeroImgBox.resize(350, 180); mHeroImgBox.x = 20; mHeroImgBox.y = 175; mHeroImgBox.cornerRadius = 14; mHeroImgBox.fills = [{ type: "SOLID", color: cDark }]; mHero.appendChild(mHeroImgBox);
  addImageRect(mHeroImgBox, "video", 0, 0, 350, 180, 14);
  const mPlay = figma.createFrame(); mPlay.resize(44, 44); mPlay.x = 153; mPlay.y = 68; mPlay.cornerRadius = 22; mPlay.fills = [{ type: "SOLID", color: cPrimary }]; mHeroImgBox.appendChild(mPlay);
  helperText(mPlay, "▶", 16, "Bold", cWhite, 16, 12);

  const mBtn = figma.createFrame(); mBtn.resize(350, 44); mBtn.x = 20; mBtn.y = 370; mBtn.cornerRadius = 8; mBtn.fills = [{ type: "SOLID", color: cPrimary }]; mHero.appendChild(mBtn);
  helperText(mBtn, "Розрахувати зарядку →", 13, "Bold", cWhite, 95, 13);

  // Mobile Calculator Card WITH SLIDER (ПОВЗУНОК)
  const mCalc = figma.createFrame(); mCalc.resize(350, 260); mCalc.x = 20; mCalc.y = 535; mCalc.cornerRadius = 14; mCalc.fills = [{ type: "SOLID", color: cWhite }]; mCalc.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mCalc);
  helperText(mCalc, "Калькулятор витрат", 17, "Bold", cDark, 16, 16);
  helperText(mCalc, "VW ID.4 · 20% → 80%", 13, "Semi Bold", cPrimary, 16, 42);

  // Slider on Mobile
  const mSlTrack = figma.createFrame(); mSlTrack.resize(318, 8); mSlTrack.x = 16; mSlTrack.y = 78; mSlTrack.cornerRadius = 4; mSlTrack.fills = [{ type: "SOLID", color: cBorder }]; mCalc.appendChild(mSlTrack);
  const mSlFill = figma.createFrame(); mSlFill.resize(190, 8); mSlFill.x = 64; mSlFill.y = 78; mSlFill.cornerRadius = 4; mSlFill.fills = [{ type: "SOLID", color: cPrimary }]; mCalc.appendChild(mSlFill);
  const mSlKnob = figma.createFrame(); mSlKnob.resize(20, 20); mSlKnob.x = 244; mSlKnob.y = 72; mSlKnob.cornerRadius = 10; mSlKnob.fills = [{ type: "SOLID", color: cWhite }]; mSlKnob.strokes = [{ type: "SOLID", color: cPrimary }]; mCalc.appendChild(mSlKnob);
  helperText(mCalc, "0%        20% (Старт)        50%        80% (Ціль)        100%", 9, "Medium", cMuted, 16, 96);

  helperText(mCalc, "652.50 ₴ (~28 хв)", 21, "Bold", cDark, 16, 122);
  helperText(mCalc, "Тариф: 14.12 ₴/кВт·год · 46.2 кВт", 12, "Regular", cMuted, 16, 154);
  const mCalcAct = figma.createFrame(); mCalcAct.resize(318, 42); mCalcAct.x = 16; mCalcAct.y = 195; mCalcAct.cornerRadius = 8; mCalcAct.fills = [{ type: "SOLID", color: cPrimary }]; mCalc.appendChild(mCalcAct);
  helperText(mCalcAct, "Знайти вільну станцію", 13, "Bold", cWhite, 85, 13);

  // Mobile Station Cards (2 cards)
  helperText(fMobile, "Популярні зарядні хаби", 18, "Bold", cDark, 20, 815);
  stationsData.slice(0, 2).forEach((st, idx) => {
    const mSc = figma.createFrame(); mSc.resize(350, 280); mSc.x = 20; mSc.y = 850 + idx * 295; mSc.cornerRadius = 14; mSc.fills = [{ type: "SOLID", color: cWhite }]; mSc.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mSc);
    addImageRect(mSc, st.img, 0, 0, 350, 140, 0);
    helperText(mSc, st.title, 14, "Bold", cDark, 16, 155);
    helperText(mSc, st.addr, 11, "Regular", cMuted, 16, 178);

    const mPill = figma.createFrame(); mPill.resize(160, 22); mPill.x = 16; mPill.y = 202; mPill.cornerRadius = 4; mPill.fills = [{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }]; mSc.appendChild(mPill);
    helperText(mPill, st.gen ? "🔋 Генератор ON" : "⚡ Мережа ON", 10, "Bold", st.gen ? cSuccess : cPrimary, 8, 4);

    const mSb = figma.createFrame(); mSb.resize(318, 38); mSb.x = 16; mSb.y = 230; mSb.cornerRadius = 8; mSb.fills = [{ type: "SOLID", color: cPrimary }]; mSc.appendChild(mSb);
    helperText(mSb, "Прокласти маршрут", 12, "Bold", cWhite, 95, 11);
  });

  // Mobile Map Section
  const mMapSec = figma.createFrame(); mMapSec.resize(350, 200); mMapSec.x = 20; mMapSec.y = 1460; mMapSec.cornerRadius = 14; mMapSec.fills = [{ type: "SOLID", color: cBgSurface }]; mMapSec.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mMapSec);
  helperText(mMapSec, "Live-карта зарядної мережі", 15, "Bold", cDark, 16, 16);
  mapPinsData.slice(0, 2).forEach((pin, pidx) => {
    const mp = figma.createFrame(); mp.resize(180, 22); mp.x = 16; mp.y = 110 + pidx * 35; mp.cornerRadius = 4; mp.fills = [{ type: "SOLID", color: cDark }]; mMapSec.appendChild(mp);
    helperText(mp, pin.name.slice(0, 22) + "...", 9, "Bold", cWhite, 6, 5);
  });

  // Mobile Generator Section
  const mGenSec = figma.createFrame(); mGenSec.resize(350, 240); mGenSec.x = 20; mGenSec.y = 1680; mGenSec.cornerRadius = 14; mGenSec.fills = [{ type: "SOLID", color: cDark }]; fMobile.appendChild(mGenSec);
  addImageRect(mGenSec, "generator", 0, 0, 350, 110, 0);
  helperText(mGenSec, "⚡ Резервне живлення 160 кВт", 11, "Bold", { r: 74/255, g: 222/255, b: 128/255 }, 16, 125);
  helperText(mGenSec, "180+ станцій працюють під час блекаутів", 14, "Bold", cWhite, 16, 145);
  helperText(mGenSec, "Автоматичний генератор гарантує швидку зарядку навіть у разі аварійних вимкнень.", 11, "Regular", { r: 203/255, g: 213/255, b: 225/255 }, 16, 175, 318);

  // Mobile Steps
  helperText(fMobile, "Як зарядитися за 3 кроки", 18, "Bold", cDark, 20, 1940);
  stepsList.forEach((sp, idx) => {
    const mSt = figma.createFrame(); mSt.resize(350, 70); mSt.x = 20; mSt.y = 1975 + idx * 80; mSt.cornerRadius = 10; mSt.fills = [{ type: "SOLID", color: cBgSurface }]; mSt.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mSt);
    const mCirc = figma.createFrame(); mCirc.resize(30, 30); mCirc.x = 14; mCirc.y = 20; mCirc.cornerRadius = 15; mCirc.fills = [{ type: "SOLID", color: cPrimary }]; mSt.appendChild(mCirc);
    helperText(mCirc, sp.num, 13, "Bold", cWhite, 10, 7);
    helperText(mSt, sp.title, 13, "Bold", cDark, 54, 16);
    helperText(mSt, sp.desc, 11, "Regular", cMuted, 54, 38, 280);
  });

  // Mobile Reviews
  helperText(fMobile, "Відгуки водіїв", 18, "Bold", cDark, 20, 2235);
  reviewsList.slice(0, 2).forEach((rv, idx) => {
    const mRv = figma.createFrame(); mRv.resize(350, 140); mRv.x = 20; mRv.y = 2270 + idx * 150; mRv.cornerRadius = 12; mRv.fills = [{ type: "SOLID", color: cWhite }]; mRv.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mRv);
    helperText(mRv, "★★★★★", 11, "Bold", { r: 245/255, g: 158/255, b: 11/255 }, 14, 12);
    helperText(mRv, `«${rv.text}»`, 11.5, "Medium", cDark, 14, 34, 320);
    addImageRect(mRv, rv.av, 14, 90, 32, 32, 16);
    helperText(mRv, rv.name, 12, "Bold", cDark, 54, 92);
    helperText(mRv, rv.car, 10, "Regular", cMuted, 54, 108);
  });

  // Mobile B2B Form
  const mForm = figma.createFrame(); mForm.resize(350, 180); mForm.x = 20; mForm.y = 2590; mForm.cornerRadius = 12; mForm.fills = [{ type: "SOLID", color: cDark }]; fMobile.appendChild(mForm);
  helperText(mForm, "Встановіть станцію ChargeUA", 15, "Bold", cWhite, 16, 16);
  helperText(mForm, "Отримуйте дохід від зарядки авто клієнтів", 11, "Regular", { r: 148/255, g: 163/255, b: 184/255 }, 16, 38);
  const mInp = figma.createFrame(); mInp.resize(318, 36); mInp.x = 16; mInp.y = 68; mInp.cornerRadius = 6; mInp.fills = [{ type: "SOLID", color: { r: 30/255, g: 41/255, b: 59/255 } }]; mForm.appendChild(mInp);
  helperText(mInp, "Ваше ім'я та телефон", 11, "Regular", cMuted, 12, 10);
  const mSub = figma.createFrame(); mSub.resize(318, 38); mSub.x = 16; mSub.y = 118; mSub.cornerRadius = 6; mSub.fills = [{ type: "SOLID", color: cPrimary }]; mForm.appendChild(mSub);
  helperText(mSub, "Подати заявку на монтаж", 12, "Bold", cWhite, 75, 11);

  // Mobile Footer
  const mFooter = figma.createFrame(); mFooter.resize(390, 200); mFooter.y = 2790; mFooter.fills = [{ type: "SOLID", color: cDark }]; fMobile.appendChild(mFooter);
  addSvgNode(mFooter, "logo", 20, 20, 24, 24);
  helperText(mFooter, "ChargeUA", 16, "Bold", cWhite, 52, 23);
  helperText(mFooter, "Національний агрегатор зарядної інфраструктури України.", 11, "Regular", { r: 148/255, g: 163/255, b: 184/255 }, 20, 56, 350);
  helperText(mFooter, "0 800 300 400 · support@charge.ua\\n© 2026 ChargeUA · Лемішка Андрій, ПП-24", 10, "Regular", { r: 100/255, g: 116/255, b: 139/255 }, 20, 100);

  // Sticky Bottom Navigation
  const mBottomNav = figma.createFrame(); mBottomNav.resize(390, 54); mBottomNav.y = 3000; mBottomNav.fills = [{ type: "SOLID", color: cWhite }]; mBottomNav.strokes = [{ type: "SOLID", color: cBorder }]; fMobile.appendChild(mBottomNav);
  helperText(mBottomNav, "⚡ Головна           🗺 Карта           🧮 Калькулятор           👤 Профіль", 11, "Bold", cDark, 20, 18);
"""

# Replace block from `const fDesktop = figma.createFrame();` to `const fCatalog = figma.createFrame();`
pos_desk = code.find('const fDesktop = figma.createFrame();')
pos_cat = code.find('const fCatalog = figma.createFrame();')

new_code = code[:pos_desk] + new_desktop_tablet_mobile + "\n  " + code[pos_cat:]

with open(GEN_SCRIPT, "w", encoding="utf-8") as f:
    f.write(new_code)

print("Updated generate_final_figma_plugin.py successfully!")
