import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from app.models.post import Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.connection import Base

class TestPostModel(unittest.TestCase):

    def setUp(self):
        # Configuración inicial de la base de datos en memoria para pruebas
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        # Limpiar la base de datos
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_create_post(self):
        # Crear una instancia del modelo Post
        post = Post(author="John Doe", title="Sample Post", body="This is a test post.")
        self.session.add(post)
        self.session.commit()

        # Verificar que el post se haya guardado correctamente
        retrieved_post = self.session.query(Post).first()
        self.assertEqual(retrieved_post.author, "John Doe")
        self.assertEqual(retrieved_post.title, "Sample Post")
        self.assertEqual(retrieved_post.body, "This is a test post.")
        self.assertIsNotNone(retrieved_post.date)

if __name__ == '__main__':
    unittest.main()
