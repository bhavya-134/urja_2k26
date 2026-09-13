import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gallery block
old_gallery_pattern = r'<div class="tab-panel" id="tab-gallery" hidden>.*?<!-- ==================== TAB: TEAMS ==================== -->'

new_gallery = '''<div class="tab-panel" id="tab-gallery" hidden>
    <section class="page-section">
      <div class="page-header" data-reveal>
        <div class="page-label">SIGNAL ARCHIVED</div>
        <h2 class="page-title">LIVE GALLERY</h2>
        <p class="page-sub">Photos sync automatically from Google Drive.</p>
      </div>

      <!-- Filters -->
      <div class="gallery-chips" data-reveal style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px;">
        <button class="gchip active" data-gf="all">ALL</button>
        <button class="gchip" data-gf="aavishkar">AAVISHKAR</button>
        <button class="gchip" data-gf="robo-soccer">ROBO SOCCER</button>
        <button class="gchip" data-gf="f1-arena">F1 ARENA</button>
        <button class="gchip" data-gf="sync">SYNC</button>
      </div>
      
      <!-- Dynamic Grid Container -->
      <div class="gallery-grid" id="dynamic-gallery-grid">
        <!-- Javascript will inject images here -->
      </div>
      
    </section>
  </div>
  
  <!-- ==================== TAB: TEAMS ==================== -->'''

html = re.sub(old_gallery_pattern, new_gallery, html, flags=re.DOTALL)

# Inject script tag at the bottom
if '<script src="gallery-app.js" defer></script>' not in html:
    html = html.replace('<script src="app.js" defer></script>', '<script src="app.js" defer></script>\n  <script src="gallery-app.js" defer></script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated gallery HTML!")
