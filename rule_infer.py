def infer_rules(base_request):

    rules = {}

    for field, value in base_request.items():

        if isinstance(value, str):
            rules[field] = {
                "type": "string",
                "required": True
            }

        elif isinstance(value, int):
            rules[field] = {
                "type": "int",
                "min": 0,
                "max": max(value * 10, 100)
            }

        elif isinstance(value, list):
            rules[field] = {
                "type": "array",
                "required": True
            }

        else:
            rules[field] = {
                "type": "unknown"
            }

    return rules