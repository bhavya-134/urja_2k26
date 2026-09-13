
(function(){
  var stage = document.getElementById('stage');
  var logoImg = document.getElementById('logoImg');
  var core = document.getElementById('core');
  var ringGlow = document.getElementById('ringGlow');
  var particles = document.getElementById('particles');
  var flash = document.getElementById('flash');
  var label = document.getElementById('progressLabel');
  var fill = document.getElementById('progressFill');

  function easeOutCubic(x){ return 1 - Math.pow(1 - x, 3); }

  // mask starts fully closed (nothing visible) except a pinhole
  function setMask(rPx, featherPx){
    var m = 'radial-gradient(circle at 50% 50%, black 0px, black ' + rPx + 'px, transparent ' + (rPx+featherPx) + 'px)';
    logoImg.style.webkitMaskImage = m;
    logoImg.style.maskImage = m;
  }
  setMask(0, 30);

  var W = stage.clientWidth;
  var maxR = (W/2) + 12; // covers the visible circular crop plus a little buffer

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

  // Step 1: core spark appears
  setTimeout(function(){
    core.classList.add('show');
    label.textContent = 'Igniting the spark';
    fill.style.transition = 'width .4s ease';
    fill.style.width = '8%';
  }, 120);

  // Step 2: ring expansion begins
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

      setMask(r, 26 - 18*eased); // edge feather tightens as it grows
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
        document.getElementById('site').style.display = 'flex';
      }, 800);
    }, 1100);
  }
})();

