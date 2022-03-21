from flask_tech_talk.blueprints.user.models import User


def test_user_instanciation():
    user = User(username='José')
    assert user.id == None
    assert user.username == 'José'
    assert user.__repr__() == "<User 'José'>"