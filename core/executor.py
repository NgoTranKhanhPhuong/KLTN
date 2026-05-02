import requests
import json


class APIExecutor:

    def __init__(self, session, url):
        self.session = session
        self.url = url

    def call(self, data):

        try:
            res = self.session.post(
                self.url,
                json=data,
                timeout=10,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            )

            # =========================
            # SAFE JSON PARSING
            # =========================
            body = None
            content_type = res.headers.get("Content-Type", "")

            if "application/json" in content_type:
                try:
                    body = res.json()
                except:
                    body = {"raw": res.text}
            else:
                body = {"raw": res.text}

            return {
                "status_code": res.status_code,
                "body": body,
                "headers": dict(res.headers),
                "success": 200 <= res.status_code < 300
            }

        except requests.exceptions.Timeout:
            return {
                "status_code": 408,
                "body": {"error": "TIMEOUT"},
                "headers": {},
                "success": False
            }

        except requests.exceptions.ConnectionError:
            return {
                "status_code": 503,
                "body": {"error": "CONNECTION_ERROR"},
                "headers": {},
                "success": False
            }

        except Exception as e:
            return {
                "status_code": 500,
                "body": {"error": str(e)},
                "headers": {},
                "success": False
            }