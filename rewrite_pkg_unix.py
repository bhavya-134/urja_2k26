import json
import os

file_path = 'package.json'

data = {
  "name": "urja-2k26-backend",
  "version": "1.0.0",
  "dependencies": {
    "googleapis": "^134.0.0"
  }
}

# Write with Unix line endings
with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(data, f, indent=2)
print("Created pure UNIX package.json")
