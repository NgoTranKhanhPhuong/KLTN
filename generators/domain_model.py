DOMAIN = {
    "payment_type_id": {
        "type": "int",
        "valid": [1, 2, 3],
        "invalid": [-1, 0, 999],
        "boundary": [1, 3],
        "required": True
    },
    "to_name": {
        "type": "string",
        "min_len": 1,
        "max_len": 50,
        "invalid": ["", None, "12345"],
        "required": True
    },
    "to_phone": {
        "type": "string",
        "pattern": "phone_vn",
        "invalid": ["abc", "", None],
        "required": True
    },
    "weight": {
        "type": "float",
        "min": 0.1,
        "max": 500,
        "boundary": [0.1, 500],
        "invalid": [-1, 0],
        "required": True
    }
}