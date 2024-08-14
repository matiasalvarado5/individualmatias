import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.connection import Base
from app.models.user import User

# Crear una base de datos en memoria para las pruebas
@pytest.fixture(scope='function')
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_user(session):
    # Crear un nuevo usuario
    new_user = User(
        name="Alice",
        surname="Wonderland",
        username="alice123",
        password="securepassword"
    )

    # Agregar el usuario a la sesión y hacer commit
    session.add(new_user)
    session.commit()

    # Verificar que el usuario se haya guardado correctamente
    saved_user = session.query(User).filter_by(username="alice123").first()
    
    assert saved_user is not None
    assert saved_user.name == "Alice"
    assert saved_user.surname == "Wonderland"
    assert saved_user.username == "alice123"
    assert saved_user.password == "securepassword"
    assert saved_user.id_rol == 2

def test_username_uniqueness(session):
    # Crear dos usuarios con el mismo username
    user1 = User(
        name="Alice",
        surname="Wonderland",
        username="alice123",
        password="securepassword"
    )

    user2 = User(
        name="Bob",
        surname="Builder",
        username="alice123",  # Mismo username
        password="anotherpassword"
    )

    # Agregar y hacer commit del primer usuario
    session.add(user1)
    session.commit()

    # Intentar agregar y hacer commit del segundo usuario
    session.add(user2)
    with pytest.raises(Exception):  # Esperamos que lance una excepción por la unicidad del username
        session.commit()

def test_default_id_rol(session):
    # Crear un nuevo usuario sin especificar id_rol
    new_user = User(
        name="Charlie",
        surname="Chaplin",
        username="charlie123",
        password="securepassword"
    )

    # Agregar el usuario a la sesión y hacer commit
    session.add(new_user)
    session.commit()

    # Verificar que el usuario tenga el id_rol por defecto
    saved_user = session.query(User).filter_by(username="charlie123").first()
    
    assert saved_user.id_rol == 2  # id_rol por defecto
