from flask import Flask, redirect, url_for, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        subprocess.Popen(['python3','stress_cpu.py'])
        return "Success"
    else:
        return socket.gethostname()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
