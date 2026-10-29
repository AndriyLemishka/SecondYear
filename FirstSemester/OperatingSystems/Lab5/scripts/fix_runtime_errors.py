# -*- coding: utf-8 -*-
HTML_PATH = r"D:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5\Explenation material\index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    c = f.read()

# Fix filterGlossary implementation
old_fg = """    function filterGlossary(cat) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      if (event && event.currentTarget) event.currentTarget.classList.add('active');

      const list = document.getElementById('glossaryList');
      if (!list) return;
      list.innerHTML = '';
      const filtered = cat === 'all' ? glossaryData : glossaryData.filter(i => i.cat === cat);
      filtered.forEach(item => {
        const div = document.createElement('div');
        div.className = 'glossary-item';
        div.innerHTML = `<div class="glossary-term">${item.term}</div><div class="glossary-desc">${item.desc}</div>`;
        list.appendChild(div);
      });
    }"""

new_fg = """    function filterGlossary(cat, clickedBtn) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      if (clickedBtn && clickedBtn.classList) {
        clickedBtn.classList.add('active');
      } else if (typeof window !== 'undefined' && window.event && window.event.currentTarget && window.event.currentTarget.classList) {
        window.event.currentTarget.classList.add('active');
      } else {
        const defaultBtn = document.querySelector('.filter-btn');
        if (defaultBtn) defaultBtn.classList.add('active');
      }

      const list = document.getElementById('glossaryList');
      if (!list) return;
      list.innerHTML = '';
      const filtered = cat === 'all' ? glossaryData : glossaryData.filter(i => i.cat === cat);
      filtered.forEach(item => {
        const div = document.createElement('div');
        div.className = 'glossary-item';
        div.innerHTML = `<div class="glossary-term">${item.term}</div><div class="glossary-desc">${item.desc}</div>`;
        list.appendChild(div);
      });
    }"""

if old_fg in c:
    c = c.replace(old_fg, new_fg)
else:
    print("WARNING: old_fg not found exactly")

# Fix showNodeDetails implementation
old_snd = """    function showNodeDetails(key) {
      document.querySelectorAll('.tree-node').forEach(n => n.classList.remove('selected'));
      if (event && event.currentTarget) event.currentTarget.classList.add('selected');
      const item = nodeData[key];
      const box = document.getElementById('adNodeInfo');
      if (box && item) {
        box.innerHTML = `<strong>${item.title}</strong><p style="margin-top:6px;">${item.desc}</p>`;
      }
    }"""

new_snd = """    function showNodeDetails(key, clickedNode) {
      document.querySelectorAll('.tree-node').forEach(n => n.classList.remove('selected'));
      if (clickedNode && clickedNode.classList) {
        clickedNode.classList.add('selected');
      } else if (typeof window !== 'undefined' && window.event && window.event.currentTarget && window.event.currentTarget.classList) {
        window.event.currentTarget.classList.add('selected');
      }
      const item = nodeData[key];
      const box = document.getElementById('adNodeInfo');
      if (box && item) {
        box.innerHTML = `<strong>${item.title}</strong><p style="margin-top:6px;">${item.desc}</p>`;
      }
    }"""

if old_snd in c:
    c = c.replace(old_snd, new_snd)
else:
    print("WARNING: old_snd not found exactly")

# Update HTML calls in glossary buttons
c = c.replace("onclick=\"filterGlossary('all')\"", "onclick=\"filterGlossary('all', this)\"")
c = c.replace("onclick=\"filterGlossary('ad')\"", "onclick=\"filterGlossary('ad', this)\"")
c = c.replace("onclick=\"filterGlossary('net')\"", "onclick=\"filterGlossary('net', this)\"")
c = c.replace("onclick=\"filterGlossary('sec')\"", "onclick=\"filterGlossary('sec', this)\"")
c = c.replace("onclick=\"filterGlossary('storage')\"", "onclick=\"filterGlossary('storage', this)\"")

# Update HTML calls in AD tree
c = c.replace("onclick=\"showNodeDetails('forest')\"", "onclick=\"showNodeDetails('forest', this)\"")
c = c.replace("onclick=\"showNodeDetails('domain')\"", "onclick=\"showNodeDetails('domain', this)\"")
c = c.replace("onclick=\"showNodeDetails('ou_fin')\"", "onclick=\"showNodeDetails('ou_fin', this)\"")
c = c.replace("onclick=\"showNodeDetails('ou_it')\"", "onclick=\"showNodeDetails('ou_it', this)\"")
c = c.replace("onclick=\"showNodeDetails('ou_groups')\"", "onclick=\"showNodeDetails('ou_groups', this)\"")

# Update nav button label for Tab 0 so it's clean and doesn't wrap awkwardly
c = c.replace(
    '<button class="nav-btn active" data-tab="tab-basics"><span class="nav-icon">💡</span> 0. Базис: Сервер, IP, DNS, Шлюз</button>',
    '<button class="nav-btn active" data-tab="tab-basics"><span class="nav-icon">💡</span> 0. Мережевий базис (IP, DNS)</button>'
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated HTML and safe handlers.")
