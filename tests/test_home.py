import unittest
from flask import Flask
from app.routes.home import home
from unittest.mock import patch, MagicMock

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(home)
        self.client = self.app.test_client()

    @patch('app.routes.home.select_all_users')
    def test_home_get_users(self, mock_select_all_users):
        mock_select_all_users.return_value = [
            MagicMock(id=1, name='Test', surname='User', username='testuser')
        ]
        response = self.client.get('/home/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test', response.data)

    @patch('app.routes.home.get_user_by_id')
    def test_home_get_user(self, mock_get_user_by_id):
        mock_get_user_by_id.return_value = MagicMock(id=1, name='Test', surname='User', username='testuser')
        response = self.client.get('/home/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)
