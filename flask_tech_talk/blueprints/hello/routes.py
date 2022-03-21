from flask import request


def hello_world():
    return "<p>Hello, World!</p>"


def hello_name():
    name = request.args.get("n", "anonymous")
    return f"<p>Hello, {name}!</p>"
