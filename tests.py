from main import hello_world
from unittest import TestCase


class BasicTests(TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(),"<p>Hello, World!</p>")