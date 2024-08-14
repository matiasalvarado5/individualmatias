
from sqlalchemy import Column, Integer, String, DateTime
from app.database.connection import Base
from datetime import datetime


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    author = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    body = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
