def test_insert_user(client):
    response = client.post('/user/insert', json={"name": "Igor"})
    assert response.data == b'User Igor inserted'