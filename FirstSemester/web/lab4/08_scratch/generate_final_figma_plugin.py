# -*- coding: utf-8 -*-
"""
Full Generator for ChargeUA Figma Builder Plugin.
Builds complete, production-grade, pixel-perfect frames:
  00_Cover (1440x900)
  01_User_Flow (1440x900)
  02_Sitemap (1440x900)
  03_Wireframes (1440x900)
  04.0_Brand_Assets_LR3 (1440x900)
  04.1_Design_System (1440x1100)
  05_Desktop (1440x3650) - Full page, car+hub hero aligned, NO video in steps, clean 3-step cards, reviews, lead form, footer
  06_Tablet (768x3350) - Complete responsive page, all sections, NO white voids
  07_Mobile (390x3250) - Complete mobile page, all stations, generator, steps, reviews, form, footer, sticky bottom nav
  08_Catalog_Map (1440x1720) - Full header, search & filter chips, 6 station cards with telemetry, pagination, footer
  09_Station_Details (1440x1650) - Full header, breadcrumbs, photo banner, 4 ports telemetry grid, specs, amenities, tariffs, route assistant, footer
  10_Overlays (1440x900) - Mobile drawer & pure route assistant modal (zero booking)
"""

import os, io, base64
from PIL import Image

BASE_DIR = r"d:\Studing\SecondYear\FirstSemester\web\lab4"
MAT_DIR = os.path.join(BASE_DIR, "materials")
OUT_PLUGIN = os.path.join(BASE_DIR, "05_figma_exports", "figma_builder_plugin.js")
OUT_CODE = os.path.join(BASE_DIR, "05_figma_exports", "charge", "code.js")

