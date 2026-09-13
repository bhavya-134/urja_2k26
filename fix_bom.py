import json
import codecs

# Read the package.json (handling potential BOM automatically using utf-8-sig)
file_path = 'package.json'
with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Parse it to ensure it's valid, then write it back as clean UTF-8 (NO BOM)
try:
    data = json.loads(content)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Fixed package.json BOM issue!")
except Exception as e:
    print(f"Error parsing JSON: {e}")
