# -*- coding: utf-8 -*-
"""
Script to apply all required modifications to generate_final_figma_plugin.py:
1. Remove supervisor and university department from 00_Cover.
2. Rebuild 03_Wireframes to match Image 5 grey-block schematic style with Live Map after Calculator.
3. Update 04.1_Design_System: replace B2B promo code and offer with Search, battery capacity, driver filters, and generator switches.
4. Fix 05_Desktop Hero vertical alignment to completely eliminate text overlap.
5. Add linkScroll helper and connect all interactive buttons to page anchors.
"""

import re

SRC_FILE = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\generate_final_figma_plugin.py"

with open(SRC_FILE, "r", encoding="utf-8") as f:
    code = f.read()

# -----------------------------------------------------------------------------
# 1. ADD linkScroll HELPER FUNCTION
# -----------------------------------------------------------------------------
scroll_func = """  async function linkScroll(sourceNode, targetNode) {
    if (!sourceNode || !targetNode || !targetNode.id) return;
    try {
      const reaction = {
        trigger: { type: "ON_CLICK" },
        action: {
          type: "NODE",
          destinationId: targetNode.id,
          navigation: "SCROLL_TO",
          transition: {
            type: "SMART_ANIMATE",
            duration: 0.35,
            easing: { type: "EASE_IN_AND_OUT" }
          }
        }
      };
      if (typeof sourceNode.setReactionsAsync === "function") {
        await sourceNode.setReactionsAsync([reaction]);
      } else {
        sourceNode.reactions = [reaction];
      }
    } catch (e) {
      console.warn("linkScroll error:", e);
    }
  }
"""

if "async function linkScroll" not in code:
    code = code.replace("  async function linkClose(sourceNode) {", scroll_func + "\n  async function linkClose(sourceNode) {")

# -----------------------------------------------------------------------------
# 2. UPDATE 00_COVER: REMOVE SUPERVISOR AND UNIVERSITY HEAD OF DEPARTMENT
# -----------------------------------------------------------------------------
old_cover_pattern = re.compile(
    r'  // FRAME 00: COVER.*?addImageRect\(coverCard, "hero", 60, 540, 1200, 200, 16\);',
    re.DOTALL
)

new_cover_block = """  // FRAME 00: COVER
  const fCover = figma.createFrame();
  fCover.name = "00_Cover";
  fCover.resize(1440, 900);
  fCover.x = 0; fCover.y = 0;
  fCover.fills = [{ type: "SOLID", color: cDark }];

  const coverCard = figma.createFrame();
  coverCard.resize(1320, 780);
  coverCard.x = 60; coverCard.y = 60;
  coverCard.cornerRadius = 24;
  coverCard.fills = [{ type: "SOLID", color: { r: 30/255, g: 41/255, b: 59/255 } }];
  fCover.appendChild(coverCard);

  addSvgNode(coverCard, "logo", 60, 60, 64, 64);
  helperText(coverCard, "ChargeUA", 36, "Bold", cWhite, 140, 75);
  helperText(coverCard, "Лабораторна робота №4 · Проєктування інтерфейсу користувача (UI/UX)", 18, "Medium", cPrimary, 60, 155);
  helperText(coverCard, "Національний веб-сервіс та агрегатор швидкісних електрозарядних станцій", 34, "Bold", cWhite, 60, 195, 1200);

  const metaBox = figma.createFrame();
  metaBox.resize(1200, 180);
  metaBox.x = 60; metaBox.y = 310;
  metaBox.cornerRadius = 16;
  metaBox.fills = [{ type: "SOLID", color: cDark }];
  coverCard.appendChild(metaBox);

  helperText(metaBox, "Автор проєкту:", 13, "Medium", cMuted, 40, 28);
  helperText(metaBox, "Лемішка Андрій, студент групи ПП-24", 16, "Bold", cWhite, 40, 50);
  helperText(metaBox, "Дисципліна:", 13, "Medium", cMuted, 40, 95);
  helperText(metaBox, "Технології розробки веб-застосунків (2026)", 15, "Semi Bold", cWhite, 40, 118);

  helperText(metaBox, "Архітектура та стандарти:", 13, "Medium", cMuted, 620, 28);
  helperText(metaBox, "Desktop (1440px) · Tablet (768px) · Mobile (390px)", 16, "Bold", cWhite, 620, 50);
  helperText(metaBox, "UI Kit & Статус:", 13, "Medium", cMuted, 620, 95);
  helperText(metaBox, "WCAG 2.2 AA · 100% Компонентність · Interactive Prototype (76+ зв'язків)", 15, "Semi Bold", { r: 74/255, g: 222/255, b: 128/255 }, 620, 118);

  addImageRect(coverCard, "hero", 60, 520, 1200, 220, 16);"""

code = old_cover_pattern.sub(new_cover_block, code)

# -----------------------------------------------------------------------------
# 3. REBUILD 03_WIREFRAMES: EXACT IMAGE 5 STYLE (GREY BLOCKS + DASHED DIVIDERS + LIVE MAP AFTER CALC)
# -----------------------------------------------------------------------------
old_wf_pattern = re.compile(
    r'  // FRAME 03: WIREFRAMES.*?// FRAME 04: DESIGN ASSETS',
    re.DOTALL
)

