from flask import request
from flask_tech_talk.hello import bp_hello


@bp_hello.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@bp_hello.route("/name")
def hello_name():
    name = request.args.get("n", "anonymous")
    return f"<p>Hello, {name}!</p>"
