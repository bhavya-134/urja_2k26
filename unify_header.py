import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make the '2K26' part of the header inherit the same blue color as 'URJA'
css = css.replace('.gh-name span { color: var(--amber-l); }', '.gh-name span { color: var(--blue-l); }')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Unified header text color to a single shade of blue!")
