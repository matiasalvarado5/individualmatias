import sys
import os
import unittest

# Añadir el directorio raíz del proyecto a la ruta de búsqueda
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database.connection import get_server_connection, get_db_connection

class TestConnection(unittest.TestCase):

    def test_get_server_connection(self):
        # Tu código de prueba aquí
        pass

    def test_get_db_connection(self):
        # Tu código de prueba aquí
        pass

if __name__ == '__main__':
    unittest.main()
