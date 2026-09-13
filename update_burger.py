import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('color: #F2B33D;', 'color: #3AA0FF;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated header menu button to blue!")
