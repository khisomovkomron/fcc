from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_root():

    res = client.get('/')
    print(res.json().get('message')) 
    assert res.json()['message'] == "This is Fastapi Course", "Incorrect message text"
    assert res.status_code == 200, "Incorrect status code"



def test_create_user():
    res = client.post('/users', json={"email": "komron3@gmail.com", 
                                      "password": "pass123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "komron3@gmail.com"
    assert res.status_code == 201
    


# pytest flags

# -x stop after first fail
# -v verbosity
# --disable-warnings run tests without warnings 