new_wf_block = """  // FRAME 03: WIREFRAMES
  const fWireframes = figma.createFrame();
  fWireframes.name = "03_Wireframes";
  fWireframes.resize(1440, 1080);
  fWireframes.x = 4800; fWireframes.y = 0;
  fWireframes.fills = [{ type: "SOLID", color: cBgSurface }];

  helperText(fWireframes, "03 Каркаси сторінок (Wireframes)", 28, "Bold", cDark, 60, 40);
  helperText(fWireframes, "Низькодеталізовані схематичні каркаси: Головна сторінка Desktop (1440px) та Mobile (390px)", 15, "Regular", cMuted, 60, 75);

  // Desktop Wireframe Box (Left side: 780 x 920)
  const wfDesk = figma.createFrame();
  wfDesk.resize(780, 920);
  wfDesk.x = 60; wfDesk.y = 120;
  wfDesk.cornerRadius = 12;
  wfDesk.fills = [{ type: "SOLID", color: cWhite }];
  wfDesk.strokes = [{ type: "SOLID", color: { r: 148/255, g: 163/255, b: 184/255 } }];
  fWireframes.appendChild(wfDesk);

  // 1. Header wireframe
  const wfDHead = figma.createFrame(); wfDHead.resize(740, 42); wfDHead.x = 20; wfDHead.y = 16; wfDHead.cornerRadius = 6; wfDHead.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; wfDesk.appendChild(wfDHead);
  helperText(wfDHead, "⚡ [LOGO] ChargeUA", 11, "Bold", cDark, 14, 13);
  helperText(wfDHead, "Головна | Калькулятор | Карта станцій | Популярні хаби | Інструкція | Відгуки", 9.5, "Medium", cMuted, 150, 14);
  const wfDHBtn = figma.createFrame(); wfDHBtn.resize(86, 26); wfDHBtn.x = 640; wfDHBtn.y = 8; wfDHBtn.cornerRadius = 4; wfDHBtn.fills = [{ type: "SOLID", color: cDark }]; wfDHead.appendChild(wfDHBtn);
  helperText(wfDHBtn, "[Знайти хаб]", 9, "Bold", cWhite, 12, 7);

  // Divider 1
  const div1 = figma.createFrame(); div1.resize(740, 1.5); div1.x = 20; div1.y = 66; div1.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div1);

  // 2. Hero Section wireframe
  helperText(wfDesk, "HERO SECTION", 9.5, "Bold", cMuted, 20, 76);
  const wfDHl1 = figma.createFrame(); wfDHl1.resize(260, 14); wfDHl1.x = 20; wfDHl1.y = 96; wfDHl1.cornerRadius = 3; wfDHl1.fills = [{ type: "SOLID", color: { r: 148/255, g: 163/255, b: 184/255 } }]; wfDesk.appendChild(wfDHl1);
  const wfDHl2 = figma.createFrame(); wfDHl2.resize(340, 8); wfDHl2.x = 20; wfDHl2.y = 118; wfDHl2.cornerRadius = 2; wfDHl2.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(wfDHl2);
  const wfDHl3 = figma.createFrame(); wfDHl3.resize(220, 8); wfDHl3.x = 20; wfDHl3.y = 132; wfDHl3.cornerRadius = 2; wfDHl3.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(wfDHl3);
  const wfDB1 = figma.createFrame(); wfDB1.resize(100, 26); wfDB1.x = 20; wfDB1.y = 150; wfDB1.cornerRadius = 4; wfDB1.fills = [{ type: "SOLID", color: cPrimary }]; wfDesk.appendChild(wfDB1);
  helperText(wfDB1, "Розрахувати →", 9, "Bold", cWhite, 16, 7);
  const wfDB2 = figma.createFrame(); wfDB2.resize(85, 26); wfDB2.x = 128; wfDB2.y = 150; wfDB2.cornerRadius = 4; wfDB2.fills = [{ type: "SOLID", color: cWhite }]; wfDB2.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDB2);
  helperText(wfDB2, "На карті", 9, "Bold", cDark, 18, 7);
  const wfDHImg = figma.createFrame(); wfDHImg.resize(250, 85); wfDHImg.x = 490; wfDHImg.y = 90; wfDHImg.cornerRadius = 6; wfDHImg.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfDHImg.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDHImg);
  helperText(wfDHImg, "[Hero Image: Car + Station]", 9.5, "Medium", cMuted, 38, 35);

  // Divider 2
  const div2 = figma.createFrame(); div2.resize(740, 1.5); div2.x = 20; div2.y = 188; div2.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div2);

  // 3. 3 Benefits Strip
  helperText(wfDesk, "3 BENEFITS STRIP", 9.5, "Bold", cMuted, 20, 196);
  const bTitles = ["[Icon] Калькулятор", "[Icon] Live-карта 480+", "[Icon] 100% Генератор"];
  bTitles.forEach((bt, bIdx) => {
    const bCard = figma.createFrame(); bCard.resize(236, 38); bCard.x = 20 + bIdx * 252; bCard.y = 216; bCard.cornerRadius = 6; bCard.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; bCard.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(bCard);
    helperText(bCard, bt, 9.5, "Bold", cDark, 30, 12);
  });

  // Divider 3
  const div3 = figma.createFrame(); div3.resize(740, 1.5); div3.x = 20; div3.y = 266; div3.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div3);

  // 4. Interactive Calculator
  helperText(wfDesk, "INTERACTIVE CALCULATOR", 9.5, "Bold", cMuted, 20, 274);
  const wfDCalc = figma.createFrame(); wfDCalc.resize(740, 72); wfDCalc.x = 20; wfDCalc.y = 294; wfDCalc.cornerRadius = 6; wfDCalc.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfDCalc.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDCalc);
  helperText(wfDCalc, "[Car Presets: Tesla Model 3 | VW ID.4 | Nissan Leaf]", 9.5, "Bold", cDark, 16, 10);
  const slBar = figma.createFrame(); slBar.resize(540, 6); slBar.x = 16; slBar.y = 34; slBar.cornerRadius = 3; slBar.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDCalc.appendChild(slBar);
  const slThm = figma.createFrame(); slThm.resize(14, 14); slThm.x = 340; slThm.y = 30; slThm.cornerRadius = 7; slThm.fills = [{ type: "SOLID", color: cPrimary }]; wfDCalc.appendChild(slThm);
  helperText(wfDCalc, "652.50 ₴ · ~28 хв (CCS2 Ultra) · Заощадження vs бензин: ~1 450 ₴", 10, "Bold", cDark, 16, 48);

  // Divider 4
  const div4 = figma.createFrame(); div4.resize(740, 1.5); div4.x = 20; div4.y = 378; div4.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div4);

  // 5. LIVE-КАРТА (IMMEDIATELY AFTER CALCULATOR!)
  helperText(wfDesk, "LIVE-КАРТА ЗАРЯДНОЇ МЕРЕЖІ (ONLINE MAP)", 9.5, "Bold", cPrimary, 20, 386);
  const wfDMapBox = figma.createFrame(); wfDMapBox.resize(740, 84); wfDMapBox.x = 20; wfDMapBox.y = 406; wfDMapBox.cornerRadius = 6; wfDMapBox.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; wfDMapBox.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDMapBox);
  helperText(wfDMapBox, "🗺 [Інтерактивна Live-карта: 480+ станцій онлайн із телеметрією конекторів]", 10, "Bold", cPrimary, 20, 18);
  helperText(wfDMapBox, "[Фільтри: Тільки вільні порти | Потужність 120–160 кВт | 🔋 Гарантований генератор]", 9, "Medium", cMuted, 20, 44);

  // Divider 5
  const div5 = figma.createFrame(); div5.resize(740, 1.5); div5.x = 20; div5.y = 502; div5.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div5);

  // 6. Popular Stations Grid
  helperText(wfDesk, "POPULAR STATIONS GRID", 9.5, "Bold", cMuted, 20, 510);
  const stWireData = [
    { title: "[Card] Хаб «Київ-Поділ» · 120 кВт CCS2", addr: "вул. Сагайдачного, 12 · 3/4 вільно", gen: "🔋 Генератор ON" },
    { title: "[Card] Хаб «Львів-Арена» · 160 кВт CCS2", addr: "вул. Стрийська, 199 · 5/6 вільно", gen: "🔋 Генератор ON" }
  ];
  stWireData.forEach((st, sIdx) => {
    const sBox = figma.createFrame(); sBox.resize(360, 64); sBox.x = 20 + sIdx * 380; sBox.y = 530; sBox.cornerRadius = 6; sBox.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; sBox.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(sBox);
    helperText(sBox, st.title, 9.5, "Bold", cDark, 12, 10);
    helperText(sBox, st.addr, 8.5, "Regular", cMuted, 12, 26);
    helperText(sBox, st.gen, 8.5, "Bold", cSuccess, 12, 42);
    const sBtn = figma.createFrame(); sBtn.resize(100, 22); sBtn.x = 246; sBtn.y = 34; sBtn.cornerRadius = 4; sBtn.fills = [{ type: "SOLID", color: cPrimary }]; sBox.appendChild(sBtn);
    helperText(sBtn, "Маршрут CCS2", 8.5, "Bold", cWhite, 12, 5);
  });

  // Divider 6
  const div6 = figma.createFrame(); div6.resize(740, 1.5); div6.x = 20; div6.y = 606; div6.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div6);

  // 7. Blackout Protection
  helperText(wfDesk, "BLACKOUT PROTECTION", 9.5, "Bold", cMuted, 20, 614);
  const wfDGen = figma.createFrame(); wfDGen.resize(740, 62); wfDGen.x = 20; wfDGen.y = 634; wfDGen.cornerRadius = 6; wfDGen.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfDGen.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDGen);
  helperText(wfDGen, "⚡ [Industrial Generator Cummins 160 kW Specs]", 10, "Bold", cDark, 16, 12);
  helperText(wfDGen, "Автономність 48 годин без електромережі · Супутниковий Starlink · Автоматичний ввід резерву 15 сек", 9, "Regular", cMuted, 16, 34);

  // Divider 7
  const div7 = figma.createFrame(); div7.resize(740, 1.5); div7.x = 20; div7.y = 708; div7.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfDesk.appendChild(div7);

  // 8. How to Charge & Driver Reviews
  helperText(wfDesk, "HOW TO CHARGE & DRIVER REVIEWS", 9.5, "Bold", cMuted, 20, 716);
  const wfDRev = figma.createFrame(); wfDRev.resize(740, 56); wfDRev.x = 20; wfDRev.y = 736; wfDRev.cornerRadius = 6; wfDRev.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; wfDRev.strokes = [{ type: "SOLID", color: cBorder }]; wfDesk.appendChild(wfDRev);
  helperText(wfDRev, "[Крок 1: Карта] → [Крок 2: CCS2] → [Крок 3: Оплата]", 9, "Semi Bold", cDark, 16, 12);
  helperText(wfDRev, "★★★★★ «Під час блекауту дуже виручило! Генератор на Подолі працював безперебійно.»", 9, "Regular", cMuted, 16, 32);

  // 9. Footer
  const wfDFoot = figma.createFrame(); wfDFoot.resize(740, 52); wfDFoot.x = 20; wfDFoot.y = 810; wfDFoot.cornerRadius = 6; wfDFoot.fills = [{ type: "SOLID", color: cDark }]; wfDesk.appendChild(wfDFoot);
  helperText(wfDFoot, "⚡ [Footer 4 Columns & Copyright ChargeUA 2026]", 9.5, "Bold", cWhite, 20, 18);

  // Mobile Wireframe Box (Right side: 480 x 920)
  const wfMob = figma.createFrame();
  wfMob.resize(480, 920);
  wfMob.x = 880; wfMob.y = 120;
  wfMob.cornerRadius = 12;
  wfMob.fills = [{ type: "SOLID", color: cWhite }];
  wfMob.strokes = [{ type: "SOLID", color: { r: 148/255, g: 163/255, b: 184/255 } }];
  fWireframes.appendChild(wfMob);

  // Mobile Header
  const wfMHead = figma.createFrame(); wfMHead.resize(440, 40); wfMHead.x = 20; wfMHead.y = 16; wfMHead.cornerRadius = 6; wfMHead.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; wfMob.appendChild(wfMHead);
  helperText(wfMHead, "⚡ [LOGO] ChargeUA", 11, "Bold", cDark, 14, 12);
  helperText(wfMHead, "[☰ Меню]", 11, "Bold", cPrimary, 370, 12);

  // Mobile Hero
  const mDiv1 = figma.createFrame(); mDiv1.resize(440, 1.5); mDiv1.x = 20; mDiv1.y = 66; mDiv1.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv1);
  helperText(wfMob, "HERO (MOBILE 390px)", 9.5, "Bold", cMuted, 20, 76);
  const wfMHImg = figma.createFrame(); wfMHImg.resize(440, 70); wfMHImg.x = 20; wfMHImg.y = 96; wfMHImg.cornerRadius = 6; wfMHImg.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfMHImg.strokes = [{ type: "SOLID", color: cBorder }]; wfMob.appendChild(wfMHImg);
  helperText(wfMHImg, "[Hero Visual: Авто + Хаб]", 9.5, "Medium", cMuted, 140, 26);
  const wfMBtn = figma.createFrame(); wfMBtn.resize(440, 30); wfMBtn.x = 20; wfMBtn.y = 176; wfMBtn.cornerRadius = 4; wfMBtn.fills = [{ type: "SOLID", color: cPrimary }]; wfMob.appendChild(wfMBtn);
  helperText(wfMBtn, "Знайти найближчу станцію (GPS)", 9.5, "Bold", cWhite, 120, 8);

  // Mobile Benefits
  const mDiv2 = figma.createFrame(); mDiv2.resize(440, 1.5); mDiv2.x = 20; mDiv2.y = 218; mDiv2.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv2);
  helperText(wfMob, "3 BENEFITS STRIP", 9.5, "Bold", cMuted, 20, 226);
  const wfMBen = figma.createFrame(); wfMBen.resize(440, 48); wfMBen.x = 20; wfMBen.y = 246; wfMBen.cornerRadius = 6; wfMBen.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfMob.appendChild(wfMBen);
  helperText(wfMBen, "• Розрахунок витрат   • Live-карта 480+ хабів   • 100% Генератори", 9, "Semi Bold", cDark, 20, 16);

  // Mobile Calculator
  const mDiv3 = figma.createFrame(); mDiv3.resize(440, 1.5); mDiv3.x = 20; mDiv3.y = 304; mDiv3.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv3);
  helperText(wfMob, "MOBILE CALCULATOR", 9.5, "Bold", cMuted, 20, 312);
  const wfMCalc = figma.createFrame(); wfMCalc.resize(440, 64); wfMCalc.x = 20; wfMCalc.y = 332; wfMCalc.cornerRadius = 6; wfMCalc.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfMCalc.strokes = [{ type: "SOLID", color: cBorder }]; wfMob.appendChild(wfMCalc);
  helperText(wfMCalc, "Tesla Model 3 · 20% → 80%", 9, "Regular", cMuted, 16, 12);
  helperText(wfMCalc, "652.50 ₴ · ~28 хв (CCS2)", 10, "Bold", cDark, 16, 36);

  // Mobile Live Map (Immediately after Calculator!)
  const mDiv4 = figma.createFrame(); mDiv4.resize(440, 1.5); mDiv4.x = 20; mDiv4.y = 408; mDiv4.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv4);
  helperText(wfMob, "LIVE-КАРТА (MOBILE VIEW)", 9.5, "Bold", cPrimary, 20, 416);
  const wfMMap = figma.createFrame(); wfMMap.resize(440, 72); wfMMap.x = 20; wfMMap.y = 436; wfMMap.cornerRadius = 6; wfMMap.fills = [{ type: "SOLID", color: { r: 248/255, g: 250/255, b: 252/255 } }]; wfMMap.strokes = [{ type: "SOLID", color: cBorder }]; wfMob.appendChild(wfMMap);
  helperText(wfMMap, "🗺 [Мобільна карта станцій]", 9.5, "Bold", cPrimary, 16, 14);
  helperText(wfMMap, "[Фільтри: Вільні порти | 160 кВт | 🔋 Gen]", 8.5, "Regular", cMuted, 16, 38);

  // Mobile Hub Card
  const mDiv5 = figma.createFrame(); mDiv5.resize(440, 1.5); mDiv5.x = 20; mDiv5.y = 520; mDiv5.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv5);
  helperText(wfMob, "ПОПУЛЯРНІ СТАНЦІЇ", 9.5, "Bold", cMuted, 20, 528);
  const wfMHub = figma.createFrame(); wfMHub.resize(440, 64); wfMHub.x = 20; wfMHub.y = 548; wfMHub.cornerRadius = 6; wfMHub.fills = [{ type: "SOLID", color: { r: 241/255, g: 245/255, b: 249/255 } }]; wfMob.appendChild(wfMHub);
  helperText(wfMHub, "Хаб «Київ-Поділ» · 120 кВт CCS2", 9, "Bold", cDark, 12, 10);
  helperText(wfMHub, "🔋 Генератор ON · 3/4 вільні", 8.5, "Bold", cSuccess, 12, 28);
  const mHubBtn = figma.createFrame(); mHubBtn.resize(110, 20); mHubBtn.x = 318; mHubBtn.y = 34; mHubBtn.cornerRadius = 4; mHubBtn.fills = [{ type: "SOLID", color: cPrimary }]; wfMHub.appendChild(mHubBtn);
  helperText(mHubBtn, "Маршрут", 8.5, "Bold", cWhite, 28, 4);

  // Mobile Blackout Protection
  const mDiv6 = figma.createFrame(); mDiv6.resize(440, 1.5); mDiv6.x = 20; mDiv6.y = 624; mDiv6.fills = [{ type: "SOLID", color: { r: 203/255, g: 213/255, b: 225/255 } }]; wfMob.appendChild(mDiv6);
  helperText(wfMob, "РЕЗЕРВНЕ ЖИВЛЕННЯ 160 КВТ", 9.5, "Bold", cMuted, 20, 632);
  const wfMGen = figma.createFrame(); wfMGen.resize(440, 52); wfMGen.x = 20; wfMGen.y = 652; wfMGen.cornerRadius = 6; wfMGen.fills = [{ type: "SOLID", color: cDark }]; wfMob.appendChild(wfMGen);
  helperText(wfMGen, "⚡ 180+ станцій працюють під час блекаутів", 9, "Bold", { r: 74/255, g: 222/255, b: 128/255 }, 16, 10);
  helperText(wfMGen, "Автоматичні дизель-генератори Cummins", 8.5, "Regular", cWhite, 16, 28);

  // Mobile Footer & Bottom Nav
  const wfMFoot = figma.createFrame(); wfMFoot.resize(440, 46); wfMFoot.x = 20; wfMFoot.y = 724; wfMFoot.cornerRadius = 6; wfMFoot.fills = [{ type: "SOLID", color: cDark }]; wfMob.appendChild(wfMFoot);
  helperText(wfMFoot, "© 2026 ChargeUA · Гаряча лінія: 0 800 300 400", 8.5, "Regular", cWhite, 16, 16);
  const wfMNav = figma.createFrame(); wfMNav.resize(440, 36); wfMNav.x = 20; wfMNav.y = 780; wfMNav.cornerRadius = 6; wfMNav.fills = [{ type: "SOLID", color: cPrimary }]; wfMob.appendChild(wfMNav);
  helperText(wfMNav, "🗺 Карта            🧮 Калькулятор            ⚡ Хаби", 9, "Bold", cWhite, 70, 11);

  // FRAME 04: DESIGN ASSETS"""

