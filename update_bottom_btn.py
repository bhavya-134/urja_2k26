import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Shrink the bottom close button
old_btn = 'style="width: 100%; padding: 16px; border-radius: 40px; background: transparent; border: 1px solid var(--dim); color: var(--dim); font-family: var(--font-head); font-weight: 700; font-size: 15px; cursor: pointer; margin-top: -8px;"'
new_btn = 'style="width: auto; padding: 10px 24px; border-radius: 30px; background: transparent; border: 1px solid var(--dim); color: var(--dim); font-family: var(--font-head); font-weight: 600; font-size: 13px; cursor: pointer; margin-top: -4px;"'

js = js.replace(old_btn, new_btn)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated bottom close button size!")
