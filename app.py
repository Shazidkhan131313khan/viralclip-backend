from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Viral Clip Backend Running 🚀"

@app.route("/clip", methods=["POST"])
def clip_video():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return jsonify({
        "status": "success",
        "message": "Video downloaded successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
