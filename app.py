from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/test")
def test():
    return "✅ API is working properly!"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
