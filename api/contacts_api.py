import requests
from config import BASE_URL


def create_contact(headers, payload):

    response = requests.post(
        f"{BASE_URL}/contacts",
        headers=headers,
        json=payload
    )

    return response


def get_contact(headers, contact_id):

    response = requests.get(
        f"{BASE_URL}/contacts/{contact_id}",
        headers=headers
    )

    return response


def update_contact(headers, contact_id, payload):

    response = requests.patch(
        f"{BASE_URL}/contacts/{contact_id}",
        headers=headers,
        json=payload
    )

    return response


def delete_contact(headers, contact_id):

    response = requests.delete(
        f"{BASE_URL}/contacts/{contact_id}",
        headers=headers
    )

    return response