with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's find 'document.querySelectorAll('.gitem').forEach' or 'Lightbox' which was right below it
idx = js.find('// Lightbox')
if idx != -1:
    print(js[max(0, idx-300):idx+200])
else:
    print("Could not find Lightbox section.")
