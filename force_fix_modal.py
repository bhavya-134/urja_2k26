import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the old SVG logic using a robust regex pattern
pattern = r"const iconSvg = cat === 'technical'[\s\S]*?: '<svg viewBox=\"0 0 24 24\"><polygon points=\"13 2 3 14 12 14 11 22 21 10 12 10 13 2\"/></svg>';"
replacement = """const iconDiv = card.querySelector('.ecard-icon');
      const iconSvg = iconDiv ? iconDiv.innerHTML : '';"""

new_js = re.sub(pattern, replacement, js)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_js)
print("Updated icon logic successfully!")
