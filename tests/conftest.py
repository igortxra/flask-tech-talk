from flask_tech_talk import app, db
import pytest


@pytest.fixture(scope="module")
def client():
    app.testing = True # Change FLask internal behavior to make tests easier
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
    db.create_all()
    client = app.test_client()
    yield client
    db.session.remove()
    db.drop_all()
