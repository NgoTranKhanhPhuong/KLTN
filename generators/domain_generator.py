# generators/domain_generator.py

def generate_domain_cases(base):

    cases = []

    DOMAIN = {
        "payment_type_id": {
            "valid": [1, 2, 3],
            "invalid": [-1, 0, 999],
            "boundary": [1, 3]
        },
        "to_name": {
            "valid": ["A", "Nguyen Van A"],
            "invalid": ["", None, "12345"],
            "boundary": ["A", "A"*50]
        },
        "to_phone": {
            "valid": ["0909", "0911222333"],
            "invalid": ["abc", "", None],
            "boundary": ["0", "999999999999"]
        },
        "weight": {
            "valid": [1, 10, 50],
            "invalid": [-1, 0],
            "boundary": [0.1, 1000]
        }
    }

    for field, rules in DOMAIN.items():

        for v in rules["valid"]:
            c = base.copy()
            c[field] = v
            cases.append({
                "name": f"{field}_valid",
                "data": c,
                "expected": {"status_code": 200}
            })

        for v in rules["invalid"]:
            c = base.copy()
            c[field] = v
            cases.append({
                "name": f"{field}_invalid",
                "data": c,
                "expected": {"status_code": 400}
            })

        for v in rules["boundary"]:
            c = base.copy()
            c[field] = v
            cases.append({
                "name": f"{field}_boundary",
                "data": c,
                "expected": {"status_code": 200}
            })

    return cases