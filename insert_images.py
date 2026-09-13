import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Schedule image
html = html.replace('src="./schedule.png"', 'src="./URJA TIME TABLE.jpg"')

# Replace Powered By placeholders
powered_by_html = '''<div class="hs-powered">
          <span>POWERED BY</span>
          <img src="./powered by.jpeg" class="hs-logo" alt="Powered By">
        </div>'''
html = re.sub(
    r'<div class="hs-powered">\s*<span>POWERED BY</span>\s*<div class="hs-logo-ph">LOGO</div>\s*</div>',
    powered_by_html,
    html
)

# Replace Co-Powered By placeholders
copowered_by_html = '''<div class="hs-co">
          <span>CO-POWERED BY</span>
          <img src="./copowered by.jpeg" class="hs-logo" alt="Co-Powered By">
        </div>'''
html = re.sub(
    r'<div class="hs-co">\s*<span>CO-POWERED BY</span>\s*<div class="hs-logo-ph">LOGO</div>\s*</div>',
    copowered_by_html,
    html
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML images successfully!")
