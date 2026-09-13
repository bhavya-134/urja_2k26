import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Map of event names to their logo files
logos = {
    "Aavishkar": "./logos/AAVISHKAR.jpeg",
    "F1 Arena": "./logos/F1.jpeg",
    "SYNC: The Tech Relay": "./logos/SYNC THE TECH RELAY.jpeg",
    "Power Up": "./logos/POWER UP.jpeg",
    "Abhivyakti": "./logos/ABHIVYAKTI.jpeg",
    "Human Ludo": "./logos/HUMAN LUDO.jpeg",
    "Game of Drones": "./logos/GAME OF DRONE.jpeg",
    "Quiz Whiz Blitz": "./logos/QUIZ WHIZ BLITZ.jpeg",
    "Escape the Unknown": "./logos/ESCAPE THE UNKNOWN.jpeg",
    "Clash of Minds": "./logos/CLASH OF MINDS.png",
    "Robo-Soccer": "./logos/ROBO SOCCER.jpeg"
}

for event_name, logo_path in logos.items():
    # The regex looks for the ecard block that contains this event_name
    # Then it finds the <div class="ecard-icon">...</div> right before it
    # We can match the exact structure:
    # <div class="ecard-icon">
    #   <svg ...>...</svg>
    # </div>
    # <h3 class="ecard-name">Event Name</h3>
    
    # Let's use a simpler approach. We will split by '<h3 class="ecard-name">' + event_name + '</h3>'
    # The part BEFORE this split ends with the ecard-icon div.
    
    parts = html.split('<h3 class="ecard-name">' + event_name + '</h3>')
    if len(parts) > 1:
        before = parts[0]
        # Find the last <div class="ecard-icon"> in `before`
        icon_start = before.rfind('<div class="ecard-icon">')
        icon_end = before.rfind('</div>') + 6 # end of the icon div
        
        # Replace the contents of ecard-icon
        new_icon = f'<div class="ecard-icon" style="overflow: hidden; padding: 2px;"><img src="{logo_path}" alt="{event_name} Logo" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;"></div>\n          '
        
        parts[0] = before[:icon_start] + new_icon
        html = f'<h3 class="ecard-name">{event_name}</h3>'.join(parts)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated event logos!")