code = old_wf_pattern.sub(new_wf_block, code)

# -----------------------------------------------------------------------------
# 4. UPDATE 04.1_DESIGN_SYSTEM: INPUTS & CONTROLS (NO OFFERS, NO PROMOCODES)
# -----------------------------------------------------------------------------
old_inp_pattern = re.compile(
    r'  // Left Card: TextField States.*?// Right Card: Controls & Selection',
    re.DOTALL
)

new_inp_block = """  // Left Card: TextField States (width 630, height 380)
  const fInpCard = figma.createFrame();
  fInpCard.resize(630, 380);
  fInpCard.x = 60; fInpCard.y = 400;
  fInpCard.cornerRadius = 14;
  fInpCard.fills = [{ type: "SOLID", color: cWhite }];
  fInpCard.strokes = [{ type: "SOLID", color: cBorder }];
  fDesignSystem.appendChild(fInpCard);

  helperText(fInpCard, "СТАНИ ПОЛІВ ПОШУКУ ТА ФІЛЬТРАЦІЇ (INPUT STATES)", 12, "Bold", cPrimary, 20, 16);

  // Field 1: Search in Focus
  helperText(fInpCard, "Пошук станції за адресою / містом", 12, "Bold", cDark, 20, 44);
  const bFocBadge = figma.createFrame(); bFocBadge.resize(110, 18); bFocBadge.x = 500; bFocBadge.y = 44; bFocBadge.cornerRadius = 4; bFocBadge.fills = [{ type: "SOLID", color: { r: 239/255, g: 246/255, b: 255/255 } }]; fInpCard.appendChild(bFocBadge);
  helperText(bFocBadge, "Focus (Введення)", 10, "Bold", cPrimary, 8, 3);
  const fInpFoc = figma.createFrame(); fInpFoc.resize(590, 38); fInpFoc.x = 20; fInpFoc.y = 66; fInpFoc.cornerRadius = 8; fInpFoc.fills = [{ type: "SOLID", color: cWhite }]; fInpFoc.strokes = [{ type: "SOLID", color: cPrimary }]; fInpCard.appendChild(fInpFoc);
  helperText(fInpFoc, "м. Львів, вул. Стрийська, 199|", 13, "Bold", cDark, 14, 10);
  helperText(fInpCard, "Активне поле пошуку: синя акцентна рамка (#005EC9) та фокусне кільце", 11, "Regular", cMuted, 20, 108);

  // Field 2: Capacity with Error
  helperText(fInpCard, "Мінімальна потужність хабу (кВт)", 12, "Bold", cDark, 20, 130);
  const bErrBadge = figma.createFrame(); bErrBadge.resize(95, 18); bErrBadge.x = 515; bErrBadge.y = 130; bErrBadge.cornerRadius = 4; bErrBadge.fills = [{ type: "SOLID", color: { r: 254/255, g: 242/255, b: 242/255 } }]; fInpCard.appendChild(bErrBadge);
  helperText(bErrBadge, "Error (Помилка)", 10, "Bold", { r: 220/255, g: 38/255, b: 38/255 }, 8, 3);
  const fInpErr = figma.createFrame(); fInpErr.resize(590, 38); fInpErr.x = 20; fInpErr.y = 152; fInpErr.cornerRadius = 8; fInpErr.fills = [{ type: "SOLID", color: { r: 254/255, g: 242/255, b: 242/255 } }]; fInpErr.strokes = [{ type: "SOLID", color: { r: 239/255, g: 68/255, b: 68/255 } }]; fInpCard.appendChild(fInpErr);
  helperText(fInpErr, "0 кВт", 13, "Bold", { r: 220/255, g: 38/255, b: 38/255 }, 14, 10);
  helperText(fInpCard, "⚠ Помилка! Вкажіть потужність від 22 до 160 кВт для фільтрації на карті", 11, "Semi Bold", { r: 220/255, g: 38/255, b: 38/255 }, 20, 194);

  // Field 3: Car Model Default
  helperText(fInpCard, "Модель електромобіля (для автопідбору)", 12, "Bold", cDark, 20, 216);
  const bDefBadge = figma.createFrame(); bDefBadge.resize(130, 18); bDefBadge.x = 480; bDefBadge.y = 216; bDefBadge.cornerRadius = 4; bDefBadge.fills = [{ type: "SOLID", color: cBgSurface }]; fInpCard.appendChild(bDefBadge);
  helperText(bDefBadge, "Default (Плейсхолдер)", 10, "Bold", cMuted, 8, 3);
  const fInpDef = figma.createFrame(); fInpDef.resize(590, 38); fInpDef.x = 20; fInpDef.y = 238; fInpDef.cornerRadius = 8; fInpDef.fills = [{ type: "SOLID", color: cWhite }]; fInpDef.strokes = [{ type: "SOLID", color: cBorder }]; fInpCard.appendChild(fInpDef);
  helperText(fInpDef, "Наприклад: Tesla Model 3, VW ID.4...", 13, "Regular", cMuted, 14, 10);
  helperText(fInpCard, "Стан за замовчуванням: нейтральна рамка #CBD5E1, автоматичний підбір роз'єму", 11, "Regular", cMuted, 20, 280);

  // Field 4: Region Disabled
  helperText(fInpCard, "Фільтр мереж за межами України", 12, "Bold", cDark, 20, 302);
  const bDisBadge = figma.createFrame(); bDisBadge.resize(120, 18); bDisBadge.x = 490; bDisBadge.y = 302; bDisBadge.cornerRadius = 4; bDisBadge.fills = [{ type: "SOLID", color: cBgSurface }]; bDisBadge.strokes = [{ type: "SOLID", color: cBorder }]; fInpCard.appendChild(bDisBadge);
  helperText(bDisBadge, "Disabled (Заблоковано)", 10, "Bold", cMuted, 8, 3);
  const fInpDis = figma.createFrame(); fInpDis.resize(590, 38); fInpDis.x = 20; fInpDis.y = 324; fInpDis.cornerRadius = 8; fInpDis.fills = [{ type: "SOLID", color: cBgSurface }]; fInpDis.strokes = [{ type: "SOLID", color: cBorder }]; fInpCard.appendChild(fInpDis);
  helperText(fInpDis, "Доступно лише в межах України", 13, "Regular", cMuted, 14, 10);

  // Right Card: Controls & Selection"""

