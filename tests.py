from main import app
from unittest import TestCase


class BasicTests(TestCase):

    def test_hello_world(self):
        app.testing = True
        with app.test_client() as client:
            response = client.get('/')
        self.assertEqual(response.data, b"<p>Hello, World!</p>")

    def test_hello_name(self):
        app.testing = True
        with app.test_client() as client:
            response = client.get('/name')
        self.assertEqual(response.data, b"<p>Hello, anonymous!</p>")

    def test_hello_name_passing_name(self):
        app.testing = True
        with app.test_client() as client:
            response = client.get("/name?n=Jhon Doe")
        self.assertEqual(response.data, b"<p>Hello, Jhon Doe!</p>")
