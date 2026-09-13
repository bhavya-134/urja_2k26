import re

api_path = 'api/gallery.js'
with open(api_path, 'r', encoding='utf-8') as f:
    api = f.read()

# Increase pageSize to 200 for smooth 100+ image loading
api = api.replace("pageSize: 50,", "pageSize: 200,")

with open(api_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(api)
print("Updated API pageSize to 200!")