code = old_inp_pattern.sub(new_inp_block, code)

# Update right controls card in Design System (checkboxes/radios)
old_ctrl_cb = 'helperText(cb1, "Погоджуюсь з умовами оферти (Touch target 48 px)", 12, "Semi Bold", cDark, 42, 14);'
new_ctrl_cb = 'helperText(cb1, "Тільки вільні конектори прямо зараз (Touch target 48 px)", 12, "Semi Bold", cDark, 42, 14);'
code = code.replace(old_ctrl_cb, new_ctrl_cb)

# -----------------------------------------------------------------------------
# 5. FIX 05_DESKTOP HERO VERTICAL SPACING (ELIMINATE TEXT OVERLAP)
# -----------------------------------------------------------------------------
old_dhero_text = """  // Left-aligned Hero Content
  helperText(dHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ", 12, "Bold", cPrimary, 60, 48);
  helperText(dHero, "Швидка та надійна зарядка\\nелектромобілів по всій Україні", 42, "Bold", cDark, 60, 80, 640);
  helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 60, 205, 600);

  // Hero Actions
  const dHeroBtn1 = figma.createFrame();
  dHeroBtn1.resize(230, 48);
  dHeroBtn1.x = 60; dHeroBtn1.y = 285;
  dHeroBtn1.cornerRadius = 8;
  dHeroBtn1.fills = [{ type: "SOLID", color: cPrimary }];
  dHero.appendChild(dHeroBtn1);
  helperText(dHeroBtn1, "Розрахувати зарядку →", 14, "Bold", cWhite, 32, 15);

  const dHeroBtn2 = figma.createFrame();
  dHeroBtn2.resize(180, 48);
  dHeroBtn2.x = 305; dHeroBtn2.y = 285;
  dHeroBtn2.cornerRadius = 8;
  dHeroBtn2.fills = [{ type: "SOLID", color: cWhite }];
  dHeroBtn2.strokes = [{ type: "SOLID", color: cBorder }];
  dHero.appendChild(dHeroBtn2);
  helperText(dHeroBtn2, "Знайти на карті", 14, "Semi Bold", cDark, 30, 15);

  // Chips
  const heroChips = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 З генератором"];
  heroChips.forEach((ch, idx) => {
    const chBox = figma.createFrame();
    chBox.resize(130, 32);
    chBox.x = 60 + idx * 142; chBox.y = 355;"""

