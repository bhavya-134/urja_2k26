import re

api_path = 'api/gallery.js'
with open(api_path, 'r', encoding='utf-8') as f:
    api = f.read()

# Revert pageSize to 50 just in case that broke the Google API
api = api.replace("pageSize: 200,", "pageSize: 50,")

with open(api_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(api)
print("Reverted API pageSize to 50!")
