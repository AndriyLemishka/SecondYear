# -*- coding: utf-8 -*-
import sys

source_path = r"d:\Studing\SecondYear\FirstSemester\web\lab4\08_scratch\generate_final_figma_plugin.py"

with open(source_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Brand Assets (banner_ai and video_tutorial)
old_brand = """  helperText(bannerCard, "Промо-банер хабу (fig3_banner.png)", 14, "Bold", cDark, 24, 20);
  addImageRect(bannerCard, "banner", 24, 60, 352, 180, 8);

  const videoCard = figma.createFrame();
  videoCard.resize(400, 260);
  videoCard.x = 500; videoCard.y = 430;
  videoCard.cornerRadius = 14;
  videoCard.fills = [{{ type: "SOLID", color: cWhite }}];
  videoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(videoCard);
  helperText(videoCard, "Відеопрезентація сервісу (fig5_video.png)", 14, "Bold", cDark, 24, 20);
  addImageRect(videoCard, "video", 24, 60, 352, 180, 8);"""

new_brand = """  helperText(bannerCard, "AI Промо-банер мережі (ai_promo_banner.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(bannerCard, "banner_ai", 24, 60, 352, 180, 8);

  const videoCard = figma.createFrame();
  videoCard.resize(400, 260);
  videoCard.x = 500; videoCard.y = 430;
  videoCard.cornerRadius = 14;
  videoCard.fills = [{{ type: "SOLID", color: cWhite }}];
  videoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(videoCard);
  helperText(videoCard, "Відео-навчання та демо (ai_video_tutorial.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(videoCard, "video_tutorial", 24, 60, 352, 180, 8);"""

assert old_brand in content, "old_brand not found"
content = content.replace(old_brand, new_brand, 1)

# 2. Update Overlays: make fDrawerOverlay and fModalOverlay top-level frames
old_overlays = """  // FRAME 10: OVERLAYS
  const fOverlays = figma.createFrame();
  fOverlays.name = "10_Overlays";
  fOverlays.resize(1440, 900);
  fOverlays.x = 3400; fOverlays.y = 1050;
  fOverlays.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fOverlays, "10 — Оверлеї прототипу (Interactions & Overlays)", 28, "Bold", cDark, 60, 40);
  helperText(fOverlays, "Мобільне навігаційне меню та модальне вікно асистента навігації (без бронювання)", 15, "Regular", cMuted, 60, 80);

  // Mobile Drawer Overlay
  const drawerCard = figma.createFrame();
  drawerCard.resize(360, 620);
  drawerCard.x = 100; drawerCard.y = 140;
  drawerCard.cornerRadius = 16;
  drawerCard.fills = [{{ type: "SOLID", color: cWhite }}];
  drawerCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fOverlays.appendChild(drawerCard);

  helperText(drawerCard, "ChargeUA", 20, "Bold", cPrimary, 24, 24);
  helperText(drawerCard, "✕", 20, "Bold", cMuted, 310, 24);

  const navLinks = ["Головна", "Калькулятор витрат", "Карта станцій", "Тарифи операторів", "Для бізнесу (B2B)", "FAQ & Контакти"];
  navLinks.forEach((l, i) => helperText(drawerCard, l, 16, "Semi Bold", cDark, 24, 80 + i * 45));

  const closeBtn = figma.createFrame();
  closeBtn.resize(312, 46);
  closeBtn.x = 24; closeBtn.y = 530;
  closeBtn.cornerRadius = 8;
  closeBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  drawerCard.appendChild(closeBtn);
  helperText(closeBtn, "Закрити меню", 14, "Bold", cWhite, 105, 14);

  // Modal Dialog Overlay (Assistant route confirmation, ZERO booking)
  const modalBackdrop = figma.createFrame();
  modalBackdrop.resize(700, 620);
  modalBackdrop.x = 560; modalBackdrop.y = 140;
  modalBackdrop.cornerRadius = 16;
  modalBackdrop.fills = [{{ type: "SOLID", color: {{ r: 15/255, g: 23/255, b: 42/255 }}, opacity: 0.75 }}];
  fOverlays.appendChild(modalBackdrop);

  const modalBox = figma.createFrame();
  modalBox.resize(520, 360);
  modalBox.x = 90; modalBox.y = 130;
  modalBox.cornerRadius = 16;
  modalBox.fills = [{{ type: "SOLID", color: cWhite }}];
  modalBackdrop.appendChild(modalBox);

  const mSuccessPill = figma.createFrame();
  mSuccessPill.resize(190, 28);
  mSuccessPill.x = 30; mSuccessPill.y = 30;
  mSuccessPill.cornerRadius = 6;
  mSuccessPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
  modalBox.appendChild(mSuccessPill);
  helperText(mSuccessPill, "● Маршрут побудовано", 11, "Bold", cSuccess, 10, 6);

  helperText(modalBox, "Помічник ChargeUA: Станцію обрано!", 20, "Bold", cDark, 30, 75);
  helperText(modalBox, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв.", 14, "Regular", cMuted, 30, 115, 460);

  const mOkBtn = figma.createFrame();
  mOkBtn.resize(460, 48);
  mOkBtn.x = 30; mOkBtn.y = 260;
  mOkBtn.cornerRadius = 8;
  mOkBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  modalBox.appendChild(mOkBtn);
  helperText(mOkBtn, "Відкрити навігатор Waze / Google Maps", 14, "Bold", cWhite, 95, 15);"""

new_overlays = """  // ==========================================================================
  // TOP-LEVEL OVERLAYS ДЛЯ FIGMA PROTOTYPE (SIMULATION MODE)
  // ==========================================================================

  // OVERLAY 1: Mobile Navigation Drawer (Top-level frame destination for OVERLAY)
  const fDrawerOverlay = figma.createFrame();
  fDrawerOverlay.name = "10_Overlay_Drawer";
  fDrawerOverlay.resize(360, 640);
  fDrawerOverlay.x = 3200; fDrawerOverlay.y = 1050;
  fDrawerOverlay.cornerRadius = 16;
  fDrawerOverlay.fills = [{{ type: "SOLID", color: cWhite }}];
  fDrawerOverlay.strokes = [{{ type: "SOLID", color: cBorder }}];

  helperText(fDrawerOverlay, "ChargeUA", 20, "Bold", cPrimary, 24, 24);
  const drawerCloseX = figma.createFrame();
  drawerCloseX.resize(36, 36);
  drawerCloseX.x = 300; drawerCloseX.y = 18;
  drawerCloseX.cornerRadius = 6;
  drawerCloseX.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerCloseX);
  helperText(drawerCloseX, "✕", 18, "Bold", cMuted, 10, 8);

  const drawerLinkHome = figma.createFrame();
  drawerLinkHome.resize(312, 36);
  drawerLinkHome.x = 24; drawerLinkHome.y = 80;
  drawerLinkHome.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkHome);
  helperText(drawerLinkHome, "⚡ Головна сторінка", 16, "Semi Bold", cPrimary, 0, 6);

  const drawerLinkCalc = figma.createFrame();
  drawerLinkCalc.resize(312, 36);
  drawerLinkCalc.x = 24; drawerLinkCalc.y = 125;
  drawerLinkCalc.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkCalc);
  helperText(drawerLinkCalc, "🧮 Калькулятор витрат", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkMap = figma.createFrame();
  drawerLinkMap.resize(312, 36);
  drawerLinkMap.x = 24; drawerLinkMap.y = 170;
  drawerLinkMap.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkMap);
  helperText(drawerLinkMap, "🗺 Карта станцій онлайн", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkTariff = figma.createFrame();
  drawerLinkTariff.resize(312, 36);
  drawerLinkTariff.x = 24; drawerLinkTariff.y = 215;
  drawerLinkTariff.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkTariff);
  helperText(drawerLinkTariff, "💳 Тарифи операторів", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkB2b = figma.createFrame();
  drawerLinkB2b.resize(312, 36);
  drawerLinkB2b.x = 24; drawerLinkB2b.y = 260;
  drawerLinkB2b.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkB2b);
  helperText(drawerLinkB2b, "🏢 Для бізнесу (B2B)", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkFaq = figma.createFrame();
  drawerLinkFaq.resize(312, 36);
  drawerLinkFaq.x = 24; drawerLinkFaq.y = 305;
  drawerLinkFaq.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkFaq);
  helperText(drawerLinkFaq, "❓ FAQ & Підтримка 24/7", 16, "Semi Bold", cDark, 0, 6);

  const drawerCloseBtn = figma.createFrame();
  drawerCloseBtn.resize(312, 46);
  drawerCloseBtn.x = 24; drawerCloseBtn.y = 560;
  drawerCloseBtn.cornerRadius = 8;
  drawerCloseBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  fDrawerOverlay.appendChild(drawerCloseBtn);
  helperText(drawerCloseBtn, "Закрити меню", 14, "Bold", cWhite, 105, 14);

  // OVERLAY 2: Route Assistant Modal Dialog (Top-level frame destination for OVERLAY)
  const fModalOverlay = figma.createFrame();
  fModalOverlay.name = "10_Overlay_Modal";
  fModalOverlay.resize(540, 380);
  fModalOverlay.x = 3620; fModalOverlay.y = 1050;
  fModalOverlay.cornerRadius = 16;
  fModalOverlay.fills = [{{ type: "SOLID", color: cWhite }}];
  fModalOverlay.strokes = [{{ type: "SOLID", color: cBorder }}];

  const mSuccessPill = figma.createFrame();
  mSuccessPill.resize(200, 28);
  mSuccessPill.x = 30; mSuccessPill.y = 30;
  mSuccessPill.cornerRadius = 6;
  mSuccessPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
  fModalOverlay.appendChild(mSuccessPill);
  helperText(mSuccessPill, "● Маршрут сформовано", 11, "Bold", cSuccess, 12, 6);

  const modalCloseX = figma.createFrame();
  modalCloseX.resize(36, 36);
  modalCloseX.x = 474; modalCloseX.y = 26;
  modalCloseX.cornerRadius = 6;
  modalCloseX.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fModalOverlay.appendChild(modalCloseX);
  helperText(modalCloseX, "✕", 18, "Bold", cMuted, 10, 8);

  helperText(fModalOverlay, "Помічник ChargeUA: Станцію обрано!", 20, "Bold", cDark, 30, 75);
  helperText(fModalOverlay, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв.\\n\\nЖодних передоплат чи депозитів — оплата за фактом спожитих кВт·год.", 13, "Regular", cMuted, 30, 115, 480);

  const mOkBtn = figma.createFrame();
  mOkBtn.resize(480, 48);
  mOkBtn.x = 30; mOkBtn.y = 295;
  mOkBtn.cornerRadius = 8;
  mOkBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  fModalOverlay.appendChild(mOkBtn);
  helperText(mOkBtn, "Відкрити навігатор Waze / Google Maps", 14, "Bold", cWhite, 105, 15);

  // OVERVIEW FRAME: 10_Overlays_Spec
  const fOverlays = figma.createFrame();
  fOverlays.name = "10_Overlays";
  fOverlays.resize(1000, 640);
  fOverlays.x = 4220; fOverlays.y = 1050;
  fOverlays.cornerRadius = 16;
  fOverlays.fills = [{{ type: "SOLID", color: cBgSurface }}];
  fOverlays.strokes = [{{ type: "SOLID", color: cBorder }}];

  helperText(fOverlays, "10 — Оверлеї прототипу (Interactions & Overlays)", 26, "Bold", cDark, 50, 40);
  helperText(fOverlays, "Специфікація мікровзаємодій та оверлеїв у режимі симуляції Figma Prototype", 15, "Regular", cMuted, 50, 80);

  const specBox1 = figma.createFrame();
  specBox1.resize(420, 460);
  specBox1.x = 50; specBox1.y = 130;
  specBox1.cornerRadius = 12;
  specBox1.fills = [{{ type: "SOLID", color: cWhite }}];
  specBox1.strokes = [{{ type: "SOLID", color: cBorder }}];
  fOverlays.appendChild(specBox1);
  helperText(specBox1, "📱 Мобільне меню (Drawer Overlay)", 16, "Bold", cDark, 24, 24);
  helperText(specBox1, "• Тригер: Натискання на іконку ☰ у шапці Mobile\\n• Анімація: Dissolve 250ms (Ease In & Out)\\n• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей\\n• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map\\n• Стан: Активний розділ «Головна сторінка»\\n• Zero-booking: Доступ до довідки та тарифів", 13, "Regular", cMuted, 24, 65, 370);

  const specBox2 = figma.createFrame();
  specBox2.resize(420, 460);
  specBox2.x = 510; specBox2.y = 130;
  specBox2.cornerRadius = 12;
  specBox2.fills = [{{ type: "SOLID", color: cWhite }}];
  specBox2.strokes = [{{ type: "SOLID", color: cBorder }}];
  fOverlays.appendChild(specBox2);
  helperText(specBox2, "⚡ Асистент навігації (Modal Overlay)", 16, "Bold", cDark, 24, 24);
  helperText(specBox2, "• Тригер: Натискання «Прокласти маршрут» на станції\\n• Анімація: Центрований модальний оверлей 250ms\\n• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)\\n• Дія кнопки: Запуск зовнішнього додатку навігатора\\n• Закриття: Клік на кнопку Waze або ✕ закриває оверлей\\n• Живий статус: 3 з 4 вільні, генератор активний", 13, "Regular", cMuted, 24, 65, 370);"""

assert old_overlays in content, "old_overlays not found"
content = content.replace(old_overlays, new_overlays, 1)

# 3. Update Desktop popular stations: collect sBtn into array
old_desk_stat = """  stationsData.slice(0, 3).forEach((st, idx) => {
    const sCard = figma.createFrame();
    sCard.resize(420, 380);
    sCard.x = 60 + idx * 450; sCard.y = 1740;
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
  });"""

# Need to match with escaped curly braces in the file
old_desk_stat_pattern = """  stationsData.slice(0, 3).forEach((st, idx) => {{
    const sCard = figma.createFrame();
    sCard.resize(420, 380);
    sCard.x = 60 + idx * 450; sCard.y = 1740;
    sCard.cornerRadius = 16;
    sCard.fills = [{{ type: "SOLID", color: cWhite }}];
    sCard.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesktop.appendChild(sCard);

    addImageRect(sCard, st.img, 0, 0, 420, 190, 0);
    helperText(sCard, st.title, 16, "Bold", cDark, 20, 205);
    helperText(sCard, st.addr, 13, "Regular", cMuted, 20, 232);

    const sPill = figma.createFrame();
    sPill.resize(170, 26);
    sPill.x = 20; sPill.y = 265;
    sPill.cornerRadius = 6;
    sPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}];
    sCard.appendChild(sPill);
    helperText(sPill, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 6);

    const sBtn = figma.createFrame();
    sBtn.resize(380, 44);
    sBtn.x = 20; sBtn.y = 315;
    sBtn.cornerRadius = 8;
    sBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
    sCard.appendChild(sBtn);
    helperText(sBtn, "Прокласти маршрут", 13, "Bold", cWhite, 120, 13);
  }});"""

new_desk_stat = """  const desktopStationBtns = [];
  stationsData.slice(0, 3).forEach((st, idx) => {{
    const sCard = figma.createFrame();
    sCard.resize(420, 380);
    sCard.x = 60 + idx * 450; sCard.y = 1740;
    sCard.cornerRadius = 16;
    sCard.fills = [{{ type: "SOLID", color: cWhite }}];
    sCard.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesktop.appendChild(sCard);

    addImageRect(sCard, st.img, 0, 0, 420, 190, 0);
    helperText(sCard, st.title, 16, "Bold", cDark, 20, 205);
    helperText(sCard, st.addr, 13, "Regular", cMuted, 20, 232);

    const sPill = figma.createFrame();
    sPill.resize(170, 26);
    sPill.x = 20; sPill.y = 265;
    sPill.cornerRadius = 6;
    sPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}];
    sCard.appendChild(sPill);
    helperText(sPill, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 6);

    const sBtn = figma.createFrame();
    sBtn.resize(380, 44);
    sBtn.x = 20; sBtn.y = 315;
    sBtn.cornerRadius = 8;
    sBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
    sCard.appendChild(sBtn);
    helperText(sBtn, "Прокласти маршрут", 13, "Bold", cWhite, 120, 13);
    desktopStationBtns.push(sBtn);
  }});"""

assert old_desk_stat_pattern in content, "old_desk_stat_pattern not found"
content = content.replace(old_desk_stat_pattern, new_desk_stat, 1)

# 4. Update Tablet popular stations: add tSb and collect into array
old_tab_stat = """  stationsData.slice(0, 2).forEach((st, idx) => {{
    const tSc = figma.createFrame(); tSc.resize(708, 280); tSc.x = 30; tSc.y = 1305 + idx * 300; tSc.cornerRadius = 14; tSc.fills = [{{ type: "SOLID", color: cWhite }}]; tSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tSc);
    addImageRect(tSc, st.img, 0, 0, 708, 150, 0);
    helperText(tSc, st.title, 16, "Bold", cDark, 20, 170);
    helperText(tSc, st.addr, 13, "Regular", cMuted, 20, 195);
    const tSp = figma.createFrame(); tSp.resize(170, 24); tSp.x = 20; tSp.y = 225; tSp.cornerRadius = 6; tSp.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; tSc.appendChild(tSp);
    helperText(tSp, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 5);
  }});"""

new_tab_stat = """  const tabletStationBtns = [];
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const tSc = figma.createFrame(); tSc.resize(708, 280); tSc.x = 30; tSc.y = 1305 + idx * 300; tSc.cornerRadius = 14; tSc.fills = [{{ type: "SOLID", color: cWhite }}]; tSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tSc);
    addImageRect(tSc, st.img, 0, 0, 708, 150, 0);
    helperText(tSc, st.title, 16, "Bold", cDark, 20, 170);
    helperText(tSc, st.addr, 13, "Regular", cMuted, 20, 195);
    const tSp = figma.createFrame(); tSp.resize(170, 24); tSp.x = 20; tSp.y = 225; tSp.cornerRadius = 6; tSp.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; tSc.appendChild(tSp);
    helperText(tSp, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 5);
    const tSb = figma.createFrame(); tSb.resize(220, 36); tSb.x = 468; tSb.y = 220; tSb.cornerRadius = 6; tSb.fills = [{{ type: "SOLID", color: cPrimary }}]; tSc.appendChild(tSb);
    helperText(tSb, "Прокласти маршрут", 12, "Bold", cWhite, 45, 10);
    tabletStationBtns.push(tSb);
  }});"""

assert old_tab_stat in content, "old_tab_stat not found"
content = content.replace(old_tab_stat, new_tab_stat, 1)

# 5. Update Mobile Header (mBurgerBtn) and bottom nav
old_mob_head = """  // Mobile Header
  const mHead = figma.createFrame(); mHead.resize(390, 56); mHead.y = 34; mHead.fills = [{{ type: "SOLID", color: cWhite }}]; mHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mHead);
  addSvgNode(mHead, "logo", 16, 14, 28, 28);
  helperText(mHead, "ChargeUA", 19, "Bold", cPrimary, 52, 17);
  helperText(mHead, "☰", 22, "Bold", cDark, 350, 14);"""

new_mob_head = """  // Mobile Header
  const mHead = figma.createFrame(); mHead.resize(390, 56); mHead.y = 34; mHead.fills = [{{ type: "SOLID", color: cWhite }}]; mHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mHead);
  addSvgNode(mHead, "logo", 16, 14, 28, 28);
  helperText(mHead, "ChargeUA", 19, "Bold", cPrimary, 52, 17);
  const mBurgerBtn = figma.createFrame();
  mBurgerBtn.resize(40, 40);
  mBurgerBtn.x = 340; mBurgerBtn.y = 8;
  mBurgerBtn.cornerRadius = 6;
  mBurgerBtn.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mHead.appendChild(mBurgerBtn);
  helperText(mBurgerBtn, "☰", 22, "Bold", cDark, 10, 6);"""

assert old_mob_head in content, "old_mob_head not found"
content = content.replace(old_mob_head, new_mob_head, 1)

# 6. Update Mobile station cards: collect mSb
old_mob_stat = """  stationsData.slice(0, 2).forEach((st, idx) => {{
    const mSc = figma.createFrame(); mSc.resize(350, 280); mSc.x = 20; mSc.y = 830 + idx * 295; mSc.cornerRadius = 14; mSc.fills = [{{ type: "SOLID", color: cWhite }}]; mSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSc);
    addImageRect(mSc, st.img, 0, 0, 350, 140, 0);
    helperText(mSc, st.title, 14, "Bold", cDark, 16, 155);
    helperText(mSc, st.addr, 11, "Regular", cMuted, 16, 178);

    const mPill = figma.createFrame(); mPill.resize(160, 22); mPill.x = 16; mPill.y = 202; mPill.cornerRadius = 4; mPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; mSc.appendChild(mPill);
    helperText(mPill, st.gen ? "🔋 Генератор ON" : "⚡ Мережа ON", 10, "Bold", st.gen ? cSuccess : cPrimary, 8, 4);

    const mSb = figma.createFrame(); mSb.resize(318, 38); mSb.x = 16; mSb.y = 230; mSb.cornerRadius = 8; mSb.fills = [{{ type: "SOLID", color: cPrimary }}]; mSc.appendChild(mSb);
    helperText(mSb, "Прокласти маршрут", 12, "Bold", cWhite, 95, 11);
  }});"""

new_mob_stat = """  const mobileStationBtns = [];
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const mSc = figma.createFrame(); mSc.resize(350, 280); mSc.x = 20; mSc.y = 830 + idx * 295; mSc.cornerRadius = 14; mSc.fills = [{{ type: "SOLID", color: cWhite }}]; mSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSc);
    addImageRect(mSc, st.img, 0, 0, 350, 140, 0);
    helperText(mSc, st.title, 14, "Bold", cDark, 16, 155);
    helperText(mSc, st.addr, 11, "Regular", cMuted, 16, 178);

    const mPill = figma.createFrame(); mPill.resize(160, 22); mPill.x = 16; mPill.y = 202; mPill.cornerRadius = 4; mPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; mSc.appendChild(mPill);
    helperText(mPill, st.gen ? "🔋 Генератор ON" : "⚡ Мережа ON", 10, "Bold", st.gen ? cSuccess : cPrimary, 8, 4);

    const mSb = figma.createFrame(); mSb.resize(318, 38); mSb.x = 16; mSb.y = 230; mSb.cornerRadius = 8; mSb.fills = [{{ type: "SOLID", color: cPrimary }}]; mSc.appendChild(mSb);
    helperText(mSb, "Прокласти маршрут", 12, "Bold", cWhite, 95, 11);
    mobileStationBtns.push(mSb);
  }});"""

assert old_mob_stat in content, "old_mob_stat not found"
content = content.replace(old_mob_stat, new_mob_stat, 1)

# 7. Update Mobile Bottom Navigation: interactive tab items
old_bottom_nav = """  // Sticky Bottom Navigation
  const mBottomNav = figma.createFrame(); mBottomNav.resize(390, 54); mBottomNav.y = 2970; mBottomNav.fills = [{{ type: "SOLID", color: cWhite }}]; mBottomNav.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mBottomNav);
  helperText(mBottomNav, "⚡ Головна           🗺 Карта           🧮 Калькулятор           👤 Профіль", 11, "Bold", cDark, 20, 18);"""

new_bottom_nav = """  // Sticky Bottom Navigation with interactive tabs
  const mBottomNav = figma.createFrame(); mBottomNav.resize(390, 54); mBottomNav.y = 2970; mBottomNav.fills = [{{ type: "SOLID", color: cWhite }}]; mBottomNav.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mBottomNav);

  const mBottomNavHome = figma.createFrame();
  mBottomNavHome.resize(90, 54);
  mBottomNavHome.x = 5; mBottomNavHome.y = 0;
  mBottomNavHome.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavHome);
  helperText(mBottomNavHome, "⚡ Головна", 11, "Bold", cPrimary, 15, 18);

  const mBottomNavMap = figma.createFrame();
  mBottomNavMap.resize(90, 54);
  mBottomNavMap.x = 100; mBottomNavMap.y = 0;
  mBottomNavMap.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavMap);
  helperText(mBottomNavMap, "🗺 Карта", 11, "Bold", cDark, 18, 18);

  const mBottomNavCalc = figma.createFrame();
  mBottomNavCalc.resize(100, 54);
  mBottomNavCalc.x = 195; mBottomNavCalc.y = 0;
  mBottomNavCalc.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavCalc);
  helperText(mBottomNavCalc, "🧮 Калькулятор", 11, "Bold", cDark, 10, 18);

  const mBottomNavProfile = figma.createFrame();
  mBottomNavProfile.resize(85, 54);
  mBottomNavProfile.x = 300; mBottomNavProfile.y = 0;
  mBottomNavProfile.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavProfile);
  helperText(mBottomNavProfile, "👤 Профіль", 11, "Bold", cDark, 12, 18);"""

assert old_bottom_nav in content, "old_bottom_nav not found"
content = content.replace(old_bottom_nav, new_bottom_nav, 1)

# 8. Update Catalog Header and Station Cards
old_cat_head = """  const catHead = figma.createFrame(); catHead.resize(1440, 76); catHead.y = 40; catHead.fills = [{{ type: "SOLID", color: cWhite }}]; catHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(catHead);
  addSvgNode(catHead, "logo", 60, 20, 36, 36);
  helperText(catHead, "ChargeUA", 22, "Bold", cPrimary, 105, 24);
  helperText(catHead, "Головна        Калькулятор        Карта станцій        Тарифи        Для бізнесу", 14, "Semi Bold", cDark, 420, 28);
  const catHeadCta = figma.createFrame(); catHeadCta.resize(160, 42); catHeadCta.x = 1220; catHeadCta.y = 17; catHeadCta.cornerRadius = 8; catHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}]; catHead.appendChild(catHeadCta);
  helperText(catHeadCta, "Мій кабінет", 13, "Bold", cWhite, 40, 12);"""

new_cat_head = """  const catHead = figma.createFrame(); catHead.resize(1440, 76); catHead.y = 40; catHead.fills = [{{ type: "SOLID", color: cWhite }}]; catHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(catHead);
  const catLogo = figma.createFrame(); catLogo.resize(180, 40); catLogo.x = 60; catLogo.y = 18; catLogo.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; catHead.appendChild(catLogo);
  addSvgNode(catLogo, "logo", 0, 2, 36, 36);
  helperText(catLogo, "ChargeUA", 22, "Bold", cPrimary, 45, 6);
  helperText(catHead, "Головна        Калькулятор        Карта станцій        Тарифи        Для бізнесу", 14, "Semi Bold", cDark, 420, 28);
  const catHeadCta = figma.createFrame(); catHeadCta.resize(160, 42); catHeadCta.x = 1220; catHeadCta.y = 17; catHeadCta.cornerRadius = 8; catHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}]; catHead.appendChild(catHeadCta);
  helperText(catHeadCta, "← На головну", 13, "Bold", cWhite, 32, 12);"""

assert old_cat_head in content, "old_cat_head not found"
content = content.replace(old_cat_head, new_cat_head, 1)

# 9. Update Catalog Station Cards: collect cBtn
old_cat_stat = """  stationsData.forEach((st, idx) => {{
    const row = Math.floor(idx / 2);
    const col = idx % 2;
    const cd = figma.createFrame(); cd.resize(640, 310); cd.x = 60 + col * 680; cd.y = 360 + row * 335; cd.cornerRadius = 16; cd.fills = [{{ type: "SOLID", color: cWhite }}]; cd.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(cd);
    addImageRect(cd, st.img, 0, 0, 640, 160, 0);

    helperText(cd, st.title, 17, "Bold", cDark, 20, 175);
    helperText(cd, st.addr, 13, "Regular", cMuted, 20, 202);

    const sPill = figma.createFrame(); sPill.resize(170, 26); sPill.x = 20; sPill.y = 230; sPill.cornerRadius = 6; sPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; cd.appendChild(sPill);
    helperText(sPill, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 6);

    const portBadge = figma.createFrame(); portBadge.resize(140, 26); portBadge.x = 200; portBadge.y = 230; portBadge.cornerRadius = 6; portBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; cd.appendChild(portBadge);
    helperText(portBadge, `● ${{st.freePorts}}`, 11, "Medium", cDark, 12, 6);

    const cBtn = figma.createFrame(); cBtn.resize(240, 42); cBtn.x = 380; cBtn.y = 250; cBtn.cornerRadius = 8; cBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; cd.appendChild(cBtn);
    helperText(cBtn, "Прокласти маршрут", 13, "Bold", cWhite, 45, 12);
  }});"""

new_cat_stat = """  const catalogStationBtns = [];
  stationsData.forEach((st, idx) => {{
    const row = Math.floor(idx / 2);
    const col = idx % 2;
    const cd = figma.createFrame(); cd.resize(640, 310); cd.x = 60 + col * 680; cd.y = 360 + row * 335; cd.cornerRadius = 16; cd.fills = [{{ type: "SOLID", color: cWhite }}]; cd.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(cd);
    addImageRect(cd, st.img, 0, 0, 640, 160, 0);

    helperText(cd, st.title, 17, "Bold", cDark, 20, 175);
    helperText(cd, st.addr, 13, "Regular", cMuted, 20, 202);

    const sPill = figma.createFrame(); sPill.resize(170, 26); sPill.x = 20; sPill.y = 230; sPill.cornerRadius = 6; sPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; cd.appendChild(sPill);
    helperText(sPill, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 6);

    const portBadge = figma.createFrame(); portBadge.resize(140, 26); portBadge.x = 200; portBadge.y = 230; portBadge.cornerRadius = 6; portBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; cd.appendChild(portBadge);
    helperText(portBadge, `● ${{st.freePorts}}`, 11, "Medium", cDark, 12, 6);

    const cBtn = figma.createFrame(); cBtn.resize(240, 42); cBtn.x = 380; cBtn.y = 250; cBtn.cornerRadius = 8; cBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; cd.appendChild(cBtn);
    helperText(cBtn, "Прокласти маршрут", 13, "Bold", cWhite, 45, 12);
    catalogStationBtns.push(cBtn);
  }});"""

assert old_cat_stat in content, "old_cat_stat not found"
content = content.replace(old_cat_stat, new_cat_stat, 1)

# 10. Update Station Details: detLogo
old_det_head = """  const detHead = figma.createFrame(); detHead.resize(1440, 76); detHead.y = 40; detHead.fills = [{{ type: "SOLID", color: cWhite }}]; detHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detHead);
  addSvgNode(detHead, "logo", 60, 20, 36, 36);
  helperText(detHead, "ChargeUA", 22, "Bold", cPrimary, 105, 24);"""

new_det_head = """  const detHead = figma.createFrame(); detHead.resize(1440, 76); detHead.y = 40; detHead.fills = [{{ type: "SOLID", color: cWhite }}]; detHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detHead);
  const detLogo = figma.createFrame(); detLogo.resize(180, 40); detLogo.x = 60; detLogo.y = 18; detLogo.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; detHead.appendChild(detLogo);
  addSvgNode(detLogo, "logo", 0, 2, 36, 36);
  helperText(detLogo, "ChargeUA", 22, "Bold", cPrimary, 45, 6);"""

assert old_det_head in content, "old_det_head not found"
content = content.replace(old_det_head, new_det_head, 1)

# 11. Add Prototyping Link Connections & Flow Starting Points before zoom
old_end = """  // Zoom into view
  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("🎉 Готово! Усі 12 фреймів ChargeUA, вектори та фотографії успішно згенеровані!");"""

new_end = """  // ==========================================================================
  // НАЛАШТУВАННЯ ІНТЕРАКТИВНОСТІ FIGMA PROTOTYPE (SIMULATION MODE)
  // ==========================================================================

  // 1. Desktop Interactions
  await linkNodes(dHeadCta, fCatalog);
  await linkNodes(dHeroBtn2, fCatalog);
  for (const btn of desktopStationBtns) {{
    await linkNodes(btn, fStationDetails);
  }}

  // 2. Tablet Interactions
  await linkNodes(tHeadCta, fCatalog);
  await linkNodes(tBtn2, fCatalog);
  await linkNodes(tCalcBtn, fCatalog);
  for (const btn of tabletStationBtns) {{
    await linkNodes(btn, fStationDetails);
  }}

  // 3. Mobile Interactions (Burger -> Drawer Overlay, Map -> Catalog, Cards -> Details)
  await linkOverlay(mBurgerBtn, fDrawerOverlay);
  await linkNodes(mBtnMap, fCatalog);
  await linkNodes(mCalcAct, fCatalog);
  for (const btn of mobileStationBtns) {{
    await linkNodes(btn, fStationDetails);
  }}
  await linkNodes(mBottomNavHome, fMobile);
  await linkNodes(mBottomNavMap, fCatalog);

  // 4. Catalog Interactions
  await linkNodes(catLogo, fDesktop);
  await linkNodes(catHeadCta, fDesktop);
  for (const btn of catalogStationBtns) {{
    await linkNodes(btn, fStationDetails);
  }}

  // 5. Station Details Interactions
  await linkNodes(detLogo, fDesktop);
  await linkNodes(detHeadCta, fCatalog);
  await linkOverlay(detRouteBtn, fModalOverlay);

  // 6. Overlays Interactions
  await linkClose(drawerCloseBtn);
  await linkClose(drawerCloseX);
  await linkNodes(drawerLinkHome, fMobile);
  await linkNodes(drawerLinkMap, fCatalog);
  await linkClose(mOkBtn);
  await linkClose(modalCloseX);

  // 7. Flow Starting Points for Figma Prototype Simulator
  try {{
    figma.currentPage.flowStartingPoints = [
      {{ nodeId: fDesktop.id, name: "Головний потік (Desktop)" }},
      {{ nodeId: fMobile.id, name: "Мобільний потік (Mobile)" }},
      {{ nodeId: fCatalog.id, name: "Каталог і Карта станцій" }}
    ];
  }} catch (e) {{
    console.warn("Could not set flowStartingPoints:", e);
  }}

  // Zoom into view
  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("🎉 Готово! Усі 12 фреймів ChargeUA, вектори, фотографії та симуляція Prototype успішно налаштовані!");"""

assert old_end in content, "old_end not found"
content = content.replace(old_end, new_end, 1)

# Write back
with open(source_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: generate_final_figma_plugin.py patched successfully!")