new_dhero_text = """  // Left-aligned Hero Content
  helperText(dHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ", 12, "Bold", cPrimary, 60, 44);
  helperText(dHero, "Швидка та надійна зарядка\\nелектромобілів по всій Україні", 38, "Bold", cDark, 60, 74, 640);
  helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\\nта подорожуйте без хвилювань навіть під час блекаутів.", 15, "Regular", cMuted, 60, 195, 600);

  // Hero Actions
  const dHeroBtn1 = figma.createFrame();
  dHeroBtn1.resize(230, 48);
  dHeroBtn1.x = 60; dHeroBtn1.y = 270;
  dHeroBtn1.cornerRadius = 8;
  dHeroBtn1.fills = [{ type: "SOLID", color: cPrimary }];
  dHero.appendChild(dHeroBtn1);
  helperText(dHeroBtn1, "Розрахувати зарядку →", 14, "Bold", cWhite, 32, 15);

  const dHeroBtn2 = figma.createFrame();
  dHeroBtn2.resize(180, 48);
  dHeroBtn2.x = 305; dHeroBtn2.y = 270;
  dHeroBtn2.cornerRadius = 8;
  dHeroBtn2.fills = [{ type: "SOLID", color: cWhite }];
  dHeroBtn2.strokes = [{ type: "SOLID", color: cBorder }];
  dHero.appendChild(dHeroBtn2);
  helperText(dHeroBtn2, "Знайти на карті", 14, "Semi Bold", cDark, 30, 15);

  // Chips
  const heroChips = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 З генератором"];
  heroChips.forEach((ch, idx) => {
    const chBox = figma.createFrame();
    chBox.resize(130, 32);
    chBox.x = 60 + idx * 142; chBox.y = 338;"""

