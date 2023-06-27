from app import schemas
from .database import session, client


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
