import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace uppercase
html = html.replace("QUIZ WHITZ BLITZ", "QUIZ WHIZ BLITZ")
# Replace title case
html = html.replace("Quiz Whitz Blitz", "Quiz Whiz Blitz")

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Fixed spelling error in index.html!")
