try:
    with open('teams-app.js', 'r', encoding='utf-8') as f:
        content = f.read()
    if content.count('{') != content.count('}'):
        print(f"Brace mismatch: {content.count('{')} vs {content.count('}')}")
    else:
        print("Braces balanced. Syntax OK.")
except Exception as e:
    print(e)
