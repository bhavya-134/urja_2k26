import os

file_path = 'api/gallery.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Write with Unix line endings
with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("Converted api/gallery.js to UNIX LF")