code = code.replace(old_dhero_text, new_dhero_text)

# Also update dNav items so we can link them to sections!
old_dnav_str = """  const dNav = figma.createFrame();
  dNav.resize(720, 30);
  dNav.x = 320; dNav.y = 25;
  dNav.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }];
  dHeader.appendChild(dNav);
  helperText(dNav, "Головна     Калькулятор     Карта станцій     Популярні хаби     Інструкція     Відгуки", 14, "Semi Bold", cMuted, 10, 5);"""

new_dnav_str = """  const dNav = figma.createFrame();
  dNav.resize(760, 30);
  dNav.x = 300; dNav.y = 25;
  dNav.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }];
  dHeader.appendChild(dNav);

  const dNavHome = figma.createFrame(); dNavHome.resize(80, 28); dNavHome.x = 0; dNavHome.y = 0; dNavHome.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavHome);
  helperText(dNavHome, "Головна", 14, "Bold", cPrimary, 5, 5);

  const dNavCalc = figma.createFrame(); dNavCalc.resize(105, 28); dNavCalc.x = 85; dNavCalc.y = 0; dNavCalc.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavCalc);
  helperText(dNavCalc, "Калькулятор", 14, "Medium", cMuted, 5, 5);

  const dNavMap = figma.createFrame(); dNavMap.resize(115, 28); dNavMap.x = 195; dNavMap.y = 0; dNavMap.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavMap);
  helperText(dNavMap, "Карта станцій", 14, "Medium", cMuted, 5, 5);

  const dNavHubs = figma.createFrame(); dNavHubs.resize(125, 28); dNavHubs.x = 315; dNavHubs.y = 0; dNavHubs.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavHubs);
  helperText(dNavHubs, "Популярні хаби", 14, "Medium", cMuted, 5, 5);

  const dNavSteps = figma.createFrame(); dNavSteps.resize(95, 28); dNavSteps.x = 445; dNavSteps.y = 0; dNavSteps.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavSteps);
  helperText(dNavSteps, "Інструкція", 14, "Medium", cMuted, 5, 5);

  const dNavRev = figma.createFrame(); dNavRev.resize(80, 28); dNavRev.x = 545; dNavRev.y = 0; dNavRev.fills = [{ type: "SOLID", color: cWhite, opacity: 0.01 }]; dNav.appendChild(dNavRev);
  helperText(dNavRev, "Відгуки", 14, "Medium", cMuted, 5, 5);"""

