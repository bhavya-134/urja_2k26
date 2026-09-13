import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the inline amber style with blue
old_span = 'URJA <span style="color: #FF8A00;">2K26</span>'
new_span = 'URJA <span style="color: #3AA0FF;">2K26</span>'
html = html.replace(old_span, new_span)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed inline amber style from header!")
