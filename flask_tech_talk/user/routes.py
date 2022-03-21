from flask import request
from flask_tech_talk import db
from flask_tech_talk.user import bp_user
from flask_tech_talk.user.models import User


@bp_user.route('/insert', methods=['POST'])
def insert_user():
    json_data = request.json or {}
    name = json_data.get("name")
    if not name:
        return f"Missing name", 400
    user_object = User(username=name)
    
    db.session.add(user_object)
    db.session.commit()
    
    return f"User {name} inserted"


@bp_user.route('/get')
def get_users():
    users = User.query.all()
    
    if not users:
        return "no user found"
    return {"users": [user.username for user in users]}
