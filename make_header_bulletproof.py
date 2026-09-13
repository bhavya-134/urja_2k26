import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the global header bulletproof and clickable
new_header = '''<header id="global-header" style="position: fixed; top: 0; left: 0; right: 0; height: 65px; display: flex; align-items: center; padding: 0 20px; background: rgba(5,5,8,0.9); border-bottom: 1px solid rgba(242,179,61,0.3); z-index: 99999; cursor: pointer; backdrop-filter: blur(15px);" onclick="window.URJA.switchTab('home')">
    <div class="gh-logo" style="width: 40px; height: 40px; border-radius: 50%; overflow: hidden; margin-right: 12px; border: 1px solid var(--gold);">
      <img src="./LOGO.jpeg" alt="Logo" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none';">
    </div>
    <div class="gh-name" style="font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 700; color: #F2B33D; letter-spacing: 1px;">URJA <span style="color: #FF8A00;">2K26</span></div>
  </header>'''

html = re.sub(r'<header id="global-header">.*?</header>', new_header, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated global header to be bulletproof!")
