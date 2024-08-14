import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.connection import Base
from app.models.post import Post

class TestPostModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear la base de datos en memoria y la sesión
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        # Cerrar la conexión a la base de datos
        cls.engine.dispose()

    def setUp(self):
        # Crear una nueva sesión antes de cada test
        self.session = self.Session()

    def tearDown(self):
        # Cerrar la sesión después de cada test
        self.session.close()

    def test_create_post(self):
        # Crear un nuevo post
        new_post = Post(
            author="John Doe",
            title="My First Post",
            body="This is the body of my first post"
        )

        # Agregar el post a la sesión y hacer commit
        self.session.add(new_post)
        self.session.commit()

        # Verificar que el post se haya guardado correctamente
        saved_post = self.session.query(Post).filter_by(title="My First Post").first()

        self.assertIsNotNone(saved_post)
        self.assertEqual(saved_post.author, "John Doe")
        self.assertEqual(saved_post.title, "My First Post")
        self.assertEqual(saved_post.body, "This is the body of my first post")
        self.assertIsNotNone(saved_post.date)

    def test_post_without_author(self):
        # Crear un post sin autor (esto debería fallar debido a la restricción de nullable=False)
        new_post = Post(
            title="Title without Author",
            body="This post should fail"
        )

        # Intentar agregar y hacer commit del post
        self.session.add(new_post)
        with self.assertRaises(Exception):  # Esperamos que lance una excepción
            self.session.commit()

    def test_post_without_title(self):
        # Crear un post sin título (esto debería fallar debido a la restricción de nullable=False)
        new_post = Post(
            author="John Doe",
            body="This post has no title"
        )

        # Intentar agregar y hacer commit del post
        self.session.add(new_post)
        with self.assertRaises(Exception):  # Esperamos que lance una excepción
            self.session.commit()

    def test_post_without_body(self):
        # Crear un post sin cuerpo (esto debería fallar debido a la restricción de nullable=False)
        new_post = Post(
            author="John Doe",
            title="This post has no body"
        )

        # Intentar agregar y hacer commit del post
        self.session.add(new_post)
        with self.assertRaises(Exception):  # Esperamos que lance una excepción
            self.session.commit()

if __name__ == '__main__':
    unittest.main()
