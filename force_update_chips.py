import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gallery-chips div and all its buttons
pattern = r"<div class=\"gallery-chips\" data-reveal style=\"display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px;\">[\s\S]*?</div>"
new_chips = """<div class="gallery-chips" data-reveal style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px;">
            <button class="gchip active" data-gf="all">ALL</button>
            <button class="gchip" data-gf="faces-of-urja">FACES OF URJA</button>
            <button class="gchip" data-gf="decoration">DECORATION</button>
            <button class="gchip" data-gf="aavishkar">AAVISHKAR</button>
            <button class="gchip" data-gf="f1-arena">F1 ARENA</button>
            <button class="gchip" data-gf="sync">SYNC</button>
            <button class="gchip" data-gf="power-up">POWER UP</button>
            <button class="gchip" data-gf="abhivyakti">ABHIVYAKTI</button>
            <button class="gchip" data-gf="human-ludo">HUMAN LUDO</button>
            <button class="gchip" data-gf="game-of-drones">GAME OF DRONES</button>
            <button class="gchip" data-gf="quiz-whiz">QUIZ WHIZ BLITZ</button>
            <button class="gchip" data-gf="escape">ESCAPE THE UNKNOWN</button>
            <button class="gchip" data-gf="clash-of-minds">CLASH OF MINDS</button>
            <button class="gchip" data-gf="robo-soccer">ROBO SOCCER</button>
          </div>"""

html = re.sub(pattern, new_chips, html)

with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print("Updated Gallery HTML chips!")
