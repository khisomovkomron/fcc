from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
import pytest
from alembic import command

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():   

        db = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()
    # command.upgrade('head')
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)
    # command.downgrade('base')



def test_root(client):

    res = client.get('/')
    print(res.json().get('message')) 
    assert res.json()['message'] == "This is Fastapi Course", "Incorrect message text"
    assert res.status_code == 200, "Incorrect status code"



def test_create_user(client):
    res = client.post('/users', json={"email": "komron@gmail.com", 
                                      "password": "pass123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "komron@gmail.com"
    assert res.status_code == 201
    


# pytest flags

# -x stop after first fail
# -v verbosity
# --disable-warnings run tests without warnings 
