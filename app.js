/* ============================================================
   URJA 2K26 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â app.js  (no loader version)
   Neural canvas bg, tab system, event modals, schedule,
   gallery lightbox, teams, countdown, touch trail, PWA
   ============================================================ */
(function () {
  'use strict';

  // ============================================================
  //  NEURAL NETWORK CANVAS ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â interactive background
  // ============================================================
  const neuralCanvas = document.getElementById('neural-canvas');
  const nCtx = neuralCanvas ? neuralCanvas.getContext('2d') : null;
  let nW = 0, nH = 0, nNodes = [], nMouse = { x: -999, y: -999 };
  const NODE_COUNT = 35, LINK_DIST = 130;

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
        r: Math.random() * 2 + 1.5, pulse: 0,
        type: Math.random() > .5 ? 'amber' : 'blue'
      });
    }
  }
  function drawNeural() {
    if (!nCtx || document.hidden) { requestAnimationFrame(drawNeural); return; }
    requestAnimationFrame(drawNeural);
    nCtx.clearRect(0, 0, nW, nH);
    nNodes.forEach(n => {
      n.x += n.vx; n.y += n.vy;
      if (n.x < 0 || n.x > nW) n.vx *= -1;
      if (n.y < 0 || n.y > nH) n.vy *= -1;
      if (n.pulse > 0) n.pulse -= .02;
    });
    let nearest = null, nd2 = Infinity;
    nNodes.forEach(n => {
      const d2 = (n.x - nMouse.x) ** 2 + (n.y - nMouse.y) ** 2;
      if (d2 < nd2) { nd2 = d2; nearest = n; }
    });
    if (nearest && nd2 < 120 ** 2) nearest.pulse = Math.min(nearest.pulse + .06, 1);
    for (let i = 0; i < nNodes.length; i++) {
      for (let j = i + 1; j < nNodes.length; j++) {
        const a = nNodes[i], b = nNodes[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist > LINK_DIST) continue;
        const alpha = (1 - dist / LINK_DIST) * .12 + Math.max(a.pulse, b.pulse) * .25;
        const col = a.type === b.type
          ? (a.type === 'amber' ? `rgba(255,138,0,${alpha})` : `rgba(58,160,255,${alpha})`)
          : `rgba(58,160,255,${alpha * 1.5})`;
        nCtx.beginPath(); nCtx.moveTo(a.x, a.y); nCtx.lineTo(b.x, b.y);
        nCtx.strokeStyle = col; nCtx.lineWidth = .8; nCtx.stroke();
      }
    }
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
        nCtx.fillStyle = g; nCtx.fill();
      }
    });
  }
  window.addEventListener('click', e => {
    nNodes.forEach(n => {
      const d = Math.sqrt((n.x - e.clientX) ** 2 + (n.y - e.clientY) ** 2);
      if (d < 150) n.pulse = Math.min(n.pulse + (1 - d / 150), 1);
    });
  });
  window.addEventListener('mousemove', e => { nMouse.x = e.clientX; nMouse.y = e.clientY; }, { passive: true });
  window.addEventListener('touchmove', e => { nMouse.x = e.touches[0].clientX; nMouse.y = e.touches[0].clientY; }, { passive: true });
  if (nCtx) {
    resizeNeural(); createNodes();
    window.addEventListener('resize', () => { resizeNeural(); createNodes(); }, { passive: true });
    drawNeural();
  }

  // ============================================================
  //  TOUCH TRAIL
  // ============================================================
  const trailCanvas = document.getElementById('trail-canvas');
  const tCtx = trailCanvas ? trailCanvas.getContext('2d') : null;
  let trailParts = [];
  if (tCtx) {
    trailCanvas.width = window.innerWidth; trailCanvas.height = window.innerHeight;
    window.addEventListener('resize', () => { trailCanvas.width = window.innerWidth; trailCanvas.height = window.innerHeight; }, { passive: true });
    function addParticle(x, y) { trailParts.push({ x, y, life: 1, r: Math.random() * 3 + 2 }); if (trailParts.length > 60) trailParts.shift(); }
    window.addEventListener('touchmove', e => { for (let t of e.touches) addParticle(t.clientX, t.clientY); }, { passive: true });
    window.addEventListener('mousemove', e => { if (Math.random() > .6) addParticle(e.clientX, e.clientY); }, { passive: true });
    (function trailLoop() {
      requestAnimationFrame(trailLoop);
      tCtx.clearRect(0, 0, trailCanvas.width, trailCanvas.height);
      trailParts = trailParts.filter(p => p.life > .02);
      trailParts.forEach(p => {
        p.life *= .9;
        const g = tCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 3);
        g.addColorStop(0, `rgba(58,160,255,${p.life * .5})`); g.addColorStop(1, 'rgba(0,0,0,0)');
        tCtx.beginPath(); tCtx.arc(p.x, p.y, p.r * 3, 0, Math.PI * 2); tCtx.fillStyle = g; tCtx.fill();
      });
    })();
  }

  // ============================================================
  //  TAB SYSTEM
  // ============================================================
  const TABS = ['home', 'events', 'schedule', 'gallery', 'teams', 'sponsors'];
  const SIGNAL = { home: 'SIGNAL INITIATED', events: 'SIGNAL ROUTED', schedule: 'SIGNAL SYNCHRONIZED', gallery: 'SIGNAL ARCHIVED', teams: 'NETWORK CONNECTED', sponsors: 'POWER SUPPLIED' };
  const TAB_LOADER_TEXT = { home: 'INITIATING SYNAPSE', events: 'THE CONNECTIONS', schedule: 'SIGNAL FLOW', gallery: 'SIGNALS FROM THE PAST', teams: 'THE NETWORK', sponsors: 'POWERING THE SIGNAL' };
  let currentTab = 'home';
  const signalEl = document.getElementById('signal-state');
  const tabLoader = document.getElementById('tab-loader');
  const tlText = document.getElementById('tl-text');

  function switchTab(tabId) {
    if (tabId === currentTab) return;
    if (navigator.vibrate) navigator.vibrate(10);
    if (tabLoader && tlText) { tlText.textContent = TAB_LOADER_TEXT[tabId] || ''; tabLoader.classList.add('active'); }
    setTimeout(() => {
      currentTab = tabId;
      TABS.forEach(id => { const el = document.getElementById('tab-' + id); if (el) el.hidden = true; });
      const panel = document.getElementById('tab-' + tabId);
      if (panel) { panel.hidden = false; panel.classList.remove('animate'); void panel.offsetWidth; panel.classList.add('animate'); }
      document.querySelectorAll('.dock-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.tab === tabId));
      if (signalEl) signalEl.textContent = SIGNAL[tabId] || '';
      window.scrollTo({ top: 0, behavior: 'instant' });
      if (tabLoader) tabLoader.classList.remove('active');
      requestAnimationFrame(() => requestAnimationFrame(() => {
        triggerReveal();
        if (tabId === 'home') { runCountUp(); updateCountdown(); }
        if (tabId === 'teams') triggerMcards();
        if (tabId === 'schedule') triggerTimelineNodes();
      }));
    }, 900);
  }
  window.URJA = { switchTab };

  document.querySelectorAll('.dock-btn').forEach(btn => btn.addEventListener('click', () => switchTab(btn.dataset.tab)));

  // ============================================================
  //  REVEAL
  // ============================================================
  function triggerReveal() {
    const panel = document.getElementById('tab-' + currentTab);
    if (!panel) return;
    panel.querySelectorAll('[data-reveal]').forEach((el, i) => {
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
      const id = setInterval(() => { n = Math.min(n + step, target); el.textContent = Math.floor(n); if (n >= target) { el.textContent = target; clearInterval(id); } }, 16);
    });
  }

  // ============================================================
  //  COUNTDOWN
  // ============================================================
  const FEST = new Date('2026-09-18T09:00:00');
  
  function updateCountdown() {
    const diff = FEST - new Date();
    const pad = v => String(Math.max(0, Math.floor(v))).padStart(2, '0');
    const dEl = document.getElementById('cd-days'), hEl = document.getElementById('cd-hours'), mEl = document.getElementById('cd-mins'), sEl = document.getElementById('cd-secs');
    if (diff <= 0) { [dEl, hEl, mEl, sEl].forEach(e => { if (e) e.textContent = '00'; }); return; }
    if (dEl) dEl.textContent = pad(diff / 86400000);
    if (hEl) hEl.textContent = pad((diff % 86400000) / 3600000);
    if (mEl) mEl.textContent = pad((diff % 3600000) / 60000);
    if (sEl) sEl.textContent = pad((diff % 60000) / 1000);
    
    // Calculate charging fill (approx 55 days total)
    const totalMs = 55 * 86400000;
    const pct = Math.min(Math.max(1 - diff / totalMs, 0), 1);
    
    
    const bulbRing = document.getElementById('bulb-ring-active');
    if (bulbRing) {
      const dash = 283;
      bulbRing.style.strokeDashoffset = dash - (dash * pct);
    }
  }
  setInterval(updateCountdown, 1000);

    // ============================================================
  //  EVENTS - FILTER + PROGRESS + MODAL
  // ============================================================
  const brainFilter = document.getElementById('brain-filter');
  const hemis = document.querySelectorAll('.hemi');
  const brainLabels = document.querySelectorAll('.brain-labels span');
  const ecards = document.querySelectorAll('.ecard');
  const scrollProg = document.getElementById('event-scroll-progress');

  // Scroll Progress
  const evObserver = new IntersectionObserver((entries) => {
    let visibleCards = Array.from(ecards).filter(c => !c.classList.contains('dissolve'));
    entries.forEach(e => {
      if (e.isIntersecting) {
        let index = visibleCards.indexOf(e.target) + 1;
        if(index > 0) scrollProg.textContent = 'SIGNAL ROUTING: ' + index + '/' + visibleCards.length;
      }
    });
  }, { threshold: 0.5 });
  ecards.forEach(c => evObserver.observe(c));

      // Brain Filter
  function applyFilter(f) {
    // Update SVG glow
    brainFilter.setAttribute('class', 'brain-filter active-' + f);
    
    // Update labels
    brainLabels.forEach(l => {
      if(f === 'technical' && l.classList.contains('bl-right')) l.classList.add('active');
      else if(f === 'non-technical' && l.classList.contains('bl-left')) l.classList.add('active');
      else if(f === 'all' && l.classList.contains('bl-center')) l.classList.add('active');
      else l.classList.remove('active');
    });

    // Animate Cards (Dissolve & Filter)
    ecards.forEach(c => {
      const isVisible = (f === 'all' || c.dataset.cat === f);
      
      // Store current target visibility to avoid race conditions
      c.dataset.targetVis = isVisible;

      if(!isVisible && !c.classList.contains('dissolve')) {
        for(let i=0; i<15; i++) {
          let p = document.createElement('div');
          p.className = 'particle';
          p.style.background = '#F2B33D';
          p.style.left = (Math.random()*100) + '%';
          p.style.top = (Math.random()*100) + '%';
          c.appendChild(p);
          setTimeout(() => { p.style.opacity=1; p.style.transform = 'translate(-50%,-50%) scale('+(Math.random()*2)+') translate('+(Math.random()*60-30)+'px, '+(Math.random()*60-30)+'px)'; }, 10);
          setTimeout(() => { if (p.parentNode === c) p.remove(); }, 700);
        }
        c.classList.add('dissolve');
        setTimeout(() => { 
          if(c.dataset.targetVis === 'false') {
            c.style.display = 'none'; 
            updateRoutingInfo(); 
          }
        }, 400);
      } else if(isVisible && (c.classList.contains('dissolve') || c.style.display === 'none')) {
        c.style.display = '';
        setTimeout(() => {
          if(c.dataset.targetVis === 'true') {
            c.classList.remove('dissolve');
          }
        }, 50);
        updateRoutingInfo();
      }
    });
  }

    hemis.forEach(hemi => hemi.addEventListener('click', () => applyFilter(hemi.dataset.filter)));
  const spine = document.querySelector('.brain-spine');
  if (spine) spine.addEventListener('click', () => applyFilter('all'));

  brainLabels.forEach(l => {
    l.addEventListener('click', () => {
      let f = 'all';
      if(l.classList.contains('bl-left')) f = 'non-technical';
      if(l.classList.contains('bl-right')) f = 'technical';
      applyFilter(f);
    });
  });

  function updateRoutingInfo() {
    let visibleCards = Array.from(ecards).filter(c => !c.classList.contains('dissolve'));
    scrollProg.textContent = 'SIGNAL ROUTING: 1/' + visibleCards.length;
  }

  const backdrop = document.getElementById('modal-backdrop');
  const modal = document.getElementById('event-modal');
  const modalBody = document.getElementById('modal-body');
  const circuitFlash = document.getElementById('circuit-flash');

    
    const eventTimeMapping = {
      'Aavishkar': 'Day 1: 09:30 AM - 10:30 AM',
      'F1 Arena': 'Day 1: 01:30 PM - 04:00 PM | Day 2: 12:00 PM - 03:00 PM',
      'SYNC: The Tech Relay': 'Day 1: 01:30 PM - 04:00 PM | Day 2: 09:30 AM - 10:30 AM',
      'Power Up': 'Day 1 & 2: 10:00 AM - ONWARDS',
      'Abhivyakti': 'Day 1: 09:30 AM - 10:30 AM',
      'Human Ludo': 'Day 1 & 2: 11:00 AM - ONWARDS',
      'Game of Drones': 'Day 1: 12:00 PM - ONWARDS | Day 2: 01:30 PM - 03:30 PM',
      'Quiz Whitz Blitz': 'Day 1: 12:00 PM - 01:00 PM | Day 2: 09:30 AM - 10:30 AM',
      'Escape the Unknown': 'Day 1 & 2: 11:00 AM - ONWARDS',
      'Clash of Minds': 'Day 1 & 2: 10:30 AM - 12:00 PM',
      'Robo Soccer': 'Day 1: 11:00 AM - ONWARDS | Day 2: 09:30 AM - 10:30 AM & 01:30 PM - 03:30 PM'
    };

    function openModal(card) {
      const cat = card.dataset.cat || 'technical';
      const fee = card.dataset.fee || 'FREE'; const isFree = fee === 'FREE';
      const iconDiv = card.querySelector('.ecard-icon');
      const iconSvg = iconDiv ? iconDiv.innerHTML : '';
      
      // Card micro-interaction
      card.style.transform = 'scale(0.95)';
      const glow = card.querySelector('.ecard-glow');
      if(glow) glow.style.opacity = '1';

      setTimeout(() => {
        card.style.transform = '';
        if(glow) glow.style.opacity = '';
        
        modalBody.innerHTML = `
          <button class="modal-close-btn" id="modal-close-btn" aria-label="Close modal">&times;</button>
          <div class="modal-icon ${cat}" id="mi-target">${iconSvg}</div>
          <div class="modal-title" id="mt-target">${card.dataset.name || ''}</div>
          <div class="modal-poster" id="mp-target"><img src="${card.dataset.poster || ''}" alt="${card.dataset.name}" loading="lazy"></div>
          <div class="modal-desc">${card.dataset.desc || ''}</div>
          <div class="modal-meta" style="flex-direction: column; align-items: flex-start; gap: 4px;">
              <span class="modal-meta-lbl" style="margin-bottom: 2px;">TIME & SCHEDULE</span>
              <span style="color: var(--gold); font-family: var(--font-mono); font-size: 13px; font-weight: 600;">${eventTimeMapping[card.dataset.name] || 'TBA'}</span>
            </div>
            <div class="modal-meta"><span class="modal-meta-lbl">ENTRY FEE</span><span class="badge ${isFree ? 'free' : 'paid'}">${isFree ? 'FREE' : '&#8377;' + fee}</span></div>
          <div class="modal-meta"><span class="modal-meta-lbl">TEAM SIZE</span><span class="badge neutral">${card.dataset.team || 'Solo'}</span></div>
          <div class="modal-meta"><span class="modal-meta-lbl">COORDINATOR</span><div class="modal-coord">${card.dataset.coord || ''}</div></div>
          <button class="modal-reg reg-charge" id="modal-reg-btn">REGISTER NOW &rarr;</button>
            <button class="modal-close-bottom" id="modal-close-bottom-btn" style="width: auto; padding: 10px 24px; border-radius: 30px; background: transparent; border: 1px solid var(--dim); color: var(--dim); font-family: var(--font-head); font-weight: 600; font-size: 13px; cursor: pointer; margin-top: -4px;">CLOSE DETAILS</button>
        `;
        
                  const closeXBtn = document.getElementById('modal-close-btn');
          if(closeXBtn) closeXBtn.addEventListener('click', closeModal);
          const closeBottomBtn = document.getElementById('modal-close-bottom-btn');
          if(closeBottomBtn) closeBottomBtn.addEventListener('click', closeModal);

        const regBtn = document.getElementById('modal-reg-btn');
          regBtn.addEventListener('click', () => {
            regBtn.classList.add('charging');
            if (circuitFlash) { circuitFlash.classList.add('flash'); setTimeout(() => circuitFlash.classList.remove('flash'), 180); }
            setTimeout(() => {
              regBtn.classList.remove('charging');
              const url = card.dataset.link || '#';
              if(url !== '#') {
                window.open(url, '_blank', 'noopener');
              } else {
                alert('Registration link coming soon!');
              }
            }, 150);
          });

        // Parallax poster
        const poster = document.getElementById('mp-target');
        if(poster) {
          modal.addEventListener('mousemove', (e) => {
              const rect = poster.getBoundingClientRect();
              const x = e.clientX - rect.left - rect.width/2;
              const y = e.clientY - rect.top - rect.height/2;
              const tiltX = (y / rect.height) * -6; 
              const tiltY = (x / rect.width) * 6;
              poster.style.transform = `perspective(800px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02,1.02,1.02)`;
          });
          modal.addEventListener('mouseleave', () => { poster.style.transform = ''; });
        }

        backdrop.classList.add('show'); modal.setAttribute('aria-hidden', 'false'); modal.hidden = false; document.body.style.overflow = 'hidden';
      }, 200);
    }
  function closeModal() {
    backdrop.classList.remove('show'); modal.setAttribute('aria-hidden', 'true');
    setTimeout(() => { modal.hidden = true; }, 400); document.body.style.overflow = '';
  }
  document.querySelectorAll('.ecard').forEach(card => card.addEventListener('click', e => { if (!card.classList.contains('hidden')) openModal(card); }));
    // Hook up schedule cards to open modals
    document.querySelectorAll('.tl-card').forEach(tCard => {
      tCard.style.cursor = 'pointer'; // Make it look clickable
      tCard.addEventListener('click', () => {
        const tTitle = tCard.querySelector('.tl-title').innerText.toUpperCase();
        let targetName = null;
        if (tTitle.includes('AAVISHKAR')) targetName = 'Aavishkar';
        else if (tTitle.includes('F1')) targetName = 'F1 Arena';
        else if (tTitle.includes('SYNC')) targetName = 'SYNC: The Tech Relay';
        else if (tTitle.includes('POWER')) targetName = 'Power Up';
        else if (tTitle.includes('ABHIVYAKTI')) targetName = 'Abhivyakti';
        else if (tTitle.includes('LUDO')) targetName = 'Human Ludo';
        else if (tTitle.includes('DRONES')) targetName = 'Game of Drones';
        else if (tTitle.includes('QUIZ')) targetName = 'Quiz Whitz Blitz';
        else if (tTitle.includes('ESCAPE')) targetName = 'Escape the Unknown';
        else if (tTitle.includes('CLASH')) targetName = 'Clash of Minds';
        else if (tTitle.includes('SOCCER')) targetName = 'Robo Soccer';
        
        if (targetName) {
          const matchingCard = Array.from(document.querySelectorAll('.ecard')).find(c => c.dataset.name === targetName);
          if (matchingCard) openModal(matchingCard);
        }
      });
    });

  if (backdrop) backdrop.addEventListener('click', closeModal);
  let mTY = 0;
  if (modal) {
    
  }

  // ============================================================
  // ============================================================
  //  SCHEDULE - Side Axon & Grid Layout
  // ============================================================
  const tContainer = document.getElementById('timeline-container');
  const d1 = document.getElementById('timeline-d1');
  const d2 = document.getElementById('timeline-d2');
  const fdBtn1 = document.getElementById('fd-btn-1');
  const fdBtn2 = document.getElementById('fd-btn-2');

  let currentScheduleDay = 1;

  function switchDay(day) {
    if(currentScheduleDay === day) return;
    currentScheduleDay = day;
    
    if(fdBtn1) { if(day === 1) fdBtn1.classList.add('active'); else fdBtn1.classList.remove('active'); }
    if(fdBtn2) { if(day === 2) fdBtn2.classList.add('active'); else fdBtn2.classList.remove('active'); }
    
    if(tContainer) tContainer.classList.add('static-distortion');
    setTimeout(() => {
      if(d1) { if(day === 1) d1.removeAttribute('hidden'); else d1.setAttribute('hidden', ''); }
      if(d2) { if(day === 2) d2.removeAttribute('hidden'); else d2.setAttribute('hidden', ''); }
      if(tContainer) tContainer.classList.remove('static-distortion');
      triggerTimelineNodes();
    }, 200);
  }
  
  if(fdBtn1) fdBtn1.addEventListener('click', () => switchDay(1));
  if(fdBtn2) fdBtn2.addEventListener('click', () => switchDay(2));

  // Tuning Frequencies
  const tuners = document.querySelectorAll('.tuner-btn');
  let myCircuitActive = false;
  tuners.forEach(btn => btn.addEventListener('click', () => {
    const f = btn.dataset.tf;
    tuners.forEach(b => b.classList.toggle('active', b === btn));
    myCircuitActive = (f === 'my-circuit');
    
    if(tContainer) tContainer.classList.add('static-distortion');
    setTimeout(() => {
      // Filter individual cards
      document.querySelectorAll('.tl-card').forEach(n => {
        const cat = n.dataset.scat || 'default';
        const isStarred = n.classList.contains('starred');
        n.classList.remove('lost-signal', 'hide-compact');
        if (myCircuitActive) {
          if(!isStarred && cat !== 'break' && cat !== 'default') n.classList.add('hide-compact');
        } else {
          if (f !== 'all' && cat !== f && cat !== 'default' && cat !== 'break') n.classList.add('lost-signal');
        }
      });
      // Hide slots that have no visible cards
      document.querySelectorAll('.tl-slot').forEach(slot => {
        const hasVisible = Array.from(slot.querySelectorAll('.tl-card')).some(c => !c.classList.contains('hide-compact') && !c.classList.contains('lost-signal'));
        slot.style.display = hasVisible ? 'flex' : 'none';
      });

      if(tContainer) tContainer.classList.remove('static-distortion');
      triggerTimelineNodes();
    }, 200);
  }));

  // My Circuit (LocalStorage)
  let starredEvents = [];
  try { starredEvents = JSON.parse(localStorage.getItem('urja_starred') || '[]'); } catch(e) {}
  
  document.querySelectorAll('.tl-card').forEach(n => {
    const id = n.dataset.id;
    if(id && starredEvents.includes(id)) n.classList.add('starred');
  });

  document.addEventListener('click', e => {
    const starBtn = e.target.closest('.tl-star');
    if (starBtn) {
      e.stopPropagation();
      const node = starBtn.closest('.tl-card');
      const id = node.dataset.id;
      if(!id) return;
      if(starredEvents.includes(id)) {
        starredEvents = starredEvents.filter(x => x !== id);
        node.classList.remove('starred');
        if(myCircuitActive) {
          node.classList.add('hide-compact');
          const slot = node.closest('.tl-slot');
          const hasVisible = Array.from(slot.querySelectorAll('.tl-card')).some(c => !c.classList.contains('hide-compact'));
          if(!hasVisible) slot.style.display = 'none';
        }
      } else {
        starredEvents.push(id);
        node.classList.add('starred');
      }
      try { localStorage.setItem('urja_starred', JSON.stringify(starredEvents)); } catch(e) {}
    }
  });

  // Axon Scroll Observer
  let axonObserver = null;
  function triggerTimelineNodes() {
    // 1. Reveal slots sequentially
    document.querySelectorAll('.timeline:not([hidden]) .tl-slot').forEach((n, i) => {
      n.classList.remove('in');
      setTimeout(() => n.classList.add('in'), i * 80);
    });

    // 2. Restart Axon Observer
    if(axonObserver) axonObserver.disconnect();
    axonObserver = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if(e.isIntersecting) {
          e.target.classList.add('fired');
          const track = e.target.closest('.axon-track');
          if(track) {
            const glowLine = track.querySelector('.axon-glow-line');
            if(glowLine) {
              const nodeTop = e.target.offsetTop;
              glowLine.style.height = (nodeTop + 20) + 'px';
            }
          }
        } else {
          if(e.boundingClientRect.y > 0) e.target.classList.remove('fired');
        }
      });
    }, { rootMargin: '-50% 0px -40% 0px' });
    
    document.querySelectorAll('.timeline:not([hidden]) .tl-slot').forEach(n => {
      if(n.style.display !== 'none') axonObserver.observe(n);
    });
  }
    // ============================================================ ΓÇö filter + lightbox
  // ============================================================
  
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
  // ============================================================
  //  TEAMS ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â filter + stagger
  // ============================================================
  document.querySelectorAll('.tf-btn').forEach(btn => btn.addEventListener('click', () => {
    const f = btn.dataset.tf;
    document.querySelectorAll('.tf-btn').forEach(b => b.classList.toggle('active', b.dataset.tf === f));
    document.querySelectorAll('.mcard').forEach(c => c.classList.toggle('hidden', f !== 'all' && c.dataset.tc !== f));
    triggerMcards();
  }));
  function triggerMcards() {
    const panel = document.getElementById('tab-teams'); if (!panel) return;
    const base = panel.querySelectorAll('[data-reveal]').length * 80;
    panel.querySelectorAll('.mcard:not(.hidden)').forEach((c, i) => { c.classList.remove('in'); setTimeout(() => c.classList.add('in'), base + i * 70); });
  }

  // ============================================================
  //  KEYBOARD
  // ============================================================
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { closeModal(); if (lb) lb.setAttribute('aria-hidden', 'true'); }
  });

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
  //  LOADER & BOOT
  // ============================================================
  if (!sessionStorage.getItem('urja-seen')) {
    document.body.style.overflow = 'hidden';
    
    var stage = document.getElementById('stage');
    var logoImg = document.getElementById('logoImg');
    var core = document.getElementById('core');
    var ringGlow = document.getElementById('ringGlow');
    var particles = document.getElementById('particles');
    var flash = document.getElementById('flash');
    var label = document.getElementById('progressLabel');
    var fill = document.getElementById('progressFill');
  
    function easeOutCubic(x){ return 1 - Math.pow(1 - x, 3); }
  
    function setMask(rPx, featherPx){
      var m = 'radial-gradient(circle at 50% 50%, black 0px, black ' + rPx + 'px, transparent ' + (rPx+featherPx) + 'px)';
      logoImg.style.webkitMaskImage = m;
      logoImg.style.maskImage = m;
    }
    setMask(0, 30);
  
    var W = stage.clientWidth;
    var maxR = (W/2) + 12; 
  
    var lastParticleTime = 0;
  
    function spawnParticle(rNow){
      var angle = Math.random() * Math.PI * 2;
      var x = 50 + (rNow / W) * 100 * Math.cos(angle);
      var y = 50 + (rNow / W) * 100 * Math.sin(angle);
      var p = document.createElement('div');
      p.className = 'particle';
      p.style.left = x + '%';
      p.style.top = y + '%';
      particles.appendChild(p);
      requestAnimationFrame(function(){
        p.style.opacity = 1;
        p.style.transform = 'translate(-50%,-50%) scale(1.6)';
      });
      setTimeout(function(){
        p.style.opacity = 0;
        p.style.transform = 'translate(-50%,-50%) scale(0.4)';
      }, 90);
      setTimeout(function(){ p.remove(); }, 700);
    }
  
    setTimeout(function(){
      core.classList.add('show');
      label.textContent = 'Igniting the spark';
      fill.style.transition = 'width .4s ease';
      fill.style.width = '8%';
    }, 120);
  
    var EXPAND_START = 520;
    var EXPAND_DUR = 1900;
  
    setTimeout(function(){
      label.textContent = 'Expanding connections';
      var start = null;
      function frame(ts){
        if(!start) start = ts;
        var elapsed = ts - start;
        var t = Math.min(elapsed / EXPAND_DUR, 1);
        var eased = easeOutCubic(t);
        var r = maxR * eased;
  
        setMask(r, 26 - 18*eased); 
        ringGlow.style.width = (r*2) + 'px';
        ringGlow.style.height = (r*2) + 'px';
        ringGlow.style.opacity = (t < 0.94) ? (0.9 - eased*0.15) : (0.9 - eased*0.15) * (1 - (t-0.94)/0.06);
  
        fill.style.transition = 'none';
        fill.style.width = (8 + t*84) + '%';
  
        if(elapsed - lastParticleTime > 55 && t < 0.97){
          spawnParticle(r);
          lastParticleTime = elapsed;
        }
  
        if(t < 1){
          requestAnimationFrame(frame);
        } else {
          finish();
        }
      }
      requestAnimationFrame(frame);
    }, EXPAND_START);
  
    function finish(){
      label.textContent = 'Ready';
      fill.style.transition = 'width .3s ease';
      fill.style.width = '100%';
      core.classList.add('fade');
      flash.classList.add('pulse');
      setTimeout(function(){ flash.classList.remove('pulse'); flash.classList.add('pulse-out'); }, 380);
  
      setTimeout(function(){
        var loader = document.getElementById('loader');
        loader.classList.add('hide');
        setTimeout(function(){
            loader.style.display = 'none';
            sessionStorage.setItem('urja-seen', '1');
            document.body.style.overflow = '';
            triggerReveal();
            runCountUp();
            updateCountdown();
        }, 600);
      }, 800);
    }
    
    // Hard failsafe
    setTimeout(() => {
      const ldr = document.getElementById('loader');
      if (ldr && ldr.style.display !== 'none') {
        ldr.style.display = 'none';
        document.body.style.overflow = '';
        sessionStorage.setItem('urja-seen', '1');
        triggerReveal();
        runCountUp();
        updateCountdown();
      }
    }, 6000);
  } else {
    var loader = document.getElementById('loader');
    if (loader) loader.style.display = 'none';
    setTimeout(() => {
      triggerReveal();
      runCountUp();
      updateCountdown();
    }, 100);
  }


})();


















