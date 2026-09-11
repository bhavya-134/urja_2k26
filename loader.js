/* ============================================================
   loader.js — Logo Formation Cinematic Sequence
   ============================================================ */

(function() {
  'use strict';

  const overlay = document.getElementById('loader-overlay');
  if (!overlay) return;

  // Skip loader if seen this session
  if (sessionStorage.getItem('urja-loader-seen')) {
    overlay.style.display = 'none';
    document.body.style.overflow = '';
    return;
  }

  // Prevent scroll during loader
  document.body.style.overflow = 'hidden';

  const svg = document.getElementById('loader-svg');
  if (!svg) return;

  // Get all animated elements
  const signalAmber = document.getElementById('signal-amber');
  const signalBlue  = document.getElementById('signal-blue');
  const logoRing    = document.getElementById('logo-ring');
  const logoCircuits= document.getElementById('logo-circuits');
  const logoNeurons = document.getElementById('logo-neurons');
  const logoBulb    = document.getElementById('logo-bulb');
  const loaderSpark = document.getElementById('loader-spark');
  const letters     = document.querySelectorAll('.urja-letter');
  const tagline     = document.getElementById('loader-tagline');
  const subtext     = document.getElementById('loader-subtext');
  const cta         = document.getElementById('loader-cta');

  // Compute path lengths
  function setPathReady(el, length) {
    if (!el) return;
    const paths = el.tagName === 'path' ? [el] : el.querySelectorAll('path, circle');
    paths.forEach(p => {
      const len = p.getTotalLength ? p.getTotalLength() : 100;
      p.style.strokeDasharray = len;
      p.style.strokeDashoffset = len;
      p.style.transition = 'none';
    });
  }

  function animatePath(el, duration, delay) {
    if (!el) return;
    const paths = el.tagName === 'path' || el.tagName === 'circle' ? [el] : el.querySelectorAll('path, circle');
    paths.forEach((p, i) => {
      const len = p.getTotalLength ? p.getTotalLength() : 100;
      p.style.strokeDasharray = len;
      p.style.strokeDashoffset = len;
      setTimeout(() => {
        p.style.transition = `stroke-dashoffset ${duration}ms ease`;
        p.style.strokeDashoffset = '0';
      }, delay + (i * 80));
    });
  }

  // Prepare all elements — hidden
  [signalAmber, signalBlue].forEach(el => {
    if (el) {
      const len = el.getTotalLength ? el.getTotalLength() : 80;
      el.style.strokeDasharray = len;
      el.style.strokeDashoffset = len;
    }
  });

  if (logoRing) {
    const len = logoRing.getTotalLength ? logoRing.getTotalLength() : 628;
    logoRing.style.strokeDasharray = len;
    logoRing.style.strokeDashoffset = len;
    logoRing.style.opacity = '0';
  }

  if (logoCircuits) {
    logoCircuits.style.opacity = '0';
    setPathReady(logoCircuits, 100);
  }
  if (logoNeurons) {
    logoNeurons.style.opacity = '0';
    setPathReady(logoNeurons, 100);
  }
  if (logoBulb) logoBulb.style.opacity = '0';
  if (loaderSpark) loaderSpark.style.opacity = '0';

  // SEQUENCE
  // Step 1 (0ms): amber signal travels from left
  setTimeout(() => {
    if (signalAmber) {
      signalAmber.style.transition = 'stroke-dashoffset 300ms ease';
      signalAmber.style.strokeDashoffset = '0';
    }
  }, 100);

  // Step 2 (300ms): blue signal from right
  setTimeout(() => {
    if (signalBlue) {
      signalBlue.style.transition = 'stroke-dashoffset 300ms ease';
      signalBlue.style.strokeDashoffset = '0';
    }
  }, 300);

  // Step 3 (600ms): spark glow at center
  setTimeout(() => {
    if (loaderSpark) {
      loaderSpark.style.transition = 'opacity 100ms ease';
      loaderSpark.style.opacity = '0.9';
      setTimeout(() => {
        loaderSpark.style.opacity = '0.2';
      }, 150);
    }
  }, 600);

  // Step 4 (800ms): ring draws in
  setTimeout(() => {
    if (logoRing) {
      logoRing.style.opacity = '1';
      logoRing.style.transition = 'stroke-dashoffset 400ms ease';
      logoRing.style.strokeDashoffset = '0';
    }
  }, 800);

  // Step 5 (1200ms): circuits appear
  setTimeout(() => {
    if (logoCircuits) {
      logoCircuits.style.opacity = '1';
      animatePath(logoCircuits, 250, 0);
    }
  }, 1200);

  // Step 6 (1600ms): neurons appear
  setTimeout(() => {
    if (logoNeurons) {
      logoNeurons.style.opacity = '1';
      animatePath(logoNeurons, 250, 0);
    }
  }, 1500);

  // Step 7 (2000ms): bulb lights up
  setTimeout(() => {
    if (logoBulb) {
      logoBulb.style.transition = 'opacity 300ms ease, filter 300ms ease';
      logoBulb.style.opacity = '1';
      logoBulb.style.filter = 'brightness(1.5) drop-shadow(0 0 8px #F2B33D)';
    }
    if (loaderSpark) {
      loaderSpark.style.transition = 'opacity 200ms ease';
      loaderSpark.style.opacity = '0.6';
    }
  }, 2000);

  // Step 8 (2300ms): URJA letters fire one by one
  setTimeout(() => {
    letters.forEach((letter, i) => {
      setTimeout(() => {
        letter.style.animation = 'letter-flicker 400ms ease forwards';
        letter.style.animationDelay = '0ms';
      }, i * 80);
    });
  }, 2300);

  // Step 9 (2600ms): tagline, subtext, CTA
  setTimeout(() => {
    if (tagline) {
      tagline.style.transition = 'opacity 400ms ease';
      tagline.style.opacity = '1';
    }
  }, 2600);

  setTimeout(() => {
    if (subtext) {
      subtext.style.transition = 'opacity 400ms ease';
      subtext.style.opacity = '1';
    }
  }, 2800);

  setTimeout(() => {
    if (cta) {
      cta.style.transition = 'opacity 400ms ease';
      cta.style.opacity = '1';
    }
  }, 2900);

  // Complete loader at 3.4s
  function completeLoader() {
    sessionStorage.setItem('urja-loader-seen', '1');
    document.body.style.overflow = '';
    overlay.classList.add('fade-out');
    setTimeout(() => {
      overlay.style.display = 'none';
    }, 450);
  }

  // CTA button skips loader
  if (cta) {
    cta.addEventListener('click', completeLoader);
    cta.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') completeLoader();
    });
  }

  // Auto-complete
  setTimeout(completeLoader, 3400);

})();
