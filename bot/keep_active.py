from flask import Flask
import threading 

### This file is used to keep the bot alive by running a Flask server that responds to ping requests.

app = Flask(__name__)

@app.route('/ping')
def ping():
    print("Ping received")
    return 'Pong!'

def run():
    app.run(host="0.0.0.0", port=8080)

def start_server():
        server_thread = threading.Thread(target=run)
        server_thread.start()
        threading.start()