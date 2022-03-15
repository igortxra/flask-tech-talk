from main import app
from flask import request


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/name")
def hello_name():
    name = request.args.get("n", "anonymous")
    return f"<p>Hello, {name}!</p>"