from flask_tech_talk import app
from flask import request


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/name")
def hello_name():
    name = request.args.get("n", "anonymous")
    return f"<p>Hello, {name}!</p>"


@app.route("/welcome", methods=["POST"])
def welcome_world():
    return f"<p>Welcome, World!</p>"


@app.route("/welcome/name", methods=['POST'])
def welcome_name_age():
    json_data = request.json or {}
    name = json_data.get("name", "anonymous")
    age = json_data.get("age", "unknown")
    return f"<p>Welcome, {name}! Your age is {age}</p>"

