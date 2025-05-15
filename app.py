
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Win-Win Syndicate App Running!'

# Новый маршрут для обработки вебхуков от Kick
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print
