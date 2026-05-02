def equivalence_partition(field, rule, base):
    cases = []

    if rule.get("type") == "string":
        tc = base.copy()
        tc[field] = "VALID"
        cases.append((f"{field}_valid", tc, "Valid input"))

        tc = base.copy()
        tc[field] = ""
        cases.append((f"{field}_invalid_empty", tc, "Should fail - empty"))

    return cases


def boundary_test(field, rule, base):
    cases = []

    if "min" in rule:
        tc = base.copy()
        tc[field] = rule["min"]
        cases.append((f"{field}_min", tc, "Boundary min"))

    if "max" in rule:
        tc = base.copy()
        tc[field] = rule["max"]
        cases.append((f"{field}_max", tc, "Boundary max"))

        tc = base.copy()
        tc[field] = rule["max"] + 1
        cases.append((f"{field}_over", tc, "Should fail - over max"))

    return cases


def dependency_test(rule, base):
    cases = []

    if rule.get("dependency"):
        tc = base.copy()
        tc["cod_amount"] = 100000
        tc.pop("payment_type_id", None)

        cases.append(("dependency_violation", tc, "Should fail - dependency violation"))

    return cases


def generate_test_cases(base, rules):
    all_cases = []

    for field, rule in rules.items():
        all_cases += equivalence_partition(field, rule, base)
        all_cases += boundary_test(field, rule, base)
        all_cases += dependency_test(rule, base)

    final_cases = []

    for i, case in enumerate(all_cases):

        if not isinstance(case, tuple) or len(case) != 3:
            raise Exception(f"Broken case format: {case}")

        name, data, expected = case
        tc_id = f"TC{i+1:03}"

        final_cases.append((tc_id, name, data, expected))

    return final_cases