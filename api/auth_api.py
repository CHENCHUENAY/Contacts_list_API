import requests
from config import BASE_URL


def login(email, password):

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(
        f"{BASE_URL}/users/login",
        json=payload
    )

    return response