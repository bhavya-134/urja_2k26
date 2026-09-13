import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change max-height of event-modal to avoid the header
css = css.replace("max-height:90vh;", "max-height:calc(100vh - 100px);")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated modal max-height!")
