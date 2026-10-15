# -*- coding: utf-8 -*-
import sys, re

print("Starting layout and navigation fixes with precise marker indices...")

# ==============================================================================
# 1. PATCH generate_final_figma_plugin.py
# ==============================================================================
with open("lab4/08_scratch/generate_final_figma_plugin.py", "r", encoding="utf-8") as f:
    plugin_src = f.read()

# 1.1 Drawer Overlay (10_Overlay_Drawer)
pos_drw_start = plugin_src.find('  const drawerLinkTariff = figma.createFrame();')
pos_drw_end = plugin_src.find('  const drawerCloseBtn = figma.createFrame();')
assert pos_drw_start != -1 and pos_drw_end != -1, "Drawer link positions not found"

new_drawer_links = '''  const drawerLinkStations = figma.createFrame();
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

'''
plugin_src = plugin_src[:pos_drw_start] + new_drawer_links + plugin_src[pos_drw_end:]

# 1.2 Desktop Header Navigation
plugin_src = re.sub(
    r'helperText\(dHead,\s*"Головна\s+Калькулятор\s+Карта станцій\s+Тарифи\s+Для бізнесу",\s*14,\s*"Semi Bold",\s*cDark,\s*\d+,\s*28\);',
    'helperText(dHead, "Головна        Калькулятор        Карта станцій        Популярні хаби        Інструкція        Відгуки", 14, "Semi Bold", cDark, 380, 28);',
    plugin_src
)

# 1.3 Desktop B2B Form & Footer removal/update
pos_d_b2b = plugin_src.find('  // B2B Lead Form')
pos_d_tab = plugin_src.find('  // FRAME 06: FULL TABLET')
assert pos_d_b2b != -1 and pos_d_tab != -1, "Desktop B2B / Tablet boundary not found"

new_d_footer = '''  // Desktop Footer (Без B2B форми, чиста навігація)
  const dFooter = figma.createFrame();
  dFooter.resize(1440, 320);
  dFooter.y = 3190;
  dFooter.fills = [{{ type: "SOLID", color: cDark }}];
  fDesktop.appendChild(dFooter);

  addSvgNode(dFooter, "logo", 60, 45, 38, 38);
  helperText(dFooter, "ChargeUA", 24, "Bold", cWhite, 110, 50);
  helperText(dFooter, "Національний агрегатор та веб-помічник зарядної інфраструктури України.\\\\nШвидкий пошук та моніторинг станцій у блекаути.", 13, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 60, 100, 380);

  helperText(dFooter, "Навігація\\\\n\\\\nГоловна\\\\nКалькулятор\\\\nLive-карта", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 560, 50);
  helperText(dFooter, "Розділи сайту\\\\n\\\\nПопулярні хаби\\\\nЯк зарядитися (3 кроки)\\\\nВідгуки водіїв", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 780, 50);
  helperText(dFooter, "Підтримка 24/7\\\\n\\\\n0 800 300 400\\\\nsupport@charge.ua\\\\nм. Київ, вул. Сагайдачного, 12", 13, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 1040, 50);

  const dFootLine = figma.createFrame(); dFootLine.resize(1320, 1); dFootLine.x = 60; dFootLine.y = 240; dFootLine.fills = [{{ type: "SOLID", color: {{ r: 30/255, g: 41/255, b: 59/255 }} }}]; dFooter.appendChild(dFootLine);
  helperText(dFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24 · Кафедра САПР, НУ «Львівська політехніка»", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 60, 265);
  helperText(dFooter, "Всі системи онлайн (100% Uptime)", 12, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 1120, 265);

'''
plugin_src = plugin_src[:pos_d_b2b] + new_d_footer + plugin_src[pos_d_tab:]
plugin_src = plugin_src.replace('fDesktop.resize(1440, 3800);', 'fDesktop.resize(1440, 3520);', 1)

# 1.4 Tablet Header Navigation & Removal of B2B Form
plugin_src = re.sub(
    r'helperText\(tHead,\s*"Головна\s+Калькулятор\s+Карта\s+Тарифи",\s*13,\s*"Semi Bold",\s*cDark,\s*\d+,\s*26\);',
    'helperText(tHead, "Головна     Калькулятор     Карта     Хаби     Відгуки", 13, "Semi Bold", cDark, 240, 26);',
    plugin_src
)

pos_t_b2b = plugin_src.find('  // Tablet B2B Form')
pos_t_mob = plugin_src.find('  // FRAME 07: FULL MOBILE')
assert pos_t_b2b != -1 and pos_t_mob != -1, "Tablet B2B / Mobile boundary not found"

