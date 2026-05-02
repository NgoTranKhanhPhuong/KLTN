def analyze_coverage(test_cases, base_request):

    total_fields = set(base_request.keys())
    tested_fields = set()

    valid = 0
    invalid = 0

    for tc_id, name, tc, expected in test_cases:

        if "Success" in str(expected):
            valid += 1
        else:
            invalid += 1

        tested_fields.update(tc.keys())

    coverage_percent = round(
        len(tested_fields & total_fields) / len(total_fields) * 100,
        2
    ) if total_fields else 0

    return {
        "total": len(test_cases),
        "valid": valid,
        "invalid": invalid,
        "total_fields": len(total_fields),
        "fields_tested": list(tested_fields),
        "coverage_percent": coverage_percent
    }