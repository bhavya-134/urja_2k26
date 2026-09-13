import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Aggressively remove the modal swipe down logic
js = re.sub(r"modal\.addEventListener\('touchstart', e => { mTY = e\.touches\[0\]\.clientY; }[\s\S]*?closeModal\(\); \}, \{ passive: true \}\);", "", js)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Aggressively removed modal swipe logic!")
