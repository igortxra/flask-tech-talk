from flask_tech_talk.user.models import User
from flask_tech_talk import app, db


def test_user_instanciation():
    user = User(username='José')
    assert user.id == None
    assert user.username == 'José'
    assert user.__repr__() == "<User 'José'>"