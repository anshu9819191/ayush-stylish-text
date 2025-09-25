from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Decorative elements for Option 1
DECORATION_1 = """●▬▬▬▬๑۩۩๑▬▬▬▬▬●🍾🍾
🦋┅═══❁⊱💋💋💋💋💋⊰❁═══┅🦋
🦋┅═══❁⊱🖤💞💞💞💞🖤⊰❁═══┅
❤❤❤❤❤❤❤❤❤❤❤😎
(^🍁 🐥^)
||👁️||
❥❥══════❥❥❥══════❥❥
||❤️||||👁️||
----------☆☆○○°□□☆☆
😈❤️💋🌿||❤️||
- 🌻🩶🌻•||||🩶||
[[💋😈✋]]"""

# Emojis for Option 3
EMOJIS_3 = ['🪽', '🐰', '🦎', '🪼', '🌿', '💫', '✨', '✍️', '🗡️', '🪱', '🏵️', '🌺', '🍂']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        option = request.form.get('option', '1')
        
        if not text:
            return render_template('index.html', result="Please enter some text!")
        
        if option == '1':
            # Option 1: Prepend the full decoration to the text
            result = f"{DECORATION_1}\n\n{text}"
        elif option == '2':
            # Option 2: Wrap entire text in (())
            result = f"(({text}))"
        elif option == '3':
            # Option 3: Intersperse emojis around the text (simple framing with random selection)
            import random
            selected_emojis = random.sample(EMOJIS_3, min(5, len(EMOJIS_3)))  # Pick 5 random
            top = ' '.join(selected_emojis[:3])
            bottom = ' '.join(selected_emojis[3:])
            result = f"{top}\n\n{text}\n\n{bottom}"
        elif option == '4':
            # Option 4: Mix all - Decoration 1 + wrap in (()) + Option 3 emojis
            wrapped = f"(({text}))"
            selected_emojis = random.sample(EMOJIS_3, min(3, len(EMOJIS_3)))
            mix_decor = f"{DECORATION_1}\n\n{wrapped}\n\n{' '.join(selected_emojis)}"
            result = mix_decor
        else:
            result = text  # Fallback
        
        return render_template('index.html', result=result, original_text=text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
