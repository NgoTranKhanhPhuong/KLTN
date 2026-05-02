def generate_test_cases(base, rules):

    cases = []

    fields = [
        "payment_type_id",
        "to_name",
        "to_phone",
        "to_address",
        "weight",
        "length",
        "width",
        "height",
        "service_type_id"
    ]

    def build_description(field, case_type):
        if case_type == "min":
            return f"Kiểm tra giá trị nhỏ nhất của trường {field}"
        elif case_type == "empty":
            return f"Kiểm tra khi trường {field} để trống"
        else:
            return f"Kiểm tra trường {field}"

    def build_expected(field, case_type):
        if case_type == "empty":
            return f"Hệ thống báo lỗi: {field} không được để trống"
        elif case_type == "min":
            return f"Hệ thống xử lý giá trị nhỏ nhất của {field}"
        else:
            return "Hệ thống xử lý thành công"

    for i, field in enumerate(fields):

        # ===== MIN CASE =====
        tc_min = base.copy()
        tc_min[field] = 0

        cases.append((
            f"TC_{i+1:03}",
            build_description(field, "min"),
            tc_min,
            build_expected(field, "min")
        ))

        # ===== EMPTY CASE =====
        if isinstance(base.get(field), str):
            tc_empty = base.copy()
            tc_empty[field] = ""

            cases.append((
                f"TC_{i+1+100:03}",
                build_description(field, "empty"),
                tc_empty,
                build_expected(field, "empty")
            ))

    return cases

def generate_steps(tc):

    return [
        "Prepare request JSON",
        "Send API request",
        "Receive response",
        "Validate response vs expected",
        "Extract execution features"
    ]