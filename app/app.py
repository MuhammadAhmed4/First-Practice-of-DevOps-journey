from flask import Flask, jsonify
import socket
import pyt

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from DevOps Project 1", hostname=socket.gethostname())


@app.route("/health")
def health():
    return jsonify(status="ok"), 200
