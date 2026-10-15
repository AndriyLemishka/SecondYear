const fs = require('fs');
const allInteractiveNodes = [];

class MockNode {
  static idCounter = 1;
  constructor(type) {
    this.id = 'node_' + (MockNode.idCounter++);
    this.type = type;
    this.children = [];
    this.width = 100;
    this.height = 100;
    this.x = 0;
    this.y = 0;
    this.fills = [];
    this.strokes = [];
    this.name = '';
    this.reactions = [];
  }
  async setReactionsAsync(r) {
    this.reactions = r;
    allInteractiveNodes.push(this);
  }
  appendChild(child) {
    this.children.push(child);
  }
  resize(w, h) {
    this.width = w;
    this.height = h;
  }
}

const rootChildren = [];
const mockFigma = {
  notify: (msg) => console.log('FIGMA NOTIFY:', msg),
  loadFontAsync: async (f) => {},
  createImage: (bytes) => ({ hash: 'mock_hash_' + bytes.length }),
  createText: () => new MockNode('TEXT'),
  createRectangle: () => new MockNode('RECTANGLE'),
  createFrame: () => {
    const f = new MockNode('FRAME');
    rootChildren.push(f);
    return f;
  },
  createNodeFromSvg: (svg) => new MockNode('FRAME_SVG'),
  currentPage: {
    children: rootChildren,
    flowStartingPoints: [],
    appendChild: (n) => {
      if (!rootChildren.includes(n)) rootChildren.push(n);
    }
  },
  viewport: {
    scrollAndZoomIntoView: (nodes) => console.log('Zoomed into view, nodes count:', nodes.length)
  }
};

global.figma = mockFigma;

let code = fs.readFileSync('d:/Studing/SecondYear/FirstSemester/web/lab4/05_figma_exports/figma_builder_plugin.js', 'utf8');

eval(code);

run().then(() => {
  console.log('>>> ALL FRAMES & ASSETS BUILT COMPLETELY WITH 0 ERRORS! <<<');
  console.log('Flow starting points:', mockFigma.currentPage.flowStartingPoints);
  console.log('Interactive prototype nodes count:', allInteractiveNodes.length);
  allInteractiveNodes.forEach((node, i) => {
    console.log(`  [${i+1}] Node ID: ${node.id}, trigger: ${node.reactions[0]?.trigger?.type}, action: ${JSON.stringify(node.reactions[0]?.action)}`);
  });
}).catch(err => {
  console.error('FAILED AT RUNTIME:', err);
});

