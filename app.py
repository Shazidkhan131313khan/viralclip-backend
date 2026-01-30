from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Viral Clip Backend is running!"

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
        "message": "Clip received",
        "url": url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
