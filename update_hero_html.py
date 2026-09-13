import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('<section class="hero-section">')
if start_idx == -1:
    print("Could not find hero-section")
    exit(1)
end_idx = html.find('</section>', start_idx) + 10

new_hero = '''<section class="hero-section" id="hero-section">
    <canvas id="eeg-canvas"></canvas>
    
    <svg class="hero-circuit left" viewBox="0 0 100 200" preserveAspectRatio="none">
      <path d="M0,50 L30,50 L40,60 L40,90 L60,110 L60,130" fill="none" stroke="currentColor" stroke-width="0.5"/>
      <circle cx="60" cy="130" r="1.5" fill="currentColor"/>
      <path d="M0,120 L20,120 L30,130 L30,160 L50,180" fill="none" stroke="currentColor" stroke-width="0.5"/>
      <circle cx="50" cy="180" r="1.5" fill="currentColor"/>
    </svg>
    <svg class="hero-circuit right" viewBox="0 0 100 200" preserveAspectRatio="none">
      <path d="M100,70 L70,70 L60,80 L60,110 L40,130 L40,150" fill="none" stroke="currentColor" stroke-width="0.5"/>
      <circle cx="40" cy="150" r="1.5" fill="currentColor"/>
      <path d="M100,140 L80,140 L70,150 L70,180 L50,200" fill="none" stroke="currentColor" stroke-width="0.5"/>
      <circle cx="50" cy="200" r="1.5" fill="currentColor"/>
    </svg>

    <div class="hero-inner">
      <p class="hero-kicker" data-reveal>Department of Electrical Engineering</p>
      <h1 class="hero-title" data-reveal>
        <span class="ht-urja">URJA</span>
        <span class="ht-year">2K26</span>
      </h1>
      <p class="hero-tagline" data-reveal>One Spark, Endless Connections</p>
      <p class="hero-date-venue" data-reveal>September 18-19, 2026 &bull; SCET</p>
      
      <div class="hero-btns" data-reveal>
        <button class="btn-primary btn-ripple" id="hero-cta-btn" onclick="window.URJA.switchTab('events')">EXPLORE EVENTS &rarr;</button>
        <button class="btn-ghost trace-btn" onclick="window.URJA.switchTab('schedule')">
          <span>VIEW SCHEDULE</span>
          <svg class="btn-trace" viewBox="0 0 100 100" preserveAspectRatio="none">
            <rect x="0" y="0" width="100%" height="100%" fill="none" vector-effect="non-scaling-stroke"></rect>
          </svg>
        </button>
      </div>

      <div class="countdown-wrap" data-reveal>
        <div class="cd-label">TIME UNTIL SIGNAL FIRES</div>
        <div class="cd-units">
          <div class="cd-unit"><span id="cd-days" class="cd-num">--</span><span class="cd-sub">DAYS</span></div>
          <span class="cd-colon">:</span>
          <div class="cd-unit"><span id="cd-hours" class="cd-num">--</span><span class="cd-sub">HRS</span></div>
          <span class="cd-colon">:</span>
          <div class="cd-unit"><span id="cd-mins" class="cd-num">--</span><span class="cd-sub">MIN</span></div>
          <span class="cd-colon">:</span>
          <div class="cd-unit"><span id="cd-secs" class="cd-num">--</span><span class="cd-sub">SEC</span></div>
        </div>
        
        <svg class="synapse-bulb" viewBox="0 0 100 130" fill="none" aria-hidden="true">
          <defs>
            <linearGradient id="bg-fill" x1="0" y1="1" x2="0" y2="0">
              <stop offset="0%" stop-color="#FF8A00"/>
              <stop offset="100%" stop-color="#FFC94A"/>
            </linearGradient>
            <clipPath id="bulb-cp">
              <path d="M50,25 Q72,25 72,47 Q72,62 62,72 L62,85 Q62,90 50,90 Q38,90 38,85 L38,72 Q28,62 28,47 Q28,25 50,25Z"/>
            </clipPath>
          </defs>
          <circle id="bulb-ring" cx="50" cy="50" r="45" stroke="#F2B33D" stroke-width="1" stroke-dasharray="283" stroke-dashoffset="283" opacity="0.3"/>
          <circle id="bulb-ring-active" cx="50" cy="50" r="45" stroke="#F2B33D" stroke-width="2" stroke-dasharray="283" stroke-dashoffset="283" style="transition: stroke-dashoffset 1s ease-out;" />
          
          <path d="M50,25 Q72,25 72,47 Q72,62 62,72 L62,85 Q62,90 50,90 Q38,90 38,85 L38,72 Q28,62 28,47 Q28,25 50,25Z" stroke="#F2B33D" stroke-width="1.5" />
          <rect id="bulb-fill" x="28" y="25" width="44" height="65" fill="url(#bg-fill)" clip-path="url(#bulb-cp)" transform="translate(0,65) scale(1,0)" style="transition: transform 1s ease-out; transform-origin: center bottom;" />
          
          <path d="M42,85 L58,85" stroke="#F2B33D" stroke-width="2" stroke-linecap="round"/>
          <path d="M44,90 L56,90" stroke="#F2B33D" stroke-width="1.5" stroke-linecap="round"/>
          <path d="M48,95 L52,95" stroke="#F2B33D" stroke-width="1" stroke-linecap="round"/>
          
          <line x1="50" y1="20" x2="50" y2="16" stroke="#F2B33D" stroke-width="1.5"/>
          <line x1="76" y1="36" x2="80" y2="32" stroke="#F2B33D" stroke-width="1.5"/>
          <line x1="24" y1="36" x2="20" y2="32" stroke="#F2B33D" stroke-width="1.5"/>
        </svg>
      </div>

      <div class="hero-sponsors" data-reveal>
        <div class="hs-powered">
          <span>POWERED BY</span>
          <div class="hs-logo-ph">LOGO</div>
        </div>
        <div class="hs-sep"></div>
        <div class="hs-co">
          <span>CO-POWERED BY</span>
          <div class="hs-logo-ph">LOGO</div>
        </div>
      </div>

      <div class="scroll-indicator" data-reveal>
        <div class="si-line"><div class="si-dot"></div></div>
        <div class="si-text">SIGNAL CONTINUES</div>
      </div>
    </div>
  </section>'''

html = html[:start_idx] + new_hero + html[end_idx:]
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated hero HTML!")
