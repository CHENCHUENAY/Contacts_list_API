import random

from api.contacts_api import (
    create_contact,
    get_contact,
    update_contact,
    delete_contact
)

def test_contact_lifecycle_positive(headers):

    payload = {
        "firstName": "Enay",
        "lastName": "QA",
        "birthdate": "1995-01-01",
        "email": f"enay_{random.randint(1000,9999)}@test.com",
        "phone": "123456789"
    }

    # CREATE
    create_response = create_contact(headers, payload)
    assert create_response.status_code == 201

    contact_id = create_response.json()["_id"]

    # GET
    get_response = get_contact(headers, contact_id)
    assert get_response.status_code == 200

    # UPDATE
    update_payload = {
        "firstName": "UpdatedName"
    }

    update_response = update_contact(headers, contact_id, update_payload)
    assert update_response.status_code == 200

    # DELETE
    delete_response = delete_contact(headers, contact_id)
    assert delete_response.status_code == 200

    verify_delete = get_contact(headers, contact_id)
    assert verify_delete.status_code == 404

    print("This test ran: test_contact_lifecycle_positive")