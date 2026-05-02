from api_client import call_real_api
from core.oracle import TestOracle

class TestRunner:

    def __init__(self, session):
        self.session = session

    def run(self, test_case):

        response = call_real_api(self.session, test_case.data)

        test_case.actual = response

        test_case.passed = TestOracle.validate(test_case.data, response)

        return test_case