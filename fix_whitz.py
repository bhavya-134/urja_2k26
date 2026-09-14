import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all occurrences of WHIZ with WHITZ
html = html.replace("QUIZ WHIZ BLITZ", "QUIZ WHITZ BLITZ")
html = html.replace("Quiz Whiz Blitz", "Quiz Whitz Blitz")

# Change the category from non-technical to technical for this specific event card
# It looks like: <div data-reveal class="ecard non-technical" data-cat="non-technical" data-name="Quiz Whitz Blitz"
# Let's target it specifically.
html = html.replace('class="ecard non-technical" data-cat="non-technical" data-name="Quiz Whitz Blitz"', 
                    'class="ecard technical" data-cat="technical" data-name="Quiz Whitz Blitz"')

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Updated spelling to WHITZ and category to Technical!")
