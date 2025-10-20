import random
import time
import threading
from datetime import datetime

from flask import Flask, jsonify, Response
from flask_cors import CORS
from sim_user_count import increment_user_count

app = Flask(__name__)
CORS(app)

user_count = random.randint(10, 50)  # Random number between 10 and 50

def update_user_count():
    global user_count
    while True:
        user_count = increment_user_count(user_count)
        time.sleep(2)

threading.Thread(target=update_user_count, daemon=True).start()


@app.route('/api/count', methods=['GET'])
def get_count():
    """Endpoint polling : retourne le compteur actuel"""


    return jsonify({
        'count': user_count,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8080)
