from flask_tech_talk import create_app
from flask_tech_talk.ext.database import db
import pytest


@pytest.fixture(scope="session")
def app():
    app = create_app()
    db.create_all(app=app)
    yield app
    db.drop_all(app=app)


@pytest.fixture(scope="module")
def client(app):
    client = app.test_client()
    yield client