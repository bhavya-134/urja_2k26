import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Completely rewrite the close button CSS to be an obvious sticky button at the top right
pattern = r"\.modal-close-btn \{.*?transition: background 0\.3s; \}"
replacement = ".modal-close-btn { position: sticky; top: -10px; float: right; margin-right: -10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.4); color: #fff; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 24px; cursor: pointer; z-index: 9999; backdrop-filter: blur(5px); }"

css = re.sub(pattern, replacement, css)

with open(css_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)
print("Updated close button CSS!")