// ============================================================
// EEG HERO CANVAS ANIMATION
// ============================================================
(function initEEG() {
  const canvas = document.getElementById('eeg-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let w, h, animationId;
  let offset = 0;
  
  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = document.querySelector('.hero-section').offsetHeight || window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  function draw() {
    ctx.clearRect(0, 0, w, h);
    ctx.beginPath();
    ctx.strokeStyle = '#3AA0FF';
    ctx.lineWidth = 2;
    
    const centerY = h / 2;
    const amplitude = 30;
    const frequency = 0.01;
    
    // Occasionally spike
    const isSpike = Math.sin(offset * 0.05) > 0.95;
    
    for (let x = 0; x < w; x++) {
      let y = centerY + Math.sin((x + offset) * frequency) * amplitude;
      if (isSpike && x > w/2 - 50 && x < w/2 + 50) {
        y += (Math.random() - 0.5) * 150; 
      }
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
    offset += 2;
    animationId = requestAnimationFrame(draw);
  }

  // Only animate when home tab is active
  const homeTab = document.getElementById('tab-home');
  const observer = new MutationObserver(() => {
    if (homeTab.hasAttribute('hidden')) {
      cancelAnimationFrame(animationId);
    } else {
      resize();
      draw();
    }
  });
  observer.observe(homeTab, { attributes: true, attributeFilter: ['hidden'] });
  
  if (!homeTab.hasAttribute('hidden')) draw();
})();





(function initBulbParticles() {
  const svg = document.querySelector('.synapse-bulb');
  const group = document.getElementById('bulb-particles');
  const glassPath = document.querySelector('#hitbox-path');
  if (!svg || !group || !glassPath) return;

  const NUM_PARTICLES = 50;
  const colors = ['#f5a623', '#5cb8ff'];
  const particles = [];

  for (let i = 0; i < NUM_PARTICLES; i++) {
    const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    c.setAttribute('r', (Math.random() * 0.5 + 1.0).toFixed(1));
    const color = colors[i % colors.length];
    c.setAttribute('fill', color);
    group.appendChild(c);

    particles.push({
      el: c,
      x: 30 + Math.random() * 40,
      y: 30 + Math.random() * 50,
      vx: (Math.random() - 0.5) * 2,
      vy: (Math.random() - 0.5) * 2,
      baseColor: color,
      rush: null
    });
  }

  const TRAIL_POOL_SIZE = 12;
  const trailPool = [];
  let trailIdx = 0;
  for (let i = 0; i < TRAIL_POOL_SIZE; i++) {
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    t.setAttribute('r', '1.5');
    t.setAttribute('fill', '#ffffff');
    t.style.opacity = '0';
    t.style.pointerEvents = 'none';
    group.appendChild(t);
    trailPool.push({ el: t });
  }

  const pointer = {
    isDown: false, downTime: 0,
    downX: 0, downY: 0,
    x: 50, y: 50,
    hasMoved: false,
    state: 'idle',
    maxVortexRadius: 25
  };

  let lastTapTime = 0;
  let tapCombo = 0;
  let wind = null;
  let doublePulse = null;
  
  const checkPt = svg.createSVGPoint();
  const pathLength = glassPath.getTotalLength();

  // Helper: Find closest distance from point to the path border
  function getDistanceToEdge(px, py) {
    let minSq = Infinity;
    for (let l = 0; l <= pathLength; l += 4) {
      const pt = glassPath.getPointAtLength(l);
      const dx = pt.x - px, dy = pt.y - py;
      const sq = dx*dx + dy*dy;
      if (sq < minSq) minSq = sq;
    }
    return Math.sqrt(minSq);
  }

  function getSvgCoords(e) {
    const pt = svg.createSVGPoint();
    pt.x = e.clientX || (e.touches && e.touches[0].clientX);
    pt.y = e.clientY || (e.touches && e.touches[0].clientY);
    return pt.matrixTransform(svg.getScreenCTM().inverse());
  }

  const prevent = e => e.preventDefault();
  // Removed touchstart/move blocks so mobile users can still scroll vertically
  svg.addEventListener('contextmenu', prevent);
  svg.addEventListener('selectstart', prevent);

  svg.addEventListener('pointerdown', (e) => {
    try { svg.setPointerCapture(e.pointerId); } catch(err) {}
    pointer.isDown = true;
    pointer.downTime = Date.now();
    pointer.hasMoved = false;
    pointer.state = 'idle';
    const coords = getSvgCoords(e);
    pointer.x = pointer.downX = coords.x;
    pointer.y = pointer.downY = coords.y;
    pointer.maxVortexRadius = getDistanceToEdge(pointer.x, pointer.y);
  });

  svg.addEventListener('pointermove', (e) => {
    if (!pointer.isDown) return;
    const coords = getSvgCoords(e);
    const dx = coords.x - pointer.downX;
    const dy = coords.y - pointer.downY;
    
    if (!pointer.hasMoved && (dx*dx + dy*dy > 64)) {
      pointer.hasMoved = true;
      if (pointer.state !== 'hold') pointer.state = 'drag';
    }
    
    pointer.x = coords.x;
    pointer.y = coords.y;
    
    // Update dynamic vortex constraint if dragging the hold center
    if (pointer.state === 'hold') {
       pointer.maxVortexRadius = getDistanceToEdge(pointer.x, pointer.y);
    }

    if (pointer.state === 'drag') {
      const t = trailPool[trailIdx];
      trailIdx = (trailIdx + 1) % TRAIL_POOL_SIZE;
      t.el.style.transition = 'none';
      t.el.setAttribute('cx', pointer.x);
      t.el.setAttribute('cy', pointer.y);
      t.el.setAttribute('r', '1.5');
      t.el.style.opacity = '0.7';
      
      requestAnimationFrame(() => {
        t.el.style.transition = 'opacity 0.4s ease-out, r 0.4s ease-out';
        t.el.setAttribute('r', '6');
        t.el.style.opacity = '0';
      });
    }
  });

  function releasePointer(e) {
    if (!pointer.isDown) return;
    pointer.isDown = false;
    const now = Date.now();
    const duration = now - pointer.downTime;

    if (pointer.state === 'hold') {
      console.log('Hold released - EXPLODE!');
      particles.forEach(p => {
        const dx = p.x - pointer.x, dy = p.y - pointer.y;
        const dist = Math.hypot(dx, dy) || 1;
        p.vx = (dx/dist) * 8 + (Math.random()-0.5)*2;
        p.vy = (dy/dist) * 8 + (Math.random()-0.5)*2;
        p.el.setAttribute('fill', p.baseColor);
      });
    } 
    else if (pointer.state === 'drag' && duration < 400) {
      const vx = (pointer.x - pointer.downX) / (duration||1) * 15;
      const vy = (pointer.y - pointer.downY) / (duration||1) * 15;
      wind = { vx, vy, until: now + 300 };
    } 
    else if (!pointer.hasMoved && duration < 300) {
      if (now - lastTapTime < 350) {
        tapCombo++;
      } else {
        tapCombo = 1;
      }
      lastTapTime = now;

      if (tapCombo >= 2) {
        doublePulse = { step: 'rush', until: now + 250, combo: tapCombo };
      } else {
        particles.forEach(p => {
          const dx = pointer.x - p.x, dy = pointer.y - p.y;
          if (dx*dx + dy*dy < 95*95) {
            p.rush = { x: pointer.x, y: pointer.y, until: now + 170, combo: tapCombo, scattered: false };
            p.el.setAttribute('fill', p.baseColor);
          }
        });
      }
    }
    
    pointer.state = 'idle';
  }

  svg.addEventListener('pointerup', releasePointer);
  svg.addEventListener('pointercancel', releasePointer);

  function animate() {
    const now = Date.now();

    if (pointer.isDown && pointer.state !== 'hold' && !pointer.hasMoved && (now - pointer.downTime) > 350) {
      pointer.state = 'hold';
      pointer.maxVortexRadius = getDistanceToEdge(pointer.x, pointer.y);
      console.log('Hold started!');
    }

    if (doublePulse) {
      if (doublePulse.step === 'rush' && now > doublePulse.until) {
        doublePulse.step = 'explode';
        doublePulse.until = now + 400;
        particles.forEach(p => {
          const dx = p.x - 50, dy = p.y - 57; // 57 is roughly center of mass
          const dist = Math.hypot(dx, dy) || 1;
          const power = 6 * (1 + doublePulse.combo * 0.15);
          p.vx = (dx/dist) * power;
          p.vy = (dy/dist) * power;
          p.el.setAttribute('fill', p.baseColor);
        });
      } else if (doublePulse.step === 'explode' && now > doublePulse.until) {
        doublePulse = null;
      }
    }

    particles.forEach(p => {
      // 1. Interactive Forces
      if (doublePulse && doublePulse.step === 'rush') {
        const dx = 50 - p.x, dy = 57 - p.y;
        p.vx += dx * 0.05; p.vy += dy * 0.05;
        p.vx *= 0.85; p.vy *= 0.85;
        p.el.setAttribute('fill', p.baseColor);
      } 
      else if (pointer.state === 'hold') {
        p.el.setAttribute('fill', p.baseColor);
        const holdDur = now - pointer.downTime;
        const strength = Math.max(0, Math.min(1, (holdDur - 350) / 1800));
        
        const dx = p.x - pointer.x, dy = p.y - pointer.y;
        const dist = Math.hypot(dx, dy) || 1;
        const nx = dx / dist, ny = dy / dist;
        const tx = -ny, ty = nx;
        
        const tangPush = 1.2 + 2.2 * strength;
        
        // Dynamically clamp orbit radius using real path distance
        const baseOrbit = 25 - 20 * strength;
        const maxOrbit = Math.max(1, pointer.maxVortexRadius - 2); // 2px safety padding
        const targetOrbit = Math.min(baseOrbit, maxOrbit);
        
        const radialPull = (dist - targetOrbit) * 0.06;
        
        p.vx += tx * tangPush - nx * radialPull;
        p.vy += ty * tangPush - ny * radialPull;
        p.vx *= 0.85; p.vy *= 0.85;
      } 
      else if (p.rush) {
        if (now < p.rush.until) {
          const dx = p.rush.x - p.x, dy = p.rush.y - p.y;
          const dist = Math.hypot(dx, dy) || 1;
          p.vx += (dx/dist) * 3.2;
          p.vy += (dy/dist) * 3.2;
          p.vx *= 0.85; p.vy *= 0.85;
        } else {
          if (!p.rush.scattered) {
            p.rush.scattered = true;
            p.el.setAttribute('fill', p.baseColor);
            const scatterBase = 3 + Math.random() * 2.5;
            const scatterSpeed = scatterBase * (1 + p.rush.combo * 0.1);
            p.vx = (Math.random()-0.5)*2 * scatterSpeed;
            p.vy = (Math.random()-0.5)*2 * scatterSpeed;
          } else {
            p.rush = null;
          }
        }
      } 
      else if (pointer.state === 'drag') {
        const dx = p.x - pointer.x, dy = p.y - pointer.y;
        const distSq = dx*dx + dy*dy;
        if (distSq < 26*26 && distSq > 0.1) {
          const dist = Math.sqrt(distSq);
          p.vx += (dx / dist) * 0.9;
          p.vy += (dy / dist) * 0.9;
        }
      } 
      
      if (wind && now < wind.until) {
        p.vx += wind.vx * 0.1;
        p.vy += wind.vy * 0.1;
      }

      // 2. Idle Drift
      if (pointer.state !== 'hold' && !p.rush && !(doublePulse && doublePulse.step==='rush')) {
        p.vx += (Math.random() - 0.5) * 0.05;
        p.vy += (Math.random() - 0.5) * 0.05;
        
        const speed = Math.hypot(p.vx, p.vy) || 0.001;
        const newSpeed = speed * 0.9 + 0.5 * 0.1;
        p.vx = (p.vx / speed) * newSpeed;
        p.vy = (p.vy / speed) * newSpeed;
      }

      p.x += p.vx;
      p.y += p.vy;

      // 3. Absolute Boundary Check (Runs every frame for every particle)
      checkPt.x = p.x;
      checkPt.y = p.y;
      
      // If particle escaped the real SVG clip path
      if (!glassPath.isPointInFill(checkPt)) {
        // Find the vector pointing towards the bulb's center of mass (50, 57)
        const cx = 50, cy = 57;
        const dx = cx - p.x;
        const dy = cy - p.y;
        const dist = Math.hypot(dx, dy) || 1;
        
        // Apply an aggressive restorative force inward along the normal
        p.vx += (dx / dist) * 1.5;
        p.vy += (dy / dist) * 1.5;
        
        // Hard-clamp the velocity to prevent glitchy wall-hugging vibration
        p.vx *= 0.6;
        p.vy *= 0.6;
        
        // Immediately nudge the position back inside a bit to avoid getting stuck
        p.x += p.vx;
        p.y += p.vy;
      }

      p.el.setAttribute('cx', p.x.toFixed(2));
      p.el.setAttribute('cy', p.y.toFixed(2));
    });

    requestAnimationFrame(animate);
  }
  
  animate();
})();