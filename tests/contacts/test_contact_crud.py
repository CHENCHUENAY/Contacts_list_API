import random
import pytest

from api.contacts_api import (
    create_contact,
    get_contact,
    update_contact,
    delete_contact
)

# -----------------------------
# Helper: reusable contact creator
# -----------------------------
def create_test_contact(headers):

    email = f"enay_{random.randint(1000,9999)}@test.com"

    payload = {
        "firstName": "Enay",
        "lastName": "QA",
        "email": email,
        "phone": "123456789"
    }

    response = create_contact(headers, payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    return data


# -----------------------------
# Fixture: provides contact to tests
# -----------------------------
@pytest.fixture(scope="function")
def created_contact(headers):
    data = create_test_contact(headers)
    yield data
    delete_contact(headers, data["_id"])  # cleanup: remove test data after each test


# -----------------------------
# TEST: create contact
# -----------------------------
def test_create_contact(headers):
    data = create_test_contact(headers)
    assert "_id" in data


# -----------------------------
# TEST: get contact
# -----------------------------
def test_get_contact(headers, created_contact):

    contact_id = created_contact["_id"]
    response = get_contact(headers, contact_id)
    assert response.status_code == 200


# -----------------------------
# TEST: update contact
# -----------------------------
def test_update_contact(headers, created_contact):

    contact_id = created_contact["_id"]
    update_payload = {
        "firstName": "UpdatedName"
    }
    response = update_contact(headers, contact_id, update_payload)
    assert response.status_code == 200


# -----------------------------
# TEST: delete contact
# -----------------------------
def test_delete_contact(headers, created_contact):

    contact_id = created_contact["_id"]
    response = delete_contact(headers, contact_id)
    assert response.status_code == 200