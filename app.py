# Основной backend-файл приложения

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Win-Win Syndicate App Running!'