from flask import request


def welcome_world():
    return "<p>Welcome, World!</p>"


def welcome_name_age():
    json_data = request.json or {}
    name = json_data.get("name", "anonymous")
    age = json_data.get("age", "unknown")
    return f"<p>Welcome, {name}! Your age is {age}</p>"
