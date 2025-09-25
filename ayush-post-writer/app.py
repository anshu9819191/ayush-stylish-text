from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["user_text"]
        option = request.form["option"]

        if option == "1":
            result = f"""
●▬▬▬▬๑۩۩๑▬▬▬▬▬●🍾🍾
🦋┅═══❁⊱💋💋💋💋💋⊰❁═══┅🦋
🦋┅═══❁⊱🖤💞💞💞💞🖤⊰❁═══┅
❤❤❤❤❤❤❤❤❤❤❤😎
{text}
_________(^🍁 🐥^)
||👁️||
❥❥══════❥❥❥══════❥❥ 
||❤️||____________||👁️||
----------☆☆○○°□□☆□□°○○☆☆
😈❤️💋🌿_____||❤️||
•🌻🩶🌻•||______________||🩶||
[[💋😈✋]]____________|| 
"""

        elif option == "2":
            result = f"(({text}))"

        elif option == "3":
            result = f"🪽🐰🦎🪼🌿💫✨✍️🗡️🪱🏵️🌺🍂 {text} 🪽🐰🦎🪼🌿💫✨✍️🗡️🪱🏵️🌺🍂"

        elif option == "4":
            result = f"""
●▬▬▬▬๑۩۩๑▬▬▬▬▬●🍾🍾
((🪽🐰🦎🪼🌿💫✨ {text} ✍️🗡️🪱🏵️🌺🍂))
❤❤❤❤❤❤❤❤❤❤❤😎
😈❤️💋🌿_____||❤️|| [[💋😈✋]]
"""

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
