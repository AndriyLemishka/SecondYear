/**
 * ChargeUA — Модуль мобільної навігації (Header Hamburger Menu)
 * Відповідає стандартам W3C WAI-ARIA
 */
document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu-toggle');
  const mobileNav = document.getElementById('mobile-menu');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', String(!isExpanded));
      mobileNav.classList.toggle('hidden');
    });

    // Закриття при кліку на посилання
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.setAttribute('aria-expanded', 'false');
        mobileNav.classList.add('hidden');
      });
    });
  }
});
