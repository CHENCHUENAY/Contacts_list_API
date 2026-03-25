contact_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"}  # optional — API accepts contacts without phone
    },
    "required": ["_id", "firstName", "lastName", "email"]
}