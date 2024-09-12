#!/usr/bin/env python3
"""basic flask app
"""
from flask import Flask, jsonify


app = Flask()


@app.route("/")
def hello():
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
