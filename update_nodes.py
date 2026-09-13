import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update the terminal line on the Teams page to 90 nodes
html = html.replace('100 NODES ONLINE', '90 NODES ONLINE')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated node count!")
