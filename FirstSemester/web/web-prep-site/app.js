document.addEventListener('DOMContentLoaded', () => {
  // Theme toggle
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('theme') || (prefersDark ? 'dark' : 'light');
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  });

  function updateThemeIcon(theme) {
    themeToggle.innerHTML = theme === 'dark' ? '☀️ Світла' : '🌙 Темна';
  }

  // Sidebar navigation highlight on scroll
  const navLinks = document.querySelectorAll('.sidebar .nav-item');
  const sections = document.querySelectorAll('.lecture-block, #tools, #quiz');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 120;

    sections.forEach(sec => {
      if (sec.offsetTop <= scrollPos) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // Live search
  const searchInput = document.getElementById('search-input');
  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    const cards = document.querySelectorAll('.card, .exam-box');

    if (!query) {
      cards.forEach(c => c.style.display = '');
      document.querySelectorAll('.lecture-block').forEach(b => b.style.display = '');
      return;
    }

    document.querySelectorAll('.lecture-block').forEach(block => {
      let hasMatch = false;
      const blockCards = block.querySelectorAll('.card, .exam-box');
      blockCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(query)) {
          card.style.display = '';
          hasMatch = true;
        } else {
          card.style.display = 'none';
        }
      });
      block.style.display = hasMatch ? '' : 'none';
    });
  });

  // Task 13: Interactive Color Converter & Diagram
  const colorSelect = document.getElementById('color-preset');
  const alphaSlider = document.getElementById('alpha-slider');
  const alphaValSpan = document.getElementById('alpha-val');
  
  const rgbOut = document.getElementById('out-rgb');
  const rgbaOut = document.getElementById('out-rgba');
  const hexOut = document.getElementById('out-hex');
  const hexAlphaOut = document.getElementById('out-hexalpha');
  const swatchBox = document.getElementById('color-swatch');

  const colorMap = {
    white: { r: 255, g: 255, b: 255, name: 'White' },
    black: { r: 0, g: 0, b: 0, name: 'Black' },
    red: { r: 255, g: 0, b: 0, name: 'Red' },
    green: { r: 0, g: 255, b: 0, name: 'Green' },
    blue: { r: 0, g: 0, b: 255, name: 'Blue' },
    magenta: { r: 255, g: 0, b: 255, name: 'Magenta' },
    yellow: { r: 255, g: 255, b: 0, name: 'Yellow' },
    cyan: { r: 0, g: 255, b: 255, name: 'Cyan' }
  };

  function updateColorCalc() {
    const key = colorSelect.value;
    const c = colorMap[key];
    const alphaPct = parseInt(alphaSlider.value, 10);
    const alphaDecimal = (alphaPct / 100).toFixed(2);
    const alphaHexNum = Math.round((alphaPct / 100) * 255);
    const alphaHex = alphaHexNum.toString(16).padStart(2, '0').toUpperCase();

    const rHex = c.r.toString(16).padStart(2, '0');
    const gHex = c.g.toString(16).padStart(2, '0');
    const bHex = c.b.toString(16).padStart(2, '0');
    const hexBase = `#${rHex}${gHex}${bHex}`;

    alphaValSpan.textContent = `${alphaPct}%`;

    rgbOut.textContent = `rgb(${c.r}, ${c.g}, ${c.b})`;
    rgbaOut.textContent = `rgba(${c.r}, ${c.g}, ${c.b}, ${alphaDecimal == '1.00' ? '1' : (alphaDecimal == '0.00' ? '0' : alphaDecimal.replace(/\.?0+$/, ''))})`;
    hexOut.textContent = hexBase;
    hexAlphaOut.textContent = `${hexBase}${alphaHex}`;

    swatchBox.style.background = `rgba(${c.r}, ${c.g}, ${c.b}, ${alphaPct / 100})`;
    swatchBox.style.color = (c.r * 0.299 + c.g * 0.587 + c.b * 0.114) > 140 ? '#000' : '#fff';

    // Highlight diagram circles
    highlightDiagram(key);
  }

  function highlightDiagram(activeColor) {
    const circles = ['circle-r', 'circle-g', 'circle-b'];
    circles.forEach(id => {
      const el = document.getElementById(id);
      if (el) el.setAttribute('stroke-width', '1');
    });

    if (activeColor === 'red') document.getElementById('circle-r')?.setAttribute('stroke-width', '4');
    if (activeColor === 'green') document.getElementById('circle-g')?.setAttribute('stroke-width', '4');
    if (activeColor === 'blue') document.getElementById('circle-b')?.setAttribute('stroke-width', '4');
  }

  colorSelect.addEventListener('change', updateColorCalc);
  alphaSlider.addEventListener('input', updateColorCalc);
  updateColorCalc();

  // Task 14: Interactive Flexbox Sandbox
  const flexJustify = document.getElementById('flex-justify');
  const flexAlign = document.getElementById('flex-align');
  const flexDir = document.getElementById('flex-dir');
  const flexContainer = document.getElementById('demo-flex-container');

  function updateFlexDemo() {
    flexContainer.style.justifyContent = flexJustify.value;
    flexContainer.style.alignItems = flexAlign.value;
    flexContainer.style.flexDirection = flexDir.value;
  }

  flexJustify.addEventListener('change', updateFlexDemo);
  flexAlign.addEventListener('change', updateFlexDemo);
  flexDir.addEventListener('change', updateFlexDemo);

  // Quiz evaluation
  const quizItems = document.querySelectorAll('.quiz-item');
  quizItems.forEach(item => {
    const options = item.querySelectorAll('.quiz-opt');
    const feedback = item.querySelector('.quiz-feedback');
    const correctIdx = parseInt(item.getAttribute('data-correct'), 10);

    options.forEach((opt, idx) => {
      opt.addEventListener('click', () => {
        // Clear previous state for this question
        options.forEach(o => {
          o.classList.remove('correct', 'wrong');
        });

        if (idx === correctIdx) {
          opt.classList.add('correct');
          feedback.textContent = '✓ Правильно! Чудова робота.';
          feedback.style.background = 'rgba(16, 185, 129, 0.15)';
          feedback.style.color = 'var(--success)';
        } else {
          opt.classList.add('wrong');
          options[correctIdx].classList.add('correct');
          feedback.textContent = '✗ Невірно. Правильну відповідь підсвічено зеленим.';
          feedback.style.background = 'rgba(239, 68, 68, 0.15)';
          feedback.style.color = 'var(--danger)';
        }
        feedback.classList.add('show');
      });
    });
  });
});
