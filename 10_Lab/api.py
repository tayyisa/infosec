from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify(message="Hello from Flask API")

if __name__ == '__main__':
    app.run(port=5000)
