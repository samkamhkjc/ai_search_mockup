#!/usr/bin/env python3
"""Flask app to serve the AI Search POC."""
import os
from flask import Flask, send_from_directory

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
@app.route("/index.html")
def index():
    return send_from_directory(ROOT, "index.html")


@app.route("/results.html")
def results():
    return send_from_directory(ROOT, "results.html")


@app.route("/data/<path:filename>")
def data(filename):
    return send_from_directory(os.path.join(ROOT, "data"), filename)


@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory(os.path.join(ROOT, "css"), filename)


@app.route("/js/<path:filename>")
def js(filename):
    return send_from_directory(os.path.join(ROOT, "js"), filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="localhost", port=port, debug=False)
