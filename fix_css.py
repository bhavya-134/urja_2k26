import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the global btn-ghost overriding
css = css.replace('.btn-ghost { border-color: rgba(58, 160, 255, 0.4); color: var(--blue-l); }', '.btn-ghost.blue { border-color: rgba(58, 160, 255, 0.4); color: var(--blue-l); }')
css = css.replace('.btn-ghost:hover { background: rgba(58, 160, 255, 0.1); border-color: var(--blue-l); box-shadow: 0 0 15px rgba(58, 160, 255, 0.2); }', '.btn-ghost.blue:hover { background: rgba(58, 160, 255, 0.1); border-color: var(--blue-l); box-shadow: 0 0 15px rgba(58, 160, 255, 0.2); }')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Fixed btn-ghost blue scoping!")
