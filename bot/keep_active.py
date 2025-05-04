from flask import Flask
import threading 

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'

def run():
    app.run(host="0.0.0.0", port=8080)

def start_server():
        server_thread = threading.Thread(target=run)
        server_thread.start()
        threading.start()