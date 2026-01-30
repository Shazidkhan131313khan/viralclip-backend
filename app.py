from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Backend connected successfully",
        "url": data.get("url")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Backend connected successfully",
        "url": data.get("url")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
