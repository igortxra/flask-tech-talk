from main import app
import pytest


@pytest.fixture
def client():
    app.testing = True # Change FLask internal behabior to make tests easier
    client = app.test_client()
    return client


def test_hello_world(client):
    response = client.get('/')
    assert response.data == b"<p>Hello, World!</p>"


def test_hello_name(client):
    response = client.get('/name')
    assert response.data == b"<p>Hello, anonymous!</p>"


def test_hello_name_passing_name(client):
    response = client.get("/name?n=Jhon Doe")
    assert response.data == b"<p>Hello, Jhon Doe!</p>"
