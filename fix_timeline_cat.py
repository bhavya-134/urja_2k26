import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix R-1
pattern_r1 = r'<div class="tl-card non-technical" data-scat="non-technical" data-id="ev-d1-9">([\s\S]*?)<div class="tl-title">THE QUIZ WHITZ BLITZ \(R-1\)</div>'
replace_r1 = r'<div class="tl-card technical" data-scat="technical" data-id="ev-d1-9">\1<div class="tl-title">THE QUIZ WHITZ BLITZ (R-1)</div>'
html = re.sub(pattern_r1, replace_r1, html)

# Fix R-2
pattern_r2 = r'<div class="tl-card non-technical" data-scat="non-technical" data-id="ev-d2-2">([\s\S]*?)<div class="tl-title">THE QUIZ WHITZ BLITZ \(R-2\)</div>'
replace_r2 = r'<div class="tl-card technical" data-scat="technical" data-id="ev-d2-2">\1<div class="tl-title">THE QUIZ WHITZ BLITZ (R-2)</div>'
html = re.sub(pattern_r2, replace_r2, html)

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Updated timeline cards to Technical!")
