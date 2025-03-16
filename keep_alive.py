from flask import Flask
import threading

app = Flask(__name__)

@app.route("/keep-alive")
def keep_alive():
    return "I'm alive!", 200

def run_keep_alive():
    app.run(host="0.0.0.0", port=8081)

# Start keep-alive server in a background thread
threading.Thread(target=run_keep_alive, daemon=True).start()
