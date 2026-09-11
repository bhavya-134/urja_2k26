/* ============================================================
   events.js — Events Carousel, Filter, Bottom-Sheet Modal
   ============================================================ */

(function() {
  'use strict';

  // ====== HEMISPHERE FILTER ======
  const hemiBtns = document.querySelectorAll('.hemi-btn');
  const eventCards = document.querySelectorAll('.event-card');

  function setFilter(filter) {
    hemiBtns.forEach(b => {
      const isActive = b.dataset.filter === filter;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-pressed', isActive);
    });
    eventCards.forEach(card => {
      const cat = card.dataset.category;
      const hidden = filter !== 'all' && cat !== filter;
      card.classList.toggle('hidden-filter', hidden);
    });
  }

  hemiBtns.forEach(btn => {
    btn.addEventListener('click', () => setFilter(btn.dataset.filter));
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); setFilter(btn.dataset.filter); }
    });
  });

  // ====== MODAL ======
  const backdrop    = document.getElementById('modal-backdrop');
  const modal       = document.getElementById('event-modal');
  const modalIcon   = document.getElementById('modal-icon-wrap');
  const modalName   = document.getElementById('modal-event-name');
  const modalPoster = document.getElementById('modal-poster-img');
  const modalDesc   = document.getElementById('modal-desc');
  const modalFee    = document.getElementById('modal-fee');
  const modalTeam   = document.getElementById('modal-team');
  const modalCoord  = document.getElementById('modal-coordinator');
  const modalReg    = document.getElementById('modal-register-btn');
  const circuitFlash= document.getElementById('circuit-flash');

  let currentFormUrl = '#';

  function openModal(card) {
    const cat  = card.dataset.category || 'technical';
    const name = card.dataset.name || '';
    const fee  = card.dataset.fee || 'FREE';
    const team = card.dataset.team || 'Solo';
    const desc = card.dataset.desc || '';
    const coord= card.dataset.coordinator || '';
    const form = card.dataset.form || '#';
    const poster= card.dataset.poster || 'https://picsum.photos/seed/event/400/600';

    modalIcon.className = 'modal-icon-wrap ' + cat;
    const isTech = cat === 'technical';

    // icon SVG
    modalIcon.innerHTML = isTech
      ? '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M4.93 4.93a10 10 0 0 0 0 14.14M8.46 8.46a5 5 0 0 0 0 7.07"/></svg>'
      : '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>';

    modalName.textContent = name;
    modalPoster.src = poster;
    modalPoster.alt = name + ' event poster';
    modalDesc.textContent = desc;

    const isFree = fee === 'FREE';
    modalFee.textContent = isFree ? 'FREE' : '₹' + fee;
    modalFee.className = 'event-chip chip-fee ' + (isFree ? 'free' : 'paid');

    modalTeam.textContent = team;
    modalCoord.textContent = coord;
    currentFormUrl = form;

    backdrop.classList.add('visible');
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    modal.focus();
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    backdrop.classList.remove('visible');
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Open on card click
  eventCards.forEach(card => {
    function handleOpen(e) {
      // Spark ripple
      createRipple(e, card);
      openModal(card);
    }
    card.addEventListener('click', handleOpen);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card); }
    });

    // VIEW EVENT button
    const viewBtn = card.querySelector('.event-view-btn');
    if (viewBtn) {
      viewBtn.addEventListener('click', (e) => { e.stopPropagation(); openModal(card); });
    }
  });

  // Close on backdrop
  backdrop.addEventListener('click', closeModal);

  // Register button
  if (modalReg) {
    modalReg.addEventListener('click', () => {
      // Circuit flash
      if (circuitFlash) {
        circuitFlash.classList.add('flash');
        setTimeout(() => circuitFlash.classList.remove('flash'), 200);
      }
      setTimeout(() => {
        if (currentFormUrl && currentFormUrl !== '#') {
          window.open(currentFormUrl, '_blank', 'noopener,noreferrer');
        }
      }, 150);
    });
  }

  // Poster → lightbox
  if (modalPoster) {
    modalPoster.addEventListener('click', () => {
      openLightbox(modalPoster.src, modalName.textContent);
    });
  }

  // ====== SWIPE DOWN TO DISMISS ======
  let touchStartY = 0;
  let isDragging = false;

  modal.addEventListener('touchstart', (e) => {
    touchStartY = e.touches[0].clientY;
    isDragging = true;
  }, { passive: true });

  modal.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    const dy = e.touches[0].clientY - touchStartY;
    if (dy > 0) {
      modal.style.transform = `translateY(${dy}px)`;
    }
  }, { passive: true });

  modal.addEventListener('touchend', (e) => {
    if (!isDragging) return;
    const dy = e.changedTouches[0].clientY - touchStartY;
    modal.style.transform = '';
    modal.style.transition = 'transform 400ms cubic-bezier(.32,.72,0,1)';
    if (dy > 100) {
      closeModal();
    }
    isDragging = false;
  }, { passive: true });

  // ====== RIPPLE EFFECT ======
  function createRipple(e, container) {
    const rect = container.getBoundingClientRect();
    const x = (e.clientX || e.touches?.[0]?.clientX || rect.left + rect.width / 2) - rect.left;
    const y = (e.clientY || e.touches?.[0]?.clientY || rect.top + rect.height / 2) - rect.top;
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    container.appendChild(ripple);
    setTimeout(() => ripple.remove(), 700);
  }

  // Hero CTA ripple
  const heroCta = document.getElementById('hero-cta-btn');
  if (heroCta) {
    heroCta.addEventListener('click', (e) => {
      createRipple(e, heroCta);
      setTimeout(() => {
        const evSection = document.getElementById('events');
        if (evSection) evSection.scrollIntoView({ behavior: 'smooth' });
      }, 200);
    });
  }

  // ====== LIGHTBOX ======
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxClose = document.getElementById('lightbox-close');
  let lightboxImages = [];
  let lightboxIndex = 0;

  function openLightbox(src, caption) {
    lightboxImg.src = src;
    lightboxImg.alt = caption || '';
    lightboxCaption.textContent = caption || '';
    lightbox.classList.add('open');
    lightbox.setAttribute('aria-hidden', 'false');
    lightboxClose.focus();
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
  }

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target === lightboxImg) closeLightbox();
    });
  }

  // Expose globally for gallery.js
  window.openLightbox = openLightbox;

  // Keyboard dismiss
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeLightbox();
      closeModal();
    }
  });

})();
