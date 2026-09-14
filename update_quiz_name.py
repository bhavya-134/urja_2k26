import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update the event card name to precisely what they asked for
html = html.replace('<h3 class="ecard-name">Quiz Whitz Blitz</h3>', '<h3 class="ecard-name">QUIZ WHITZ BLITZ</h3>')
html = html.replace('<h3 class="ecard-name">Quiz Whiz Blitz</h3>', '<h3 class="ecard-name">QUIZ WHITZ BLITZ</h3>')

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Updated quiz name in HTML!")
