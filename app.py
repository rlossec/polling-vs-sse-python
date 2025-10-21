import random
import time
import threading
from datetime import datetime, timezone
import json

from flask import Flask, jsonify, Response
from flask_cors import CORS
from sim_user_count import increment_user_count

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


user_count = random.randint(10, 50)

def update_user_count():
    global user_count
    while True:
        user_count = increment_user_count(user_count)
        random_delay = random.randint(2, 3)
        time.sleep(random_delay)

threading.Thread(target=update_user_count, daemon=True).start()


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route('/api/count', methods=['GET'])
def get_count():
    """Endpoint polling : retourne le compteur actuel"""


    return jsonify({
        'count': user_count,
        'timestamp': datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/stream", methods=["GET"])
def stream():
    """Envoie le compteur en temps réel via SSE"""

    def generate():
        last_value = None
        while True:
            global user_count

            if user_count != last_value:
                last_value = user_count
                data = json.dumps({
                    "count": user_count,
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
                yield f"data: {data}\n\n"

            time.sleep(2)

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


if __name__ == '__main__':
    print("🚀 Serveur démarré sur http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
