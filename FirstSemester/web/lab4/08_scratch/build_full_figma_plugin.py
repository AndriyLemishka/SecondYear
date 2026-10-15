# -*- coding: utf-8 -*-
"""
Script to generate the complete figma_builder_plugin.js with:
- Native SVG vectors (Logo.svg, Calculator.svg, Location.svg, Information.svg) via figma.createNodeFromSvg()
- Base64 embedded images (hero, hubs, generator, video, cable, avatars) via figma.createImage()
- Full 11 frames on canvas:
  00_Cover, 01_User_Flow, 02_Sitemap, 03_Wireframes, 04.0_Brand_Assets_LR3,
  04.1_Design_System, 05_Desktop (3800px full page), 06_Tablet (3400px full page),
  07_Mobile (3200px full page), 08_Catalog_Map, 09_Station_Details, 10_Overlays
"""

import os, io, base64
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
OUT_JS = os.path.join(BASE_DIR, "05_figma_exports", "figma_builder_plugin.js")

# 1. Read SVG assets
def read_svg(filename):
    p = os.path.join(MAT_DIR, filename)
    with open(p, "r", encoding="utf-8") as f:
        # strip newlines and unneeded spaces for js string
        return f.read().replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

svg_logo = read_svg("Logo.svg")
svg_calc = read_svg("Calculator.svg")
svg_loc = read_svg("Location.svg")
svg_info = read_svg("Information.svg")

