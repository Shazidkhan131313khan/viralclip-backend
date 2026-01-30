from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/test")
def test():
    return jsonify({"status": "API working ✅"})

@app.route("/clip", methods=["POST"])
def clip():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    return jsonify({
        "status": "success",
        "message": "Clip processing started",
        "video_url": url
    })
