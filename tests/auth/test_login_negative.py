from api.auth_api import login

def test_login_invalid_password():

    response = login(
        email="test2.enay@fake.com",
        password="wrong_password"
    )

    assert response.status_code == 401