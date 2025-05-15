import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Win-Win Syndicate App Running!'

# Маршрут для обработки вебхуков от Kick
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📥 Получен вебхук:", data)  # лог в консоль
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"

    app.run(host=host, port=port, debug=debug)

