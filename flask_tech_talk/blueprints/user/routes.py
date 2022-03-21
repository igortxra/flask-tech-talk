from flask import request
from flask_tech_talk.ext.database import db
from flask_tech_talk.blueprints.user.models import User


def insert_user():
    json_data = request.json or {}
    name = json_data.get("name")
    if not name:
        return f"Missing name", 400
    user_object = User(username=name)
    
    db.session.add(user_object)
    db.session.commit()
    
    return f"User {name} inserted"


def get_users():
    users = User.query.all()
    
    if not users:
        return "no user found"
    return {"users": [user.username for user in users]}
