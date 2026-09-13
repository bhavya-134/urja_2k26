import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gallery grid with an 11-item version
old_grid_pattern = r'<div class="gallery-grid" id="gallery-grid">.*?</div>\s*<div style="text-align: center; margin-top: 50px;" data-reveal>'

new_grid = '''<div class="gallery-grid" id="gallery-grid">
        <div data-reveal class="gitem col2 row2"><img src="./GALLERY/1.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+1'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/2.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+2'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/3.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+3'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem row2"><img src="./GALLERY/4.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+4'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/5.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+5'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/6.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+6'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem col2"><img src="./GALLERY/7.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+7'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/8.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+8'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem row2"><img src="./GALLERY/9.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+9'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem"><img src="./GALLERY/10.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+10'"><div class="gitem-label">URJA Memory</div></div>
        <div data-reveal class="gitem col2"><img src="./GALLERY/11.jpg" alt="URJA Memory" loading="lazy" onerror="this.src='https://placehold.co/600x600/1a1a1f/F2B33D?text=Photo+11'"><div class="gitem-label">URJA Memory</div></div>
      </div>

      <div style="text-align: center; margin-top: 50px;" data-reveal>'''

html = re.sub(old_grid_pattern, new_grid, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML with 11 gallery slots!")
