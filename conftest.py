import pytest
from api.auth_api import login
from config import EMAIL, PASSWORD

@pytest.fixture(scope="session")
def token():

    response = login(EMAIL, PASSWORD)
    assert response.status_code == 200

    data = response.json()
    assert "token" in data

    return data["token"]


@pytest.fixture
def headers(token):

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    return headers

def pytest_sessionfinish(session, exitstatus):
    # runs once after ALL tests are done
    with open("results/logs/test_run.log", "a") as f:
        f.write("                                --- End of test run ---\n \n")
         