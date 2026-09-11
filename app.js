/* ============================================================
   URJA 2K26 — app.js
   Full interactivity: Neural canvas, loader, tabs, modal,
   schedule accordion, gallery lightbox, countdown, PWA
   ============================================================ */
(function () {
  'use strict';

  // ============================================================
  //  NEURAL NETWORK CANVAS — interactive background
  //  Nodes connected by lines; closest node to cursor glows;
  //  clicking sends a pulse along connected edges.
  // ============================================================
  const neuralCanvas = document.getElementById('neural-canvas');
  const nCtx = neuralCanvas ? neuralCanvas.getContext('2d') : null;
  let nW = 0, nH = 0, nNodes = [], nMouse = { x: -999, y: -999 };
  const NODE_COUNT = 60, LINK_DIST = 130;

  function resizeNeural() {
    nW = neuralCanvas.width = window.innerWidth;
    nH = neuralCanvas.height = window.innerHeight;
  }

  function createNodes() {
    nNodes = [];
    for (let i = 0; i < NODE_COUNT; i++) {
      nNodes.push({
        x: Math.random() * nW, y: Math.random() * nH,
        vx: (Math.random() - .5) * .4, vy: (Math.random() - .5) * .4,
        r: Math.random() * 2 + 1.5,
        pulse: 0,
        type: Math.random() > .5 ? 'amber' : 'blue'
      });
    }
  }

  function drawNeural() {
    if (!nCtx || document.hidden) { requestAnimationFrame(drawNeural); return; }
    requestAnimationFrame(drawNeural);
    nCtx.clearRect(0, 0, nW, nH);

    // Move nodes
    nNodes.forEach(n => {
      n.x += n.vx; n.y += n.vy;
      if (n.x < 0 || n.x > nW) n.vx *= -1;
      if (n.y < 0 || n.y > nH) n.vy *= -1;
      if (n.pulse > 0) n.pulse -= .02;
    });

    // Mouse proximity — boost nearest node
    let nearest = null, nd2 = Infinity;
    nNodes.forEach(n => {
      const d2 = (n.x - nMouse.x) ** 2 + (n.y - nMouse.y) ** 2;
      if (d2 < nd2) { nd2 = d2; nearest = n; }
    });
    if (nearest && nd2 < 120 ** 2) nearest.pulse = Math.min(nearest.pulse + .06, 1);

    // Draw edges
    for (let i = 0; i < nNodes.length; i++) {
      for (let j = i + 1; j < nNodes.length; j++) {
        const a = nNodes[i], b = nNodes[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist > LINK_DIST) continue;
        const alpha = (1 - dist / LINK_DIST) * .12 + Math.max(a.pulse, b.pulse) * .25;
        const col = a.type === b.type
          ? (a.type === 'amber' ? `rgba(255,138,0,${alpha})` : `rgba(58,160,255,${alpha})`)
          : `rgba(242,179,61,${alpha * 1.5})`;
        nCtx.beginPath();
        nCtx.moveTo(a.x, a.y);
        nCtx.lineTo(b.x, b.y);
        nCtx.strokeStyle = col;
        nCtx.lineWidth = .8;
        nCtx.stroke();
      }
    }

    // Draw nodes
    nNodes.forEach(n => {
      const col = n.type === 'amber' ? [255, 138, 0] : [58, 160, 255];
      const a = .15 + n.pulse * .7;
      nCtx.beginPath();
      nCtx.arc(n.x, n.y, n.r + n.pulse * 3, 0, Math.PI * 2);
      nCtx.fillStyle = `rgba(${col[0]},${col[1]},${col[2]},${a})`;
      nCtx.fill();
      if (n.pulse > .1) {
        const g = nCtx.createRadialGradient(n.x, n.y, 0, n.x, n.y, (n.r + n.pulse * 4) * 3);
        g.addColorStop(0, `rgba(${col[0]},${col[1]},${col[2]},${n.pulse * .5})`);
        g.addColorStop(1, 'rgba(0,0,0,0)');
        nCtx.beginPath();
        nCtx.arc(n.x, n.y, (n.r + n.pulse * 4) * 3, 0, Math.PI * 2);
        nCtx.fillStyle = g;
        nCtx.fill();
      }
    });
  }

  // Click pulse
  window.addEventListener('click', e => {
    // Send pulse from clicked position
    nNodes.forEach(n => {
      const d = Math.sqrt((n.x - e.clientX) ** 2 + (n.y - e.clientY) ** 2);
      if (d < 150) n.pulse = Math.min(n.pulse + (1 - d / 150), 1);
    });
  });

  window.addEventListener('mousemove', e => { nMouse.x = e.clientX; nMouse.y = e.clientY; }, { passive: true });
  window.addEventListener('touchmove', e => { nMouse.x = e.touches[0].clientX; nMouse.y = e.touches[0].clientY; }, { passive: true });

  if (nCtx) {
    resizeNeural();
    createNodes();
    window.addEventListener('resize', () => { resizeNeural(); createNodes(); }, { passive: true });
    drawNeural();
  }

  // ============================================================
  //  TOUCH TRAIL
  // ============================================================
  const trailCanvas = document.getElementById('trail-canvas');
  const tCtx = trailCanvas ? trailCanvas.getContext('2d') : null;
  let particles = [];

  if (tCtx) {
    trailCanvas.width = window.innerWidth;
    trailCanvas.height = window.innerHeight;
    window.addEventListener('resize', () => {
      trailCanvas.width = window.innerWidth;
      trailCanvas.height = window.innerHeight;
    }, { passive: true });

    function addParticle(x, y) {
      particles.push({ x, y, life: 1, r: Math.random() * 3 + 2 });
      if (particles.length > 60) particles.shift();
    }

    window.addEventListener('touchmove', e => {
      for (let t of e.touches) addParticle(t.clientX, t.clientY);
    }, { passive: true });
    window.addEventListener('mousemove', e => {
      if (Math.random() > .6) addParticle(e.clientX, e.clientY);
    }, { passive: true });

    function trailLoop() {
      requestAnimationFrame(trailLoop);
      tCtx.clearRect(0, 0, trailCanvas.width, trailCanvas.height);
      particles = particles.filter(p => p.life > .02);
      particles.forEach(p => {
        p.life *= .9;
        const a = p.life * .5;
        const g = tCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 3);
        g.addColorStop(0, `rgba(242,179,61,${a})`);
        g.addColorStop(1, 'rgba(0,0,0,0)');
        tCtx.beginPath();
        tCtx.arc(p.x, p.y, p.r * 3, 0, Math.PI * 2);
        tCtx.fillStyle = g;
        tCtx.fill();
      });
    }
    trailLoop();
  }

  // ============================================================
  //  LOADER ANIMATION
  // ============================================================
  const loader = document.getElementById('loader');
  const loaderCanvas = document.getElementById('loader-canvas');
  const lCtx = loaderCanvas ? loaderCanvas.getContext('2d') : null;
  let loaderPhase = 0;

  if (lCtx) {
    loaderCanvas.width = window.innerWidth;
    loaderCanvas.height = window.innerHeight;

    function loaderParticleLoop() {
      if (!loader.classList.contains('done')) requestAnimationFrame(loaderParticleLoop);
      else return;
      lCtx.clearRect(0, 0, loaderCanvas.width, loaderCanvas.height);
      loaderPhase += .02;
      // Draw faint circuit grid
      lCtx.strokeStyle = 'rgba(242,179,61,.04)';
      lCtx.lineWidth = 1;
      for (let x = 0; x < loaderCanvas.width; x += 40) {
        lCtx.beginPath(); lCtx.moveTo(x, 0); lCtx.lineTo(x, loaderCanvas.height); lCtx.stroke();
      }
      for (let y = 0; y < loaderCanvas.height; y += 40) {
        lCtx.beginPath(); lCtx.moveTo(0, y); lCtx.lineTo(loaderCanvas.width, y); lCtx.stroke();
      }
      // Traveling pulse
      const px = (Math.sin(loaderPhase) * .5 + .5) * loaderCanvas.width;
      const py = loaderCanvas.height / 2 + Math.cos(loaderPhase * 1.3) * 60;
      const g = lCtx.createRadialGradient(px, py, 0, px, py, 60);
      g.addColorStop(0, 'rgba(255,138,0,.3)'); g.addColorStop(1, 'rgba(0,0,0,0)');
      lCtx.beginPath(); lCtx.arc(px, py, 60, 0, Math.PI * 2); lCtx.fillStyle = g; lCtx.fill();
    }
    loaderParticleLoop();
  }

  // SVG loader animation sequence
  if (!sessionStorage.getItem('urja-seen')) {
    document.body.style.overflow = 'hidden';
    const ring = document.getElementById('lc-ring');
    const bolt = document.getElementById('lc-bolt');
    const nl = document.getElementById('lc-neuron-l');
    const nr = document.getElementById('lc-neuron-r');
    const nl2 = document.getElementById('lc-node-l');
    const nr2 = document.getElementById('lc-node-r');
    const spark = document.getElementById('lc-spark');
    const letters = document.querySelectorAll('#loader-urja span');
    const year = document.getElementById('loader-year');
    const tag = document.getElementById('loader-tag');
    const bar = document.getElementById('loader-bar');

    let progress = 0;
    const barInterval = setInterval(() => {
      progress += 2;
      if (bar) bar.style.width = Math.min(progress, 100) + '%';
      if (progress >= 100) clearInterval(barInterval);
    }, 60);

    function ease(el, prop, val, delay) {
      setTimeout(() => { if (el) { el.style.transition = prop + ' .4s ease'; el[prop.split(':')[0]] = val; } }, delay);
    }

    // Ring draws in
    setTimeout(() => { if (ring) { ring.style.transition = 'stroke-dashoffset .7s ease'; ring.style.strokeDashoffset = '0'; } }, 200);
    // Neurons
    setTimeout(() => {
      [nl, nr].forEach(el => { if (el) { el.style.transition = 'stroke-dashoffset .5s ease'; el.style.strokeDashoffset = '0'; } });
    }, 700);
    // Nodes
    setTimeout(() => {
      [nl2, nr2].forEach(el => { if (el) { el.style.transition = 'opacity .3s ease'; el.style.opacity = '1'; } });
    }, 1100);
    // Bolt
    setTimeout(() => {
      if (bolt) { bolt.style.transition = 'opacity .3s ease, filter .3s ease'; bolt.style.opacity = '1'; bolt.style.filter = 'drop-shadow(0 0 8px #FF8A00)'; }
    }, 1300);
    // Spark
    setTimeout(() => {
      if (spark) { spark.style.transition = 'opacity .1s'; spark.style.opacity = '1'; }
      setTimeout(() => { if (spark) spark.style.opacity = '.3'; }, 150);
    }, 1500);
    // Letters
    setTimeout(() => {
      letters.forEach((l, i) => setTimeout(() => {
        l.style.animation = 'letterFlicker .4s ease forwards';
      }, i * 80));
    }, 1600);
    // Year
    setTimeout(() => { if (year) { year.style.transition = 'opacity .4s'; year.style.opacity = '1'; } }, 2100);
    // Tag
    setTimeout(() => { if (tag) { tag.style.transition = 'opacity .4s'; tag.style.opacity = '1'; } }, 2400);
    // Complete
    setTimeout(() => {
      sessionStorage.setItem('urja-seen', '1');
      document.body.style.overflow = '';
      if (loader) loader.classList.add('done');
      setTimeout(() => { if (loader) loader.style.display = 'none'; }, 700);
    }, 3200);
  } else {
    if (loader) loader.style.display = 'none';
  }

  // Letter flicker keyframe
  const kfStyle = document.createElement('style');
  kfStyle.textContent = '@keyframes letterFlicker{0%{opacity:0}30%{opacity:1}45%{opacity:.4}60%{opacity:1}80%{opacity:.7}100%{opacity:1}}';
  document.head.appendChild(kfStyle);

  // ============================================================
  //  TAB SYSTEM
  // ============================================================
  const TABS = ['home', 'events', 'schedule', 'gallery', 'teams', 'sponsors'];
  const SIGNAL = {
    home: 'SIGNAL INITIATED', events: 'SIGNAL ROUTED',
    schedule: 'SIGNAL SYNCHRONIZED', gallery: 'SIGNAL ARCHIVED',
    teams: 'NETWORK CONNECTED', sponsors: 'POWER SUPPLIED'
  };
  let currentTab = 'home';
  const signalEl = document.getElementById('signal-state');

  function switchTab(tabId) {
    if (tabId === currentTab) return;
    currentTab = tabId;
    if (navigator.vibrate) navigator.vibrate(10);

    // Hide all
    TABS.forEach(id => {
      const el = document.getElementById('tab-' + id);
      if (el) el.hidden = true;
    });

    // Show active
    const panel = document.getElementById('tab-' + tabId);
    if (panel) {
      panel.hidden = false;
      panel.classList.remove('animate');
      void panel.offsetWidth;
      panel.classList.add('animate');
    }

    // Update dock
    document.querySelectorAll('.dock-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabId);
    });

    // Signal state
    if (signalEl) signalEl.textContent = SIGNAL[tabId] || '';

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'instant' });

    // Trigger per-tab animations
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        triggerReveal();
        if (tabId === 'home') { runCountUp(); updateCountdown(); }
        if (tabId === 'teams') triggerMcards();
        if (tabId === 'schedule') triggerTimelineNodes();
      });
    });
  }
  window.URJA = { switchTab };

  // Dock clicks
  document.querySelectorAll('.dock-btn').forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
  });

  // ============================================================
  //  REVEAL
  // ============================================================
  function triggerReveal() {
    document.querySelectorAll('[data-reveal]').forEach((el, i) => {
      el.classList.remove('visible');
      setTimeout(() => el.classList.add('visible'), i * 80);
    });
  }

  // ============================================================
  //  COUNT-UP
  // ============================================================
  function runCountUp() {
    document.querySelectorAll('[data-count]').forEach(el => {
      const target = parseInt(el.dataset.count, 10);
      let n = 0; const step = target / 60;
      el.textContent = '0';
      const id = setInterval(() => {
        n = Math.min(n + step, target);
        el.textContent = Math.floor(n);
        if (n >= target) { el.textContent = target; clearInterval(id); }
      }, 16);
    });
  }

  // ============================================================
  //  COUNTDOWN
  // ============================================================
  const FEST = new Date('2026-11-01T09:00:00');
  const bulbFill = document.getElementById('bulb-fill');

  function updateCountdown() {
    const now = new Date(), diff = FEST - now;
    const days = document.getElementById('cd-days');
    const hours = document.getElementById('cd-hours');
    const mins = document.getElementById('cd-mins');
    const secs = document.getElementById('cd-secs');
    if (diff <= 0) {
      if (days) days.textContent = '00';
      if (hours) hours.textContent = '00';
      if (mins) mins.textContent = '00';
      if (secs) secs.textContent = '00';
      if (bulbFill) bulbFill.setAttribute('transform', 'translate(0,0) scale(1,1)');
      return;
    }
    const d = Math.floor(diff / 86400000);
    const h = Math.floor((diff % 86400000) / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    const pad = v => String(v).padStart(2, '0');
    if (days) days.textContent = pad(d);
    if (hours) hours.textContent = pad(h);
    if (mins) mins.textContent = pad(m);
    if (secs) secs.textContent = pad(s);
    // Animate bulb fill
    const pct = Math.min(Math.max(1 - diff / (365 * 86400000), 0), 1);
    const ty = 65 - 65 * pct;
    if (bulbFill) bulbFill.setAttribute('transform', `translate(0,${ty.toFixed(1)}) scale(1,${pct.toFixed(3)})`);
  }
  setInterval(updateCountdown, 1000);

  // ============================================================
  //  EVENTS — hemisphere filter + modal
  // ============================================================
  const hemiBtns = document.querySelectorAll('.hemi-btn');
  hemiBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const f = btn.dataset.filter;
      hemiBtns.forEach(b => b.classList.toggle('active', b.dataset.filter === f));
      document.querySelectorAll('.ecard').forEach(c => {
        c.classList.toggle('hidden', f !== 'all' && c.dataset.cat !== f);
      });
    });
  });

  // Event card modal
  const backdrop = document.getElementById('modal-backdrop');
  const modal = document.getElementById('event-modal');
  const modalBody = document.getElementById('modal-body');
  const circuitFlash = document.getElementById('circuit-flash');

  function openModal(card) {
    const cat = card.dataset.cat || 'technical';
    const name = card.dataset.name || '';
    const fee = card.dataset.fee || 'FREE';
    const team = card.dataset.team || 'Solo';
    const desc = card.dataset.desc || '';
    const coord = card.dataset.coord || '';
    const poster = card.dataset.poster || 'https://picsum.photos/400/600';
    const isFree = fee === 'FREE';

    const iconSvg = cat === 'technical'
      ? '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07M4.93 4.93a10 10 0 000 14.14M8.46 8.46a5 5 0 000 7.07"/></svg>'
      : '<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>';

    modalBody.innerHTML = `
      <div class="modal-icon ${cat}">${iconSvg}</div>
      <div class="modal-title">${name}</div>
      <div class="modal-poster"><img src="${poster}" alt="${name}" loading="lazy"></div>
      <div class="modal-desc">${desc}</div>
      <div class="modal-meta">
        <span class="modal-meta-lbl">ENTRY FEE</span>
        <span class="badge ${isFree ? 'free' : 'paid'}">${isFree ? 'FREE' : '&#8377;' + fee}</span>
      </div>
      <div class="modal-meta">
        <span class="modal-meta-lbl">TEAM SIZE</span>
        <span class="badge neutral">${team}</span>
      </div>
      <div class="modal-meta">
        <span class="modal-meta-lbl">COORDINATOR</span>
        <div class="modal-coord">${coord}</div>
      </div>
      <button class="modal-reg" onclick="window.URJA.regClick()">REGISTER NOW &rarr;</button>
    `;
    window.URJA.regClick = () => {
      if (circuitFlash) { circuitFlash.classList.add('flash'); setTimeout(() => circuitFlash.classList.remove('flash'), 180); }
      setTimeout(() => window.open('https://forms.gle/placeholder', '_blank', 'noopener'), 150);
    };

    backdrop.classList.add('show');
    modal.setAttribute('aria-hidden', 'false');
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    backdrop.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
    setTimeout(() => { modal.hidden = true; }, 400);
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.ecard, .ecard-btn').forEach(el => {
    el.addEventListener('click', e => {
      const card = el.closest('.ecard') || el;
      if (card.classList.contains('hidden')) return;
      e.stopPropagation();
      openModal(card);
    });
  });
  backdrop.addEventListener('click', closeModal);

  // Swipe down to close modal
  let mTouchY = 0;
  modal.addEventListener('touchstart', e => { mTouchY = e.touches[0].clientY; }, { passive: true });
  modal.addEventListener('touchmove', e => {
    const dy = e.touches[0].clientY - mTouchY;
    if (dy > 0) modal.style.transform = `translateY(${dy}px)`;
  }, { passive: true });
  modal.addEventListener('touchend', e => {
    const dy = e.changedTouches[0].clientY - mTouchY;
    modal.style.transform = '';
    if (dy > 100) closeModal();
  }, { passive: true });

  // ============================================================
  //  SCHEDULE — day toggle + filter + accordion
  // ============================================================
  document.querySelectorAll('.day-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const day = btn.dataset.day;
      document.querySelectorAll('.day-tab').forEach(b => b.classList.toggle('active', b.dataset.day === day));
      ['d1', 'd2'].forEach(id => {
        const el = document.getElementById('timeline-' + id);
        if (el) el.hidden = id !== 'd' + day;
      });
      triggerTimelineNodes();
    });
  });

  document.querySelectorAll('.sf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const f = btn.dataset.sf;
      document.querySelectorAll('.sf-btn').forEach(b => b.classList.toggle('active', b.dataset.sf === f));
      document.querySelectorAll('.tl-node').forEach(n => {
        const cat = n.dataset.scat || 'default';
        n.classList.toggle('filtered', f !== 'all' && cat !== f && cat !== 'default' && cat !== 'break');
      });
    });
  });

  // Timeline accordion
  document.addEventListener('click', e => {
    const node = e.target.closest('.tl-node');
    if (!node) return;
    const wasOpen = node.classList.contains('open');
    document.querySelectorAll('.tl-node.open').forEach(n => n.classList.remove('open'));
    if (!wasOpen) node.classList.add('open');
  });

  function triggerTimelineNodes() {
    const active = document.querySelector('.timeline:not([hidden])');
    if (!active) return;
    active.querySelectorAll('.tl-node').forEach((n, i) => {
      n.classList.remove('in');
      setTimeout(() => n.classList.add('in'), i * 70);
    });
  }

  // ============================================================
  //  GALLERY — filter + lightbox
  // ============================================================
  document.querySelectorAll('.gchip').forEach(chip => {
    chip.addEventListener('click', () => {
      const f = chip.dataset.gf;
      document.querySelectorAll('.gchip').forEach(c => c.classList.toggle('active', c.dataset.gf === f));
      document.querySelectorAll('.gitem').forEach(item => {
        item.classList.toggle('hidden', f !== 'all' && item.dataset.ge !== f);
      });
    });
  });

  // Lightbox
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lb-img');
  const lbCap = document.getElementById('lb-caption');
  const lbClose = document.getElementById('lb-close');
  let lbImages = [], lbIdx = 0;

  document.querySelectorAll('.gitem').forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const cap = item.querySelector('.gitem-label');
      if (!img) return;
      lbImages = Array.from(document.querySelectorAll('.gitem:not(.hidden) img'));
      lbIdx = lbImages.indexOf(img);
      showLb(lbIdx);
    });
  });

  function showLb(idx) {
    const img = lbImages[idx];
    if (!img) return;
    lbImg.src = img.src; lbImg.alt = img.alt;
    const label = img.closest('.gitem')?.querySelector('.gitem-label');
    if (lbCap) lbCap.textContent = label ? label.textContent : '';
    lb.setAttribute('aria-hidden', 'false');
  }

  if (lbClose) lbClose.addEventListener('click', () => lb.setAttribute('aria-hidden', 'true'));
  if (lb) {
    lb.addEventListener('click', e => { if (e.target === lb) lb.setAttribute('aria-hidden', 'true'); });
    let lbTx = 0;
    lb.addEventListener('touchstart', e => { lbTx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - lbTx;
      if (Math.abs(dx) > 50) { lbIdx = (lbIdx + (dx < 0 ? 1 : -1) + lbImages.length) % lbImages.length; showLb(lbIdx); }
    }, { passive: true });
  }

  // ============================================================
  //  TEAMS — filter + stagger reveal
  // ============================================================
  document.querySelectorAll('.tf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const f = btn.dataset.tf;
      document.querySelectorAll('.tf-btn').forEach(b => b.classList.toggle('active', b.dataset.tf === f));
      document.querySelectorAll('.mcard').forEach(c => {
        c.classList.toggle('hidden', f !== 'all' && c.dataset.tc !== f);
      });
      triggerMcards();
    });
  });

  function triggerMcards() {
    document.querySelectorAll('.mcard:not(.hidden)').forEach((c, i) => {
      c.classList.remove('in');
      setTimeout(() => c.classList.add('in'), i * 70);
    });
  }

  // ============================================================
  //  PWA
  // ============================================================
  let dp = null;
  window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault(); dp = e;
    setTimeout(() => {
      const b = document.createElement('div');
      b.style.cssText = 'position:fixed;bottom:calc(var(--dock-h)+10px);left:12px;right:60px;background:var(--surface2);border:1px solid var(--b-gold);border-radius:12px;padding:12px 16px;z-index:800;display:flex;align-items:center;gap:10px;';
      b.innerHTML = '<div style="flex:1"><div style="font-family:var(--font-head);font-size:12px;color:var(--gold)">Install URJA</div><div style="font-family:var(--font-mono);font-size:9px;color:var(--dim)">Add to Home Screen</div></div><button id="pwa-ok" style="background:var(--gold);color:#000;border:none;border-radius:16px;padding:7px 14px;font-family:var(--font-mono);font-size:10px;cursor:pointer">INSTALL</button><button id="pwa-x" style="background:none;border:none;color:var(--dim);font-size:18px;cursor:pointer">&times;</button>';
      document.body.appendChild(b);
      document.getElementById('pwa-ok').addEventListener('click', () => { dp.prompt(); b.remove(); });
      document.getElementById('pwa-x').addEventListener('click', () => b.remove());
    }, 30000);
  });

  // ============================================================
  //  KEYBOARD
  // ============================================================
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeModal();
      if (lb) lb.setAttribute('aria-hidden', 'true');
    }
  });

  // ============================================================
  //  BOOT
  // ============================================================
  // init home tab visually
  triggerReveal();
  runCountUp();
  updateCountdown();

})();
