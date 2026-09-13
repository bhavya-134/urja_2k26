import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject Global Header
header_html = '''
<!-- GLOBAL HEADER -->
<header id="global-header">
  <div class="gh-logo">
    <!-- Drop your fest logo here -->
    <img src="./logo.png" alt="Logo" onerror="this.style.display='none'; this.parentNode.innerHTML='LOGO';">
  </div>
  <div class="gh-name">URJA <span>2K26</span></div>
</header>
'''
# Find <canvas id="trail-canvas" aria-hidden="true"></canvas> and inject after it
trail_canvas = '<canvas id="trail-canvas" aria-hidden="true"></canvas>'
if trail_canvas in html:
    html = html.replace(trail_canvas, trail_canvas + "\n" + header_html)

# 2. Inject Schedule Image in Hero
schedule_img_html = '''
      <div class="hero-schedule-img" data-reveal onclick="window.URJA.switchTab('schedule')">
        <div class="hsi-label">VIEW MASTER SCHEDULE</div>
        <img src="./schedule.png" alt="Event Schedule" class="hsi-image" onerror="this.src='https://placehold.co/600x320/1a1a1f/F2B33D?text=Master+Schedule'">
      </div>
'''
# Find <div class="hero-sponsors" data-reveal> and inject before it
sponsors_div = '<div class="hero-sponsors" data-reveal>'
if sponsors_div in html:
    html = html.replace(sponsors_div, schedule_img_html + "\n      " + sponsors_div)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected header and schedule image successfully!")
