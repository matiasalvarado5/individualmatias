import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models.users import User
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from app.database.connection import Base

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_create_user(self):
        user = User(name="John", surname="Doe", username="johndoe", password="password")
        self.session.add(user)
        self.session.commit()

        retrieved_user = self.session.query(User).first()
        self.assertEqual(retrieved_user.username, "johndoe")

    def test_unique_username(self):
        user1 = User(name="John", surname="Doe", username="johndoe", password="password")
        self.session.add(user1)
        self.session.commit()

        user2 = User(name="Jane", surname="Doe", username="johndoe", password="password123")
        self.session.add(user2)

        with self.assertRaises(IntegrityError):
            self.session.commit()

if __name__ == '__main__':
    unittest.main()

