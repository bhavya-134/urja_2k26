import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

fixed_transform = r"bulbFill.setAttribute('transform', `translate(0,${(65 - 65 * pct).toFixed(1)}) scale(1,${pct.toFixed(3)})`);"

js = re.sub(r'bulbFill\.style\.transform = .*?;', fixed_transform, js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed app.js syntax error!")
