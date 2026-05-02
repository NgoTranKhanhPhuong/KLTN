import requests

API_URL = "http://103.189.208.131:54333/Admin/Order/GetTotalOrder"

def call_real_api(session, data):

    try:
        res = session.post(API_URL, json=data, timeout=10)

        return {
            "status_code": res.status_code,
            "body": res.text,
            "headers": dict(res.headers)
        }

    except Exception as e:
        return {
            "status_code": None,
            "body": str(e),
            "headers": {}
        }