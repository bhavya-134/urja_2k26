import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the full-width styling of gh-menu with a right-aligned, compact styling
old_style = 'display: none; position: fixed; top: 65px; left: 0; right: 0; background: rgba(5,5,8,0.95); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(242,179,61,0.3); z-index: 99998; padding: 20px 0; flex-direction: column; align-items: stretch;'
new_style = 'display: none; position: fixed; top: 75px; right: 20px; width: 180px; background: rgba(5,5,8,0.95); backdrop-filter: blur(15px); border: 1px solid rgba(242,179,61,0.3); border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.8); z-index: 99998; padding: 10px 0; flex-direction: column; align-items: stretch;'

if old_style in html:
    html = html.replace(old_style, new_style)
else:
    # Fallback regex just in case
    html = re.sub(r'<div id="gh-menu" style=".*?">', f'<div id="gh-menu" style="{new_style}">', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated gh-menu inline styles!")
