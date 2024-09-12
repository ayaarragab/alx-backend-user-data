#!/usr/bin/env python3
"""basic flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ Base route for authentication service API """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def register() -> str:
    """
    register endpoint
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)
    try:
        user = AUTH.register_user(email=email, password=password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    else:
        return jsonify({"email": f"{email}", "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """login
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)
    isValid = AUTH.valid_login(email, password)
    if not isValid:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": f"{email}", "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/profile', methods=['GET'])
def logout() -> str:
    """logout
    """
    session_id = request.cookies['session_id']
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
