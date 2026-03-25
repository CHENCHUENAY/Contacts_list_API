import random

from api.contacts_api import (
    create_contact,
    get_contact,
    update_contact,
    delete_contact
)
from jsonschema import validate
from schemas.contact_schema import contact_schema
from utils.logger import logger

def test_contact_lifecycle_positive(headers):

    payload = {
        "firstName": "Enay",
        "lastName": "QA",
        "birthdate": "1995-01-01",
        "email": f"enay_{random.randint(1000, 9999)}@test.com",
        "phone": "123456789"
    }

    # -------------------
    # CREATE
    # -------------------
    logger.info(f"Creating contact: {payload['email']}")
    response = create_contact(headers, payload)
    assert response.status_code == 201

    data = response.json()
    validate(instance=data, schema=contact_schema)

    contact_id = data["_id"]
    logger.info(f"Contact created with ID: {contact_id}")

    # -------------------
    # GET
    # -------------------
    logger.info(f"Fetching contact ID: {contact_id}")
    response = get_contact(headers, contact_id)
    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=contact_schema)
    logger.info("GET contact passed schema validation")

    # -------------------
    # UPDATE
    # -------------------
    update_payload = {"firstName": "Chenchu"}

    logger.info(f"Updating contact ID: {contact_id} with payload: {update_payload}")
    response = update_contact(headers, contact_id, update_payload)
    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=contact_schema)

    assert data["firstName"] == "Chenchu"
    logger.info(f"Contact updated. New firstName: {data['firstName']}")

    # -------------------
    # DELETE
    # -------------------
    logger.info(f"Deleting contact ID: {contact_id}")
    response = delete_contact(headers, contact_id)
    assert response.status_code == 200
    logger.info("Contact deleted successfully")

    # verify deletion
    logger.info(f"Verifying deletion — expecting 404 for ID: {contact_id}")
    response = get_contact(headers, contact_id)
    assert response.status_code == 404
    logger.info("Deletion verified. Contact no longer exists.")