/* ============================================================
   schedule.js — Schedule Timeline Logic
   ============================================================ */

(function() {
  'use strict';

  // ====== DAY TOGGLE ======
  const dayBtns = document.querySelectorAll('.day-btn');
  const timelines = { 1: document.getElementById('timeline-day1'), 2: document.getElementById('timeline-day2') };
  let currentDay = 1;

  function switchDay(day) {
    currentDay = day;
    dayBtns.forEach(b => {
      const isActive = Number(b.dataset.day) === day;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-pressed', isActive);
    });
    Object.entries(timelines).forEach(([d, el]) => {
      if (!el) return;
      if (Number(d) === day) {
        el.classList.add('active');
        el.style.opacity = '0';
        requestAnimationFrame(() => {
          el.style.transition = 'opacity 300ms ease';
          el.style.opacity = '1';
        });
      } else {
        el.classList.remove('active');
      }
    });
    applyScheduleFilter(currentSchedFilter);
    checkLiveIndicator();
  }

  dayBtns.forEach(btn => {
    btn.addEventListener('click', () => switchDay(Number(btn.dataset.day)));
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); switchDay(Number(btn.dataset.day)); }
    });
  });

  // ====== CATEGORY FILTER ======
  const schedFilterBtns = document.querySelectorAll('.sched-filter-btn');
  let currentSchedFilter = 'all';

  function applyScheduleFilter(filter) {
    currentSchedFilter = filter;
    schedFilterBtns.forEach(b => {
      const isActive = b.dataset.sfilter === filter;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-pressed', isActive);
    });
    const activeTimeline = timelines[currentDay];
    if (!activeTimeline) return;
    const nodes = activeTimeline.querySelectorAll('.timeline-node');
    nodes.forEach(node => {
      const cat = node.dataset.scat || 'default';
      const filtered = filter !== 'all' && cat !== filter && cat !== 'default' && cat !== 'break';
      node.classList.toggle('filtered-out', filtered && !(cat === 'default' || cat === 'break'));
    });
  }

  schedFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => applyScheduleFilter(btn.dataset.sfilter));
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); applyScheduleFilter(btn.dataset.sfilter); }
    });
  });

  // ====== NODE EXPAND (ACCORDION) ======
  document.querySelectorAll('.timeline-node-header').forEach(header => {
    header.addEventListener('click', () => {
      const node = header.closest('.timeline-node');
      if (!node) return;
      const details = node.querySelector('.node-details');
      if (!details) return; // break nodes have no details
      const expanded = node.classList.toggle('expanded');
      header.setAttribute('aria-expanded', expanded);
    });
    header.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); header.click(); }
    });
  });

  // ====== LIVE PULSE INDICATOR ======
  // Fest dates: Day 1 = 2026-11-01, Day 2 = 2026-11-02 (placeholder)
  const FEST_DAY1_START = new Date('2026-11-01T09:00:00');
  const FEST_DAY1_END   = new Date('2026-11-01T20:00:00');
  const FEST_DAY2_START = new Date('2026-11-02T09:00:00');
  const FEST_DAY2_END   = new Date('2026-11-02T20:00:00');

  const liveIndicator = document.getElementById('live-indicator');

  function checkLiveIndicator() {
    const now = new Date();
    let isLive = false;
    if (currentDay === 1 && now >= FEST_DAY1_START && now <= FEST_DAY1_END) isLive = true;
    if (currentDay === 2 && now >= FEST_DAY2_START && now <= FEST_DAY2_END) isLive = true;

    if (liveIndicator) {
      liveIndicator.classList.toggle('visible', isLive);
    }

    // Mark current node as live
    const activeTimeline = timelines[currentDay];
    if (!activeTimeline) return;
    activeTimeline.querySelectorAll('.node-dot').forEach(d => d.classList.remove('live'));

    if (isLive) {
      const now = new Date();
      const nowMin = now.getHours() * 60 + now.getMinutes();
      const nodes = activeTimeline.querySelectorAll('.timeline-node');
      let liveNode = null;
      nodes.forEach(node => {
        const timeEl = node.querySelector('.node-time');
        if (!timeEl) return;
        const [h, m] = timeEl.textContent.split(':').map(Number);
        const nodeMin = h * 60 + m;
        if (nodeMin <= nowMin) liveNode = node;
      });
      if (liveNode) {
        const dot = liveNode.querySelector('.node-dot');
        if (dot) dot.classList.add('live');
      }
    }
  }

  checkLiveIndicator();
  setInterval(checkLiveIndicator, 60000); // update every minute

  // Initialize day 1
  switchDay(1);

})();
