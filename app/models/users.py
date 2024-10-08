from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    surname = Column(String(25))
    username = Column(String(25), unique=True)
    password = Column(String(300))
    id_rol = Column(Integer,default=2)