new_t_footer = '''  // Tablet Footer (Чиста навігація)
  const tFooter = figma.createFrame(); tFooter.resize(768, 260); tFooter.y = 2770; tFooter.fills = [{{ type: "SOLID", color: cDark }}]; fTablet.appendChild(tFooter);
  addSvgNode(tFooter, "logo", 30, 35, 32, 32);
  helperText(tFooter, "ChargeUA", 20, "Bold", cWhite, 72, 40);
  helperText(tFooter, "Національний агрегатор зарядної інфраструктури України.", 12, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 30, 80, 260);
  helperText(tFooter, "Навігація:\\\\n• Головна\\\\n• Калькулятор\\\\n• Live-карта\\\\n• Відгуки", 12, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 330, 40);
  helperText(tFooter, "Контакти:\\\\n• 0 800 300 400\\\\n• support@charge.ua\\\\n• м. Київ, Сагайдачного 12", 12, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 530, 40);
  helperText(tFooter, "© 2026 ChargeUA · Лемішка Андрій, ПП-24", 11, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 30, 210);

'''
plugin_src = plugin_src[:pos_t_b2b] + new_t_footer + plugin_src[pos_t_mob:]
plugin_src = plugin_src.replace('fTablet.resize(768, 3280);', 'fTablet.resize(768, 3040);', 1)

# 1.5 Mobile: Live Map IMMEDIATELY AFTER Calculator, then Stations, then Generator, then Steps, then Reviews, then Footer!
pos_m_start = plugin_src.find('  // Mobile Station Cards (2 cards)')
pos_m_end = plugin_src.find('  // Sticky Bottom Navigation')
assert pos_m_start != -1 and pos_m_end != -1, "Mobile sections boundary not found"

new_m_sections = '''  // Mobile Map Section (ОДРАЗУ ПІСЛЯ КАЛЬКУЛЯТОРА!)
  const mMapSec = figma.createFrame(); mMapSec.resize(350, 200); mMapSec.x = 20; mMapSec.y = 795; mMapSec.cornerRadius = 14; mMapSec.fills = [{{ type: "SOLID", color: cBgSurface }}]; mMapSec.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mMapSec);
  addImageRect(mMapSec, "map_lviv", 0, 0, 350, 200, 14);
  helperText(mMapSec, "Live-карта зарядної мережі", 15, "Bold", cDark, 16, 16);
  mapPinsData.slice(0, 2).forEach((pin, pidx) => {{
    const mp = figma.createFrame(); mp.resize(180, 22); mp.x = 16; mp.y = 110 + pidx * 35; mp.cornerRadius = 4; mp.fills = [{{ type: "SOLID", color: cDark }}]; mMapSec.appendChild(mp);
    helperText(mp, pin.name.slice(0, 22) + "...", 9, "Bold", cWhite, 6, 5);
  }});

  // Mobile Station Cards (2 cards - після карти)
  helperText(fMobile, "Популярні зарядні хаби", 18, "Bold", cDark, 20, 1015);
  const mobileStationBtns = [];
  stationsData.slice(0, 2).forEach((st, idx) => {{
    const mSc = figma.createFrame(); mSc.resize(350, 280); mSc.x = 20; mSc.y = 1050 + idx * 295; mSc.cornerRadius = 14; mSc.fills = [{{ type: "SOLID", color: cWhite }}]; mSc.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSc);
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
  const mGenSec = figma.createFrame(); mGenSec.resize(350, 240); mGenSec.x = 20; mGenSec.y = 1655; mGenSec.cornerRadius = 14; mGenSec.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mGenSec);
  addImageRect(mGenSec, "generator", 0, 0, 350, 110, 0);
  helperText(mGenSec, "⚡ Резервне живлення 160 кВт", 11, "Bold", {{ r: 74/255, g: 222/255, b: 128/255 }}, 16, 125);
  helperText(mGenSec, "180+ станцій працюють під час блекаутів", 14, "Bold", cWhite, 16, 145);
  helperText(mGenSec, "Автоматичний генератор гарантує швидку зарядку навіть у разі аварійних вимкнень.", 11, "Regular", {{ r: 203/255, g: 213/255, b: 225/255 }}, 16, 175, 318);

  // Mobile Steps (Як зарядитися за 3 кроки)
  helperText(fMobile, "Як зарядитися за 3 кроки", 18, "Bold", cDark, 20, 1915);
  stepsList.forEach((sp, idx) => {{
    const mSt = figma.createFrame(); mSt.resize(350, 70); mSt.x = 20; mSt.y = 1950 + idx * 80; mSt.cornerRadius = 10; mSt.fills = [{{ type: "SOLID", color: cBgSurface }}]; mSt.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mSt);
    const mCirc = figma.createFrame(); mCirc.resize(30, 30); mCirc.x = 14; mCirc.y = 20; mCirc.cornerRadius = 15; mCirc.fills = [{{ type: "SOLID", color: cPrimary }}]; mSt.appendChild(mCirc);
    helperText(mCirc, sp.num, 13, "Bold", cWhite, 10, 7);
    helperText(mSt, sp.title, 13, "Bold", cDark, 54, 16);
    helperText(mSt, sp.desc, 11, "Regular", cMuted, 54, 38, 280);
  }});

  // Mobile Reviews (Відгуки)
  helperText(fMobile, "Відгуки водіїв", 18, "Bold", cDark, 20, 2210);
  reviewsList.slice(0, 2).forEach((rv, idx) => {{
    const mRv = figma.createFrame(); mRv.resize(350, 140); mRv.x = 20; mRv.y = 2245 + idx * 150; mRv.cornerRadius = 12; mRv.fills = [{{ type: "SOLID", color: cWhite }}]; mRv.strokes = [{{ type: "SOLID", color: cBorder }}]; fMobile.appendChild(mRv);
    helperText(mRv, "★★★★★", 11, "Bold", {{ r: 245/255, g: 158/255, b: 11/255 }}, 14, 12);
    helperText(mRv, `«${{rv.text}}»`, 11.5, "Medium", cDark, 14, 34, 320);
    addImageRect(mRv, rv.av, 14, 90, 32, 32, 16);
    helperText(mRv, rv.name, 12, "Bold", cDark, 54, 92);
    helperText(mRv, rv.car, 10, "Regular", cMuted, 54, 108);
  }});

  // Mobile Footer (Без форми B2B)
  const mFooter = figma.createFrame(); mFooter.resize(390, 180); mFooter.y = 2560; mFooter.fills = [{{ type: "SOLID", color: cDark }}]; fMobile.appendChild(mFooter);
  addSvgNode(mFooter, "logo", 20, 20, 24, 24);
  helperText(mFooter, "ChargeUA", 16, "Bold", cWhite, 52, 23);
  helperText(mFooter, "Національний агрегатор зарядної інфраструктури України.", 11, "Regular", {{ r: 148/255, g: 163/255, b: 184/255 }}, 20, 56, 350);
  helperText(mFooter, "0 800 300 400 · support@charge.ua\\\\n© 2026 ChargeUA · Лемішка Андрій, ПП-24", 10, "Regular", {{ r: 100/255, g: 116/255, b: 139/255 }}, 20, 100);

'''

