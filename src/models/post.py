
from sqlalchemy import Column, Integer, String
from src.database.connection import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(25))
    title = Column(String(25))
    body = Column(String(50))
    date = Column(String(60))

