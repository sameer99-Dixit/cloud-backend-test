from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "backend",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