plugin_src = plugin_src[:pos_m_start] + new_m_sections + plugin_src[pos_m_end:]
plugin_src = plugin_src.replace('mBottomNav.y = 2970;', 'mBottomNav.y = 2740;')
plugin_src = plugin_src.replace('fMobile.resize(390, 2990);', 'fMobile.resize(390, 2800);', 1)

# 1.6 Header links in Catalog, Details & Wireframe
plugin_src = re.sub(
    r'helperText\(catHead,\s*"Головна\s+Калькулятор\s+Карта станцій\s+Тарифи\s+Для бізнесу",\s*14,\s*"Semi Bold",\s*cDark,\s*\d+,\s*28\);',
    'helperText(catHead, "Головна        Калькулятор        Карта станцій        Популярні хаби        Інструкція        Відгуки", 14, "Semi Bold", cDark, 380, 28);',
    plugin_src
)
plugin_src = re.sub(
    r'helperText\(detHead,\s*"Головна\s+Калькулятор\s+Карта станцій\s+Тарифи\s+Для бізнесу",\s*14,\s*"Semi Bold",\s*cDark,\s*\d+,\s*28\);',
    'helperText(detHead, "Головна        Калькулятор        Карта станцій        Популярні хаби        Інструкція        Відгуки", 14, "Semi Bold", cDark, 380, 28);',
    plugin_src
)

# 1.7 Interactivity links for drawer
old_drw_links_call = '''  await linkNodes(drawerLinkHome, fMobile);
  await linkNodes(drawerLinkMap, fCatalog);'''

new_drw_links_call = '''  await linkNodes(drawerLinkHome, fMobile);
  await linkNodes(drawerLinkCalc, fMobile);
  await linkNodes(drawerLinkMap, fCatalog);
  await linkNodes(drawerLinkStations, fCatalog);
  await linkNodes(drawerLinkSteps, fMobile);
  await linkNodes(drawerLinkReviews, fMobile);'''

assert old_drw_links_call in plugin_src, "old_drw_links_call not found"
plugin_src = plugin_src.replace(old_drw_links_call, new_drw_links_call, 1)

with open("lab4/08_scratch/generate_final_figma_plugin.py", "w", encoding="utf-8") as f:
    f.write(plugin_src)