code = code.replace(old_dnav_str, new_dnav_str)

# -----------------------------------------------------------------------------
# 6. ENHANCE PROTOTYPE CONNECTIONS (SCROLL_TO ANCHORS, BUTTON ACTIONS)
# -----------------------------------------------------------------------------
old_proto_block = """  // 1. Desktop Interactions
  await linkNodes(dHeadCta, fCatalog);
  await linkNodes(dHeroBtn2, fCatalog);
  for (const btn of desktopStationBtns) {
    await linkNodes(btn, fDetails);
  }

  // 2. Tablet Interactions
  await linkNodes(tHeadCta, fCatalog);
  await linkNodes(tBtn2, fCatalog);
  await linkNodes(tCalcBtn, fCatalog);
  for (const btn of tabletStationBtns) {
    await linkNodes(btn, fDetails);
  }

  // 3. Mobile Interactions (Burger -> Drawer Overlay, Map -> Catalog, Cards -> Details)
  await linkOverlay(mBurgerBtn, fDrawerOverlay);
  await linkNodes(mBtnMap, fCatalog);
  await linkNodes(mCalcAct, fCatalog);
  for (const btn of mobileStationBtns) {
    await linkNodes(btn, fDetails);
  }
  await linkNodes(mBottomNavHome, fMobile);
  await linkNodes(mBottomNavMap, fCatalog);"""

