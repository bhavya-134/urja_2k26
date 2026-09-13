import re

app_path = 'app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace iconSvg logic with extracting the ecard-icon contents
old_icon_logic = """const iconSvg = cat === 'technical'
          ? '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07M4.93 4.93a10 10 0 000 14.14M8.46 8.46a5 5 0 000 7.07"/></svg>'
          : '<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>';"""

new_icon_logic = """const iconDiv = card.querySelector('.ecard-icon');
        const iconSvg = iconDiv ? iconDiv.innerHTML : '';"""

js = js.replace(old_icon_logic, new_icon_logic)

with open(app_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(js)
print("Updated app.js to use the card's actual image logo in the modal!")
