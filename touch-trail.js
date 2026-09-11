/* ============================================================
   touch-trail.js — Glowing Touch Trail Canvas Effect
   ============================================================ */

(function() {
  'use strict';

  // Only on touch devices, respect reduced motion
  if (!('ontouchstart' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const canvas = document.getElementById('touch-trail-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particles = [];
  let rafId = null;
  let isVisible = true;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  // Pause when tab hidden
  document.addEventListener('visibilitychange', () => {
    isVisible = !document.hidden;
    if (isVisible && !rafId) loop();
  });

  function addParticle(x, y) {
    particles.push({
      x, y,
      life: 1.0,
      size: Math.random() * 3 + 2,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5
    });
    // Limit particles
    if (particles.length > 80) particles.splice(0, particles.length - 80);
  }

  document.addEventListener('touchmove', (e) => {
    if (!isVisible) return;
    for (let i = 0; i < e.touches.length; i++) {
      const t = e.touches[i];
      addParticle(t.clientX, t.clientY);
      if (Math.random() > 0.5) addParticle(t.clientX + (Math.random()-0.5)*8, t.clientY + (Math.random()-0.5)*8);
    }
    if (!rafId) loop();
  }, { passive: true });

  function loop() {
    rafId = requestAnimationFrame(loop);
    if (!isVisible) { rafId = null; return; }

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles = particles.filter(p => p.life > 0.01);

    particles.forEach(p => {
      p.life *= 0.93;
      p.x += p.vx;
      p.y += p.vy;

      const alpha = p.life * 0.5;
      const radius = p.size * p.life;

      // Glow
      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, radius * 3);
      grad.addColorStop(0, `rgba(242,179,61,${alpha})`);
      grad.addColorStop(0.5, `rgba(242,179,61,${alpha * 0.3})`);
      grad.addColorStop(1, `rgba(242,179,61,0)`);

      ctx.beginPath();
      ctx.arc(p.x, p.y, radius * 3, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();

      // Core dot
      ctx.beginPath();
      ctx.arc(p.x, p.y, radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,201,74,${alpha})`;
      ctx.fill();
    });

    if (!particles.length) {
      rafId = null;
    }
  }

})();