new_proto_block = """  // 1. Desktop Interactions (Scroll to anchors + Navigate)
  await linkScroll(dHeroBtn1, dCalc);
  await linkScroll(dHeroBtn2, dMapSec);
  await linkNodes(dHeadCta, fCatalog);

  // Desktop Header Nav Scroll Links
  await linkScroll(dNavHome, dHero);
  await linkScroll(dNavCalc, dCalc);
  await linkScroll(dNavMap, dMapSec);
  await linkScroll(dNavHubs, dHubsSec);
  await linkScroll(dNavSteps, dStepsSec);
  await linkScroll(dNavRev, dRevSec);

  for (const btn of desktopStationBtns) {
    await linkNodes(btn, fDetails);
  }

  // 2. Tablet Interactions (Scroll to anchors + Navigate)
  await linkScroll(tBtn1, tCalc);
  await linkScroll(tBtn2, tMapSec);
  await linkScroll(tCalcBtn, tMapSec);
  await linkNodes(tHeadCta, fCatalog);
  for (const btn of tabletStationBtns) {
    await linkNodes(btn, fDetails);
  }

  // 3. Mobile Interactions (Burger -> Drawer Overlay, Anchors, Cards -> Details)
  await linkOverlay(mBurgerBtn, fDrawerOverlay);
  await linkScroll(mBtnMap, mMapSec);
  await linkScroll(mCalcAct, mMapSec);
  for (const btn of mobileStationBtns) {
    await linkNodes(btn, fDetails);
  }
  await linkScroll(mBottomNavHome, mHero);
  await linkScroll(mBottomNavMap, mMapSec);
  await linkScroll(mBottomNavCalc, mCalc);"""

code = code.replace(old_proto_block, new_proto_block)

# In drawer overlay links:
old_drawer_links = """  await linkNodes(drawerLinkHome, fMobile);
  await linkNodes(drawerLinkCalc, fMobile);
  await linkNodes(drawerLinkMap, fCatalog);
  await linkNodes(drawerLinkStations, fCatalog);
  await linkNodes(drawerLinkSteps, fMobile);
  await linkNodes(drawerLinkReviews, fMobile);"""

new_drawer_links = """  await linkScroll(drawerLinkHome, mHero);
  await linkScroll(drawerLinkCalc, mCalc);
  await linkScroll(drawerLinkMap, mMapSec);
  await linkScroll(drawerLinkStations, mHubsSec);
  await linkScroll(drawerLinkSteps, mStepsSec);
  await linkScroll(drawerLinkReviews, mRevSec);"""

code = code.replace(old_drawer_links, new_drawer_links)

with open(SRC_FILE, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Successfully updated {SRC_FILE}!")
