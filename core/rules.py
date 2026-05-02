DOMAIN_RULES = {
    "order": {
        "required_fields": [
            "payment_type_id",
            "to_name",
            "to_phone",
            "to_address"
        ],
        "constraints": {
            "weight": {"min": 1},
            "length": {"min": 1},
            "width": {"min": 1},
            "height": {"min": 1},
            "service_type_id": {"allowed": [1, 2, 3]}
        }
    }
}
def validate_business_logic(data):

    if data.get("weight", 0) <= 0:
        return False, "Invalid weight"

    if not data.get("to_name"):
        return False, "Name required"

    return True, "OK"