from api.auth_api import login
from config import EMAIL
def test_login_invalid_password():

    response = login(
        email=EMAIL,
        password="invalid"
    )

    assert response.status_code == 401


