from generators.domain_model import DOMAIN

def generate_test_cases(base):

    cases = []
    tc_id = 1

    for field, spec in DOMAIN.items():

        # =====================
        # VALID CASE
        # =====================
        tc = base.copy()
        tc[field] = spec["valid"][0] if "valid" in spec else base.get(field)

        cases.append({
            "id": f"TC_{tc_id:03}",
            "name": f"{field}_valid",
            "data": tc,
            "expected": {
    "status_code": 200,
    "type": "success",
    "message": "OK"
}
        })
        tc_id += 1

        # =====================
        # INVALID CASES
        # =====================
        for v in spec.get("invalid", []):
            tc = base.copy()
            tc[field] = v

            cases.append({
                "id": f"TC_{tc_id:03}",
                "name": f"{field}_invalid",
                "data": tc,
                "expected": {
                    "status_code": 400,
                    "type": "error",
                    "rule": f"{field}_constraint"
                }
            })
            tc_id += 1

        # =====================
        # BOUNDARY CASES
        # =====================
        if "boundary" in spec:
            for b in spec["boundary"]:
                tc = base.copy()
                tc[field] = b

                cases.append({
                    "id": f"TC_{tc_id:03}",
                    "name": f"{field}_boundary",
                    "data": tc,
                    "expected": {
    "status_code": 400,
    "type": "error",
    "message": "validation failed"
}
                })
                tc_id += 1

    return cases