import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change modal close button to top left
old_btn = ".modal-close-btn { position: absolute; top: 12px; right: 12px;"
new_btn = ".modal-close-btn { position: absolute; top: 12px; left: 12px; right: auto;"
css = css.replace(old_btn, new_btn)

# Make sure to update the hover state if it's currently hardcoded to gold, let's make it blue if it was updated,
# Wait, let's just do the left change first.
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Moved modal close button to the top left!")
