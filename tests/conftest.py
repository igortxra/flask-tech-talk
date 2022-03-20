from flask_tech_talk import app
import pytest


@pytest.fixture
def client():
    app.testing = True # Change FLask internal behabior to make tests easier
    client = app.test_client()
    return client