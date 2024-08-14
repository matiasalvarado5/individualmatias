import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from flask import Flask
from app.routes.auth import auth
from unittest.mock import patch, MagicMock


class AuthTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear una aplicación Flask y registrar el blueprint de auth
        cls.app = Flask(__name__)
        cls.app.register_blueprint(auth)
        cls.client = cls.app.test_client()

    @patch('app.routes.auth.get_db_connection')
    @patch('app.routes.auth.register_user')
    @patch('app.routes.auth.select_user')
    def test_register_user(self, mock_select_user, mock_register_user, mock_get_db_connection):
        # Mock de la conexión a la base de datos
        mock_get_db_connection.return_value = (MagicMock(), MagicMock())
        mock_select_user.return_value = None
        response = self.client.post('/auth/register', json={
            'name': 'Test',
            'surname': 'User',
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Usuario registrado correctamente', response.data)

    @patch('app.routes.auth.get_db_connection')
    @patch('app.routes.auth.select_user')
    @patch('app.routes.auth.generate_token')
    def test_login_user(self, mock_generate_token, mock_select_user, mock_get_db_connection):
        # Mock de la conexión a la base de datos
        mock_get_db_connection.return_value = (MagicMock(), MagicMock())
        mock_select_user.return_value = MagicMock(password='hashed_password')
        mock_generate_token.return_value = 'test_token'
        
        with patch('app.routes.auth.check_password_hash', return_value=True):
            response = self.client.post('/auth/login', json={
                'username': 'testuser',
                'password': 'password'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'test_token', response.data)

if __name__ == '__main__':
    unittest.main()
