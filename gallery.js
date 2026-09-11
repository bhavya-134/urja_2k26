/* ============================================================
   gallery.js — Gallery Filter, Scan-line, Lightbox, Swipe
   ============================================================ */

(function() {
  'use strict';

  const galleryGrid   = document.getElementById('gallery-grid');
  const galleryChips  = document.querySelectorAll('.gallery-chip');
  const yearBtns      = document.querySelectorAll('.year-btn');
  const items         = document.querySelectorAll('.gallery-item');

  let currentGFilter  = 'all';
  let currentYearFilter = 'archive';

  // ====== SCAN LINE REVEAL on Intersection ======
  const scanObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const overlay = entry.target.querySelector('.scan-line-overlay');
        if (overlay) {
          overlay.style.animation = 'none';
          requestAnimationFrame(() => {
            overlay.style.animation = 'scan-reveal 600ms ease-out forwards';
          });
        }
        scanObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  items.forEach(item => scanObserver.observe(item));

  // ====== FILTER LOGIC ======
  function applyFilters() {
    items.forEach(item => {
      const event = item.dataset.event || 'other';
      const year  = item.dataset.year  || '2025';

      const yearMatch = currentYearFilter === 'all' ||
        (currentYearFilter === 'archive' && year !== '2026') ||
        (currentYearFilter === '2026'   && year === '2026');

      const eventMatch = currentGFilter === 'all' || event === currentGFilter;

      const visible = yearMatch && eventMatch;
      item.classList.toggle('hidden-filter', !visible);
      if (visible) item.style.display = '';
      else item.style.display = 'none';
    });
  }

  // Year filter
  yearBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      currentYearFilter = btn.dataset.yearFilter;
      yearBtns.forEach(b => {
        const isActive = b.dataset.yearFilter === currentYearFilter;
        b.classList.toggle('active', isActive);
        b.setAttribute('aria-pressed', isActive);
      });
      applyFilters();
    });
  });

  // Event filter chips
  galleryChips.forEach(chip => {
    chip.addEventListener('click', () => {
      currentGFilter = chip.dataset.gfilter;
      galleryChips.forEach(c => {
        const isActive = c.dataset.gfilter === currentGFilter;
        c.classList.toggle('active', isActive);
        c.setAttribute('aria-pressed', isActive);
      });
      applyFilters();
    });
  });

  // ====== LIGHTBOX ======
  let lightboxImages = [];
  let lightboxIndex  = 0;

  function buildLightboxImages() {
    lightboxImages = [];
    items.forEach(item => {
      if (!item.classList.contains('hidden-filter') && item.style.display !== 'none') {
        const img = item.querySelector('img');
        if (img) {
          lightboxImages.push({
            src: img.src,
            caption: item.dataset.caption || ''
          });
        }
      }
    });
  }

  items.forEach((item, idx) => {
    item.addEventListener('click', () => {
      buildLightboxImages();
      const img = item.querySelector('img');
      if (!img) return;
      lightboxIndex = lightboxImages.findIndex(i => i.src === img.src);
      if (lightboxIndex < 0) lightboxIndex = 0;
      showLightboxAt(lightboxIndex);
    });
  });

  function showLightboxAt(index) {
    if (!lightboxImages.length) return;
    const data = lightboxImages[index];
    if (window.openLightbox) {
      window.openLightbox(data.src, data.caption);
    }
  }

  // Swipe between images in lightbox
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    let lbTouchX = 0;
    lightbox.addEventListener('touchstart', (e) => {
      lbTouchX = e.touches[0].clientX;
    }, { passive: true });
    lightbox.addEventListener('touchend', (e) => {
      const dx = e.changedTouches[0].clientX - lbTouchX;
      if (Math.abs(dx) > 50) {
        if (dx < 0) {
          lightboxIndex = (lightboxIndex + 1) % lightboxImages.length;
        } else {
          lightboxIndex = (lightboxIndex - 1 + lightboxImages.length) % lightboxImages.length;
        }
        showLightboxAt(lightboxIndex);
      }
    }, { passive: true });
  }

  // Initialize
  applyFilters();

})();
