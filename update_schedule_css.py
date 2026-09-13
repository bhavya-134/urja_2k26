import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change font-size from 16px to 14px for tl-title
old_title = ".tl-title { font-family: var(--font-head); font-size: 16px; font-weight: 700; letter-spacing: 1px; color: #fff; line-height: 1.3; padding-right: 24px; }"
new_title = ".tl-title { font-family: var(--font-head); font-size: 14px; font-weight: 700; letter-spacing: 1px; color: #fff; line-height: 1.3; padding-right: 24px; }"
css = css.replace(old_title, new_title)

# Also let's change text-transform just in case, but Title Case in HTML already handles it.
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated CSS font size!")
