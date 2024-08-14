import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app
from flask import json

class AuthTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def test_register_get(self):
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pagina de registro', response.data)

    def test_register_post(self):
        response = self.client.post('/auth/register', json={
            "name": "John",
            "surname": "Doe",
            "username": "johndoe",
            "password": "securepassword"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Usuario registrado correctamente', response.data)

    def test_login_get(self):
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pagina de inicio de sesion', response.data)

    def test_login_post(self):
        response = self.client.post('/auth/login', json={
            "username": "johndoe",
            "password": "securepassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Inicio de sesion correcto', response.data)

    def test_logout(self):
        response = self.client.post('/auth/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Sesion Finalizada')

if __name__ == '__main__':
    unittest.main()
