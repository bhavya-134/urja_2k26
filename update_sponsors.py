import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title Sponsor with Powered By
html = html.replace('<div class="stier-label">TITLE SPONSOR</div>', '<div class="stier-label">POWERED BY</div>')
html = re.sub(
    r'<div class="scard title"><div class="scard-text">TITLE SPONSOR<br><span>Your Logo Here</span></div></div>',
    r'<div class="scard title"><img src="./powered by.jpeg" alt="Powered By"></div>',
    html
)

# Replace Gold Sponsors with Co-Powered By
html = html.replace('<div class="stier-label">GOLD SPONSORS</div>', '<div class="stier-label">CO-POWERED BY</div>')
html = re.sub(
    r'<div class="sgrid gold"><div class="scard"><div class="scard-text">GOLD SPONSOR 1</div></div><div class="scard"><div class="scard-text">GOLD SPONSOR 2</div></div></div>',
    r'<div class="sgrid gold" style="grid-template-columns: 1fr;"><div class="scard"><img src="./copowered by.jpeg" alt="Co-Powered By"></div></div>',
    html
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated tab-sponsors successfully!")
