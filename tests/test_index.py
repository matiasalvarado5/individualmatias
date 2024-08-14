import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
import unittest

class IndexTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar la aplicación para pruebas
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['DEBUG'] = False
    
    def test_index(self):
        # Realiza una solicitud GET a la ruta '/'
        response = self.client.get('/')
        
        # Verifica el código de estado de la respuesta
        self.assertEqual(response.status_code, 200)
        
        # Verifica que se haya renderizado la plantilla correcta
        self.assertIn(b'<!doctype html>', response.data)  # Verifica que la plantilla HTML está siendo rendereada
        
        # Puedes verificar el contenido específico de la plantilla si es necesario
        self.assertIn(b'Index Page Content', response.data)  # Reemplaza 'Index Page Content' con algo que esperas en la plantilla

if __name__ == '__main__':
    unittest.main()