# 2. Convert images to optimized base64
def get_b64_jpeg(filename, max_w, max_h, quality=75):
    p = os.path.join(MAT_DIR, filename)
    im = Image.open(p).convert("RGB")
    im.thumbnail((max_w, max_h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")

b64_hero = get_b64_jpeg("hero_bg.jpg", 600, 350, 75)
b64_hub_kyiv = get_b64_jpeg("ai_hub_kyiv.jpg", 400, 250, 75)
b64_hub_lviv = get_b64_jpeg("ai_hub_lviv.jpg", 400, 250, 75)
b64_generator = get_b64_jpeg("ai_generator_blackout.jpg", 400, 250, 75)
b64_cable = get_b64_jpeg("ai_step_cable.jpg", 300, 200, 75)
b64_video = get_b64_jpeg("fig5_video.png", 400, 200, 75)
b64_banner = get_b64_jpeg("fig3_banner.png", 400, 200, 75)
b64_av1 = get_b64_jpeg("ai_avatar_oleksiy.jpg", 120, 120, 75)
b64_av2 = get_b64_jpeg("ai_avatar_olena.jpg", 120, 120, 75)
b64_av3 = get_b64_jpeg("ai_avatar_sergiy.jpg", 120, 120, 75)

print("All assets processed. Generating plugin JS...")

js_content = f"""// ==============================================================================
// ChargeUA Figma Builder Plugin (Лабораторна робота №4)
// Студент: Лемішка Андрій Анатолійович (група ПП-24)
// Кафедра САПР, НУ «Львівська політехніка»
// Повна генерація всіх макетів, компонентів, сторінок, векторних логотипів та зображень
// ==============================================================================

function base64ToBytes(base64) {{
  const bin = atob(base64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) {{
    bytes[i] = bin.charCodeAt(i);
  }}
  return bytes;
}}

const ASSETS_B64 = {{
  hero: "{b64_hero}",
  hub_kyiv: "{b64_hub_kyiv}",
  hub_lviv: "{b64_hub_lviv}",
  generator: "{b64_generator}",
  cable: "{b64_cable}",
  video: "{b64_video}",
  banner: "{b64_banner}",
  av1: "{b64_av1}",
  av2: "{b64_av2}",
  av3: "{b64_av3}"
}};

const SVG_ASSETS = {{
  logo: `{svg_logo}`,
  calc: `{svg_calc}`,
  loc: `{svg_loc}`,
  info: `{svg_info}`
}};

async function run() {{
  figma.notify("🚀 Завантаження шрифтів та ініціалізація ChargeUA...");
  await figma.loadFontAsync({{ family: "Inter", style: "Regular" }});
  await figma.loadFontAsync({{ family: "Inter", style: "Medium" }});
  await figma.loadFontAsync({{ family: "Inter", style: "Semi Bold" }});
  await figma.loadFontAsync({{ family: "Inter", style: "Bold" }});

  // Прекешування зображень у Figma
  const imageHashes = {{}};
  for (const key of Object.keys(ASSETS_B64)) {{
    try {{
      const imgBytes = base64ToBytes(ASSETS_B64[key]);
      const imgObj = figma.createImage(imgBytes);
      imageHashes[key] = imgObj.hash;
    }} catch (e) {{
      console.warn("Image load failed for", key, e);
    }}
  }}

  // Кольори бренду ChargeUA
  const cPrimary = {{ r: 0 / 255, g: 94 / 255, b: 201 / 255 }}; // #005EC9
  const cPrimaryHover = {{ r: 0 / 255, g: 75 / 255, b: 181 / 255 }};
  const cCyan = {{ r: 0 / 255, g: 229 / 255, b: 255 / 255 }}; // #00E5FF
  const cDark = {{ r: 15 / 255, g: 23 / 255, b: 42 / 255 }}; // #0F172A
  const cWhite = {{ r: 1, g: 1, b: 1 }};
  const cBgSurface = {{ r: 248 / 255, g: 250 / 255, b: 252 / 255 }}; // #F8FAFC
  const cBorder = {{ r: 226 / 255, g: 232 / 255, b: 240 / 255 }}; // #E2E8F0
  const cSuccess = {{ r: 4 / 255, g: 120 / 255, b: 87 / 255 }}; // #047857
  const cSuccessBg = {{ r: 209 / 255, g: 250 / 255, b: 229 / 255 }}; // #D1FAE5
  const cMuted = {{ r: 100 / 255, g: 116 / 255, b: 139 / 255 }}; // #64748B

  function helperText(parent, text, size, style, color, x = 0, y = 0, width = null) {{
    const t = figma.createText();
    t.fontName = {{ family: "Inter", style: style }};
    t.characters = text;
    t.fontSize = size;
    t.fills = [{{ type: "SOLID", color: color }}];
    t.x = x;
    t.y = y;
    if (width) {{
      t.textAutoResize = "HEIGHT";
      t.resize(width, t.height);
    }}
    parent.appendChild(t);
    return t;
  }}

  function addImageRect(parent, imgKey, x, y, width, height, radius = 8) {{
    const rect = figma.createRectangle();
    rect.x = x;
    rect.y = y;
    rect.resize(width, height);
    rect.cornerRadius = radius;
    if (imageHashes[imgKey]) {{
      rect.fills = [{{ type: "IMAGE", scaleMode: "FILL", imageHash: imageHashes[imgKey] }}];
    }} else {{
      rect.fills = [{{ type: "SOLID", color: cBorder }}];
    }}
    parent.appendChild(rect);
    return rect;
  }}

  function addSvgNode(parent, svgKey, x, y, targetWidth = null, targetHeight = null) {{
    try {{
      const node = figma.createNodeFromSvg(SVG_ASSETS[svgKey]);
      node.x = x;
      node.y = y;
      if (targetWidth && targetHeight) {{
        node.rescale(targetWidth / node.width);
      }}
      parent.appendChild(node);
      return node;
    }} catch (e) {{
      console.warn("SVG error for", svgKey, e);
      return null;
    }}
  }}

  // ==========================================================================
  // РЯД 1: COVER, USER FLOW, SITEMAP, WIREFRAMES
  // ==========================================================================
  
  // FRAME 00: COVER
  const fCover = figma.createFrame();
  fCover.name = "00_Cover";
  fCover.resize(1440, 900);
  fCover.x = 0; fCover.y = 0;
  fCover.fills = [{{ type: "SOLID", color: cDark }}];

  const coverCard = figma.createFrame();
  coverCard.resize(1080, 620);
  coverCard.x = 180; coverCard.y = 140;
  coverCard.cornerRadius = 24;
  coverCard.fills = [{{ type: "SOLID", color: cWhite }}];
  fCover.appendChild(coverCard);

  helperText(coverCard, "ЛЬВІВСЬКА ПОЛІТЕХНІКА • КАФЕДРА САПР", 14, "Bold", cPrimary, 60, 60);
  helperText(coverCard, "Лабораторна робота №4", 42, "Bold", cDark, 60, 95);
  helperText(coverCard, "UX/UI прототипування та дизайн-система", 22, "Semi Bold", cMuted, 60, 155);
  helperText(coverCard, "Тема: «Лендинг мережі зарядних станцій «ChargeUA» (веб-помічник та агрегатор станцій)»", 16, "Medium", cDark, 60, 220);
  helperText(coverCard, "Дисципліна: Технології веб-розробки та дизайну · Варіант № 7", 15, "Regular", cMuted, 60, 255);

  const metaBox = figma.createFrame();
  metaBox.resize(960, 150);
  metaBox.x = 60; metaBox.y = 350;
  metaBox.cornerRadius = 14;
  metaBox.fills = [{{ type: "SOLID", color: cBgSurface }}];
  metaBox.strokes = [{{ type: "SOLID", color: cBorder }}];
  coverCard.appendChild(metaBox);

  helperText(metaBox, "Виконав: студент групи ПП-24", 15, "Regular", cDark, 30, 30);
  helperText(metaBox, "Лемішка Андрій Анатолійович", 22, "Bold", cPrimary, 30, 56);
  helperText(metaBox, "Науковий керівник: доц. Стефанович Т. О.", 15, "Regular", cDark, 30, 96);
  helperText(metaBox, "Львів — 2026", 16, "Bold", cMuted, 800, 96);

  // FRAME 01: USER FLOW
  const fUserFlow = figma.createFrame();
  fUserFlow.name = "01_User_Flow";
  fUserFlow.resize(1440, 900);
  fUserFlow.x = 1600; fUserFlow.y = 0;
  fUserFlow.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fUserFlow, "01 — Шляхи Користувача (User Flows)", 28, "Bold", cDark, 60, 50);
  helperText(fUserFlow, "3 критичні сценарії взаємодії водія із сервісом ChargeUA", 16, "Regular", cMuted, 60, 90);

  const flows = [
    {{ num: "1", title: "Екстрений пошук станції з генератором під час блекауту", desc: "Головна → Фільтр 'З генератором' → Карта станцій → Вибір вільного порту CCS2 → Навігатор Waze" }},
    {{ num: "2", title: "Розрахунок вартості підзарядки та порівняння тарифів мереж", desc: "Головна → Hero CTA 'Розрахувати' → Вибір моделі авто → Слайдер 20%→80% → Порівняння Yasno/EcoFactor → Вибір станції" }},
    {{ num: "3", title: "Онбординг та покроковий гайд для водія-новачка", desc: "Меню 'Як це працює' → 3 кроки підключення → Селектор конекторів → Правила безпеки → Карта" }}
  ];

  flows.forEach((fl, idx) => {{
    const card = figma.createFrame();
    card.resize(1320, 190);
    card.x = 60; card.y = 150 + idx * 240;
    card.cornerRadius = 16;
    card.fills = [{{ type: "SOLID", color: cWhite }}];
    card.strokes = [{{ type: "SOLID", color: cBorder }}];
    fUserFlow.appendChild(card);

    helperText(card, `СЦЕНАРІЙ ${{fl.num}}`, 12, "Bold", cPrimary, 24, 24);
    helperText(card, fl.title, 18, "Bold", cDark, 24, 46);
    helperText(card, fl.desc, 14, "Medium", cMuted, 24, 80);

    const sPill = figma.createFrame();
    sPill.resize(230, 34);
    sPill.x = 24; sPill.y = 130;
    sPill.cornerRadius = 6;
    sPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
    card.appendChild(sPill);
    helperText(sPill, "✓ Success State: Підтверджено", 11, "Bold", cSuccess, 14, 9);
  }});

  // FRAME 02: SITEMAP (RELUME STYLE)
  const fSitemap = figma.createFrame();
  fSitemap.name = "02_Sitemap";
  fSitemap.resize(1440, 900);
  fSitemap.x = 3200; fSitemap.y = 0;
  fSitemap.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fSitemap, "02 — Карта сайту (Sitemap · Relume AI Architecture)", 28, "Bold", cDark, 60, 50);
  helperText(fSitemap, "Дворівнева ієрархічна структура згенерована в Relume AI", 16, "Regular", cMuted, 60, 90);

  const homeNode = figma.createFrame();
  homeNode.resize(320, 240);
  homeNode.x = 560; homeNode.y = 150;
  homeNode.cornerRadius = 12;
  homeNode.fills = [{{ type: "SOLID", color: cWhite }}];
  homeNode.strokes = [{{ type: "SOLID", color: cPrimary }}];
  homeNode.strokeWeight = 2;
  fSitemap.appendChild(homeNode);

  helperText(homeNode, "Головна (Home) /", 16, "Bold", cPrimary, 20, 20);
  const homeSecs = ["• Header & Brand Logo", "• Hero + Quick Finder", "• Калькулятор витрат", "• Live-карта станцій", "• Енергонезалежність", "• Як це працює", "• Відгуки водіїв", "• Footer & Контакти"];
  homeSecs.forEach((s, i) => helperText(homeNode, s, 11, "Medium", cDark, 20, 52 + i * 20));

  const childPages = [
    {{ title: "Карта станцій", items: ["• Пошук за містом", "• Фільтр конекторів", "• Фільтр Генератор", "• Маркери на карті", "• Сортування потужності"] }},
    {{ title: "Сторінка станції", items: ["• Фото та адреса", "• Телеметрія портів", "• Тарифні плани", "• Бронювання CCS2", "• Маршрут у Waze"] }},
    {{ title: "Тарифи & Кальк", items: ["• Пресети моделей", "• Слайдер батареї", "• AC/DC розрахунок", "• Порівняння мереж", "• Економія vs Бензин"] }},
    {{ title: "Для бізнесу (B2B)", items: ["• Умови партнерства", "• ROI станції", "• Заявка на монтаж", "• Блекаут-рішення", "• FAQ партнерів"] }}
  ];

  childPages.forEach((cp, idx) => {{
    const cNode = figma.createFrame();
    cNode.resize(280, 200);
    cNode.x = 60 + idx * 340; cNode.y = 480;
    cNode.cornerRadius = 12;
    cNode.fills = [{{ type: "SOLID", color: cWhite }}];
    cNode.strokes = [{{ type: "SOLID", color: cBorder }}];
    fSitemap.appendChild(cNode);

    helperText(cNode, cp.title, 15, "Bold", cDark, 18, 18);
    cp.items.forEach((it, i) => helperText(cNode, it, 11, "Regular", cMuted, 18, 48 + i * 22));
  }});

  // FRAME 03: WIREFRAMES
  const fWireframes = figma.createFrame();
  fWireframes.name = "03_Wireframes";
  fWireframes.resize(1440, 900);
  fWireframes.x = 4800; fWireframes.y = 0;
  fWireframes.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fWireframes, "03 — Низькодеталізовані каркаси (Wireframes)", 28, "Bold", cDark, 60, 50);
  helperText(fWireframes, "Схематичні сірі каркаси Desktop (1440px) та Mobile (390px)", 16, "Regular", cMuted, 60, 90);

  // Desktop Wireframe box
  const wfDesk = figma.createFrame();
  wfDesk.resize(720, 680);
  wfDesk.x = 60; wfDesk.y = 150;
  wfDesk.cornerRadius = 12;
  wfDesk.fills = [{{ type: "SOLID", color: cWhite }}];
  wfDesk.strokes = [{{ type: "SOLID", color: cBorder }}];
  fWireframes.appendChild(wfDesk);
  helperText(wfDesk, "Desktop 1440 Wireframe Layout", 14, "Bold", cMuted, 20, 20);

  const wfDeskBlocks = ["Header [Logo | Nav | CTA]", "Hero [H1 Title | Text | Action Buttons | Placeholder Image]", "Calculator [Vehicle Presets | Battery Slider | Price Estimate]", "Station Map [Search Bar | Filter Chips | 3x Cards Grid]", "Blackout Section [Generator Specs | Uptime Badge]", "Testimonials [3x Review Cards] | Footer [4 Columns]"];
  wfDeskBlocks.forEach((b, i) => {{
    const blk = figma.createFrame();
    blk.resize(680, 75);
    blk.x = 20; blk.y = 55 + i * 95;
    blk.cornerRadius = 8;
    blk.fills = [{{ type: "SOLID", color: cBgSurface }}];
    blk.strokes = [{{ type: "SOLID", color: cBorder }}];
    wfDesk.appendChild(blk);
    helperText(blk, b, 12, "Semi Bold", cDark, 20, 28);
  }});

  // Mobile Wireframe box
  const wfMob = figma.createFrame();
  wfMob.resize(360, 680);
  wfMob.x = 840; wfMob.y = 150;
  wfMob.cornerRadius = 12;
  wfMob.fills = [{{ type: "SOLID", color: cWhite }}];
  wfMob.strokes = [{{ type: "SOLID", color: cBorder }}];
  fWireframes.appendChild(wfMob);
  helperText(wfMob, "Mobile 390 Wireframe Layout", 14, "Bold", cMuted, 20, 20);

  const wfMobBlocks = ["Header [Logo | Burger]", "Hero [H1 | Action Button]", "Calculator [Slider | Price]", "Stations [Vertical List]", "Generator [Badge | Card]", "Footer [Compact]"];
  wfMobBlocks.forEach((b, i) => {{
    const blk = figma.createFrame();
    blk.resize(320, 80);
    blk.x = 20; blk.y = 55 + i * 100;
    blk.cornerRadius = 8;
    blk.fills = [{{ type: "SOLID", color: cBgSurface }}];
    blk.strokes = [{{ type: "SOLID", color: cBorder }}];
    wfMob.appendChild(blk);
    helperText(blk, b, 11, "Semi Bold", cDark, 16, 30);
  }});

  // ==========================================================================
  // РЯД 2: BRAND ASSETS, DESIGN SYSTEM, OVERLAYS
  // ==========================================================================

  // FRAME 04.0: BRAND ASSETS FROM LR3
  const fAssets = figma.createFrame();
  fAssets.name = "04.0_Brand_Assets_LR3";
  fAssets.resize(1440, 900);
  fAssets.x = 0; fAssets.y = 1050;
  fAssets.fills = [{{ type: "SOLID", color: cWhite }}];

  helperText(fAssets, "Brand Assets · Векторні та растрові активи з ЛР3", 28, "Bold", cDark, 60, 40);
  helperText(fAssets, "Оригінальні активи: Logo.svg, Calculator.svg, Location.svg, Information.svg, hero_bg.jpg, fig3_banner.png, fig5_video.png", 15, "Regular", cMuted, 60, 80);

  // Logo Preview
  const logoCard = figma.createFrame();
  logoCard.resize(400, 260);
  logoCard.x = 60; logoCard.y = 130;
  logoCard.cornerRadius = 14;
  logoCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  logoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(logoCard);
  helperText(logoCard, "Векторний логотип бренду (Logo.svg)", 14, "Bold", cDark, 24, 20);
  addSvgNode(logoCard, "logo", 100, 70, 200, 170);

  // 3 Icons Preview
  const iconsCard = figma.createFrame();
  iconsCard.resize(400, 260);
  iconsCard.x = 500; iconsCard.y = 130;
  iconsCard.cornerRadius = 14;
  iconsCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  iconsCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(iconsCard);
  helperText(iconsCard, "Векторні піктограми послуг (ЛР3)", 14, "Bold", cDark, 24, 20);
  addSvgNode(iconsCard, "calc", 40, 90, 80, 80);
  addSvgNode(iconsCard, "loc", 160, 90, 80, 80);
  addSvgNode(iconsCard, "info", 280, 90, 80, 80);

  // Hero BG Preview
  const heroCard = figma.createFrame();
  heroCard.resize(420, 260);
  heroCard.x = 940; heroCard.y = 130;
  heroCard.cornerRadius = 14;
  heroCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  heroCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(heroCard);
  helperText(heroCard, "3D Hero Visual (hero_bg.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(heroCard, "hero", 24, 60, 372, 180, 8);

  // Banner Preview
  const bannerCard = figma.createFrame();
  bannerCard.resize(420, 260);
  bannerCard.x = 60; bannerCard.y = 430;
  bannerCard.cornerRadius = 14;
  bannerCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  bannerCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(bannerCard);
  helperText(bannerCard, "Промо-банер мережі (fig3_banner.png)", 14, "Bold", cDark, 24, 20);
  addImageRect(bannerCard, "banner", 24, 60, 372, 180, 8);

  // Video Preview
  const videoCard = figma.createFrame();
  videoCard.resize(420, 260);
  videoCard.x = 500; videoCard.y = 430;
  videoCard.cornerRadius = 14;
  videoCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  videoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(videoCard);
  helperText(videoCard, "Відеопрев'ю роботи сервісу (fig5_video.png)", 14, "Bold", cDark, 24, 20);
  addImageRect(videoCard, "video", 24, 60, 372, 180, 8);

  // Blackout Generator Preview
  const genCard = figma.createFrame();
  genCard.resize(420, 260);
  genCard.x = 940; genCard.y = 430;
  genCard.cornerRadius = 14;
  genCard.fills = [{{ type: "SOLID", color: cBgSurface }}];
  genCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(genCard);
  helperText(genCard, "Резервний дизель-генератор (Figma AI)", 14, "Bold", cDark, 24, 20);
  addImageRect(genCard, "generator", 24, 60, 372, 180, 8);

  // FRAME 04.1: DESIGN SYSTEM
  const fDesignSystem = figma.createFrame();
  fDesignSystem.name = "04.1_Design_System";
  fDesignSystem.resize(1600, 1100);
  fDesignSystem.x = 1600; fDesignSystem.y = 1050;
  fDesignSystem.fills = [{{ type: "SOLID", color: cWhite }}];

  helperText(fDesignSystem, "04.1 — Дизайн-система ChargeUA (Design Tokens & UI Kit)", 28, "Bold", cDark, 60, 40);

  // Colors
  helperText(fDesignSystem, "1. Колірні стилі (Color Tokens)", 18, "Bold", cDark, 60, 90);
  const colorSwatches = [
    {{ name: "Primary / #005EC9", col: cPrimary }},
    {{ name: "Primary Hover / #004BB5", col: cPrimaryHover }},
    {{ name: "Accent Cyan / #00E5FF", col: cCyan }},
    {{ name: "Dark Text / #0F172A", col: cDark }},
    {{ name: "Success Green / #047857", col: cSuccess }},
    {{ name: "Surface Bg / #F8FAFC", col: cBgSurface }},
    {{ name: "Border Slate / #E2E8F0", col: cBorder }}
  ];
  colorSwatches.forEach((sw, idx) => {{
    const sBox = figma.createFrame();
    sBox.resize(180, 80);
    sBox.x = 60 + idx * 210; sBox.y = 125;
    sBox.cornerRadius = 8;
    sBox.fills = [{{ type: "SOLID", color: sw.col }}];
    sBox.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesignSystem.appendChild(sBox);
    helperText(fDesignSystem, sw.name, 11, "Bold", cDark, 60 + idx * 210, 215);
  }});

  // Buttons Matrix
  helperText(fDesignSystem, "2. Матриця кнопок Button (3 типи × 6 станів × 2 розміри = 36 варіантів)", 18, "Bold", cDark, 60, 260);
  const btnTypes = [
    {{ name: "Primary (#005EC9)", fill: cPrimary, textCol: cWhite }},
    {{ name: "Accent CTA (#00E5FF)", fill: cCyan, textCol: cDark }},
    {{ name: "Secondary (Outline)", fill: cWhite, textCol: cDark, stroke: cBorder }}
  ];
  btnTypes.forEach((bt, tIdx) => {{
    ["Default", "Hover", "Active", "Focus", "Disabled", "Loading"].forEach((st, sIdx) => {{
      const bNode = figma.createFrame();
      bNode.resize(130, 42);
      bNode.x = 60 + sIdx * 145;
      bNode.y = 300 + tIdx * 70;
      bNode.cornerRadius = 8;
      bNode.fills = [{{ type: "SOLID", color: st === "Hover" ? cPrimaryHover : (st === "Disabled" ? cBorder : bt.fill) }}];
      if (bt.stroke) bNode.strokes = [{{ type: "SOLID", color: bt.stroke }}];
      fDesignSystem.appendChild(bNode);
      helperText(bNode, st === "Loading" ? "Очікування..." : st, 12, "Bold", st === "Disabled" ? cMuted : bt.textCol, 15, 12);
    }});
  }});

  // Components Section
  helperText(fDesignSystem, "3. Елементи форми, чіпи та картки станцій", 18, "Bold", cDark, 60, 540);

  // Input Field
  const inpField = figma.createFrame();
  inpField.resize(320, 50);
  inpField.x = 60; inpField.y = 580;
  inpField.cornerRadius = 8;
  inpField.fills = [{{ type: "SOLID", color: cWhite }}];
  inpField.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(inpField);
  helperText(inpField, "Введіть місто або назву станції...", 13, "Regular", cMuted, 16, 16);

  // Chips
  const chipLabels = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 З генератором"];
  chipLabels.forEach((cl, i) => {{
    const ch = figma.createFrame();
    ch.resize(140, 36);
    ch.x = 410 + i * 155; ch.y = 585;
    ch.cornerRadius = 18;
    ch.fills = [{{ type: "SOLID", color: i === 3 ? cSuccessBg : cBgSurface }}];
    ch.strokes = [{{ type: "SOLID", color: i === 3 ? cSuccess : cBorder }}];
    fDesignSystem.appendChild(ch);
    helperText(ch, cl, 12, "Bold", i === 3 ? cSuccess : cDark, 14, 9);
  }});

  // Card/Station Component
  const cStatComp = figma.createFrame();
  cStatComp.resize(440, 360);
  cStatComp.x = 60; cStatComp.y = 660;
  cStatComp.cornerRadius = 16;
  cStatComp.fills = [{{ type: "SOLID", color: cWhite }}];
  cStatComp.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(cStatComp);

  addImageRect(cStatComp, "hub_kyiv", 0, 0, 440, 180, 0);
  helperText(cStatComp, "Хаб «Київ-Поділ» · 120 кВт CCS2", 16, "Bold", cDark, 20, 200);
  helperText(cStatComp, "м. Київ, вул. Сагайдачного, 12 · 4 порти", 13, "Regular", cMuted, 20, 226);

  const statPill = figma.createFrame();
  statPill.resize(170, 28);
  statPill.x = 20; statPill.y = 260;
  statPill.cornerRadius = 6;
  statPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
  cStatComp.appendChild(statPill);
  helperText(statPill, "🔋 Працює від генератора", 11, "Bold", cSuccess, 10, 6);

  const bookBtn = figma.createFrame();
  bookBtn.resize(400, 42);
  bookBtn.x = 20; bookBtn.y = 300;
  bookBtn.cornerRadius = 8;
  bookBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  cStatComp.appendChild(bookBtn);
  helperText(bookBtn, "Забронювати конектор CCS2", 13, "Bold", cWhite, 100, 12);

  // Card/Testimonial Component
  const cRevComp = figma.createFrame();
  cRevComp.resize(440, 220);
  cRevComp.x = 540; cRevComp.y = 660;
  cRevComp.cornerRadius = 16;
  cRevComp.fills = [{{ type: "SOLID", color: cWhite }}];
  cRevComp.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesignSystem.appendChild(cRevComp);

  helperText(cRevComp, "★★★★★", 16, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 24, 24);
  helperText(cRevComp, "«Під час останнього блекауту у Києві ChargeUA буквально врятував поїздку. Забронював порт на Подолі — генератор працював без збоїв!»", 13, "Medium", cDark, 24, 56, 390);
  addImageRect(cRevComp, "av1", 24, 140, 48, 48, 24);
  helperText(cRevComp, "Олексій К.", 14, "Bold", cDark, 84, 144);
  helperText(cRevComp, "Водій Tesla Model Y · Київ", 12, "Regular", cMuted, 84, 166);

  // FRAME 10: OVERLAYS
  const fOverlays = figma.createFrame();
  fOverlays.name = "10_Overlays";
  fOverlays.resize(1440, 900);
  fOverlays.x = 3400; fOverlays.y = 1050;
  fOverlays.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fOverlays, "10 — Оверлеї прототипу (Interactions & Overlays)", 28, "Bold", cDark, 60, 40);
  helperText(fOverlays, "Мобільне навігаційне меню та модальне вікно підтвердження бронювання", 15, "Regular", cMuted, 60, 80);

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

  // Modal Dialog Overlay (with dim backdrop)
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
  helperText(mSuccessPill, "● Бронювання підтверджено", 11, "Bold", cSuccess, 10, 6);

  helperText(modalBox, "Дякуємо! Слот CCS2 заброньовано", 22, "Bold", cDark, 30, 75);
  helperText(modalBox, "Вам надіслано SMS із кодом доступу до станції «Київ-Поділ». Час резервування: 20 хвилин. Станція автоматично увімкне живлення після введення коду.", 14, "Regular", cMuted, 30, 115, 460);

  const mOkBtn = figma.createFrame();
  mOkBtn.resize(460, 48);
  mOkBtn.x = 30; mOkBtn.y = 260;
  mOkBtn.cornerRadius = 8;
  mOkBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
  modalBox.appendChild(mOkBtn);
  helperText(mOkBtn, "Зрозуміло, відкрити маршрут", 14, "Bold", cWhite, 130, 15);

  // ==========================================================================
  // РЯД 3: ПОВНІ ЕКРАНИ (DESKTOP, TABLET, MOBILE, CATALOG, DETAILS)
  // ==========================================================================

  // FRAME 05: FULL DESKTOP HOMEPAGE (1440 × 3800)
  const fDesktop = figma.createFrame();
  fDesktop.name = "05_Desktop";
  fDesktop.resize(1440, 3800);
  fDesktop.x = 0; fDesktop.y = 2300;
  fDesktop.fills = [{{ type: "SOLID", color: cWhite }}];

  // Top Bar
  const dTop = figma.createFrame();
  dTop.resize(1440, 40);
  dTop.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dTop);
  helperText(dTop, "● Мережа ChargeUA: 480+ станцій онлайн по Україні | 100% телеметрія в реальному часі", 12, "Medium", cWhite, 60, 12);
  helperText(dTop, "Гаряча лінія 24/7: 0 800 300 400 | UA", 12, "Medium", cWhite, 1150, 12);

  // Header
  const dHead = figma.createFrame();
  dHead.resize(1440, 76);
  dHead.y = 40;
  dHead.fills = [{{ type: "SOLID", color: cWhite }}];
  dHead.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dHead);
  addSvgNode(dHead, "logo", 60, 20, 36, 36);
  helperText(dHead, "ChargeUA", 22, "Bold", cPrimary, 105, 24);
  helperText(dHead, "Головна        Калькулятор        Карта станцій        Тарифи        Для бізнесу", 14, "Semi Bold", cDark, 420, 28);
  const dHeadCta = figma.createFrame();
  dHeadCta.resize(160, 42);
  dHeadCta.x = 1220; dHeadCta.y = 17;
  dHeadCta.cornerRadius = 8;
  dHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}];
  dHead.appendChild(dHeadCta);
  helperText(dHeadCta, "Знайти зарядку", 13, "Bold", cWhite, 26, 12);

  // Hero Section (with full car & station in center-right!)
  const dHero = figma.createFrame();
  dHero.resize(1440, 520);
  dHero.y = 116;
  dHero.fills = [{{ type: "SOLID", color: cWhite }}];
  fDesktop.appendChild(dHero);

  addImageRect(dHero, "hero", 540, 0, 900, 520, 0);

  helperText(dHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ", 11, "Bold", cPrimary, 60, 50);
  helperText(dHero, "Швидка та надійна зарядка\nелектромобілів по всій Україні", 42, "Bold", cDark, 60, 85);
  helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 60, 210, 500);

  const dHeroBtn1 = figma.createFrame();
  dHeroBtn1.resize(230, 48);
  dHeroBtn1.x = 60; dHeroBtn1.y = 290;
  dHeroBtn1.cornerRadius = 8;
  dHeroBtn1.fills = [{{ type: "SOLID", color: cPrimary }}];
  dHero.appendChild(dHeroBtn1);
  helperText(dHeroBtn1, "Розрахувати зарядку →", 14, "Bold", cWhite, 32, 15);

  const dHeroBtn2 = figma.createFrame();
  dHeroBtn2.resize(180, 48);
  dHeroBtn2.x = 310; dHeroBtn2.y = 290;
  dHeroBtn2.cornerRadius = 8;
  dHeroBtn2.fills = [{{ type: "SOLID", color: cWhite }}];
  dHeroBtn2.strokes = [{{ type: "SOLID", color: cBorder }}];
  dHero.appendChild(dHeroBtn2);
  helperText(dHeroBtn2, "Знайти на карті", 14, "Semi Bold", cDark, 30, 15);

  // Chips
  const heroChips = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 З генератором"];
  heroChips.forEach((ch, idx) => {{
    const chBox = figma.createFrame();
    chBox.resize(130, 32);
    chBox.x = 60 + idx * 140; chBox.y = 370;
    chBox.cornerRadius = 16;
    chBox.fills = [{{ type: "SOLID", color: idx === 3 ? cSuccessBg : cBgSurface }}];
    chBox.strokes = [{{ type: "SOLID", color: idx === 3 ? cSuccess : cBorder }}];
    dHero.appendChild(chBox);
    helperText(chBox, ch, 11, "Bold", idx === 3 ? cSuccess : cDark, 12, 8);
  }});

  // Benefit Strip
  const dStrip = figma.createFrame();
  dStrip.resize(1440, 150);
  dStrip.y = 636;
  dStrip.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dStrip.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dStrip);

  const stripItems = [
    {{ svg: "calc", title: "Точний калькулятор витрат", desc: "Автоматичний підбір моделі авто та тарифу" }},
    {{ svg: "loc", title: "Live-карта 480+ станцій", desc: "Актуальний статус зайнятості та світла" }},
    {{ svg: "info", title: "100% Енергонезалежність", desc: "Робота від генераторів у блекаути" }}
  ];
  stripItems.forEach((st, idx) => {{
    const card = figma.createFrame();
    card.resize(400, 100);
    card.x = 60 + idx * 450; card.y = 25;
    card.cornerRadius = 12;
    card.fills = [{{ type: "SOLID", color: cWhite }}];
    card.strokes = [{{ type: "SOLID", color: cBorder }}];
    dStrip.appendChild(card);
    addSvgNode(card, st.svg, 20, 25, 48, 48);
    helperText(card, st.title, 15, "Bold", cDark, 80, 26);
    helperText(card, st.desc, 12, "Regular", cMuted, 80, 50);
  }});

  // Interactive Calculator Section
  const dCalcSec = figma.createFrame();
  dCalcSec.resize(1320, 360);
  dCalcSec.x = 60; dCalcSec.y = 820;
  dCalcSec.cornerRadius = 16;
  dCalcSec.fills = [{{ type: "SOLID", color: cWhite }}];
  dCalcSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dCalcSec);

  helperText(dCalcSec, "Калькулятор вартості зарядки та вибору тарифу", 24, "Bold", cDark, 40, 40);
  helperText(dCalcSec, "Розрахуйте точну вартість сесії для вашого електрокара перед виїздом", 14, "Regular", cMuted, 40, 75);

  helperText(dCalcSec, "1. Оберіть модель авто:", 13, "Bold", cDark, 40, 125);
  const cars = ["Tesla Model Y", "Volkswagen ID.4", "Nissan Leaf (62 kWh)", "Hyundai Ioniq 5"];
  cars.forEach((c, idx) => {{
    const cPill = figma.createFrame();
    cPill.resize(160, 38);
    cPill.x = 40 + idx * 175; cPill.y = 155;
    cPill.cornerRadius = 8;
    cPill.fills = [{{ type: "SOLID", color: idx === 1 ? cPrimary : cBgSurface }}];
    if (idx !== 1) cPill.strokes = [{{ type: "SOLID", color: cBorder }}];
    dCalcSec.appendChild(cPill);
    helperText(cPill, c, 12, "Bold", idx === 1 ? cWhite : cDark, 14, 11);
  }});

  // Result card inside calc
  const calcRes = figma.createFrame();
  calcRes.resize(480, 160);
  calcRes.x = 780; calcRes.y = 140;
  calcRes.cornerRadius = 12;
  calcRes.fills = [{{ type: "SOLID", color: cBgSurface }}];
  calcRes.strokes = [{{ type: "SOLID", color: cPrimary }}];
  dCalcSec.appendChild(calcRes);

  helperText(calcRes, "Орієнтовний розрахунок (20% → 80%):", 13, "Bold", cDark, 24, 20);
  helperText(calcRes, "Час на 120 кВт DC: ~28 хв", 15, "Semi Bold", cPrimary, 24, 50);
  helperText(calcRes, "652.50 ₴ (14.50 ₴/кВт·год)", 26, "Bold", cDark, 24, 80);
  helperText(calcRes, "Економія проти бензину: ~1 420 ₴", 12, "Bold", cSuccess, 24, 120);

  // Popular Stations Grid (with real photos)
  helperText(fDesktop, "Популярні зарядні хаби мережі", 28, "Bold", cDark, 60, 1230);
  helperText(fDesktop, "Вільні швидкісні станції з гарантованим енергозабезпеченням", 15, "Regular", cMuted, 60, 1270);

  const stationsData = [
    {{ img: "hub_kyiv", title: "Хаб «Київ-Поділ» · 120 кВт CCS2", addr: "м. Київ, вул. Сагайдачного, 12", gen: true, price: "14.50 ₴" }},
    {{ img: "hub_lviv", title: "Хаб «Арена Львів» · 160 кВт CCS2", addr: "м. Львів, вул. Стрийська, 199", gen: true, price: "15.00 ₴" }},
    {{ img: "generator", title: "ЕкоХаб «Тернопіль-Центр» · 75 кВт", addr: "м. Тернопіль, вул. Руська, 8", gen: true, price: "13.80 ₴" }}
  ];

  stationsData.forEach((st, idx) => {{
    const sCard = figma.createFrame();
    sCard.resize(410, 360);
    sCard.x = 60 + idx * 455; sCard.y = 1320;
    sCard.cornerRadius = 16;
    sCard.fills = [{{ type: "SOLID", color: cWhite }}];
    sCard.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesktop.appendChild(sCard);

    addImageRect(sCard, st.img, 0, 0, 410, 190, 0);
    helperText(sCard, st.title, 16, "Bold", cDark, 20, 210);
    helperText(sCard, st.addr, 12, "Regular", cMuted, 20, 235);

    const sPill = figma.createFrame();
    sPill.resize(160, 26);
    sPill.x = 20; sPill.y = 265;
    sPill.cornerRadius = 6;
    sPill.fills = [{{ type: "SOLID", color: cSuccessBg }}];
    sCard.appendChild(sPill);
    helperText(sPill, "🔋 Генератор ON · Вільний", 11, "Bold", cSuccess, 10, 5);

    const sBtn = figma.createFrame();
    sBtn.resize(370, 40);
    sBtn.x = 20; sBtn.y = 305;
    sBtn.cornerRadius = 8;
    sBtn.fills = [{{ type: "SOLID", color: cPrimary }}];
    sCard.appendChild(sBtn);
    helperText(sBtn, "Забронювати конектор", 13, "Bold", cWhite, 110, 11);
  }});

  // Blackout Energy Independence Section
  const dGenSec = figma.createFrame();
  dGenSec.resize(1320, 340);
  dGenSec.x = 60; dGenSec.y = 1730;
  dGenSec.cornerRadius = 16;
  dGenSec.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dGenSec);

  addImageRect(dGenSec, "generator", 740, 20, 550, 300, 12);
  helperText(dGenSec, "ЕНЕРГОНЕЗАЛЕЖНІСТЬ 24/7", 12, "Bold", cCyan, 40, 40);
  helperText(dGenSec, "Заряджайте авто навіть\nпід час повних блекаутів", 32, "Bold", cWhite, 40, 70);
  helperText(dGenSec, "Кожен наш ключовий хаб обладнано промисловим дизель-генератором потужністю 150–250 кВт. Автоматичний перехід на резервне живлення за 8 секунд гарантує безперебійну зарядку.", 14, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 40, 160, 640);

  const genBadge = figma.createFrame();
  genBadge.resize(240, 44);
  genBadge.x = 40; genBadge.y = 250;
  genBadge.cornerRadius = 8;
  genBadge.fills = [{{ type: "SOLID", color: cCyan }}];
  dGenSec.appendChild(genBadge);
  helperText(genBadge, "Показати станції зі світлом", 13, "Bold", cDark, 26, 14);

  // Video Demonstration Section
  const dVidSec = figma.createFrame();
  dVidSec.resize(1320, 360);
  dVidSec.x = 60; dVidSec.y = 2110;
  dVidSec.cornerRadius = 16;
  dVidSec.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dVidSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dVidSec);

  addImageRect(dVidSec, "video", 40, 40, 580, 280, 12);
  helperText(dVidSec, "ВІДЕОДЕМОНСТРАЦІЯ РОБОТИ СЕРВІСУ", 12, "Bold", cPrimary, 660, 50);
  helperText(dVidSec, "Як зарядитися за 3 кроки:\nвід пошуку до повної батареї", 28, "Bold", cDark, 660, 80);
  helperText(dVidSec, "Подивіться коротке 45-секундне відео про те, як працює алгоритм підбору хабу, розрахунок вартості та автоматичне підключення конектора CCS2.", 14, "Regular", cMuted, 660, 165, 580);

  // How it works / Steps
  const dStepsSec = figma.createFrame();
  dStepsSec.resize(1320, 240);
  dStepsSec.x = 60; dStepsSec.y = 2510;
  dStepsSec.cornerRadius = 16;
  dStepsSec.fills = [{{ type: "SOLID", color: cWhite }}];
  dStepsSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dStepsSec);

  const stepsList = [
    {{ num: "1", title: "Знайдіть вільну станцію", desc: "Фільтруйте за потужністю, конектором або наявністю генератора на карті." }},
    {{ num: "2", title: "Підключіть конектор CCS2", desc: "Вставте кабель у роз'єм — індикатор загориться зеленим кольором." }},
    {{ num: "3", title: "Оплатіть у 1 клік", desc: "Apple Pay, Google Pay або картка без жодних депозитів чи переплат." }}
  ];
  stepsList.forEach((sp, idx) => {{
    const sCol = figma.createFrame();
    sCol.resize(380, 180);
    sCol.x = 40 + idx * 430; sCol.y = 30;
    dStepsSec.appendChild(sCol);

    const sCircle = figma.createFrame();
    sCircle.resize(44, 44);
    sCircle.cornerRadius = 22;
    sCircle.fills = [{{ type: "SOLID", color: cPrimary }}];
    sCol.appendChild(sCircle);
    helperText(sCircle, sp.num, 18, "Bold", cWhite, 16, 11);

    helperText(sCol, sp.title, 16, "Bold", cDark, 60, 10);
    helperText(sCol, sp.desc, 13, "Regular", cMuted, 60, 42, 310);
  }});

  // Testimonials with Avatars
  helperText(fDesktop, "Відгуки реальних водіїв", 28, "Bold", cDark, 60, 2790);
  helperText(fDesktop, "Що кажуть власники електрокарів про сервіс ChargeUA", 15, "Regular", cMuted, 60, 2830);

  const reviewsList = [
    {{ av: "av1", name: "Олексій К.", role: "Водій Tesla Model Y · Київ", text: "Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, кава гаряча, станція стабільна. Найкращий сервіс!" }},
    {{ av: "av2", name: "Олена М.", role: "Водійка Nissan Leaf · Львів", text: "Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів." }},
    {{ av: "av3", name: "Сергій В.", role: "Керівник автопарку електробусів", text: "Для комерційного флоту функція бронювання слотів — це знахідка. Жодних простоїв та черг на трасі Київ-Львів." }}
  ];

  reviewsList.forEach((rv, idx) => {{
    const rCard = figma.createFrame();
    rCard.resize(410, 230);
    rCard.x = 60 + idx * 455; rCard.y = 2880;
    rCard.cornerRadius = 16;
    rCard.fills = [{{ type: "SOLID", color: cWhite }}];
    rCard.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesktop.appendChild(rCard);

    helperText(rCard, "★★★★★", 16, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 24, 20);
    helperText(rCard, `«${{rv.text}}»`, 13, "Medium", cDark, 24, 50, 360);
    addImageRect(rCard, rv.av, 24, 155, 48, 48, 24);
    helperText(rCard, rv.name, 14, "Bold", cDark, 84, 158);
    helperText(rCard, rv.role, 11, "Regular", cMuted, 84, 180);
  }});

  // Contact / B2B Form Section
  const dFormSec = figma.createFrame();
  dFormSec.resize(1320, 280);
  dFormSec.x = 60; dFormSec.y = 3150;
  dFormSec.cornerRadius = 16;
  dFormSec.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dFormSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dFormSec);

  helperText(dFormSec, "Маєте локацію? Встановіть станцію ChargeUA", 24, "Bold", cDark, 40, 40);
  helperText(dFormSec, "Отримуйте стабільний пасивний дохід від зарядки авто ваших клієнтів", 14, "Regular", cMuted, 40, 75);

  const inp1 = figma.createFrame(); inp1.resize(360, 46); inp1.x = 40; inp1.y = 125; inp1.cornerRadius = 8; inp1.fills = [{{ type: "SOLID", color: cWhite }}]; inp1.strokes = [{{ type: "SOLID", color: cBorder }}]; dFormSec.appendChild(inp1);
  helperText(inp1, "Ваше ім'я", 13, "Regular", cMuted, 16, 14);

  const inp2 = figma.createFrame(); inp2.resize(360, 46); inp2.x = 430; inp2.y = 125; inp2.cornerRadius = 8; inp2.fills = [{{ type: "SOLID", color: cWhite }}]; inp2.strokes = [{{ type: "SOLID", color: cBorder }}]; dFormSec.appendChild(inp2);
  helperText(inp2, "Номер телефону (+380...)", 13, "Regular", cMuted, 16, 14);

  const inp3 = figma.createFrame(); inp3.resize(360, 46); inp3.x = 820; inp3.y = 125; inp3.cornerRadius = 8; inp3.fills = [{{ type: "SOLID", color: cWhite }}]; inp3.strokes = [{{ type: "SOLID", color: cBorder }}]; dFormSec.appendChild(inp3);
  helperText(inp3, "Місто та адреса об'єкта", 13, "Regular", cMuted, 16, 14);

  const subBtn = figma.createFrame(); subBtn.resize(280, 48); subBtn.x = 40; subBtn.y = 195; subBtn.cornerRadius = 8; subBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; dFormSec.appendChild(subBtn);
  helperText(subBtn, "Подати заявку на монтаж", 14, "Bold", cWhite, 45, 15);

  // Footer
  const dFooter = figma.createFrame();
  dFooter.resize(1440, 320);
  dFooter.y = 3480;
  dFooter.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dFooter);

  addSvgNode(dFooter, "logo", 60, 40, 36, 36);
  helperText(dFooter, "ChargeUA", 22, "Bold", cWhite, 105, 44);
  helperText(dFooter, "Національний агрегатор та веб-помічник зарядної інфраструктури України.", 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 60, 90, 320);

  const fCols = [
    {{ title: "Навігація", links: ["Головна", "Калькулятор", "Карта станцій", "Тарифи"] }},
    {{ title: "Для бізнесу", links: ["Встановити хаб", "B2B-калькулятор", "Партнерство", "Резервне живлення"] }},
    {{ title: "Контакти", links: ["0 800 300 400", "support@charge.ua", "м. Київ, вул. Подолу, 12", "Telegram Бот"] }}
  ];
  fCols.forEach((fc, idx) => {{
    helperText(dFooter, fc.title, 15, "Bold", cWhite, 480 + idx * 260, 44);
    fc.links.forEach((lk, i) => helperText(dFooter, lk, 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 480 + idx * 260, 80 + i * 28));
  }});

  helperText(dFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 60, 260);

  // FRAME 06: FULL TABLET (768 × 3400)
  const fTablet = figma.createFrame();
  fTablet.name = "06_Tablet";
  fTablet.resize(768, 3400);
  fTablet.x = 1600; fTablet.y = 2300;
  fTablet.fills = [{{ type: "SOLID", color: cWhite }}];

  // Header Tablet
  const tHead = figma.createFrame(); tHead.resize(768, 70); tHead.fills = [{{ type: "SOLID", color: cWhite }}]; tHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tHead);
  addSvgNode(tHead, "logo", 30, 20, 30, 30);
  helperText(tHead, "ChargeUA", 20, "Bold", cPrimary, 70, 24);
  helperText(tHead, "☰", 24, "Bold", cDark, 710, 20);

  // Hero Tablet
  const tHero = figma.createFrame(); tHero.resize(768, 480); tHero.y = 70; tHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; fTablet.appendChild(tHero);
  addImageRect(tHero, "hero", 220, 0, 548, 480, 0);
  helperText(tHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР", 10, "Bold", cPrimary, 30, 35);
  helperText(tHero, "Швидка та надійна\nзарядка по Україні", 32, "Bold", cDark, 30, 65);
  helperText(tHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди навіть під час блекаутів.", 14, "Regular", cMuted, 30, 160, 360);

  const tBtn1 = figma.createFrame(); tBtn1.resize(200, 44); tBtn1.x = 30; tBtn1.y = 235; tBtn1.cornerRadius = 8; tBtn1.fills = [{{ type: "SOLID", color: cPrimary }}]; tHero.appendChild(tBtn1);
  helperText(tBtn1, "Розрахувати зарядку", 13, "Bold", cWhite, 25, 14);

  // Calc Tablet
  const tCalc = figma.createFrame(); tCalc.resize(708, 300); tCalc.x = 30; tCalc.y = 580; tCalc.cornerRadius = 14; tCalc.fills = [{{ type: "SOLID", color: cWhite }}]; tCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tCalc);
  helperText(tCalc, "Калькулятор вартості зарядки", 18, "Bold", cDark, 24, 24);
  helperText(tCalc, "Volkswagen ID.4 (77 кВт·год) · 20% → 80%", 14, "Semi Bold", cPrimary, 24, 56);
  helperText(tCalc, "652.50 ₴ · ~28 хв на DC 120 кВт", 22, "Bold", cDark, 24, 90);

  // Stations Tablet (2 cards stacked)
  helperText(fTablet, "Популярні зарядні хаби", 22, "Bold", cDark, 30, 920);
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const tSc = figma.createFrame(); tSc.resize(708, 320); tSc.x = 30; tSc.y = 960 + idx * 340; tSc.cornerRadius = 14; tSc.fills = [{{ type: "SOLID", color: cWhite }}]; tSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tSc);
    addImageRect(tSc, st.img, 0, 0, 708, 180, 0);
    helperText(tSc, st.title, 16, "Bold", cDark, 20, 200);
    helperText(tSc, st.addr, 13, "Regular", cMuted, 20, 226);
  }});

  // FRAME 07: FULL MOBILE (390 × 3200)
  const fMobile = figma.createFrame();
  fMobile.name = "07_Mobile";
  fMobile.resize(390, 3200);
  fMobile.x = 2500; fMobile.y = 2300;
  fMobile.fills = [{{ type: "SOLID", color: cWhite }}];

  // Mobile Topbar
  const mTop = figma.createFrame(); mTop.resize(390, 34); mTop.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mTop);
  helperText(mTop, "● 480+ станцій онлайн | Генератори ON", 10, "Medium", cWhite, 16, 9);

  // Mobile Header
  const mHead = figma.createFrame(); mHead.resize(390, 60); mHead.y = 34; mHead.fills = [{{ type: "SOLID", color: cWhite }}]; mHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mHead);
  addSvgNode(mHead, "logo", 16, 16, 28, 28);
  helperText(mHead, "ChargeUA", 18, "Bold", cPrimary, 52, 19);
  helperText(mHead, "☰", 22, "Bold", cDark, 350, 16);

  // Mobile Hero
  const mHero = figma.createFrame(); mHero.resize(390, 460); mHero.y = 94; mHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; fMobile.appendChild(mHero);
  helperText(mHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР", 9, "Bold", cPrimary, 20, 20);
  helperText(mHero, "Заряджайте авто\nбез стресу", 28, "Bold", cDark, 20, 45);
  helperText(mHero, "Усі мережі на одній карті з фільтром генераторів у блекаути.", 13, "Regular", cMuted, 20, 125, 350);

  addImageRect(mHero, "hero", 20, 175, 350, 190, 12);

  const mBtn = figma.createFrame(); mBtn.resize(350, 44); mBtn.x = 20; mBtn.y = 385; mBtn.cornerRadius = 8; mBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; mHero.appendChild(mBtn);
  helperText(mBtn, "Розрахувати зарядку →", 13, "Bold", cWhite, 95, 13);

  // Mobile Calc
  const mCalc = figma.createFrame(); mCalc.resize(350, 240); mCalc.x = 20; mCalc.y = 580; mCalc.cornerRadius = 14; mCalc.fills = [{{ type: "SOLID", color: cWhite }}]; mCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mCalc);
  helperText(mCalc, "Калькулятор витрат", 16, "Bold", cDark, 16, 16);
  helperText(mCalc, "VW ID.4 · 20% → 80%", 13, "Semi Bold", cPrimary, 16, 44);
  helperText(mCalc, "652.50 ₴ (~28 хв)", 20, "Bold", cDark, 16, 75);

  // Mobile Station Card
  const mSc = figma.createFrame(); mSc.resize(350, 320); mSc.x = 20; mSc.y = 850; mSc.cornerRadius = 14; mSc.fills = [{{ type: "SOLID", color: cWhite }}]; mSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSc);
  addImageRect(mSc, "hub_kyiv", 0, 0, 350, 160, 0);
  helperText(mSc, "Хаб «Київ-Поділ» · 120 кВт", 15, "Bold", cDark, 16, 175);
  helperText(mSc, "Сагайдачного, 12 · 4 порти", 12, "Regular", cMuted, 16, 200);

  const mSb = figma.createFrame(); mSb.resize(318, 40); mSb.x = 16; mSb.y = 265; mSb.cornerRadius = 8; mSb.fills = [{{ type: "SOLID", color: cPrimary }}]; mSc.appendChild(mSb);
  helperText(mSb, "Забронювати CCS2", 12, "Bold", cWhite, 95, 12);

  // FRAME 08: CATALOG MAP
  const fCatalog = figma.createFrame();
  fCatalog.name = "08_Catalog_Map";
  fCatalog.resize(1440, 1600);
  fCatalog.x = 3000; fCatalog.y = 2300;
  fCatalog.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fCatalog, "Карта та каталог зарядних станцій ChargeUA", 32, "Bold", cDark, 60, 40);
  helperText(fCatalog, "Повний перелік 480+ перевірених станцій з живою телеметрією", 16, "Regular", cMuted, 60, 85);

  // Search and Filter Bar
  const sBar = figma.createFrame(); sBar.resize(1320, 60); sBar.x = 60; sBar.y = 130; sBar.cornerRadius = 12; sBar.fills = [{{ type: "SOLID", color: cWhite }}]; sBar.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(sBar);
  helperText(sBar, "🔍 Пошук за містом, адресою або назвою хабу...", 14, "Regular", cMuted, 24, 20);

  // 4 Cards Grid
  stationsData.concat([stationsData[0]]).forEach((st, idx) => {{
    const row = Math.floor(idx / 2);
    const col = idx % 2;
    const cd = figma.createFrame(); cd.resize(640, 340); cd.x = 60 + col * 680; cd.y = 220 + row * 370; cd.cornerRadius = 16; cd.fills = [{{ type: "SOLID", color: cWhite }}]; cd.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(cd);
    addImageRect(cd, st.img, 0, 0, 640, 180, 0);
    helperText(cd, st.title, 18, "Bold", cDark, 24, 200);
    helperText(cd, st.addr, 13, "Regular", cMuted, 24, 230);
  }});

  // FRAME 09: STATION DETAILS
  const fDetails = figma.createFrame();
  fDetails.name = "09_Station_Details";
  fDetails.resize(1440, 1600);
  fDetails.x = 4600; fDetails.y = 2300;
  fDetails.fills = [{{ type: "SOLID", color: cWhite }}];

  addImageRect(fDetails, "hub_kyiv", 60, 40, 1320, 420, 16);
  helperText(fDetails, "Хаб «Київ-Поділ» · 120 кВт CCS2", 34, "Bold", cDark, 60, 490);
  helperText(fDetails, "м. Київ, вул. Петра Сагайдачного, 12 · Оператор: ChargeUA Network", 16, "Regular", cMuted, 60, 535);

  const detCard = figma.createFrame(); detCard.resize(800, 240); detCard.x = 60; detCard.y = 590; detCard.cornerRadius = 14; detCard.fills = [{{ type: "SOLID", color: cBgSurface }}]; detCard.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detCard);
  helperText(detCard, "Характеристики станції та тарифи:", 16, "Bold", cDark, 24, 24);
  helperText(detCard, "• Потужність: 120 кВт DC (швидка зарядка)", 14, "Medium", cDark, 24, 60);
  helperText(detCard, "• Конектори: 2x CCS2, 1x CHAdeMO, 1x Type 2 (22 кВт)", 14, "Medium", cDark, 24, 90);
  helperText(detCard, "• Тариф: 14.50 ₴ / кВт·год (безкоштовне паркування 1 год)", 14, "Medium", cPrimary, 24, 120);
  helperText(detCard, "• Резервне живлення: Промисловий дизель-генератор 160 кВт (100% Uptime)", 14, "Bold", cSuccess, 24, 150);

  const detBookBtn = figma.createFrame(); detBookBtn.resize(480, 54); detBookBtn.x = 900; detBookBtn.y = 590; detBookBtn.cornerRadius = 10; detBookBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; fDetails.appendChild(detBookBtn);
  helperText(detBookBtn, "Забронювати слот на 20 хвилин", 16, "Bold", cWhite, 100, 17);

  // Zoom into view
  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("🎉 Готово! Усі 11 фреймів ChargeUA, вектори та зображення успішно згенеровані!");
}}

run();
"""

with open(OUT_JS, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {OUT_JS} ({len(js_content)} bytes)")
