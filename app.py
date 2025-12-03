from flask import Flask, render_template, request, redirect
import json
import random

app = Flask(__name__)

def load_quotes():
    try:
        with open("quotes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_quotes(quotes):
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

@app.route("/")
def home():
    quotes = load_quotes()
    random_quote = random.choice(quotes) if quotes else "Aucune citation pour le moment. Ajoutez-en une !"
    return render_template("index.html", quote=random_quote)

@app.route("/add", methods=["POST"])
def add_quote():
    new_quote = request.form.get("quote")
    if new_quote and new_quote.strip():
        quotes = load_quotes()
        quotes.append(new_quote.strip())
        save_quotes(quotes)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
