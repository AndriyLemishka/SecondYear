with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  function addSvgNode(parent, svgKey, x, y, targetWidth = null, targetHeight = null) {
    try {
      const node = figma.createNodeFromSvg(SVG_ASSETS[svgKey]);
      node.x = x;
      node.y = y;
      if (targetWidth && targetHeight) {
        node.rescale(targetWidth / node.width);
      }
      parent.appendChild(node);
      return node;
    } catch (e) {
      console.warn("SVG error for", svgKey, e);
      return null;
    }
  }"""

replacement = """  function addSvgNode(parent, svgKey, x, y, targetWidth = null, targetHeight = null) {
    try {
      if (!SVG_ASSETS[svgKey]) return null;
      const node = figma.createNodeFromSvg(SVG_ASSETS[svgKey]);
      node.x = x;
      node.y = y;
      if (targetWidth && targetHeight && node.width > 0 && node.height > 0) {
        function makeScalable(n) {
          if ('constraints' in n) {
            n.constraints = { horizontal: "SCALE", vertical: "SCALE" };
          }
          if ('children' in n && Array.isArray(n.children)) {
            for (const ch of n.children) makeScalable(ch);
          }
        }
        makeScalable(node);
        node.resize(targetWidth, targetHeight);
      }
      parent.appendChild(node);
      return node;
    } catch (e) {
      console.warn("SVG error for", svgKey, e);
      return null;
    }
  }"""

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\figma_builder_plugin.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
    with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\charge\code.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
    with open(r'd:\Studing\SecondYear\FirstSemester\web\lab4\05_figma_exports\charge\code.ts', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESS: Updated all 3 figma plugin files!")
else:
    print("ERROR: target block not found")
