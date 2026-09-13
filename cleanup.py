import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update the logo filename in global-header
html = html.replace('<img src="./logo.png"', '<img src="./LOGO.jpeg"')

# Remove top-brand
top_brand_pattern = r'<!-- TOP HEADER BRAND -->\s*<div id="top-brand".*?</div>\s*</div>'
html = re.sub(top_brand_pattern, '', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed top-brand and updated logo to LOGO.jpeg!")
