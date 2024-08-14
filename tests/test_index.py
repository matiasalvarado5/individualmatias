import unittest
from flask import Flask
from app.routes.index import index

class IndexTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(index)
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'index/index.html', response.data)

