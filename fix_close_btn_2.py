import re

css_path = 'styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

pattern = r"\.modal-close-btn \{.*?backdrop-filter: blur\(5px\); \}"
replacement = ".modal-close-btn { position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.1); border: 2px solid #fff; color: #fff; border-radius: 50%; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; cursor: pointer; z-index: 9999; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }"

css = re.sub(pattern, replacement, css)

with open(css_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)
print("Updated close button CSS to be massive and absolute!")
