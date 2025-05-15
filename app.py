import os
from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/')
def index():
    return 'Win-Win Syndicate App Running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Получен вебхук:", data)
    return jsonify({"status": "received"}), 200

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
