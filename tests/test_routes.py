from flask_tech_talk import app 
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


def test_welcome(client):
    response = client.post('/welcome')
    assert response.data == b"<p>Welcome, World!</p>"


def test_welcome_name_age(client):
    response = client.post('/welcome/name', json={"name": "Igor", "age": 21})
    assert response.data == b"<p>Welcome, Igor! Your age is 21</p>"


def test_welcome_name_age_without_json(client):
    response = client.post('/welcome/name')
    assert response.data == b"<p>Welcome, anonymous! Your age is unknown</p>"


