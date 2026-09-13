import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;}', '.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;grid-auto-flow:dense;}')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Added grid-auto-flow:dense!")
