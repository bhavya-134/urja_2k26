try:
    with open('gallery-app.js', 'r', encoding='utf-8') as f:
        code = f.read()
    print("Length of gallery-app.js:", len(code))
except Exception as e:
    print(e)
