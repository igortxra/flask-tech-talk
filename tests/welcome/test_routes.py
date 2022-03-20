def test_welcome(client):
    response = client.get('/welcome/')
    assert response.data == b"<p>Welcome, World!</p>"


def test_welcome_name_age(client):
    response = client.post('/welcome/name', json={"name": "Igor", "age": 21})
    assert response.data == b"<p>Welcome, Igor! Your age is 21</p>"


def test_welcome_name_age_without_json(client):
    response = client.post('/welcome/name')
    assert response.data == b"<p>Welcome, anonymous! Your age is unknown</p>"


