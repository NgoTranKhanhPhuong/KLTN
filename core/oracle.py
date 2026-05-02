class TestOracle:

    @staticmethod
    def evaluate(actual, expected):

        actual_code = actual.get("status_code")

        expected_code = expected.get("status_code")

        # =========================
        # CASE 1: expected không có status_code
        # → fallback rule-based
        # =========================
        if expected_code is None:
            # nếu API trả 2xx coi là pass
            return 200 <= actual_code < 300, "NO_EXPECTED_STATUS"

        # =========================
        # CASE 2: normal HTTP compare
        # =========================
        if actual_code != expected_code:
            return False, "HTTP_MISMATCH"

        return True, "OK"
        # =========================
        # 1. STATUS CODE CHECK
        # =========================
        status_match = True
        if expected_code is not None:
            status_match = (actual_code == expected_code)

        # =========================
        # 2. HTTP SEMANTIC CHECK
        # =========================
        def is_success(code):
            return 200 <= code < 300

        def is_client_error(code):
            return 400 <= code < 500

        semantic_ok = True

        if expected_type == "success":
            semantic_ok = is_success(actual_code)

        elif expected_type == "error":
            semantic_ok = is_client_error(actual_code)

        # =========================
        # 3. RESPONSE CONTRACT CHECK
        # =========================
        contract_ok = True

        if expected_type == "success":
            contract_ok = "message" in actual_body or actual_type == "success"

        if expected_type == "error":
            contract_ok = "error" in str(actual_body).lower() or actual_type == "error"

        # =========================
        # FINAL RESULT
        # =========================
        passed = status_match and semantic_ok and contract_ok

        return passed, {
            "status_match": status_match,
            "semantic": semantic_ok,
            "contract": contract_ok
        }