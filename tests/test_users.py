from app import schemas
from .database import session, client
import pytest 
from jose import jwt
from app.config import settings


@pytest.fixture
def test_user(client):
    user_data = {'email': "komron@gmail.com", 
                 "password": "pass123"}
    res = client.post('/users', json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    yield new_user

def test_create_user(client):
    res = client.post('/users/', json={"email": "komron@gmail.com", 
                                      "password": "pass123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "komron@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post('/login', data={"username": test_user['email'], 
                                      "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

# pytest flags

# -x stop after first fail
# -v verbosity
# --disable-warnings run tests without warnings 
