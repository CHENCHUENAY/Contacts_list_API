from api.auth_api import login
from config import EMAIL, PASSWORD

def test_login_valid_password():

    response = login(
        email=EMAIL,
        password=PASSWORD
    )

    assert response.status_code == 200