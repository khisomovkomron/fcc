from app import schemas
from jose import jwt
from app.config import settings
import pytest

def test_create_user(client):
    res = client.post('/users/', json={'email': "komron@gmail.com", 
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


@pytest.mark.parametrize('email, password, status_code', [
    ('wrongemail@gmail.com', 'password123', 403),
    ('komron@gmail.com', 'wrongpass', 403),
    ('wrongemail@gmail.com', 'wrongpass', 403),
    (None, 'wrongpass', 422),
    ('komron@gmail.com', None, 422),
])
def test_incorrect_login(client, email, password, status_code):
    res = client.post('/login', data={'username': email,
                                      'password': password})
    
    assert res.status_code == status_code
    assert res.json().get('detail') == 'Invalid credentials'

# pytest flags

# -x stop after first fail
# -v verbosity
# --disable-warnings run tests without warnings 
