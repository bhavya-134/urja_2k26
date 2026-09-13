import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the events grid container
grid_start_idx = html.find('<div class="events-grid" id="events-grid">')
if grid_start_idx == -1:
    print("Could not find events-grid")
    exit(1)

grid_start_idx = html.find('>', grid_start_idx) + 1
grid_end_idx = html.find('</div>\n    </section>', grid_start_idx)

grid_content = html[grid_start_idx:grid_end_idx]

# Split by the ecard start
blocks = grid_content.split('<div data-reveal class="ecard')

ecards = {}
# The first block is just whitespace
for block in blocks[1:]:
    full_block = '<div data-reveal class="ecard' + block
    
    # Extract name
    name_match = re.search(r'data-name="(.*?)"', full_block)
    if name_match:
        name = name_match.group(1).strip()
        ecards[name] = full_block

# Desired order
desired_order = [
    "Aavishkar",
    "F1 Arena",
    "SYNC: The Tech Relay",
    "Power Up",
    "Abhivyakti",
    "Human Ludo",
    "Game of Drones",
    "Quiz Whiz Blitz",
    "Escape the Unknown",
    "Clash of Minds",
    "Robo-Soccer"
]

# Note: The user said "SYNC - The Tech Relay" but the HTML says "SYNC: The Tech Relay" or "SYNC"
# Same for Robo-Soccer (sometimes Robo Soccer). I'll map them carefully.
ordered_html = ""
for target_name in desired_order:
    found = False
    for k in ecards.keys():
        if target_name.lower().replace('-', '').replace(':', '') in k.lower().replace('-', '').replace(':', ''):
            ordered_html += "\n      " + ecards[k].strip() + "\n"
            found = True
            break
        elif k.lower().startswith(target_name.lower().split(' ')[0]):
            ordered_html += "\n      " + ecards[k].strip() + "\n"
            found = True
            break
    if not found:
        print(f"Warning: could not find {target_name}")

new_html = html[:grid_start_idx] + "\n" + ordered_html + "\n    " + html[grid_end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Reordered events successfully!")
