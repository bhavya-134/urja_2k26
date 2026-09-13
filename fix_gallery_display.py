import re

js_path = 'gallery-app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the toggle logic to explicitly remove/set the hidden attribute
pattern = r"viewMemories\.style\.display = 'block';\s*viewCurrent\.style\.display = 'none';"
replacement = """viewMemories.style.display = 'block'; viewMemories.removeAttribute('hidden');
      viewCurrent.style.display = 'none'; viewCurrent.setAttribute('hidden', '');"""
js = re.sub(pattern, replacement, js)

pattern2 = r"viewCurrent\.style\.display = 'block';\s*viewMemories\.style\.display = 'none';"
replacement2 = """viewCurrent.style.display = 'block'; viewCurrent.removeAttribute('hidden');
      viewMemories.style.display = 'none'; viewMemories.setAttribute('hidden', '');"""
js = re.sub(pattern2, replacement2, js)

with open(js_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated Gallery toggle logic to fix hidden attribute override!")
