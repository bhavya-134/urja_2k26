import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace updateCountdown
new_countdown = '''function updateCountdown() {
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
    
    if (bulbFill) {
      bulbFill.style.transform = 	ranslate(0,px) scale(1,);
    }
    const bulbRing = document.getElementById('bulb-ring-active');
    if (bulbRing) {
      const dash = 283;
      bulbRing.style.strokeDashoffset = dash - (dash * pct);
    }
  }'''

js = re.sub(r'function updateCountdown\(\) \{.*?\}(?=\n\s*setInterval)', new_countdown, js, flags=re.DOTALL)

# Add EEG logic at the end of the file
eeg_logic = '''
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
    ctx.strokeStyle = '#F2B33D';
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
'''

# Check if eeg logic already added to prevent duplicates
if 'EEG HERO CANVAS' not in js:
    js += eeg_logic

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js!")
