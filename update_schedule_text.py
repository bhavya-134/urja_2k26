import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all tl-title tags and convert their contents to Title Case
def title_case(match):
    text = match.group(1)
    # Special cases handling
    # text.title() converts "ROUND-1" to "Round-1"
    # But let's just use simple title case
    cased = text.title()
    # Fix some specific acronyms if needed, like F1, PR, etc.
    cased = cased.replace("F1", "F1").replace("Pr ", "PR ").replace("Ir ", "IR ")
    return f'<div class="tl-title">{cased}</div>'

html = re.sub(r'<div class="tl-title">(.*?)</div>', title_case, html)

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Updated HTML to Title Case!")
