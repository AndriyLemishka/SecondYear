/**
 * ChargeUA — Інтерактивна фільтрація та керування виводом каталогу станцій
 */
(function () {
  'use strict';

  function initFilter() {
    const searchInput = document.getElementById('station-search-input');
    const freeOnlyBtn = document.getElementById('filter-free-only');
    const cityChips = document.querySelectorAll('.city-chip');
    const grid = document.getElementById('stations-grid');
    const cards = grid ? Array.from(grid.querySelectorAll('.card')) : [];
    const countBadge = document.getElementById('stations-shown-count');
    const emptyState = document.getElementById('stations-empty');
    const resetBtn = document.getElementById('reset-filters-btn');
    const loadMoreWrap = document.getElementById('stations-load-more-wrap');
    const loadMoreBtn = document.getElementById('stations-load-more');
    const remainingCountSpan = document.getElementById('remaining-count');

    if (!grid || cards.length === 0) return;

    const INITIAL_LIMIT = 3;
    let isExpanded = false;
    let activeCity = 'all';
    let onlyFree = false;
    let searchQuery = '';

    function filterStations() {
      const isFiltered = (activeCity !== 'all' || onlyFree || searchQuery.length > 0);
      let matchingCards = [];

      cards.forEach(function (card) {
        const cardCity = card.getAttribute('data-city') || '';
        const hasFree = card.getAttribute('data-has-free') === 'true';
        const cardText = card.textContent.toLowerCase();

        const matchesCity = (activeCity === 'all' || cardCity.toLowerCase() === activeCity.toLowerCase());
        const matchesFree = (!onlyFree || hasFree);
        const matchesSearch = (!searchQuery || cardText.includes(searchQuery));

        if (matchesCity && matchesFree && matchesSearch) {
          matchingCards.push(card);
        } else {
          card.style.display = 'none';
        }
      });

      const totalMatching = matchingCards.length;

      // Якщо фільтр не застосовано і не натиснуто "Показати ще", лімітуємо до INITIAL_LIMIT
      const shouldLimit = (!isFiltered && !isExpanded && totalMatching > INITIAL_LIMIT);

      matchingCards.forEach(function (card, index) {
        if (shouldLimit && index >= INITIAL_LIMIT) {
          card.style.display = 'none';
        } else {
          card.style.display = '';
        }
      });

      const currentlyVisible = shouldLimit ? INITIAL_LIMIT : totalMatching;

      if (countBadge) {
        countBadge.textContent = currentlyVisible;
      }

      // Керування кнопкою "Показати ще"
      if (loadMoreWrap) {
        if (shouldLimit) {
          loadMoreWrap.style.display = 'block';
          if (remainingCountSpan) {
            remainingCountSpan.textContent = totalMatching - INITIAL_LIMIT;
          }
        } else {
          loadMoreWrap.style.display = 'none';
        }
      }

      // Відображення порожнього стану
      if (emptyState) {
        if (totalMatching === 0) {
          emptyState.classList.remove('hidden');
          grid.classList.add('hidden');
        } else {
          emptyState.classList.add('hidden');
          grid.classList.remove('hidden');
        }
      }
    }

    // Слухач "Показати ще"
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', function () {
        isExpanded = true;
        filterStations();
      });
    }

    // Слухач пошуку
    if (searchInput) {
      searchInput.addEventListener('input', function (e) {
        searchQuery = e.target.value.trim().toLowerCase();
        filterStations();
      });
    }

    // Слухач фільтра "Тільки вільні"
    if (freeOnlyBtn) {
      freeOnlyBtn.addEventListener('click', function () {
        onlyFree = !onlyFree;
        if (onlyFree) {
          freeOnlyBtn.classList.add('active');
        } else {
          freeOnlyBtn.classList.remove('active');
        }
        filterStations();
      });
    }

    // Слухач чіпсів міст
    cityChips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        cityChips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        activeCity = this.getAttribute('data-city') || 'all';
        filterStations();
      });
    });

    // Скидання фільтрів
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        activeCity = 'all';
        onlyFree = false;
        searchQuery = '';
        isExpanded = false;
        if (searchInput) searchInput.value = '';
        if (freeOnlyBtn) freeOnlyBtn.classList.remove('active');
        cityChips.forEach(function (c) {
          if (c.getAttribute('data-city') === 'all') {
            c.classList.add('active');
          } else {
            c.classList.remove('active');
          }
        });
        filterStations();
      });
    }

    // Початковий виклик
    filterStations();
  }

  let isFilterInitialized = false;
  function ensureFilterInit() {
    if (isFilterInitialized) return;
    isFilterInitialized = true;
    initFilter();
  }

  function setupLazyFilter() {
    const stationsSec = document.getElementById('stations');
    if ('IntersectionObserver' in window && stationsSec) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting || entry.intersectionRatio > 0) {
            ensureFilterInit();
            observer.disconnect();
          }
        });
      }, { rootMargin: '0px' });
      observer.observe(stationsSec);
      stationsSec.addEventListener('pointerdown', ensureFilterInit, { once: true, passive: true });
      stationsSec.addEventListener('focusin', ensureFilterInit, { once: true, passive: true });
    } else {
      // lazy init on scroll/interaction only
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupLazyFilter);
  } else {
    setupLazyFilter();
  }
})();
