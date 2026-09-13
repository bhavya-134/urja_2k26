import os

files_to_check = ['api/gallery.js']

for fp in files_to_check:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {fp}")
