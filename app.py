from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/')
def index():
    return 'Win-Win Syndicate App Running!'

# Новый маршрут для обработки вебхуков от Kick
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Получен вебхук:", data)  # для логов
    return jsonify({"status": "received"}), 200
