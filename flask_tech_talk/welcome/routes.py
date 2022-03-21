from flask import request
from flask_tech_talk.welcome import bp_welcome


@bp_welcome.route("/")
def welcome_world():
    return "<p>Welcome, World!</p>"


@bp_welcome.route("/name", methods=['POST'])
def welcome_name_age():
    json_data = request.json or {}
    name = json_data.get("name", "anonymous")
    age = json_data.get("age", "unknown")
    return f"<p>Welcome, {name}! Your age is {age}</p>"