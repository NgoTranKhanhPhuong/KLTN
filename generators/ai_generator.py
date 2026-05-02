def ai_generate_test_cases(base, rules):
    if rules is None:
        rules = {}

    cases = []

    for i, (field, rule) in enumerate(rules.items()):
        cases.append((
            f"AI_{i+1:03}",
            f"Kiểm tra nâng cao cho trường {field}",
            base,
            {
                "status": "success",
                "desc": f"Hệ thống xử lý đúng logic của trường {field}"
            }
        ))

    return cases