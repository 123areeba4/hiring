from flask import Flask, request, jsonify, render_template
from gpt4all import GPT4All

app = Flask(__name__)

# Load GPT4All Model (Download pehli dafa hoga)
model = GPT4All("orca-mini-3b.gguf2.q4_0")

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")
    response = model.generate(user_message)
    return jsonify({"reply": response})

if __name__ == "_main_":
    app.run(debug=True)