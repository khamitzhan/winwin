

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Win-Win Kick MVP работает!"

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))  # здесь 8000 вместо 5000
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    
    app.run(host=host, port=port, debug=debug)
