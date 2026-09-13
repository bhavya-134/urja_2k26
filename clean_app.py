import re

js_path = 'app.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the old gchip event listeners
old_gchip_pattern = r"document\.querySelectorAll\('\.gchip'\)\.forEach\(chip => \{.*?\}\);\n    \}\);"
# The regex above is tricky. Let's use simple string replacement or a better regex.

start_str = "document.querySelectorAll('.gchip').forEach(chip => {"
if start_str in js:
    start_idx = js.find(start_str)
    end_idx = js.find("});\n    });", start_idx) + 11
    js = js[:start_idx] + js[end_idx:]
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Removed old gchip logic from app.js!")
else:
    print("Could not find old gchip logic.")
