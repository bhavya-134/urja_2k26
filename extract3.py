import json
import codecs
import sys

longest = ''
filepath = r"C:\Users\Dell\.gemini\antigravity\brain\2a08fdd2-89c2-44b7-9abb-af7b4f704262\.system_generated\logs\transcript_full.jsonl"
with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            data = json.loads(line)
            if 'tool_calls' in data:
                for tc in data['tool_calls']:
                    args = tc.get('arguments', {})
                    if 'ReplacementContent' in args and 'tl-cards' in args['ReplacementContent']:
                        if len(args['ReplacementContent']) > len(longest):
                            longest = args['ReplacementContent']
                    elif 'CodeContent' in args and 'tl-cards' in args['CodeContent']:
                        if len(args['CodeContent']) > len(longest):
                            longest = args['CodeContent']
        except Exception as e:
            pass

if longest:
    with open('recovered_schedule.html', 'w', encoding='utf-8') as f:
        f.write(longest)
    print("Saved to recovered_schedule.html!")
else:
    print("Not found.")
