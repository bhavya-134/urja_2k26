import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the header bottom border
old_header = 'border-bottom: 1px solid rgba(242,179,61,0.3);'
new_header = 'border-bottom: 1px solid rgba(58,160,255,0.3);'
html = html.replace(old_header, new_header)

# Fix the logo border
old_logo_border = 'border: 1px solid var(--gold);'
new_logo_border = 'border: 1px solid var(--blue-l);'
html = html.replace(old_logo_border, new_logo_border)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed ALL inline amber styles from the header!")
