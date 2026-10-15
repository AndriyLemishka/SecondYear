# -*- coding: utf-8 -*-
import sys, re

with open("lab4/08_scratch/generate_final_figma_plugin.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update image resolutions and add map_lviv
old_imgs = '''print("Processing Image assets...")
b64_hero = get_b64_jpeg("hero_bg.jpg", 640, 360, 75)
b64_hub_kyiv = get_b64_jpeg("ai_hub_kyiv.jpg", 420, 240, 75)
b64_hub_lviv = get_b64_jpeg("ai_hub_lviv.jpg", 420, 240, 75)
b64_hub_obolon = get_b64_jpeg("ai_hub_obolon.jpg", 420, 240, 75)
b64_hub_odesa = get_b64_jpeg("ai_hub_odesa.jpg", 420, 240, 75)
b64_hub_dnipro = get_b64_jpeg("ai_hub_dnipro.jpg", 420, 240, 75)
b64_hub_zhytomyr = get_b64_jpeg("ai_hub_zhytomyr.jpg", 420, 240, 75)
b64_banner_ai = get_b64_jpeg("ai_promo_banner.jpg", 420, 240, 75)
b64_video_tutorial = get_b64_jpeg("ai_video_tutorial.jpg", 420, 240, 75)
b64_generator = get_b64_jpeg("ai_generator_blackout.jpg", 420, 260, 75)
b64_cable = get_b64_jpeg("ai_step_cable.jpg", 360, 220, 75)
b64_video = get_b64_jpeg("video_frame_30.jpg", 960, 540, 85)
b64_banner = get_b64_jpeg("fig3_banner.png", 400, 200, 75)
b64_av1 = get_b64_jpeg("ai_avatar_oleksiy.jpg", 120, 120, 75)
b64_av2 = get_b64_jpeg("ai_avatar_olena.jpg", 120, 120, 75)
b64_av3 = get_b64_jpeg("ai_avatar_sergiy.jpg", 120, 120, 75)'''

new_imgs = '''print("Processing Image assets (High Definition 1280x720 / q85)...")
b64_hero = get_b64_jpeg("hero_bg.jpg", 1280, 720, 85)
b64_hub_kyiv = get_b64_jpeg("ai_hub_kyiv.jpg", 1280, 720, 85)
b64_hub_lviv = get_b64_jpeg("ai_hub_lviv.jpg", 1280, 720, 85)
b64_hub_obolon = get_b64_jpeg("ai_hub_obolon.jpg", 1280, 720, 85)
b64_hub_odesa = get_b64_jpeg("ai_hub_odesa.jpg", 1280, 720, 85)
b64_hub_dnipro = get_b64_jpeg("ai_hub_dnipro.jpg", 1280, 720, 85)
b64_hub_zhytomyr = get_b64_jpeg("ai_hub_zhytomyr.jpg", 1280, 720, 85)
b64_banner_ai = get_b64_jpeg("ai_promo_banner.jpg", 1280, 720, 85)
b64_video_tutorial = get_b64_jpeg("ai_video_tutorial.jpg", 1280, 720, 85)
b64_generator = get_b64_jpeg("ai_generator_blackout.jpg", 1280, 720, 85)
b64_cable = get_b64_jpeg("ai_step_cable.jpg", 1280, 720, 85)
b64_video = get_b64_jpeg("video_frame_30.jpg", 1280, 720, 85)
b64_banner = get_b64_jpeg("fig3_banner.png", 740, 360, 85)
b64_av1 = get_b64_jpeg("ai_avatar_oleksiy.jpg", 400, 400, 85)
b64_av2 = get_b64_jpeg("ai_avatar_olena.jpg", 400, 400, 85)
b64_av3 = get_b64_jpeg("ai_avatar_sergiy.jpg", 400, 400, 85)
b64_map_lviv = get_b64_jpeg("map_lviv.jpg", 1280, 720, 85)'''

assert old_imgs in content, "old_imgs not found"
content = content.replace(old_imgs, new_imgs, 1)

# 2. Update ASSETS_B64
old_assets = '''  av1: "{b64_av1}",
  av2: "{b64_av2}",
  av3: "{b64_av3}"
}};'''

new_assets = '''  av1: "{b64_av1}",
  av2: "{b64_av2}",
  av3: "{b64_av3}",
  map_lviv: "{b64_map_lviv}"
}};'''

assert old_assets in content, "old_assets not found"
content = content.replace(old_assets, new_assets, 1)

# 3. Replace Wireframes section
old_wf_marker = '  // FRAME 03: WIREFRAMES'
old_wf_end = '  // FRAME 04.0: BRAND ASSETS'
pos_wf_start = content.find(old_wf_marker)
pos_wf_end = content.find(old_wf_end)
assert pos_wf_start != -1 and pos_wf_end != -1, "Wireframes boundaries not found"

new_wireframes = '''  // FRAME 03: WIREFRAMES (Low-Fidelity Architecture Matching Report Fig 5 & 6)
  const fWireframes = figma.createFrame();
  fWireframes.name = "03_Wireframes";
  fWireframes.resize(1440, 1050);
  fWireframes.x = 4800; fWireframes.y = 0;
  fWireframes.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fWireframes, "03 Каркаси сторінок (Wireframes)", 28, "Bold", cDark, 60, 40);
  helperText(fWireframes, "Низькодеталізовані макети ключових екранів: Головна сторінка Desktop (1440px) та Mobile (390px)", 15, "Regular", cMuted, 60, 80);

  // Desktop Wireframe Box (Left side: 760 x 880)
  const wfDesk = figma.createFrame();
  wfDesk.resize(760, 880);
  wfDesk.x = 60; wfDesk.y = 130;
  wfDesk.cornerRadius = 12;
  wfDesk.fills = [{{ type: "SOLID", color: cWhite }}];
  wfDesk.strokes = [{{ type: "SOLID", color: cBorder }}];
  fWireframes.appendChild(wfDesk);

  // Header wireframe
  const wfDHead = figma.createFrame(); wfDHead.resize(712, 40); wfDHead.x = 24; wfDHead.y = 20; wfDHead.cornerRadius = 6; wfDHead.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDHead.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDHead);
  helperText(wfDHead, "⚡ [LOGO] ChargeUA", 11, "Bold", cDark, 14, 12);
  helperText(wfDHead, "Головна   |   Калькулятор   |   Мапа   |   Тарифи   |   Для бізнесу", 10, "Medium", cMuted, 160, 13);
  const wfDHBtn = figma.createFrame(); wfDHBtn.resize(80, 26); wfDHBtn.x = 618; wfDHBtn.y = 7; wfDHBtn.cornerRadius = 4; wfDHBtn.fills = [{{ type: "SOLID", color: cDark }}]; wfDHead.appendChild(wfDHBtn);
  helperText(wfDHBtn, "[Знайти хаб]", 9, "Bold", cWhite, 12, 7);

  // Hero section wireframe
  const wfDHero = figma.createFrame(); wfDHero.resize(712, 130); wfDHero.x = 24; wfDHero.y = 70; wfDHero.cornerRadius = 8; wfDHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDHero.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDHero);
  helperText(wfDHero, "[HERO SECTION · Desktop 1440px]", 10, "Bold", cMuted, 16, 12);
  const wfDHl = figma.createFrame(); wfDHl.resize(280, 16); wfDHl.x = 16; wfDHl.y = 34; wfDHl.cornerRadius = 3; wfDHl.fills = [{{ type: "SOLID", color: {{ r: 148/255, g: 163/255, b: 184/255 }} }}]; wfDHero.appendChild(wfDHl);
  const wfDSub = figma.createFrame(); wfDSub.resize(320, 10); wfDSub.x = 16; wfDSub.y = 58; wfDSub.cornerRadius = 2; wfDSub.fills = [{{ type: "SOLID", color: {{ r: 203/255, g: 213/255, b: 225/255 }} }}]; wfDHero.appendChild(wfDSub);
  const wfDSub2 = figma.createFrame(); wfDSub2.resize(220, 10); wfDSub2.x = 16; wfDSub2.y = 74; wfDSub2.cornerRadius = 2; wfDSub2.fills = [{{ type: "SOLID", color: {{ r: 203/255, g: 213/255, b: 225/255 }} }}]; wfDHero.appendChild(wfDSub2);
  const wfDB1 = figma.createFrame(); wfDB1.resize(100, 28); wfDB1.x = 16; wfDB1.y = 92; wfDB1.cornerRadius = 4; wfDB1.fills = [{{ type: "SOLID", color: cPrimary }}]; wfDHero.appendChild(wfDB1);
  helperText(wfDB1, "Знайти станцію", 9, "Bold", cWhite, 16, 8);
  const wfDB2 = figma.createFrame(); wfDB2.resize(90, 28); wfDB2.x = 124; wfDB2.y = 92; wfDB2.cornerRadius = 4; wfDB2.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDB2.fills = [{{ type: "SOLID", color: cWhite }}]; wfDHero.appendChild(wfDB2);
  helperText(wfDB2, "Калькулятор", 9, "Bold", cDark, 14, 8);
  const wfDHImg = figma.createFrame(); wfDHImg.resize(250, 105); wfDHImg.x = 445; wfDHImg.y = 12; wfDHImg.cornerRadius = 6; wfDHImg.fills = [{{ type: "SOLID", color: cWhite }}]; wfDHImg.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDHero.appendChild(wfDHImg);
  helperText(wfDHImg, "🖼 [Візуальний блок: Авто + Хаб]", 10, "Semi Bold", cMuted, 36, 44);

  // 3 Benefits Strip wireframe
  const wfDBen = figma.createFrame(); wfDBen.resize(712, 60); wfDBen.x = 24; wfDBen.y = 210; wfDBen.cornerRadius = 8; wfDBen.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDBen.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDBen);
  const bTitles = ["[🧮 Розрахунок витрат]", "[🗺 Live-карта 480+ хабів]", "[⚡ 100% захист від блекаутів]"];
  bTitles.forEach((bt, bIdx) => {{
    const bCard = figma.createFrame(); bCard.resize(220, 44); bCard.x = 12 + bIdx * 232; bCard.y = 8; bCard.cornerRadius = 6; bCard.fills = [{{ type: "SOLID", color: cWhite }}]; bCard.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDBen.appendChild(bCard);
    helperText(bCard, bt, 10, "Bold", cDark, 20, 15);
  }});

  // Calculator wireframe
  const wfDCalc = figma.createFrame(); wfDCalc.resize(712, 100); wfDCalc.x = 24; wfDCalc.y = 280; wfDCalc.cornerRadius = 8; wfDCalc.fills = [{{ type: "SOLID", color: cWhite }}]; wfDCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDCalc);
  helperText(wfDCalc, "[SECTION · Інтерактивний калькулятор зарядки]", 11, "Bold", cDark, 16, 12);
  helperText(wfDCalc, "Авто: [Tesla Model 3]   [VW ID.4]   [Nissan Leaf]       |       Батарея: [ 20% ======●====== 80% ]", 10, "Regular", cMuted, 16, 38);
  const wfDCalcRes = figma.createFrame(); wfDCalcRes.resize(680, 34); wfDCalcRes.x = 16; wfDCalcRes.y = 58; wfDCalcRes.cornerRadius = 6; wfDCalcRes.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDCalc.appendChild(wfDCalcRes);
  helperText(wfDCalcRes, "📊 Орієнтовна вартість: 652.50 ₴ · Час зарядки: ~28 хв (CCS2 Ultra) · Заощадження vs бензин: ~1 450 ₴", 10, "Bold", cDark, 16, 10);

  // Stations Grid wireframe (2 cards)
  const wfDStat = figma.createFrame(); wfDStat.resize(712, 110); wfDStat.x = 24; wfDStat.y = 390; wfDStat.cornerRadius = 8; wfDStat.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDStat.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDStat);
  helperText(wfDStat, "[SECTION · Популярні зарядні хаби]", 11, "Bold", cDark, 16, 10);
  const stWireData = [
    {{ title: "Хаб «Київ-Поділ» · 120 кВт CCS2", addr: "вул. Сагайдачного, 12 · 3/4 вільно", gen: "🔋 Генератор ON" }},
    {{ title: "Хаб «Львів-Арена» · 160 кВт CCS2", addr: "вул. Стрийська, 199 · 5/6 вільно", gen: "🔋 Генератор ON" }}
  ];
  stWireData.forEach((st, sIdx) => {{
    const sBox = figma.createFrame(); sBox.resize(336, 68); sBox.x = 16 + sIdx * 348; sBox.y = 32; sBox.cornerRadius = 6; sBox.fills = [{{ type: "SOLID", color: cWhite }}]; sBox.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDStat.appendChild(sBox);
    helperText(sBox, st.title, 10, "Bold", cDark, 12, 10);
    helperText(sBox, st.addr, 9, "Regular", cMuted, 12, 28);
    helperText(sBox, st.gen, 9, "Bold", cSuccess, 12, 46);
    const sBtn = figma.createFrame(); sBtn.resize(110, 24); sBtn.x = 214; sBtn.y = 36; sBtn.cornerRadius = 4; sBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; sBox.appendChild(sBtn);
    helperText(sBtn, "Маршрут CCS2", 9, "Bold", cWhite, 16, 6);
  }});

  // Blackout Generator Section wireframe
  const wfDGen = figma.createFrame(); wfDGen.resize(712, 90); wfDGen.x = 24; wfDGen.y = 510; wfDGen.cornerRadius = 8; wfDGen.fills = [{{ type: "SOLID", color: cDark }}]; wfDesk.appendChild(wfDGen);
  helperText(wfDGen, "⚡ 100% РЕЗЕРВНЕ ЖИВЛЕННЯ · 180+ СТАНЦІЙ З ГЕНЕРАТОРАМИ", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 16, 12);
  helperText(wfDGen, "Автономні промислові генератори Cummins 160 кВт з автоматичним вводом резерву (АВР 15 сек).", 10, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 16, 34);
  const wfDGenBox = figma.createFrame(); wfDGenBox.resize(680, 28); wfDGenBox.x = 16; wfDGenBox.y = 54; wfDGenBox.cornerRadius = 4; wfDGenBox.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.1 }}]; wfDGen.appendChild(wfDGenBox);
  helperText(wfDGenBox, "Паливний резервуар: 48 годин безперервної роботи · Онлайн-моніторинг телеметрії через супутниковий Starlink", 9, "Medium", cWhite, 12, 7);

  // Reviews & Steps wireframe
  const wfDRev = figma.createFrame(); wfDRev.resize(712, 90); wfDRev.x = 24; wfDRev.y = 610; wfDRev.cornerRadius = 8; wfDRev.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDRev.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDRev);
  helperText(wfDRev, "[SECTION · Як зарядитися за 3 кроки & Відгуки водіїв]", 11, "Bold", cDark, 16, 10);
  const rBoxes = [
    "[Крок 1: Оберіть хаб на мапі]",
    "[Крок 2: Підключіть CCS2 / Type 2]",
    "[Крок 3: Оплата карткою / Apple Pay]",
    "★★★★★ «Під час блекауту дуже виручило!»"
  ];
  rBoxes.forEach((rb, rIdx) => {{
    const rF = figma.createFrame(); rF.resize(162, 48); rF.x = 16 + rIdx * 172; rF.y = 32; rF.cornerRadius = 6; rF.fills = [{{ type: "SOLID", color: cWhite }}]; rF.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDRev.appendChild(rF);
    helperText(rF, rb, 8.5, "Semi Bold", cMuted, 8, 16);
  }});

  // Footer wireframe
  const wfDFoot = figma.createFrame(); wfDFoot.resize(712, 60); wfDFoot.x = 24; wfDFoot.y = 710; wfDFoot.cornerRadius = 8; wfDFoot.fills = [{{ type: "SOLID", color: cDark }}]; wfDesk.appendChild(wfDFoot);
  helperText(wfDFoot, "⚡ ChargeUA — Національна мережа швидкісних електрозарядних комплексів", 10, "Bold", cWhite, 16, 14);
  helperText(wfDFoot, "© 2026 ChargeUA. Усі права захищено. Створено в рамках ЛР4 студентом Андрієм Лемішкою (ПП-24)", 9, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 16, 36);

  // Mobile Wireframe Box (Right side: 380 x 880)
  const wfMob = figma.createFrame();
  wfMob.resize(380, 880);
  wfMob.x = 880; wfMob.y = 130;
  wfMob.cornerRadius = 12;
  wfMob.fills = [{{ type: "SOLID", color: cWhite }}];
  wfMob.strokes = [{{ type: "SOLID", color: cBorder }}];
  fWireframes.appendChild(wfMob);

  // Mobile Header
  const wfMHead = figma.createFrame(); wfMHead.resize(340, 38); wfMHead.x = 20; wfMHead.y = 20; wfMHead.cornerRadius = 6; wfMHead.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMHead.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMHead);
  helperText(wfMHead, "⚡ ChargeUA", 11, "Bold", cPrimary, 12, 11);
  helperText(wfMHead, "[☰ Меню]", 11, "Bold", cDark, 275, 11);

  // Mobile Hero
  const wfMHero = figma.createFrame(); wfMHero.resize(340, 115); wfMHero.x = 20; wfMHero.y = 66; wfMHero.cornerRadius = 6; wfMHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMHero.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMHero);
  helperText(wfMHero, "[HERO · Mobile 390px]", 9.5, "Bold", cMuted, 12, 8);
  const wfMHl = figma.createFrame(); wfMHl.resize(190, 14); wfMHl.x = 12; wfMHl.y = 28; wfMHl.cornerRadius = 3; wfMHl.fills = [{{ type: "SOLID", color: {{ r: 148/255, g: 163/255, b: 184/255 }} }}]; wfMHero.appendChild(wfMHl);
  const wfMSub = figma.createFrame(); wfMSub.resize(260, 8); wfMSub.x = 12; wfMSub.y = 48; wfMSub.cornerRadius = 2; wfMSub.fills = [{{ type: "SOLID", color: {{ r: 203/255, g: 213/255, b: 225/255 }} }}]; wfMHero.appendChild(wfMSub);
  const wfMB1 = figma.createFrame(); wfMB1.resize(316, 26); wfMB1.x = 12; wfMB1.y = 66; wfMB1.cornerRadius = 4; wfMB1.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMHero.appendChild(wfMB1);
  helperText(wfMB1, "Знайти найближчу станцію (GPS)", 9, "Bold", cWhite, 80, 7);

  // Mobile Benefits
  const wfMBen = figma.createFrame(); wfMBen.resize(340, 70); wfMBen.x = 20; wfMBen.y = 189; wfMBen.cornerRadius = 6; wfMBen.fills = [{{ type: "SOLID", color: cWhite }}]; wfMBen.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMBen);
  helperText(wfMBen, "• Швидкий розрахунок витрат (автопресети)", 9, "Regular", cDark, 12, 10);
  helperText(wfMBen, "• Live-карта: 480+ хабів із живою телеметрією", 9, "Regular", cDark, 12, 28);
  helperText(wfMBen, "• 100% захист від блекаутів завдяки генераторам", 9, "Regular", cDark, 12, 46);

  // Mobile Calculator
  const wfMCalc = figma.createFrame(); wfMCalc.resize(340, 85); wfMCalc.x = 20; wfMCalc.y = 267; wfMCalc.cornerRadius = 6; wfMCalc.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMCalc);
  helperText(wfMCalc, "[Мобільний калькулятор]", 10, "Bold", cDark, 12, 8);
  helperText(wfMCalc, "Модель: Tesla Model 3 · Батарея 20% → 80%", 9, "Medium", cMuted, 12, 28);
  const wfMCRes = figma.createFrame(); wfMCRes.resize(316, 26); wfMCRes.x = 12; wfMCRes.y = 48; wfMCRes.cornerRadius = 4; wfMCRes.fills = [{{ type: "SOLID", color: cWhite }}]; wfMCRes.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMCalc.appendChild(wfMCRes);
  helperText(wfMCRes, "652.50 ₴ · ~28 хв (CCS2)", 9.5, "Bold", cDark, 95, 6);

  // Mobile Station Card
  const wfMStat = figma.createFrame(); wfMStat.resize(340, 95); wfMStat.x = 20; wfMStat.y = 360; wfMStat.cornerRadius = 6; wfMStat.fills = [{{ type: "SOLID", color: cWhite }}]; wfMStat.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMStat);
  helperText(wfMStat, "Хаб «Київ-Поділ» · 120 кВт CCS2", 10, "Bold", cDark, 12, 10);
  helperText(wfMStat, "вул. Сагайдачного, 12 · 🔋 Генератор ON", 9, "Regular", cMuted, 12, 28);
  const wfMSb = figma.createFrame(); wfMSb.resize(316, 28); wfMSb.x = 12; wfMSb.y = 52; wfMSb.cornerRadius = 4; wfMSb.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMStat.appendChild(wfMSb);
  helperText(wfMSb, "Прокласти маршрут CCS2", 9.5, "Bold", cWhite, 95, 7);

  // Mobile Generator & Steps
  const wfMGen = figma.createFrame(); wfMGen.resize(340, 75); wfMGen.x = 20; wfMGen.y = 463; wfMGen.cornerRadius = 6; wfMGen.fills = [{{ type: "SOLID", color: cDark }}]; wfMob.appendChild(wfMGen);
  helperText(wfMGen, "⚡ Резервне живлення 160 кВт", 10, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 12, 10);
  helperText(wfMGen, "180+ станцій працюють під час аварійних відключень.", 9, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 12, 28);
  helperText(wfMGen, "Автоматичні генератори Cummins гарантують зарядку.", 8.5, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 12, 46);

  // Mobile Review
  const wfMRev = figma.createFrame(); wfMRev.resize(340, 60); wfMRev.x = 20; wfMRev.y = 546; wfMRev.cornerRadius = 6; wfMRev.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMRev.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMRev);
  helperText(wfMRev, "★★★★★ «Під час блекауту виручило!»", 9, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 12, 12);
  helperText(wfMRev, "Олексій К. · Tesla Model Y · 15 хв тому", 8.5, "Regular", cMuted, 12, 32);

  // Mobile Footer & Sticky Bottom Nav
  const wfMFoot = figma.createFrame(); wfMFoot.resize(340, 60); wfMFoot.x = 20; wfMFoot.y = 614; wfMFoot.cornerRadius = 6; wfMFoot.fills = [{{ type: "SOLID", color: cDark }}]; wfMob.appendChild(wfMFoot);
  helperText(wfMFoot, "© 2026 ChargeUA · Мобільна версія", 9, "Regular", cWhite, 12, 14);
  helperText(wfMFoot, "Гаряча лінія 24/7: 0 800 300 400", 8.5, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 12, 32);

  // Sticky Bar Wireframe
  const wfMBot = figma.createFrame(); wfMBot.resize(340, 36); wfMBot.x = 20; wfMBot.y = 680; wfMBot.cornerRadius = 6; wfMBot.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMob.appendChild(wfMBot);
  helperText(wfMBot, "🗺 Карта        |        🧮 Калькулятор        |        👤 Профіль", 9.5, "Bold", cWhite, 35, 10);

  // ==========================================================================
  // РОЗДІЛ 2: АСЕТИ, ТОКЕНИ ТА ДИЗАЙН-СИСТЕМА
  // ==========================================================================

'''

content = content[:pos_wf_start] + new_wireframes + content[pos_wf_end:]

# 4. Replace Design System Inputs & Controls section
old_ds_marker = '  // Input Fields & Chips'
old_ds_end = '  // ==========================================================================\n  // TOP-LEVEL OVERLAYS'
pos_ds_start = content.find(old_ds_marker)
pos_ds_end = content.find(old_ds_end)
assert pos_ds_start != -1 and pos_ds_end != -1, "Design System inputs boundaries not found"

new_ds_section = '''  // ==========================================================================
  // ПОЛЯ ВВОДУ ТА ЕЛЕМЕНТИ КЕРУВАННЯ (INPUTS, CHIPS, CHECKBOXES, SWITCHES - FIG 21)
  // ==========================================================================
  helperText(fDesignSystem, "Поля вводу та елементи керування (Inputs, Chips, Checkboxes, Switches)", 18, "Bold", cDark, 60, 340);
  helperText(fDesignSystem, "Анатомія станів текстових полів: Default, Focus, Error та Disabled згідно з WCAG 2.1 AA", 13, "Regular", cMuted, 60, 368);

  // Left Card: TextField States (width 630, height 380)
  const fInpCard = figma.createFrame();
  fInpCard.resize(630, 380);
  fInpCard.x = 60; fInpCard.y = 400;
  fInpCard.cornerRadius = 14;
  fInpCard.fills = [{{ type: "SOLID", color: cWhite }}];
  fInpCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(fInpCard);

  helperText(fInpCard, "СТАНИ ПОЛІВ ВВЕДЕННЯ (TEXTFIELD STATES)", 12, "Bold", cPrimary, 20, 16);

  // Field 1: Name in Focus
  helperText(fInpCard, "Ім'я та прізвище водія", 12, "Bold", cDark, 20, 44);
  const bFocBadge = figma.createFrame(); bFocBadge.resize(110, 18); bFocBadge.x = 500; bFocBadge.y = 44; bFocBadge.cornerRadius = 4; bFocBadge.fills = [{{ type: "SOLID", color: {{ r: 239/255, g: 246/255, b: 255/255 }} }}]; fInpCard.appendChild(bFocBadge);
  helperText(bFocBadge, "Focus (Введення)", 10, "Bold", cPrimary, 8, 3);
  const fInpFoc = figma.createFrame(); fInpFoc.resize(590, 38); fInpFoc.x = 20; fInpFoc.y = 66; fInpFoc.cornerRadius = 8; fInpFoc.fills = [{{ type: "SOLID", color: cWhite }}]; fInpFoc.strokes = [{{ type: "SOLID", color: cPrimary }}]; fInpCard.appendChild(fInpFoc);
  helperText(fInpFoc, "Андрій Лемішка|", 13, "Bold", cDark, 14, 10);
  helperText(fInpCard, "Активне поле: синя акцентна рамка (#005EC9) та фокусне кільце", 11, "Regular", cMuted, 20, 108);

  // Field 2: Phone with Error
  helperText(fInpCard, "Номер телефону", 12, "Bold", cDark, 20, 130);
  const bErrBadge = figma.createFrame(); bErrBadge.resize(95, 18); bErrBadge.x = 515; bErrBadge.y = 130; bErrBadge.cornerRadius = 4; bErrBadge.fills = [{{ type: "SOLID", color: {{ r: 254/255, g: 242/255, b: 242/255 }} }}]; fInpCard.appendChild(bErrBadge);
  helperText(bErrBadge, "Error (Помилка)", 10, "Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 8, 3);
  const fInpErr = figma.createFrame(); fInpErr.resize(590, 38); fInpErr.x = 20; fInpErr.y = 152; fInpErr.cornerRadius = 8; fInpErr.fills = [{{ type: "SOLID", color: {{ r: 254/255, g: 242/255, b: 242/255 }} }}]; fInpErr.strokes = [{{ type: "SOLID", color: {{ r: 239/255, g: 68/255, b: 68/255 }} }}]; fInpCard.appendChild(fInpErr);
  helperText(fInpErr, "+380 99 123", 13, "Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 14, 10);
  helperText(fInpCard, "⚠ Некоректний номер телефону! Введіть 9 цифр після коду оператора", 11, "Semi Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 20, 194);

  // Field 3: Email Default
  helperText(fInpCard, "Електронна пошта (Email)", 12, "Bold", cDark, 20, 216);
  const bDefBadge = figma.createFrame(); bDefBadge.resize(130, 18); bDefBadge.x = 480; bDefBadge.y = 216; bDefBadge.cornerRadius = 4; bDefBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; fInpCard.appendChild(bDefBadge);
  helperText(bDefBadge, "Default (Плейсхолдер)", 10, "Bold", cMuted, 8, 3);
  const fInpDef = figma.createFrame(); fInpDef.resize(590, 38); fInpDef.x = 20; fInpDef.y = 238; fInpDef.cornerRadius = 8; fInpDef.fills = [{{ type: "SOLID", color: cWhite }}]; fInpDef.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(fInpDef);
  helperText(fInpDef, "driver@charge.ua", 13, "Regular", cMuted, 14, 10);
  helperText(fInpCard, "Стан за замовчуванням: нейтральна рамка #CBD5E1, плейсхолдер #94A3B8", 11, "Regular", cMuted, 20, 280);

  // Field 4: Promo Disabled
  helperText(fInpCard, "Корпоративний промокод B2B", 12, "Bold", cDark, 20, 302);
  const bDisBadge = figma.createFrame(); bDisBadge.resize(120, 18); bDisBadge.x = 490; bDisBadge.y = 302; bDisBadge.cornerRadius = 4; bDisBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; bDisBadge.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(bDisBadge);
  helperText(bDisBadge, "Disabled (Заблоковано)", 10, "Bold", cMuted, 8, 3);
  const fInpDis = figma.createFrame(); fInpDis.resize(590, 38); fInpDis.x = 20; fInpDis.y = 324; fInpDis.cornerRadius = 8; fInpDis.fills = [{{ type: "SOLID", color: cBgSurface }}]; fInpDis.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(fInpDis);
  helperText(fInpDis, "Знижка недоступна", 13, "Regular", cMuted, 14, 10);

  // Right Card: Controls & Selection (width 630, height 380)
  const fCtrlCard = figma.createFrame();
  fCtrlCard.resize(630, 380);
  fCtrlCard.x = 750; fCtrlCard.y = 400;
  fCtrlCard.cornerRadius = 14;
  fCtrlCard.fills = [{{ type: "SOLID", color: cWhite }}];
  fCtrlCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(fCtrlCard);

  helperText(fCtrlCard, "ФІЛЬТРИ, ЧІПИ ТА ПЕРЕМИКАЧІ (CONTROLS)", 12, "Bold", cPrimary, 20, 16);

  helperText(fCtrlCard, "Швидкі чіпи вибору конекторів (Chips):", 12, "Bold", cDark, 20, 44);
  const cPill1 = figma.createFrame(); cPill1.resize(135, 32); cPill1.x = 20; cPill1.y = 68; cPill1.cornerRadius = 16; cPill1.fills = [{{ type: "SOLID", color: cPrimary }}]; fCtrlCard.appendChild(cPill1);
  helperText(cPill1, "⚡ Type 2 (Активний)", 11, "Bold", cWhite, 12, 8);

  const cPill2 = figma.createFrame(); cPill2.resize(120, 32); cPill2.x = 165; cPill2.y = 68; cPill2.cornerRadius = 16; cPill2.fills = [{{ type: "SOLID", color: cBgSurface }}]; cPill2.strokes = [{{ type: "SOLID", color: cBorder }}]; fCtrlCard.appendChild(cPill2);
  helperText(cPill2, "CCS 2 (160 кВт)", 11, "Bold", cDark, 14, 8);

  const cPill3 = figma.createFrame(); cPill3.resize(145, 32); cPill3.x = 295; cPill3.y = 68; cPill3.cornerRadius = 16; cPill3.fills = [{{ type: "SOLID", color: cSuccessBg }}]; cPill3.strokes = [{{ type: "SOLID", color: cSuccess }}]; fCtrlCard.appendChild(cPill3);
  helperText(cPill3, "🔋 З генератором", 11, "Bold", cSuccess, 14, 8);

  helperText(fCtrlCard, "Чекбокси та радіокнопки (WCAG зона дотику 48×48 px):", 12, "Bold", cDark, 20, 118);

  // Checkbox 1
  const cb1 = figma.createFrame(); cb1.resize(590, 44); cb1.x = 20; cb1.y = 142; cb1.cornerRadius = 8; cb1.fills = [{{ type: "SOLID", color: cBgSurface }}]; fCtrlCard.appendChild(cb1);
  const cb1Box = figma.createFrame(); cb1Box.resize(20, 20); cb1Box.x = 12; cb1Box.y = 12; cb1Box.cornerRadius = 4; cb1Box.fills = [{{ type: "SOLID", color: cPrimary }}]; cb1.appendChild(cb1Box);
  helperText(cb1Box, "✓", 12, "Bold", cWhite, 4, 3);
  helperText(cb1, "Погоджуюсь з умовами оферти (Touch target 48 px)", 12, "Semi Bold", cDark, 42, 14);

  // Checkbox 2
  const cb2 = figma.createFrame(); cb2.resize(590, 44); cb2.x = 20; cb2.y = 196; cb2.cornerRadius = 8; cb2.fills = [{{ type: "SOLID", color: cBgSurface }}]; fCtrlCard.appendChild(cb2);
  const cb2Box = figma.createFrame(); cb2Box.resize(20, 20); cb2Box.x = 12; cb2Box.y = 12; cb2Box.cornerRadius = 4; cb2Box.fills = [{{ type: "SOLID", color: cWhite }}]; cb2Box.strokes = [{{ type: "SOLID", color: cBorder }}]; cb2.appendChild(cb2Box);
  helperText(cb2, "Сповіщати про статус генератора в Telegram", 12, "Regular", cDark, 42, 14);

  // Radio Buttons & Switch
  helperText(fCtrlCard, "Тип заряджання & Перемикач мережі:", 12, "Bold", cDark, 20, 252);
  const radRow = figma.createFrame(); radRow.resize(590, 44); radRow.x = 20; radRow.y = 276; radRow.cornerRadius = 8; radRow.fills = [{{ type: "SOLID", color: cWhite }}]; radRow.strokes = [{{ type: "SOLID", color: cBorder }}]; fCtrlCard.appendChild(radRow);
  const radDot1 = figma.createFrame(); radDot1.resize(18, 18); radDot1.x = 12; radDot1.y = 13; radDot1.cornerRadius = 9; radDot1.fills = [{{ type: "SOLID", color: cPrimary }}]; radDot1.strokes = [{{ type: "SOLID", color: cWhite }}]; radRow.appendChild(radDot1);
  helperText(radRow, "Звичайна AC (до 22 кВт)", 12, "Bold", cDark, 38, 14);
  const radDot2 = figma.createFrame(); radDot2.resize(18, 18); radDot2.x = 230; radDot2.y = 13; radDot2.cornerRadius = 9; radDot2.fills = [{{ type: "SOLID", color: cWhite }}]; radDot2.strokes = [{{ type: "SOLID", color: cBorder }}]; radRow.appendChild(radDot2);
  helperText(radRow, "DC Ultra (160 кВт)", 12, "Regular", cMuted, 256, 14);

  // Toggle Switch
  const swRow = figma.createFrame(); swRow.resize(590, 44); swRow.x = 20; swRow.y = 328; swRow.cornerRadius = 8; swRow.fills = [{{ type: "SOLID", color: cBgSurface }}]; fCtrlCard.appendChild(swRow);
  const swTrk = figma.createFrame(); swTrk.resize(40, 22); swTrk.x = 12; swTrk.y = 11; swTrk.cornerRadius = 11; swTrk.fills = [{{ type: "SOLID", color: cSuccess }}]; swRow.appendChild(swTrk);
  const swThm = figma.createFrame(); swThm.resize(16, 16); swThm.x = 21; swThm.y = 3; swThm.cornerRadius = 8; swThm.fills = [{{ type: "SOLID", color: cWhite }}]; swTrk.appendChild(swThm);
  helperText(swRow, "Тільки активні станції з гарантованим генератором [ON]", 12, "Bold", cDark, 62, 14);

  // Live Station Card Component & Reviews (y: 800)
  helperText(fDesignSystem, "Компоненти карток (Station & Review Cards)", 18, "Bold", cDark, 60, 800);
  const cStatComp = figma.createFrame();
  cStatComp.resize(440, 370);
  cStatComp.x = 60; cStatComp.y = 835;
  cStatComp.cornerRadius = 16;
  cStatComp.fills = [{{ type: "SOLID", color: cWhite }}];
  cStatComp.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(cStatComp);

  addImageRect(cStatComp, "hub_kyiv", 0, 0, 440, 180, 0);
  helperText(cStatComp, "Хаб «Київ-Поділ» · 120 кВт CCS2", 16, "Bold", cDark, 20, 195);
  helperText(cStatComp, "м. Київ, вул. Сагайдачного, 12 · 4 порти", 13, "Regular", cMuted, 20, 222);

  const statPill = figma.createFrame();
  statPill.resize(170, 26);
  statPill.x = 20; statPill.y = 250;
  statPill.cornerRadius = 6;
  statPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
  cStatComp.appendChild(statPill);
  helperText(statPill, "🔋 Працює від генератора", 11, "Bold", cSuccess, 10, 6);

  const routeBtn = figma.createFrame();
  routeBtn.resize(400, 44);
  routeBtn.x = 20; routeBtn.y = 305;
  routeBtn.cornerRadius = 8;
  routeBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  cStatComp.appendChild(routeBtn);
  helperText(routeBtn, "Прокласти маршрут CCS2", 13, "Bold", cWhite, 110, 13);

  // Review Card Component
  const cRevComp = figma.createFrame();
  cRevComp.resize(440, 240);
  cRevComp.x = 540; cRevComp.y = 835;
  cRevComp.cornerRadius = 16;
  cRevComp.fills = [{{ type: "SOLID", color: cWhite }}];
  cRevComp.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(cRevComp);

  helperText(cRevComp, "★★★★★", 16, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 24, 24);
  helperText(cRevComp, "«Під час останнього блекауту у Києві ChargeUA буквально врятував поїздку. Проклав маршрут до хабу на Подолі — генератор працював стабільно!»", 13, "Medium", cDark, 24, 56, 390);
  addImageRect(cRevComp, "av1", 24, 155, 48, 48, 24);
  helperText(cRevComp, "Олексій К.", 14, "Bold", cDark, 84, 160);
  helperText(cRevComp, "Водій Tesla Model Y · Київ", 12, "Regular", cMuted, 84, 182);

'''

content = content[:pos_ds_start] + new_ds_section + content[pos_ds_end:]

# Also expand fDesignSystem height from 1260 to 1300
content = content.replace('fDesignSystem.resize(1440, 1260);', 'fDesignSystem.resize(1440, 1280);', 1)

# 5. Inject map_lviv into Desktop, Tablet, Mobile maps
# Desktop: dMapCanvas
old_dmap = '''  dMapCanvas.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dMapCanvas.strokes = [{{ type: "SOLID", color: cBorder }}];
  dMapSec.appendChild(dMapCanvas);'''

new_dmap = '''  dMapCanvas.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dMapCanvas.strokes = [{{ type: "SOLID", color: cBorder }}];
  dMapSec.appendChild(dMapCanvas);
  addImageRect(dMapCanvas, "map_lviv", 0, 0, 1260, 310, 12);'''

assert old_dmap in content, "old_dmap not found"
content = content.replace(old_dmap, new_dmap, 1)

# Tablet: tMapSec
old_tmap = '''const tMapSec = figma.createFrame(); tMapSec.resize(708, 250); tMapSec.x = 30; tMapSec.y = 990; tMapSec.cornerRadius = 14; tMapSec.fills = [{{ type: "SOLID", color: cBgSurface }}]; tMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tMapSec);'''

new_tmap = '''const tMapSec = figma.createFrame(); tMapSec.resize(708, 250); tMapSec.x = 30; tMapSec.y = 990; tMapSec.cornerRadius = 14; tMapSec.fills = [{{ type: "SOLID", color: cBgSurface }}]; tMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tMapSec);
  addImageRect(tMapSec, "map_lviv", 0, 0, 708, 250, 14);'''

assert old_tmap in content, "old_tmap not found"
content = content.replace(old_tmap, new_tmap, 1)

# Mobile: mMapSec
old_mmap = '''const mMapSec = figma.createFrame(); mMapSec.resize(350, 200); mMapSec.x = 20; mMapSec.y = 1440; mMapSec.cornerRadius = 14; mMapSec.fills = [{{ type: "SOLID", color: cBgSurface }}]; mMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mMapSec);'''

new_mmap = '''const mMapSec = figma.createFrame(); mMapSec.resize(350, 200); mMapSec.x = 20; mMapSec.y = 1440; mMapSec.cornerRadius = 14; mMapSec.fills = [{{ type: "SOLID", color: cBgSurface }}]; mMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mMapSec);
  addImageRect(mMapSec, "map_lviv", 0, 0, 350, 200, 14);'''

assert old_mmap in content, "old_mmap not found"
content = content.replace(old_mmap, new_mmap, 1)

with open("lab4/08_scratch/generate_final_figma_plugin.py", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Patch applied to generate_final_figma_plugin.py!")
