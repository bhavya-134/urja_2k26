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

with open(file_path, 'w', encoding='ascii') as f:
    json.dump(data, f, indent=2)
print("Created pure ASCII package.json")
