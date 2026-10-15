/**
 * ChargeUA — Модуль мобільної навігації (Hamburger Menu)
 * Забезпечує доступність (WCAG 2.2), керування aria-expanded, фокусом та Escape
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('.site-header');
    const burgerBtn = document.getElementById('burger-btn');
    const nav = document.getElementById('site-nav');

    if (!burgerBtn || !nav) return;

    function openNav() {
      burgerBtn.setAttribute('aria-expanded', 'true');
      header.classList.add('nav-open');
      nav.classList.add('is-open');
      document.body.classList.add('nav-locked');
    }

    function closeNav() {
      burgerBtn.setAttribute('aria-expanded', 'false');
      header.classList.remove('nav-open');
      nav.classList.remove('is-open');
      document.body.classList.remove('nav-locked');
    }

    function toggleNav() {
      const isExpanded = burgerBtn.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeNav();
      } else {
        openNav();
      }
    }

    burgerBtn.addEventListener('click', toggleNav);

    // Закриття меню при кліку на посилання навігації
    const navLinks = nav.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', function () {
        closeNav();
      });
    });

    // Закриття меню клавішею Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        closeNav();
        burgerBtn.focus();
      }
    });

    // Автоматичне закриття при зміні розміру вікна вище 1160px
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1160 && nav.classList.contains('is-open')) {
        closeNav();
      }
    });
  });
})();
