from api.contacts_api import create_contact


def test_invalid_email_contact_creation(headers):

    payload = {
        "firstName": "Enay",
        "lastName": "QA",
        "email": "invalid_email",
        "phone": "123456789"
    }

    response = create_contact(headers, payload)

    assert response.status_code == 400

    data = response.json()
    assert data is not None


def test_create_contact_without_token():

    payload = {
        "firstName": "Enay",
        "lastName": "QA",
        "email": "test@test.com",
        "phone": "123456789"
    }

    response = create_contact({}, payload)

    assert response.status_code == 401

    data = response.json()
    assert data is not None


def test_create_contact_missing_firstname(headers):

    payload = {
        "lastName": "QA",
        "email": "test@test.com",
        "phone": "123456789"
    }

    response = create_contact(headers, payload)

    assert response.status_code == 400

    data = response.json()
    assert data is not None