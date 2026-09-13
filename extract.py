import json

html_outputs = []
with open('recovered_all.txt', 'r', encoding='utf-16') as f:
    for line in f:
        try:
            data = json.loads(line)
            if 'tool_calls' in data:
                for tc in data['tool_calls']:
                    for k, v in tc.get('arguments', {}).items():
                        if isinstance(v, str) and 'tl-cards' in v:
                            html_outputs.append(v)
        except:
            pass

if html_outputs:
    with open('recovered_schedule.html', 'w', encoding='utf-8') as f:
        # get the longest one which is likely the full replacement
        longest = max(html_outputs, key=len)
        f.write(longest)
    print(f"Found {len(html_outputs)} HTML snippets, saved the longest!")
else:
    print("Could not find HTML")
