import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the footer branding to use the exact same blue as the header
html = html.replace('<span style="color:#00f0ff">2K26</span>', '<span style="color:var(--blue-l)">2K26</span>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Unified footer text color to a single shade of blue!")
