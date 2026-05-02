import requests
import json

from generators.rule_generator import generate_test_cases
from generators.llm_generator import LLMGenerator
from core.features import extract_features

from core.executor import APIExecutor
from core.oracle import TestOracle
from core.step_generator import generate_steps
from exporter import export_to_excel
from core.optimizer import greedy_set_cover_safe

API_URL = "http://103.189.208.131:54333/Admin/Order/GetTotalOrder"


def main():

    session = requests.Session()
    executor = APIExecutor(session, API_URL)

    base = {
        "payment_type_id": 1,
        "to_name": "A",
        "to_phone": "0909",
        "to_address": "DN",
        "weight": 10
    }

    # ======================
    # GENERATE
    # ======================
    rule_cases = generate_test_cases(base)
    llm_cases = LLMGenerator().generate(base)

    all_cases = rule_cases + llm_cases

    enriched = []
    wrapped_objects = []

    # ======================
    # EXECUTE + ENRICH (PHẢI NẰM TRONG main)
    # ======================
    for c in all_cases:

        actual = executor.call(c["data"])
        features = extract_features(c["data"], actual)

        record = {
            "id": c["id"],
            "name": c["name"],
            "precondition": "Login required",
            "test_data": c["data"],
            "steps": " | ".join(generate_steps(c)),
            "expected": c["expected"],
            "actual": actual.get("status_code", ""),
            "priority": "Medium",
            "pass_fail": "",
            "status": "",
            "date": "27/04/2026",
            "features": features
        }

        enriched.append(record)

        wrapped_objects.append(type("W", (), {
            "id": c["id"],
            "features": features
        })())

    # ======================
    # OPTIMIZE
    # ======================
    selected_wrapped = greedy_set_cover_safe(wrapped_objects)

    selected_ids = set(x.id for x in selected_wrapped)

    selected = [x for x in enriched if x["id"] in selected_ids]

    # ======================
    # EXPORT
    # ======================
    export_to_excel(enriched, {}, selected)

    # ======================
    # OUTPUT
    # ======================
    print("\nTOTAL:", len(enriched))
    print("SELECTED:", len(selected))

    print("\n================ SELECTED TEST CASES ================\n")

    for tc in selected:
        print(tc["id"], "-", tc["name"])


if __name__ == "__main__":
    main()