def read_svg(filename):
    p = os.path.join(MAT_DIR, filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read().replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def get_b64_jpeg(filename, max_w, max_h, quality=75):
    p = os.path.join(MAT_DIR, filename)
    im = Image.open(p).convert("RGB")
    im.thumbnail((max_w, max_h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")

print("Processing SVG assets...")
svg_logo = read_svg("Logo.svg")
svg_calc = read_svg("Calculator.svg")
svg_loc = read_svg("Location.svg")
svg_info = read_svg("Information.svg")

print("Processing Image assets (High Definition 1280x720 / q85)...")
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
b64_map_lviv = get_b64_jpeg("map_lviv.jpg", 1280, 720, 85)

print("Writing JS generator...")

js_code = f"""// ==============================================================================
// ChargeUA Figma Builder Plugin (Лабораторна робота №4)
// Автор: Лемішка Андрій (ПП-24)
// Повна генерація всіх 12 фреймів сайту ChargeUA
// Чистий інтерфейс, векторні SVG, фотоматеріали, повний адаптив, без бронювання
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
  hub_obolon: "{b64_hub_obolon}",
  hub_odesa: "{b64_hub_odesa}",
  hub_dnipro: "{b64_hub_dnipro}",
  hub_zhytomyr: "{b64_hub_zhytomyr}",
  banner_ai: "{b64_banner_ai}",
  video_tutorial: "{b64_video_tutorial}",
  generator: "{b64_generator}",
  cable: "{b64_cable}",
  video: "{b64_video}",
  banner: "{b64_banner}",
  av1: "{b64_av1}",
  av2: "{b64_av2}",
  av3: "{b64_av3}",
  map_lviv: "{b64_map_lviv}"
}};

const SVG_ASSETS = {{
  logo: `{svg_logo}`,
  calc: `{svg_calc}`,
  loc: `{svg_loc}`,
  info: `{svg_info}`
}};

async function run() {{
  figma.notify("🧹 Очищення старих та накладених фреймів ChargeUA...");
  const toRemove = [];
  for (const child of figma.currentPage.children) {{
    if (
      /^(0[1-9]|1[0-2])_/.test(child.name) ||
      child.name.includes("ChargeUA") ||
      child.name.includes("Desktop") ||
      child.name.includes("Tablet") ||
      child.name.includes("Mobile") ||
      child.name.includes("Catalog") ||
      child.name.includes("Station") ||
      child.name.includes("Wireframe") ||
      child.name.includes("Design_System") ||
      child.name.includes("Brand_Assets") ||
      child.name.includes("Overlays")
    ) {{
      toRemove.push(child);
    }}
  }}
  toRemove.forEach(n => n.remove());
  if (toRemove.length > 0) {{
    figma.notify(`🧹 Очищено ${{toRemove.length}} старих / накладених фреймів! Створюємо чисті фрейми...`);
  }}

  try {{
    await figma.loadFontAsync({{ family: "Inter", style: "Regular" }});
    await figma.loadFontAsync({{ family: "Inter", style: "Medium" }});
    await figma.loadFontAsync({{ family: "Inter", style: "Semi Bold" }});
    await figma.loadFontAsync({{ family: "Inter", style: "Bold" }});
  }} catch (e) {{
    console.warn("Could not load Inter, fallback to default font", e);
  }}

  const cPrimary = {{ r: 2/255, g: 132/255, b: 199/255 }};       // #0284C7
  const cPrimaryDark = {{ r: 3/255, g: 105/255, b: 161/255 }};   // #0369A1
  const cDark = {{ r: 15/255, g: 23/255, b: 42/255 }};           // #0F172A
  const cMuted = {{ r: 100/255, g: 116/255, b: 139/255 }};       // #64748B
  const cBorder = {{ r: 226/255, g: 232/255, b: 240/255 }};      // #E2E8F0
  const cBgSurface = {{ r: 248/255, g: 250/255, b: 252/255 }};   // #F8FAFC
  const cWhite = {{ r: 1, g: 1, b: 1 }};
  const cSuccess = {{ r: 22/255, g: 163/255, b: 74/255 }};       // #16A34A
  const cSuccessBg = {{ r: 240/255, g: 253/255, b: 244/255 }};   // #F0FDF4
  const cWarning = {{ r: 217/255, g: 119/255, b: 6/255 }};       // #D97706
  const cWarningBg = {{ r: 254/255, g: 243/255, b: 199/255 }};   // #FEF3C7

  const imgHashes = {{}};
  for (const [key, b64] of Object.entries(ASSETS_B64)) {{
    try {{
      const bytes = base64ToBytes(b64);
      const img = figma.createImage(bytes);
      imgHashes[key] = img.hash;
    }} catch (e) {{
      console.warn("Failed creating image for key:", key, e);
    }}
  }}

  function helperText(parent, str, size, weight, color, x, y, wrapWidth = null) {{
    const t = figma.createText();
    t.fontName = {{ family: "Inter", style: weight }};
    t.characters = str;
    t.fontSize = size;
    t.fills = [{{ type: "SOLID", color: color }}];
    t.x = x;
    t.y = y;
    if (wrapWidth) {{
      t.textAutoResize = "HEIGHT";
      t.resize(wrapWidth, t.height);
    }}
    parent.appendChild(t);
    return t;
  }}

  function addImageRect(parent, imgKey, x, y, w, h, radius = 0) {{
    const rect = figma.createRectangle();
    rect.resize(w, h);
    rect.x = x;
    rect.y = y;
    rect.cornerRadius = radius;
    if (imgHashes[imgKey]) {{
      rect.fills = [{{ type: "IMAGE", scaleMode: "FILL", imageHash: imgHashes[imgKey] }}];
    }} else {{
      rect.fills = [{{ type: "SOLID", color: {{ r: 0.9, g: 0.9, b: 0.9 }} }}];
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
        if (typeof node.rescale === "function") {{
          node.rescale(targetWidth / node.width);
        }} else if (typeof node.resize === "function") {{
          node.resize(targetWidth, targetHeight);
        }}
      }}
      parent.appendChild(node);
      return node;
    }} catch (e) {{
      console.warn("Error inserting SVG:", svgKey, e);
      return null;
    }}
  }}

  async function linkNodes(sourceNode, targetNode, navType = "NAVIGATE") {{
    if (!sourceNode || !targetNode || !targetNode.id) return;
    try {{
      const reaction = {{
        trigger: {{ type: "ON_CLICK" }},
        action: {{
          type: "NODE",
          destinationId: targetNode.id,
          navigation: navType,
          transition: {{
            type: "DISSOLVE",
            duration: 0.25,
            easing: {{ type: "EASE_IN_AND_OUT" }}
          }},
          resetScrollPosition: false
        }}
      }};
      if (typeof sourceNode.setReactionsAsync === "function") {{
        await sourceNode.setReactionsAsync([reaction]);
      }} else {{
        sourceNode.reactions = [reaction];
      }}
    }} catch (e) {{
      console.warn("linkNodes error:", e);
    }}
  }}

  async function linkOverlay(sourceNode, overlayNode) {{
    if (!sourceNode || !overlayNode || !overlayNode.id) return;
    try {{
      const reaction = {{
        trigger: {{ type: "ON_CLICK" }},
        action: {{
          type: "NODE",
          destinationId: overlayNode.id,
          navigation: "OVERLAY",
          transition: {{
            type: "DISSOLVE",
            duration: 0.25,
            easing: {{ type: "EASE_IN_AND_OUT" }}
          }}
        }}
      }};
      if (typeof sourceNode.setReactionsAsync === "function") {{
        await sourceNode.setReactionsAsync([reaction]);
      }} else {{
        sourceNode.reactions = [reaction];
      }}
    }} catch (e) {{
      console.warn("linkOverlay error:", e);
    }}
  }}

  async function linkScroll(sourceNode, targetNode) {{
    if (!sourceNode || !targetNode || !targetNode.id) return;
    try {{
      const reaction = {{
        trigger: {{ type: "ON_CLICK" }},
        action: {{
          type: "NODE",
          destinationId: targetNode.id,
          navigation: "SCROLL_TO",
          transition: {{
            type: "SMART_ANIMATE",
            duration: 0.35,
            easing: {{ type: "EASE_IN_AND_OUT" }}
          }}
        }}
      }};
      if (typeof sourceNode.setReactionsAsync === "function") {{
        await sourceNode.setReactionsAsync([reaction]);
      }} else {{
        sourceNode.reactions = [reaction];
      }}
    }} catch (e) {{
      console.warn("linkScroll error:", e);
    }}
  }}

  async function linkClose(sourceNode) {{
    if (!sourceNode) return;
    try {{
      const reaction = {{
        trigger: {{ type: "ON_CLICK" }},
        action: {{ type: "CLOSE" }}
      }};
      if (typeof sourceNode.setReactionsAsync === "function") {{
        await sourceNode.setReactionsAsync([reaction]);
      }} else {{
        sourceNode.reactions = [reaction];
      }}
    }} catch (e) {{
      console.warn("linkClose error:", e);
    }}
  }}

  const stationsData = [
    {{ title: "Хаб «Київ-Поділ» · 120 кВт CCS2", addr: "вул. Сагайдачного, 12 · 4 порти (3 вільні)", img: "hub_kyiv", gen: true, freePorts: "3 з 4 вільні" }},
    {{ title: "Хаб «Львів-Арена» · 160 кВт CCS2", addr: "вул. Стрийська, 199 · 6 портів (4 вільні)", img: "hub_lviv", gen: true, freePorts: "4 з 6 вільні" }},
    {{ title: "Хаб «Київ-Оболонь» · 120 кВт CCS2", addr: "просп. Оболонський, 1-Б · 4 порти (2 вільні)", img: "hub_obolon", gen: false, freePorts: "2 з 4 вільні" }},
    {{ title: "Хаб «Одеса-Аркадія» · 100 кВт CCS2", addr: "вул. Генуезька, 5 · 4 порти (3 вільні)", img: "hub_odesa", gen: false, freePorts: "3 з 4 вільні" }},
    {{ title: "Хаб «Дніпро-Центр» · 120 кВт CCS2", addr: "просп. Д. Яворницького, 22 · 4 порти (1 вільний)", img: "hub_dnipro", gen: true, freePorts: "1 з 4 вільні" }},
    {{ title: "Хаб «Житомир-Траса» · 160 кВт Ultra-Fast", addr: "траса М06 Київ-Чоп, 128 км · 4 порти (4 вільні)", img: "hub_zhytomyr", gen: true, freePorts: "4 з 4 вільні" }}
  ];

  // ==========================================================================
  // РЯД 1: ДОСЛІДЖЕННЯ ТА АРХІТЕКТУРА
  // ==========================================================================

  // FRAME 00: COVER
  const fCover = figma.createFrame();
  fCover.name = "00_Cover";
  fCover.resize(1440, 900);
  fCover.x = 0; fCover.y = 0;
  fCover.fills = [{{ type: "SOLID", color: cDark }}];

  const coverCard = figma.createFrame();
  coverCard.resize(1320, 780);
  coverCard.x = 60; coverCard.y = 60;
  coverCard.cornerRadius = 24;
  coverCard.fills = [{{ type: "SOLID", color: {{ r: 30/255, g: 41/255, b: 59/255 }} }}];
  fCover.appendChild(coverCard);

  addSvgNode(coverCard, "logo", 60, 60, 64, 64);
  helperText(coverCard, "ChargeUA", 36, "Bold", cWhite, 140, 75);
  helperText(coverCard, "Лабораторна робота №4 · Проєктування інтерфейсу користувача (UI/UX)", 18, "Medium", cPrimary, 60, 155);
  helperText(coverCard, "Національний веб-сервіс та агрегатор швидкісних електрозарядних станцій", 34, "Bold", cWhite, 60, 195, 1200);

  const metaBox = figma.createFrame();
  metaBox.resize(1200, 180);
  metaBox.x = 60; metaBox.y = 310;
  metaBox.cornerRadius = 16;
  metaBox.fills = [{{ type: "SOLID", color: cDark }}];
  coverCard.appendChild(metaBox);

  helperText(metaBox, "Автор проєкту:", 13, "Medium", cMuted, 40, 28);
  helperText(metaBox, "Лемішка Андрій, студент групи ПП-24", 16, "Bold", cWhite, 40, 50);
  helperText(metaBox, "Дисципліна:", 13, "Medium", cMuted, 40, 95);
  helperText(metaBox, "Технології розробки веб-застосунків (2026)", 15, "Semi Bold", cWhite, 40, 118);

  helperText(metaBox, "Архітектура та стандарти:", 13, "Medium", cMuted, 620, 28);
  helperText(metaBox, "Desktop (1440px) · Tablet (768px) · Mobile (390px)", 16, "Bold", cWhite, 620, 50);
  helperText(metaBox, "UI Kit & Статус:", 13, "Medium", cMuted, 620, 95);
  helperText(metaBox, "WCAG 2.2 AA · 100% Компонентність · Interactive Prototype (76+ зв'язків)", 15, "Semi Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 620, 118);

  addImageRect(coverCard, "hero", 60, 520, 1200, 220, 16);

  // FRAME 01: USER FLOW
  const fUserFlow = figma.createFrame();
  fUserFlow.name = "01_User_Flow";
  fUserFlow.resize(1440, 900);
  fUserFlow.x = 1600; fUserFlow.y = 0;
  fUserFlow.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fUserFlow, "01 — Сценарії взаємодії користувача (User Flows)", 28, "Bold", cDark, 60, 40);
  helperText(fUserFlow, "Два ключові маршрути: (1) Пошук та розрахунок вартості, (2) Навігація до станції з резервним генератором", 15, "Regular", cMuted, 60, 80);

  const flows = [
    {{ title: "Сценарій 1: Швидкий підбір та розрахунок вартості зарядки", steps: ["1. Вхід на головну сторінку", "2. Вибір марки/моделі авто у калькуляторі", "3. Встановлення слайдера заряду (20% → 80%)", "4. Отримання точного розрахунку (кВт·год, час, ціна)", "5. Перехід до карти станцій"] }},
    {{ title: "Сценарій 2: Навігація до станції під час блекауту (генератор)", steps: ["1. Активація швидкого фільтра «🔋 З генератором»", "2. Перегляд списку доступних хабів із живим статусом", "3. Перевірка наявності вільних конекторів CCS2", "4. Відкриття детальної сторінки хабу", "5. Запуск навігатора (Google Maps / Waze)"] }}
  ];

  flows.forEach((fl, idx) => {{
    const card = figma.createFrame();
    card.resize(1320, 310);
    card.x = 60; card.y = 130 + idx * 350;
    card.cornerRadius = 16;
    card.fills = [{{ type: "SOLID", color: cWhite }}];
    card.strokes = [{{ type: "SOLID", color: cBorder }}];
    fUserFlow.appendChild(card);

    helperText(card, fl.title, 18, "Bold", cDark, 30, 25);
    fl.steps.forEach((step, sIdx) => {{
      const sPill = figma.createFrame();
      sPill.resize(230, 190);
      sPill.x = 30 + sIdx * 255; sPill.y = 75;
      sPill.cornerRadius = 12;
      sPill.fills = [{{ type: "SOLID", color: cBgSurface }}];
      sPill.strokes = [{{ type: "SOLID", color: cBorder }}];
      card.appendChild(sPill);
      helperText(sPill, `Крок 0${{sIdx + 1}}`, 12, "Bold", cPrimary, 16, 20);
      helperText(sPill, step, 14, "Semi Bold", cDark, 16, 50, 195);
    }});
  }});

  // FRAME 02: SITEMAP
  const fSitemap = figma.createFrame();
  fSitemap.name = "02_Sitemap";
  fSitemap.resize(1440, 900);
  fSitemap.x = 3200; fSitemap.y = 0;
  fSitemap.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fSitemap, "02 — Інформаційна архітектура (Sitemap)", 28, "Bold", cDark, 60, 40);
  helperText(fSitemap, "Структура сайту, згенерована в Relume AI та адаптована під український ринок EV", 15, "Regular", cMuted, 60, 80);

  const homeNode = figma.createFrame();
  homeNode.resize(280, 80);
  homeNode.x = 580; homeNode.y = 140;
  homeNode.cornerRadius = 12;
  homeNode.fills = [{{ type: "SOLID", color: cPrimary }}];
  fSitemap.appendChild(homeNode);
  helperText(homeNode, "Головна сторінка (Home)", 16, "Bold", cWhite, 35, 20);
  helperText(homeNode, "ChargeUA National Hub", 12, "Regular", {{ r: 224/255, g: 242/255, b: 254/255 }}, 55, 45);

  const siteChildren = [
    {{ title: "01 · Головна сторінка (Home)", desc: "Інтерактивний калькулятор зарядки, Live-карта хабів, генератори в блекаути, як зарядитися та відгуки" }},
    {{ title: "02 · Карта та каталог станцій (Map)", desc: "Пошук 480+ локацій, фільтри CCS2/генератор, живий статус зайнятості та порти онлайн" }},
    {{ title: "03 · Деталі зарядної станції (Details)", desc: "Жива телеметрія 4 портів, потужність кВт, резервне живлення та пряма навігація" }}
  ];

  siteChildren.forEach((ch, idx) => {{
    const cNode = figma.createFrame();
    cNode.resize(400, 160);
    cNode.x = 60 + idx * 450; cNode.y = 290;
    cNode.cornerRadius = 12;
    cNode.fills = [{{ type: "SOLID", color: cWhite }}];
    cNode.strokes = [{{ type: "SOLID", color: cBorder }}];
    fSitemap.appendChild(cNode);
    helperText(cNode, ch.title, 16, "Bold", cDark, 24, 24);
    helperText(cNode, ch.desc, 13, "Regular", cMuted, 24, 58, 350);
  }});

  // FRAME 03: WIREFRAMES (Low-Fidelity Architecture Matching Report Fig 5 & 6)
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
  const wfDHead = figma.createFrame(); wfDHead.resize(712, 40); wfDHead.x = 24; wfDHead.y = 16; wfDHead.cornerRadius = 6; wfDHead.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDHead.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDHead);
  helperText(wfDHead, "⚡ [LOGO] ChargeUA", 11, "Bold", cDark, 14, 12);
  helperText(wfDHead, "Головна   |   Калькулятор   |   Live-карта   |   Хаби   |   Як зарядитись   |   Відгуки", 10, "Medium", cMuted, 140, 13);
  const wfDHBtn = figma.createFrame(); wfDHBtn.resize(80, 26); wfDHBtn.x = 618; wfDHBtn.y = 7; wfDHBtn.cornerRadius = 4; wfDHBtn.fills = [{{ type: "SOLID", color: cDark }}]; wfDHead.appendChild(wfDHBtn);
  helperText(wfDHBtn, "[Знайти хаб]", 9, "Bold", cWhite, 12, 7);

  // Hero section wireframe
  const wfDHero = figma.createFrame(); wfDHero.resize(712, 115); wfDHero.x = 24; wfDHero.y = 62; wfDHero.cornerRadius = 8; wfDHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDHero.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDHero);
  helperText(wfDHero, "[HERO SECTION · Desktop 1440px]", 10, "Bold", cMuted, 16, 10);
  const wfDHl = figma.createFrame(); wfDHl.resize(280, 14); wfDHl.x = 16; wfDHl.y = 28; wfDHl.cornerRadius = 3; wfDHl.fills = [{{ type: "SOLID", color: {{ r: 148/255, g: 163/255, b: 184/255 }} }}]; wfDHero.appendChild(wfDHl);
  const wfDSub = figma.createFrame(); wfDSub.resize(320, 9); wfDSub.x = 16; wfDSub.y = 48; wfDSub.cornerRadius = 2; wfDSub.fills = [{{ type: "SOLID", color: {{ r: 203/255, g: 213/255, b: 225/255 }} }}]; wfDHero.appendChild(wfDSub);
  const wfDB1 = figma.createFrame(); wfDB1.resize(100, 26); wfDB1.x = 16; wfDB1.y = 68; wfDB1.cornerRadius = 4; wfDB1.fills = [{{ type: "SOLID", color: cPrimary }}]; wfDHero.appendChild(wfDB1);
  helperText(wfDB1, "Знайти станцію", 9, "Bold", cWhite, 16, 7);
  const wfDB2 = figma.createFrame(); wfDB2.resize(90, 26); wfDB2.x = 124; wfDB2.y = 68; wfDB2.cornerRadius = 4; wfDB2.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDB2.fills = [{{ type: "SOLID", color: cWhite }}]; wfDHero.appendChild(wfDB2);
  helperText(wfDB2, "Калькулятор", 9, "Bold", cDark, 14, 7);
  const wfDHImg = figma.createFrame(); wfDHImg.resize(250, 92); wfDHImg.x = 445; wfDHImg.y = 10; wfDHImg.cornerRadius = 6; wfDHImg.fills = [{{ type: "SOLID", color: cWhite }}]; wfDHImg.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDHero.appendChild(wfDHImg);
  helperText(wfDHImg, "🖼 [Візуальний блок: Авто + Хаб]", 10, "Semi Bold", cMuted, 36, 38);

  // 3 Benefits Strip wireframe
  const wfDBen = figma.createFrame(); wfDBen.resize(712, 48); wfDBen.x = 24; wfDBen.y = 184; wfDBen.cornerRadius = 8; wfDBen.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDBen.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDBen);
  const bTitles = ["[🧮 Розрахунок витрат]", "[🗺 Live-карта 480+ хабів]", "[⚡ 100% захист від блекаутів]"];
  bTitles.forEach((bt, bIdx) => {{
    const bCard = figma.createFrame(); bCard.resize(220, 34); bCard.x = 12 + bIdx * 232; bCard.y = 7; bCard.cornerRadius = 6; bCard.fills = [{{ type: "SOLID", color: cWhite }}]; bCard.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDBen.appendChild(bCard);
    helperText(bCard, bt, 9.5, "Bold", cDark, 20, 10);
  }});

  // Calculator wireframe
  const wfDCalc = figma.createFrame(); wfDCalc.resize(712, 85); wfDCalc.x = 24; wfDCalc.y = 238; wfDCalc.cornerRadius = 8; wfDCalc.fills = [{{ type: "SOLID", color: cWhite }}]; wfDCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDCalc);
  helperText(wfDCalc, "[SECTION · Інтерактивний калькулятор зарядки]", 11, "Bold", cDark, 16, 10);
  helperText(wfDCalc, "Авто: [Tesla Model 3]   [VW ID.4]   [Nissan Leaf]       |       Батарея: [ 20% ======●====== 80% ]", 9.5, "Regular", cMuted, 16, 32);
  const wfDCalcRes = figma.createFrame(); wfDCalcRes.resize(680, 26); wfDCalcRes.x = 16; wfDCalcRes.y = 50; wfDCalcRes.cornerRadius = 5; wfDCalcRes.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDCalc.appendChild(wfDCalcRes);
  helperText(wfDCalcRes, "📊 Орієнтовна вартість: 652.50 ₴ · Час: ~28 хв (CCS2 Ultra) · Заощадження vs бензин: ~1 450 ₴", 9.5, "Bold", cDark, 16, 6);

  // Live Map wireframe (ОДРАЗУ ПІСЛЯ КАЛЬКУЛЯТОРА!)
  const wfDMap = figma.createFrame(); wfDMap.resize(712, 85); wfDMap.x = 24; wfDMap.y = 330; wfDMap.cornerRadius = 8; wfDMap.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDMap.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDMap);
  helperText(wfDMap, "[SECTION · Live-карта зарядної мережі України (Online Map)]", 11, "Bold", cDark, 16, 10);
  helperText(wfDMap, "🗺 [Live-карта 480+ станцій] · Налаштування: 🔍 Пошук адреси | CCS2, Type 2 | 🔋 Генератор ON | ☑ Вільні", 9.5, "Medium", cPrimary, 16, 30);
  const wfDMapBox = figma.createFrame(); wfDMapBox.resize(680, 26); wfDMapBox.x = 16; wfDMapBox.y = 50; wfDMapBox.cornerRadius = 4; wfDMapBox.fills = [{{ type: "SOLID", color: cWhite }}]; wfDMap.appendChild(wfDMapBox);
  helperText(wfDMapBox, "Київ-Поділ 🔋 (3/4) · Львів-Арена 🔋 (5/6) · Одеса-Порт 🔋 (1/2) · Дніпро-Сіті 🔋 (2/2)", 9, "Semi Bold", cDark, 12, 6);

  // Stations Grid wireframe (2 cards)
  const wfDStat = figma.createFrame(); wfDStat.resize(712, 95); wfDStat.x = 24; wfDStat.y = 422; wfDStat.cornerRadius = 8; wfDStat.fills = [{{ type: "SOLID", color: cWhite }}]; wfDStat.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDStat);
  helperText(wfDStat, "[SECTION · Популярні зарядні хаби]", 11, "Bold", cDark, 16, 10);
  const stWireData = [
    {{ title: "Хаб «Київ-Поділ» · 120 кВт CCS2", addr: "вул. Сагайдачного, 12 · 3/4 вільно", gen: "🔋 Генератор ON" }},
    {{ title: "Хаб «Львів-Арена» · 160 кВт CCS2", addr: "вул. Стрийська, 199 · 5/6 вільно", gen: "🔋 Генератор ON" }}
  ];
  stWireData.forEach((st, sIdx) => {{
    const sBox = figma.createFrame(); sBox.resize(336, 56); sBox.x = 16 + sIdx * 348; sBox.y = 30; sBox.cornerRadius = 6; sBox.fills = [{{ type: "SOLID", color: cBgSurface }}]; sBox.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDStat.appendChild(sBox);
    helperText(sBox, st.title, 9.5, "Bold", cDark, 12, 8);
    helperText(sBox, st.addr + " · " + st.gen, 8.5, "Regular", cMuted, 12, 28);
    const sBtn = figma.createFrame(); sBtn.resize(95, 20); sBtn.x = 228; sBtn.y = 26; sBtn.cornerRadius = 4; sBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; sBox.appendChild(sBtn);
    helperText(sBtn, "Маршрут CCS2", 8.5, "Bold", cWhite, 12, 4);
  }});

  // Blackout Generator Section wireframe
  const wfDGen = figma.createFrame(); wfDGen.resize(712, 80); wfDGen.x = 24; wfDGen.y = 524; wfDGen.cornerRadius = 8; wfDGen.fills = [{{ type: "SOLID", color: cDark }}]; wfDesk.appendChild(wfDGen);
  helperText(wfDGen, "⚡ 100% РЕЗЕРВНЕ ЖИВЛЕННЯ · 180+ СТАНЦІЙ З ГЕНЕРАТОРАМИ", 10.5, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 16, 10);
  helperText(wfDGen, "Автономні промислові генератори Cummins 160 кВт з автоматичним вводом резерву (АВР 15 сек).", 9.5, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 16, 30);
  const wfDGenBox = figma.createFrame(); wfDGenBox.resize(680, 24); wfDGenBox.x = 16; wfDGenBox.y = 48; wfDGenBox.cornerRadius = 4; wfDGenBox.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.1 }}]; wfDGen.appendChild(wfDGenBox);
  helperText(wfDGenBox, "Паливний резервуар: 48 годин безперервної роботи · Онлайн-моніторинг телеметрії через Starlink", 8.5, "Medium", cWhite, 12, 5);

  // Reviews & Steps wireframe
  const wfDRev = figma.createFrame(); wfDRev.resize(712, 80); wfDRev.x = 24; wfDRev.y = 611; wfDRev.cornerRadius = 8; wfDRev.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfDRev.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDesk.appendChild(wfDRev);
  helperText(wfDRev, "[SECTION · Як зарядитися за 3 кроки & Відгуки водіїв]", 10.5, "Bold", cDark, 16, 8);
  const rBoxes = [
    "[Крок 1: Оберіть хаб на мапі]",
    "[Крок 2: Підключіть CCS2 / Type 2]",
    "[Крок 3: Оплата карткою / Apple Pay]",
    "★★★★★ «Під час блекауту дуже виручило!»"
  ];
  rBoxes.forEach((rb, rIdx) => {{
    const rF = figma.createFrame(); rF.resize(162, 42); rF.x = 16 + rIdx * 172; rF.y = 28; rF.cornerRadius = 6; rF.fills = [{{ type: "SOLID", color: cWhite }}]; rF.strokes = [{{ type: "SOLID", color: cBorder }}]; wfDRev.appendChild(rF);
    helperText(rF, rb, 8, "Semi Bold", cMuted, 8, 14);
  }});

  // Footer wireframe
  const wfDFoot = figma.createFrame(); wfDFoot.resize(712, 52); wfDFoot.x = 24; wfDFoot.y = 698; wfDFoot.cornerRadius = 8; wfDFoot.fills = [{{ type: "SOLID", color: cDark }}]; wfDesk.appendChild(wfDFoot);
  helperText(wfDFoot, "⚡ ChargeUA — Національна мережа швидкісних електрозарядних комплексів", 9.5, "Bold", cWhite, 16, 12);
  helperText(wfDFoot, "© 2026 ChargeUA. Усі права захищено. Створено в рамках ЛР4 студентом Андрієм Лемішкою (ПП-24)", 8.5, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 16, 30);

  // Mobile Wireframe Box (Right side: 380 x 880)
  const wfMob = figma.createFrame();
  wfMob.resize(380, 880);
  wfMob.x = 880; wfMob.y = 130;
  wfMob.cornerRadius = 12;
  wfMob.fills = [{{ type: "SOLID", color: cWhite }}];
  wfMob.strokes = [{{ type: "SOLID", color: cBorder }}];
  fWireframes.appendChild(wfMob);

  // Mobile Header
  const wfMHead = figma.createFrame(); wfMHead.resize(340, 36); wfMHead.x = 20; wfMHead.y = 16; wfMHead.cornerRadius = 6; wfMHead.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMHead.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMHead);
  helperText(wfMHead, "⚡ ChargeUA", 11, "Bold", cPrimary, 12, 10);
  helperText(wfMHead, "[☰ Меню]", 11, "Bold", cDark, 275, 10);

  // Mobile Hero
  const wfMHero = figma.createFrame(); wfMHero.resize(340, 105); wfMHero.x = 20; wfMHero.y = 58; wfMHero.cornerRadius = 6; wfMHero.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMHero.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMHero);
  helperText(wfMHero, "[HERO · Mobile 390px]", 9, "Bold", cMuted, 12, 8);
  const wfMHl = figma.createFrame(); wfMHl.resize(190, 12); wfMHl.x = 12; wfMHl.y = 26; wfMHl.cornerRadius = 3; wfMHl.fills = [{{ type: "SOLID", color: {{ r: 148/255, g: 163/255, b: 184/255 }} }}]; wfMHero.appendChild(wfMHl);
  const wfMSub = figma.createFrame(); wfMSub.resize(260, 8); wfMSub.x = 12; wfMSub.y = 44; wfMSub.cornerRadius = 2; wfMSub.fills = [{{ type: "SOLID", color: {{ r: 203/255, g: 213/255, b: 225/255 }} }}]; wfMHero.appendChild(wfMSub);
  const wfMB1 = figma.createFrame(); wfMB1.resize(316, 24); wfMB1.x = 12; wfMB1.y = 62; wfMB1.cornerRadius = 4; wfMB1.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMHero.appendChild(wfMB1);
  helperText(wfMB1, "Знайти найближчу станцію (GPS)", 9, "Bold", cWhite, 80, 6);

  // Mobile Benefits
  const wfMBen = figma.createFrame(); wfMBen.resize(340, 58); wfMBen.x = 20; wfMBen.y = 170; wfMBen.cornerRadius = 6; wfMBen.fills = [{{ type: "SOLID", color: cWhite }}]; wfMBen.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMBen);
  helperText(wfMBen, "• Швидкий розрахунок витрат (автопресети)", 8.5, "Regular", cDark, 12, 8);
  helperText(wfMBen, "• Live-карта: 480+ хабів із живою телеметрією", 8.5, "Regular", cDark, 12, 23);
  helperText(wfMBen, "• 100% захист від блекаутів завдяки генераторам", 8.5, "Regular", cDark, 12, 38);

  // Mobile Calculator
  const wfMCalc = figma.createFrame(); wfMCalc.resize(340, 75); wfMCalc.x = 20; wfMCalc.y = 235; wfMCalc.cornerRadius = 6; wfMCalc.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMCalc);
  helperText(wfMCalc, "[Мобільний калькулятор]", 9.5, "Bold", cDark, 12, 8);
  helperText(wfMCalc, "Модель: Tesla Model 3 · Батарея 20% → 80%", 8.5, "Medium", cMuted, 12, 26);
  const wfMCRes = figma.createFrame(); wfMCRes.resize(316, 24); wfMCRes.x = 12; wfMCRes.y = 44; wfMCRes.cornerRadius = 4; wfMCRes.fills = [{{ type: "SOLID", color: cWhite }}]; wfMCRes.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMCalc.appendChild(wfMCRes);
  helperText(wfMCRes, "652.50 ₴ · ~28 хв (CCS2)", 9, "Bold", cDark, 95, 5);

  // Mobile Live Map (ОДРАЗУ ПІСЛЯ КАЛЬКУЛЯТОРА!)
  const wfMMap = figma.createFrame(); wfMMap.resize(340, 75); wfMMap.x = 20; wfMMap.y = 318; wfMMap.cornerRadius = 6; wfMMap.fills = [{{ type: "SOLID", color: cWhite }}]; wfMMap.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMMap);
  helperText(wfMMap, "🗺 [Live-карта 480+ хабів онлайн]", 9.5, "Bold", cDark, 12, 8);
  helperText(wfMMap, "Фільтри: 🔍 Пошук | CCS2 / Type 2 | 🔋 Генератор ON | ☑ Вільні", 8, "Medium", cPrimary, 12, 26);
  const wfMMapPin = figma.createFrame(); wfMMapPin.resize(316, 22); wfMMapPin.x = 12; wfMMapPin.y = 44; wfMMapPin.cornerRadius = 4; wfMMapPin.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMMap.appendChild(wfMMapPin);
  helperText(wfMMapPin, "Київ-Поділ (3/4) · Львів-Арена (5/6)", 8.5, "Bold", cDark, 60, 5);

  // Mobile Station Card
  const wfMStat = figma.createFrame(); wfMStat.resize(340, 80); wfMStat.x = 20; wfMStat.y = 400; wfMStat.cornerRadius = 6; wfMStat.fills = [{{ type: "SOLID", color: cWhite }}]; wfMStat.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMStat);
  helperText(wfMStat, "Хаб «Київ-Поділ» · 120 кВт CCS2", 9.5, "Bold", cDark, 12, 8);
  helperText(wfMStat, "вул. Сагайдачного, 12 · 🔋 Генератор ON", 8.5, "Regular", cMuted, 12, 24);
  const wfMSb = figma.createFrame(); wfMSb.resize(316, 24); wfMSb.x = 12; wfMSb.y = 46; wfMSb.cornerRadius = 4; wfMSb.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMStat.appendChild(wfMSb);
  helperText(wfMSb, "Прокласти маршрут CCS2", 9, "Bold", cWhite, 95, 5);

  // Mobile Generator & Steps
  const wfMGen = figma.createFrame(); wfMGen.resize(340, 68); wfMGen.x = 20; wfMGen.y = 488; wfMGen.cornerRadius = 6; wfMGen.fills = [{{ type: "SOLID", color: cDark }}]; wfMob.appendChild(wfMGen);
  helperText(wfMGen, "⚡ Резервне живлення 160 кВт", 9.5, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 12, 8);
  helperText(wfMGen, "180+ станцій працюють під час аварійних відключень.", 8.5, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 12, 26);
  helperText(wfMGen, "Автоматичні генератори Cummins гарантують зарядку.", 8, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 12, 44);

  // Mobile Review
  const wfMRev = figma.createFrame(); wfMRev.resize(340, 54); wfMRev.x = 20; wfMRev.y = 563; wfMRev.cornerRadius = 6; wfMRev.fills = [{{ type: "SOLID", color: cBgSurface }}]; wfMRev.strokes = [{{ type: "SOLID", color: cBorder }}]; wfMob.appendChild(wfMRev);
  helperText(wfMRev, "★★★★★ «Під час блекауту виручило!»", 8.5, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 12, 10);
  helperText(wfMRev, "Олексій К. · Tesla Model Y · 15 хв тому", 8, "Regular", cMuted, 12, 28);

  // Mobile Footer & Sticky Bottom Nav
  const wfMFoot = figma.createFrame(); wfMFoot.resize(340, 48); wfMFoot.x = 20; wfMFoot.y = 624; wfMFoot.cornerRadius = 6; wfMFoot.fills = [{{ type: "SOLID", color: cDark }}]; wfMob.appendChild(wfMFoot);
  helperText(wfMFoot, "© 2026 ChargeUA · Мобільна версія", 8.5, "Regular", cWhite, 12, 12);
  helperText(wfMFoot, "Гаряча лінія 24/7: 0 800 300 400", 8, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 12, 28);

  // Sticky Bar Wireframe (NO Profile! 3 tabs)
  const wfMBot = figma.createFrame(); wfMBot.resize(340, 34); wfMBot.x = 20; wfMBot.y = 679; wfMBot.cornerRadius = 6; wfMBot.fills = [{{ type: "SOLID", color: cPrimary }}]; wfMob.appendChild(wfMBot);
  helperText(wfMBot, "🗺 Карта        |        🧮 Калькулятор        |        ⚡ Генератор 100%", 9.5, "Bold", cWhite, 25, 9);

  // ==========================================================================
  // РОЗДІЛ 2: АСЕТИ, ТОКЕНИ ТА ДИЗАЙН-СИСТЕМА
  // ==========================================================================

  // FRAME 04.0: BRAND ASSETS
  const fAssets = figma.createFrame();
  fAssets.name = "04.0_Brand_Assets_LR3";
  fAssets.resize(1440, 1260);
  fAssets.x = 0; fAssets.y = 1050;
  fAssets.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fAssets, "04.0 — Бренд-матеріали та AI-ілюстрації (з ЛР №3)", 28, "Bold", cDark, 60, 40);
  helperText(fAssets, "Векторні SVG логотипи, фотографії хабів, генератор резервного живлення та відеопрезентація", 15, "Regular", cMuted, 60, 80);

  const logoCard = figma.createFrame();
  logoCard.resize(400, 260);
  logoCard.x = 60; logoCard.y = 140;
  logoCard.cornerRadius = 14;
  logoCard.fills = [{{ type: "SOLID", color: cWhite }}];
  logoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(logoCard);
  helperText(logoCard, "Векторний логотип (Logo.svg)", 14, "Bold", cDark, 24, 20);
  addSvgNode(logoCard, "logo", 140, 80, 100, 100);

  const iconsCard = figma.createFrame();
  iconsCard.resize(400, 260);
  iconsCard.x = 500; iconsCard.y = 140;
  iconsCard.cornerRadius = 14;
  iconsCard.fills = [{{ type: "SOLID", color: cWhite }}];
  iconsCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(iconsCard);
  helperText(iconsCard, "Векторні іконки розділів (SVG)", 14, "Bold", cDark, 24, 20);
  addSvgNode(iconsCard, "calc", 40, 90, 64, 64);
  addSvgNode(iconsCard, "loc", 160, 90, 64, 64);
  addSvgNode(iconsCard, "info", 280, 90, 64, 64);

  const heroCard = figma.createFrame();
  heroCard.resize(440, 260);
  heroCard.x = 940; heroCard.y = 140;
  heroCard.cornerRadius = 14;
  heroCard.fills = [{{ type: "SOLID", color: cWhite }}];
  heroCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(heroCard);
  helperText(heroCard, "Головне фото авто та хабу (hero_bg.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(heroCard, "hero", 24, 60, 392, 180, 8);

  const bannerCard = figma.createFrame();
  bannerCard.resize(400, 260);
  bannerCard.x = 60; bannerCard.y = 430;
  bannerCard.cornerRadius = 14;
  bannerCard.fills = [{{ type: "SOLID", color: cWhite }}];
  bannerCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(bannerCard);
  helperText(bannerCard, "AI Промо-банер мережі (ai_promo_banner.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(bannerCard, "banner_ai", 24, 60, 352, 180, 8);

  const videoCard = figma.createFrame();
  videoCard.resize(400, 260);
  videoCard.x = 500; videoCard.y = 430;
  videoCard.cornerRadius = 14;
  videoCard.fills = [{{ type: "SOLID", color: cWhite }}];
  videoCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(videoCard);
  helperText(videoCard, "Відео-навчання та демо (ai_video_tutorial.jpg)", 14, "Bold", cDark, 24, 20);
  addImageRect(videoCard, "video_tutorial", 24, 60, 352, 180, 8);

  const genCard = figma.createFrame();
  genCard.resize(440, 260);
  genCard.x = 940; genCard.y = 430;
  genCard.cornerRadius = 14;
  genCard.fills = [{{ type: "SOLID", color: cWhite }}];
  genCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(genCard);
  helperText(genCard, "Дизель-генератор 160 кВт (Резервне живлення)", 14, "Bold", cDark, 24, 20);
  addImageRect(genCard, "generator", 24, 60, 392, 180, 8);

  // Row 3: Hubs & Cable
  const hubKyivCard = figma.createFrame();
  hubKyivCard.resize(400, 250);
  hubKyivCard.x = 60; hubKyivCard.y = 710;
  hubKyivCard.cornerRadius = 14;
  hubKyivCard.fills = [{{ type: "SOLID", color: cWhite }}];
  hubKyivCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(hubKyivCard);
  helperText(hubKyivCard, "Зарядний хаб «Київ-Поділ» 120 кВт (ai_hub_kyiv.jpg)", 13, "Bold", cDark, 24, 18);
  addImageRect(hubKyivCard, "hub_kyiv", 24, 52, 352, 175, 8);

  const hubLvivCard = figma.createFrame();
  hubLvivCard.resize(400, 250);
  hubLvivCard.x = 500; hubLvivCard.y = 710;
  hubLvivCard.cornerRadius = 14;
  hubLvivCard.fills = [{{ type: "SOLID", color: cWhite }}];
  hubLvivCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(hubLvivCard);
  helperText(hubLvivCard, "Зарядний хаб «Арена Львів» 160 кВт (ai_hub_lviv.jpg)", 13, "Bold", cDark, 24, 18);
  addImageRect(hubLvivCard, "hub_lviv", 24, 52, 352, 175, 8);

  const cableCard = figma.createFrame();
  cableCard.resize(440, 250);
  cableCard.x = 940; cableCard.y = 710;
  cableCard.cornerRadius = 14;
  cableCard.fills = [{{ type: "SOLID", color: cWhite }}];
  cableCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(cableCard);
  helperText(cableCard, "Смарт-конектор CCS2 (ai_step_cable.jpg)", 13, "Bold", cDark, 24, 18);
  addImageRect(cableCard, "cable", 24, 52, 392, 175, 8);

  // Row 4: Avatars & Video Loop
  const avatarsCard = figma.createFrame();
  avatarsCard.resize(620, 230);
  avatarsCard.x = 60; avatarsCard.y = 980;
  avatarsCard.cornerRadius = 14;
  avatarsCard.fills = [{{ type: "SOLID", color: cWhite }}];
  avatarsCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(avatarsCard);
  helperText(avatarsCard, "Аватари водіїв (ai_avatar_oleksiy, olena, sergiy)", 13, "Bold", cDark, 24, 18);
  addImageRect(avatarsCard, "av1", 30, 58, 64, 64, 32);
  helperText(avatarsCard, "Олексій К.\\nTesla Model Y", 11, "Bold", cDark, 105, 72);
  addImageRect(avatarsCard, "av2", 230, 58, 64, 64, 32);
  helperText(avatarsCard, "Олена М.\\nNissan Leaf", 11, "Bold", cDark, 305, 72);
  addImageRect(avatarsCard, "av3", 420, 58, 64, 64, 32);
  helperText(avatarsCard, "Сергій В.\\nАвтопарк", 11, "Bold", cDark, 495, 72);

  const videoLoopCard = figma.createFrame();
  videoLoopCard.resize(660, 230);
  videoLoopCard.x = 720; videoLoopCard.y = 980;
  videoLoopCard.cornerRadius = 14;
  videoLoopCard.fills = [{{ type: "SOLID", color: cWhite }}];
  videoLoopCard.strokes = [{{ type: "SOLID", color: cBorder }}];
  fAssets.appendChild(videoLoopCard);
  helperText(videoLoopCard, "Анімований GIF луп фонового відео Hero (hero_loop_opt.gif)", 13, "Bold", cDark, 24, 18);
  addImageRect(videoLoopCard, "video", 24, 52, 310, 155, 8);
  helperText(videoLoopCard, "⚡ Роздільність: 1280×720 (60 fps)\\n⚡ Палітра: Адаптивна 256 кольорів\\n⚡ Призначення: Фоновий GIF-луп Hero", 12, "Medium", cDark, 355, 70, 280);
  helperText(videoLoopCard, "100% інтеграція з ЛР №3", 11, "Bold", cPrimary, 355, 150);

  // FRAME 04.1: DESIGN SYSTEM
  const fDesignSystem = figma.createFrame();
  fDesignSystem.name = "04.1_Design_System";
  fDesignSystem.resize(1440, 1280);
  fDesignSystem.x = 1600; fDesignSystem.y = 1050;
  fDesignSystem.fills = [{{ type: "SOLID", color: cBgSurface }}];

  helperText(fDesignSystem, "04.1 — Дизайн-система ChargeUA (Design Tokens & UI Kit)", 28, "Bold", cDark, 60, 40);
  helperText(fDesignSystem, "Кольори, шкала типографіки Inter, матриця кнопок, поля введення, картки телеметрії та відгуків", 15, "Regular", cMuted, 60, 80);

  const swatches = [
    {{ name: "Primary #0284C7", col: cPrimary }},
    {{ name: "Primary Dark #0369A1", col: cPrimaryDark }},
    {{ name: "Dark Slate #0F172A", col: cDark }},
    {{ name: "Muted #64748B", col: cMuted }},
    {{ name: "Border #E2E8F0", col: cBorder }},
    {{ name: "Success Green #16A34A", col: cSuccess }},
    {{ name: "Warning #D97706", col: cWarning }}
  ];

  swatches.forEach((sw, idx) => {{
    const sBox = figma.createFrame();
    sBox.resize(160, 80);
    sBox.x = 60 + idx * 185; sBox.y = 130;
    sBox.cornerRadius = 8;
    sBox.fills = [{{ type: "SOLID", color: sw.col }}];
    sBox.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesignSystem.appendChild(sBox);
    helperText(sBox, sw.name, 11, "Bold", (idx === 4 ? cDark : cWhite), 10, 50);
  }});

  // Buttons Matrix
  helperText(fDesignSystem, "Матриця кнопок (Button Matrix)", 18, "Bold", cDark, 60, 240);
  const btnRows = [
    {{ title: "Primary", bg: cPrimary, txt: cWhite }},
    {{ title: "Secondary", bg: cWhite, txt: cDark, border: true }},
    {{ title: "Success", bg: cSuccess, txt: cWhite }},
    {{ title: "Disabled", bg: cBorder, txt: cMuted }}
  ];

  btnRows.forEach((b, idx) => {{
    const bNode = figma.createFrame();
    bNode.resize(180, 44);
    bNode.x = 60 + idx * 200; bNode.y = 280;
    bNode.cornerRadius = 8;
    bNode.fills = [{{ type: "SOLID", color: b.bg }}];
    if (b.border) bNode.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesignSystem.appendChild(bNode);
    helperText(bNode, b.title, 14, "Bold", b.txt, 40, 13);
  }});

  // ==========================================================================
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

  helperText(fInpCard, "СТАНИ ПОЛІВ ПОШУКУ ТА ФІЛЬТРАЦІЇ (INPUT STATES)", 12, "Bold", cPrimary, 20, 16);

  // Field 1: Search in Focus
  helperText(fInpCard, "Пошук станції за адресою / містом", 12, "Bold", cDark, 20, 44);
  const bFocBadge = figma.createFrame(); bFocBadge.resize(110, 18); bFocBadge.x = 500; bFocBadge.y = 44; bFocBadge.cornerRadius = 4; bFocBadge.fills = [{{ type: "SOLID", color: {{ r: 239/255, g: 246/255, b: 255/255 }} }}]; fInpCard.appendChild(bFocBadge);
  helperText(bFocBadge, "Focus (Введення)", 10, "Bold", cPrimary, 8, 3);
  const fInpFoc = figma.createFrame(); fInpFoc.resize(590, 38); fInpFoc.x = 20; fInpFoc.y = 66; fInpFoc.cornerRadius = 8; fInpFoc.fills = [{{ type: "SOLID", color: cWhite }}]; fInpFoc.strokes = [{{ type: "SOLID", color: cPrimary }}]; fInpCard.appendChild(fInpFoc);
  helperText(fInpFoc, "м. Львів, вул. Стрийська, 199|", 13, "Bold", cDark, 14, 10);
  helperText(fInpCard, "Активне поле пошуку: синя акцентна рамка (#005EC9) та фокусне кільце", 11, "Regular", cMuted, 20, 108);

  // Field 2: Capacity with Error
  helperText(fInpCard, "Мінімальна потужність хабу (кВт)", 12, "Bold", cDark, 20, 130);
  const bErrBadge = figma.createFrame(); bErrBadge.resize(95, 18); bErrBadge.x = 515; bErrBadge.y = 130; bErrBadge.cornerRadius = 4; bErrBadge.fills = [{{ type: "SOLID", color: {{ r: 254/255, g: 242/255, b: 242/255 }} }}]; fInpCard.appendChild(bErrBadge);
  helperText(bErrBadge, "Error (Помилка)", 10, "Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 8, 3);
  const fInpErr = figma.createFrame(); fInpErr.resize(590, 38); fInpErr.x = 20; fInpErr.y = 152; fInpErr.cornerRadius = 8; fInpErr.fills = [{{ type: "SOLID", color: {{ r: 254/255, g: 242/255, b: 242/255 }} }}]; fInpErr.strokes = [{{ type: "SOLID", color: {{ r: 239/255, g: 68/255, b: 68/255 }} }}]; fInpCard.appendChild(fInpErr);
  helperText(fInpErr, "0 кВт", 13, "Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 14, 10);
  helperText(fInpCard, "⚠ Помилка! Вкажіть потужність від 22 до 160 кВт для фільтрації на карті", 11, "Semi Bold", {{ r: 220/255, g: 38/255, b: 38/255 }}, 20, 194);

  // Field 3: Car Model Default
  helperText(fInpCard, "Модель електромобіля (для автопідбору)", 12, "Bold", cDark, 20, 216);
  const bDefBadge = figma.createFrame(); bDefBadge.resize(130, 18); bDefBadge.x = 480; bDefBadge.y = 216; bDefBadge.cornerRadius = 4; bDefBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; fInpCard.appendChild(bDefBadge);
  helperText(bDefBadge, "Default (Плейсхолдер)", 10, "Bold", cMuted, 8, 3);
  const fInpDef = figma.createFrame(); fInpDef.resize(590, 38); fInpDef.x = 20; fInpDef.y = 238; fInpDef.cornerRadius = 8; fInpDef.fills = [{{ type: "SOLID", color: cWhite }}]; fInpDef.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(fInpDef);
  helperText(fInpDef, "Наприклад: Tesla Model 3, VW ID.4...", 13, "Regular", cMuted, 14, 10);
  helperText(fInpCard, "Стан за замовчуванням: нейтральна рамка #CBD5E1, автоматичний підбір роз'єму", 11, "Regular", cMuted, 20, 280);

  // Field 4: Region Disabled
  helperText(fInpCard, "Фільтр мереж за межами України", 12, "Bold", cDark, 20, 302);
  const bDisBadge = figma.createFrame(); bDisBadge.resize(120, 18); bDisBadge.x = 490; bDisBadge.y = 302; bDisBadge.cornerRadius = 4; bDisBadge.fills = [{{ type: "SOLID", color: cBgSurface }}]; bDisBadge.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(bDisBadge);
  helperText(bDisBadge, "Disabled (Заблоковано)", 10, "Bold", cMuted, 8, 3);
  const fInpDis = figma.createFrame(); fInpDis.resize(590, 38); fInpDis.x = 20; fInpDis.y = 324; fInpDis.cornerRadius = 8; fInpDis.fills = [{{ type: "SOLID", color: cBgSurface }}]; fInpDis.strokes = [{{ type: "SOLID", color: cBorder }}]; fInpCard.appendChild(fInpDis);
  helperText(fInpDis, "Доступно лише в межах України", 13, "Regular", cMuted, 14, 10);

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
  helperText(cb1, "Тільки вільні конектори прямо зараз (Touch target 48 px)", 12, "Semi Bold", cDark, 42, 14);

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

  // ==========================================================================
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

  const drawerLinkStations = figma.createFrame();
  drawerLinkStations.resize(312, 36);
  drawerLinkStations.x = 24; drawerLinkStations.y = 215;
  drawerLinkStations.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkStations);
  helperText(drawerLinkStations, "⚡ Популярні зарядні хаби", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkSteps = figma.createFrame();
  drawerLinkSteps.resize(312, 36);
  drawerLinkSteps.x = 24; drawerLinkSteps.y = 260;
  drawerLinkSteps.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkSteps);
  helperText(drawerLinkSteps, "📋 Як зарядитися (3 кроки)", 16, "Semi Bold", cDark, 0, 6);

  const drawerLinkReviews = figma.createFrame();
  drawerLinkReviews.resize(312, 36);
  drawerLinkReviews.x = 24; drawerLinkReviews.y = 305;
  drawerLinkReviews.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  fDrawerOverlay.appendChild(drawerLinkReviews);
  helperText(drawerLinkReviews, "★ Відгуки водіїв", 16, "Semi Bold", cDark, 0, 6);

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
  helperText(fModalOverlay, "Маршрут до швидкісного хабу «Київ-Поділ» успішно сформовано. Конектор CCS2 (120 кВт) наразі вільний. Навігація в Google Maps / Waze активована, орієнтовний час прибуття: 14 хв. Жодних передоплат чи депозитів — оплата за фактом спожитих кВт·год.", 13, "Regular", cMuted, 30, 115, 480);

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
  const specLines1 = [
    "• Тригер: Натискання на іконку ☰ у шапці Mobile",
    "• Анімація: Dissolve 250ms (Ease In & Out)",
    "• Взаємодія: Клік на «Закрити» або ✕ закриває оверлей",
    "• Перехід: Пункт «Карта станцій» веде на 08_Catalog_Map",
    "• Стан: Активний розділ «Головна сторінка»",
    "• Zero-booking: Доступ до довідки та тарифів"
  ];
  specLines1.forEach((ln, lIdx) => {{
    helperText(specBox1, ln, 13, "Regular", cMuted, 24, 65 + lIdx * 25, 370);
  }});

  const specBox2 = figma.createFrame();
  specBox2.resize(420, 460);
  specBox2.x = 510; specBox2.y = 130;
  specBox2.cornerRadius = 12;
  specBox2.fills = [{{ type: "SOLID", color: cWhite }}];
  specBox2.strokes = [{{ type: "SOLID", color: cBorder }}];
  fOverlays.appendChild(specBox2);
  const specLines2 = [
    "• Тригер: Натискання «Прокласти маршрут» на станції",
    "• Анімація: Центрований модальний оверлей 250ms",
    "• Логіка: Помічник підбору вільних конекторів (БЕЗ бронювання)",
    "• Дія кнопки: Запуск зовнішнього додатку навігатора",
    "• Закриття: Клік на кнопку Waze або ✕ закриває оверлей",
    "• Живий статус: 3 з 4 вільні, генератор активний"
  ];
  specLines2.forEach((ln, lIdx) => {{
    helperText(specBox2, ln, 13, "Regular", cMuted, 24, 65 + lIdx * 25, 370);
  }});

  // ==========================================================================
  // РЯД 3: ПОВНІ ЕКРАНИ
  // ==========================================================================

  // FRAME 05: FULL DESKTOP (1440 × 3800)
  const fDesktop = figma.createFrame();
  fDesktop.name = "05_Desktop";
  fDesktop.resize(1440, 4020);
  fDesktop.x = 0; fDesktop.y = 2450;
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
  const dNavHome = figma.createFrame(); dNavHome.resize(75, 30); dNavHome.x = 360; dNavHome.y = 23; dNavHome.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavHome);
  helperText(dNavHome, "Головна", 14, "Bold", cPrimary, 0, 5);

  const dNavCalc = figma.createFrame(); dNavCalc.resize(105, 30); dNavCalc.x = 445; dNavCalc.y = 23; dNavCalc.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavCalc);
  helperText(dNavCalc, "Калькулятор", 14, "Semi Bold", cDark, 0, 5);

  const dNavMap = figma.createFrame(); dNavMap.resize(115, 30); dNavMap.x = 560; dNavMap.y = 23; dNavMap.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavMap);
  helperText(dNavMap, "Карта станцій", 14, "Semi Bold", cDark, 0, 5);

  const dNavHubs = figma.createFrame(); dNavHubs.resize(125, 30); dNavHubs.x = 685; dNavHubs.y = 23; dNavHubs.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavHubs);
  helperText(dNavHubs, "Популярні хаби", 14, "Semi Bold", cDark, 0, 5);

  const dNavSteps = figma.createFrame(); dNavSteps.resize(95, 30); dNavSteps.x = 820; dNavSteps.y = 23; dNavSteps.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavSteps);
  helperText(dNavSteps, "Інструкція", 14, "Semi Bold", cDark, 0, 5);

  const dNavRev = figma.createFrame(); dNavRev.resize(80, 30); dNavRev.x = 925; dNavRev.y = 23; dNavRev.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; dHead.appendChild(dNavRev);
  helperText(dNavRev, "Відгуки", 14, "Semi Bold", cDark, 0, 5);
  const dHeadCta = figma.createFrame();
  dHeadCta.resize(160, 42);
  dHeadCta.x = 1220; dHeadCta.y = 17;
  dHeadCta.cornerRadius = 8;
  dHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}];
  dHead.appendChild(dHeadCta);
  helperText(dHeadCta, "Знайти зарядку", 13, "Bold", cWhite, 26, 12);

  // Hero Section - WITH BACKGROUND VIDEO LOOP (GIF)
  const dHero = figma.createFrame();
  dHero.resize(1440, 540);
  dHero.y = 116;
  dHero.fills = [{{ type: "SOLID", color: cWhite }}];
  fDesktop.appendChild(dHero);

  // Background Video Image on the Right (video_content.mp4 frame)
  addImageRect(dHero, "video", 500, 0, 940, 540, 0);

  // Smooth White Gradient Fade Overlay
  const dFade = figma.createRectangle();
  dFade.resize(450, 540);
  dFade.x = 420; dFade.y = 0;
  dFade.fills = [{{
    type: "GRADIENT_LINEAR",
    gradientTransform: [[1, 0, 0], [0, 1, 0]],
    gradientStops: [
      {{ color: {{ r: 1, g: 1, b: 1, a: 1 }}, position: 0 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0.9 }}, position: 0.5 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0 }}, position: 1 }}
    ]
  }}];
  dHero.appendChild(dFade);

  // Left-aligned Hero Content
  helperText(dHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДНИХ СТАНЦІЙ", 12, "Bold", cPrimary, 60, 48);
  helperText(dHero, "Швидка та надійна зарядка\\nелектромобілів по всій Україні", 42, "Bold", cDark, 60, 80, 640);
  helperText(dHero, "Знаходьте найближчі станції, розраховуйте вартість за лічені секунди\\nта подорожуйте без хвилювань навіть під час блекаутів.", 16, "Regular", cMuted, 60, 205, 600);

  // Hero Actions
  const dHeroBtn1 = figma.createFrame();
  dHeroBtn1.resize(230, 48);
  dHeroBtn1.x = 60; dHeroBtn1.y = 285;
  dHeroBtn1.cornerRadius = 8;
  dHeroBtn1.fills = [{{ type: "SOLID", color: cPrimary }}];
  dHero.appendChild(dHeroBtn1);
  helperText(dHeroBtn1, "Розрахувати зарядку →", 14, "Bold", cWhite, 32, 15);

  const dHeroBtn2 = figma.createFrame();
  dHeroBtn2.resize(180, 48);
  dHeroBtn2.x = 305; dHeroBtn2.y = 285;
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
    chBox.x = 60 + idx * 142; chBox.y = 355;
    chBox.cornerRadius = 16;
    chBox.fills = [{{ type: "SOLID", color: idx === 3 ? cSuccessBg : cWhite }}];
    chBox.strokes = [{{ type: "SOLID", color: idx === 3 ? cSuccess : cBorder }}];
    dHero.appendChild(chBox);
    helperText(chBox, ch, 11, "Bold", idx === 3 ? cSuccess : cDark, 12, 8);
  }});

  // Benefits Strip
  const dStrip = figma.createFrame();
  dStrip.resize(1440, 140);
  dStrip.y = 716;
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
    card.resize(400, 90);
    card.x = 60 + idx * 450; card.y = 25;
    card.cornerRadius = 12;
    card.fills = [{{ type: "SOLID", color: cWhite }}];
    card.strokes = [{{ type: "SOLID", color: cBorder }}];
    dStrip.appendChild(card);
    addSvgNode(card, st.svg, 20, 20, 48, 48);
    helperText(card, st.title, 15, "Bold", cDark, 80, 22);
    helperText(card, st.desc, 12, "Regular", cMuted, 80, 48);
  }});

  // Interactive Calculator with SLIDER (повзунок)
  const dCalcSec = figma.createFrame();
  dCalcSec.resize(1320, 360);
  dCalcSec.x = 60; dCalcSec.y = 926;
  dCalcSec.cornerRadius = 16;
  dCalcSec.fills = [{{ type: "SOLID", color: cWhite }}];
  dCalcSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dCalcSec);

  helperText(dCalcSec, "Розрахуйте точну вартість та час зарядки ChargeUA", 24, "Bold", cDark, 40, 30);
  helperText(dCalcSec, "Оберіть марку електромобіля та налаштуйте бажаний рівень батареї за допомогою повзунка:", 14, "Regular", cMuted, 40, 65);

  const carPills = ["Volkswagen ID.4 (77 кВт·год)", "Tesla Model 3 (60 кВт·год)", "Nissan Leaf (40 кВт·год)", "Hyundai Ioniq 5 (72 кВт·год)"];
  carPills.forEach((cp, idx) => {{
    const cPill = figma.createFrame();
    cPill.resize(250, 38);
    cPill.x = 40 + idx * 265; cPill.y = 105;
    cPill.cornerRadius = 8;
    cPill.fills = [{{ type: "SOLID", color: idx === 0 ? cPrimary : cBgSurface }}];
    if (idx !== 0) cPill.strokes = [{{ type: "SOLID", color: cBorder }}];
    dCalcSec.appendChild(cPill);
    helperText(cPill, cp, 12, "Semi Bold", idx === 0 ? cWhite : cDark, 12, 10);
  }});

  // Calculator SLIDER Box (Повзунок)
  const dSliderBox = figma.createFrame();
  dSliderBox.resize(760, 160);
  dSliderBox.x = 40; dSliderBox.y = 165;
  dSliderBox.cornerRadius = 12;
  dSliderBox.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dSliderBox.strokes = [{{ type: "SOLID", color: cBorder }}];
  dCalcSec.appendChild(dSliderBox);

  helperText(dSliderBox, "Регулювання рівня заряду (Повзунок %):", 13, "Bold", cDark, 20, 18);
  helperText(dSliderBox, "20% → 80% (Додано +46.2 кВт·год)", 13, "Bold", cPrimary, 490, 18);

  // Slider Track & Fill
  const dSliderTrack = figma.createFrame();
  dSliderTrack.resize(720, 10);
  dSliderTrack.x = 20; dSliderTrack.y = 65;
  dSliderTrack.cornerRadius = 5;
  dSliderTrack.fills = [{{ type: "SOLID", color: cBorder }}];
  dSliderBox.appendChild(dSliderTrack);

  const dSliderFill = figma.createFrame();
  dSliderFill.resize(432, 10);
  dSliderFill.x = 144; dSliderFill.y = 65;
  dSliderFill.cornerRadius = 5;
  dSliderFill.fills = [{{ type: "SOLID", color: cPrimary }}];
  dSliderBox.appendChild(dSliderFill);

  // Slider Knob at 80% (576px mark)
  const dSliderKnob = figma.createFrame();
  dSliderKnob.resize(26, 26);
  dSliderKnob.x = 563; dSliderKnob.y = 57;
  dSliderKnob.cornerRadius = 13;
  dSliderKnob.fills = [{{ type: "SOLID", color: cWhite }}];
  dSliderKnob.strokes = [{{ type: "SOLID", color: cPrimary }}];
  dSliderBox.appendChild(dSliderKnob);

  // Tooltip Badge
  const dSliderTip = figma.createFrame();
  dSliderTip.resize(80, 24);
  dSliderTip.x = 536; dSliderTip.y = 26;
  dSliderTip.cornerRadius = 4;
  dSliderTip.fills = [{{ type: "SOLID", color: cPrimary }}];
  dSliderBox.appendChild(dSliderTip);
  helperText(dSliderTip, "80% (Ціль)", 10, "Bold", cWhite, 10, 5);

  helperText(dSliderBox, "0% (Розряджена)       20% (Старт)               50%                 80% (Рекомендовано DC)      100%", 11, "Medium", cMuted, 20, 95);

  // Result Card on Right
  const calcRes = figma.createFrame();
  calcRes.resize(440, 160);
  calcRes.x = 840; calcRes.y = 165;
  calcRes.cornerRadius = 12;
  calcRes.fills = [{{ type: "SOLID", color: {{ r: 240/255, g: 247/255, b: 255/255 }} }}];
  calcRes.strokes = [{{ type: "SOLID", color: {{ r: 191/255, g: 219/255, b: 254/255 }} }}];
  dCalcSec.appendChild(calcRes);

  helperText(calcRes, "ОРІЄНТОВНА ВАРТІСТЬ СЕСІЇ:", 11, "Bold", cMuted, 24, 20);
  helperText(calcRes, "652.50 ₴", 32, "Bold", cPrimary, 24, 45);
  helperText(calcRes, "Тариф: 14.12 ₴ / кВт·год · 46.2 кВт·год", 12, "Regular", cDark, 24, 88);
  helperText(calcRes, "● Час на DC 120 кВт: ~28 хв", 12, "Bold", cDark, 24, 115);

  // LIVE MAP SECTION (Карта з зарядками та повними налаштуваннями)
  const dMapSec = figma.createFrame();
  dMapSec.resize(1320, 560);
  dMapSec.x = 60; dMapSec.y = 1356;
  dMapSec.cornerRadius = 16;
  dMapSec.fills = [{{ type: "SOLID", color: cWhite }}];
  dMapSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dMapSec);

  helperText(dMapSec, "Live-карта зарядної мережі України", 24, "Bold", cDark, 30, 24);
  helperText(dMapSec, "Налаштування фільтрації: типи роз'ємів, вільні конектори та гарантоване живлення від генератора", 13.5, "Regular", cMuted, 30, 58);

  // Map Filter Controls Bar (Налаштування самої карти)
  const dMapFilters = figma.createFrame();
  dMapFilters.resize(1260, 60);
  dMapFilters.x = 30; dMapFilters.y = 90;
  dMapFilters.cornerRadius = 10;
  dMapFilters.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dMapFilters.strokes = [{{ type: "SOLID", color: cBorder }}];
  dMapSec.appendChild(dMapFilters);

  // 1. Search Field
  const dMapSearch = figma.createFrame();
  dMapSearch.resize(320, 40);
  dMapSearch.x = 10; dMapSearch.y = 10;
  dMapSearch.cornerRadius = 8;
  dMapSearch.fills = [{{ type: "SOLID", color: cWhite }}];
  dMapSearch.strokes = [{{ type: "SOLID", color: cPrimary }}];
  dMapFilters.appendChild(dMapSearch);
  helperText(dMapSearch, "🔍 м. Львів, вул. Стрийська, 199", 11.5, "Medium", cDark, 12, 11);

  // 2. Connector Chips
  const dChipsData = [
    {{ label: "⚡ Всі (480+)", bg: cPrimary, color: cWhite, border: cPrimary, w: 100 }},
    {{ label: "CCS 2 (160 кВт)", bg: cWhite, color: cDark, border: cBorder, w: 125 }},
    {{ label: "Type 2 (22 кВт)", bg: cWhite, color: cDark, border: cBorder, w: 120 }},
    {{ label: "🔋 З генератором [ON]", bg: cSuccessBg, color: cSuccess, border: cSuccess, w: 160 }}
  ];
  let chipX = 340;
  dChipsData.forEach(ch => {{
    const cBox = figma.createFrame();
    cBox.resize(ch.w, 40);
    cBox.x = chipX; cBox.y = 10;
    cBox.cornerRadius = 8;
    cBox.fills = [{{ type: "SOLID", color: ch.bg }}];
    cBox.strokes = [{{ type: "SOLID", color: ch.border }}];
    dMapFilters.appendChild(cBox);
    helperText(cBox, ch.label, 11, "Bold", ch.color, 12, 11);
    chipX += ch.w + 8;
  }});

  // 3. Checkbox "Тільки вільні"
  const dFreeBox = figma.createFrame();
  dFreeBox.resize(200, 40);
  dFreeBox.x = chipX + 5; dFreeBox.y = 10;
  dFreeBox.cornerRadius = 8;
  dFreeBox.fills = [{{ type: "SOLID", color: cWhite }}];
  dFreeBox.strokes = [{{ type: "SOLID", color: cBorder }}];
  dMapFilters.appendChild(dFreeBox);
  
  const dCheckIcon = figma.createFrame();
  dCheckIcon.resize(18, 18); dCheckIcon.x = 10; dCheckIcon.y = 11; dCheckIcon.cornerRadius = 4;
  dCheckIcon.fills = [{{ type: "SOLID", color: cPrimary }}];
  dFreeBox.appendChild(dCheckIcon);
  helperText(dCheckIcon, "✓", 11, "Bold", cWhite, 4, 1);
  helperText(dFreeBox, "Тільки вільні (48px)", 11, "Semi Bold", cDark, 34, 11);

  // Map Canvas Box
  const dMapCanvas = figma.createFrame();
  dMapCanvas.resize(1260, 360);
  dMapCanvas.x = 30; dMapCanvas.y = 165;
  dMapCanvas.cornerRadius = 12;
  dMapCanvas.fills = [{{ type: "SOLID", color: cBgSurface }}];
  dMapCanvas.strokes = [{{ type: "SOLID", color: cBorder }}];
  dMapSec.appendChild(dMapCanvas);
  addImageRect(dMapCanvas, "map_lviv", 0, 0, 1260, 360, 12);

  // Pins on Map Canvas
  const mapPinsData = [
    {{ name: "Хаб «Київ-Поділ» · 120 кВт (3/4 вільно) 🔋", x: 620, y: 70, color: cPrimary }},
    {{ name: "Хаб «Львів-Арена» · 160 кВт (5/6 вільно) 🔋", x: 180, y: 110, color: cSuccess }},
    {{ name: "Хаб «Одеса-Порт» · 100 кВт (1/2 вільно) 🔋", x: 680, y: 220, color: cWarning }},
    {{ name: "Хаб «Дніпро-Сіті» · 120 кВт (2/2 вільно) 🔋", x: 960, y: 160, color: cPrimary }}
  ];
  mapPinsData.forEach(pin => {{
    const pDot = figma.createFrame();
    pDot.resize(14, 14);
    pDot.x = pin.x; pDot.y = pin.y;
    pDot.cornerRadius = 7;
    pDot.fills = [{{ type: "SOLID", color: pin.color }}];
    pDot.strokes = [{{ type: "SOLID", color: cWhite }}];
    dMapCanvas.appendChild(pDot);

    const pTag = figma.createFrame();
    pTag.resize(250, 26);
    pTag.x = pin.x - 110; pTag.y = pin.y + 18;
    pTag.cornerRadius = 5;
    pTag.fills = [{{ type: "SOLID", color: cDark }}];
    dMapCanvas.appendChild(pTag);
    helperText(pTag, pin.name, 10, "Bold", cWhite, 8, 6);
  }});

  // Popular Charging Hubs (3 Cards)
  helperText(fDesktop, "Популярні зарядні хаби по Україні", 28, "Bold", cDark, 60, 1986);
  helperText(fDesktop, "Перевірені локації з високою потужністю та гарантованим резервним живленням", 15, "Regular", cMuted, 60, 2026);

  let dFirstStationCard = null;
  const desktopStationBtns = [];
  stationsData.slice(0, 3).forEach((st, idx) => {{
    const sCard = figma.createFrame();
    if (idx === 0) dFirstStationCard = sCard;
    sCard.resize(420, 380);
    sCard.x = 60 + idx * 450; sCard.y = 2066;
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
  }});

  // Generator Blackout Section
  const dGenSec = figma.createFrame();
  dGenSec.resize(1320, 320);
  dGenSec.x = 60; dGenSec.y = 2516;
  dGenSec.cornerRadius = 16;
  dGenSec.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dGenSec);

  addImageRect(dGenSec, "generator", 760, 20, 540, 280, 12);

  const genBadge = figma.createFrame();
  genBadge.resize(230, 28);
  genBadge.x = 40; genBadge.y = 35;
  genBadge.cornerRadius = 6;
  genBadge.fills = [{{ type: "SOLID", color: {{ r: 34/255, g: 197/255, b: 94/255 }}, opacity: 0.2 }}];
  dGenSec.appendChild(genBadge);
  helperText(genBadge, "⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 12, 6);

  helperText(dGenSec, "Заряджайте авто навіть\\nпід час повних блекаутів", 32, "Bold", cWhite, 40, 75);
  helperText(dGenSec, "Понад 180 станцій мережі ChargeUA обладнані промисловими дизель-генераторами потужністю від 160 кВт. Автоматичний запуск за 15 секунд після знеструмлення мережі гарантує стабільний струм та безперебійне живлення.", 14, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 40, 160, 680);

  // How it works / Steps (CLEAN: NO video box! Text & 3 Step Cards)
  const dStepsSec = figma.createFrame();
  dStepsSec.resize(1320, 350);
  dStepsSec.x = 60; dStepsSec.y = 2906;
  dStepsSec.cornerRadius = 16;
  dStepsSec.fills = [{{ type: "SOLID", color: cWhite }}];
  dStepsSec.strokes = [{{ type: "SOLID", color: cBorder }}];
  fDesktop.appendChild(dStepsSec);

  helperText(dStepsSec, "⚡ ПРОСТИЙ ТА ПРОЗОРИЙ ПРОЦЕС", 11, "Bold", cPrimary, 40, 30);
  helperText(dStepsSec, "Як зарядитися за 3 кроки: від пошуку до повної батареї", 26, "Bold", cDark, 40, 55);
  helperText(dStepsSec, "Швидкий алгоритм підключення без заплутаних депозитів, тривалих реєстрацій чи черг на локації.", 14, "Regular", cMuted, 40, 95);

  const stepsList = [
    {{ num: "1", title: "Знайдіть вільну станцію", desc: "Фільтруйте за потужністю, конектором або наявністю генератора на онлайн-карті ChargeUA." }},
    {{ num: "2", title: "Підключіть конектор CCS2", desc: "Вставте кабель у роз'єм електромобіля — розумний індикатор спалахне зеленим кольором." }},
    {{ num: "3", title: "Оплатіть у 1 клік", desc: "Apple Pay, Google Pay або картка без жодних передплат — списується лише фактично спожита енергія." }}
  ];

  stepsList.forEach((sp, idx) => {{
    const sCol = figma.createFrame();
    sCol.resize(390, 180);
    sCol.x = 40 + idx * 420; sCol.y = 140;
    sCol.cornerRadius = 12;
    sCol.fills = [{{ type: "SOLID", color: cBgSurface }}];
    sCol.strokes = [{{ type: "SOLID", color: cBorder }}];
    dStepsSec.appendChild(sCol);

    const sCircle = figma.createFrame();
    sCircle.resize(44, 44);
    sCircle.x = 24; sCircle.y = 24;
    sCircle.cornerRadius = 22;
    sCircle.fills = [{{ type: "SOLID", color: cPrimary }}];
    sCol.appendChild(sCircle);
    helperText(sCircle, sp.num, 18, "Bold", cWhite, 16, 10);

    helperText(sCol, sp.title, 16, "Bold", cDark, 24, 85);
    helperText(sCol, sp.desc, 13, "Regular", cMuted, 24, 115, 340);
  }});

  // Reviews Section
  helperText(fDesktop, "Відгуки реальних водіїв", 28, "Bold", cDark, 60, 3326);
  helperText(fDesktop, "Що кажуть власники електромобілів про сервіс швидкої зарядки ChargeUA", 15, "Regular", cMuted, 60, 3366);

  const reviewsList = [
    {{ name: "Олексій Коваленко", car: "Tesla Model Y", text: "Під час блекауту на Подолі зарядився за 25 хвилин. Генератор гуде, станція стабільна, кава поруч. Найкращий сервіс!", av: "av1" }},
    {{ name: "Олена Мельник", car: "Nissan Leaf", text: "Дуже зручний калькулятор. Одразу видно скільки кіловат потрібно і яка буде фінальна вартість без прихованих платежів.", av: "av2" }},
    {{ name: "Сергій Васильчук", car: "Керівник автопарку", text: "Для комерційного автопарку зручний моніторинг вільних станцій — це знахідка. Жодних простоїв та черг на трасі Київ-Львів.", av: "av3" }}
  ];

  let dFirstReviewCard = null;
  reviewsList.forEach((rv, idx) => {{
    const rCard = figma.createFrame();
    if (idx === 0) dFirstReviewCard = rCard;
    rCard.resize(420, 200);
    rCard.x = 60 + idx * 450; rCard.y = 3406;
    rCard.cornerRadius = 16;
    rCard.fills = [{{ type: "SOLID", color: cWhite }}];
    rCard.strokes = [{{ type: "SOLID", color: cBorder }}];
    fDesktop.appendChild(rCard);

    helperText(rCard, "★★★★★", 14, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 24, 20);
    helperText(rCard, `«${{rv.text}}»`, 13, "Medium", cDark, 24, 48, 370);
    addImageRect(rCard, rv.av, 24, 130, 44, 44, 22);
    helperText(rCard, rv.name, 14, "Bold", cDark, 80, 132);
    helperText(rCard, rv.car, 12, "Regular", cMuted, 80, 152);
  }});

  // Desktop Footer (Без B2B форми, чиста навігація)
  const dFooter = figma.createFrame();
  dFooter.resize(1440, 320);
  dFooter.y = 3686;
  dFooter.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dFooter);

  addSvgNode(dFooter, "logo", 60, 45, 38, 38);
  helperText(dFooter, "ChargeUA", 24, "Bold", cWhite, 110, 50);
  helperText(dFooter, "Національний агрегатор та веб-помічник зарядної інфраструктури України.\\nШвидкий пошук та моніторинг станцій у блекаути.", 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 60, 100, 380);

  helperText(dFooter, "Навігація\\n\\nГоловна\\nКалькулятор\\nLive-карта", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 560, 50);
  helperText(dFooter, "Розділи сайту\\n\\nПопулярні хаби\\nЯк зарядитися (3 кроки)\\nВідгуки водіїв", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 780, 50);
  helperText(dFooter, "Підтримка 24/7\\n\\n0 800 300 400\\nsupport@charge.ua\\nм. Київ, вул. Сагайдачного, 12", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 1040, 50);

  const dFootLine = figma.createFrame(); dFootLine.resize(1320, 1); dFootLine.x = 60; dFootLine.y = 240; dFootLine.fills = [{{ type: "SOLID", color: {{ r: 30/255, g: 41/255, b: 59/255 }} }}]; dFooter.appendChild(dFootLine);
  helperText(dFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 60, 265);
  helperText(dFooter, "Всі системи онлайн (100% Uptime)", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 1120, 265);

  // FRAME 06: FULL TABLET (768 × 3350)
  const fTablet = figma.createFrame();
  fTablet.name = "06_Tablet";
  fTablet.resize(768, 3530);
  fTablet.x = 1600; fTablet.y = 2450;
  fTablet.fills = [{{ type: "SOLID", color: cWhite }}];

  // Tablet Header
  const tHead = figma.createFrame(); tHead.resize(768, 70); tHead.fills = [{{ type: "SOLID", color: cWhite }}]; tHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tHead);
  addSvgNode(tHead, "logo", 30, 18, 32, 32);
  helperText(tHead, "ChargeUA", 20, "Bold", cPrimary, 70, 22);
  helperText(tHead, "Головна     Калькулятор     Карта     Хаби     Відгуки", 13, "Semi Bold", cDark, 240, 26);
  const tHeadCta = figma.createFrame(); tHeadCta.resize(120, 36); tHeadCta.x = 618; tHeadCta.y = 17; tHeadCta.cornerRadius = 6; tHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}]; tHead.appendChild(tHeadCta);
  helperText(tHeadCta, "Знайти", 12, "Bold", cWhite, 36, 10);

  // Tablet Hero - WITH BACKGROUND VIDEO LOOP (GIF)
  const tHero = figma.createFrame(); tHero.resize(768, 480); tHero.y = 70; tHero.fills = [{{ type: "SOLID", color: cWhite }}]; fTablet.appendChild(tHero);

  // Background Video Image on the Right
  addImageRect(tHero, "video", 240, 0, 528, 480, 0);

  // Fade Overlay from White
  const tFade = figma.createRectangle();
  tFade.resize(320, 480);
  tFade.x = 180; tFade.y = 0;
  tFade.fills = [{{
    type: "GRADIENT_LINEAR",
    gradientTransform: [[1, 0, 0], [0, 1, 0]],
    gradientStops: [
      {{ color: {{ r: 1, g: 1, b: 1, a: 1 }}, position: 0 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0.92 }}, position: 0.5 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0 }}, position: 1 }}
    ]
  }}];
  tHero.appendChild(tFade);

  // Tablet Hero Content
  helperText(tHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР ЗАРЯДОК", 11, "Bold", cPrimary, 30, 45);
  helperText(tHero, "Швидка та надійна зарядка\\nпо всій Україні", 30, "Bold", cDark, 30, 72, 420);
  helperText(tHero, "Знаходьте найближчі станції, розраховуйте вартість за секунди та подорожуйте без стресу у блекаути.", 13, "Regular", cMuted, 30, 168, 380);

  const tBtn1 = figma.createFrame();
  tBtn1.resize(210, 44);
  tBtn1.x = 30; tBtn1.y = 240;
  tBtn1.cornerRadius = 8;
  tBtn1.fills = [{{ type: "SOLID", color: cPrimary }}];
  tHero.appendChild(tBtn1);
  helperText(tBtn1, "Розрахувати зарядку →", 12, "Bold", cWhite, 34, 14);

  const tBtn2 = figma.createFrame();
  tBtn2.resize(150, 44);
  tBtn2.x = 255; tBtn2.y = 240;
  tBtn2.cornerRadius = 8;
  tBtn2.fills = [{{ type: "SOLID", color: cWhite }}];
  tBtn2.strokes = [{{ type: "SOLID", color: cBorder }}];
  tHero.appendChild(tBtn2);
  helperText(tBtn2, "Знайти на карті", 12, "Semi Bold", cDark, 26, 14);

  const tHeroChips = ["Type 2 (22 кВт)", "CCS 2 (160 кВт)", "🔋 З генератором"];
  tHeroChips.forEach((ch, idx) => {{
    const chBox = figma.createFrame();
    chBox.resize(125, 30);
    chBox.x = 30 + idx * 135; chBox.y = 305;
    chBox.cornerRadius = 15;
    chBox.fills = [{{ type: "SOLID", color: idx === 2 ? cSuccessBg : cWhite }}];
    chBox.strokes = [{{ type: "SOLID", color: idx === 2 ? cSuccess : cBorder }}];
    tHero.appendChild(chBox);
    helperText(chBox, ch, 10, "Bold", idx === 2 ? cSuccess : cDark, 12, 7);
  }});

  // Tablet Benefits Strip
  const tStrip = figma.createFrame(); tStrip.resize(708, 80); tStrip.x = 30; tStrip.y = 590; tStrip.cornerRadius = 12; tStrip.fills = [{{ type: "SOLID", color: cBgSurface }}]; tStrip.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tStrip);
  helperText(tStrip, "⚡ 480+ станцій онлайн", 13, "Bold", cDark, 25, 30);
  helperText(tStrip, "🔋 100% робота в блекаути", 13, "Bold", cSuccess, 260, 30);
  helperText(tStrip, "⏱ Розрахунок за 3 секунди", 13, "Bold", cPrimary, 510, 30);

  // Tablet Calculator with SLIDER
  const tCalc = figma.createFrame(); tCalc.resize(708, 300); tCalc.x = 30; tCalc.y = 730; tCalc.cornerRadius = 14; tCalc.fills = [{{ type: "SOLID", color: cWhite }}]; tCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tCalc);
  helperText(tCalc, "Калькулятор вартості зарядки", 18, "Bold", cDark, 24, 20);
  helperText(tCalc, "Volkswagen ID.4 (77 кВт·год) · 20% → 80%", 13, "Medium", cPrimary, 24, 50);

  // Slider on Tablet
  const tSlTrack = figma.createFrame(); tSlTrack.resize(660, 8); tSlTrack.x = 24; tSlTrack.y = 100; tSlTrack.cornerRadius = 4; tSlTrack.fills = [{{ type: "SOLID", color: cBorder }}]; tCalc.appendChild(tSlTrack);
  const tSlFill = figma.createFrame(); tSlFill.resize(396, 8); tSlFill.x = 132; tSlFill.y = 100; tSlFill.cornerRadius = 4; tSlFill.fills = [{{ type: "SOLID", color: cPrimary }}]; tCalc.appendChild(tSlFill);
  const tSlKnob = figma.createFrame(); tSlKnob.resize(22, 22); tSlKnob.x = 517; tSlKnob.y = 93; tSlKnob.cornerRadius = 11; tSlKnob.fills = [{{ type: "SOLID", color: cWhite }}]; tSlKnob.strokes = [{{ type: "SOLID", color: cPrimary }}]; tCalc.appendChild(tSlKnob);
  helperText(tCalc, "0%                                  20% (Старт)                                 80% (Ціль)                      100%", 11, "Medium", cMuted, 24, 120);

  helperText(tCalc, "652.50 ₴ · ~28 хв на DC 120 кВт", 22, "Bold", cDark, 24, 160);
  helperText(tCalc, "Тариф: 14.12 ₴ / кВт·год · Спожито: 46.2 кВт·год", 12, "Regular", cMuted, 24, 195);
  const tCalcBtn = figma.createFrame(); tCalcBtn.resize(240, 42); tCalcBtn.x = 24; tCalcBtn.y = 230; tCalcBtn.cornerRadius = 8; tCalcBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; tCalc.appendChild(tCalcBtn);
  helperText(tCalcBtn, "Знайти вільну станцію", 13, "Bold", cWhite, 45, 12);

  // Tablet Map Section with Full Filter Controls
  const tMapSec = figma.createFrame(); tMapSec.resize(708, 400); tMapSec.x = 30; tMapSec.y = 1090; tMapSec.cornerRadius = 14; tMapSec.fills = [{{ type: "SOLID", color: cWhite }}]; tMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tMapSec);
  helperText(tMapSec, "Live-карта зарядної мережі України", 18, "Bold", cDark, 20, 18);
  helperText(tMapSec, "Налаштування фільтрів: конектори та генератори онлайн", 12, "Regular", cMuted, 20, 44);

  // Tablet Filter bar
  const tMapFilter = figma.createFrame(); tMapFilter.resize(668, 44); tMapFilter.x = 20; tMapFilter.y = 70; tMapFilter.cornerRadius = 8; tMapFilter.fills = [{{ type: "SOLID", color: cBgSurface }}]; tMapFilter.strokes = [{{ type: "SOLID", color: cBorder }}]; tMapSec.appendChild(tMapFilter);
  const tMapSearch = figma.createFrame(); tMapSearch.resize(190, 32); tMapSearch.x = 6; tMapSearch.y = 6; tMapSearch.cornerRadius = 6; tMapSearch.fills = [{{ type: "SOLID", color: cWhite }}]; tMapSearch.strokes = [{{ type: "SOLID", color: cPrimary }}]; tMapFilter.appendChild(tMapSearch);
  helperText(tMapSearch, "🔍 вул. Стрийська, 199", 10.5, "Medium", cDark, 8, 7);

  const tChip1 = figma.createFrame(); tChip1.resize(75, 32); tChip1.x = 202; tChip1.y = 6; tChip1.cornerRadius = 6; tChip1.fills = [{{ type: "SOLID", color: cPrimary }}]; tMapFilter.appendChild(tChip1);
  helperText(tChip1, "⚡ Всі", 10, "Bold", cWhite, 16, 8);

  const tChip2 = figma.createFrame(); tChip2.resize(95, 32); tChip2.x = 283; tChip2.y = 6; tChip2.cornerRadius = 6; tChip2.fills = [{{ type: "SOLID", color: cWhite }}]; tChip2.strokes = [{{ type: "SOLID", color: cBorder }}]; tMapFilter.appendChild(tChip2);
  helperText(tChip2, "CCS 2 (160 кВт)", 9.5, "Bold", cDark, 8, 8);

  const tChip3 = figma.createFrame(); tChip3.resize(130, 32); tChip3.x = 384; tChip3.y = 6; tChip3.cornerRadius = 6; tChip3.fills = [{{ type: "SOLID", color: cSuccessBg }}]; tChip3.strokes = [{{ type: "SOLID", color: cSuccess }}]; tMapFilter.appendChild(tChip3);
  helperText(tChip3, "🔋 Генератор [ON]", 10, "Bold", cSuccess, 10, 8);

  const tFreeBox = figma.createFrame(); tFreeBox.resize(135, 32); tFreeBox.x = 520; tFreeBox.y = 6; tFreeBox.cornerRadius = 6; tFreeBox.fills = [{{ type: "SOLID", color: cWhite }}]; tFreeBox.strokes = [{{ type: "SOLID", color: cBorder }}]; tMapFilter.appendChild(tFreeBox);
  helperText(tFreeBox, "✓ Тільки вільні", 10, "Bold", cDark, 12, 8);

  const tMapCanvas = figma.createFrame(); tMapCanvas.resize(668, 240); tMapCanvas.x = 20; tMapCanvas.y = 125; tMapCanvas.cornerRadius = 10; tMapSec.appendChild(tMapCanvas);
  addImageRect(tMapCanvas, "map_lviv", 0, 0, 668, 240, 10);
  mapPinsData.slice(0, 3).forEach((pin, pidx) => {{
    const pt = figma.createFrame(); pt.resize(200, 24); pt.x = 20 + pidx * 215; pt.y = 195; pt.cornerRadius = 5; pt.fills = [{{ type: "SOLID", color: cDark }}]; tMapCanvas.appendChild(pt);
    helperText(pt, pin.name.slice(0, 26) + "...", 9, "Bold", cWhite, 6, 6);
  }});

  // Tablet Popular Stations (2 cards)
  helperText(fTablet, "Популярні зарядні хаби", 22, "Bold", cDark, 30, 1540);
  const tabletStationBtns = [];
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const tSc = figma.createFrame(); tSc.resize(708, 280); tSc.x = 30; tSc.y = 1580 + idx * 300; tSc.cornerRadius = 14; tSc.fills = [{{ type: "SOLID", color: cWhite }}]; tSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tSc);
    addImageRect(tSc, st.img, 0, 0, 708, 150, 0);
    helperText(tSc, st.title, 16, "Bold", cDark, 20, 170);
    helperText(tSc, st.addr, 13, "Regular", cMuted, 20, 195);
    const tSp = figma.createFrame(); tSp.resize(170, 24); tSp.x = 20; tSp.y = 225; tSp.cornerRadius = 6; tSp.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; tSc.appendChild(tSp);
    helperText(tSp, st.gen ? "🔋 Працює від генератора" : "⚡ Мережа онлайн", 11, "Bold", st.gen ? cSuccess : cPrimary, 10, 5);
    const tSb = figma.createFrame(); tSb.resize(220, 36); tSb.x = 468; tSb.y = 220; tSb.cornerRadius = 6; tSb.fills = [{{ type: "SOLID", color: cPrimary }}]; tSc.appendChild(tSb);
    helperText(tSb, "Прокласти маршрут", 12, "Bold", cWhite, 45, 10);
    tabletStationBtns.push(tSb);
  }});

  // Tablet Generator Section
  const tGenSec = figma.createFrame(); tGenSec.resize(708, 260); tGenSec.x = 30; tGenSec.y = 2220; tGenSec.cornerRadius = 14; tGenSec.fills = [{{ type: "SOLID", color: cDark }}]; fTablet.appendChild(tGenSec);
  addImageRect(tGenSec, "generator", 420, 15, 270, 230, 10);
  helperText(tGenSec, "⚡ ЕНЕРГОНЕЗАЛЕЖНІСТЬ 100%", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 20, 25);
  helperText(tGenSec, "Заряджайте авто\\nпід час блекаутів", 22, "Bold", cWhite, 20, 60);
  helperText(tGenSec, "180+ станцій мережі обладнані потужними генераторами 160 кВт.", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 20, 130, 380);

  // Tablet Steps
  helperText(fTablet, "Як зарядитися за 3 кроки", 22, "Bold", cDark, 30, 2540);
  stepsList.forEach((sp, idx) => {{
    const tSt = figma.createFrame(); tSt.resize(708, 75); tSt.x = 30; tSt.y = 2580 + idx * 85; tSt.cornerRadius = 10; tSt.fills = [{{ type: "SOLID", color: cBgSurface }}]; tSt.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tSt);
    const tCirc = figma.createFrame(); tCirc.resize(32, 32); tCirc.x = 16; tCirc.y = 21; tCirc.cornerRadius = 16; tCirc.fills = [{{ type: "SOLID", color: cPrimary }}]; tSt.appendChild(tCirc);
    helperText(tCirc, sp.num, 14, "Bold", cWhite, 11, 7);
    helperText(tSt, sp.title, 14, "Bold", cDark, 60, 18);
    helperText(tSt, sp.desc, 12, "Regular", cMuted, 60, 42, 620);
  }});

  // Tablet Reviews
  helperText(fTablet, "Відгуки водіїв", 22, "Bold", cDark, 30, 2900);
  reviewsList.slice(0, 2).forEach((rv, idx) => {{
    const tRev = figma.createFrame(); tRev.resize(344, 180); tRev.x = 30 + idx * 364; tRev.y = 2940; tRev.cornerRadius = 12; tRev.fills = [{{ type: "SOLID", color: cWhite }}]; tRev.strokes = [{{ type: "SOLID", color: cBorder }}]; fTablet.appendChild(tRev);
    helperText(tRev, "★★★★★", 12, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 18, 16);
    helperText(tRev, `«${{rv.text}}»`, 12, "Medium", cDark, 18, 42, 308);
    addImageRect(tRev, rv.av, 18, 120, 36, 36, 18);
    helperText(tRev, rv.name, 13, "Bold", cDark, 64, 122);
    helperText(tRev, rv.car, 11, "Regular", cMuted, 64, 140);
  }});

  // Tablet Footer (Чиста навігація)
  const tFooter = figma.createFrame(); tFooter.resize(768, 260); tFooter.y = 3200; tFooter.fills = [{{ type: "SOLID", color: cDark }}]; fTablet.appendChild(tFooter);
  addSvgNode(tFooter, "logo", 30, 35, 32, 32);
  helperText(tFooter, "ChargeUA", 20, "Bold", cWhite, 72, 40);
  helperText(tFooter, "Національний агрегатор зарядної інфраструктури України.", 12, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 30, 80, 260);
  helperText(tFooter, "Навігація:\\n• Головна\\n• Калькулятор\\n• Live-карта\\n• Відгуки", 12, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 330, 40);
  helperText(tFooter, "Контакти:\\n• 0 800 300 400\\n• support@charge.ua\\n• м. Київ, Сагайдачного 12", 12, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 530, 40);
  // FRAME 07: FULL MOBILE (390 × 3420) - WITH BACKGROUND VIDEO LOOP
  const fMobile = figma.createFrame();
  fMobile.name = "07_Mobile";
  fMobile.resize(390, 3420);
  fMobile.x = 2500; fMobile.y = 2450;
  fMobile.fills = [{{ type: "SOLID", color: cWhite }}];

  // Mobile Topbar
  const mTop = figma.createFrame(); mTop.resize(390, 34); mTop.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mTop);
  helperText(mTop, "● 480+ станцій онлайн | 0 800 300 400", 10, "Medium", cWhite, 16, 9);

  // Mobile Header
  const mHead = figma.createFrame(); mHead.resize(390, 56); mHead.y = 34; mHead.fills = [{{ type: "SOLID", color: cWhite }}]; mHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mHead);
  addSvgNode(mHead, "logo", 16, 14, 28, 28);
  helperText(mHead, "ChargeUA", 19, "Bold", cPrimary, 52, 17);
  const mBurgerBtn = figma.createFrame();
  mBurgerBtn.resize(40, 40);
  mBurgerBtn.x = 340; mBurgerBtn.y = 8;
  mBurgerBtn.cornerRadius = 6;
  mBurgerBtn.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mHead.appendChild(mBurgerBtn);
  helperText(mBurgerBtn, "☰", 22, "Bold", cDark, 10, 6);

  // Mobile Hero - WITH BACKGROUND VIDEO LOOP (video_content.mp4 from LR3)
  const mHero = figma.createFrame(); mHero.resize(390, 410); mHero.y = 90; mHero.fills = [{{ type: "SOLID", color: cWhite }}]; fMobile.appendChild(mHero);

  // Background Video Image (filling hero)
  addImageRect(mHero, "video", 0, 30, 390, 380, 0);

  // Fade Overlay (Vertical Gradient from White to transparent)
  const mFade = figma.createRectangle();
  mFade.resize(390, 410);
  mFade.x = 0; mFade.y = 0;
  mFade.fills = [{{
    type: "GRADIENT_LINEAR",
    gradientTransform: [[0, 1, 0], [-1, 0, 1]],
    gradientStops: [
      {{ color: {{ r: 1, g: 1, b: 1, a: 0.98 }}, position: 0 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0.88 }}, position: 0.48 }},
      {{ color: {{ r: 1, g: 1, b: 1, a: 0.35 }}, position: 1 }}
    ]
  }}];
  mHero.appendChild(mFade);

  helperText(mHero, "⚡ НАЦІОНАЛЬНИЙ АГРЕГАТОР", 10, "Bold", cPrimary, 20, 18);
  helperText(mHero, "Заряджайте авто\\nбез стресу", 28, "Bold", cDark, 20, 42);
  helperText(mHero, "Усі мережі на одній карті з фільтром генераторів у блекаути.", 13, "Regular", cDark, 20, 120, 350);

  // Quick Chips
  const mChip1 = figma.createFrame(); mChip1.resize(165, 30); mChip1.x = 20; mChip1.y = 175; mChip1.cornerRadius = 15; mChip1.fills = [{{ type: "SOLID", color: cWhite }}]; mChip1.strokes = [{{ type: "SOLID", color: cBorder }}]; mHero.appendChild(mChip1);
  helperText(mChip1, "⚡ CCS 2 (160 кВт)", 10, "Bold", cDark, 14, 8);
  const mChip2 = figma.createFrame(); mChip2.resize(175, 30); mChip2.x = 195; mChip2.y = 175; mChip2.cornerRadius = 15; mChip2.fills = [{{ type: "SOLID", color: cSuccessBg }}]; mChip2.strokes = [{{ type: "SOLID", color: cSuccess }}]; mHero.appendChild(mChip2);
  helperText(mChip2, "🔋 Тільки генератор", 10, "Bold", cSuccess, 14, 8);

  const mBtn = figma.createFrame(); mBtn.resize(350, 44); mBtn.x = 20; mBtn.y = 220; mBtn.cornerRadius = 8; mBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; mHero.appendChild(mBtn);
  helperText(mBtn, "Розрахувати зарядку →", 13, "Bold", cWhite, 95, 13);

  const mBtnMap = figma.createFrame(); mBtnMap.resize(350, 40); mBtnMap.x = 20; mBtnMap.y = 274; mBtnMap.cornerRadius = 8; mBtnMap.fills = [{{ type: "SOLID", color: cWhite }}]; mBtnMap.strokes = [{{ type: "SOLID", color: cBorder }}]; mHero.appendChild(mBtnMap);
  helperText(mBtnMap, "Знайти найближчий хаб", 12.5, "Semi Bold", cDark, 95, 11);

  // Mobile Calculator Card WITH SLIDER (ПОВЗУНОК) - SPACIOUS (gap 50px)
  const mCalc = figma.createFrame(); mCalc.resize(350, 260); mCalc.x = 20; mCalc.y = 550; mCalc.cornerRadius = 14; mCalc.fills = [{{ type: "SOLID", color: cWhite }}]; mCalc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mCalc);
  helperText(mCalc, "Калькулятор витрат", 17, "Bold", cDark, 16, 16);
  helperText(mCalc, "VW ID.4 · 20% → 80%", 13, "Semi Bold", cPrimary, 16, 42);

  // Slider on Mobile
  const mSlTrack = figma.createFrame(); mSlTrack.resize(318, 8); mSlTrack.x = 16; mSlTrack.y = 78; mSlTrack.cornerRadius = 4; mSlTrack.fills = [{{ type: "SOLID", color: cBorder }}]; mCalc.appendChild(mSlTrack);
  const mSlFill = figma.createFrame(); mSlFill.resize(190, 8); mSlFill.x = 64; mSlFill.y = 78; mSlFill.cornerRadius = 4; mSlFill.fills = [{{ type: "SOLID", color: cPrimary }}]; mCalc.appendChild(mSlFill);
  const mSlKnob = figma.createFrame(); mSlKnob.resize(20, 20); mSlKnob.x = 244; mSlKnob.y = 72; mSlKnob.cornerRadius = 10; mSlKnob.fills = [{{ type: "SOLID", color: cWhite }}]; mSlKnob.strokes = [{{ type: "SOLID", color: cPrimary }}]; mCalc.appendChild(mSlKnob);
  helperText(mCalc, "0%        20% (Старт)        50%        80% (Ціль)        100%", 9, "Medium", cMuted, 16, 96);

  helperText(mCalc, "652.50 ₴ (~28 хв)", 21, "Bold", cDark, 16, 122);
  helperText(mCalc, "Тариф: 14.12 ₴/кВт·год · 46.2 кВт", 12, "Regular", cMuted, 16, 154);
  const mCalcAct = figma.createFrame(); mCalcAct.resize(318, 42); mCalcAct.x = 16; mCalcAct.y = 195; mCalcAct.cornerRadius = 8; mCalcAct.fills = [{{ type: "SOLID", color: cPrimary }}]; mCalc.appendChild(mCalcAct);
  helperText(mCalcAct, "Знайти вільну станцію", 13, "Bold", cWhite, 85, 13);

  // Mobile Map Section with Full Filter Controls
  const mMapSec = figma.createFrame(); mMapSec.resize(350, 360); mMapSec.x = 20; mMapSec.y = 860; mMapSec.cornerRadius = 14; mMapSec.fills = [{{ type: "SOLID", color: cWhite }}]; mMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mMapSec);
  helperText(mMapSec, "Live-карта зарядної мережі", 16, "Bold", cDark, 16, 16);
  helperText(mMapSec, "Налаштування фільтрів та статус світла:", 11, "Regular", cMuted, 16, 38);

  // Mobile Map Search
  const mMapFilter = figma.createFrame(); mMapFilter.resize(318, 36); mMapFilter.x = 16; mMapFilter.y = 60; mMapFilter.cornerRadius = 8; mMapFilter.fills = [{{ type: "SOLID", color: cWhite }}]; mMapFilter.strokes = [{{ type: "SOLID", color: cPrimary }}]; mMapSec.appendChild(mMapFilter);
  helperText(mMapFilter, "🔍 м. Львів, вул. Стрийська, 199", 11, "Medium", cDark, 10, 9);

  // Mobile Chips Row
  const mMapChip1 = figma.createFrame(); mMapChip1.resize(65, 26); mMapChip1.x = 16; mMapChip1.y = 104; mMapChip1.cornerRadius = 6; mMapChip1.fills = [{{ type: "SOLID", color: cPrimary }}]; mMapSec.appendChild(mMapChip1);
  helperText(mMapChip1, "⚡ Всі", 9.5, "Bold", cWhite, 14, 5);

  const mMapChip2 = figma.createFrame(); mMapChip2.resize(95, 26); mMapChip2.x = 87; mMapChip2.y = 104; mMapChip2.cornerRadius = 6; mMapChip2.fills = [{{ type: "SOLID", color: cWhite }}]; mMapChip2.strokes = [{{ type: "SOLID", color: cBorder }}]; mMapSec.appendChild(mMapChip2);
  helperText(mMapChip2, "CCS 2 (160 кВт)", 9, "Bold", cDark, 6, 5);

  const mMapChip3 = figma.createFrame(); mMapChip3.resize(115, 26); mMapChip3.x = 188; mMapChip3.y = 104; mMapChip3.cornerRadius = 6; mMapChip3.fills = [{{ type: "SOLID", color: cSuccessBg }}]; mMapChip3.strokes = [{{ type: "SOLID", color: cSuccess }}]; mMapSec.appendChild(mMapChip3);
  helperText(mMapChip3, "🔋 Генератор ON", 9, "Bold", cSuccess, 8, 5);

  // Checkbox: Тільки вільні
  const mMFreeBox = figma.createFrame(); mMFreeBox.resize(318, 22); mMFreeBox.x = 16; mMFreeBox.y = 138; mMFreeBox.fills = []; mMapSec.appendChild(mMFreeBox);
  const mMChk = figma.createFrame(); mMChk.resize(16, 16); mMChk.x = 0; mMChk.y = 3; mMChk.cornerRadius = 3; mMChk.fills = [{{ type: "SOLID", color: cPrimary }}]; mMFreeBox.appendChild(mMChk);
  helperText(mMChk, "✓", 9.5, "Bold", cWhite, 4, 1);
  helperText(mMFreeBox, "Тільки вільні конектори прямо зараз", 10.5, "Semi Bold", cDark, 24, 3);

  // Map Canvas
  const mMapCanvas = figma.createFrame(); mMapCanvas.resize(318, 175); mMapCanvas.x = 16; mMapCanvas.y = 168; mMapCanvas.cornerRadius = 10; mMapSec.appendChild(mMapCanvas);
  addImageRect(mMapCanvas, "map_lviv", 0, 0, 318, 175, 10);
  mapPinsData.slice(0, 2).forEach((pin, pidx) => {{
    const mp = figma.createFrame(); mp.resize(180, 22); mp.x = 12; mp.y = 100 + pidx * 35; mp.cornerRadius = 4; mp.fills = [{{ type: "SOLID", color: cDark }}]; mMapCanvas.appendChild(mp);
    helperText(mp, pin.name.slice(0, 22) + "...", 9, "Bold", cWhite, 6, 5);
  }});

  // Mobile Station Cards (2 cards - після карти)
  helperText(fMobile, "Популярні зарядні хаби", 18, "Bold", cDark, 20, 1270);
  let mFirstStationCard = null;
  const mobileStationBtns = [];
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const mSc = figma.createFrame();
    if (idx === 0) mFirstStationCard = mSc;
    mSc.resize(350, 280); mSc.x = 20; mSc.y = 1310 + idx * 310; mSc.cornerRadius = 14; mSc.fills = [{{ type: "SOLID", color: cWhite }}]; mSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSc);
    addImageRect(mSc, st.img, 0, 0, 350, 140, 0);
    helperText(mSc, st.title, 14, "Bold", cDark, 16, 155);
    helperText(mSc, st.addr, 11, "Regular", cMuted, 16, 178);

    const mPill = figma.createFrame(); mPill.resize(160, 22); mPill.x = 16; mPill.y = 202; mPill.cornerRadius = 4; mPill.fills = [{{ type: "SOLID", color: st.gen ? cSuccessBg : cBgSurface }}]; mSc.appendChild(mPill);
    helperText(mPill, st.gen ? "🔋 Генератор ON" : "⚡ Мережа ON", 10, "Bold", st.gen ? cSuccess : cPrimary, 8, 4);

    const mSb = figma.createFrame(); mSb.resize(318, 38); mSb.x = 16; mSb.y = 230; mSb.cornerRadius = 8; mSb.fills = [{{ type: "SOLID", color: cPrimary }}]; mSc.appendChild(mSb);
    helperText(mSb, "Прокласти маршрут", 12, "Bold", cWhite, 95, 11);
    mobileStationBtns.push(mSb);
  }});

  // Mobile Generator Section
  const mGenSec = figma.createFrame(); mGenSec.resize(350, 240); mGenSec.x = 20; mGenSec.y = 1970; mGenSec.cornerRadius = 14; mGenSec.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mGenSec);
  addImageRect(mGenSec, "generator", 0, 0, 350, 110, 0);
  helperText(mGenSec, "⚡ Резервне живлення 160 кВт", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 16, 125);
  helperText(mGenSec, "180+ станцій працюють під час блекаутів", 14, "Bold", cWhite, 16, 145);
  helperText(mGenSec, "Автоматичний генератор гарантує швидку зарядку навіть у разі аварійних вимкнень.", 11, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 16, 175, 318);

  // Mobile Steps (Як зарядитися за 3 кроки)
  helperText(fMobile, "Як зарядитися за 3 кроки", 18, "Bold", cDark, 20, 2260);
  let mFirstStep = null;
  stepsList.forEach((sp, idx) => {{
    const mSt = figma.createFrame();
    if (idx === 0) mFirstStep = mSt;
    mSt.resize(350, 70); mSt.x = 20; mSt.y = 2300 + idx * 80; mSt.cornerRadius = 10; mSt.fills = [{{ type: "SOLID", color: cBgSurface }}]; mSt.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSt);
    const mCirc = figma.createFrame(); mCirc.resize(30, 30); mCirc.x = 14; mCirc.y = 20; mCirc.cornerRadius = 15; mCirc.fills = [{{ type: "SOLID", color: cPrimary }}]; mSt.appendChild(mCirc);
    helperText(mCirc, sp.num, 13, "Bold", cWhite, 10, 7);
    helperText(mSt, sp.title, 13, "Bold", cDark, 54, 16);
    helperText(mSt, sp.desc, 11, "Regular", cMuted, 54, 38, 280);
  }});

  // Mobile Reviews (Відгуки)
  helperText(fMobile, "Відгуки водіїв", 18, "Bold", cDark, 20, 2580);
  let mFirstReview = null;
  reviewsList.slice(0, 2).forEach((rv, idx) => {{
    const mRv = figma.createFrame();
    if (idx === 0) mFirstReview = mRv;
    mRv.resize(350, 140); mRv.x = 20; mRv.y = 2620 + idx * 155; mRv.cornerRadius = 12; mRv.fills = [{{ type: "SOLID", color: cWhite }}]; mRv.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mRv);
    helperText(mRv, "★★★★★", 11, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 14, 12);
    helperText(mRv, `«${{rv.text}}»`, 11.5, "Medium", cDark, 14, 34, 320);
    addImageRect(mRv, rv.av, 14, 90, 32, 32, 16);
    helperText(mRv, rv.name, 12, "Bold", cDark, 54, 92);
    helperText(mRv, rv.car, 10, "Regular", cMuted, 54, 108);
  }});

  // Mobile Footer
  const mFooter = figma.createFrame(); mFooter.resize(390, 180); mFooter.y = 2970; mFooter.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mFooter);
  addSvgNode(mFooter, "logo", 20, 20, 24, 24);
  helperText(mFooter, "ChargeUA", 16, "Bold", cWhite, 52, 23);
  helperText(mFooter, "Національний агрегатор зарядної інфраструктури України.", 11, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 20, 56, 350);
  helperText(mFooter, "0 800 300 400 · support@charge.ua\\n© 2026 ChargeUA · Лемішка Андрій, ПП-24", 10, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 20, 100);

  // Sticky Bottom Navigation (3 Tabs ONLY, NO Profile!)
  const mBottomNav = figma.createFrame(); mBottomNav.resize(390, 54); mBottomNav.y = 3190; mBottomNav.fills = [{{ type: "SOLID", color: cWhite }}]; mBottomNav.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mBottomNav);

  const mBottomNavHome = figma.createFrame();
  mBottomNavHome.resize(115, 54);
  mBottomNavHome.x = 10; mBottomNavHome.y = 0;
  mBottomNavHome.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavHome);
  helperText(mBottomNavHome, "⚡ Головна", 11, "Bold", cPrimary, 25, 18);

  const mBottomNavMap = figma.createFrame();
  mBottomNavMap.resize(115, 54);
  mBottomNavMap.x = 135; mBottomNavMap.y = 0;
  mBottomNavMap.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavMap);
  helperText(mBottomNavMap, "🗺 Карта", 11, "Bold", cDark, 32, 18);

  const mBottomNavCalc = figma.createFrame();
  mBottomNavCalc.resize(115, 54);
  mBottomNavCalc.x = 260; mBottomNavCalc.y = 0;
  mBottomNavCalc.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}];
  mBottomNav.appendChild(mBottomNavCalc);
  helperText(mBottomNavCalc, "🧮 Калькулятор", 11, "Bold", cDark, 15, 18);

  const fCatalog = figma.createFrame();
  fCatalog.name = "08_Catalog_Map";
  fCatalog.resize(1440, 1720);
  fCatalog.x = 3000; fCatalog.y = 2450;
  fCatalog.fills = [{{ type: "SOLID", color: cBgSurface }}];

  // Top Bar & Header
  const catTop = figma.createFrame(); catTop.resize(1440, 40); catTop.fills = [{{ type: "SOLID", color: cDark }}]; fCatalog.appendChild(catTop);
  helperText(catTop, "● Каталог ChargeUA: 480+ станцій онлайн | Жива телеметрія портів", 12, "Medium", cWhite, 60, 12);
  helperText(catTop, "Гаряча лінія: 0 800 300 400", 12, "Medium", cWhite, 1230, 12);

  const catHead = figma.createFrame(); catHead.resize(1440, 76); catHead.y = 40; catHead.fills = [{{ type: "SOLID", color: cWhite }}]; catHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(catHead);
  const catLogo = figma.createFrame(); catLogo.resize(180, 40); catLogo.x = 60; catLogo.y = 18; catLogo.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; catHead.appendChild(catLogo);
  addSvgNode(catLogo, "logo", 0, 2, 36, 36);
  helperText(catLogo, "ChargeUA", 22, "Bold", cPrimary, 45, 6);
  helperText(catHead, "Головна        Калькулятор        Карта станцій        Популярні хаби        Інструкція        Відгуки", 14, "Semi Bold", cDark, 380, 28);
  const catHeadCta = figma.createFrame(); catHeadCta.resize(160, 42); catHeadCta.x = 1220; catHeadCta.y = 17; catHeadCta.cornerRadius = 8; catHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}]; catHead.appendChild(catHeadCta);
  helperText(catHeadCta, "← На головну", 13, "Bold", cWhite, 32, 12);

  // Title
  helperText(fCatalog, "Каталог та інтерактивна карта станцій ChargeUA", 32, "Bold", cDark, 60, 140);
  helperText(fCatalog, "Повний перелік 480+ швидкісних хабів України з живою телеметрією конекторів та фільтром генераторів", 16, "Regular", cMuted, 60, 185);

  // Search & Filters Bar
  const sBar = figma.createFrame(); sBar.resize(1320, 60); sBar.x = 60; sBar.y = 230; sBar.cornerRadius = 12; sBar.fills = [{{ type: "SOLID", color: cWhite }}]; sBar.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(sBar);
  helperText(sBar, "🔍 Пошук за містом, адресою або назвою хабу (наприклад: Київ, Сагайдачного)...", 14, "Regular", cMuted, 24, 20);

  const catChips = ["Всі міста (Київ, Львів, Одеса, Дніпро)", "CCS 2 (160 кВт)", "CHAdeMO", "🔋 Тільки з генератором", "Вільні зараз"];
  catChips.forEach((ch, idx) => {{
    const chF = figma.createFrame(); chF.resize(idx === 0 ? 250 : 160, 34); chF.x = 60 + (idx === 0 ? 0 : 265 + (idx - 1) * 175); chF.y = 305; chF.cornerRadius = 17;
    chF.fills = [{{ type: "SOLID", color: idx === 3 ? cSuccessBg : cWhite }}];
    chF.strokes = [{{ type: "SOLID", color: idx === 3 ? cSuccess : cBorder }}];
    fCatalog.appendChild(chF);
    helperText(chF, ch, 11, "Bold", idx === 3 ? cSuccess : cDark, 14, 9);
  }});

  // 6 Station Cards Grid (2 cols x 3 rows)
  const catalogStationBtns = [];
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
  }});

  // Pagination Bar
  const pag = figma.createFrame(); pag.resize(1320, 50); pag.x = 60; pag.y = 1380; pag.cornerRadius = 8; pag.fills = [{{ type: "SOLID", color: cWhite }}]; pag.strokes = [{{ type: "SOLID", color: cBorder }}]; fCatalog.appendChild(pag);
  helperText(pag, "Показано 1–6 із 480 станцій         ‹   [1]   2   3   4   5   ...   80   ›", 13, "Medium", cDark, 420, 16);

  // Catalog Dark Footer
  const catFooter = figma.createFrame(); catFooter.resize(1440, 260); catFooter.y = 1460; catFooter.fills = [{{ type: "SOLID", color: cDark }}]; fCatalog.appendChild(catFooter);
  addSvgNode(catFooter, "logo", 60, 40, 36, 36);
  helperText(catFooter, "ChargeUA · Каталог станцій", 20, "Bold", cWhite, 105, 44);
  helperText(catFooter, "Покриття усіх областей України. Цілодобова телеметрія та технічна підтримка.", 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 60, 85, 420);
  helperText(catFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 60, 200);

  // FRAME 09: STATION DETAILS (1440 × 1650)
  const fDetails = figma.createFrame();
  fDetails.name = "09_Station_Details";
  fDetails.resize(1440, 1650);
  fDetails.x = 4600; fDetails.y = 2450;
  fDetails.fills = [{{ type: "SOLID", color: cWhite }}];

  // Top Bar & Header
  const detTop = figma.createFrame(); detTop.resize(1440, 40); detTop.fills = [{{ type: "SOLID", color: cDark }}]; fDetails.appendChild(detTop);
  helperText(detTop, "● Деталі хабу | Live-телеметрія CCS2 онлайн", 12, "Medium", cWhite, 60, 12);
  helperText(detTop, "Гаряча лінія: 0 800 300 400", 12, "Medium", cWhite, 1230, 12);

  const detHead = figma.createFrame(); detHead.resize(1440, 76); detHead.y = 40; detHead.fills = [{{ type: "SOLID", color: cWhite }}]; detHead.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detHead);
  const detLogo = figma.createFrame(); detLogo.resize(180, 40); detLogo.x = 60; detLogo.y = 18; detLogo.fills = [{{ type: "SOLID", color: cWhite, opacity: 0.01 }}]; detHead.appendChild(detLogo);
  addSvgNode(detLogo, "logo", 0, 2, 36, 36);
  helperText(detLogo, "ChargeUA", 22, "Bold", cPrimary, 45, 6);
  helperText(detHead, "Головна        Калькулятор        Карта станцій        Популярні хаби        Інструкція        Відгуки", 14, "Semi Bold", cDark, 380, 28);
  const detHeadCta = figma.createFrame(); detHeadCta.resize(160, 42); detHeadCta.x = 1220; detHeadCta.y = 17; detHeadCta.cornerRadius = 8; detHeadCta.fills = [{{ type: "SOLID", color: cPrimary }}]; detHead.appendChild(detHeadCta);
  helperText(detHeadCta, "Назад до карти", 13, "Bold", cWhite, 30, 12);

  // Breadcrumbs
  helperText(fDetails, "Головна   ›   Карта станцій   ›   Київ   ›   Хаб «Київ-Поділ» (вул. Сагайдачного, 12)", 13, "Medium", cMuted, 60, 135);

  // Banner Photo with Live Badge Overlay
  const dPhotoBox = figma.createFrame(); dPhotoBox.resize(1320, 360); dPhotoBox.x = 60; dPhotoBox.y = 165; dPhotoBox.cornerRadius = 16; dPhotoBox.fills = [{{ type: "SOLID", color: cBgSurface }}]; fDetails.appendChild(dPhotoBox);
  addImageRect(dPhotoBox, "hub_kyiv", 0, 0, 1320, 360, 16);

  const photoBadge = figma.createFrame(); photoBadge.resize(280, 36); photoBadge.x = 24; photoBadge.y = 24; photoBadge.cornerRadius = 8; photoBadge.fills = [{{ type: "SOLID", color: cDark }}, {{ type: "SOLID", color: cDark, opacity: 0.85 }}]; dPhotoBox.appendChild(photoBadge);
  helperText(photoBadge, "● 3 з 4 портів вільні | 🔋 Дизель-генератор ON", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 12, 10);

  // Left Column (840px): Info, Telemetry Grid, Specs, Amenities
  helperText(fDetails, "Хаб «Київ-Поділ» · 120 кВт Ultra-Fast", 32, "Bold", cDark, 60, 545);
  helperText(fDetails, "м. Київ, вул. Петра Сагайдачного, 12 · Оператор: ChargeUA Network · Працює цілодобово 24/7", 15, "Regular", cMuted, 60, 588);

  // 4-Port Live Telemetry Grid
  helperText(fDetails, "Живий статус портів зарядної станції (Real-time Telemetry):", 18, "Bold", cDark, 60, 635);
  const portsList = [
    {{ name: "Порт 1 · CCS 2 (120 кВт)", status: "🟢 Вільний (Готовий до підключення)", isFree: true, detail: "DC Ultra-Fast · Макс. струм 300A" }},
    {{ name: "Порт 2 · CCS 2 (120 кВт)", status: "🟡 Зайнятий (Залишилося ~14 хв)", isFree: false, detail: "DC Ultra-Fast · Поточний заряд 78%" }},
    {{ name: "Порт 3 · CHAdeMO (50 кВт)", status: "🟢 Вільний (Готовий до підключення)", isFree: true, detail: "DC Fast · Макс. напруга 500V" }},
    {{ name: "Порт 4 · Type 2 (22 кВт)", status: "🟢 Вільний (Готовий до підключення)", isFree: true, detail: "AC Повільна зарядка · 3 фази 32A" }}
  ];

  portsList.forEach((pt, i) => {{
    const ptCard = figma.createFrame(); ptCard.resize(405, 100); ptCard.x = 60 + (i % 2) * 435; ptCard.y = 675 + Math.floor(i / 2) * 115; ptCard.cornerRadius = 12;
    ptCard.fills = [{{ type: "SOLID", color: pt.isFree ? cSuccessBg : cWarningBg }}];
    ptCard.strokes = [{{ type: "SOLID", color: pt.isFree ? cSuccess : cWarning }}];
    fDetails.appendChild(ptCard);
    helperText(ptCard, pt.name, 14, "Bold", cDark, 16, 16);
    helperText(ptCard, pt.status, 12, "Bold", pt.isFree ? cSuccess : cWarning, 16, 42);
    helperText(ptCard, pt.detail, 11, "Regular", cMuted, 16, 68);
  }});

  // Specs Card
  const detSpecs = figma.createFrame(); detSpecs.resize(840, 180); detSpecs.x = 60; detSpecs.y = 930; detSpecs.cornerRadius = 14; detSpecs.fills = [{{ type: "SOLID", color: cBgSurface }}]; detSpecs.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detSpecs);
  helperText(detSpecs, "Технічні характеристики та надійність:", 16, "Bold", cDark, 24, 20);
  helperText(detSpecs, "• Сумарна потужність: 160 кВт DC + 22 кВт AC (динамічний розподіл потужності)", 13, "Medium", cDark, 24, 52);
  helperText(detSpecs, "• Резервне живлення: Промисловий дизель-генератор Cummins 160 кВт (100% автономність)", 13, "Bold", cSuccess, 24, 80);
  helperText(detSpecs, "• Середній час зарядки (20% → 80%): ~25 хвилин для авто з батареєю 60-80 кВт·год", 13, "Medium", cDark, 24, 108);
  helperText(detSpecs, "• Сумісність: Усі європейські, американські та китайські електрокари (CCS2, Type2, CHAdeMO, GB/T через перехідник)", 13, "Regular", cMuted, 24, 136);

  // Amenities Card
  const detAmen = figma.createFrame(); detAmen.resize(840, 110); detAmen.x = 60; detAmen.y = 1130; detAmen.cornerRadius = 14; detAmen.fills = [{{ type: "SOLID", color: cWhite }}]; detAmen.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detAmen);
  helperText(detAmen, "Зручності на локації (Amenities):", 15, "Bold", cDark, 24, 18);
  helperText(detAmen, "☕ Кав'ярня зі свіжою кавою та випічкою    📶 Безкоштовний швидкісний Wi-Fi 100 Мбіт    🚻 Чиста вбиральня", 13, "Medium", cDark, 24, 48);
  helperText(detAmen, "🛒 Цілодобовий супермаркет поруч        🅿️ Освітлений паркінг під відеонаглядом 24/7", 13, "Medium", cMuted, 24, 76);

  // Right Column (440px): Tariffs & Route Assistant (ZERO booking!)
  const detTariff = figma.createFrame(); detTariff.resize(440, 240); detTariff.x = 940; detTariff.y = 545; detTariff.cornerRadius = 14; detTariff.fills = [{{ type: "SOLID", color: cBgSurface }}]; detTariff.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detTariff);
  helperText(detTariff, "Тарифи на зарядку:", 16, "Bold", cDark, 24, 20);
  helperText(detTariff, "DC Швидка зарядка (CCS2 / CHAdeMO):", 13, "Medium", cMuted, 24, 52);
  helperText(detTariff, "14.50 ₴ / кВт·год", 22, "Bold", cPrimary, 24, 74);
  helperText(detTariff, "AC Повільна зарядка (Type 2):", 13, "Medium", cMuted, 24, 118);
  helperText(detTariff, "9.80 ₴ / кВт·год", 18, "Bold", cDark, 24, 138);
  helperText(detTariff, "• Безкоштовний паркінг під час зарядки + 15 хв після завершення", 11, "Regular", cMuted, 24, 180);

  // Navigation & Assistant Card
  const detNavCard = figma.createFrame(); detNavCard.resize(440, 310); detNavCard.x = 940; detNavCard.y = 805; detNavCard.cornerRadius = 14; detNavCard.fills = [{{ type: "SOLID", color: cWhite }}]; detNavCard.strokes = [{{ type: "SOLID", color: cBorder }}]; fDetails.appendChild(detNavCard);
  helperText(detNavCard, "Помічник навігації ChargeUA", 18, "Bold", cDark, 24, 24);
  helperText(detNavCard, "Прокладіть найшвидший маршрут до вільного порту через навігаційні сервіси без жодних передоплат чи бронювання.", 13, "Regular", cMuted, 24, 56, 390);

  const detRouteBtn = figma.createFrame(); detRouteBtn.resize(392, 48); detRouteBtn.x = 24; detRouteBtn.y = 125; detRouteBtn.cornerRadius = 8; detRouteBtn.fills = [{{ type: "SOLID", color: cPrimary }}]; detNavCard.appendChild(detRouteBtn);
  helperText(detRouteBtn, "Прокласти маршрут (Google Maps / Waze)", 13, "Bold", cWhite, 55, 15);

  const detShareBtn = figma.createFrame(); detShareBtn.resize(392, 44); detShareBtn.x = 24; detShareBtn.y = 185; detShareBtn.cornerRadius = 8; detShareBtn.fills = [{{ type: "SOLID", color: cWhite }}]; detShareBtn.strokes = [{{ type: "SOLID", color: cBorder }}]; detNavCard.appendChild(detShareBtn);
  helperText(detShareBtn, "Поділитися локацією з пасажиром", 13, "Semi Bold", cDark, 85, 13);

  const assistBox = figma.createFrame(); assistBox.resize(392, 50); assistBox.x = 24; assistBox.y = 240; assistBox.cornerRadius = 8; assistBox.fills = [{{ type: "SOLID", color: cSuccessBg }}]; detNavCard.appendChild(assistBox);
  helperText(assistBox, "⚡ Помічник: Порт 1 вільний. Розрахунковий час доїзду: 12 хв.", 11, "Bold", cSuccess, 16, 17);

  // Details Footer
  const detFooter = figma.createFrame(); detFooter.resize(1440, 260); detFooter.y = 1390; detFooter.fills = [{{ type: "SOLID", color: cDark }}]; fDetails.appendChild(detFooter);
  addSvgNode(detFooter, "logo", 60, 40, 36, 36);
  helperText(detFooter, "ChargeUA · Деталі зарядної станції", 20, "Bold", cWhite, 105, 44);
  helperText(detFooter, "Технічні дані оновлюються в режимі реального часу за стандартом OCPP 2.0.1.", 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 60, 85, 420);
  helperText(detFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 60, 200);

  // ==========================================================================
  // НАЛАШТУВАННЯ ІНТЕРАКТИВНОСТІ FIGMA PROTOTYPE (SIMULATION MODE)
  // ==========================================================================

  // 1. Desktop Interactions (Scroll to anchors + Navigate)
  await linkScroll(dHeroBtn1, dCalcSec);
  await linkScroll(dHeroBtn2, dMapSec);
  await linkNodes(dHeadCta, fCatalog);

  // Desktop Header Nav Scroll Links
  await linkScroll(dNavHome, dHero);
  await linkScroll(dNavCalc, dCalcSec);
  await linkScroll(dNavMap, dMapSec);
  await linkScroll(dNavHubs, dFirstStationCard);
  await linkScroll(dNavSteps, dStepsSec);
  await linkScroll(dNavRev, dFirstReviewCard);

  for (const btn of desktopStationBtns) {{
    await linkNodes(btn, fDetails);
  }}

  // 2. Tablet Interactions (Scroll to anchors + Navigate)
  await linkScroll(tBtn1, tCalc);
  await linkScroll(tBtn2, tMapSec);
  await linkScroll(tCalcBtn, tMapSec);
  await linkNodes(tHeadCta, fCatalog);
  for (const btn of tabletStationBtns) {{
    await linkNodes(btn, fDetails);
  }}

  // 3. Mobile Interactions (Burger -> Drawer Overlay, Anchors, Cards -> Details)
  await linkOverlay(mBurgerBtn, fDrawerOverlay);
  await linkScroll(mBtnMap, mMapSec);
  for (const btn of mobileStationBtns) {{
    await linkNodes(btn, fDetails);
  }}
  await linkScroll(mBottomNavHome, mHero);
  await linkScroll(mBottomNavMap, mMapSec);
  await linkScroll(mBottomNavCalc, mCalc);

  // 4. Catalog Interactions
  await linkNodes(catLogo, fDesktop);
  await linkNodes(catHeadCta, fDesktop);
  for (const btn of catalogStationBtns) {{
    await linkNodes(btn, fDetails);
  }}

  // 5. Station Details Interactions
  await linkNodes(detLogo, fDesktop);
  await linkNodes(detHeadCta, fCatalog);
  await linkOverlay(detRouteBtn, fModalOverlay);

  // 6. Overlays Interactions
  await linkClose(drawerCloseBtn);
  await linkClose(drawerCloseX);
  await linkScroll(drawerLinkHome, mHero);
  await linkScroll(drawerLinkCalc, mCalc);
  await linkScroll(drawerLinkMap, mMapSec);
  await linkScroll(drawerLinkStations, mFirstStationCard);
  await linkScroll(drawerLinkSteps, mFirstStep);
  await linkScroll(drawerLinkReviews, mFirstReview);
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
  figma.notify("🎉 Готово! Усі 12 фреймів ChargeUA, вектори, фотографії та симуляція Prototype успішно налаштовані!");
}}

run();
"""

with open(OUT_PLUGIN, "w", encoding="utf-8") as f:
    f.write(js_code)

with open(OUT_CODE, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Generated {OUT_PLUGIN} ({len(js_code)} bytes)")
print(f"Generated {OUT_CODE} ({len(js_code)} bytes)")
