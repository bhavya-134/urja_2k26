with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('// Lightbox')
if idx != -1:
    snippet = js[max(0, idx-200):idx+200]
    with open('snippet.txt', 'w', encoding='utf-8') as out:
        out.write(snippet)