print("SUCCESS: generate_final_figma_plugin.py updated perfectly!")

# ==============================================================================
# 2. PATCH render_new_clean_figures.py
# ==============================================================================
with open("lab4/08_scratch/render_new_clean_figures.py", "r", encoding="utf-8") as f:
    render_src = f.read()

# Remove B2B form from Desktop Bottom
pos_b2b_start = render_src.find('  <!-- B2B LEAD FORM -->')
pos_b2b_end = render_src.find('  <!-- FOOTER -->')
if pos_b2b_start != -1 and pos_b2b_end != -1:
    render_src = render_src[:pos_b2b_start] + render_src[pos_b2b_end:]

# Replace "Для бізнесу" in desktop footer
render_src = re.sub(
    r'<div class="f-col-title">Для бізнесу</div>\s*<div class="f-col-links">.*?</div>',
    '<div class="f-col-title">Розділи сайту</div>\n        <div class="f-col-links">\n          <span>Популярні хаби</span>\n          <span>Як зарядитися (3 кроки)</span>\n          <span>Відгуки водіїв</span>\n          <span>Гарантія Uptime 100%</span>\n        </div>',
    render_src,
    flags=re.DOTALL
)

# Update Tablet Body: map right after calc, remove b2b
pos_t_hubs = render_src.find('  <section class="hubs-sec">\n    <h2 class="sec-heading">Популярні зарядні хаби</h2>')
pos_t_gen = render_src.find('  <section class="gen-sec">')
if pos_t_hubs != -1 and pos_t_gen != -1:
    tablet_hubs_and_map = render_src[pos_t_hubs:pos_t_gen]
    # Check if map is inside
    pos_m_in_t = tablet_hubs_and_map.find('  <section class="map-sec">')
    if pos_m_in_t != -1:
        t_hubs_part = tablet_hubs_and_map[:pos_m_in_t]
        t_map_part = tablet_hubs_and_map[pos_m_in_t:]
        # Swap so map comes before hubs!
        new_t_hubs_map = t_map_part + "\n" + t_hubs_part
        render_src = render_src[:pos_t_hubs] + new_t_hubs_map + render_src[pos_t_gen:]

# Remove B2B from tablet
pos_t_b2b = render_src.find('  <section class="b2b-sec">')
pos_t_foot = render_src.find('  <div class="footer">')
if pos_t_b2b != -1 and pos_t_foot != -1 and pos_t_b2b < pos_t_foot:
    render_src = render_src[:pos_t_b2b] + render_src[pos_t_foot:]

# Update Mobile Body: map right after calc, remove b2b
# In mobile, find hubs-sec and gen-sec
last_pos_hubs = render_src.rfind('  <section class="hubs-sec">\n    <h2 class="sec-heading">Популярні зарядні хаби</h2>')
last_pos_gen = render_src.rfind('  <section class="gen-sec">')
if last_pos_hubs != -1 and last_pos_gen != -1:
    mob_hubs_and_map = render_src[last_pos_hubs:last_pos_gen]
    pos_m_in_m = mob_hubs_and_map.find('  <section class="map-sec">')
    if pos_m_in_m != -1:
        m_hubs_part = mob_hubs_and_map[:pos_m_in_m]
        m_map_part = mob_hubs_and_map[pos_m_in_m:]
        new_m_hubs_map = m_map_part + "\n" + m_hubs_part
        render_src = render_src[:last_pos_hubs] + new_m_hubs_map + render_src[last_pos_gen:]

# Remove B2B from mobile
last_pos_b2b = render_src.rfind('  <section class="b2b-sec">')
last_pos_foot = render_src.rfind('  <div class="footer">')
if last_pos_b2b != -1 and last_pos_foot != -1 and last_pos_b2b < last_pos_foot:
    render_src = render_src[:last_pos_b2b] + render_src[last_pos_foot:]

# Adjust render heights
render_src = render_src.replace('render_chrome(f14_path, out_f14, 1440, 2200, scale=1.5)', 'render_chrome(f14_path, out_f14, 1440, 1850, scale=1.5)')
render_src = render_src.replace('render_chrome(f15_path, temp_tablet, 768, 3300, scale=1.5)', 'render_chrome(f15_path, temp_tablet, 768, 2900, scale=1.5)')
render_src = render_src.replace('render_chrome(f16_path, temp_mobile, 390, 3600, scale=1.5)', 'render_chrome(f16_path, temp_mobile, 390, 3100, scale=1.5)')

with open("lab4/08_scratch/render_new_clean_figures.py", "w", encoding="utf-8") as f:
    f.write(render_src)

print("SUCCESS: render_new_clean_figures.py updated!")
